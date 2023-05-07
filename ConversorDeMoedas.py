import requests # Instale a biblioteca requests no terminal PowerShell do windows "pip install requests --user"
import os

# loop infinito
while True:
    
    url = "https://economia.awesomeapi.com.br/json/"

    # vou pedir pra ler o documento moedas.txt e gravar na variavel moedas
    with open("moedas.txt", "r") as file:
        moedas = file.read()
        print("\n Moedas Úteis: \n---\n ", moedas,"\n---\n")

    # Coleta de informação
    moeda1 = input('Insira o sufixo da moeda que você tem: ').upper()
    moedaHistorico1 = moeda1
    
    # se tiver o sufixo digitado em moedas ele vai continuar
    if moeda1 in moedas:
        resposta = requests.get(url+moeda1) # Vou pegar a resposta do Get url+moeda
        respostaJson = resposta.json()[0]["bid"]# Retornou uma lista, então quero o valor 0 pois não tem mais nenhum valor
        
        # Aqui ele vai armazenar apenas 2 casas depois da "Vírgula"
        moeda1 = float(respostaJson)
        moeda1 = "{:.2f}".format(moeda1)
        
    # Se não tiver o sufixo ele vai avisar e fechar
    else:
        print('Moeda inválida!')
        exit()

    # Coletando informação
    moeda2 = input('Insira a moeda de destino: ').upper()
    moedaHistorico2 = moeda2
    
    # Se tiver o sufixo...
    if moeda2 in moedas:
        resposta = requests.get(url+moeda2)
        respostaJson = resposta.json()[0]["bid"]

        # Salvar apenas os 2 numeros depois da Vírgula
        moeda2 = float(respostaJson)
        moeda2 = "{:.2f}".format(moeda2)
    
    # se não tiver o sufixo...
    else:
        print('Moeda Inválida!')
        exit()

    # Função pra converter da Moeda1 pra Moeda2
    def Converter(moeda1, moeda2):
        resultado = float(moeda1) / float(moeda2)
        return resultado

    # Formatando pra ter apenas 2 casas depois da vírgula
    resultado = Converter(moeda1, moeda2) # Chamando a função pra retornar o resultado
    resultado = "{:.2f}".format(resultado)
    
    # Insira a quantia que quer converter!
    quantia = float(input('Insira a quantidade a ser convertida: '))
    
    # Convertendo o valor digitado
    totalConvertido = quantia * float(resultado)
    totalConvertido = "{:.2f}".format(totalConvertido)
    print(totalConvertido)

    # Vai armazenar no Historico
    with open('histórico.txt', 'a') as arquivo:
        arquivo.write(f"Conversão Feita: \n {moedaHistorico1}: {moeda1} para {moedaHistorico2}: {moeda2} \nQuantia de {moedaHistorico1}: {quantia} \nTotal de {moedaHistorico2}: {totalConvertido}\n----------------------------\n")
    
    if input("Deseja ver o histórico?").upper() == "S":
        with open("histórico.txt", "r") as file:
            print(file.read())
            print("\n")

# Aprendi a pouco tempo a mexer um pouco com a biblioteca request, conforme eu for aprendendo pretendo melhorar este código!
