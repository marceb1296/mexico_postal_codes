from typing import List
import zipfile
import requests as r
import xlrd
import io
import logging
import functools
import re
from django.db import transaction


from core.models import LastModifyModel
from postal_codes.models import PostalCode

# Create your views here.


logger = logging.getLogger(__name__)


def exception_decorator(str_err: str):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper_decorator(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                logger.error(str_err % str(
                    e), exc_info=True)
                exit(1)
        return wrapper_decorator
    return decorator


class PostalCodeHandler:

    """
    Main class to download, parse and save postal codes into model
    """

    def __init__(self) -> None:

        self.body = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "__VIEWSTATE": "/wEPDwUINzcwOTQyOTgPZBYCAgEPZBYCAgEPZBYGAgMPDxYCHgRUZXh0BTjDmmx0aW1hIEFjdHVhbGl6YWNpw7NuIGRlIEluZm9ybWFjacOzbjogTWFyem8gMTkgZGUgMjAyNGRkAgcPEA8WBh4NRGF0YVRleHRGaWVsZAUDRWRvHg5EYXRhVmFsdWVGaWVsZAUFSWRFZG8eC18hRGF0YUJvdW5kZ2QQFSEjLS0tLS0tLS0tLSBUICBvICBkICBvICBzIC0tLS0tLS0tLS0OQWd1YXNjYWxpZW50ZXMPQmFqYSBDYWxpZm9ybmlhE0JhamEgQ2FsaWZvcm5pYSBTdXIIQ2FtcGVjaGUUQ29haHVpbGEgZGUgWmFyYWdvemEGQ29saW1hB0NoaWFwYXMJQ2hpaHVhaHVhEUNpdWRhZCBkZSBNw6l4aWNvB0R1cmFuZ28KR3VhbmFqdWF0bwhHdWVycmVybwdIaWRhbGdvB0phbGlzY28HTcOpeGljbxRNaWNob2Fjw6FuIGRlIE9jYW1wbwdNb3JlbG9zB05heWFyaXQLTnVldm8gTGXDs24GT2F4YWNhBlB1ZWJsYQpRdWVyw6l0YXJvDFF1aW50YW5hIFJvbxBTYW4gTHVpcyBQb3Rvc8OtB1NpbmFsb2EGU29ub3JhB1RhYmFzY28KVGFtYXVsaXBhcwhUbGF4Y2FsYR9WZXJhY3J1eiBkZSBJZ25hY2lvIGRlIGxhIExsYXZlCFl1Y2F0w6FuCVphY2F0ZWNhcxUhAjAwAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyAjEzAjE0AjE1AjE2AjE3AjE4AjE5AjIwAjIxAjIyAjIzAjI0AjI1AjI2AjI3AjI4AjI5AjMwAjMxAjMyFCsDIWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAh0PPCsACwBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtidG5EZXNjYXJnYYucF9pvIFrjPF64652VQ9+m5LKC",
            "__VIEWSTATEGENERATOR": "BE1A6D2E",
            "__EVENTVALIDATION": "/wEWKAL5mO3yBQLG/OLvBgLWk4iCCgLWk4SCCgLWk4CCCgLWk7yCCgLWk7iCCgLWk7SCCgLWk7CCCgLWk6yCCgLWk+iBCgLWk+SBCgLJk4iCCgLJk4SCCgLJk4CCCgLJk7yCCgLJk7iCCgLJk7SCCgLJk7CCCgLJk6yCCgLJk+iBCgLJk+SBCgLIk4iCCgLIk4SCCgLIk4CCCgLIk7yCCgLIk7iCCgLIk7SCCgLIk7CCCgLIk6yCCgLIk+iBCgLIk+SBCgLLk4iCCgLLk4SCCgLLk4CCCgLL+uTWBALa4Za4AgK+qOyRAQLI56b6CwL1/KjtBYbqVyjwpbbGy/2H8eqgVHc4byIw",
            "cboEdo": "00",
            "rblTipo": "xls",
            "btnDescarga.x": "0",
            "btnDescarga.y": "9",
        }
        self.url = "https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx"

    def manage(self):
        last_modify, exists = self.verify_last_update

        if exists:
            return True

        elif not exists and last_modify:
            _, created = self.create_first_update(last_modify)

            data = self.handle_data

            if created:
                self.save_to_model(data)
            else:
                self.bulk_update_postal_codes(data)

        return False

    @property
    def handle_data(self):
        zip = self.download_xls_zip_file
        return self.unzip_and_parse_xls_file(zip)

    def create_first_update(self, last_modify):
        return LastModifyModel.objects.update_or_create(identifier=1, defaults={"last_modify": last_modify})

    @property
    @exception_decorator("Couldn't fetch url from 'Servicio Postal Mexicano' url, Exception: %s")
    def fetch_last_update(self):
        response = r.get(self.url).text

        last_modify = re.search(
            r'<span id="lblfec" class="lblback">[\w\s]+:\s(.*)</span>', response)

        return last_modify.group(1)

    @property
    def verify_last_update(self):

        last_update = self.fetch_last_update

        # using identifier to have only one record; based on this, instead of creating and deleting, just update it
        return last_update, LastModifyModel.objects.filter(last_modify=last_update).exists()

    @property
    @exception_decorator("Couldn't fetch file from 'Servicio Postal Mexicano' url, Exception: %s")
    def download_xls_zip_file(self):

        return r.post(self.url, data=self.body).content

    @exception_decorator("Couldn't parse data from zip file, Exception: %s")
    def unzip_and_parse_xls_file(self, zip_file: bytes):

        data = []

        with zipfile.ZipFile(io.BytesIO(zip_file)) as File:
            with File.open('CPdescarga.xls') as xls_buffer:
                with xlrd.open_workbook(file_contents=xls_buffer.read(), on_demand=True) as wb:
                    for _ws in wb.sheet_names()[1:]:

                        ws = wb.sheet_by_name(_ws)

                        columns = [ws.cell_value(0, col)
                                   for col in range(ws.ncols)]

                        for row in range(1, ws.nrows):
                            data.append({
                                columns[col]: ws.cell_value(row, col).strip() if isinstance(
                                    ws.cell_value(row, col), str) else ws.cell_value(row, col)
                                for col in range(ws.ncols)
                            })

        return data

    @exception_decorator("Couldn't save objects to model PostalCode, Exception: %s")
    def save_to_model(self, data: list):

        PostalCode.objects.bulk_create(
            [PostalCode(**obj) for obj in data])

    @transaction.atomic
    def bulk_update_postal_codes(self, data):
        """
        Iterates over a new instance of data.
        Searches for records in the PostalCode model using specific criteria to identify unique entries.
        If a matching record is found, verifies if specified fields have been modified and updates them if necessary.
        If no matching record is found, creates a new one.
        """

        skiped_fields = [
            "d_codigo",
            "D_mnpio",
            "id_asenta_cpcons"
        ]

        for record in data:

            unique_fileds = {
                key: value for key, value in record.items() if key in skiped_fields
            }

            instance = PostalCode.objects.filter(**unique_fileds)

            if instance.exists():
                _instance = instance.first()
                update_fields = []

                for field in _instance._meta.fields:
                    if field.name == 'id' or field.name in skiped_fields:
                        continue

                    if getattr(_instance, field.name, None) != record.get(field.name):
                        update_fields.append(field.name)
                        setattr(_instance, field.name, record.get(field.name))

                if update_fields:
                    _instance.save(update_fields=update_fields)
            else:
                PostalCode.objects.create(**record)
