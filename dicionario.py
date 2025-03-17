    
produto = {
    'Nome': ['Feijão','Arroz','Farinha'],
    'Quantidade': [10, 10, 100],
    'preco' : [10, 20, 30]
}

for nome, quantidade, preco in zip(produto['Nome'], produto['Quantidade'], produto['preco']):
    print(f'Nome: {nome}, Quantidade: {quantidade}, Preço: {preco}')
    