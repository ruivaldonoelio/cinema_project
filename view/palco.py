import PySimpleGUI as pg

superior = ["K","J","I","H","G"]
inferior = ["E","D","C","B"]

pg.theme("Reddit")

def posicao (lugares):
    palco = [[pg.Text(text=p ,size = (2, 1)),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "1"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "2"),
        pg.Text(text= "   "),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "3"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "4"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "5"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "6"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "7"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "8"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "9"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "10"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "11"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "12"),
        pg.Text(text= "   "),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "13"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = p + "14")
        ]for p in lugares]
    return palco

def VIP (lugares):
    palco = [pg.Text(text= lugares ,size = (2, 1)),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "1"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "2"),
        pg.Text(text="                  VIP -"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "6"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "7"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "8"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "9"),
        pg.Text(text= "- VIP                   "),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "13"),
        pg.Text(text= "",background_color = '#ABABAB', size = (2, 1), k = lugares + "14"),
        ]
    return palco

def palco ():

    letras = ["K","J","I","H","G","F","E","D","C","B","A"]
    palco =[
        [pg.Text(text="        1      2             3      4     5      6      7     8     9     10     11    12          13     14")],
        posicao(superior),
        VIP("F"),
        posicao(inferior),
        VIP("A"),
        [pg.Combo(values = letras ,key = "letra", enable_events = True),pg.Combo(values= "", key = "numero", size = (2,1)),pg.Text(text="                                         Palco", size = (45,3),background_color = '#ABABAB')],
        [pg.Button("Continuar", visible = True,k = "Continuar"),pg.Button("Voltar", visible = True, k = "Voltar"),pg.Button("Voltar",visible = False,k = "voltar_2"),pg.Button("Alterar", visible = False, k = "alterar"),pg.Text("Preencha todos os campos", key = "aviso_1", text_color = "#FF0000", visible = False),pg.Text("Assento indisponível", key = "aviso_2", text_color = "#FF0000", visible = False)]
    ]
    return pg.Window("Palco", layout=palco, finalize=True)