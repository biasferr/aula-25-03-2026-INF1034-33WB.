from turtle import *
from random import randint



t = Turtle()

def criar_planocartesiano():
    t.pu()
    t.goto(200,0)
    t.pd()
    t.stamp()
    t.left(180)
    t.forward(400)
    t.stamp()

    t.pu()
    t.goto(0,-200)
    t.left(90)
    t.pd()
    t.stamp()
    t.right(180)
    t.forward(400)
    t.stamp()
    t.pu()

    t.goto(100,100)
    t.pendown()

def criar_triângulo(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (3):
        t.fd(lado)
        t.rt(120)
    t.end_fill()

def criar_hexagono(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (6):
        t.fd(lado)
        t.rt(60)
    t.end_fill()

def criar_pentagono(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(5):
        t.fd(lado)
        t.rt(72)
    t.end_fill()

def criar_octonogono(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(8):
        t.fd(lado)
        t.rt(45)
    t.end_fill()


def poligono_regular(x,y,aresta,angulo,n_lados,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (n_lados):
        t.fd(aresta)
        t.rt(angulo)
    t.end_fill()





#plano cartesiano
criar_planocartesiano()

#primeiro quadrante
x1= randint(0,200)
y1= randint(50,200)

#triângulo
color= textinput("obter cor", "digite uma cor:")
criar_triângulo(x1,y1,70,color)

#segundo quadrante
x2= randint(-200,-70)
y2= randint(70,200)

#hexágono
color= textinput("obter cor", "digite uma cor:")
criar_hexagono(x2,y2,50,color)

#terceiro quadrante 
x3= randint(-200,-70)
y3= randint(-200,-70)

#pentagono
color= textinput("obter cor", "digite uma cor:")
criar_pentagono(x3,y3,50,color)

#quarto quadrante
x4= randint(40,200)
y4= randint(-200,-70)

#octonogo
color= textinput("obter cor", "digite uma cor:")
criar_octonogono(x4,y4,40,color)

#polígono
poligono_regular(250,0,100,120,3,"red")

mainloop()