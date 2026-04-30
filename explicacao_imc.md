# Explicação do Código de IMC

Este arquivo descreve o funcionamento do programa `nome.py`, que calcula o Índice de Massa Corporal (IMC) a partir do peso e da altura informados pelo usuário.

## Como funciona

1. O programa define duas funções principais:
   - `calcular_imc(peso_kg, altura_m)`: calcula o IMC usando a fórmula `peso / altura^2`.
   - `classificar_imc(imc)`: classifica o resultado do IMC nas categorias:
     - Abaixo do peso
     - Peso normal
     - Sobrepeso
     - Obesidade

2. No bloco `if __name__ == "__main__":` o programa solicita ao usuário:
   - Peso em quilogramas
   - Altura em metros

3. Depois de receber a entrada, o programa:
   - converte os valores digitados para `float`
   - calcula o IMC chamando `calcular_imc`
   - produz a classificação chamada `classificar_imc`
   - exibe o IMC com duas casas decimais
   - exibe a classificação correspondente

## Validação de entrada

O código verifica se a altura é maior que zero. Se o usuário informar um valor inválido (por exemplo, texto ou altura igual a zero), o programa captura a exceção `ValueError` e mostra uma mensagem de erro com o motivo.

## Exemplo de uso

```bash
python nome.py
```

Quando executado, o programa pode solicitar:

```text
Digite seu peso em kg: 70
Digite sua altura em metros (por exemplo, 1.75): 1.75
```

E então exibe:

```text
Seu IMC é: 22.86
Classificação: Peso normal
```

## Fórmula do IMC

A fórmula utilizada é:

```python
imc = peso_kg / (altura_m ** 2)
```

Onde:
- `peso_kg` é o peso do usuário em quilogramas
- `altura_m` é a altura em metros

## Objetivo

O objetivo do programa é demonstrar como ler dados do usuário, fazer cálculos simples em Python e apresentar resultados de forma clara.
