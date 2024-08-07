Web VPython 3.2

#Caixa da Esquerda
esquerda = box(pos=vec(-10, 0, 0), length=1, height=1, width=1, color=color.white)

#Caixa da Direita
direita = box(pos=vec(10, 0, 0), length=1, height=1, width=1, color=color.white)

#Esfera no meio
esfera = sphere(pos=vector(0,0,0), radius=1, color=color.red)


while esfera.pos.x-1 > esquerda.pos.x:
    rate(70)
    esfera.pos.x = esfera.pos.x-0.1
    
    
while esfera.pos.x+1 < direita.pos.x:
    rate(70)
    esfera.pos.x = esfera.pos.x+0.1
    

while esfera.pos.x > 0:
    rate(70)
    esfera.pos.x = esfera.pos.x-0.1
    

    
# O código consiste em fazer com que a esfera que inicia no centro, vá para esquerda, direita e no fim retorne ao centro
# Feito no --> Web VPython

  
# Matheus Nogueira Albuquerque
