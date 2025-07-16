# Python BlizzAPI

[![PyPI](https://img.shields.io/pypi/v/blizzapi?label=blizzapi)](https://pypi.org/project/blizzapi/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/blizzapi)](https://pypistats.org/packages/blizzapi)
![Python Versions](https://img.shields.io/badge/python-3.10+-blue?logo=python)
<img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues/nickstuer/blizzapi">

![Lines Of Code](https://tokei.rs/b1/github/nickstuer/blizzapi)
[![Codecov](https://img.shields.io/codecov/c/github/nickstuer/blizzapi)](https://app.codecov.io/gh/nickstuer/blizzapi)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nickstuer/blizzapi/run_tests.yml)](https://github.com/nickstuer/blizzapi/actions/workflows/run_tests.yml)

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![license](https://img.shields.io/github/license/nickstuer/blizzapi.svg)](LICENSE)

This Python package is a user-friendly interface for the Blizzard API. It simplifies the process of retrieving data from Blizzard's API, allowing developers and enthusiasts to seamlessly access and interact with game-related information.

## Table of Contents

- [Features](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-features)
- [Install](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-install)
- [Usage](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-usage)
- [Development](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-development)
- [Contributing](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-contributing)
- [License](https://github.com/nickstuer/blizzapi?tab=readme-ov-file#-license)

## 📖 Features

### Comprehensive API Coverage
Access a wide range of game data, including player profiles, achievements, character information and guild information as documented in the official [Blizzard API Documenation](https://develop.battle.net/documentation).

### Oauth2 Integration
Authenticate using Blizzard's OAuth2 system to ensure reliable access to private and public data.

### Ease of Use
With clean and intuitive methods, developers can fetch data without deep diving into Blizzard's API documentation.

### Data Format
Conveniently structured JSON responses make it easy to integrate with applications.

### Supported APIs
| API                                   | Status                              |
| :----------------------------------:  | :--------------------------------:  |
| World Of Warcraft (Retail)            | Supported (Game Data/Profile APIs)  |
| World Of Warcraft (Classic)           | Supported (Game Data/Profile APIs)  |
| World of Warcraft (Classic Era)       | Supported (Game Data/Profile APIs)  |
| Hearthstone                           | Unplanned                           |
| StarCraft 2                           | Unplanned                           |
| Diablo 3                              | Unplanned                           |
| Diablo 4                              | Unsupported (No Blizzard API)       |
| Overwatch 2                           | Unsupported (No Blizzard API)       |


## 🛠 Install

```
# PyPI
pip install blizzapi
```
or
```
uv add blizzapi
```

### Blizzard API Client ID/Secret
You must request API access from blizzard in order to use this module.

[Request API Access](https://develop.battle.net/access/)

##  📌 Dependencies
Python 3.10 or greater

## 🎮 Usage

### WoW Classic Era
```python
from blizzapi import ClassicEraClient
client = ClassicEraClient(client_id=XXX, client_secret=YYY)

result = client.connected_realm_search(fields={"status.type": "UP"})
result = client.character_profile(realmSlug="doomhowl", characterName="thetusk")
```

### WoW Retail
```python
from blizzapi import RetailClient
client = RetailClient(client_id=XXX, client_secret=YYY)

result = client.wow_token_index()
```

## 💻 Development

#### Virtual Environment Setup
Helpful notes on how to set up a virtual enviroment for developing python applications using VS Code.

<details><summary><b>Show Instructions</b></summary>

1. Ensure python and uv are installed on PC. [uv Instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

2. Open "Folder" in VS Code

3. Change the Default Terminal in VS Code
    1. Press CTRL + SHIFT + P (on Windows) or CMD + SHIFT + P (on macOS)
    2. Select 'Terminal: Select Default Profile'
    3. Choose 'Command Prompt' on Windows or 'bash' on macOS

4. Create Virtual Environment
    1. Press CTRL + SHIFT + ` to open a Terminal
    2. Enter 'uv venv'
    3. Enter 'source .venv/bin/activate'
    4. Verify the prompt begins with '(.venv)'

5. Select Python Interpreter
    1. Press CTRL + SHIFT + P (on Windows) or CMD + SHIFT + P (on macOS)
    2. Select 'Python: Select Interpreter'
    3. Choose the .venv python binary

6. Install the dependenies
    1. Enter 'uv sync'
        
</details>

## 🏆 Contributing

PRs accepted.

If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

#### Bug Reports and Feature Requests
Please use the [issue tracker](https://github.com/nickstuer/blizzapi/issues) to report any bugs or request new features.

#### Contributors

<a href = "https://github.com/nickstuer/blizzapi/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=nickstuer/blizzapi"/>
</a>

## 📃 License

[MIT © Nick Stuer](LICENSE)
