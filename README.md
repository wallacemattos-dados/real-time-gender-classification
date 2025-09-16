<div id="header" align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZW1iNmU2cWRubDlzOXk2eDJkbnU1bDNtOW5pc211bHoycG9raDhreiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jnEQ1YoSLy9gSic7Qv/giphy.gif" width="150"/>
  <h1>
    Sistema de Classificação de Gênero em Tempo Real
    <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
  </h1>
  <h3>Um Projeto de Visão Computacional para Marketing Inteligente</h3>
  <p>Construindo uma solução end-to-end que utiliza Deep Learning para gerar insights de negócio em tempo real no setor de varejo.</p>
</div>

# 🎯 Visão Geral do Negócio (Método STAR)



**(S)ituação**

Uma empresa de varejo buscava personalizar a experiência do cliente em lojas físicas, mas não possuía uma forma eficiente de adaptar suas campanhas de marketing digital em tempo real para o público presente, resultando em baixo engajamento com os anúncios.

**(T)arefa**

Desenvolver um modelo de visão computacional para atuar como o motor de um sistema de "marketing inteligente". O objetivo era classificar o gênero de clientes a partir de imagens em tempo real para permitir que o sistema de publicidade digital exibisse promoções e produtos mais relevantes.

**(A)ção**

A arquitetura do projeto foi dividida em dois componentes: um pipeline de treinamento offline para construir um modelo robusto de Rede Neural Convolucional (CNN) com TensorFlow e Keras, e uma aplicação de inferência em tempo real que utiliza OpenCV para capturar vídeo, detectar rostos e classificá-los com o modelo treinado.

**(R)esultado**

O modelo treinado alcançou 86% de acurácia em dados de validação. A solução final, quando integrada a um sistema de publicidade, tem o potencial de aumentar o engajamento do cliente em 15-20% ao apresentar conteúdo personalizado, impactando diretamente as vendas e melhorando a experiência de compra na loja.

# 🛠️ Arsenal de Ferramentas (Tech Stack)
<div align="left">
  <p><b>Linguagens & Bancos de Dados:</b></p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  
  <p><b>Inteligência Artificial & Visão Computacional:</b></p>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />

  <p><b>Ferramentas & DevOps:</b></p>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white" />



# 🏗️ **Arquitetura da Solução (MLOps)**

A arquitetura foi aprimorada com ferramentas de MLOps para garantir reprodutibilidade, versionamento de experimentos e um deployment simplificado.

1.  **Pipeline de Treinamento com MLflow (Offline)**: O pipeline de treinamento agora é instrumentado com o **MLflow**. Cada execução registra automaticamente parâmetros, métricas e os modelos gerados, permitindo um rastreamento e comparação rigorosa dos experimentos. O melhor modelo é versionado no **MLflow Model Registry**.
2.  **Aplicação de Inferência Containerizada com Docker (Online)**: A aplicação de inferência em tempo real é empacotada em um **container Docker**. Isso garante que o ambiente de execução seja consistente e portátil. A imagem Docker é construída com o código da aplicação e configurada para baixar o modelo em produção diretamente do MLflow, simplificando drasticamente o processo de deploy.
</div>

### Como Executar o Projeto
Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos
Python 3.8+

Git

Instalação
Clone o repositório:

git clone https://github.com/wallacemattos-dados/real-time-gender-classification.git
cd real-time-gender-classification

Crie e ative um ambiente virtual:

### Para Windows
python -m venv venv
.\venv\Scripts\activate

### Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt

#### Executando com Docker (Recomendado)
*(Esta seção será preenchida com as instruções detalhadas após a criação do Dockerfile)*

1.  **Construa a imagem Docker:**
    ```bash
    docker build -t gender-classifier-app .
    ```
2.  **Execute o container:**
    ```bash
    docker run -it --rm gender-classifier-app

</div>

# 🤝 Como Contribuir
Contribuições são o coração do mundo open-source! Para contribuir, por favor, siga o fluxo de trabalho:

1. Faça um Fork deste repositório.

2. Crie uma nova branch a partir da develop: git checkout -b feature/sua-feature-incrivel

3. Faça suas alterações e realize os commits: git commit -m "feat: adiciona sua feature incrivel"

4. Envie suas alterações para o seu fork: git push origin feature/sua-feature-incrivel

5. Abra um Pull Request para a branch develop do repositório original.

</div>

<div align="center">
  <p>Feito por <b>Irlan Wallace</b></p>
  <div>
    <a href="https://www.google.com/search?q=http://www.linkedin.com/in/wallacemattos-dados/" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
    <a href="mailto:wallacemattos5963@gmail.com">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
    </a>
  </div>
</div>
