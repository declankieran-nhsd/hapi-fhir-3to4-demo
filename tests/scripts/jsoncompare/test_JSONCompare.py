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


def test__transform_element_list__invalid_input(data__input_empty):
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
