senha = input("Digite uma senha: ")

if senha == "12345678":
    print("Senha inválida.")
elif len(senha) < 8:
    print("A senha deve conter pelo menos 8 caracteres.")
else:
    print("Senha válida.")
