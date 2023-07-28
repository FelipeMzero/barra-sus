import barcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

def calcular_digito_verificacao(numero_cns):
    # Verifica se o número CNS tem 15 dígitos
    if len(numero_cns) != 15 or not numero_cns.isdigit():
        raise ValueError("Número CNS inválido. Deve conter exatamente 15 dígitos numéricos.")

    # Extrai os 12 dígitos iniciais do CNS para calcular o dígito de verificação
    numero_cns_12_digitos = numero_cns[:12]

    # Calcula o dígito de verificação utilizando o algoritmo módulo 11
    soma = 0
    for i in range(11):
        soma += int(numero_cns_12_digitos[i]) * (15 - i)
    resto = soma % 11
    digito_verificacao = 11 - resto if resto != 0 else 0

    return str(digito_verificacao)

def gerar_codigo_de_barras(numero_cns, largura, altura):
    # Calcula o dígito de verificação do CNS
    digito_verificacao = calcular_digito_verificacao(numero_cns)

    # Adiciona o dígito de verificação ao número do CNS
    numero_cns_com_digito = numero_cns + digito_verificacao

    # Gera o código de barras EAN-13
    codigo_barra = EAN13(numero_cns_com_digito, writer=ImageWriter())

    # Define as dimensões do código de barras
    options = {
        'module_width': largura,
        'module_height': altura
    }

    # Salva o código de barras em um arquivo PNG
    codigo_barra.save('codigo_barra_cns', options)

    # Exibe o código de barras gerado
    imagem_codigo_barra = Image.open('codigo_barra_cns.png')
    imagem_codigo_barra.show()

# Exemplo de uso: o usuário digita o número do CNS
numero_cns = input("Digite o número do CNS (15 dígitos): ")
largura = 1.46
altura = 25.93

gerar_codigo_de_barras(numero_cns, largura, altura)
705002422873451