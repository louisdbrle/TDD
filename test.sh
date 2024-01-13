#!/bin/sh

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TEST_RUNNER=${PROJECT_DIR}/funcs/tests/funcs_tests_main.py
MODULE_DIR=${PROJECT_DIR}/funcs

echo "Testing funcs"

python3 -m unittest ${TEST_RUNNER}

echo "Done testing funcs"

TEST_RUNNER=${PROJECT_DIR}/structs/tests/structs_tests_main.py
MODULE_DIR=${PROJECT_DIR}/structs

echo "Testing structs"

python3 -m unittest ${TEST_RUNNER}

echo "Done testing structs"

TEST_RUNNER=${PROJECT_DIR}/bstpy/tests/bstpy_tests_main.py
MODULE_DIR=${PROJECT_DIR}/bstpy

echo "Testing bstpy"

python3 -m unittest ${TEST_RUNNER}

echo "Done testing bstpy"