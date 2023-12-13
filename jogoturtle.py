'''
Alexsandro Martins Alves _ UFC-RUSSAS
CC
SEMESTRE  - 2022.2 
MATRICULA: 541581
TRABALHO DE FUP1
'''

import turtle 
import random

#Variaveis Globais

partida = 0
v = 0
pontuacao = 0
combustivel = 100

#Janela do jogo 

tela = turtle.Screen()
tela.setup(900, 700)
tela.title('Warriors Galaxtic ')
tela.bgcolor('black')
tela.tracer(0)

#Adicionando Imagens(shape)

tela.addshape('assents\wnave.gif')
tela.addshape('assents\meteoro1.gif')
tela.addshape('assents\galax1.gif')
tela.addshape('assents\explosao.gif')
tela.addshape('assents\eBonus.gif')

#Cenario1

cenario1 = turtle.Turtle()
cenario1.shape('assents\galax1.gif')
cenario1.speed(0)
cenario1.right(90)
cenario1.up()

#Cenario2

cenario2 = turtle.Turtle()
cenario2.shape('assents\galax1.gif')
cenario2.speed(0)
cenario2.right(90)
cenario2.sety(800)
cenario2.up()

#Personagem1

nave = turtle.Turtle()
nave.shape('assents\wnave.gif')
nave.speed(2)
nave.up()
nave.goto(0, -300)

#Pontuaçao

score = turtle.Turtle()
score.color('white')
score.speed(0)
score.up()
score.goto(-280, 310)
score.write(f'Pontuação:\n{pontuacao}', font=('Italic', 14, 'bold'))
score.hideturtle()

# Nivel do combustivel

nivel = turtle.Turtle()
nivel.color('white')
nivel.speed(0)
nivel.up()
nivel.goto(150, 310 )
nivel.write(f'Combustivel:\n{combustivel}', font=('Italic', 14, 'bold'))
nivel.hideturtle()

# titulo do comecar_jogo

titulo = turtle.Turtle()
titulo.color('red')
titulo.speed(0)
titulo.penup()
titulo.goto(-250, 100)
titulo.write('APERTE SPACE PARA COMEÇAR' ,font=('Italic', 24, 'bold'))
titulo.hideturtle()

#Obstaculo1

asteroide = turtle.Turtle()
asteroide.speed(2)
asteroide.shape('assents\meteoro1.gif')
asteroide.up()
asteroide.goto(random.randint(-250, 250), 460)
velocidade = 8

#Combustivel

bonus = turtle.Turtle()
bonus.speed(0)
bonus.shape('assents\eBonus.gif')
bonus.up()
bonus.goto(random.randint(-250, 250), 960)
velocidade = 5

#asteroide e estrela denntro da minha area

def obsloop():
    asteroide.setx(random.randint(-250, 250)) 

def bonusloop():
    bonus.setx(random.randint(-250,250))

# Colisao do bonus com a nave

def obsbonus():
    distanciax = bonus.xcor() - nave.xcor()
    distanciay = bonus.ycor() - nave.ycor()
    if distanciax <= 70 and distanciax >= -70 and distanciay <= 80 and distanciay >= -80:
        bonus.sety(540)

#Colisao do bonus com a nave

def colibonus():
    global pontuacao, combustivel
    distanciax = bonus.xcor() - nave.xcor()
    distanciay = bonus.ycor() - nave.ycor()
    if distanciax <= 70 and distanciax >= -70 and distanciay <= 80 and distanciay >= -80:
        bonus.sety(960)
        pontuacao = pontuacao + 10
        score.clear()
        score.write(f'Pontuação:\n{pontuacao}', font=('Italic', 14, 'bold'))
        combustivel = combustivel + 10
        nivel.clear()
        nivel.write(f'Combustivel:\n{combustivel}', font=('Italic', 14, 'bold'))

#Colisao Nave com o asteroide

