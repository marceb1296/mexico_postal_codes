import json
from rest_framework import serializers

from .models import PostalCode


class PostalCodeSerializer(serializers.ModelSerializer):

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance, data, **kwargs)

        query_params = self.context.get("request").query_params

        if "exclude" in query_params:
            exclude = query_params.get("exclude")

            # in case user send a str list
            exclude = exclude.replace("[", "").replace("]", "")
            if exclude:

                self.fields = {
                    key: value for key, value in self.fields.items() if key not in exclude.split(",")
                }

        if "only" in query_params:
            only = query_params.get("only")

            # in case user send a str list
            only = only.replace("[", "").replace("]", "")
            if only:

                self.fields = {
                    key: value for key, value in self.fields.items() if key in only.split(",")
                }

    class Meta:
        model = PostalCode
        fields = [
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
