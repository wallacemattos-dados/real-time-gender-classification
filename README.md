Sistema de Classificação de Gênero em Tempo Real para Marketing Inteligente
Autor: Irlan Wallace Mattos
Status: Em Desenvolvimento

1. Visão Geral do Projeto (Método STAR)
Este projeto implementa um sistema de visão computacional capaz de detectar rostos e classificar o gênero de pessoas em tempo real a partir de um feed de vídeo. A solução foi projetada para atuar como o motor de um sistema de "marketing inteligente" em lojas de varejo, permitindo a personalização de anúncios digitais com base no público presente.

(S) Situação: Uma empresa do setor de varejo buscava personalizar a experiência do cliente em suas lojas físicas, mas não tinha uma maneira eficiente de adaptar suas campanhas de marketing digital em tempo real para o público presente, resultando em baixo engajamento.

(T) Tarefa: Desenvolver um modelo de visão computacional para classificar o gênero de clientes a partir de imagens em tempo real, permitindo que o sistema de publicidade exiba promoções e produtos mais relevantes.

(A) Ação: A arquitetura do projeto foi dividida em dois componentes principais: um pipeline de treinamento offline para construir um modelo robusto de Rede Neural Convolucional (CNN) e uma aplicação de inferência em tempo real que utiliza o modelo treinado para detectar e classificar rostos a partir de uma fonte de vídeo.

(R) Resultado Esperado: Criar uma solução que, integrada a um sistema de publicidade, possa aumentar o engajamento do cliente em campanhas na loja em estimados 15-20%, ao apresentar conteúdo mais relevante e personalizado, impactando diretamente as vendas. O modelo treinado alcançou uma acurácia de 86% em dados de validação.

2. Arquitetura da Solução
O sistema é composto por dois módulos principais:

Pipeline de Treinamento (Offline): Responsável por pré-processar o dataset de imagens, treinar o modelo de classificação de gênero e salvar o artefato do modelo.

Aplicação de Inferência (Tempo Real): Utiliza OpenCV para capturar o feed de vídeo, um modelo pré-treinado para detecção de rostos, e o nosso modelo treinado para classificar o gênero, exibindo os resultados em tempo real.

3. Tecnologias Utilizadas
Linguagem: Python

Bibliotecas de Deep Learning: TensorFlow, Keras

Bibliotecas de Visão Computacional: OpenCV

Bibliotecas de Análise de Dados: Pandas, NumPy, Matplotlib

Versionamento: Git & GitHub

4. Como Executar o Projeto
(Esta seção será preenchida posteriormente com as instruções de instalação e execução)

Clone o repositório: git clone https://github.com/wallacemattos-dados/real-time-gender-classification.git

Crie e ative um ambiente virtual.

Instale as dependências: pip install -r requirements.txt

Execute a aplicação: python src/run_inference.py