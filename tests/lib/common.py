import os, shutil, subprocess, json
from lxml import etree

## @package common
#  Helper and common functions for tests

## Helper function for fetching the input files.  
#  Maybe look at fixtures if the reporting isn't clear enough
#  @param path     Path of folder with input files
#  @param filetype Filetype to return from folder
#  @return List of files from given path of type given in filetype. 
#          Hidden files are ignored.
def get_input_files(path, filetype):
   return [path + filename for filename in os.listdir(path) if not filename.startswith('.') if filename.endswith(filetype)]

## Common function for tests to call the validator_cli.  If running locally, 
#  download the validator_cli.jar from 
#  https://github.com/hapifhir/org.hl7.fhir.core/releases/latest/download/validator_cli.jar 
#  and place in the root of the repo.
#
#  @param input_file The path of the input file to be transformed
#  @return void - A file will be written in temp if this completes sucessfully, 
#                 the test should check the existence of this, if an exception was raised
#                 it should not exist. Doesn't seem to be a tidier way of doing this...
def call_validator_cli(input_file):
    # Get just the filename
    base_input_file_name = os.path.basename(input_file)

    # The validator_cli.jar doesn't seem to work withi absolute or relative paths, 
    # so need to move input file into cwd.  Files are cleaned up aferwards
    shutil.copy(input_file, '.', follow_symlinks=True)
    try:
        process = subprocess.run([
                "java",
                "-jar",
                "../validator_cli.jar",
                "./" + base_input_file_name,
                "-version",
                "3.0",
                "-to-version",
                "4.0",
                "-output",
                "/tmp/expected-" + base_input_file_name
        ], 
        check=True,
        stderr=subprocess.PIPE
        )
    except:
        remove_files(['./' + base_input_file_name])
    remove_files(['./' + base_input_file_name])

## Helper function to sort the transformed files and the expected output.
#  @param input_file The path of the input file, the base of which will 
#                    be used to name the transformed file and retrieve 
#                    the expected file.  See ./README.md for details.
#  @return           The sorted versions of the transformed and expected
#                    json.
def sort_json_files(input_file):
    # Get just the filename of the input file
    base_input_file_name = os.path.basename(input_file)

    transformed_json = json.load(open('/tmp/expected-' + base_input_file_name))
    expected_json = json.load(open(input_file.replace('/input/', '/expected/')))

    transformed = json.dumps(transformed_json, sort_keys=True)
    expected = json.dumps(expected_json, sort_keys=True)

    return [transformed, expected]

## Helper function to load xml file to test equality.  Sorting in xml might 
#  be ok for testing equality, but there are order considerations moreso
#  than for the json https://www.hl7.org/fhir/xml.html.  For now just loading
#  the xml with blank text removed, but maybe look at making a document equality
#  class using a strategy pattern, that could be extended to other types, e.g
#  turtle.
#  @param input_file The path of the input file, the base of which will 
#                    be used to name the transformed file and retrieve 
#                    the expected file.  See ./README.md for details.
#  @return           The loaded xml object.
def load_xml_files(input_file):
    return etree.parse(input_file, etree.XMLParser(remove_blank_text=True))

## Helper function to remove files and ignore error if file does not exist
#  @param files List of files to remove
def remove_files(files):
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            if e.errno != errno.ENOENT:
               raise
