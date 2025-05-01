
#Nome dos integrantes: Maria Sofia, Arthur Menezes e Francisca Gabrielly

import datetime
acervo=['pequeno principe','o pintor de memórias','o colar da rainha', 'biblioteca da meia noite',' medico e o monstro','a hora da estrela','dom casmurro','admiravel mundo novo','1984','assistente do vilão','o gato que amava livros','eu sou Malala','o apanhador no campo de centeio']
   
print("Seja bem vindo a nossa biblioteca ^^")
while True:
    veri=input("voce é um usuário ou um ADM? caso queira sair digite 'sair': ")
    if veri=="sair":
        print("obrigado pela participacao!")
        break
    elif veri=="adm":
        senha=input("digite sua senha: ")
        if senha=="1234":
            print("seja bem vindo!")
            while True:
                escolha=int(input("\nEscolha um número de acordo com o que vc deseja: \n 1.adicionar livro \n 2.deletar livro \n 3.verificar livros \n 4.reservar livros \n 5.sair"))
                if escolha == 1:
                    acervo.append(input("Digite o nome do livro que deseja adicionar: ").lower())
                    print("livro adicionado com sucesso!")
                elif escolha == 2:
                    try:
                        acervo.remove(input("Digite o nome do livro que você deseja remover: ").lower())
                        print("livro removido com sucesso!")
                    except ValueError:
                        print("Esse livro NÃO existe...  ")
                elif escolha == 3:
                    print("esses são os livros: ",acervo ,"")
                elif escolha == 4:
                    reservar_livro=input("Digite o livro que desejar reservar:  ")
                    if reservar_livro in acervo:
                        print("O livro "+ reservar_livro +" está disponível!")
                        data=input("Digite a data da reserva (DD/MM/YYYY): ")
                        horario=input("Digite o horário da reserva(HH:MM): ")
                        print("O livro"+reservar_livro+" estará disponível para a data "+data+" às "+horario)
                    elif reservar_livro not in acervo:
                        print("O livro desejado não está disponível :(")
                elif escolha == 5:
                    print("volte sempre!")
                    break
                else:
                    print("Essa opção não existe")
        else:
            print("error")
    elif veri=="usuario":
        while True:
            escolha=int(input("\nEscolha um número de acordo com o que vc deseja: \n 1.verificar livros \n 2.reservar livros \n 3.sair "))
            if escolha == 1:
                print("esses são os livros: ",acervo )
            elif escolha==3:
                print("volte sempre!")
                break
            elif escolha == 2:
                reservar_livro=input("Digite o livro que desejar reservar:  ")
                if reservar_livro in acervo:
                    print("O livro "+ reservar_livro +" está disponível!")
                    data=input("Digite a data da reserva (DD/MM/YYYY): ")
                    horario=input("Digite o horário da reserva(HH:MM): ")
                    print("O livro "+reservar_livro+" estará disponível para a data "+data+" às "+horario)
                else:
                    print("O livro desejado não está disponível :(")
            