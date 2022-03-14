from scripts.lib.documentcompare import JSONCompare


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
