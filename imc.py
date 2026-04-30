def calcular_imc(peso_kg: float, altura_m: float) -> float:
    """Retorna o IMC a partir do peso em kg e altura em metros."""
    if altura_m <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso_kg / (altura_m ** 2)


def classificar_imc(imc: float) -> str:
    """Classifica o IMC conforme a tabela padrão."""
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


if __name__ == "__main__":
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros (por exemplo, 1.75): "))
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
