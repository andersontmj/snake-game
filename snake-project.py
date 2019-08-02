import sys, pygame, time, random

"""
Hello world, this is my first project
with a python language. Have a good time!
"""

DIFFICULTY = 1 # 1 ... 10
START_LENGTH = 10
WAIT	= 0.1 / DIFFICULTY
RADIUS	= 10
RES	= [800, 600]
WALL	= []
APPLE     = ()

pygame.init()

SCREEN = pygame.display.set_mode(RES)
pygame.display.set_caption("PROJETO SNAKE")

class Mob():
    def __init__(self):
        self.headx = 100
        self.heady = 100
        self.length = START_LENGTH
        self.elements = [[self.headx, self.heady]]

        while len(self.elements) != (self.length - 1):
            self.elements.append([self.headx, self.heady])
        self.speed = [RADIUS * 2, 0]
        pygame.draw.circle(SCREEN, (50,205,50), (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()

    def move(self):
        
        pygame.draw.circle(SCREEN, (0, 0, 0), (self.elements[-1][0],
            self.elements[-1][1]), RADIUS)
        self.elements.pop()
        self.headx += self.speed[0]
        self.heady += self.speed[1]
        self.elements = [[self.headx, self.heady]] + self.elements[0:]
        self.check_dead()
        for element in self.elements[1:]:
            pygame.draw.circle(SCREEN, (50,205,50), (element[0], element[1]),
                RADIUS)
        pygame.draw.circle(SCREEN, (0,128,0), (self.headx, self.heady),
            RADIUS)
        pygame.display.flip()
        self.check_apple()

    def check_dead(self):
        """Checando colisão 
        """
        if [self.headx, self.heady] in self.elements[1:]:
            exit_dead()
        if [self.headx, self.heady] in WALL:
            exit_dead()

    def check_apple(self):
        if (self.headx, self.heady) == APPLE:
            self.elements.append(self.elements[-1])
            create_apple()

def draw_map():
    """ Definindo os limites do mapa
    """
    for n in range(20, RES[0], 20): #horizontais
        pygame.draw.rect(SCREEN, (210,105,30), (n, 20, 10, 10), 5)
        WALL.append([n, 20])
        pygame.draw.rect(SCREEN, (210,105,30),(n, RES[1] - 20, 10, 10), 5)
        WALL.append([n, RES[1] - 20])
    
    for n in range(20, RES[1], 20): #verticais
        pygame.draw.rect(SCREEN, (210,105,30),(20, n, 10, 10), 5)
        WALL.append([20, n])
        pygame.draw.rect(SCREEN, (210,105,30), (RES[0] - 20, n, 10, 10), 5)
        WALL.append([RES[0] - 20 , n])
    pygame.display.flip()

def create_apple():
    """Criando a maçã
    """
    global APPLE
    APPLE = ()
    while ( list(APPLE) in WALL ) or ( list(APPLE) in SNAKE.elements) or (not APPLE):
        APPLE = (random.randrange(40, RES[0] - 40 , 20),
            (random.randrange(40, RES[1] - 40 , 20)))
    pygame.draw.circle(SCREEN, (255, 0, 0), APPLE, RADIUS)
    pygame.display.flip()
    
def event_loop():
    """Adicionando eventos do teclado
    """
    while True:
        time.sleep(WAIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_DOWN)	and \
                    (SNAKE.speed != [0, -2*RADIUS]):
                    SNAKE.speed = [0, 2*RADIUS]
                elif (event.key == pygame.K_UP) and \
                    (SNAKE.speed != [0, 2*RADIUS]):
                    SNAKE.speed = [0, -2*RADIUS]
                elif (event.key == pygame.K_RIGHT) and \
                    (SNAKE.speed != [-2* RADIUS, 0]):
                    SNAKE.speed = [2*RADIUS, 0]
                elif (event.key == pygame.K_LEFT) and \
                    (SNAKE.speed != [2* RADIUS, 0]):
                    SNAKE.speed = [-2*RADIUS, 0]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        SNAKE.move()

def exit_dead():
    """Apresentando o placar final e finalizando o jogo
    """
    print("Dificuldade:  \t%d" % DIFFICULTY)
    print("Maçãs comidas: \t%d" % (len(SNAKE.elements) - START_LENGTH + 1))
    print("Pontuação total:%d" % ((len(SNAKE.elements) - START_LENGTH + 1) * DIFFICULTY))
    time.sleep(1)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    draw_map()
    SNAKE = Mob()
    create_apple()
    event_loop()
