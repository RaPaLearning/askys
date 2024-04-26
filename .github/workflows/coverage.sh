#!/bin/bash
set -e

coverage erase

coverage run --append -m unittest discover
coverage run --append md_to_english.py test

coverage html
coverage report
COVERAGE=$(coverage report | awk 'END{print $NF}' | sed 's/[^0-9]*//g')
if [ "$COVERAGE" -lt 100 ]; then
    echo "Coverage is less than 100%. Failing the build..."
    exit 1
else
    echo "Coverage is complete :)"
fi
