# Q6. Elabore um algoritmo para representar um sistema de 
# compra de produtos agrícolas de uma feira, mas que só permite compras à vista.

print("Bem-vindo(a) a nossa loja de produtos agrícolas!")
print("O sistema só permite comprar uma unidade de cada produto e a única forma de pagamento é à vista.")
print("PRODUTOS DISPONÍVEIS NO SISTEMA: ")

class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def __str__(self):
        return f"ID: {self.id}, Produto: {self.nome}, Preço: R$ {self.preco}, Quantidade: {self.quantidade}"


produtos = [
    Produto(1, "laranja", 20, 1),
    Produto(2, "Cacau", 30, 1),
    Produto(3, "feijão", 8, 1),
    Produto(4, "beterraba", 7, 1),
    Produto(5, "café", 30, 1),
    Produto(6, "cereal", 15, 1),
    Produto(7, "milho", 10, 1),
    Produto(8, "batata inglesa", 8, 1),
    Produto(9, "batata doce", 5, 1),
    Produto(10, "soja", 20, 1)
]

for produto in produtos:
    print(produto)

print("Faça o login no sistema para realizar seu pedido")
usuarionome = input("Digite o seu nome: ")
usuariosenha = input("Digite a senha: ")
confirmarsenha = input("Confirmar senha: ")
quantidadeitens = int(input("Quantidade de itens que deseja levar (até 10 itens, 1 unidade de cada): "))

if quantidadeitens > 10:
    print("Você pode levar no máximo 10 itens.")
else:
    listacompras = []
    valorTotal = 0
    
    for _ in range(quantidadeitens):
        pedido = input("Digite o nome ou o ID do produto: ")
        
        produto_encontrado = None
        if pedido.isdigit():
            produto_encontrado = next((produto for produto in produtos if produto.id == int(pedido)), None)
        else:
            produto_encontrado = next((produto for produto in produtos if produto.nome.lower() == pedido.lower()), None)
        
        if produto_encontrado:
            listacompras.append(produto_encontrado.id)
            valorTotal += produto_encontrado.preco
        else:
            print("Produto inválido. Tente novamente.")
    
    print(f"RESUMO DO SEU PEDIDO: ")
    for id_produto in listacompras:
        produto_selecionado = next(produto for produto in produtos if produto.id == id_produto)
        print(f"{produto_selecionado}")

    print(f"O VALOR DA SUA COMPRA É: R$ {valorTotal:.2f}")
    
    formapagamento = input("Como deseja pagar? (Digite 'à vista' para confirmar): ")
    if formapagamento.lower() == "à vista":
        print(f"Obrigado, {usuarionome}, compra feita com sucesso!")
    else:
        print(f"Sinto muito, {usuarionome}, sua compra não pode ser feita e seus dados serão descartados pelo sistema.")
