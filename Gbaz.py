#Nome dos integrantes: Maria Sofia, Arthur Menezes e 

from datetime import datetime
from datetime import time

#Data e Horário atual
hoje=datetime.now().date()
abertura_hora=time(hour=7,minute=00)
fechamento_hora=time(hour=19,minute=00)
agora=datetime.now().time()

#Armazenamento de Reservas
livros_reservados=[]
reservas_usuario=[]
lista_reservas=[]

#Acervo de Livros
acervo=['O pequeno principe','O pintor de memórias','O colar da rainha','Biblioteca da meia noite','O Médico e o monstro','A hora da estrela','Dom casmurro','Admirável mundo novo','1984','Assistente do vilão','O gato que amava livros','Eu sou malala','O apanhador no campo de centeio']

#MENU
#1. Função Adicionar Livros:
def adicionar_livros():
    contribuicao=(input("\nDigite o nome do livro que deseja adicionar: ").capitalize())
    if contribuicao in livros_reservados:
        print("\n\033[1;31mNão é possível adicionar um livro que já foi reservado!\033[0m")
    else:
        acervo.append(contribuicao)
        print(f'\nO livro \033[1;32m{contribuicao.capitalize()}\033[0m foi adicionado ao acervo com sucesso!')

#2. Função Remover Livros:
def deletar_livros():
    try:
        remover=(input("\nDigite o nome do livro que você deseja remover: ").capitalize())
        acervo.remove(remover)
        print(f'\nO livro \033[1;32m{remover.capitalize()}\033[0m foi removido do acervo com sucesso!')
    except ValueError:
        print("\n\033[31mEsse livro não está no acervo...\033[0m")

#3. Função de Verificar Acervo:
def verificar_acervo():
    acervo_lista="\n".join(acervo)
    print(f'\n\033[1;38;5;69mEsses são os livros:\033[0m\n{acervo_lista}')
    

#4.Função de Reserva
def fazer_reserva():
    reservar_livro=input("\nDigite o livro que desejar reservar: ").capitalize()
    livros_reservados.append(reservar_livro)

    if reservar_livro in acervo:
        print(f'\n\033[32mO livro {reservar_livro} está disponível!\033[0m')
        while True:
            print(f'\n\033[38;5;215mHorário de disponível para reservas: 07:00 - 19:00\033[0m\n')
            data=input("\033[38;5;173mDigite a data de retirada (DD/MM/AAAA):\033[0m ")
            for formato in ['%d/%m/%Y','%d.%m.%Y','%d-%m-%Y','%d''%m''%Y','%d %m %Y','%d/%m/%y','%d.%m.%y','%d-%m-%y','%d %m %y']:
                try:    
                    data_reserva = datetime.strptime(data, formato)
                    data_string = data_reserva.strftime('%d/%m/%Y')
                    data_formatada=datetime.strptime(data_string, '%d/%m/%Y').date()
                    break
                except ValueError:
                    continue
            
            if data_formatada==hoje and fechamento_hora<agora>abertura_hora:
                print("\n\033[1;31m Reservas de hoje encerradas!\033[0m")
                break
            if data_formatada>=hoje:
                horario=input("\n\033[38;5;173mDigite o horário de retirada (HH:MM):\033[0m ")
                horario_formatado=datetime.strptime(horario, '%H:%M').time()

                if (data_formatada > hoje and fechamento_hora>=horario_formatado>=abertura_hora) or (data_formatada ==hoje and horario_formatado>agora and fechamento_hora>=horario_formatado>=abertura_hora):
                    reservas_usuario.append(veri)
                    lista_reservas.append('\n\033[1;32mLivro: \033[0m'+reservar_livro +'\033[1;32m  Data: \033[0m'+data_string +'\033[1;32m  Horário: \033[0m'+horario +'\033[1;32m  Usuário: \033[0m'+veri.capitalize())
                    print("\n\033[1;32mSeu livro foi reservado com sucesso!\033[0m\n")
                    print(f'A retirada do livro \033[1;32m{reservar_livro}\033[0m foi reservado para \033[1;32m{data_string}\033[0m às \033[1;32m{horario}\033[0m por \033[1;32m{veri.capitalize()}\033[0m')
                    try:
                        acervo.remove(reservar_livro)
                        break
                    except ValueError:
                        print("\033[31mO livro desejado já está reservado :(\033[0m")
                else:
                    print("\033[38;5;160mHorário inválido!\033[0m")
            else:
                print("\n\033[38;5;160mData inválida!\033[0m")
    else:
        print("\033[31mO livro desejado não está disponível :(\033[0m\n")