def colinave():
    global partida, v, pontuacao, combustivel
    distanciax = asteroide.xcor() - nave.xcor()
    distanciay = asteroide.ycor() - nave.ycor()
    if distanciax <= 80 and distanciax >= -80 and distanciay <= 80 and distanciay >= -80:
        partida = 0
        i = True
        nave.shape('assents\explosao.gif') 
        tela.update()
        tela.ontimer(nave.shape('assents\wnave.gif'), 500)  
        titulo.write('APERTE SPACE PARA COMEÇAR' ,font=('Italic', 24, 'bold'))
        while i: #Quando colidir, o asteroide e a estrela irao subir para o inicio da tela numa velocidade
            asteroide.sety(asteroide.ycor() + v + 10 )
            bonus.sety(bonus.ycor() + v + 10  ) #A estrela e o asteroide vao subir para o inicio da tela numa certa velocidade
            tela.ontimer(tela.update(), 1000//60) 
            if asteroide.ycor() >= 460 and bonus.ycor() >= 460:
                i = False
                partida = 0
                v = 0
                pontuacao = -10
                combustivel = 110

#Contato da nave com a borda

def borda():
    
    global partida, v, pontuacao, combustivel                                               
    if nave.xcor() >= 210 or nave.xcor() <= -210:   #Minha nave vai se distanciar um pouco da borda, para ela nao ficar travada na borda                    
        partida = 0
        i = True
        if nave.xcor() > 0:     
            nave.setx(190)
        else:
            nave.setx(-190)    
        nave.shape('assents\explosao.gif') #Quando ela colidir com a borda aparece o sprite de explosao
        tela.update()
        tela.ontimer(nave.shape('assents\wnave.gif'), 500)   
        titulo.write('APERTE SPACE PARA COMEÇAR' ,font=('Italic', 24, 'bold'))  
        while i:                                                   
            asteroide.sety(asteroide.ycor() + v + 10 )           
            bonus.sety(bonus.ycor() + v + 10 )                            
            tela.ontimer(tela.update(), 1000//60)      #fps do jogo                      
            if asteroide.ycor() >= 460 and bonus.ycor() >= 460:    
                partida = 0                                                                
                i = False
                v = 0
                pontuacao = -10
                combustivel = 110
 
#função Principal
    
def principal():
    global pontuacao, combustivel, partida, v
    colibonus()  
    borda()
    colinave()   
    obsbonus()
    if bonus.ycor() <= -500:     
        bonus.sety(960)
    if asteroide.ycor() <= -500:   
        asteroide.sety(460)
    if bonus.ycor() == 960:
        bonusloop()
    if asteroide.ycor() == 460:
        obsloop()
    tela.update() 
    tela.ontimer(principal, 1000//60)  
    cenario1.forward(partida*10) #Para o meus cenarios ficarem se repetindo
    cenario2.forward(partida*10) 
    if cenario1.ycor() <= -800:
        pontuacao = pontuacao + 10
        score.clear()
        score.write(f'Pontuação:\n{pontuacao}', font=('Italic', 14, 'bold'))
        combustivel = combustivel - 10
        nivel.clear()
        nivel.write(f'Combustivel:\n{combustivel}', font=('Italic', 14, 'bold'))
        cenario1.sety(800)
    if cenario2.ycor() <= -800:
        pontuacao = pontuacao + 10
        score.clear()
        score.write(f'Pontuação:\n{pontuacao}', font=('Italic', 14, 'bold'))
        combustivel = combustivel - 10
        nivel.clear()
        nivel.write(f'Combustivel:\n{combustivel}', font=('Italic', 14, 'bold'))
        cenario2.sety(800)
    asteroide.sety(asteroide.ycor()-v ) #faz com que o asteroide e a estrela fiquem descendo
    bonus.sety(bonus.ycor()-v )

# Quando o combustivel acabar, chegar em 0

    if combustivel <= 0: 
        partida = 0
        v = 0
        combustivel = 110
        titulo.write('APERTE SPACE PARA COMEÇAR' ,font=('Italic', 24, 'bold'))
        asteroide.goto(random.randint(-250, 250), 460)
        bonus.goto(random.randint(-250, 250), 960)
        pontuacao = -10

#Controle de setas

def direita():

    nave.forward(partida * 20)

def esquerda():

    nave.back(partida * 20)

def comecar_jogo():
    
    global partida, v
    partida = 2
    v = 9
    if partida == 2:
        titulo.clear()
    
tela.onkey(comecar_jogo,'space')
tela.onkeypress(direita,'Right')
tela.onkeypress(esquerda,'Left')
tela.listen()   

principal()

tela.mainloop()