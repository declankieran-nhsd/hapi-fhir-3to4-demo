from scripts.lib.documentcompare import JSONCompare


def test__extract_choice_types__valid_input(data__snapshot_element_choices):
    output_data = JSONCompare()._extract_choice_types(data__snapshot_element_choices)
    expected_data = [
        ['Communication', 'payload', 'contentString'],
        ['Communication', 'payload', 'contentAttachment'],
        ['Communication', 'payload', 'contentReference']
    ]
    assert output_data == expected_data


def test__transform_element_list__invalid_input(data__input_empty):
    output_data = JSONCompare()._extract_choice_types(data__input_empty)
    expected_data = []
    assert output_data == expected_data
