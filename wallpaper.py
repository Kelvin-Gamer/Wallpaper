import ctypes
import os
from PIL import Image

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if __name__ == "__main__":
    # Nome do arquivo de imagem que será definido como papel de parede
    image_filename = "test.jpg"

    # Obter o caminho completo para a imagem
    image_path = os.path.abspath(image_filename)

    # Verificar se a imagem existe antes de definir como papel de parede
    if os.path.exists(image_path):
        # Define a imagem como papel de parede
        set_wallpaper(image_path)
        print("Papel de parede definido com sucesso.")
    else:
        print(f"Erro: O arquivo {image_path} não foi encontrado.")
