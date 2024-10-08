def salvar_contato(agenda_contatos, nome, tel, email):
    contato = {"nome": nome,"tel": tel, "email": email, "favorito": False}
    agenda_contatos.append(contato)
    print(f"Contato '{nome}' salvo na agenda")
    return

def ver_lista_contatos(agenda_contatos):
    print("\nLista de contatos")
    for indice, contato in enumerate(agenda_contatos, start=1):
        status = "★" if contato["favorito"] else "☆"
        nome = contato["nome"]
        tel = contato["tel"]
        email = contato["email"]
        print(f"{indice}º Contato:\n{status} {nome}\nTel/Cel: {tel}\nE-mail: {email}")
    return

def editar_contato(agenda_contatos, indice_contato, novo_contato):
    indice_contato_atualizado = int(indice_contato) - 1
    agenda_contatos[indice_contato_atualizado] = novo_contato
    print(f"Contato {indice_contato} atualizado para {novo_contato["nome"]}")
    return

def marcar_desmarcar_favorito(agenda_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if agenda_contatos[indice_contato_ajustado]["favorito"] == False:
        agenda_contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {agenda_contatos[indice_contato_ajustado]["nome"]} marcado como favorito\nSalvo na lista CONTATOS FAVORITOS")
    else:
        agenda_contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {agenda_contatos[indice_contato_ajustado]["nome"]} desmarcado como favorito\nDeletado da lista CONTATOS FAVORITOS")
    return

def ver_lista_favoritos(agenda_contatos):
    favoritos = []
    for contato in agenda_contatos:
        if contato["favorito"]:
            favoritos.append(contato)
    print("FAVORITOS", end='')
    return ver_lista_contatos(favoritos)

# RESOLVER def deletar_contato
def deletar_contato(agenda_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1 
    print(f"{agenda_contatos[indice_contato_ajustado]["nome"]} foi DELETADO")
    agenda_contatos.pop(indice_contato_ajustado)
    return

agenda_contatos = []
while True:
    print("\nAGENDA DE CONTATOS")
    print("1. Salvar novo contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Deletar contato")
    print("7. Fechar agenda de contatos")

    opção = input("\nEscolha uma opção: ")


    if opção == "1":
        print("Informe os dados do contato:")
        nome = input("Nome: ")
        tel = input("Tel/Cel(ddd): ")
        email = input("E-mail: ")
        salvar_contato(agenda_contatos, nome, tel, email)
    
    elif opção == "2":
        ver_lista_contatos(agenda_contatos)

    elif opção == "3":
        ver_lista_contatos(agenda_contatos)
        indice_contato = input("\nDigite o indice do contato que deseja atualizar: ")
        novo_nome = input("Nome: ")
        novo_tel = input("Tel/Cel(ddd): ")
        novo_email = input("E-mail: ")
        novo_contato = {"nome": novo_nome, "tel": novo_tel, "email": novo_email, "favorito": False}
        editar_contato(agenda_contatos, indice_contato, novo_contato)

    elif opção == "4":
        ver_lista_contatos(agenda_contatos)
        print("\nMarcar/Desmarcar favorito")
        indice_contato = input("Digite o indice do contato: ")
        marcar_desmarcar_favorito(agenda_contatos, indice_contato)

    elif opção == "5":
        ver_lista_favoritos(agenda_contatos)

    elif opção == "6":
        print("\nDeletar Contato")
        ver_lista_contatos(agenda_contatos)
        indice_contato = int(input("Digite o indice do contato: "))
        deletar_contato(agenda_contatos, indice_contato)

    elif opção == "7":
        break

    else:
        print("Opção invalida. Por favor, digite a opção correta")
print("AGENDA FECHADA. Inicie o programa para abrir agenda!")
