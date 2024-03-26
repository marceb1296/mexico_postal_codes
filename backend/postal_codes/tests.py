import math
from typing import Any, Optional, Type
from django.test import TestCase
from core.handler import PostalCodeHandler
from rest_framework.test import APIClient

# Create your tests here.

# region Data test

# data len = 20
data_test = [
    {
        "d_codigo": "20000",
        "d_asenta": "Aguascalientes Centro",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0001",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20010",
        "d_asenta": "Colinas del Rio",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0005",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20010",
        "d_asenta": "Olivares Santana",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0006",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20010",
        "d_asenta": "Las Brisas",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0007",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20010",
        "d_asenta": "Ramon Romo Franco",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0008",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20010",
        "d_asenta": "San Cayetano",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0009",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20016",
        "d_asenta": "Colinas de San Ignacio",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0010",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20016",
        "d_asenta": "La Fundición",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0011",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20016",
        "d_asenta": "Fundición II",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0012",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20016",
        "d_asenta": "Los Sauces",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0013",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20018",
        "d_asenta": "Línea de Fuego",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0014",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20020",
        "d_asenta": "Buenos Aires",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0016",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20020",
        "d_asenta": "Circunvalación Norte",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0018",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20020",
        "d_asenta": "Las Arboledas",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0019",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20020",
        "d_asenta": "Villas de San Francisco",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0020",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20029",
        "d_asenta": "Villas de La Universidad",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0021",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20030",
        "d_asenta": "El Sol",
        "d_tipo_asenta": "Fraccionamiento",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "21",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0022",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20030",
        "d_asenta": "Gremial",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0023",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20030",
        "d_asenta": "Industrial",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0024",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    },
    {
        "d_codigo": "20040",
        "d_asenta": "Altavista",
        "d_tipo_asenta": "Colonia",
        "D_mnpio": "Aguascalientes",
        "d_estado": "Aguascalientes",
        "d_ciudad": "Aguascalientes",
        "d_CP": "20001",
        "c_estado": "01",
        "c_oficina": "20001",
        "c_CP": "",
        "c_tipo_asenta": "09",
        "c_mnpio": "001",
        "id_asenta_cpcons": "0026",
        "d_zona": "Urbano",
        "c_cve_ciudad": "01"
    }
]


test_first_update = "Some str date"


total_fields = [
    "d_codigo",
    "d_asenta",
    "d_tipo_asenta",
    "D_mnpio",
    "d_estado",
    "d_ciudad",
    "d_CP",
    "c_estado",
    "c_oficina",
    "c_CP",
    "c_tipo_asenta",
    "c_mnpio",
    "id_asenta_cpcons",
    "d_zona",
    "c_cve_ciudad",
]


class PostalCodeHandlerTest(PostalCodeHandler):

    @property
    def fetch_last_update(self):
        return test_first_update

    @property
    def handle_data(self):
        return data_test


# endregion


class ApiPaginationTest(TestCase):

    @classmethod
    def setUpClass(cls):
        PostalCodeHandlerTest().manage()
        cls.api_client = APIClient()
        return super().setUpClass()

    def client_get_json(self, query_params: str = ""):

        return self.api_client.get("/v1%s" % query_params, format="json", headers={
            "Content-Type": "application/json"
        })

    def test_request_status_code_should_be_200(self):
        request = self.client_get_json()
        self.assertEqual(request.status_code, 200)

    def test_request_count_should_match_with_total_data_test_len(self):
        request = self.client_get_json()

        count = request.json().get("count")
        self.assertEqual(count, len(data_test))

    def test_request_results_should_match_with_default_10_page_size(self):
        request = self.client_get_json()

        results = request.json().get("results")
        self.assertEqual(len(results), 10)

    def test_request_results_should_match_with_page_size_query_param_and_total_page(self):

        data_len = len(data_test)
        page_size = 5

        request = self.client_get_json("?page_size=%s" % page_size)

        results = request.json().get("results")
        total_pages = request.json().get("total_pages")

        self.assertEqual(len(results), page_size)
        self.assertEqual(total_pages, math.ceil(data_len / page_size))

    def test_request_result_should_has_all_model_fields(self):

        request = self.client_get_json()

        results = request.json().get("results")

        self.assertEqual(
            all([key in total_fields for key in results[0].keys()]), True)

    def test_request_should_have_only_fields_sended_into_query_params(self):

        only_fields = [
            "d_codigo",
            "d_asenta",
            "d_tipo_asenta",
        ]

        # only as simple str
        request = self.client_get_json("?only=%s" % ",".join(only_fields))

        results = request.json().get("results")

        self.assertEqual(
            all([key in results[0].keys() for key in total_fields]), False)

        self.assertEqual(
            all([key in results[0].keys() for key in only_fields]), True)

        # only as str list
        request = self.client_get_json("?only=[%s]" % ",".join(only_fields))

        results = request.json().get("results")

        self.assertEqual(
            all([key in results[0].keys() for key in total_fields]), False)

        self.assertEqual(
            all([key in results[0].keys() for key in only_fields]), True)

    def test_request_should_not_have_exclude_fields_sended_into_query_params(self):

        exclude_fields = [
            "d_codigo",
            "d_asenta",
            "d_tipo_asenta",
        ]

        # exclude as simple str
        request = self.client_get_json(
            "?exclude=%s" % ",".join(exclude_fields))

        results = request.json().get("results")

        self.assertEqual(
            all([key not in results[0].keys() for key in total_fields]), False)

        self.assertEqual(
            all([key not in results[0].keys() for key in exclude_fields]), True)

        # # exclude as str list
        request = self.client_get_json(
            "?exclude=[%s]" % ",".join(exclude_fields))

        results = request.json().get("results")

        self.assertEqual(
            all([key not in results[0].keys() for key in total_fields]), False)

        self.assertEqual(
            all([key not in results[0].keys() for key in exclude_fields]), True)

    def test_exclude_and_only_interaction(self):
        """
        If "exclude" and "only" are both present in query_params,
        and they share common fields, the fields specified in "only" will be ignored.
        """
        common_field = "d_codigo"

        exclude_fields = [
            "d_codigo",
            "d_asenta",
            "d_tipo_asenta",
        ]

        only_fields = [
            "d_codigo",

        ]

        # exclude as simple str
        request = self.client_get_json(
            "?exclude=%s&only=%s" % (",".join(exclude_fields), ",".join(only_fields)))

        results = request.json().get("results")

        self.assertEqual(
            common_field in results[0].keys(), False)

    def test_request_should_return_all_data_when_filtering_d_codigo_within_200(self):
        # All 'd_codigo' values in 'data_test' begin with '200', so filtering 'd_codigo' within '200' will return all entries in 'data_test'.

        request = self.client_get_json("?d_codigo=200")

        count = request.json().get("count")
        self.assertEqual(count, len(data_test))

    def test_request_should_return_10_records_when_filtering_d_codigo_within_2001(self):
        # There are 10 records in 'data_test' that begin with 2001

        request = self.client_get_json("?d_codigo=2001")

        count = request.json().get("count")
        self.assertEqual(count, 10)

    def test_request_should_return_1_record(self):

        request = self.client_get_json("?d_codigo=2001&id_asenta_cpcons=0005")

        count = request.json().get("count")
        self.assertEqual(count, 1)
