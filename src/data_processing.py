import os
import numpy as np
from PIL import Image
from typing import List, Tuple

def carregar_caminhos_imagens(caminho_pasta: str) -> List[str]:
    """
    Carrega os caminhos de todas as imagens em uma pasta especificada.

    Args:
        caminho_pasta (str): O caminho para a pasta contendo as imagens.

    Returns:
        list[str]: Uma lista de caminhos completos para cada imagem na pasta.
    """
    if not os.path.isdir(caminho_pasta):
            print(f"O caminho especificado '{caminho_pasta}' não é uma pasta válida.")
            return []
    
    arquivos = [os.path.join(caminho_pasta, f) for f in os.listdir(caminho_pasta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Total de imagens encontradas: {len(arquivos)}")
    return arquivos
