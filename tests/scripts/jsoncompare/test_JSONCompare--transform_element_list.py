from scripts.lib.documentcompare import JSONCompare


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
