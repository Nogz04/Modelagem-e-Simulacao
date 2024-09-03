Web VPython 3.2

# Criação das paredes e teto da "caixa"
paredeEsquerda = box(pos=vector(-20, 0, 0), size=vector(1, 20, 0.5), color=color.black)
paredeDireita = box(pos=vector(20, 0, 0), size=vector(1, 20, 0.5), color=color.black)
teto = box(pos=vector(0, 10, 0), size=vector(40, 1, 0.5), color=color.white)
chao = box(pos=vector(0, -10, 0), size=vector(40, 1, 0.5), color=color.white)

# Criação das esferas (bolas) com cores variadas
bola1 = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue, make_trail=True)
bola2 = sphere(pos=vector(-5, -5, 0), radius=1, color=color.green, make_trail=True)
bola3 = sphere(pos=vector(5, 5, 0), radius=1, color=color.yellow, make_trail=True)
bola4 = sphere(pos=vector(-10, 5, 0), radius=1, color=color.orange, make_trail=True)
bola5 = sphere(pos=vector(10, -5, 0), radius=1, color=color.purple, make_trail=True)
bola6 = sphere(pos=vector(0, 7, 0), radius=1, color=color.cyan, make_trail=True)
bola7 = sphere(pos=vector(-7, 7, 0), radius=1, color=color.magenta, make_trail=True)
bola8 = sphere(pos=vector(7, -7, 0), radius=1, color=color.white, make_trail=True)
bola9 = sphere(pos=vector(5, 0, 0), radius=1, color=color.red, make_trail=True)
bola10 = sphere(pos=vector(-5, 0, 0), radius=1, color=color.orange, make_trail=True)

# Inicialização das velocidades das bolinhas
# Apenas a bola1 começa com movimento, as outras estão paradas (velocidade 0)
velocidade1 = vector(15, 10, 0)
velocidade2 = vector(0, 0, 0)
velocidade3 = vector(0, 0, 0)
velocidade4 = vector(0, 0, 0)
velocidade5 = vector(0, 0, 0)
velocidade6 = vector(0, 0, 0)
velocidade7 = vector(0, 0, 0)
velocidade8 = vector(0, 0, 0)
velocidade9 = vector(0, 0, 0)
velocidade10 = vector(0, 0, 0)

# Função para detectar colisões entre duas bolas e trocar suas velocidades
def colisao_bolas(bolaA, bolaB, velA, velB):
    # Verifica se a distância entre as bolas é menor ou igual à soma dos raios (indica colisão)
    if mag(bolaA.pos - bolaB.pos) <= bolaA.radius + bolaB.radius:
        # Troca as velocidades entre as bolas, o que causa o efeito de "rebote"
        return velB, velA
    else:
        # Se não há colisão, mantém as velocidades inalteradas
        return velA, velB

