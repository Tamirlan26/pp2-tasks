import pygame
pygame.init()
a=int(input())
b=int(input())
window=pygame.display.set_mode((a,b))
pygame.display.set_caption("My project")
clock=pygame.time.Clock()


player=pygame.Rect(200,300,40,55)
player2=pygame.Rect(500,650,70,90)

def draw():
    window.fill((46, 184, 181))
    pygame.draw.rect(window,(212, 72, 100),player)
    pygame.draw.rect(window,(114, 204, 112),player2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        '''    
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_UP,pygame.K_w):
                player.y-=5
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN,pygame.K_s):
                player.y+=5
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT,pygame.K_a):
                player.x-=5
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_RIGHT,pygame.K_d):
                player.x+=5
        '''
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y-=5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y+=5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x-=5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x+=5
    draw()
    pygame.display.update()
    clock.tick(60)