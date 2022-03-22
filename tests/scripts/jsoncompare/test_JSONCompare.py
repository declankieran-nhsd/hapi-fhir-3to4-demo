import pytest
from _pytest import monkeypatch
from unittest.mock import Mock

from scripts.lib.documentcompare import JSONCompare


# Test _remove_ignored_keys
def test__remove_ignored_keys__key_exists(data__snapshot_element):
    output_data = JSONCompare()._remove_ignored_keys(data__snapshot_element, ['snapshot'])
    expected_data = {"resourceType": "StructureDefinition"}
    assert output_data == expected_data


def test__remove_ignored_keys__invalid_key(data__snapshot_element, data__invalid_key):
    output_data = JSONCompare()._remove_ignored_keys(data__snapshot_element, data__invalid_key)
    expected_data = data__snapshot_element
    assert output_data == expected_data


def test__remove_ignored_keys__invalid_params(data__input_empty, data__invalid_key):
    output_data = JSONCompare()._remove_ignored_keys(data__input_empty, data__invalid_key)
    expected_data = []
    assert output_data == expected_data


# Test _get_snapshot_elements
def test__get_snapshot_elements__element_exists(data__snapshot_element, data__snapshot_element_transformed_list):
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element)
    expected_data = data__snapshot_element_transformed_list
    assert output_data == expected_data


def test__get_snapshot_elements__element_empty(data__snapshot_element_empty):
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element_empty)
    expected_data = []
    assert output_data == expected_data


# Test _extract_choice_types
def test__extract_choice_types__valid_input(data__snapshot_element_choices):
    output_data = JSONCompare()._extract_choice_types(data__snapshot_element_choices)
    expected_data = [
        ['Communication', 'payload', 'contentString'],
        ['Communication', 'payload', 'contentAttachment'],
        ['Communication', 'payload', 'contentReference']
    ]
    assert output_data == expected_data


def test__extract_choice_types__invalid_input(data__input_empty):
    output_data = JSONCompare()._extract_choice_types(data__input_empty)
    expected_data = []
    assert output_data == expected_data


# Test _transform_element_list
def test__transform_element_list__valid_input(data__snapshot_element_transformed_list):
    output_data = JSONCompare()._transform_element_list(data__snapshot_element_transformed_list)
    expected_data = {
        (): ['BasicTest'],
        ('BasicTest',): ['id'],
        ('BasicTest', 'id'): ['3rdlevel']
    }
    assert output_data == expected_data


def test__transform_element_list__empty_input(data__input_empty):
    output_data = JSONCompare()._transform_element_list(data__input_empty)
    expected_data = {}
    assert output_data == expected_data


# Test _is_or_contains_dict
def test__is_or_contains_dict__contains_or_is_dict(data__contains_dict):
    output_data = JSONCompare()._is_or_contains_dict(data__contains_dict)
    expected_data = True
    assert output_data == expected_data


def test__is_or_contains_dict__no_dict(data__does_not_contain_dict):
    output_data = JSONCompare()._is_or_contains_dict(data__does_not_contain_dict)
    expected_data = False
    assert output_data == expected_data


def test__is_or_contains_dict__empty_input(data__input_empty):
    output_data = JSONCompare()._is_or_contains_dict(data__input_empty)
    expected_data = False
    assert output_data == expected_data


#Test _get_dict_from_list
def test__get_dict_from_list__contains_a_dict(data__list_contains_dict):
    output_data = JSONCompare()._search_list_for_dict(data__list_contains_dict)
    expected_data = True
    assert output_data == expected_data


def test__get_dict_from_list__does_not_contain_a_dict(data__does_not_contain_dict):
    output_data = JSONCompare()._search_list_for_dict(data__does_not_contain_dict)
    expected_data = False
    assert output_data == expected_data


def test__get_dict_from_list__empty_input(data__input_empty):
    output_data = JSONCompare()._search_list_for_dict(data__input_empty)
    expected_data = False
    assert output_data == expected_data


#Test _strip_list
def test__strip_list__list_contains_dict(data__list_contains_dict__input_and_output):
    output_data = JSONCompare()._strip_list(data__list_contains_dict__input_and_output[0])
    expected_data = data__list_contains_dict__input_and_output[1]
    assert output_data == expected_data


def test__strip_list__empty_input(data__input_empty):
    output_data = JSONCompare()._strip_list(data__input_empty)
    expected_data = {}
    assert output_data == expected_data


#Test _get_invalid_keys

def test__get_invalid_keys__valid(fixture_get_encounter_examples, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_invalid_keys(('Encounter',), fixture_get_encounter_examples[0], fixture_get_encounter_source_dic)
    expected_data = fixture_get_encounter_examples[1]
    assert output_data == expected_data


#def test__get_invalid_keys__strip_list_called(mocker):
#    mocked_fn = mocker.patch('JSONCompare._strip_list')
#    JSONCompare()._get_invalid_keys((), {'simple': 'dict'}, {(): {'simple': 'dict'}})
#    mocked_fn.assert_called_once_with({'simple': 'dict'})


def test__get_invalid_keys__empty_input_data(data__input_empty, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_invalid_keys(('Encounter',), data__input_empty, fixture_get_encounter_source_dic)
    expected_data = set()
    assert output_data == expected_data


def test__get_invalid_keys__empty_source_dic(fixture_get_encounter_examples, data__input_empty):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_invalid_keys(('Encounter',), fixture_get_encounter_examples[0], data__input_empty)

    assert "Source definition is empty" in str(exception_info.value)
