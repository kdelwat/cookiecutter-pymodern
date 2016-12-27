from setuptools import setup

import os

package_path = os.path.abspath(os.path.dirname(__file__))
requirements_path = os.path.join(package_path, 'requirements.txt')
dev_requirements_path = os.path.join(package_path, 'requirements-dev.txt')
readme_path = os.path.join(package_path, 'README.md')

with open(requirements_path, 'r') as f:
    install_requirements = f.read().splitlines()

with open(dev_requirements_path, 'r') as f:
    development_requirements = f.read().splitlines()

with open(readme_path, 'r') as f:
    readme = f.read()

setup(
    packages=['{{ cookiecutter.package_name }}'],

    # Package information
    name='{{ cookiecutter.package_name }}',
    version='{{ cookiecutter.version }}',
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',

    description='{{ cookiecutter.short_description }}',
    long_description=readme,

    url='https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.package_name }}',

    # Requirements
    install_requires=install_requirements,
    extras_require={
        'dev': development_requirements,
    },

    # Metadata
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='{{ cookiecutter.package_name }}'
)
