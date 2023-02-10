import math
import requests
import datetime

#Converte os segundos em horas
def converter(n):
    return str(datetime.timedelta(seconds=n))

#Função que busca os endereços na API da BING
def consulta_endereco(origem, destino):
    BingMapsKey = 'Ah7-h3qqVqsASp-9VcdRRX0GulPojALoBXrGBO9InXS3wR4juv9-8m2FMHBzy6oY'
    busca = (f'http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0={origem}&wp.1={destino}&key={BingMapsKey}')
    r = requests.get(busca)
    resposta = r.json()

    if resposta['statusCode'] == 400:
        return (f"Erro: {resultado['errorDetails']}")
    else:
        km = resposta['resourceSets'][0]['resources'][0]['travelDistance']
        duracao = converter(resposta['resourceSets'][0]['resources'][0]['travelDuration'])
        origem = resposta['resourceSets'][0]['resources'][0]['routeLegs'][0]['startLocation']['address']['formattedAddress']
        destino = resposta['resourceSets'][0]['resources'][0]['routeLegs'][0]['endLocation']['address']['formattedAddress']
        return origem, destino, km, duracao

#
#

#
#         if evento == 'Pesquisar':
#             if valores['origem'] and valores['destino']!='':
#                 resultado = consulta_endereco(ponto1, ponto2)
#                 km = math.ceil(mostra_info())
#             else:
#                 sg.popup('Os campos "ORIGEM" e "DESTINO"\ndevem ser preenchidos.', title='Erro')
#
#         if evento == 'Calcular Frete':
#             if valores['preco_km'] != '':
#                 f1 = int(km)
#                 f2 = int(valores['preco_km'])
#                 v_frete = (f1*f2)
#                 janela1['totalfrete'].update(f'R${v_frete},00')
#             else:
#                 sg.popup('Preencha o valor por KM', title='Erro')
#     except:
#         sg.popup('Verifique os campos', title='Erro')
#
