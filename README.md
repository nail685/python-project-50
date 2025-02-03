### Hexlet tests and linter status:
[![Actions Status](https://github.com/nail685/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/nail685/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/095852ec6ea373894305/maintainability)](https://codeclimate.com/github/nail685/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/095852ec6ea373894305/test_coverage)](https://codeclimate.com/github/nail685/python-project-50/test_coverage)


## Gendiff

## Description:

This is the difference calculator - a command line utility which can find differences between two files. It supports .json and yaml. formats.

## Installation:

Install using pip:
pip install git+https://github.com/nail685/python-project-50.git

Install using UV:
Clone the repository https://github.com/nail685/python-project-50.git
cd gendiff
uv sync

## Usage:

To find differences between two files:

gendiff <file_path1><file_path2>

Sample output:

{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}

## Options:
-h, --help 
-f, --format - set the output format (supported formats: `plain`, `json`, `stylish`). Default format 'stylish'

stylish - shows differences as a tree
plain - shows differences in following format 'Property 'common.follow' was added with value: false'
json - showa differences in json

## Dependencies:
python = "^3.10"
pyyaml = "^6.0.2"


How it works:
With .json files without nested structures



With .yaml files without nested structures



Stylish formatter



Plain formatter



JSON formatter


