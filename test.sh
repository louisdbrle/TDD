#!/bin/sh

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEST_RUNNER=${PROJECT_DIR}/funcs/tests/funcs_test_main.py
MODULE_DIR=${PROJECT_DIR}/funcs

echo "Testing funcs"

python3 -m unittest ${TEST_RUNNER}

echo "Done testing funcs"

TEST_RUNNER=${PROJECT_DIR}/structs/tests/structs_test_main.py
MODULE_DIR=${PROJECT_DIR}/structs

echo "Testing structs"

python3 -m unittest ${TEST_RUNNER}

echo "Done testing structs"