# Loop principal de simulação
while True:
    rate(120)  # Controla a taxa de quadros por segundo (FPS)
    
    # Atualiza as posições das bolas com base nas suas velocidades
    bola1.pos += velocidade1 * 0.01
    bola2.pos += velocidade2 * 0.01
    bola3.pos += velocidade3 * 0.01
    bola4.pos += velocidade4 * 0.01
    bola5.pos += velocidade5 * 0.01
    bola6.pos += velocidade6 * 0.01
    bola7.pos += velocidade7 * 0.01
    bola8.pos += velocidade8 * 0.01
    bola9.pos += velocidade9 * 0.01
    bola10.pos += velocidade10 * 0.01
    
    # Verifica colisão das bolas com as paredes e inverte a direção
    # Se a posição da bola mais o seu raio atinge a parede, inverte a velocidade
    if abs(bola1.pos.x) >= 20 - bola1.radius:
        velocidade1.x *= -1
    if abs(bola1.pos.y) >= 10 - bola1.radius:
        velocidade1.y *= -1

    if abs(bola2.pos.x) >= 20 - bola2.radius:
        velocidade2.x *= -1
    if abs(bola2.pos.y) >= 10 - bola2.radius:
        velocidade2.y *= -1

    if abs(bola3.pos.x) >= 20 - bola3.radius:
        velocidade3.x *= -1
    if abs(bola3.pos.y) >= 10 - bola3.radius:
        velocidade3.y *= -1

    if abs(bola4.pos.x) >= 20 - bola4.radius:
        velocidade4.x *= -1
    if abs(bola4.pos.y) >= 10 - bola4.radius:
        velocidade4.y *= -1

    if abs(bola5.pos.x) >= 20 - bola5.radius:
        velocidade5.x *= -1
    if abs(bola5.pos.y) >= 10 - bola5.radius:
        velocidade5.y *= -1

    if abs(bola6.pos.x) >= 20 - bola6.radius:
        velocidade6.x *= -1
    if abs(bola6.pos.y) >= 10 - bola6.radius:
        velocidade6.y *= -1

    if abs(bola7.pos.x) >= 20 - bola7.radius:
        velocidade7.x *= -1
    if abs(bola7.pos.y) >= 10 - bola7.radius:
        velocidade7.y *= -1

    if abs(bola8.pos.x) >= 20 - bola8.radius:
        velocidade8.x *= -1
    if abs(bola8.pos.y) >= 10 - bola8.radius:
        velocidade8.y *= -1

    if abs(bola9.pos.x) >= 20 - bola9.radius:
        velocidade9.x *= -1
    if abs(bola9.pos.y) >= 10 - bola9.radius:
        velocidade9.y *= -1

    if abs(bola10.pos.x) >= 20 - bola10.radius:
        velocidade10.x *= -1
    if abs(bola10.pos.y) >= 10 - bola10.radius:
        velocidade10.y *= -1

    # Verifica colisões entre todas as bolas e troca as velocidades
    # As bolas que colidem ganham movimento, enquanto as que não colidem permanecem paradas
    velocidade1, velocidade2 = colisao_bolas(bola1, bola2, velocidade1, velocidade2)
    velocidade1, velocidade3 = colisao_bolas(bola1, bola3, velocidade1, velocidade3)
    velocidade1, velocidade4 = colisao_bolas(bola1, bola4, velocidade1, velocidade4)
    velocidade1, velocidade5 = colisao_bolas(bola1, bola5, velocidade1, velocidade5)
    velocidade1, velocidade6 = colisao_bolas(bola1, bola6, velocidade1, velocidade6)
    velocidade1, velocidade7 = colisao_bolas(bola1, bola7, velocidade1, velocidade7)
    velocidade1, velocidade8 = colisao_bolas(bola1, bola8, velocidade1, velocidade8)
    velocidade1, velocidade9 = colisao_bolas(bola1, bola9, velocidade1, velocidade9)
    velocidade1, velocidade10 = colisao_bolas(bola1, bola10, velocidade1, velocidade10)
    
    # Troca de velocidades entre bolas para criar movimento contínuo nas que colidem
    velocidade2, velocidade3 = colisao_bolas(bola2, bola3, velocidade2, velocidade3)
    velocidade2, velocidade4 = colisao_bolas(bola2, bola4, velocidade2, velocidade4)
    velocidade2, velocidade5 = colisao_bolas(bola2, bola5, velocidade2, velocidade5)
    velocidade2, velocidade6 = colisao_bolas(bola2, bola6, velocidade2, velocidade6)
    velocidade2, velocidade7 = colisao_bolas(bola2, bola7, velocidade2, velocidade7)
    velocidade2, velocidade8 = colisao_bolas(bola2, bola8, velocidade2, velocidade8)
    velocidade2, velocidade9 = colisao_bolas(bola2, bola9, velocidade2, velocidade9)
    velocidade2, velocidade10 = colisao_bolas(bola2, bola10, velocidade2, velocidade10)
    
    velocidade3, velocidade4 = colisao_bolas(bola3, bola4, velocidade3, velocidade4)
    velocidade3, velocidade5 = colisao_bolas(bola3, bola5, velocidade3, velocidade5)
    velocidade3, velocidade6 = colisao_bolas(bola3, bola6, velocidade3, velocidade6)

