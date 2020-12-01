# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

from flask_resources.serializers import JSONSerializer, SerializerMixin

from datacite import schema43


class DataCite43Serializer(JSONSerializer):
    def serialize_object(self, obj):
        obj['metadata'] = self.transform(obj['metadata'])
        return obj

    def serialize_object_list(self, obj_list):
        o_l = []
        for obj in obj_list:
            o_l.append(self.serialize_object(obj))
        return o_l

    def transform(self, record):
        transformed = {}
        for k in record.keys():
            try:
                t = getattr(self, k)
                n_k, v = t(record[k])
                transformed[n_k] = v
            except AttributeError:
                pass
        return transformed

    def resource_type(self, field):
        t_field = {}
        if field['type'] == 'publication':
            t_field = {
                "resourceTypeGeneral": "Text",
                "resourceType": field['subtype'],
            }
        elif field['type'] == 'video':
            t_field = {
                "resourceTypeGeneral": "Video",
                # "resourceType": field['subtype'],
            }
        return 'types', t_field
