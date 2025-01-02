# NOTES


## PyPi

Commands for uploading packages to PyPi. Needs API key for PyPI. Needs pyproject.toml file.

### Setup
- Install twine and build if not installed.
```bash
py -m pip install --upgrade build
py -m pip install --upgrade twine
```

- Get API key from PyPI and save to ~/Users/{username}/.pypirc
```
[pypi]
  username = __token__
  password = {key with preceeding pypi- text}
```

- Create (or update) a pyproject.toml file per the documentation on PyPI

### Build and Upload
2. Build
```bash
py -m build
```

3. Upload
```bash
py -m twine upload dist/*
````