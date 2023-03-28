import pytest
import os
import filecmp
from .lib import common

EXAMPLES_PATH = os.path.dirname(os.path.realpath(__file__)) + '/../../examples/input/'
TRANSFORMED_PATH = './expected-'

json_examples = common.get_input_files(EXAMPLES_PATH, '.json')

@pytest.mark.parametrize("input_file", json_examples)
def test_json_transforms(input_file):
    transformed_file = TRANSFORMED_PATH + os.path.basename(input_file)

    # Run transform
    common.call_validator_cli(input_file)
    assert os.path.exists(transformed_file)

    # Sort json to prepare for simple comparison
    [transformed, expected] = common.sort_json_files(input_file)
    common.remove_files([transformed_file])      # Clean up transformed file

    # Test transformed matches expected
    assert transformed == expected

