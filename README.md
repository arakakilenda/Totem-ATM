# Projeto de games em Python jogo dos tres copos
# 🥤 Jogo dos Três Copos

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Terminal-1f1f1f)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success)

Jogo de adivinhação para terminal, desenvolvido em **Python**, inspirado no clássico jogo de rua *"Monte de Três Cartas"*. O jogador escolhe um valor secreto, o sistema "embaralha" esse valor entre três copos e o desafio é descobrir em qual deles ele está.

> Projeto acadêmico da disciplina **Programação de Computadores** — Atividade A2.3 (Entrega 02), Tecnologia da Informação, UNICID. Professor: Carlos Weber.

---

## 📑 Sumário

- [Descrição do jogo](#-descrição-do-jogo)
- [Regras](#-regras)
- [Como executar](#-como-executar)
- [Funcionamento do código](#-funcionamento-do-código)
- [Lógica de embaralhamento](#-lógica-de-embaralhamento)
- [Demonstração](#-demonstração)
- [Tecnologias e bibliotecas](#-tecnologias-e-bibliotecas)
- [Integrantes](#-integrantes)
- [Créditos das imagens](#-créditos-das-imagens)

---

## 🎮 Descrição do jogo

O **Jogo dos Três Copos** desafia a percepção e a sorte do usuário:

1. O usuário define um valor secreto (número ou texto).
2. O sistema "embaralha" o valor entre três copos (**C1**, **C2** e **C3**).
3. O jogador tenta adivinhar em qual copo o valor está escondido.

## 📜 Regras

- Existem três copos na mesa: `C1`, `C2` e `C3`.
- O valor escolhido pelo jogador fica escondido em apenas um deles, sorteado aleatoriamente.
- O jogador informa em qual copo acha que o valor está.
- A entrada é validada: só são aceitos `C1`, `C2` ou `C3` (não diferencia maiúsculas de minúsculas).
- Ao final, o jogo revela a situação de todos os copos e informa se o jogador acertou.
- É possível jogar várias vezes seguidas.

> Não há dependências externas: `random` e `time` fazem parte da biblioteca padrão do Python.

## ⚙️ Funcionamento do código

| Recurso | Descrição |
|---|---|
| 🔀 **Aleatoriedade** | A biblioteca `random` sorteia a posição do objeto entre as chaves `C1`, `C2` e `C3`. |
| ⏳ **Suspense** | A biblioteca `time` cria pausas dramáticas, simulando o embaralhamento real. |
| 🔁 **Estrutura** | O jogo roda dentro de um laço `while`, permitindo que o usuário jogue múltiplas vezes. |

## 🧠 Lógica de embaralhamento

A posição do valor é definida por um sorteio simples entre os três copos:

```python
# Sorteio da posição
copo_premiado = random.choice(['C1', 'C2', 'C3'])
```

## 🖥️ Demonstração

### 1. Entrada de dados

O programa solicita ao usuário um valor (string ou número) que será o objeto a ser rastreado.

```text
$ python jogo_copos.py

========================================
   BEM-VINDO AO JOGO DOS TRÊS COPOS
========================================

Temos 3 copos na mesa: C1, C2 e C3.
Escolha um número qualquer para escondermos: 42
```

### 2. Execução do jogo

O jogo valida a entrada, aceitando apenas `C1`, `C2` ou `C3` (*case insensitive*).

```text
Escondendo o número e embaralhando os copos...
[Aguardando 1 segundo...]
Embaralhando mais um pouco...
[Aguardando 1 segundo...]
Pronto!

Em qual copo você acha que o número está? (Digite C1, C2 ou C3): C2
```

### 3. Resultados e verificação

```text
----------------------------------------
             RESULTADO
----------------------------------------

🎉 PARABÉNS! Você acertou em cheio!
O número 42 realmente estava escondido no copo C2.

Situação final dos copos na mesa:
C1: Vazio
C2: 42
C3: Vazio
```

## 🛠️ Tecnologias e bibliotecas

- **Python 3**
- [`random`](https://docs.python.org/3/library/random.html): sorteio da posição do valor escondido.
- [`time`](https://docs.python.org/3/library/time.html): pausas para criar suspense.



## 🖼️ Créditos das imagens

As imagens usadas na apresentação do projeto vêm das seguintes fontes:

- [coolhunting.com](https://coolhunting.com)
- [vectorstock.com](https://www.vectorstock.com)
- [istockphoto.com](https://www.istockphoto.com)
- [kombikeg.com](https://www.kombikeg.com)

---

📫 Dúvidas? Abra uma *issue* neste repositório.
