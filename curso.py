while True:
    senha = input("Digite a senha secreta: ")
    
    if senha == "1234":
        print("Acesso liberado!")
        break  # Encerra o laço imediatamente
        
    print("Senha incorreta. Tente novamente.\n")

print("Bem-vindo ao sistema!")
