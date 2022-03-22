import pytest
from unittest import mock

# Module to test
from scripts.lib.jsoncompare import JSONCompare


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


# Test _get_dict_from_list
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


# Test _strip_list
def test__strip_list__list_contains_dict(data__list_contains_dict__input_and_output):
    output_data = JSONCompare()._strip_list(data__list_contains_dict__input_and_output[0])
    expected_data = data__list_contains_dict__input_and_output[1]
    assert output_data == expected_data


def test__strip_list__empty_input(data__input_empty):
    output_data = JSONCompare()._strip_list(data__input_empty)
    expected_data = {}
    assert output_data == expected_data


# Test _get_invalid_keys
def test__get_invalid_keys__valid(fixture_get_invalid_key_examples__encounter, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_invalid_keys(('Encounter',), fixture_get_invalid_key_examples__encounter[0], fixture_get_encounter_source_dic)
    expected_data = fixture_get_invalid_key_examples__encounter[1]
    assert output_data == expected_data


def test__get_invalid_keys__invalid_key(fixture_get_invalid_key_examples__encounter, fixture_get_encounter_source_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_invalid_keys(('Invalid key',), fixture_get_invalid_key_examples__encounter[0],
                                                      fixture_get_encounter_source_dic)
    assert "is not a key in the source definition" in str(exception_info.value)


@mock.patch('scripts.lib.jsoncompare.JSONCompare._strip_list')
def test__get_invalid_keys__strip_list_called(mocked, data__list_contains_dict):
    JSONCompare()._get_invalid_keys((), data__list_contains_dict, {(): {'dummy': 'data'}})
    mocked.assert_called_once_with(data__list_contains_dict)


def test__get_invalid_keys__empty_input_data(data__input_empty, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_invalid_keys(('Encounter',), data__input_empty, fixture_get_encounter_source_dic)
    expected_data = set()
    assert output_data == expected_data


def test__get_invalid_keys__empty_source_dic(fixture_get_invalid_key_examples__encounter, data__input_empty):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_invalid_keys(('Encounter',), fixture_get_invalid_key_examples__encounter[0], data__input_empty)
    assert "definition is empty" in str(exception_info.value)


# Test _get_valid_keys
def test__get_valid_keys__valid(fixture_get_valid_key_examples__encounter, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_valid_keys(('Encounter',), fixture_get_valid_key_examples__encounter[0], fixture_get_encounter_source_dic)
    expected_data = fixture_get_valid_key_examples__encounter[1]
    assert output_data == expected_data


def test__get_valid_keys__invalid_key(fixture_get_valid_key_examples__encounter, fixture_get_encounter_source_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_valid_keys(('Invalid key',), fixture_get_valid_key_examples__encounter[0],
                                                    fixture_get_encounter_source_dic)
    assert "is not a key in the source definition" in str(exception_info.value)


@mock.patch('scripts.lib.jsoncompare.JSONCompare._strip_list')
def test__get_valid_keys__strip_list_called(mocked, data__list_contains_dict):
    JSONCompare()._get_valid_keys((), data__list_contains_dict, {(): {'dummy': 'data'}})
    mocked.assert_called_once_with(data__list_contains_dict)


def test__get_valid_keys__empty_input_data(data__input_empty, fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_valid_keys(('Encounter',), data__input_empty, fixture_get_encounter_source_dic)
    expected_data = set()
    assert output_data == expected_data


def test__get_valid_keys__empty_source_dic(fixture_get_valid_key_examples__encounter, data__input_empty):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_valid_keys(('Encounter',), fixture_get_valid_key_examples__encounter[0], data__input_empty)
    assert "definition is empty" in str(exception_info.value)


# Test _get_lost_keys
def test__get_lost_keys__valid(fixture_get_lost_key_examples__encounter,
                               fixture_get_encounter_source_dic,
                               fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                               fixture_get_lost_key_examples__encounter[0],
                                               fixture_get_encounter_source_dic,
                                               fixture_get_lost_key_examples__encounter[1],
                                               fixture_get_encounter_target_dic)
    expected_data = fixture_get_lost_key_examples__encounter[2]
    assert output_data == expected_data


def test__get_lost_keys__invalid_key(fixture_get_lost_key_examples__encounter,
                                     fixture_get_encounter_source_dic,
                                     fixture_get_encounter_target_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_lost_keys(('Invalid key',),
                                                   fixture_get_lost_key_examples__encounter[0],
                                                   fixture_get_encounter_source_dic,
                                                   fixture_get_lost_key_examples__encounter[1],
                                                   fixture_get_encounter_target_dic)
    assert "is not a key in the source definition" in str(exception_info.value)


@mock.patch('scripts.lib.jsoncompare.JSONCompare._strip_list')
def test__get_lost_keys__strip_list_called(mocked, data__list_contains_dict):
    JSONCompare()._get_lost_keys((), data__list_contains_dict, {(): {'dummy': 'data'}}, data__list_contains_dict, {(): {'dummy': 'data'}})
    assert 2 == mocked.call_count


def test__get_lost_keys__empty_input_data(data__input_empty,
                               fixture_get_encounter_source_dic,
                               fixture_get_lost_key_examples__encounter,
                               fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                               data__input_empty,
                                               fixture_get_encounter_source_dic,
                                               fixture_get_lost_key_examples__encounter[1],
                                               fixture_get_encounter_target_dic)
    expected_data = set()
    assert output_data == expected_data


def test__get_lost_keys__empty_source_dic(fixture_get_lost_key_examples__encounter,
                                           data__input_empty,
                                           fixture_get_encounter_target_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                                   fixture_get_lost_key_examples__encounter[0],
                                                   data__input_empty,
                                                   fixture_get_lost_key_examples__encounter[1],
                                                   fixture_get_encounter_target_dic)
    assert "definition is empty" in str(exception_info.value)


def test__get_lost_keys__empty_transformed_data(fixture_get_lost_key_examples__empty_transform__encounter,
                                                fixture_get_encounter_source_dic,
                                                data__input_empty,
                                                fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                               fixture_get_lost_key_examples__empty_transform__encounter[0],
                                               fixture_get_encounter_source_dic,
                                               data__input_empty,
                                               fixture_get_encounter_target_dic)
    expected_data = fixture_get_lost_key_examples__empty_transform__encounter[2]
    assert output_data == expected_data


def test__get_lost_keys__empty_data(data__input_empty,
                                    fixture_get_encounter_source_dic,
                                    fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                               data__input_empty,
                                               fixture_get_encounter_source_dic,
                                               data__input_empty,
                                               fixture_get_encounter_target_dic)
    expected_data = set()
    assert output_data == expected_data


def test__get_lost_keys__empty_dic(fixture_get_lost_key_examples__encounter,
                                   data__input_empty):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_lost_keys(('Encounter',),
                                                   fixture_get_lost_key_examples__encounter[0],
                                                   data__input_empty,
                                                   fixture_get_lost_key_examples__encounter[1],
                                                   data__input_empty)
    assert "definition is empty" in str(exception_info.value)


# Test _get_renamed_keys
def test__get_renamed_keys__valid(fixture_get_renamed_keys_examples__encounter,
                                  fixture_get_encounter_source_dic,
                                  fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                  fixture_get_renamed_keys_examples__encounter[0],
                                                  fixture_get_encounter_source_dic,
                                                  fixture_get_renamed_keys_examples__encounter[1],
                                                  fixture_get_encounter_target_dic)
    expected_data = fixture_get_renamed_keys_examples__encounter[2]
    assert output_data == expected_data


def test__get_renamed_keys__invalid_key(fixture_get_renamed_keys_examples__encounter,
                                        fixture_get_encounter_source_dic,
                                        fixture_get_encounter_target_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_renamed_keys(('Invalid key',),
                                                      fixture_get_renamed_keys_examples__encounter[0],
                                                      fixture_get_encounter_source_dic,
                                                      fixture_get_renamed_keys_examples__encounter[1],
                                                      fixture_get_encounter_target_dic)
    assert "is not a key in the source definition" in str(exception_info.value)


@mock.patch('scripts.lib.jsoncompare.JSONCompare._strip_list')
def test__get_renamed_keys__strip_list_called(mocked, data__list_contains_dict):
    JSONCompare()._get_renamed_keys((), data__list_contains_dict, {(): {'dummy': 'data'}}, data__list_contains_dict, {(): {'dummy': 'data'}})
    mocked.assert_called_once_with(data__list_contains_dict)


def test__get_renamed_keys__empty_input_data(data__input_empty,
                                             fixture_get_encounter_source_dic,
                                             fixture_get_renamed_keys_examples__encounter,
                                             fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                  data__input_empty,
                                                  fixture_get_encounter_source_dic,
                                                  fixture_get_renamed_keys_examples__encounter[1],
                                                  fixture_get_encounter_target_dic)
    expected_data = (set(), fixture_get_renamed_keys_examples__encounter[2][1])
    assert output_data == expected_data


def test__get_renamed_keys__empty_source_dic(fixture_get_renamed_keys_examples__encounter,
                                             data__input_empty,
                                             fixture_get_encounter_target_dic):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                      fixture_get_renamed_keys_examples__encounter[0],
                                                      data__input_empty,
                                                      fixture_get_renamed_keys_examples__encounter[1],
                                                      fixture_get_encounter_target_dic)
    assert "is not a key in the source definition" in str(exception_info.value)


def test__get_renamed_keys__empty_transformed_data(fixture_get_renamed_keys_examples__encounter,
                                                   fixture_get_encounter_source_dic,
                                                   data__input_empty,
                                                   fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                  fixture_get_renamed_keys_examples__encounter[0],
                                                  fixture_get_encounter_source_dic,
                                                  data__input_empty,
                                                  fixture_get_encounter_target_dic)
    expected_data = (fixture_get_renamed_keys_examples__encounter[2][0], set())
    assert output_data == expected_data


def test__get_renamed_keys__empty_data(data__input_empty,
                                       fixture_get_encounter_source_dic,
                                       fixture_get_encounter_target_dic):
    output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                  data__input_empty,
                                                  fixture_get_encounter_source_dic,
                                                  data__input_empty,
                                                  fixture_get_encounter_target_dic)
    expected_data = (set(), set())
    assert output_data == expected_data


def test__get_renamed_keys__empty_dic(fixture_get_renamed_keys_examples__encounter,
                                      data__input_empty):
    with pytest.raises(ValueError) as exception_info:
        output_data = JSONCompare()._get_renamed_keys(('Encounter',),
                                                      fixture_get_renamed_keys_examples__encounter[0],
                                                      data__input_empty,
                                                      fixture_get_renamed_keys_examples__encounter[1],
                                                      data__input_empty)
    assert "is not a key in the source definition" in str(exception_info.value)


# Test _get_renamed_keys
def test__get_keys_to_examine__valid(fixture_get_keys_to_examine_examples__encounter,
                                     fixture_get_encounter_source_dic):
    output_data = JSONCompare()._get_keys_to_examine('Encounter',
                                                     fixture_get_keys_to_examine_examples__encounter[0],
                                                     fixture_get_keys_to_examine_examples__encounter[1],
                                                     fixture_get_keys_to_examine_examples__encounter[2],
                                                     fixture_get_encounter_source_dic)
    expected_data = fixture_get_keys_to_examine_examples__encounter[3]
    assert output_data == expected_data
