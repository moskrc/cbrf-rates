# -*- coding: utf-8 -*-
from xmltodict import parse
import requests


def get_rates():
    rates = {}
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response.encoding = 'cp1251'

    text = response.text.encode('utf-8').replace('windows-1251', 'utf-8')
    cbr = parse(text)

    rates['date'] = cbr['ValCurs']['@Date']

    for v in cbr['ValCurs']['Valute']:
        v['Value'] = float(v['Value'].replace(',', '.'))
        rates[v['CharCode']] = v

    return rates

