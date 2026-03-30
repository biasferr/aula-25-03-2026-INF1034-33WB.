#funções bandeiras

from turtle import *
from time import sleep


t= Turtle()

#funções de formas geométricas
def retangulo(x,y,base,alt,color):
    t.up()
    t.goto(x,y)
    t.begin_fill()
    t.fillcolor(color)
    t.pd()
    for _ in range (2):
        t.forward(base)
        t.left(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()


def circulo(x,y,raio,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()

def triangulo(x,y,color,lado):
    t.pu()
    t.goto(x,y)
    t.begin_fill()
    t.fillcolor(color)
    t.pd()
    t.right(45)
    t.forward(lado)
    t.rt(90)
    t.forward(lado)
    t.lt(135)
    t.end_fill()

def estrela(x,y,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(5):
        t.fd(20)
        t.lt(72)
        t.fd(20)
        t.rt(144)
    t.end_fill()

def quadrado(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (4):
        t.fd(lado)
        t.left(90)
    t.end_fill()

#funções bandeiras
def bandeira_japao():
    retangulo(-200,-100, 400, 300, "white")
    circulo(0,-20,70,"red")
    sleep(2)
    t.clear()


def bandeira_russia():
    retangulo(-200,-100, 400, 300, "white")
    retangulo(-200,0,400,100,"blue")
    retangulo(-200,-100,400,100,"red")
    sleep(2)
    t.clear()

def bandeira_islandia():
    retangulo(-200,-100, 400, 300, "#120A8F")
    retangulo(-200,17,400,70,"white")
    retangulo(-116,-100,70,300,"white")
    retangulo(-200,31,400,40,"red")
    retangulo(-102,-100,40,300,"red")
    sleep(2)
    t.clear()

def bandeira_niger():
    retangulo(-200,-100, 400, 300, "orange")
    retangulo(-200,0,400,100,"white")
    retangulo(-200,-100,400,100,"green")
    circulo(0,10,40,"orange")
    sleep(2)
    t.clear()

def bandeira_bahamas():
    retangulo(-200,-100, 400, 300, "#008B8B")
    retangulo(-200,0,400,100,"#FFD700")
    triangulo(-200,200,"black",215)
    sleep(2)
    t.clear()

def bandeira_gambia():
    retangulo(-200,-100,400,300,"red")
    retangulo(-200,0,400,100,"white")
    retangulo(-200,-100,400,100,"green")
    retangulo(-200,21,400,55,"#120A8F")
    sleep(2)
    t.clear()

def bandeira_emirados_arabes():
    retangulo(-200,-100,400,300,"green")
    retangulo(-200,0,400,100,"white")
    retangulo(-200,-100,400,100,"black")
    retangulo(-200,-100,100,300,"red")
    sleep(2)
    t.clear()

def bandeira_noruega():
    retangulo(-200,-100, 400, 300, "red")
    retangulo(-200,17,400,70,"white")
    retangulo(-116,-100,70,300,"white")
    retangulo(-200,31,400,40,"#120A8F")
    retangulo(-102,-100,40,300,"#120A8F")
    sleep(2)
    t.clear()

def bandeira_grecia():
    retangulo(-200,-100, 400, 300, "white")
    retangulo(-200,167,400,33,"#0F2284")
    retangulo(-200,101,400,33,"#0F2284")
    retangulo(-200,35,400,33,"#0F2284")
    retangulo(-200,-31,400,33,"#0F2284")
    retangulo(-200,-100,400,36,"#0F2284")
    quadrado(-200,35,165,"#0F2284")
    retangulo(-134,35,33,165,"white")
    retangulo(-200,101,165,33,"white")
    sleep(2)
    t.clear()

def bandeira_sao_tome_e_principe():
    retangulo(-200,-100, 400, 300, "green")
    retangulo(-200,0,400,100,"yellow")
    triangulo(-200,200,"red",215)
    estrela(10,60,"black")
    estrela(100,60,"black")
    sleep(2)
    t.clear()



#código
t.speed(0)

bandeiras=textinput("obter país","digite um país entre os seguintes: japao")
if bandeiras == "japao":
    bandeira_japao()
elif bandeiras == "russia":
    bandeira_russia()
elif bandeiras == "islandia":
    bandeira_islandia()
elif bandeiras== "niger":
    bandeira_niger()
elif bandeiras== "bahamas":
    bandeira_bahamas()
elif bandeiras== "gambia":
    bandeira_gambia()
elif bandeiras== "emirados arabes":
    bandeira_emirados_arabes()
elif bandeiras== ""

# russia= bandeira_russia()
# islandia= bandeira_islandia()
# niger= bandeira_niger()
# bahamas= bandeira_bahamas()
# gambia = bandeira_gambia()
# emirados_arabes= bandeira_emirados_arabes()
# noruega= bandeira_noruega()
# grecia= bandeira_grecia()
# sao_tome_e_principe= bandeira_sao_tome_e_principe()




mainloop()