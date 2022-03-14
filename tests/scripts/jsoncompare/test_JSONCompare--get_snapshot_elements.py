from unittest import TestCase

import pytest, os
from scripts.lib.documentcompare import JSONCompare

#@pytest.fixture
#def change_test_dir(request):
#    #os.chdir(request.fspath.dirname)
#    os.chdir('/home/debian11/Documents/hapi-fhir-3to4-demo/scripts')
#    yield
#    #os.chdir(request.config.invocation_dir)
#    os.chdir('/home/debian11/Documents/hapi-fhir-3to4-demo/tests/scripts/jsoncompare')

######################
# DATA - Start
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
def data__snapshot_element_empty() -> dict:
    return \
        {
            "resourceType": "StructureDefinition",
            "snapshot": {
                "notElement": "some other data"
            }
        }


@pytest.fixture(params=[data__snapshot_element_empty, [], None])
def data__get_snapshot_elements__empty(request):
    return request.param


@pytest.fixture(params=[[], None])
def input_empty(request):
    return request.param


@pytest.fixture(params=[['noKey'], [], None])
def invalid_key(request):
    return request.param


######################
# DATA - End
######################


######################
# TESTS - Start
######################


def test__get_snapshot_elements__element_exists(data__snapshot_element):
    #change_test_dir
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element)
    expected_data = [
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
    assert output_data == expected_data


def test__get_snapshot_elements__element_empty(data__snapshot_element_empty):
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element_empty)
    expected_data = []
    assert output_data == expected_data


def test__get_snapshot_elements__empty_input(input_empty):
    output_data = JSONCompare()._get_snapshot_elements(input_empty)
    expected_data = []
    assert output_data == expected_data


######################
# TESTS - End
######################
