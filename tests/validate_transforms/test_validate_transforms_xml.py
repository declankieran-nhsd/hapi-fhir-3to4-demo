import pytest
import os
import filecmp
from .lib import common

EXAMPLES_PATH = os.path.dirname(os.path.realpath(__file__)) + '/../../examples/input/'
TRANSFORMED_PATH = './expected-'

xml_examples = common.get_input_files(EXAMPLES_PATH, '.xml')

@pytest.mark.parametrize("input_file", xml_examples)
def test_xml_transforms(input_file):
    transformed_file = TRANSFORMED_PATH + os.path.basename(input_file)
    expected_file = input_file.replace('/input/', '/expected/')

    # Run transform
    common.call_validator_cli(input_file)
    assert os.path.exists(transformed_file)

    # See note in common for thoughts on xml comparison
    comparison = filecmp.cmp(expected_file, transformed_file)
    common.remove_files([transformed_file])      # Clean up transformed file

    # Test transformed matches expected
    assert comparison 

