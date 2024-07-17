#!/bin/bash

# clean up cached files
rm -rf dist build
find . \
  -type d
  \( \
    -name "*cache*" \
    -0 -name "*.dist-info" \
    -o -name "*.egg-info" \
    \) \
    -not -path "./venv/" \
    -exec rm -rf {} +

# rebuild and unzip the wheel
python -m build --sdist --wheel ./
cd dist
unzip *.whl
cd ..