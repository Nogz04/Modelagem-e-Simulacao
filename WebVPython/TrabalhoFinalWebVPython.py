Web VPython 3.2

import random


ceu = box(pos=vector(0, 20, 0), size=vector(100, 0.5, 100), color=color.cyan)  
chao = box(pos=vector(0, -10, 0), size=vector(100, 0.5, 100), color=color.green) 

estrelas = []


def criar_estrela():
    
    x_pos = random.uniform(-50, 50)
    z_pos = random.uniform(-50, 50)
    estrela = sphere(pos=vector(x_pos, 20, z_pos), radius=0.5, color=vector(random.random(), random.random(), random.random())) #randomizando posição das estrelas e as cores delas.
    estrelas.append(estrela)
    return estrela


def mover_estrelas():
   
    for estrela in estrelas:
        estrela.pos.y -= 0.1 
        if estrela.pos.y < -10:  
            estrela.visible = False  
            estrelas.remove(estrela)  

while True:
    rate(60) 
    if random.random() < 0.05: 
        criar_estrela()
    mover_estrelas()  




    
    
    
    
    
