# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Contributor Role Vocabulary."""

import csv
from collections import OrderedDict

from flask_babelex import lazy_gettext as _

from .utils import hierarchized_rows


class ContributorRoleVocabulary(object):
    """Encapsulates all contributor role vocabulary data."""

    def __init__(self, path):
        """Constructor."""
        self.path = path
        self._load_data()

    def key(self, row):
        """Returns the primary key of the row.

        row: dict-like
        returns: serializable
        """
        return row.get('role')

    def _load_data(self):
        """Sets self.data with the filled rows."""
        with open(self.path) as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            # NOTE: We use an OrderedDict to preserve on file row order
            self.data = OrderedDict([
                # NOTE: unfilled cells return '' (empty string)
                (self.key(row), row)
                for row in hierarchized_rows(reader)
            ])

    def get_entry_by_dict(self, dict_key):
        """Returns a vocabulary entry as an OrderedDict."""
        return self.data.get(self.key(dict_key))

    def get_title_by_dict(self, dict_key):
        """Returns a vocabulary entry title."""
        entry = self.get_entry_by_dict(dict_key)

        # NOTE: translations could also be done via the CSV file directly
        return _(entry.get('role_name'))

    def get_invalid(self, dict_key):
        """Returns the error message for the given dict key."""
        # TODO: Revisit with deposit to return targeted error message
        choices = set(self.data.keys())
        _input = self.key(dict_key)

        return _('Invalid role. {input} not one of {choices}.'.format(
            input=_input,
            choices=choices
        ))

    def dump_options(self):
        """Returns json-compatible dict of options for roles.

        The current shape is influenced by current frontend, but it's flexible
        enough to withstand the test of time (new frontend would be able to
        adapt it to their needs easily).

        TODO: Be attentive to generalization for all vocabularies.
        """
        options = [
            {
                'icon': '',
                'text': _(entry.get('role_name')),
                'value': key
            }
            for key, entry in self.data.items()
        ]

        return options
