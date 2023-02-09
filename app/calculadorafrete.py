import math
import requests
import datetime

#Converte os segundos em horas
def converter(n):
    return str(datetime.timedelta(seconds=n))

#Cria a interface
def cria_tela():
    frame2 = [[sg.Text(auto_size_text=True ,key='informacoes')]]
    frame0 = [[sg.Text('Origem:')],
              [sg.InputText('', key='origem', size=(64,1))],
              [sg.Text('Destino:')],
              [sg.InputText('', key='destino', size=(64,1))],
              [sg.Frame('',frame2, size=(450,110))]]
    frame1 = [[sg.Button('Pesquisar', size=(8,1))],[sg.Button('Fechar', size=(8,1), button_color='red')]]
    frame3 = [[sg.Text('Preço por KM'),sg.Text('',size=(20,1)), sg.Text('Valor do Frete')],
             [sg.InputText(key='preco_km', size=(20,1)),sg.Text('', size=(13,1)),
              sg.Text(border_width=1, background_color='white', text_color='black', size=(20,1), key='totalfrete')],
             [sg.Text('',size=(25,1)), sg.Button('Calcular Frete')],]

    janela1 = [[sg.Frame('', frame0, border_width=0), sg.Frame('', frame1, border_width=0)],
              [sg.Frame('', frame3, size=(550,90))]]

    return sg.Window('Frete', janela1, finalize=True)

#Função que busca os endereços na API da BING
def consulta_endereco(origem, destino):
    BingMapsKey = 'Ah7-h3qqVqsASp-9VcdRRX0GulPojALoBXrGBO9InXS3wR4juv9-8m2FMHBzy6oY'
    busca = (f'http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0={ponto1}&wp.1={ponto2}&key={BingMapsKey}')
    r = requests.get(busca)
    resposta = r.json()
    return resposta

#Extrai o resultado da API e exibe os dados
def mostra_info():
    if resultado['statusCode'] == 400:
        print(f"Erro: {resultado['errorDetails']}")
    else:
        km = resultado['resourceSets'][0]['resources'][0]['travelDistance']
        duracao = converter(resultado['resourceSets'][0]['resources'][0]['travelDuration'])
        origem = resultado['resourceSets'][0]['resources'][0]['routeLegs'][0]['startLocation']['address']['formattedAddress']
        destino = resultado['resourceSets'][0]['resources'][0]['routeLegs'][0]['endLocation']['address']['formattedAddress']

        janela1['informacoes'].update(f"De: \n{origem} \nPara: \n{destino} \nA distancia entre os pontos é de: {km}Km \nDuração de: {duracao}")
    return km

#
#
#     ponto1 = valores['origem']
#     ponto2 = valores['destino']
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
# janela1.close()