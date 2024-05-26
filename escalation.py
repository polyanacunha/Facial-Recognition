from PIL import Image, ImageResampling
import numpy as np

def escalar_imagem(imagem, nova_largura, nova_altura):
    # Convert the NumPy array to a PIL Image object
    img_pil = Image.fromarray(imagem)

    # Resize the image using PIL's resize method with Image.Resampling.LANCZOS
    imagem_escalada = img_pil.resize((nova_largura, nova_altura), ImageResampling.LANCZOS)

    # Convert the PIL Image back to a NumPy array
    return np.array(imagem_escalada)

# Rest of your code remains the same

def main():
    # Load the image
    imagem = np.array(Image.open("biden.jpg").convert('RGB'))

    # Get the new size from the user
    nova_largura = int(input("Digite a nova largura em pixels: "))
    nova_altura = int(input("Digite a nova altura em pixels: "))

    # Scale the image
    imagem_escalada = escalar_imagem(imagem, nova_largura, nova_altura)

    # Display the scaled image
    Image.fromarray(imagem_escalada).show()

if __name__ == "__main__":
    main()
