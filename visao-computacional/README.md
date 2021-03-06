# Ideia inicial sobre Visão Computacional - Algumas instruções! 📋

## Parte inicial (com GoogleColab) 🌐

Praticamente todo o conteúdo dessa parte está contido no notebook do GoogleColab neste [link](https://drive.google.com/drive/folders/1MtmQpWrycsldZXCx1Oeh4ZGTJUrn42m-?usp=sharing). Vocês podem acessá-lo e fazer uma cópia dele para trabalhar. Para isso, basta seguir os passos:

Arquivo > Salvar uma cópia no Drive

Feito isso, podem se dirigir até a cópia e trabalhar livremente com ela!

Uma dica é conectar o ambiente de execução antes de começar a executar as células do notebook. Para isso, basta clicar em "Conectar" na parte superior direita da página. 

Para quem nunca utilizou um ambiente semelhante ao Colab, segue um vídeo legal para se ambientar neste [link](https://www.youtube.com/watch?v=Ai9qn9YII78)!

## Para o desafio (rodando um projeto na sua máquina) 💻

O desafios que deixei proposto foi a adaptação do código do nosso estudo de caso para um script .py que vai identificar as formas em uma captura de vídeo, porém isso só é possível de realizar na sua máquina, pois o OpenCV não consegue acessar a câmera do seu computador utilizando um ambiente na web. 

Para isso, deixei um projeto pré-configurado aqui nesse material! Segue um passo a passo para que vocês possam executá-lo nas suas máquinas pessoais.

> É importante que, caso vocês queiram desenvolver o código em paralelo ao mini-curso, sigam essas configurações previamente!

### 1. Precisaremos de um ambiente virtual...

É importante o hábito de criar um ambiente virtual para seus projetos! Desse modo, quando outra pessoa for utilizar ou contribuir com o código poderá utilizar o mesmo ambiente que você desenvolveu, incluindo versionamento das bibliotecas utilizadas e também da linguagem, além de ser muito mais simples para instalar os requerimentos e consertar possíveis problemas no projeto!

Para criar o ambiente virtual em sua máquina, siga os passos indicados na própria documentação do Python neste [link](https://docs.python.org/pt-br/3.8/tutorial/venv.html#creating-virtual-environments).

> Não esqueçam de verificar se estão dentro do diretório do projeto clonado!

#### Algumas informações adicionais

- Versão do Python utilizada: 3.8.5

### 2. Instalando as bibliotecas necessárias

Observe aqui que na raiz do projeto temos um arquivo "requirements.txt". Nesse arquivo temos todas as dependências necessárias para executar o projeto em sua máquina.

Após criar o ambiente virtual você poderá instalar tudo que for necessário utilizando apenas o comando (se você utiliza o VSCode, pode fazê-lo no terminal da IDE):

Para Linux/MacOS/Windows
```
pip install -r requirements.txt
```

> Não esqueçam de verificar se estão dentro do diretório do projeto clonado!

### 3. Mão na massa! 👩‍💻

Depois de ter os passos acima executados, estamos prontas para trabalhar e se divertir com OpenCV! Espero que gostem!

Ah, por último e não menos importante, contribuam com seus códigos desenvolvidos após o mini-curso aqui nesse repositório, postem no LinkedIn, Twitter, compartilhe sua experiência! (E me marca que eu quero ver!)
