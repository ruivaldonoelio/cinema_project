import PySimpleGUI as pg

def efetuado():
    pg.theme("Reddit")
    
    sucesso = [
        [pg.Text("Numero da reserva:"), pg.Text("", key = "ID")],
        [pg.Button("OK")]
    ]
    return pg.Window("Confirmação", layout=sucesso, finalize=True)

def confirmacao():
    pg.theme("Reddit")

    aviso = [
        [pg.Text("Espetaculo:") , pg.Text("", key = "show")],
        [pg.Text("Primeiro nome:"),pg.Text("", key = "nome")],
        [pg.Text("Sobrenome:"),pg.Text("", key = "ultimo")],
        [pg.Text("Data:"),pg.Text("", key = "data")],
        [pg.Text("Hora:"),pg.Text("", key = "hora")],
        [pg.Text("Lugar:"),pg.Text("", key = "lugar")],
        [pg.Text("Preço:"),pg.Text("", key = "preco")],
        [pg.Button("OK"), pg.Button("Voltar")]
    ]
    return pg.Window("Confirmação", layout=aviso, finalize=True)

def admin_login ():
    pg.theme("Reddit")

    escolher = [
        [pg.Button("Admin"),pg.Button("Cliente")]
    ]
    return pg.Window(" ", layout=escolher, finalize=True)

def admin():
    pg.theme("Reddit")

    login_admin = [
        [pg.Text("Admin")],
        [pg.Text("Senha"),pg.Input(size = (15,1), password_char='*', key="senha_admin")],
        [pg.Button("Entrar"), pg.Button("Voltar")],
        [pg.Text('A senha que inseriu está errada.', text_color="#FF0000", visible=False, key='erro')]
    ]
    return pg.Window("Entrar", layout=login_admin, finalize=True)

def compra ():
    pg.theme("Reddit")

    cartazes = ["Titanic","Romeo e Julieta","Panda e os Caricas"]

    comprar = [
        [pg.Image("./cartaz/Titanic.png", k = "imagem")],
        [pg.Text("Espetáculo", size = (8,1)),pg.Combo(values = cartazes, enable_events = True, key = "show")],
        [pg.Text("Dia", size = (4,1)),pg.Combo(values = [],size = (6,1), key = "data"),pg.Text("Hora", size = (3,1)), pg.Combo(values = [],size = (5,1), k = "hora")],
        [pg.Text("Nome", size = (5,1)), pg.Input(size = (15,1), key = "Nome")],
        [pg.Text("Sobrenome", size = (9,1)), pg.Input(size = (15,1), key = "ultimo")],
        [pg.Text("Preencha todos os campos", key = "aviso", text_color = "#FF0000", visible = False)],
        [pg.Button("Continuar"), pg.Button("Voltar")]
    ]
    return pg.Window("Comprar", layout=comprar, finalize=True)

def escolher ():
    pg.theme("Reddit")

    escolher =  [
    [pg.Button("Comprar bilhete")],
    [pg.Button("Consultar bilhete")],
    [pg.Text("ID:", visible = False, key = "txt_ID"),pg.Input(visible = False, key = "ID", size = (7,1))],
    [pg.Text("ID invalido", key = "aviso",text_color = "#FF0000", visible = False)],
    [pg.Button("Voltar"), pg.Button("Pesquisar", key = "pesquisar", visible = False)]
    ]
    return pg.Window("Opções", layout=escolher, finalize=True)

def detail (): 
    pg.theme("Reddit")

    detail = [
        [pg.Text("Espetaculo", size = (8,1)),pg.Combo(values = "",enable_events = True, key = "show", size = (15,1) , disabled = True)],
        [pg.Text("Dia", size = (4,1)),pg.Combo(values = [],size = (5,1), key = "data"),pg.Text("hora", size = (3,1)), pg.Combo(values = [],size = (5,1), k = "hora")],
        [pg.Text("Nome", size = (5,1)), pg.Input(size = (21,1), key = "nome", disabled = True)],
        [pg.Text("Sobrenome", size = (10,1)), pg.Input(size = (10,1), key = "ultimo",disabled = True)],
        [pg.Button("Voltar"), pg.Button("Eliminar"), pg.Button("Alterar")]
    ]
    return pg.Window("Consulta", layout=detail, finalize=True)

def warning ():
    pg.theme("Reddit")

    warning = [
        [pg.Text("De certeza que pretende eliminar?")],
        [pg.Button("Sim"), pg.Button("Não")]
    ]
    return pg.Window("Confirmação", layout=warning, finalize=True)

def warning_2():
    pg.theme("Reddit")

    warning = [
        [pg.Text("Alteração completa")],
        [pg.Button("OK")]
    ]
    return pg.Window("Confirmação", layout=warning, finalize=True)

def contagem (reserva):
    pg.theme("Reddit")

    bilhete = []

    for l in range (0, len(reserva)):
        bilhete.append([])
        bilhete[l].append(reserva[l]["ID"])
        bilhete[l].append(reserva[l]["nome"])
        bilhete[l].append(reserva[l]["ultimo_nome"])
        bilhete[l].append(reserva[l]["show"])
        bilhete[l].append(reserva[l]["data"])
        bilhete[l].append(reserva[l]["hora"])
        bilhete[l].append(reserva[l]["lugar"])
        bilhete[l].append(reserva[l]["preco"])

    tabela = [
        [pg.Table(bilhete, headings = ["ID","Nome","Sobrenome","Espétaculo","Data","Hora","Lugar","Preço"])]
    ]
    
    dia = [[11,7,22],[15,7,22],[20,7,22], [10,8,22],[17,8,22],[28,8,22],[1,9,22],[30,9,22],[22,9,22]]
    mes = [[7,22],[8,22],[9,22]]

    combos = [
        [pg.Text("Dia"),pg. Combo(dia,size = (7,1),enable_events = True ,k = "dia")],
        [pg.Text("Mes"),pg. Combo(mes,size = (7,1),enable_events = True,k = "mes")],
        [pg.Text("Ano"),pg. Combo([22],size = (7,1),enable_events = True,k = "ano")],
        [pg.Text("Total de faturação:"), pg.Text("", key = "total")]
    ]

    coluna = [
        [pg.Column(tabela),pg.Column(combos)],
        [pg.Button("Voltar")]
    ]

    return pg.Window("Bilheteria", layout=coluna, finalize=True)

def price (letra,numero):

    if letra in ['A', 'F'] and numero in ['6','7','8','9']:
        preco = 12.00
    else:
        preco = 4.00

    return preco