import random

def reservar (reserva,ID,nome, ultimo, show, data, hora, lugar,preco):

    utilizador = {"ID": ID, 'nome': nome , 'ultimo_nome': ultimo, "show": show, "data": data, "hora": hora, "lugar": lugar, "preco":preco}
    reserva.append(utilizador)
    return reserva

def ID (reservas):

    existente = []

    for i in reservas:
        existente.append(i["ID"])

    ID = random.randint(1, 1000)

    while ID in existente:
        ID = random.randint(1, 1000)

    return ID

def search_id(reserva,ID):
    for n in reserva:
        if ID == n["ID"]:
            return n
    return False

def alterar(reserva,id,hora,data, letra, numero):

    for bilhete in reserva:
        if id == bilhete["ID"]:
            break
        
    bilhete["hora"] = hora
    bilhete["data"] = data
    bilhete["lugar"] = letra + numero
    bilhete["preco"] = price(letra,numero)

    return reserva

def price (letra,numero):

    if letra in ['A', 'F'] and numero in ['6','7','8','9']:
        preco = 12.00
    else:
        preco = 4.00

    return preco

def eliminar(reserva,id):

    for bilhete in reserva:
        if id == bilhete["ID"]:
            break

    reserva.remove(bilhete)
    return reserva

def verify_assento(reserva,show,data,hora):

    assentos = []

    for n in reserva:
        if show == n["show"] and data == n["data"] and hora == n["hora"]:
            assentos.append(n["lugar"])

    return assentos

def esconder(window,estado):

    window["txt_ID"].update(visible = estado)
    window["ID"].update(visible = estado, value = "")
    window["pesquisar"].update(visible = estado)

def esconder_2(window,estado,estado_2):
    window["Continuar"].update(visible = estado)
    window["Voltar"].update(visible = estado)
    window["voltar_2"].update(visible = estado_2)
    window["alterar"].update(visible = estado_2)

def atualizar_cartaz(cartazes, show):

    for n in cartazes:
        if n["nome"] == show:
            break

    return {"data":n["data"],"hora":n["hora"]}

def calcular_dia (reserva, data):

    bilheteria = 0 

    for n in reserva:
        if n["data"] == data:
            bilheteria += n["preco"]

    return bilheteria

def calcular_mes (reserva, data):

    bilheteria = 0 

    for n in reserva:
        if n["data"][1] == data[0] and n["data"][2] == data[1]:
            bilheteria += n["preco"]

    return bilheteria

def calcular_ano (reserva, data):

    bilheteria = 0 

    for n in reserva:
        if n["data"][2] == data:
            bilheteria += n["preco"]

    return bilheteria