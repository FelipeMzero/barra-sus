import cv2
import pytesseract

# Carrega a imagem
imagem = cv2.imread('imagem.png')

# Converte a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica OCR na imagem para extrair o texto
texto_extraido = pytesseract.image_to_string(imagem_cinza)

# Exibe o texto extraído
print(texto_extraido)
