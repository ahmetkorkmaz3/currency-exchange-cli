"""Currency Exchange CLI
Usage:
    app.py <base> [--count=<count>]
    app.py <base> <symbols> [--count=<count>]
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
import sys

url = 'https://api.exchangeratesapi.io/latest'


def exchange_request(base, symbols='TRY'):
    response = requests.get(url + '?base=' + base + '&symbols=' + symbols)
    return response


def exchange(base, symbols='TRY'):
    response = exchange_request(base, symbols)
    if response.status_code == 200:
        response_rate = float(response.json()["rates"][symbols])
        return response_rate
    elif response.status_code == 400:
        print("İstenilen para birimleri bulunamadı.")
        return None
    else:
        print("Beklenmeyen bir hata oluştu.")
        return None


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    opt = docopt(__doc__, sys.argv[1:])



    if arguments['<base>'] and arguments['<symbols>']:
        base = arguments['<base>']
        symbols = arguments['<symbols>']
        rate = exchange(base.upper(), symbols.upper())
        if opt['--count']:
            count = opt['--count']
            print("{} {} = {:.2f} {}".format(count, base, (rate * float(count)), symbols))
        else:
            print("{} {} = {:.2f} {}".format('1', base, rate, symbols))

    elif arguments['<base>']:
        base = arguments['<base>']
        rate = exchange(base.upper())
        symbols = 'TRY'
        if opt['--count']:
            count = opt['--count']
            print("{} {} = {:.2f} {}".format(count, base, (rate * float(count)), symbols))
        else:
            print("{} {} = {:.2f} {}".format('1', base, rate, symbols))

    else:
        print(arguments)
