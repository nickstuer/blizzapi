# Python BlizzAPI

[![license](https://img.shields.io/github/license/nickstuer/blizzapi.svg)](LICENSE)
<img alt="GitHub Issues or Pull Requests" src="https://img.shields.io/github/issues/nickstuer/blizzapi">

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

This Python package is a user-friendly interface for the Blizzard API. It simplifies the process of retrieving data from Blizzard's API, allowing developers and enthusiasts to seamlessly access and interact with game-related information.

## Table of Contents

- [Features](#📖Features)
- [Install](#🛠install)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 📖 Features

### Comprehensive API Coverage
Access a wide range of game data, including player profiles, achievements, character information and guild information as documented in the official [Blizzard API Documenation](https://develop.battle.net/documentation).

### Oauth2 Integration
Authenticate using Blizzard's OAuth2 system to ensure reliable access to private and public data.

### Ease of Use
With clean and intuitive methods, developers can fetch and manipulate data without diving deep into Blizzard's API documentation.

### Data Format
Conveniently structured JSON responses make it easy to integrate with applications.

### Rate Limit Awareness
Coming Soon

### Supported APIs
| API                                   | Status                              |
| :----------------------------------:  | :--------------------------------:  |
| World Of Warcraft (Retail)            | Partial Support                     |
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

5. Install the pip dependenies
    1. Type: pip install -r requirements.txt
        
</details>

## 🏆 Contributing

PRs accepted.

If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

#### Bug Reports and Feature Requests
Please use the [issue tracker](https://github.com/nickstuer/blizzapi/issues) to report any bugs or request new features.

#### Contributors


## 📃 License

[MIT © Nick Stuer](LICENSE)
