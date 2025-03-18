import time

# pedindo ao usuário uma lista de nomes
nomes = input("Digite o nome dos contatos: ")
nomes = [nome.strip() for nome in nomes.split(",")]

# criando uma mensagem personalizada
mensagem = "Olá {}, como você está se sentindo hoje?"

# exibir mensagem com um pequeno intervalo entre os envios
for nome in nomes:
    print(f"Enviando mensagens para {nome}...")
    print(mensagem.format(nome))
    time.sleep(3)  #aguardar 3 segundos antes de enviar a proxima mensagem
    print()
