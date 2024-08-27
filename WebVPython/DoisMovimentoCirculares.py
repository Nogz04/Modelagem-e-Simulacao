Web VPython 3.2

def calcular_y(pos_x, r):
  
    return sqrt(r**2 - (pos_x - 10)**2) + 10


planeta = sphere(pos=vector(10, 10, 0), radius=5, color=vector(1, 0, 0))  # Cor: Vermelho

satelite1 = sphere(pos=vector(10, 0, 10), radius=1, color=vector(1, 1, 1), make_trail=True)  # Cor: Branco

satelite2 = sphere(pos=vector(30, 0, 0), radius=1, color=vector(0, 1, 1), make_trail=True)  # Cor: Ciano

# Direção de movimento para o PRIMEIRO satélite
direcao1 = 1
x1 = 0

# Direção de movimento para o SEGUNDO satélite
direcao2 = 1
x2 = 0

while True:
    rate(40) 
    
    # Movimento do planeta 
    planeta.pos.z += 0.1
    
    # Calcula a posição y do PRIMEIRO satélite com base na direção e coordenada x
    if direcao1 < 0:
        y1 = 20 - calcular_y(x1, 10)
    else:
        y1 = calcular_y(x1, 10)
    
    # Atualiza a posição do PRIMEIRO satélite
    satelite1.pos.x = x1
    satelite1.pos.y = y1
    satelite1.pos.z += 0.1
    
    # Atualiza a posição do SEGUNDO satélite
    satelite2.pos.x = x2
    satelite2.pos.y = y1
    satelite2.pos.z += 0.1
    
    # Atualiza a coordenada x do PRIMEIRO satélite e inverte a direção ao atingir os limites
    x1 += direcao1
    if x1 >= 20 or x1 <= 0:
        direcao1 *= -1
    
    # Atualiza a coordenada x do SEGUNDO satélite e inverte a direção ao atingir os limites
    x2 += direcao2
    if x2 >= 20 or x2 <= 0:
        direcao2 *= -1





