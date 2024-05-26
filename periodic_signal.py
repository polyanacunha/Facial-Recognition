import numpy as np
from PIL import Image

def adicionar_sinal_periodico(imagem, amplitude=10, frequencia=10):
    """
    Adiciona uma distorção de onda senoidal horizontal à imagem

    :param imagem: A imagem como um array NumPy.
    :param amplitude: A amplitude da onda senoidal (em pixels).
    :param frequencia: A frequência da onda senoidal (em ciclos por largura da imagem).
    :return: Imagem distorcida como um array NumPy.
    """
    # Altura e largura da imagem
    altura, largura = imagem.shape[:2]

    # Criar uma grade de coordenadas Y
    yy = np.arange(altura)

    # Aplicar a onda senoidal para gerar deslocamentos
    deslocamentos = amplitude * np.sin(2 * np.pi * frequencia * yy / largura)

    # Inicializar a imagem de saída
    imagem_saida = np.zeros_like(imagem)

    # Aplicar o deslocamento em cada linha
    for y in range(altura):
        deslocamento = int(deslocamentos[y])
        imagem_saida[y, :] = np.roll(imagem[y, :], deslocamento, axis=0)

    return imagem_saida

def main():
    # Carregar a imagem
    imagem = np.array(Image.open("biden.jpg").convert('RGB'))

    # Adicionar o sinal periódico à imagem
    imagem_distorcida = adicionar_sinal_periodico(imagem, amplitude=10, frequencia=5)

    # Mostrar a imagem distorcida
    Image.fromarray(imagem_distorcida).show()

if __name__ == "__main__":
    main()
