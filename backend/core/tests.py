from django.test import TestCase
from core.handler import PostalCodeHandler
from core.models import LastModifyModel
from postal_codes.models import PostalCode


# region const for tests

test_first_update = "Some str date"
test_second_update = "Some str date updated"
test_third_update = "Some str date updated 1"


test_first_data = [
    {'d_codigo': '20124', 'd_asenta': 'Galerías', 'd_tipo_asenta': 'Zona comercial', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '33', 'c_mnpio': '001', 'id_asenta_cpcons': '1173', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20124', 'd_asenta': 'Residencial Altaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '1373', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Constitución', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0090', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Libertad', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0091', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Pozo Bravo Norte', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0092', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Soberana Convención Revolucionaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0094', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
]

# Change fields d_asenta and c_oficina in third element to simulate data updated
test_second_data = [
    {'d_codigo': '20124', 'd_asenta': 'Galerías', 'd_tipo_asenta': 'Zona comercial', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '33', 'c_mnpio': '001', 'id_asenta_cpcons': '1173', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20124', 'd_asenta': 'Residencial Altaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '1373', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Constitución 23', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20002', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0090', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Libertad', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0091', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Pozo Bravo Norte', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0092', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Soberana Convención Revolucionaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0094', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
]

# Add new record, slicing the second element
test_third_data = [
    {'d_codigo': '20124', 'd_asenta': 'Galerías', 'd_tipo_asenta': 'Zona comercial', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '33', 'c_mnpio': '001', 'id_asenta_cpcons': '1173', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20124', 'd_asenta': 'new asenta', 'd_tipo_asenta': 'Zona comercial', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '33', 'c_mnpio': '001', 'id_asenta_cpcons': '1273', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20124', 'd_asenta': 'Residencial Altaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '1373', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Constitución 23', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20002', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0090', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Libertad', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0091', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Pozo Bravo Norte', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0092', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
    {'d_codigo': '20126', 'd_asenta': 'Soberana Convención Revolucionaria', 'd_tipo_asenta': 'Fraccionamiento', 'D_mnpio': 'Aguascalientes', 'd_estado': 'Aguascalientes', 'd_ciudad': 'Aguascalientes',
        'd_CP': '20001', 'c_estado': '01', 'c_oficina': '20001', 'c_CP': '', 'c_tipo_asenta': '21', 'c_mnpio': '001', 'id_asenta_cpcons': '0094', 'd_zona': 'Urbano', 'c_cve_ciudad': '01'},
]


test_unique_fields = [
    {'d_codigo': '20124',
        'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '1373'},
    {'d_codigo': '20126',
        'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '0090'},
    {'d_codigo': '20126',
        'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '0092'},
]

test_unique_prev_updated_fields = {'d_codigo': '20126', 'd_asenta': 'Constitución',
                                   'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '0090'}

test_unique_updated_fields = {'d_codigo': '20126', 'd_asenta': 'Constitución 23',
                              'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '0090'}

test_unique_new_field = {'d_codigo': '20124', 'd_asenta': 'new asenta',
                         'D_mnpio': 'Aguascalientes', 'id_asenta_cpcons': '1273', }


# endregion


# region PostalCode for tests


class PostalCodeHandlerForFirstTest(PostalCodeHandler):

    @property
    def fetch_last_update(self):
        return test_first_update

    @property
    def handle_data(self):
        return test_first_data


class PostalCodeHandlerForSecondTest(PostalCodeHandler):

    @property
    def fetch_last_update(self):
        return test_second_update

    @property
    def handle_data(self):
        return test_second_data


class PostalCodeHandlerForThirdTest(PostalCodeHandler):

    @property
    def fetch_last_update(self):
        return test_third_update

    @property
    def handle_data(self):
        return test_third_data


# endregion


class HandlerFirstTestA(TestCase):

    def test_should_fetch_and_save_data_into_model(self):

        postal_code = PostalCodeHandlerForFirstTest().manage()
        self.assertEqual(postal_code, False)

        for record in test_unique_fields:
            self.assertEqual(PostalCode.objects.filter(
                **record).exists(), True)

        last_modify = LastModifyModel.objects.filter(
            pk=1, last_modify=test_first_update)

        self.assertEqual(last_modify.exists(), True)


class HandlerFirstTestB(TestCase):

    def setUp(cls) -> None:

        PostalCodeHandlerForFirstTest().manage()

    def test_manage_should_return_false_because_last_update_dont_change_and_data_is_the_same(self):
        # before
        last_modify = LastModifyModel.objects.filter(
            pk=1, last_modify=test_first_update)

        self.assertEqual(last_modify.exists(), True)

        # after
        PostalCodeHandlerForFirstTest().manage()

        postal_code = PostalCodeHandlerForFirstTest().manage()
        self.assertEqual(postal_code, True)


class HandlerSecondTestA(TestCase):

    def setUp(self) -> None:

        PostalCodeHandlerForFirstTest().manage()

    def test_manage_should_return_false_and_last_modify_model_should_be_updated(self):
        # before
        instance_prev_updated = PostalCode.objects.filter(
            **test_unique_prev_updated_fields).exists()

        self.assertEqual(instance_prev_updated, True)

        last_modify = LastModifyModel.objects.filter(
            pk=1, last_modify=test_first_update)

        self.assertEqual(last_modify.exists(), True)

        # after
        postal_code = PostalCodeHandlerForSecondTest().manage()
        self.assertEqual(postal_code, False)

        last_modify = LastModifyModel.objects.filter(
            pk=1, last_modify=test_first_update)

        self.assertEqual(last_modify.exists(), False)

        last_modify = LastModifyModel.objects.filter(
            pk=1, last_modify=test_second_update)

        self.assertEqual(last_modify.exists(), True)

    def test_postal_code_instances_should_be_updated(self):
        # before
        prev_instance = PostalCode.objects.filter(
            **test_unique_prev_updated_fields)
        self.assertEqual(prev_instance.exists(), True)

        # after
        PostalCodeHandlerForSecondTest().manage()

        with self.assertRaises(PostalCode.DoesNotExist):
            PostalCode.objects.get(**test_unique_prev_updated_fields)

        instance_updated = PostalCode.objects.filter(
            **test_unique_updated_fields).exists()

        self.assertEqual(instance_updated, True)


class HandlerThirdTestA(TestCase):

    def setUp(self) -> None:
        PostalCodeHandlerForSecondTest().manage()

    def test_should_not_have_new_record(self):

        with self.assertRaises(PostalCode.DoesNotExist):
            PostalCode.objects.get(**test_unique_new_field)

    def test_should_insert_new_instance(self):

        PostalCodeHandlerForThirdTest().manage()

        new_instance = PostalCode.objects.filter(**test_unique_new_field)

        self.assertEqual(new_instance.exists(), True)
