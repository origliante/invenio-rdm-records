# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Resources serializers tests."""

from os.path import dirname, join

import json, io

from datacite.schema43 import dump_etree, tostring, validate, validator


def test_datacite43_json_serializer(full_record):
    expected_data_file = 'data/datacite_43.json'
    expected_data = load_json_path(expected_data_file)
    validator.validate(expected_data)


def load_json_path(path):
    """Helper method for loading a JSON example file from a path."""
    path_base = dirname(__file__)
    with io.open(join(path_base, path), encoding='utf-8') as file:
        content = file.read()
    return json.loads(content)
