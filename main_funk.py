import turtle

class Game:
    def __init__(self):
        # m2 ir m2f resursuose testavimo failai sudeliojimui i objektini.
        pass
    
def bkiller(*args):
    "naikina nurodytus mygtukus"
    for b in args:
        b.destroy()

def city_dot(x, y):
    ''' sukuria  turtle tašką ir nukelia į x ir y koordinates
    x, y - int'''

    m_taskas = turtle.Turtle()
    m_taskas.penup()
    m_taskas.shape("circle")
    m_taskas.color("light green")
    m_taskas.goto(x, y)

def city_title(x, y, irasas, sriftas):
    ''' sukuria uzrasa ir nukelia į x ir y koordinates
    x, y - int
    irasas - str
    sriftas - tuple is 3 narių
    pavizdys: ("Courier", 16, "bold")
    '''
    mietsto_pav = turtle.Turtle()
    mietsto_pav.hideturtle()
    mietsto_pav.penup()
    mietsto_pav.goto(x, y)
    mietsto_pav.color("purple")
    mietsto_pav.write(irasas, font=sriftas)
