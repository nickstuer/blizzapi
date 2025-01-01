# Python BlizzAPI

[![license](https://img.shields.io/github/license/nickstuer/blizzapi.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Python package to connect to the blizzard API. Currently only supports WoW Classic Era but additional support coming soon.

## Table of Contents

- [Background](##background)
- [Install](##install)
- [Usage](##usage)
- [Development](##development)
- [Contributing](##contributing)
- [License](##license)

## 📖 Background

### Any optional sections

## 📌 Install

```
# PyPI
pip install blizzapi
```

## Dependencies
Python 3.10 or greater

## Usage

### WoW Classic Era
```python
from blizzapi import ClassicEraClient
client = ClassicEraClient(client_id=XXX, client_secret=YYY)

result = client.connected_realm_search(fields={"status.type": "UP"})
result = client.wow_token_index()
result = client.character_profile('doomhowl', 'thetusk')
```

### WoW Retail
```python
from blizzapi import RetailClient
client = RetailClient(client_id=XXX, client_secret=YYY)

result = client.wow_token_index()
```

## 💻 Development

#### Virtual Environment Setup
Helpful notes on how to set up a virtual enviroment for developing python applications using VS Code on Windows.

<details><summary><b>Show Instructions</b></summary>

1. Open "Folder" in VS Code

2. Create Virtual Environment
    1. Press CTRL + SHIFT + P and Select 'Python: Create Virtual Environment'
    2. Follow the prompts

3. Change Default Terminal in VS Code
    1. Press CTRL + SHIFT + P and Select 'Terminal: Select Default Profile'
    2. Choose 'Command Prompt'

4. Test the Virtual Environment
     1. Press CTRL + SHIFT + ~ to open a terminal.
     2. Ensure the prompt begins with '(.venv)'
        
</details>

## 🏆 Contributing

PRs accepted.

If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

#### Bug Reports and Feature Requests
Please use the [issue tracker](https://github.com/nickstuer/blizzapi/issues) to report any bugs or request new features.

#### Contributors


## 📃 License

[MIT © Nick Stuer](LICENSE)
