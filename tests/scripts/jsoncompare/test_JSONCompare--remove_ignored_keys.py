from unittest import TestCase

import pytest
from scripts.lib.documentcompare import JSONCompare

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


def test__remove_ignored_keys__key_exists(data__snapshot_element):
    output_data = JSONCompare()._remove_ignored_keys(data__snapshot_element, ['snapshot'])
    expected_data = {"resourceType": "StructureDefinition"}
    assert output_data == expected_data


def test__remove_ignored_keys__invalid_key(data__snapshot_element, invalid_key):
    output_data = JSONCompare()._remove_ignored_keys(data__snapshot_element, invalid_key)
    expected_data = data__snapshot_element
    assert output_data == expected_data


def test__remove_ignored_keys__invalid_params(input_empty, invalid_key):
    output_data = JSONCompare()._remove_ignored_keys(input_empty, invalid_key)
    expected_data = []
    assert output_data == expected_data


######################
# TESTS - End
######################
