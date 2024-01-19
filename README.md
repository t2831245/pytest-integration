### Generate virtualenv:
```
python3 -m venv pytest_env
source /<path>/pytest_env/bin/active
deactivate
```

### Install test packages
```
pip install pytest
pip install requests
```

### Usually run script
```
$ pytest -c pytest.dev.ini
```

### Execute test sample
```
$ pytest 
$ pytest test_offline_provision.py
$ pytest test_offline_provision.py::<function name>
$ pytest test_offline_provision.py::TestOfflineProvision::<function name>

$ pytest --capture=no
$ pytest -vv --cov
$ pytest -c pytest.dev.ini
```

### Pluggin
```
pip install pytest-env
pip install pytest-cov
pip install pytest-html
```