from turtle import *
t= Turtle()
from time import sleep 
t.speed(100)


#japão

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()

def desenha_bandeira_japao():
    desenha_retangulo(-150, -50, 300, 180, "white")

def desenha_circulo(x, y, color, raio):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()


def desenha_circulo_japão():
    desenha_circulo(0, -10, "red", 50)

desenha_bandeira_japao()
desenha_circulo_japão()

sleep(1)
t.clear()

#iralanda

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()
def desenha_bandeira_irlanda():
    desenha_retangulo(-150, -50, 300, 180, 'white')

def desenhar_ret(x, y, alt, larg,  color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (2):
        t.lt(90)
        t.fd(alt)
        t.lt(90)
        t.fd(larg)
    t.end_fill()

def desenha_retangulo_irlanda():
    desenhar_ret(-60, -50, 180, 90, 'green')

def desenhar_outro_ret(x,y,larg,alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.lt(90)
    t.fd(larg)
    t.rt(90)
    t.fd(alt)
    t.rt(90)
    t.fd(larg)
    t.rt(90)
    t.fd(alt)
    t.end_fill()

def desenhar_parte_final():
    desenhar_outro_ret(60, -50, 180, 90, 'orange')

desenha_bandeira_irlanda()
desenha_retangulo_irlanda()
desenhar_parte_final()

sleep(1)
t.clear()

#níger

def desenha_retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.lt(180)
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()

def desenha_bandeira_niger():
    desenha_retangulo(-150, -50, 300, 65, 'green')

def outra_parte(x, y, z):
    t.lt(90)
    t.fd(x)
    t.rt(90)
    t.fd(y)
    t.rt(90)
    t.fd(z)
    t.lt(180)
    t.fd(z)

def retangulo():
    outra_parte(135, 300, 70)
   
   
   
def parte_final(larg, alt, color):
    t.begin_fill()
    t.fillcolor(color)
    t.fd(65)
    t.lt(90)
    t.fd(larg)
    t.lt(90)
    t.fd(alt)
    t.lt(90)
    t.fd(larg)
    t.end_fill()

def ultparte():
    parte_final(300, 65, 'orange')

def desenha_circulo(x, y, color, raio):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()

def circulo():
    desenha_circulo(0, 20, 'orange', 30)

desenha_bandeira_niger()
retangulo()
ultparte()
circulo()

sleep(1)
t.clear()

#finlandia

def desenha_bandeira_finlandia(x, y, larg, alt):
    t.pu()
    t.goto(x, y)
    t.pd()

    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)

def desenho_retangulo():
    desenha_bandeira_finlandia(-150, -50, 300, 180)

def desenhe(x, y, z, q, color):
    t.begin_fill()
    t.fillcolor(color)
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.fd(x)
    t.rt(90)
    t.fd(y)
    t.rt(90)
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.rt(90)
    t.fd(z)
    t.rt(90)
    t.fd(y)
    t.lt(90)
    t.fd(q)
    t.rt(90)
    t.fd(y)
    t.rt(90)
    t.fd(q)
    t.lt(90)
    t.fd(y)
    t.rt(90)
    t.fd(y)
    t.end_fill()

def desenhofinal():
    desenhe(90, 60, 65, 145, 'blue')

desenho_retangulo()
desenhofinal()

sleep(1)
t.clear()

#senegal

def desenha_bandeira_senegal(x, y, larg, alt):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.lt(180)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)

def desenho_retangulo():
    desenha_bandeira_senegal(-150, -50, 300, 180)

