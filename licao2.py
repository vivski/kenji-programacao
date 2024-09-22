# Q1. Escreva 5 exemplos de identificadores válidos e 5 exemplos de identificadores inválidos. 
#validos:
# nome 
# _idade
# numero1
# velocidade_maxima
# dados_usuario

#invalidos:
# 1numero (não pode começar com um número)
# @nome (não pode conter caracteres especiais como @)
# nome-idade (não pode conter hífens, pode separar com underscore _)
# class (palavra reservada em Python)
# velocidade máxima (não pode conter espaços em branco)

# Q2. Supondo que as variáveis nome_aluno, nota_aluno, matricula_aluno, 
# genero_aluno, idade_aluno sejam utilizadas para armazenar o nome do aluno, 
# a nota na disciplina, o número de matrícula, o gênero, e a idade. 
# Qual o tipo que cada variável deve possuir para armazenar o valor adequado?

nome_aluno = ""        # tipo: str
nota_aluno = 0.0       # tipo: float (ou int se for apenas números inteiros)
matricula_aluno = 0    # tipo: int
genero_aluno = ""      # Tipo: str
idade_aluno = 0        # Tipo: int


# Q3.  Faça um programa que leia o nome de uma pessoa e a sua idade. 
# Imprima uma mensagem que diga "Olá, [nome].
# Você terá  [idade] anos daqui a 10 anos". 
# Os dados de entrada devem ser armazenados em variáveis distintas.

nome = input(" digite seu nome ");
idade = int(input(" digite sua idade "));
print("Olá ", nome, " Você terá a idade: ", idade+10, " anos daqui a 10 anos.");

# Q4. Escreva um algoritmo que leia o nome de uma pessoa, o ano em que ela nasceu. 
# Em seguida imprima uma mensagem que diga "Olá, [nome], hoje você tem [idade] anos". 
# Considere que os dados de entrada devem ser armazenados em variáveis distintas, 
# e o cálculo da idade deve se basear no ano atual.

nomepessoa = input(" digite seu nome ");
anonascimento = int(input(" digite o ano de nascimento "));

idade = 2024 - anonascimento;
print("Olá ", nomepessoa, " sua idade atual é: ", idade);

# Q5. Escreva um algoritmo que leia a nota de 3 
# estudantes e retorne a média das notas.

aluno1 = float(input("digite a nota do aluno 1: "));
aluno2 = float(input("digite a nota do aluno 2: "));
aluno3 = float(input("digite a nota do aluno 3: "));

medias = (aluno1+aluno2+aluno3)/3;
media_arredondada = round(medias,2)

print("A média é ", media_arredondada);

# Q6. Escreva um algoritmo que solicita ao usuário uma quantidade
# de tempo em segundos e então a converte para
# horas. Por exemplo, se o usuário inserir 
# 3666 segundos, o programa deve imprimir 
# "1 hora", sem considerar os segundos restantes.
segundos = int(input(" digite a quantidade de tempo em segundos "));
horas = segundos//3600
print("os ", segundos, " equivalem a ", horas , 'hora(s)')


# Q7. Escreva um algoritmo que solicita ao usuário uma temperatura
# em graus Celsius e a converte para graus Fahrenheit e Kelvin. 
# Use as fórmulas Fahrenheit = Celsius * 1.8 + 32 e 
# Kelvin = Celsius + 273.15 para realizar as conversões.
temp = int(input(" digite a temperatura em celsius "));
tempf = temp * 1.8 + 32;
tempk = temp + 273.15
print("a temperatura de celsius para graus Fahrenheit é: ", tempf, "°F. ", " e a temperatura de celsius para kelvin é: ", tempk, "K. ")


# Q8. Área de um Retângulo: Escreva um algoritmo que solicita ao usuário a 
# largura e o comprimento de um retângulo,
# depois calcula e exibe a área do retângulo. A fórmula para calcular 
# a área de um retângulo é área = largura x comprimento.

largura = int(input(" digite a largura do retangulo "));
comprimento = int(input(" digite o comprimento do retangulo "));
arearetangulo = largura * comprimento;
print("a área do retangulo é: ", arearetangulo)


# Q9. Área de um Círculo: Escreva um algoritmo que solicita ao usuário o raio de um círculo, 
# depois calcula e exibe a área do círculo. A fórmula para calcular a área de um círculo
# é área = π x raio^2. Você pode usar a aproximação de 3.1416 para π.
raiocirculo = float(input(" digite o raio do circulo "));
area = 3.1416* (raiocirculo**2)
print("A área do círculo é: {:.2f}".format(area))


# Q10. Área de um Triângulo: Escreva um algoritmo que solicita ao usuário a
# base e a altura de um triângulo, depois calcula e exibe a área do triângulo. 
# A fórmula para calcular a área de um triângulo é: área = (base x altura) / 2.
base = int(input(" digite a base do triangulo "));
altura = int(input(" digite a altura do triangulo "));
areatriangulo = (base*altura)/2;
print("a área do triangulo é: ", areatriangulo)







