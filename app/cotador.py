import requests
import time
from datetime import datetime


def cotar(escolha):
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,GBP-BRL,CAD-BRL,EUR-BRL,ARS-BRL,JPY-BRL,AUD-BRL,PYG-BRL,COP-BRL,BOB-BRL')
    cotacao = requisicao.json()
    moeda = float(cotacao[escolha]['bid'])
    return moeda
