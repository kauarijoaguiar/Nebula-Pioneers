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
inimigo_spawn_chance = 0.02

# Pontuação
pontuacao = 0

def update():
    global nave_x, tiros, inimigos, pontuacao

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

    # Spawn de inimigos aleatórios(NAO CONSIGO ARRUMAR ESSA FUNÇÃO)
    #if pyxel.frame_count % 30 == 0 and pyxel.random() < inimigo_spawn_chance:
    #    inimigos.append((pyxel.random(WINDOW_WIDTH - 16), 0))

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
            and inimigo[0] <= nave_x + 16
            and inimigo[1] >= nave_y
            and inimigo[1] <= nave_y + 16
        ):
            inimigos.remove(inimigo)
            pyxel.quit()

def draw(self, camera=pyxel):
    x,y, _right, _top=self.bb
    camera.blt(x,y,0,0,0,16,16)

def draw():
    pyxel.cls(0)

    # Desenha estrelas
    for i in range(0, 200): 
        pyxel.pset(pyxel.rndi(0, 200), pyxel.rndi(0, 200), pyxel.rndi(5, 7)) 
    # Desenhar nave
    #pyxel.rect(nave_x, nave_y, 16, 16, 6)
    pyxel.load("navezinha.pyxres")
    pyxel.blt(nave_x, nave_y, 0, 0, 128, 128, 16, 7)
    # Desenhar tiros
    for tiro in tiros:
        pyxel.rect(tiro[0], tiro[1], 2, 5, 4)

    # Desenhar inimigos
    for inimigo in inimigos:
        pyxel.rect(inimigo[0], inimigo[1], 16, 16, 8)

    # Desenhar pontuação
    pyxel.text(5, 5, f"Pontos: {pontuacao}", 7)

pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
pyxel.run(update, draw)
