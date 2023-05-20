pytest -k Tests
flake8 --ignore=E501 --per-file-ignores="Tests/*:E402"
