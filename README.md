<h1 align="center">Welcome to Currency Exchange CLI 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/ahmetmkorkmaz" target="_blank">
    <img alt="Twitter: ahmetmkorkmaz" src="https://img.shields.io/twitter/follow/ahmetmkorkmaz.svg?style=social" />
  </a>
</p>

> Döviz değişim komut istemci uygulaması

<p align="center">
  <a href="https://asciinema.org/a/315064" target="_blank">
    <img src="https://asciinema.org/a/315064.svg" />
  </a>
</p>

## Install

```bash
git clone https://github.com/ahmetkorkmaz3/currency-exchange-cli
cd currency-exchange-cli
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 exchange.py <base> <symbols> [--count=<count>]
```

## Examples
```bash
python3 exchange.py eur
python3 exchange.py eur --count=10
python3 exchange.py eur usd
python3 exchange.py usd eur --count=5
python3 exchange.py try usd
```


## Author

👤 **Ahmet Korkmaz**

* Website: ahmetkorkmaz3.github.io
* Twitter: [@ahmetmkorkmaz](https://twitter.com/ahmetmkorkmaz)
* Github: [@ahmetkorkmaz3](https://github.com/ahmetkorkmaz3)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Ahmet Korkmaz](https://github.com/ahmetkorkmaz3).<br />
This project is [MIT](https://opensource.org/licenses/MIT) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_