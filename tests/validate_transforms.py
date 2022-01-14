import pytest, os, shutil, subprocess, json

examples = next(os.walk('../examples/input'), (None, None, []))[2]

@pytest.mark.parametrize("example", examples)
def test_transforms(example):
    # validator_cli.jar doesn't work with relative paths, so need to move file into cwd
    shutil.copy("../examples/input/" + example, ".", follow_symlinks=True)
    try:
        process = subprocess.run([
		        "java",
		        "-jar",
	    	    "../validator_cli.jar",
		        "./" + example,
		        "-version",
	    	    "3.0",
                "-to-version",
                "4.0",
                "-output",
                "/tmp/expected-" + example 
        ], 
        check=True,
        stderr=subprocess.PIPE
        )
    except:
        remove_files(["./" + example])

    assert os.path.exists('/tmp/expected-' + example)

    transformed_json = json.load(open('/tmp/expected-' + example))
    expected_json = json.load(open('../examples/expected/' + example))
    
    transformed = json.dumps(transformed_json, sort_keys=True)
    expected = json.dumps(expected_json, sort_keys=True)

    remove_files([
            '/tmp/expected-' + example,   # Tranformed file
            './' + example                # Input file
    ])

    assert transformed == expected

# Helper function
# Remove files and ignore error if file does not exist
def remove_files(files):
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            if e.errno != errno.ENOENT:
               raise

