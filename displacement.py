import numpy as np
from PIL import Image

def deslocar_imagem(imagem, deslocamento):
    dx, dy = deslocamento
    shifted_image = np.zeros_like(imagem)  # Create an empty image with the same shape and type

    # Calculate the range of the original image's coordinates after the shift
    x_range = max(0, dx), min(imagem.shape[1], imagem.shape[1] + dx)
    y_range = max(0, dy), min(imagem.shape[0], imagem.shape[0] + dy)

    # Calculate the range of the new image's coordinates that will receive the values
    new_x_range = max(0, -dx), min(imagem.shape[1], imagem.shape[1] - dx)
    new_y_range = max(0, -dy), min(imagem.shape[0], imagem.shape[0] - dy)

    # Copy the original image's pixels to the new positions in the new image
    shifted_image[new_y_range[0]:new_y_range[1], new_x_range[0]:new_x_range[1]] = imagem[y_range[0]:y_range[1], x_range[0]:x_range[1]]

    return shifted_image

def main():
    imagem = np.array(Image.open("biden.jpg").convert('RGB'))

    dx = int(input("Digite o deslocamento horizontal em pixels: "))
    dy = int(input("Digite o deslocamento vertical em pixels: "))
    deslocamento = (dx, dy)
    imagem_deslocada = deslocar_imagem(imagem, deslocamento)

    Image.fromarray(imagem_deslocada).show()  # Display the shifted image

if __name__ == "__main__":
    main()
