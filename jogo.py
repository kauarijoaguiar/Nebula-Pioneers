import pyxel
import random

WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120

nave_x = WINDOW_WIDTH // 2
nave_y = WINDOW_HEIGHT - 20
nave_speed = 2

tiros = []
tiro_speed = 4

inimigos = []
inimigo_speed = 1
inimigo_spawn_chance = 0.5

pontuacao = 0

nivel=1

naves_saidas = 0


menu = 0

def iniciar_jogo():
    global nave_x, tiros, inimigos, pontuacao, nivel, menu
    nave_x = WINDOW_WIDTH // 2
    tiros = []
    inimigos = []
    pontuacao = 0
    nivel = 1
    menu=0
    
def update():
    global nave_x, tiros, inimigos, pontuacao, nivel, inimigo_speed, naves_saidas, menu
    if menu==0:
        if pyxel.btnp(pyxel.KEY_RETURN):
            menu = 1
        
    elif menu == 1:
        if pyxel.btn(pyxel.KEY_LEFT) and nave_x > 0:
            nave_x -= nave_speed
        if pyxel.btn(pyxel.KEY_RIGHT) and nave_x < WINDOW_WIDTH - 16:
            nave_x += nave_speed

        
        if pyxel.btnp(pyxel.KEY_SPACE):
            tiros.append((nave_x + 13, nave_y))

        for i in range(len(tiros)):
            tiros[i] = (tiros[i][0], tiros[i][1] - tiro_speed)

        tiros = [tiro for tiro in tiros if tiro[1] > 0]

        for i in range(len(inimigos)):
            inimigos[i] = (inimigos[i][0], inimigos[i][1] + inimigo_speed)


        for inimigo in inimigos:
            if inimigo[1] >= WINDOW_HEIGHT:
                naves_saidas += 1
                inimigos.remove(inimigo)
        

        if pyxel.frame_count % 30 == 0 and random.random() < inimigo_spawn_chance:
            novo_inimigo_x = random.randint(0, WINDOW_WIDTH - 16)
            inimigos.append((novo_inimigo_x, 0))
            
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

        for inimigo in inimigos:
            if (
                inimigo[0] >= nave_x
                and inimigo[0] <= nave_x + 15
                and inimigo[1] >= nave_y
                and inimigo[1] <= nave_y + 15
            ):
                inimigos.remove(inimigo)
                menu = 2
                
                
                
            #Nivel 2
            #aumento de velocidade
            if pontuacao==200:
                inimigo_speed = 1.5
                nivel=2
            #Nivel 3
            #aumento de velocidade
            if pontuacao==500:
                inimigo_speed = 2
                nivel=3
            #Nivel 4
            #aumento de velocidade
            if pontuacao==700:
                inimigo_speed = 2.5
                nivel=4
            #Nivel 5
            #aumento de velocidade
            if pontuacao==1000:
                inimigo_speed = 3
                nivel=5
            
            if naves_saidas >= 5:
                menu = 2
                
                
    elif menu == 2:
        if pyxel.btnp(pyxel.KEY_RETURN):
            iniciar_jogo()
            menu = 1
        if pyxel.btnp(pyxel.KEY_S):
            pyxel.quit()
        
def draw(self, camera=pyxel):
    x,y, _right, _top=self.bb
    camera.blt(x,y,0,0,0,16,16)

def draw():
    global menu
    if menu==0:
        pyxel.cls(0)
        pyxel.text(15, 45, 'Aperte \n\n"Enter"\n\n para comecar uma aventura espacial!', pyxel.frame_count % 16)
    elif menu == 1:
        pyxel.cls(0)
        for i in range(0, 200): 
            pyxel.pset(pyxel.rndi(0, 200), pyxel.rndi(0, 200), pyxel.rndi(5, 7))
            
        pyxel.load("naves.pyxres")
        for inimigo in inimigos:
            pyxel.blt(inimigo[0], inimigo[1], 0, 27,128,52,27,7)
            
        pyxel.blt(nave_x, nave_y, 0, 1, 128, 27, 15, 7)
        
        for tiro in tiros:
            pyxel.rect(tiro[0], tiro[1], 2, 5, 4)

        pyxel.text(5, 5, f"Pontos: {pontuacao}", 7)
        
        pyxel.text(15, 15, f"Nivel: {nivel}", 7)

    elif menu == 2:
        pyxel.cls(0)
        pyxel.text(15, 45, 'GAME OVER!', pyxel.frame_count % 16)
        pyxel.text(5, 5, 'Aperte "ENTER" para reiniciar\n Aperte "S" para sair', 7)

pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
pyxel.run(update, draw)