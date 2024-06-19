# Tech_Assessment
Python Autotests project

This project contains autotests to test the functionality of the application. The tests are written using the library 'pytest' and 'Selenium'.

Preconditions
Make sure you have the following components installed:

Python 3.12 or higher
pip (Python package installer)
venv (built-in Python tool for creating virtual environments)

Setup

1. Cloning repository:
git clone https://github.com/your-repo/pythonProject1.git
cd pythonProject1
2. Create a virtual environment:
python -m venv venv
3. Virtual Environment Activation:

On Windows:
venv Scripts activate

On macOS and Linux:
source venv/bin/activate
4. Dependency Setting:
pip install -r requirements.txt

Test run

Check that you are in the project root directory (where README.md is located).

Run the tests with pytest:
pytest

Notes

Make sure all import paths are correct and the pages and tests directories contain the file __init_.py.

If you have import problems, add the project root directory to PYTHONPATH. This can be done at the beginning of the test files:

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(___file__), '.')))
