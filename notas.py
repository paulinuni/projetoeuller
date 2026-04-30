def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 2
    return media

def verificar_aprovacao(media):
    if media >= 6
        print("Aluno aprovado")
    elif media >= 4:
        print("Recuperação")
    else
        print("Reprovado")

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")

media = calcular_media(nota1, nota2, nota3)

verificar_aprovacao

# Erros identificados em notas.py
# calcular_media está dividindo por 2 em vez de 3

# Causa: média de três notas deve ser (n1 + n2 + n3) / 3
# Correção: usar 3 no denominador
# Sintaxe inválida em verificar_aprovacao

# if media >= 6 está sem :
# else está sem :
# Essas faltas causam erro de sintaxe e o programa não roda
# Chamada de função incorreta no final

# verificar_aprovacao está escrito sem parênteses e sem o argumento media
# Deve ser verificar_aprovacao(media)
# As notas lidas com input(...) são strings

# Causa: input retorna texto, então n1 + n2 + n3 concatena strings
# Correção: converter para float ou int

