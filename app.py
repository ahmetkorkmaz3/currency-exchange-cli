"""Currency Exchange CLI
Usage:
    app.py <base>
    app.py <base> <symbols>
    app.py -h|--help
    app.py -v|--version
Options:
    <base>  İşlem yapılacak ana para birimi
    <symbols>  Dönüştürülmesi istenen para birimi
    -h --help  Uygulama kullanım yardımcısı
    -v --version  Uygulama versiyonu
"""
from docopt import docopt
import requests

url = 'https://api.exchangeratesapi.io/latest'


def exchange_request(base, symbols='TRY'):
    response = requests.get(url + '?base=' + base + '&symbols=' + symbols)
    return response


def exchange(base, symbols='TRY'):
    response = exchange_request(base, symbols)
    if response.status_code == 200:
        response_rate = float(response.json()["rates"][symbols])
        print("1 {0} = {1:.2f} {2}".format(base, response_rate, symbols))
    elif response.status_code == 400:
        print("İstenilen para birimleri bulunamadı.")
    else:
        print("Beklenmeyen bir hata oluştu.")


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')

    if arguments['<base>'] and arguments['<symbols>']:
        base = arguments['<base>']
        symbols = arguments['<symbols>']
        exchange(base.upper(), symbols.upper())
    elif arguments['<base>']:
        base = arguments['<base>']
        exchange(base.upper())
    else:
        print(arguments)
