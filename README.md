Sistema de Classificação de Gênero em Tempo Real para Marketing Inteligente

<!-- Badges -->

<p align="center">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Status-Em%2520Desenvolvimento-yellow%3Fstyle%3Dfor-the-badge" alt="Status do Projeto"/>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.8%252B-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython" alt="Versão do Python"/>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/TensorFlow-2.x-orange%3Fstyle%3Dfor-the-badge%26logo%3Dtensorflow" alt="Versão do TensorFlow"/>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/OpenCV-4.x-green%3Fstyle%3Dfor-the-badge%26logo%3Dopencv" alt="Versão do OpenCV"/>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Licen%25C3%25A7a-MIT-lightgrey%3Fstyle%3Dfor-the-badge" alt="Licença"/>
</p>

<!-- Banner -->

<p align="center">
<img src="https://www.google.com/search?q=https://placehold.co/1200x400/2B364A/E0E0E0%3Ftext%3DMarketing%2BInteligente%2Bcom%2BIA%26font%3Dmontserrat" alt="Banner do Projeto"/>
</p>

Este projeto implementa um sistema de visão computacional capaz de detectar rostos e classificar o gênero de pessoas em tempo real a partir de um feed de vídeo. A solução foi projetada para atuar como o motor de um sistema de "marketing inteligente" em lojas de varejo, permitindo a personalização de anúncios digitais com base no público presente.

📋 Índice

Visão Geral do Negócio (Método STAR)

🏗️ Arquitetura da Solução

🛠️ Tecnologias Utilizadas

📁 Estrutura do Projeto

🚀 Como Começar

🤝 Como Contribuir

📄 Licença

👨‍💻 Autor

🎯 Visão Geral do Negócio (Método STAR)



Descrição

(S)ituação

Uma empresa de varejo buscava personalizar a experiência do cliente em lojas físicas, mas não possuía uma forma eficiente de adaptar suas campanhas de marketing digital em tempo real para o público presente, resultando em baixo engajamento com os anúncios.

(T)arefa

Desenvolver um modelo de visão computacional para atuar como o motor de um sistema de "marketing inteligente". O objetivo era classificar o gênero de clientes a partir de imagens em tempo real para permitir que o sistema de publicidade digital exibisse promoções e produtos mais relevantes.

(A)ção

A arquitetura do projeto foi dividida em dois componentes: um pipeline de treinamento offline para construir um modelo robusto de Rede Neural Convolucional (CNN) com TensorFlow e Keras, e uma aplicação de inferência em tempo real que utiliza OpenCV para capturar vídeo, detectar rostos e classificá-los com o modelo treinado.

(R)esultado

O modelo treinado alcançou 86% de acurácia em dados de validação. A solução final, quando integrada a um sistema de publicidade, tem o potencial de aumentar o engajamento do cliente em 15-20% ao apresentar conteúdo personalizado, impactando diretamente as vendas e melhorando a experiência de compra na loja.

🏗️ Arquitetura da Solução

O sistema é modular, separado em duas responsabilidades principais para garantir manutenibilidade e escalabilidade.

Pipeline de Treinamento (Offline): Um conjunto de scripts responsáveis por carregar os dados, pré-processá-los, treinar o modelo de CNN e salvar o artefato final (.h5) no diretório models/. Este processo é executado sempre que o modelo precisa ser aprimorado.

Aplicação de Inferência (Tempo Real): Um aplicativo que carrega o modelo treinado. Ele utiliza o OpenCV para acessar a câmera, um detector de rostos pré-treinado para localizar rostos em cada frame e, em seguida, nosso modelo para classificar o gênero, exibindo o resultado na tela.

🛠️ Tecnologias Utilizadas

Ferramenta

Propósito

Python

Linguagem principal do projeto.

TensorFlow & Keras

Construção e treinamento da Rede Neural Convolucional.

OpenCV

Captura de vídeo e detecção de rostos em tempo real.

Scikit-learn

Avaliação de métricas do modelo.

NumPy & Pandas

Manipulação de dados e pré-processamento.

Matplotlib & Seaborn

Visualização de dados e resultados do treinamento.

Git & GitHub

Controle de versão e hospedagem do código.

📁 Estrutura do Projeto

A estrutura de pastas foi organizada para separar responsabilidades, seguindo as melhores práticas de projetos de Machine Learning.

/real-time-gender-classification/
│
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── README.md           # Documentação principal do projeto (este arquivo)
├── requirements.txt    # Lista de dependências Python para o projeto
│
├── data/               # (Ignorado pelo Git) Dados brutos e processados
│   └── .gitkeep
│
├── models/             # (Ignorado pelo Git) Modelos treinados
│   └── .gitkeep
│
├── notebooks/          # Notebooks Jupyter para exploração e prototipagem
│   └── initial_exploration.ipynb
│
└── src/                # Código fonte principal da aplicação
    ├── __init__.py
    ├── data_processing.py  # Funções para carregar e pré-processar imagens
    ├── model.py            # Definição da arquitetura da CNN
    ├── train.py            # Script para executar o pipeline de treinamento
    └── inference.py        # Script para executar a aplicação em tempo real


🚀 Como Começar

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos

Python 3.8 ou superior

Git

Instalação

Clone o repositório:

git clone [https://github.com/](https://github.com/)[wallacemattos-dados]/real-time-gender-classification.git
cd real-time-gender-classification


Crie e ative um ambiente virtual:

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


(As instruções de execução serão adicionadas conforme o desenvolvimento avança)

🤝 Como Contribuir

Contribuições são bem-vindas! Para contribuir com o projeto, por favor, siga o fluxo de trabalho abaixo:

Faça um Fork deste repositório.

Crie uma nova branch a partir da develop: git checkout -b feature/sua-feature-incrivel

Faça suas alterações e realize os commits: git commit -m "feat: adiciona sua feature incrivel"

Envie suas alterações para o seu fork: git push origin feature/sua-feature-incrivel

Abra um Pull Request para a branch develop do repositório original.

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👨‍💻 Autor

Feito por Irlan Wallace Mattos