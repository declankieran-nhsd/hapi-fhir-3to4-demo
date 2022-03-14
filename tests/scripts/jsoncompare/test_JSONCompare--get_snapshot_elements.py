from scripts.lib.documentcompare import JSONCompare


def test__get_snapshot_elements__element_exists(data__snapshot_element, data__snapshot_element_transformed_list):
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element)
    expected_data = data__snapshot_element_transformed_list
    assert output_data == expected_data


def test__get_snapshot_elements__element_empty(data__snapshot_element_empty):
    output_data = JSONCompare()._get_snapshot_elements(data__snapshot_element_empty)
    expected_data = []
    assert output_data == expected_data


def test__get_snapshot_elements__empty_input(data__input_empty):
    output_data = JSONCompare()._get_snapshot_elements(data__input_empty)
    expected_data = []
    assert output_data == expected_data
