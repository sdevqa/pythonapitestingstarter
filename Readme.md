# Getting Started

# Overview:


# PIP Packages:
- pip install requests
- pip install pytest
- pip install pytest-html

# Test Running Examples:
- pytest -m {markername} -- run all tests with a given marker.
- pytest {directoryname} -- run all tests in a given directory.
- pytest {filename} -- run a single file.
- pytest --config_url="https://url-you-want-to-hit" -- dynamically specify the target url. Overides value set in conftest.py
- pytest --html=report.html --self-contained-html -- Run tests and generate test output.
- pytest -s -- Debug output to terminal -- Without the -s argument command line output such as print debug will not be visibile.