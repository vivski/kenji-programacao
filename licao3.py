# Lista 03 - Operadores Lógicos e Relacionais

# Q1. Verificação Básica de Igualdade: Peça ao estudante para escrever
# um programa que compara dois números (por exemplo, 10 e 20)
# usando o operador == e imprime o resultado.

numero1 = int(input("insira um numero (primeiro valor): "));
numero2 = int(input("insira um numero (segundo valor): "));
if numero1 == numero2:
   print("os dois valores são iguais")
else: print("os valores são diferentes")

# Q2. Maior ou Menor?: Solicite a criação de um script que
# compare dois números (como 15 e 30) usando os operadores > e <, 
# imprimindo os resultados dessas comparações.
num1 = int(input("insira um primeiro valor para comparar: "));
num2 = int(input("insira um segundo valor para comparar: "));
if num1 > num2:
    print("o valor é maior")
else: print("o valor é menor")

# Q3. Combinando Operadores Lógicos: Peça para o aluno escrever
# expressões que usem and, or e not com valores booleanos ou comparações diretas
# (por exemplo, True and False, not (5 > 2), (3 < 4) or (5 > 6)), e imprimir os resultados.



# Q4. Identificando Desigualdades: Crie um exercício
# onde o aluno deve usar os operadores != e == para comparar números ou strings, 
# como por exemplo, verificar se 'Python' é igual a 'python' ou se 100 é diferente de 200.
dado1 = (input("digite um valor (numero ou string)"));
dado2 = (input("digite um valor (numero ou string)"));

if dado1 != dado2:
    print("diferente");
elif dado1 == dado2:
    print("igual");


# Q5. Comparando Múltiplos Valores: Proponha que os alunos 
# escrevam um programa que verifica se um número (por exemplo, 5) 
# é menor que 10 e maior que 3, usando operadores relacionais combinados
# com operadores lógicos, e imprima o resultado.

valor1 = int(input("digite um numero"));


if valor1 <= 10 and valor1 >= 3:
    print(f"o numero é menor que 10 e maior que 3");
else:
    print(f"O número não é menor que 10 e nem menor que 3")