#5. Função Sair
def sair_menu():
    print("\n\033[32mVolte sempre! 🖐😉\033[0m\n")

#6. Função Verificar Reservas
def verificar_reservas():
    if not lista_reservas:
        print("\n\033[31mNão há reservas :/\033[0m")
    else:
        livros_string="\n".join(lista_reservas)
        print(livros_string)

#7. Função Cancelar Reservas
def cancelar_reservas():
    global lista_reservas
    global reservas_usuario

    if veri in reservas_usuario:
        print("\n\033[1;32mEssas são as suas reservas!:")
        if reservas_usuario:
            lista_usuario = [reserva for reserva in lista_reservas if veri in reserva]
            for reserva in lista_usuario:
                print(reserva)
                cancelamento_livro=input("\nDigite o nome do livro que deseja cancelar a reserva: ").capitalize()
                if cancelamento_livro in livros_reservados:
                    print(f'\nVocê deseja remover a reservar do livro \033[1;32m{cancelamento_livro}\033[0m?\n\033[32m(S) Sim\033[0m   \033[31m(N) Não\033[0m')
                    cancelar=input("\n").upper()
                    if cancelar=="S":
                        lista_reservas=[lista_reservas for lista_reservas in lista_reservas if cancelamento_livro.capitalize() not in lista_reservas]
                        acervo.append(cancelamento_livro)
                        reservas_usuario.remove(veri)
                        print("\n\033[32mReserva cancelada!\033[0m")
                        break
                    else:
                        print("A citada reserva permanece válida!\n")
                        
                else:
                    print("\n\033[31mVocê não reservou esse livro :(\033[0m")
                    break
    else:
        print("\n\033[31mVocê não tem reservas :(\033[0m")
#8. Função Opção Inexiste
def opcao_inexiste():
    print("\n\033[31m❗ Essa opção não existe. ❗\033[0m\n")

#Interação
print("\n\033[35mSeja bem-vindo(a) a nossa biblioteca ^^\033[0m")

####################### LOGIN #########################

while True:
    veri=input("\nVocê é um Cliente ou Administrador?\n\n\033[35mAdministrador - Adm\033[0m\n\033[32mUsuário - Seu Nome\033[0m\n\033[31mLogout - Sair\033[0m\n\n").capitalize()
    if veri=="Sair":
        print("\n\033[35mObrigado pela participação! 🙃\033[0m")
        break
####################### ADMINISTRADOR ########################
    elif veri=="Adm":
        senha=input("Senha: ")
        if senha=="1234":
            print("\n\033[35mSeja Bem-Vindo(a)!\033[0m")
            while True:
                escolha=int(input(f'\n\033[1;38;5;30mEscolha um número de acordo sua necessidade:\033[0m \n 1.Adicionar livro  \n 2.Deletar livro 🗑️ \n 3.Verificar livros 🔎📂 \n 4.Reservar livros 📝\n 5.Verificar reservas 📋 \n 6.Cancelar reserva 📝❌ \n 7.Sair ❌ \n\n'))
                if escolha == 1:
                    adicionar_livros()
                elif escolha == 2:
                    deletar_livros()
                elif escolha == 3:
                    verificar_acervo()
                elif escolha == 4:
                    fazer_reserva()
                elif escolha == 5:
                    verificar_reservas()
                elif escolha ==6:
                    cancelar_reservas()
                elif escolha == 7:
                    sair_menu()
                    break
                else:
                    opcao_inexiste()
        else:
            print("error")

####################### USUÁRIO #########################
    elif veri!='adm':
        while True:
            print(f'\n\033[35mOlá,{veri.capitalize()}\033[0m\n')
            escolha=int(input(f'\033[1;38;5;30mEscolha um número de acordo sua necessidade:\033[0m \n1.Verificar livros 🔎📂 \n2.Reservar livros 📝 \n3.Verificar reservas 📋 \n4.Cancelar reserva 📝❌ \n5.Sair ❌\n\n'))
            if escolha == 1:
                verificar_acervo()
            elif escolha == 2:
                fazer_reserva()
            elif escolha == 3:
                verificar_reservas()    
            elif escolha == 4:
                cancelar_reservas()
            elif escolha == 5:
                sair_menu()
                break
            else:
                opcao_inexiste()