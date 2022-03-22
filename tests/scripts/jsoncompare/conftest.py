import pytest
from pytest_lazyfixture import lazy_fixture
import tarfile
import os
import json

ROOT_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../../../'


@pytest.fixture(params=[
    ('encounter-example-xcda.json', {'patient', 'resourceType'}),
    ('encounter-example-f203-20130311.json', {'patient', 'resourceType', '_class'})
])
def fixture_get_encounter_examples(request):
    return (json.load(open(ROOT_DIR + 'examples/input/' + request.param[0])), request.param[1])


######################
# Common DATA
######################


@pytest.fixture
def data__snapshot_element() -> dict:
    return \
        {
            "resourceType": "StructureDefinition",
            "snapshot": {
                "element": [
                    {
                        "id": "BasicTest",
                        "path": "This element and others not required"
                    },
                    {
                        "id": "BasicTest.id",
                        "other": "This key wouldn't exist"
                    },
                    {
                        "id": "BasicTest.id.3rdlevel"
                    }
                ]
            }
        }


@pytest.fixture
def data__snapshot_element_transformed_list() -> list:
    return [
        {
            "id": "BasicTest",
            "path": "This element and others not required"
        },
        {
            "id": "BasicTest.id",
            "other": "This key wouldn't exist"
        },
        {
            "id": "BasicTest.id.3rdlevel"
        }
    ]


@pytest.fixture(params=[
    lazy_fixture('data__input_empty'),
    {
        "resourceType": "StructureDefinition",
        "snapshot": {
            "notElement": "some other data"
        }
    }
])
def data__snapshot_element_empty(request) -> dict:
    return request.param


@pytest.fixture
def data__snapshot_element_choices() -> dict:
    return \
        {
            "id": "Communication.payload.content[x]",
            "type": [
                {
                    "code": "string"
                },
                {
                    "code": "Attachment"
                },
                {
                    "code": "Reference",
                    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Resource"
                }
            ]
        }


@pytest.fixture(params=[[], None])
def data__input_empty(request):
    return request.param


@pytest.fixture(params=[['noKey'], [], None])
def data__invalid_key(request):
    return request.param


@pytest.fixture(params=[
    (
            [{'valid': ['object', 'containing']}, {'lists': {'and': 'dicts'}}],
            {'valid': ['object', 'containing'], 'lists': {'and': 'dicts'}}
    ),
    (
            [{'object': ['containing', 'a', 'list']}],
            {'object': ['containing', 'a', 'list']}
    ),
    (
            [{'simpleString': 'object'}],
            {'simpleString': 'object'}
    ),
    (
            [{'integer': 123}],
            {'integer': 123}
    )
])
def data__list_contains_dict__input_and_output(request):
    return request.param


@pytest.fixture(params=[
    lazy_fixture('data__list_contains_dict__input_and_output'),
    ([[{'valid': ['object', 'containing']}], {'lists': {'and': 'dicts'}}], ['NOT_USED']),  # Not valid FHIR
])
def data__list_contains_dict(request):
    return request.param[0]


@pytest.fixture(params=[
    lazy_fixture('data__snapshot_element'),
    lazy_fixture('data__snapshot_element_choices'),
    lazy_fixture('data__list_contains_dict')
])
def data__contains_dict(request):
    return request.param


@pytest.fixture(params=[
    ['string array'],
    ['three', 'string', 'array']
    [1],
    [0, 1]
])
def data__does_not_contain_dict(request):
    return request.param

@pytest.fixture()
def fixture_get_encounter_source_dic():
    return {
        (): [
            'Encounter'
        ],
        ('Encounter',): [
         'id',
         'meta',
         'implicitRules',
         'language',
         'text',
         'contained',
         'extension',
         'modifierExtension',
         'identifier',
         'status',
         'statusHistory',
         'class',
         'classHistory',
         'type',
         'priority',
         'subject',
         'episodeOfCare',
         'incomingReferral',
         'participant',
         'appointment',
         'period',
         'length',
         'reason',
         'diagnosis',
         'account',
         'hospitalization',
         'location',
         'serviceProvider',
         'partOf'
        ],
        ('Encounter', 'statusHistory'): [
            'id',
            'extension',
            'modifierExtension',
            'status',
            'period'
        ],
        ('Encounter', 'classHistory'): [
            'id',
            'extension',
            'modifierExtension',
            'class',
            'period'
        ],
        ('Encounter', 'participant'): [
            'id',
            'extension',
            'modifierExtension',
            'type',
            'period',
            'individual'
        ],
        ('Encounter', 'diagnosis'): [
            'id',
            'extension',
            'modifierExtension',
            'condition',
            'role',
            'rank'
        ],
        ('Encounter', 'hospitalization'): [
            'id',
            'extension',
            'modifierExtension',
            'preAdmissionIdentifier',
            'origin',
            'admitSource',
            'reAdmission',
            'dietPreference',
            'specialCourtesy',
            'specialArrangement',
            'destination',
            'dischargeDisposition'
        ],
        ('Encounter', 'location'): [
            'id',
            'extension',
            'modifierExtension',
            'location',
            'status',
            'period'
        ]}
