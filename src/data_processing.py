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

def preprocessar_imagem(caminho_imagem: str, tamanho: Tuple[int, int] = (200, 250)) -> np.ndarray:
    """
    Carrega e pré-processa uma imagem: redimensiona e normaliza os valores dos pixels para o intervalo [0, 1].

    Args:
        caminho_imagem (str): O caminho para a imagem a ser processada.
        tamanho (tuple[int, int]): O tamanho para o qual a imagem deve ser redimensionada (largura, altura).

    Returns:
        np.ndarray: A imagem pré-processada como um array NumPy.
    """
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((tamanho_desejado [1], tamanho_desejado[0]))  
    imagem_array = np.array(imagem) / 255.0  # Normaliza para [0, 1]
    return imagem_array