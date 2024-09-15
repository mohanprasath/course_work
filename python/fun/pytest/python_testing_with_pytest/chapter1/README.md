# Commands Backup

## Running pytest
pytest test_one.py
pytest -v test_one.py

pytest -v test_two.py
pytest -vv test_two.py
pytest test_two.py

### tracebacks tb
pytest --tb=no
pytest --tb=no test_one.py test_two.py
cd ..
pytest --tb=no chapter1
pytest --tb=no chapter1/test_one.py::test_passing

## Test Discovery

- pytest goes off to find the tests to run is test discovery
- either cwd, or all files, or given fileanme, all sub_directories, etc
- name it like test_ for files, name classes as Test

## Test Outcomes

- PASSED, FAILED, SKIPPED, XFAIL, XPASS, ERROR
- @pytest.mark.skip(), @pytest.mark.skipif()
- @pytest.mark.xfail
