import barcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont

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

def gerar_codigo_de_barras(numero_cns):
    # Calcula o dígito de verificação do CNS
    digito_verificacao = calcular_digito_verificacao(numero_cns)

    # Adiciona o dígito de verificação ao número do CNS
    numero_cns_com_digito = numero_cns + digito_verificacao

    # Gera o código de barras EAN-13
    codigo_barra = EAN13(numero_cns_com_digito, writer=ImageWriter())

    # Salva o código de barras em um arquivo PNG
    codigo_barra.save('codigo_barra_cns', {"module_width": 0.4})

def gerar_cartao_sus(nome_completo, data_nascimento, sexo, numero_cns):
    # Gerar código de barras
    gerar_codigo_de_barras(numero_cns)

    # Cria uma imagem em branco com o fundo retangular
    cartao_sus = Image.new("RGB", (600, 360), (255, 255, 255))
    fundo_retangular = Image.new("RGB", (520, 100), (0, 128, 0))

    # Adiciona o fundo retangular à imagem do cartão do SUS
    cartao_sus.paste(fundo_retangular, (40, 130))

    draw = ImageDraw.Draw(cartao_sus)

    # Carrega a fonte para o texto
    fonte = ImageFont.truetype("arial.ttf", 20)

    # Adiciona os dados ao cartão
    draw.text((60, 150), "Nome: " + nome_completo, fill=(255, 255, 255), font=fonte)
    draw.text((60, 180), "Data Nasc.: " + data_nascimento, fill=(255, 255, 255), font=fonte)
    draw.text((60, 210), "Sexo: " + sexo, fill=(255, 255, 255), font=fonte)

    # Adiciona o número do CNS no cartão
    draw.text((200, 250), numero_cns, fill=(0, 0, 0), font=fonte)

    # Salva o cartão do SUS com os dados e o código de barras
    cartao_sus.save('cartao_sus.png')

if __name__ == "__main__":
    # Exemplo de uso: o usuário digita os dados do cartão
    nome_completo = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (formato DD/MM/AAAA): ")
    sexo = input("Digite o sexo (F ou M): ")
    numero_cns = input("Digite o número do CNS (15 dígitos): ")

    gerar_cartao_sus(nome_completo, data_nascimento, sexo, numero_cns)
