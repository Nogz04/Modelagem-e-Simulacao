Web VPython 3.2

#Caixa da Esquerda
esquerda = box(pos=vec(-10, 0, 0), length=1, height=1, width=1, color=color.white)

#Caixa da Direita
direita = box(pos=vec(10, 0, 0), length=1, height=1, width=1, color=color.white)

#Esfera no meio
esfera = sphere(pos=vector(0,0,0), radius=1, color=color.red)

while esfera.pos.x+1 < direita.pos.x:
    rate(70)
    esfera.pos.x = esfera.pos.x+0.1


#Este código move uma esfera entre 2 caixas, a esfera vai para a direita e para 1 raio antes da caixa da direita
