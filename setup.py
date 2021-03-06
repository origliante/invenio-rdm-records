# -*- coding: utf-8 -*-
#
# Copyright (C) 2019-2020 CERN.
# Copyright (C) 2019-2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""DataCite-based data model for Invenio."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'pytest-invenio>=1.4.0,<2.0.0',
    'invenio-app>=1.3.0,<2.0.0'
]

# Should follow inveniosoftware/invenio versions
invenio_db_version = '>=1.0.4,<2.0.0'
invenio_search_version = '>=1.4.0,<2.0.0'

extras_require = {
    'docs': [
        'Sphinx>=3',
    ],
    # Elasticsearch version
    'elasticsearch6': [
        'invenio-search[elasticsearch6]{}'.format(invenio_search_version),
    ],
    'elasticsearch7': [
        'invenio-search[elasticsearch7]{}'.format(invenio_search_version),
    ],
    # Databases
    'mysql': [
        'invenio-db[mysql,versioning]{}'.format(invenio_db_version),
    ],
    'postgresql': [
        'invenio-db[postgresql,versioning]{}'.format(invenio_db_version),
    ],
    'sqlite': [
        'invenio-db[versioning]{}'.format(invenio_db_version),
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name[0] == ':' or name in ('elasticsearch6', 'elasticsearch7',
                                  'mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

install_requires = [
    'arrow>=0.17.0',
    'CairoSVG>=1.0.20',
    'Faker>=2.0.3',
    'ftfy>=4.4.3,<5.0.0',
    'idutils>=1.1.7',
    'invenio-assets>=1.2.2,<1.3.0',
    'invenio-communities>=2.1.1,<3.0.0',
    'invenio-drafts-resources>=0.5.0,<0.6.0',
    'invenio-formatter[badges]>=1.1.0a1,<2.0.0',
    'invenio-i18n>=1.2.0',
    'invenio-records>=1.4.0a4,<2.0.0',
    'invenio-records-files>=1.2.1,<2.0.0',
    'invenio-records-ui>=1.2.0a1,<2.0.0',
    'invenio-previewer>=1.2.1,<2.0.0',
    # until fix in invenio-previewer is released
    'nbconvert[execute]>=4.1.0,<6.0.0',
    'pytz>=2020.4',
    # TODO: Get from invenio-base
    'six>=1.12.0'  # Needed to pass CI tests
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_rdm_records', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-rdm-records',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio data model',
    license='MIT',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-rdm-records',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'flask.commands': [
            'rdm-records = invenio_rdm_records.cli:rdm_records',
        ],
        'invenio_assets.webpack': [
            'invenio_rdm_records_theme = invenio_rdm_records.theme.webpack:theme',
        ],
        'invenio_base.apps': [
            'invenio_rdm_records = invenio_rdm_records:InvenioRDMRecords',
        ],
        'invenio_base.api_apps': [
            'invenio_rdm_records = invenio_rdm_records:InvenioRDMRecords',
        ],
        'invenio_base.blueprints': [
            'invenio_rdm_records = invenio_rdm_records.theme.views:blueprint',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_rdm_records',
        ],
        'invenio_jsonschemas.schemas': [
            'invenio_rdm_records = invenio_rdm_records.records.jsonschemas',
        ],
        'invenio_search.mappings': [
            'rdmrecords = invenio_rdm_records.records.mappings',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
