# Development Guide

## Dependencies

```bash
brew install libyaml         # Mac with Homebrew
apt-get install libyaml-dev  # Ubuntu
```

Install development dependencies:

```bash
pip install -r requirements/development.txt
```

## Tests

```bash
tox
```

## Releases

### PyPI

Add your credentials from PyPI to `~/.pypirc`:

```
[distutils]
index-servers =
    pypi

[pypi]
username:<USERNAME>
password:<PASSWORD>
```

To release a new version to PyPI:

```bash
python setup.py sdist upload
```
