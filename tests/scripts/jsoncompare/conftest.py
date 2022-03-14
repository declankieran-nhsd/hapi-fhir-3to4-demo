import pytest
import os

# Change dir to location of code
@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname + '/../../../scripts')

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


@pytest.fixture
def data__snapshot_element_empty() -> dict:
    return \
        {
            "resourceType": "StructureDefinition",
            "snapshot": {
                "notElement": "some other data"
            }
        }


@pytest.fixture(params=[[], None])
def data__input_empty(request):
    return request.param


@pytest.fixture(params=[['noKey'], [], None])
def data__invalid_key(request):
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

