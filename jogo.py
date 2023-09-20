import pyxel
import random

# Tamanho da janela do jogo
WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120

# Variáveis da nave
nave_x = WINDOW_WIDTH // 2
nave_y = WINDOW_HEIGHT - 20
nave_speed = 2

# Variáveis dos tiros
tiros = []
tiro_speed = 4

# Variáveis dos inimigos
inimigos = []
inimigo_speed = 1
inimigo_spawn_chance = 0.5

# Pontuação
pontuacao = 0

#Nivel
nivel=1

#contador
contador=0

def iniciar_jogo():
    global nave_x, tiros, inimigos, pontuacao, estado_atual,nivel,contador
    nave_x = WINDOW_WIDTH // 2
    tiros = []
    inimigos = []
    pontuacao = 0
    estado_atual = ESTADO_JOGO
    nivel=0
    contador=0
def update():
    
    global nave_x, tiros, inimigos, pontuacao, nivel, inimigo_speed,contador

    # Movimento da nave
    if pyxel.btn(pyxel.KEY_LEFT) and nave_x > 0:
        nave_x -= nave_speed
    if pyxel.btn(pyxel.KEY_RIGHT) and nave_x < WINDOW_WIDTH - 16:
        nave_x += nave_speed

    # Atirar
    if pyxel.btnp(pyxel.KEY_SPACE):
        tiros.append((nave_x + 6, nave_y))

    # Movimento dos tiros
    for i in range(len(tiros)):
        tiros[i] = (tiros[i][0], tiros[i][1] - tiro_speed)

    # Remover tiros que saíram da tela
    tiros = [tiro for tiro in tiros if tiro[1] > 0]

    # Movimento dos inimigos
    for i in range(len(inimigos)):
        inimigos[i] = (inimigos[i][0], inimigos[i][1] + inimigo_speed)

    # Remover inimigos que saíram da tela
    inimigos = [inimigo for inimigo in inimigos if inimigo[1] < WINDOW_HEIGHT]

    # Spawn de inimigos aleatórios
    if pyxel.frame_count % 30 == 0 and random.random() < inimigo_spawn_chance:
        novo_inimigo_x = random.randint(0, WINDOW_WIDTH - 16)
        inimigos.append((novo_inimigo_x, 0))
        
    # Colisão dos tiros com inimigos
    for tiro in tiros:
        for inimigo in inimigos:
            if (
                tiro[0] >= inimigo[0]
                and tiro[0] <= inimigo[0] + 16
                and tiro[1] <= inimigo[1] + 16
            ):
                tiros.remove(tiro)
                inimigos.remove(inimigo)
                pontuacao += 10

    # Colisão dos inimigos com a nave
    for inimigo in inimigos:
        if (
            inimigo[0] >= nave_x
            and inimigo[0] <= nave_x + 15
            and inimigo[1] >= nave_y
            and inimigo[1] <= nave_y + 15
        ):
            inimigos.remove(inimigo)
            pyxel.quit()
            
        #Nivel 2
        #aumento de velocidade
        if pontuacao==30:
            inimigo_speed = 1.5
            nivel=2
        #Nivel 3
        #aumento de velocidade
        if pontuacao==50:
            inimigo_speed = 2
            nivel=3
        #Nivel 4
        #aumento de velocidade
        if pontuacao==60:
            inimigo_speed = 2.5
            nivel=4
        #Nivel 5
        #aumento de velocidade
        if pontuacao==100:
            inimigo_speed = 3
            nivel=5
        
def draw(self, camera=pyxel):
    x,y, _right, _top=self.bb
    camera.blt(x,y,0,0,0,16,16)

def draw():
    pyxel.cls(0)
    # Desenha estrelas
    for i in range(0, 200): 
        pyxel.pset(pyxel.rndi(0, 200), pyxel.rndi(0, 200), pyxel.rndi(5, 7))
        
    # Desenhar inimigos
    pyxel.load("inimigo.pyxres")
    for inimigo in inimigos:
        pyxel.blt(inimigo[0], inimigo[1], 0, 1,128,15,15,7)
        
    # Desenhar nave
    #pyxel.rect(nave_x, nave_y, 16, 16, 6)
    pyxel.load("navezinha.pyxres")
    pyxel.blt(nave_x, nave_y, 0, 1, 128, 15, 15, 7)
    
    # Desenhar tiros
    for tiro in tiros:
        pyxel.rect(tiro[0], tiro[1], 2, 5, 4)

    # Desenhar pontuação
    pyxel.text(5, 5, f"Pontos: {pontuacao}", 7)
    
    pyxel.text(15, 15, f"Nivel: {nivel}", 7)
    

pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
pyxel.run(update, draw)