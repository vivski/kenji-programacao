# Q7. Elabore um algoritmo para representar um sistema de compra
# de produtos agrícolas de uma feira, mas que só permite realizar
# a compra, se a pessoa tiver dinheiro para pagar à vista e se estiver
# com a anuidade de associação de produtor rural em dia. 


print("Bem-vindo(a) a nossa loja de produtos agrícolas!")
print("O sistema só permite comprar uma unidade de cada produto e a única forma de pagamento é à vista.")
print("PRODUTOS DISPONÍVEIS NO SISTEMA:")

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"ID: {self.id}, Produto: {self.nome}, Preço: R$ {self.preco}"

produtos = [
    Produto(1, "laranja", 20),
    Produto(2, "Cacau", 30),
    Produto(3, "feijão", 8),
    Produto(4, "beterraba", 7),
    Produto(5, "café", 30),
    Produto(6, "cereal", 15),
    Produto(7, "milho", 10),
    Produto(8, "batata inglesa", 8),
    Produto(9, "batata doce", 5),
    Produto(10, "soja", 20)
]

for produto in produtos:
    print(produto)

nome_usuario = input("Digite o seu nome: ")
quantidadeitens = int(input("Quantos itens deseja levar? (até 10 itens): "))

if quantidadeitens > 10:
    print("Você pode levar no máximo 10 itens.")
else:
    listacompras = []
    valorTotal = 0


    for i in range(quantidadeitens):
        pedido = int(input("Digite o ID do produto: "))
        for produto in produtos:
            if produto.id == pedido:
                listacompras.append(produto)
                valorTotal += produto.preco
                break

    print("\nRESUMO DO SEU PEDIDO:")
    for produto in listacompras:
        print(produto)

    print(f"Valor total da compra: R$ {valorTotal}")

    pagamento = input("Pagamento à vista? (Digite 'sim' para confirmar): ").lower()
    if pagamento == "sim":
        print(f"Obrigado pela compra, {nome_usuario}!")
    else:
        print("Compra não pode ser realizada. Somente pagamento à vista.")
