# cookiecutter-pymodern

A modern package template for Cookiecutter, targetting Python 3.

# Features

- Task running using [Invoke](http://www.pyinvoke.org/), instead of a Makefile.
- PyPI registration and deployment using [Twine](https://github.com/pypa/twine).
- Linting using [Coala](https://github.com/coala/coala) as a unified interface
  to multiple linters, including [Pylint](https://github.com/PyCQA/pylint/).
- *(Optional)* support for type-checking
  with [Mypy](https://github.com/python/mypy)

# Setup

1. Ensure cookiecutter is installed: `pip install cookiecutter`
2. Create the package structure: `cookiecutter https://github.com/kdelwat/cookiecutter-pymodern`
3. Move into the package: `cd your_package_name`
4. Create a virtual environment for the project
   using [virtualenv](https://github.com/pypa/virtualenv)
   or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
   (recommended): `mkvirtualenv your_package_name`
5. Install the development requirements: `pip install -r requirements-dev.txt`

# Usage

Usage tasks are run using the `invoke` command. The following tasks are available
for general use:

- `clean`: Clean build and distribution files, including `.pyc` compiled files.
- `build`: Build the package.
- `lint`: Run Coala to lint the package with default settings.

# Deployment

`cookiecutter-pymodern` can deploy to [PyPi](https://pypi.python.org/pypi)
using [twine](https://github.com/pypa/twine).

1. Ensure you have a `.pypirc` file in your home directory, configured with
   your username and password. A minimal example from
   the [Python packaging guidelines](https://packaging.python.org) is:
   
   ``` 
   [distutils]
   index-servers=pypi

   [pypi]
   repository = https://upload.pypi.org/legacy/
   username = <username>
   password = <password>
   ```
2. Build and register the package: `invoke register`.
3. Build and deploy new versions with: `invoke deploy`
