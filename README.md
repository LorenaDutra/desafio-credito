
# Desafio  - Lorena Dutra
## O problema
Elaborar uma solução que ofereça armazenamento, processamento e disponibilização de dados.
## Armazenamento
### Base A - é extremamente sensível e deve ser protegida com os maiores níveis de segurança, mas o acesso a esses dados não precisa ser tão performática. 
Iniciei a resolução deste problema definindo quais bases de dados usaria.
Para a Base A escolhi o PostgreSQL, pois oferece vários níveis de segurança.
#### Detalhes de acesso a base
Esta base só pode ser acessada por micro-serviços e nano-serviços já cadastrados e não conceder permissões desnecessárias.
Deve conter autenticação e criptografia.
Os desenvolvedores não devem possuir acesso total a base de dados A e apenas as aplicações que as consomem devem possuir esse acesso, que deve ser monitorado e de conter proteção de SQL Injection e Web shell .
Normas de segurança - [ISO/IEC 27000]
### Base B - também possui dados críticos, mas ao contrário da Base A, o acesso precisa ser um pouco mais rápido. Uma outra característica da Base B é que além de consultas ela é utilizada para extração de dados por meio de algoritmos de aprendizado de máquina.
Para a Base B a base escolhida foi MySQL, pois além de possuir níveis de segurança é mais rápida que o PostgreSQL.
### Base C - que não possui nenhum tipo de dado crítico, mas precisa de um acesso extremamente rápido.
Para o caso da Base C, escolhi o MongoDB pois precisa de acesso mais rápido que as outras bases e não requer um grau de segurança elevado.

## Tráfego
Cada uma das bases existentes, são acessadas por sistemas em duas diferentes arquiteturas: micro-serviços e nano-serviços. 
O primeiro sistema, acessa os seguintes dados da Base A:
• CPF
• Nome
• Endereço
• Lista de dívidas

O segundo, acessa a Base B que contém dados para cálculo do Score de Crédito. O Score de Crédito é um rating utilizado por instituições de crédito (bancos, imobiliárias, etc) quando precisam analisar o risco envolvido em uma operação de crédito a uma entidade.

• Idade
• Lista de bens (Imóveis, etc)
• Endereço
• Fonte de renda

O último serviço, acessa a Base C e tem como principal funcionalidade, rastrear eventos relacionados a um determinado CPF.

• Última consulta do CPF em um Bureau de crédito (Serasa e outros).
• Movimentação financeira nesse CPF.
• Dados relacionados a última compra com cartão de crédito vinculado ao CPF.

No cenário de micros serviços, cada serviço possui suas próprias ações sequenciais necessárias para a implantação (testes, compilação, provisionamento de infraestrutura etc.) que são executadas de forma automática e independentes.
Facilita as tarefas de alterar, substituir e adicionar novos componentes de forma mais simples.
Quando é feita uma mudança na aplicação é necessário apenas que o componente modificado seja reimplantando. Isso simplifica e acelera o processo de implantação.
Em um sistema composto por múltiplos serviços, cada um pode ser desenvolvido em diferentes tecnologias. Com isso, se um componente do sistema falhar, esta falha não causará efeito cascata. O problema será isolado e o resto do sistema continuará trabalhando sem esta funcionalidade.
Ajudam a diminuir a quantidade de pessoas trabalhando em uma mesma base de código, combinando tamanho de equipe ideal com produtividade.
### Serviço A
O serviço A acessa a base de dados A e realiza as autenticações. Dessa maneira cria-se uma camada de abstração para que a aplicação web apenas consuma essas informações sem ter que lidar com gerenciamento do tráfego e com questões de segurança.

### Serviço B
O serviço B consume os dados da base B para realizar o cálculo do Score de crédito. Fornecendo apenas o ultimo para a camada da aplicação, por que é o de interesse. 
O cálculo do Score deverá ser realizado por uma lib externa, para simular a proteção do conhecimento necessário para realizar essa operação. Para entregar a informação do score de maneira otimizada uma cache será utilizada, para o desenvolvimento desse cache será utilizado o Redis.

### Serviço C
O micro serviço C deve ser capaz de condensar todas as informações referentes a um CPF em um único payload para que seja consumido pela camada da aplicação.

## Disponibilização dos Dados
Agora que os dados desejados já foram consumidos, processados e armazenados, é necessário que eles sejam disponibilizados. Será necessário também desenvolver um meio pelo qual esses dados estarão disponíveis. É interessante imaginar os possíveis interessados em consumir esses dados para que uma única solução possa ser construída de modo a atender o máximo de situações possíveis.
Para a disponibilização dos dados foi escolhido o framework javascript - React. Fácil de usar e tem suporte à reusabilidade de componentes.

## Arquitetura de micro serviços proposta

![Arquitetura](https://github.com/LorenaDutra/desafiocredito/blob/master/images/arquitetura.svg)


### Desenvolvimento

#### Criação das bases de dados em docker compose
#### Desenvolvimento das rest apis em flask
#### Front end em React basico

## Como executar o projeto
### Inicializando as Bases

Para inicializar as bases de dados deve-se executar o serviço db-admin.
```
docker-compose run db-admin
```
Com os containers das bases levantados deve-se executar um procedimento na base B (MySql) para alterar o modo de autenticação de usuarios. Para isso o procedimento se encontra em /score_calculator/base_b/mysql-auth-method.query 

```
# Entrando no container da Base B
docker-compose exec mysql /bin/bash

# Entrando no console do MySql
mysql -u root -p

# Executando alteração do modo de autenticação
ALTER USER 'bureau'@'%' IDENTIFIED WITH mysql_native_password BY 'bureau';
```
Esse processedimento só precisa ser executado uma vez (a não ser que o volume seja removido). Após isso no serviço do db-admin basta executar o script de inicialização/povoamento das bases.
Obs: Um csv com cpfs e endereços presentes nas bases será criado.

```
/app# python db_admin.py
/app# cat people.csv
```

### Executando o projeto

Para executar o projeto, basta ter o `docker` o `docker-compose` instalados e executar o `up`

```
docker-compose up
```
ou docker run caso queira executar apenas um micro serviço:
```
docker-compose run -p 5000:5000 social-id-fetcher
```
### Endpoints e Payloads

#### Micro serviço A

* Endpoint: `http://localhost:5000/person/<cpf>`

```python
payload = {
    'cpf': String,
    'name': String,
    'address': String,
    'dividas': [{
        'company': String,
        'value': Inteiro,
        'status': String,
        'contract': Inteiro
    }]
}
```

#### Micro serviço B

* Endpoint: `http://localhost:5050/score/<cpf>`

```python
payload = {
    'cpf': String,
    'score': Inteiro,
    'age': Inteiro,
    'address': String,
    'assets': [{
        'name': String,
        'value': Inteiro
    }]
}
```

#### Micro serviço C

* Endpoint: `http://localhost:5055/trail/<cpf>`

```python
payload = {
    'cpf': String,
    'last_query': Data,
    'last_purchase': {
        'company': String,
        'date': Data,
        'value': Float,
    },
    'transactions': [{
        'date': Data,
        'value': Float
    }]
}
```




