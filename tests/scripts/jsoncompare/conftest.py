import pytest

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
    pytest.lazy_fixture('data__input_empty'),
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
    pytest.lazy_fixture('data__snapshot_element'),
    pytest.lazy_fixture('data__snapshot_element_choices'),
    [{'valid': ['object', 'containing']}, {'lists': {'and': 'dicts'}}],
    [{'object': ['containing', 'a', 'list']}],
    [{'simpleString': 'object'}],
    [{'integer': 123}],
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
