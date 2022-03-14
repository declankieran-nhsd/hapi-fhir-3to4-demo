import pytest, os

# Change dir to location of code
@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname + '/../../../scripts')

