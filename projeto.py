#Nome dos integrantes: Maria Sofia, Arthur Menezes e Francisca Gabrielly
import datetime


reservas = {}

# Lista de livros que escolhemos baseado no que nós gostamosw
acervo = [
    'O pequeno principe', 'O pintor de memórias', 'O colar da rainha', 'Biblioteca da meia noite',
    'A Culpa é das estrelas', 'A hora da estrela', 'Dom casmurro', 'Admirável mundo novo',
    'Assistente do vilão', 'O gato que amava livro', 'Eu sou Malala', 'O apanhador no campo de centeio',
    'Conversa de Bicho', 'Verity', 'A dança dos dragões', 'Radio Silencio', 'Os dois morrem no final',
    'Azul é a cor mais quente', 'Salve-me', 'A menina que roubava livros', 'Eu te darei o SOL',
    'Fica entre a gente', 'Todas as suas imperfeições'
]

#funcoes  
def verificar():
    acervo.sort()
    print("\033[1;32mLivros disponíveis no \033[1;35macervo\033[1;32m 🗂️📚:\033[0m")
    for livro in acervo:
        print(livro)
    return acervo



def reservar():
    acervo = verificar()
    livro_reservado = input("\033[1;33mDigite o nome do \033[1;32mlivro\033[1;33m que você deseja \033[1;35mreservar\033[1;33m 📖💖 : \033[0m") 

    if livro_reservado not in acervo:
        print(f"\033[1;33mO livro '\033[1;35m{livro_reservado}\033[1;33m' \033[1;31mnão está disponível\033[1;33m na \033[1;32mbiblioteca\033[0m.")
    elif livro_reservado in reservas:
        print(f"Esse livro '{livro_reservado}' já foi reservado!📚📆")
    else:
        # Obter o horário atual
        horario_reserva = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reservas[livro_reservado] = horario_reserva
        print(f"\033[33mVocê reservou o livro:\033[0m '\033[32m{livro_reservado}\033[0m' \033[33màs\033[0m \033[32m{horario_reserva} !\033[0m")



def cancelar():
    acervo = verificar()
    livro_cancelado = input("\033[1;33mDigite o nome do \033[1;32mlivro\033[1;33m que você \033[1;31mdeseja cancelar\033[1;33m a reserva 📕🚨 : \033[0m") 

    if livro_cancelado not in acervo:
        print(f"\033[31mO livro '\033[0m\033[31m{livro_cancelado}\033[0m\033[31m' não está disponível na biblioteca. Tente novamente ‼️\033[0m")
    elif livro_cancelado in reservas:
        del reservas[livro_cancelado]
        print(f"\033[33mA reserva do livro '\033[31m{livro_cancelado}\033[33m' foi \033[32mcancelada !\033[33m.\033[0m")
    else:
        print(f"\033[33mOps! Esse livro '\033[31m{livro_cancelado}\033[33m' \033[35mnão está reservado\033[33m!👾\033[0m")



def adicionar():
    novo_livro = input("\033[1;33mDigite o nome do \033[1;32mlivro\033[1;33m que deseja \033[1;35madicionar\033[1;33m 📔🎉😊 : \033[0m")
    acervo.append(novo_livro)
    print(f"\033[1;33mO livro '\033[1;32m{novo_livro}\033[1;33m' foi \033[1;35madicionado\033[1;33m ao acervo 📖🎁 !\033[0m")



def remover():
    livro_remover = input("\033[1;33mDigite o nome do livro que\033[0m \033[1;31mdeseja remover\033[0m\033[1;33m 📖❌ :  \033[0m")
    if livro_remover in acervo:
        acervo.remove(livro_remover)
        print(f"\033[1;33mO livro\033[0m \033[1;31m'{livro_remover}'\033[0m \033[1;32mfoi removido do acervo 📂😉.\033[0m")
    else:
        print(f"O livro '\033[1;38;5;208m{livro_remover}\033[0m' \033[1;31mnão\033[0m \033[1;33mestá reservado no acervo.📂❌ \033[0m")



# Função de sair do sistema
def sair():

    print("\033[1;33mObrigado pela participação!\033[0m")  
    print("\n\033[32mVolte sempre! 🖐😉\033[0m\n") 
    

# verificacao
def autenticar():
    TipoUsuario = input("\n 🔒 Você é um \033[1;33musuário\033[0m ou \033[38;5;208madministrador\033[0m?\n(Digite \033[1;35m1 para usuário\033[0m e \033[38;5;208m2 para adm\033[0m): ")

    
    if TipoUsuario == "1":
        nome_usuario = input("Digite seu nome: ")
        print(f"Bem-vindo, {nome_usuario}!")
        return "usuario"
    
    elif TipoUsuario == "2":
        tentativa = 0
        while True:
            senha = input("Digite sua senha 🔒: ")
            if senha == "1234":
               print("\033[1;32mAcesso liberado 🔓\033[0m\033[1;33m, seja bem-vindo 😉 \033[0m")
               return "adm"
            elif tentativa>=2:
               print("\033[1;31mVocê atingiu o limite de tentativas !\033[0m")

               return autenticar()
            else:
                tentativa += 1
                print("\033[1;31mSenha incorreta. Tente novamente 🔒.\033[0m")


#interface 
TipoUsuario = autenticar()

while True:
    print("\n\033[1;35mMenu da\033[0m \033[1;32mBiblioteca 📚💚\033[0m:")
    print("1. Verificar acervo 🔎📂")
    print("2. Reservar livro 📚🗃️")
    print("3. Cancelar reserva 📝❌")
    print("4. Sair 📂🔚 ")
    if TipoUsuario == "adm":
        print("5. Adicionar livro 📚⭐")
        print("6. Remover livro 📖❌")
    opcao=input("escolha uma das opcoes: ")
    if opcao == "1":
        verificar()
    elif opcao == "2":
        reservar()
    elif opcao == "3":
        cancelar()
    elif opcao == "5" and TipoUsuario == "adm":
        adicionar()
    elif opcao == "6" and TipoUsuario == "adm":
        remover()
    elif opcao == "4":
        break
    else:
        print("\033[1;31mOpção inválida\033[0m. \033[38;5;208mTente novamente 🔴🟠 .\033[0m")

#Obrigada pela atenção e pela oportunidade de apresentar nossa mini reserva! 🙏🏼📚💚
#equipe: Maria Sofia,Francisca Gabrielly e Arthur Menezes ! 📚⭐