def segunda_parte(larg, alt, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhodois():
    segunda_parte(100, 180, 'green')


def terceira_parte(larg, alt, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhotres():
    terceira_parte(100, 180, 'yellow')


def quarta_parte(larg, alt, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()

def desenhoquatro():
    quarta_parte(100, 180, 'red')

def desenhoestrela1(x, y, larg, alt, exp, color, z, q, e, r ,b):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.lt(140)
    t.fd(larg)
    t.rt(140)
    t.fd(alt)
    t.rt(140)
    t.fd(larg)
    t.rt(150)
    t.fd(exp)
    t.rt(143)
    t.fd(exp)
    t.pu()
    t.rt(148)
    t.fd(z)
    t.rt(80)
    t.fd(q)
    t.rt(60)
    t.fd(e)
    t.rt(75)
    t.fd(r)
    t.rt(70)
    t.fd(b)
    t.pd()
    t.end_fill()

def estrelaum():
    desenhoestrela1(20, 0, 70, 60, 75, 'green', 50, 17, 16, 15, 18)

desenho_retangulo()
desenhodois()
desenhotres()
desenhoquatro()
estrelaum()
sleep(1)
t.clear()
#italia
def desenhar_italia(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.rt(214)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhoitalia():
    desenhar_italia(-150, -50, 100, 180, 'green', 'white', 'red')

desenhoitalia()
sleep(1)
t.clear()

#belgica

def desenhar_belgica(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()

    
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhobelgica():
    desenhar_belgica(-150, -50, 100, 180, 'black', 'yellow', 'red')
    
desenhobelgica()
sleep(1)
t.clear()

#frança

def desenhar_frança(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()

    
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhofrança():
    desenhar_frança(-150, -50, 100, 180, 'blue', 'white', 'red')

desenhofrança()
sleep(1)
t.clear()

#nigeria 

def desenhar_nigeria(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()

    
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhonigeria():
    desenhar_nigeria(-150, -50, 100, 180, 'green', 'white', 'green')
desenhonigeria()
sleep(1)
t.clear()

#Alemanha
def desenhar_alemanha(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhoalemanha():
    desenhar_alemanha(-150, -50, 300, 60, 'yellow', 'red', 'black')

desenhoalemanha()
sleep(1)
t.clear()

#Paises baixos

def desenhar_paisesbaixos(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhopaisesbaixos():
    desenhar_paisesbaixos(-150, -50, 300, 60, 'blue', 'white', 'red')

desenhopaisesbaixos()
sleep(1)
t.clear()

#colombia

def desenhar_colombia(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhocolombia():
    desenhar_colombia(-150, -50, 300, 60, 'red', 'blue', 'yellow')

desenhocolombia()
sleep(1)
t.clear()

#romenia 

def desenhar_romenia(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.rt(90)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.fd(larg)
    t.end_fill()

def desenhoromenia():
    desenhar_romenia(-150, -50, 100, 180, 'blue', 'yellow', 'red')
desenhoromenia()
sleep(1)
t.clear()


#austria

def desenhar_austria(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhoaustria():
    desenhar_austria(-150, -50, 300, 60, 'red', 'white', 'red')

desenhoaustria()
sleep(1)
t.clear()

#Russia

def desenhar_russia(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhorussia():
    desenhar_russia(-150, -50, 300, 60, 'red', 'blue', 'white')

desenhorussia()
sleep(1)
t.clear()

#polonia
def desenhar_polonia(x, y, larg, alt, color1, color2):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()
    t.lt(90)
    t.fd(alt)
    t.rt(90)

    t.begin_fill()
    t.fillcolor(color2)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()

def desenhopolonia():
    desenhar_polonia(-150, -50, 300, 90, 'red', 'white')

desenhopolonia()
sleep(1)
t.clear()
#bulgaria

def desenhar_bulgaria(x, y, larg, alt, color1, color2, color3):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color1)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color2)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()
    t.begin_fill()
    t.fillcolor(color3)
    t.rt(90)
    for _ in range (2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.lt(90)
    t.fd(alt)
    t.end_fill()

def desenhobulgaria():
    desenhar_bulgaria(-150, -50, 300, 60, 'red', 'green', 'white')

desenhobulgaria()
sleep(1)
t.clear()

mainloop()