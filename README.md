# Avaliação Analista de Testes

## Setup

- Para execução das suítes de testes automatizados é necessário que você tenha as seguintes ferramentas instaladas:

  - [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
  - [Git](https://git-scm.com/downloads)
  - [Python](https://www.python.org/downloads/)
  - [Postman](https://www.postman.com/downloads/)

## Questões Teóricas

As respostas para as questões 1-8 encontram-se dentro do diretório: "1-8 questoes" no arquivo: "Prova - Analista de Teste - Resolucao Symon Barreto.pdf"

## Questão 9: Automação de testes funcionais utilizando o Selenium WebDriver

### Casos de Testes

| ID        | Casos de Testes                                             | Gherkin                                                                                                                                                                                                                                                                                                                              | Data da Execução | Resultado Esperado                          | Resultado Obtido | Resultado Verificado  |
| --------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------- | ---------------- | --------------------- |
| **CT001** | Verificar triângulo equilátero                              | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: 3,3 e 3 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Equilátero                                    | 16/01/2025       | Equilátero                                  | Equilátero       | Executado com sucesso |
| **CT002** | Verificar triângulo isósceles                               | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: 4,4 e 3 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Isósceles                                     | 16/01/2025       | Isósceles                                   | Isósceles        | Executado com sucesso |
| **CT003** | Verificar triângulo escaleno                                | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: 5,4 e 3 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Escaleno                                      | 16/01/2025       | Escaleno                                    | Escaleno         | Executado com sucesso |
| **CT004** | Verificar valores que não formam um triângulo               | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: 10,10 e 2 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Os lados informados não formam um triângulo | 16/01/2025       | Os lados informados não formam um triângulo | Isóceles         | Executado com falha   |
| **CT005** | Verificar que valores nulos não formam um triângulo         | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: 0,0 e 0 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Valores inválidos                             | 16/01/2025       | Valores inválidos                           | Equilátero       | Executado com falha   |
| **CT006** | Verificar que valores negativos não formam um triângulo     | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: -1,-1 e -1 respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Valores inválidos                          | 16/01/2025       | Valores inválidos                           | Equilátero       | Executado com falha   |
| **CT007** | Verificar que valores não númericos não formam um triângulo | **Dado** que o usuário está na página: https://www.vanilton.net/triangulo/# <br> **Quando** ele preencher os campos: Vértice 1, Vértice 2 e Vértice 3 com os valores: a,b e c respectivamente <br> **E** clicar no botão: Identificar <br> **Então** o sistema deve exibir a mensagem: Valores inválidos                             | 16/01/2025       | Valores inválidos                           | Escaleno         | Executado com falha   |

Para validar a resposta dessa questão é necessário realizar os seguintes passo:

1. Clone esse repositório usando um terminal com o seguinte comando:

   ```bash
   git clone https://github.com/s4imu/Avaliacao-Analista-de-Testes.git
   ```

2. Acesse o repositório da questão com o seguinte comando:
   ```bash
   cd Avaliacao-Analista-de-Testes\9 automacao testes funcionais
   ```
3. Crie o virtual enviroment para instalação das depedências necessárias posteriomente:

   ```bash
   python -m venv venv
   ```

4. Ative o virtual enviroment com o seguinte comando:
   ```bash
   venv\Scripts\activate
   ```
   uma vez ativado ele deve aparecer com algo parecido no seu terminal:
   ```bash
   (venv) <caminho do diretorio>\Avaliacao-Analista-de-Testes>
   ```
5. Instale as dependencias do projeto com o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

6. Para executar a automação utilize o comando:
   ```bash
   pytest -v
   ```

<span style="color: red; font-weight: bold">Obs: Durante a execução verificou-se que o sistema não faz a verificação de que se os valores informados realmente formam um triângulo e nem exibe uma mensagem de erro caso não formem o que levou a falhas dos casos de teste: CT004, CT005, CT006 e CT007.</span>

## Questão 10: teste em APIs Rest

### Casos de Testes

| ID        | Casos de Testes    | Gherkin                                                                                                                                                                                                                                                                                                                                                                                                                                             | Data da Execução | Resultado Esperado                                                                             | Resultado Obtido                                                                               | Resultado Verificado  |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------- |
| **CT001** | Criar um produto   | **Dado** que o usuário deseja criar um produto <br> **Quando** ele enviar uma requisição: POST para o endpoint: http://localhost:8000/produtos/ <br> **E** com Content-Type: application/json <br> **E** com Body: { "nome": "Mouse", "preco": "3.00", "quantidade": 2, "categoria": 1 } <br> **Então** o sistema deve retornar resposta com código: 201 <br> **E** com Body: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 } | 16/01/2025       | Status Code: 201 e Body: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 } | Status Code: 201 e Body: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 } | Executado com sucesso |
| **CT002** | Filtrar um produto | **Dado** que o usuário deseja criar um produto <br> **Quando** ele enviar uma requisição: POST para o endpoint: http://localhost:8000/produtos/ID_PRODUTO/?format=json <br> **E** com Content-Type: application/json <br> **Então** o sistema deve retornar resposta com código: 201 <br> **E** com Body parecido com esse formato: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 }                                           | 16/01/2025       | Status Code: 200 e Body: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 } | Status Code: 200 e Body: { "nome": "Mouse", "preco": "6.00", "quantidade": 2, "categoria": 1 } | Executado com sucesso |

Para validar a resposta dessa questão é necessário realizar os seguintes passo:

- Subir o serviço em Django Rest Framework para teste (containers Docker)
  o Faça o clone do projeto git: https://github.com/Vanilton18/loja
  api.git
  o Siga os passos do README.md a partir da seção “Executar
  container API”
- <span style="color: red; font-weight: bold">Os testes foram preparados para serem executados em containers que não tenham ainda nenhum produto cadastrado</span>

1. Importe no Postman os arquivos: "11 Testes em APIs Rest - Symon Barreto.postman_collection" e "11 Testes em APIs Rest - Symon Barreto.postman_environment" dentro do diretório: 10 teste em APIs Rest.

2. Selecione o arquivo enviroment no Postman:

![Configuração Variáveis de Ambiente](/10%20teste%20em%20APIs%20Rest/asserts/var-ambiente.png)

3. Selecione a collection no Menu Lateral e em seguida clique em Run:

![Configuração Variáveis de Ambiente](/10%20teste%20em%20APIs%20Rest/asserts/run.png)

4. Por fim clique no botão: Run 11 Testes em APIs Rest - Symon Barreto e aguarde o término da execução para visualizar o resultado das validações:  
   ![Configuração Variáveis de Ambiente](/10%20teste%20em%20APIs%20Rest/asserts/runner.png)

## Questão 11: Linux

Para executar o script execute os comandos:

```bash
chmod +x symon-barreto.sh
```

```bash
./symon-barreto.sh
```

### Os testes automatizados foram desenvolvidos e válidados no seguinte ambiente de testes

|                       |                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ambiente de teste** | **Desktop**; **Processador:** Intel(R) Core(TM) i3-10100F CPU @ 3.60GHz; **RAM:** 16 GB DDR4 2400hz; **Armazenamento:** SSD ADATA 240GB; **Video:** NVIDIA GeForce GTX 750; **SO:** Windows 11 |
