Web VPython 3.2

#Caixa da Esquerda
esquerda = box(pos=vec(-10, 0, 0), length=1, height=1, width=1, color=color.white)

#Caixa da Direita
direita = box(pos=vec(10, 0, 0), length=1, height=1, width=1, color=color.white)

#Esfera no meio
esfera = sphere(pos=vector(0,0,0), radius=1, color=color.red)


while True:
    while esfera.pos.x-1 > esquerda.pos.x:
        rate(70)
        esfera.pos.x = esfera.pos.x-0.3
        
        
    while esfera.pos.x+1 < direita.pos.x:
        rate(70)
        esfera.pos.x = esfera.pos.x+0.3
    


#Este código faz com que a esfera vá para esquerda e depois para direita repetindo este movimento infinitamente. 
