senhaCerta = "xeriff"

for i in range(3):
    senha = input("Digite a senha: ")

    if senha == senhaCerta:
        print("Acesso Permitido")
        break
else:
    print("Conta Bloqueada")
 