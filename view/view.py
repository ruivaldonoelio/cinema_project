import PySimpleGUI as pg
from view.layout import *
from view.palco import *
from controller.controller import *

def main ():

    reserva = [{"ID": 345, 'nome': "Ruivaldo" , 'ultimo_nome': "Santana", "show": "Titanic", "data": [11,7,22], "hora": "15:00", "lugar": "B3", "preco":4.00},
                {"ID": 290, 'nome': "Lucas" , 'ultimo_nome': "Pontes", "show": "Titanic", "data": [11,7,22], "hora": "15:00", "lugar": "F6", "preco":12.00},
                {"ID": 980, 'nome': "Tomas" , 'ultimo_nome': "Chaves", "show": "Titanic", "data": [15,7,22], "hora": "20:30", "lugar": "A1", "preco":4.00},
                {"ID": 100, 'nome': "Paulo" , 'ultimo_nome': "Lopes", "show": "Romeo e Julieta", "data": [17,8,22], "hora": "10:00", "lugar": "G5", "preco":4.00},
                {"ID": 133, 'nome': "Ana" , 'ultimo_nome': "Gomes", "show": "Romeo e Julieta", "data": [17,8,22], "hora": "17:45", "lugar": "H4", "preco":4.00},
                {"ID": 532, 'nome': "Felipa" , 'ultimo_nome': "Miguel", "show": "Romeo e Julieta", "data": [17,8,22], "hora": "10:00", "lugar": "C9", "preco":4.00},
                {"ID": 298, 'nome': "Jose" , 'ultimo_nome': "Filipe", "show": "Panda e os Caricas", "data": [30,9,22], "hora": "12:00", "lugar": "A9", "preco":12.00},
                {"ID": 843, 'nome': "Leonor" , 'ultimo_nome': "Torres", "show": "Panda e os Caricas", "data": [30,9,22], "hora": "12:00", "lugar": "A8", "preco":12.00},
                {"ID": 65, 'nome': "Camila" , 'ultimo_nome': "Bento", "show": "Panda e os Caricas", "data": [1,9,22], "hora": "9:30", "lugar": "D13", "preco":4.00},
                {"ID": 734, 'nome': "Joana" , 'ultimo_nome': "Tome", "show": "Panda e os Caricas", "data": [22,9,22], "hora": "9:30", "lugar": "J10", "preco":4.00},
    ]

    cartazes = [{"nome": "Titanic", "data":[[11,7,22],[15,7,22],[20,7,22]], "hora":['15:00','20:30']},
                {"nome": "Romeo e Julieta", "data":[[10,8,22],[17,8,22],[28,8,22]], "hora":["10:00","17:45"]},
                {"nome": "Panda e os Caricas", "data":[[1,9,22],[30,9,22],[22,9,22]], "hora":["9:30","12:00"]}
                ]
   
    inicio = admin_login()
    pedido = None
    lugar = None
    administrador = None
    aviso = None
    sucesso = None
    option = None
    detalhes = None
    aviso_2 = None
    bilheteria = None
    aviso_3 = None

    while True:
        window, eventos,valor = pg.read_all_windows()

        if eventos == pg.WINDOW_CLOSED:
            break

        if window == sucesso and eventos == "OK":
            aviso.hide()
            sucesso.hide()
            inicio.un_hide()

        if window == administrador:
        
            if eventos == 'Entrar':
                if administrador['senha_admin'].get() == "1234":
                    bilheteria = contagem(reserva)
                    administrador['erro'].update(visible= False)
                    administrador['senha_admin'].update(value = "")
                    administrador.hide()
                else:
                    administrador['erro'].update(visible= True)
            
            if eventos == 'Voltar':
                administrador.hide()
                inicio.un_hide()

        if window == bilheteria:

            if eventos == "Voltar":
                administrador.un_hide()
                bilheteria.hide()

            if eventos == "dia":
                total = calcular_dia(reserva,valor["dia"])
                window["total"].update(value = total)

            if eventos == "mes":
                total = calcular_mes(reserva,valor["mes"])
                window["total"].update(value = total)

            if eventos == "ano":
                total = calcular_ano(reserva,valor["ano"])
                window["total"].update(value = total)    

        if window == inicio:

            if eventos == "Cliente":
                option = escolher()
                inicio.hide()

            if eventos == "Admin":
                administrador = admin()
                inicio.hide()

        if window == option:

            if eventos == "Comprar bilhete":
                esconder(window,False)
                option.hide()
                pedido = compra()
                
            if eventos == "Voltar":
                option.hide()
                inicio.un_hide()

            if eventos == "Consultar bilhete":
                esconder(window,True)

            if eventos == "pesquisar":
                bilhete = search_id(reserva,int(valor["ID"]))

                if bilhete == False:
                    window["aviso"].update(visible = True)
                else:
                    window["aviso"].update(visible = False)  
                    detalhes = detail()
                    detalhes["show"].update(value = bilhete["show"])
                    detalhes["nome"].update(value = bilhete["nome"])
                    detalhes["ultimo"].update(value = bilhete["ultimo_nome"])

                    cartaz = atualizar_cartaz(cartazes,bilhete["show"] )

                    detalhes["data"].update(values = cartaz["data"], value = bilhete["data"])
                    detalhes["hora"].update(values = cartaz["hora"], value = bilhete["hora"])
                    option.hide()

        if window == detalhes:

            if eventos == "Voltar":
                esconder(option,False)
                option.un_hide()
                detalhes.hide()

            if eventos == "Alterar":
                lugar = palco()
                esconder_2(lugar,False,True)

                for bilhete in reserva:
                        if window["show"].get() == bilhete["show"] and window["data"].get() == bilhete["data"] and window["hora"].get() == bilhete["hora"]:
                            lugar[bilhete["lugar"]].update(value = "X")

                lugar["alterar"].update(visible = True)

            if eventos =="Eliminar":
                aviso_2 = warning()

        if window == aviso_2:

            if eventos == "Sim":
                reserva = eliminar (reserva,option["ID"].get())
                esconder(option,False)
                aviso_2.hide()
                detalhes.hide()
                option.un_hide()
            else:
                aviso_2.hide()

        if window == pedido:

            if eventos == "Voltar":
                option["aviso"].update(visible = False)
                option.un_hide()
                pedido.hide()
                
            if eventos == "Continuar":
                
                if valor["show"] == "" or valor["data"] == "" or valor["hora"] == "" or valor["Nome"] == "" or valor["ultimo"] == "":
                    window["aviso"].update(visible = True)
                else:
                    window["aviso"].update(visible = False)
                    lugar = palco()
                    nome = window["Nome"].get()
                    ultimo = window["ultimo"].get()
                    dia = window["data"].get()
                    hora = window["hora"].get()
                    show = window["show"].get()

                    for bilhete in reserva:
                        if show == bilhete["show"] and dia == bilhete["data"] and hora == bilhete["hora"]:
                            lugar[bilhete["lugar"]].update(value = "X")

                    pedido.hide()

            if eventos == "show":
                window["imagem"].update("./cartaz/"+valor["show"]+".png")
            
                cartaz = atualizar_cartaz(cartazes, valor["show"])

                window["data"].update(values = cartaz["data"])
                window["hora"].update(values = cartaz["hora"])

        if window == lugar:

            if eventos == "Continuar":

                if valor["letra"] == "" or valor["numero"] == "":
                    window["aviso_1"].update(visible = True)
                else:
                    assento = window["letra"].get() + window["numero"].get()
                    if assento in verify_assento(reserva,show,dia,hora):
                        window["aviso_2"].update(visible = True)
                    else:
                        window["aviso_1"].update(visible = False)
                        window["aviso_2"].update(visible = False)
                        aviso = confirmacao()
                        aviso["show"].update(value = show)
                        aviso["nome"].update(value = nome)
                        aviso["ultimo"].update(value = ultimo)
                        aviso["data"].update(value = dia)
                        aviso["hora"].update(value = hora)
                        aviso["lugar"].update(value = assento)

                        preco = price(valor["letra"],valor["numero"])

                        aviso['preco'].update(value = preco)
                        lugar.hide()

            if eventos == "Voltar":
                pedido.un_hide()
                lugar.hide()

            if eventos == "letra":

                if valor["letra"] in ["A", "F"]:
                    window["numero"].update(values = ["1","2","6","7","8","9","13","14"])
                else:
                    window["numero"].update(values = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14"])

            if eventos == "alterar":
                reserva = alterar(reserva,option["ID"].get(),detalhes["hora"].get(),detalhes["data"].get(), lugar["letra"].get(), str(lugar["numero"].get()))
                aviso_3 = warning_2()

            if eventos == "voltar_2":
                detalhes.un_hide()
                lugar.hide()

        if window == aviso:

            if eventos == "OK":
                sucesso = efetuado() 
                novo_ID = ID(reserva)
                reserva = reservar(reserva,novo_ID,nome,ultimo,show,dia,hora,assento, preco)
                sucesso["ID"].update(value = novo_ID)

            if eventos == "Voltar":
                lugar.un_hide()
                aviso.hide()

        if window == aviso_3:

            if eventos == "OK":
                esconder(option,False)
                esconder_2(lugar, True,False)
                aviso_3.hide()
                lugar.hide()
                detalhes.hide()
                option.un_hide()