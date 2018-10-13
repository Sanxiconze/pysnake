#初始化
import pygame
import random
pygame.init()


#建立画布
blocksize = 20
W = blocksize*40
H =  blocksize*30

screen_size = (W,H)
screen = pygame.display.set_mode(screen_size,)
#方块坐标
def point(x,y):
    x=x*blocksize
    y=y*blocksize
    return [x,y]
#画方块
def draw(point,color):
    x=point[0]
    y=point[1]
    pygame.draw.rect(screen,color,(x,y,blocksize,blocksize))
#蛇吃到食物
def eated(snake,food):
    if snake[0]==food[0] and snake[1] == food [1]:
        return True
    else:
        return False

def drop(head,bodys):
    if head[0]<0 or head[1]<0 or head[0]>W or head[1]>H:
        return True
    else:
        for body in bodys:
            if head == body:
                return True

    return False
#生成食物
def food_get(head,bodys):
    while 1:
        default = False
        termfood =point(random.randint(0,int(W/blocksize)-1),random.randint(0,int(H/blocksize)-1))
        for body in bodys:
            if termfood == body:
                default = True
                break
        if not default:
            break

    return termfood


#生成基本因子
head = point(random.randint(int(W/blocksize)/2,int(W/blocksize)-1),random.randint(0,int(H/blocksize)-1))
head_color = (255,255,0)
snakebody = []
snakebody_color=(200,200,200)
food = food_get(head,snakebody)
food_color = (100,200,102)
#确定初始方向
direct ='left'
chargedirect = direct

#游戏大循环
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        print (event)
    #退出
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #键盘按键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                chargedirect='right'
            elif event.key == pygame.K_LEFT:
                chargedirect = 'left'
            elif event.key == pygame.K_UP:
                chargedirect = 'up'
            elif event.key == pygame.K_DOWN:
                chargedirect = 'down'
#确定新方向
    if chargedirect == 'left' and direct != 'right' :
        direct = chargedirect
    elif chargedirect == 'right' and direct != 'left':
        direct = chargedirect
    elif chargedirect == 'up' and direct != 'down':
        direct = chargedirect
    elif chargedirect == 'down' and direct != 'up':
        direct = chargedirect
#蛇头移动
    if len(snakebody) == 0:
        direct = chargedirect
    headcopy = list(head)

    if direct == 'left' :
        head[0] -= blocksize
    elif direct == 'right' :
        head[0] += blocksize
    elif direct == 'up':
        head[1] -= blocksize
    elif direct == 'down' :
        head[1] += blocksize


#判断碰撞
    if drop(head,snakebody):
        exit()
#判断是否吃到食物
    if not eated(head,food):

        snakebody.insert(0,headcopy)
        snakebody.pop()
    else:
        snakebody.insert(0,headcopy)
        food=food_get(head,snakebody)

#刷新窗体
    pygame.draw.rect(screen,(255,255,255), (0, 0, W, H))
    for body in snakebody:
        draw(body,snakebody_color)

    draw(head,head_color)
    draw(food,food_color)
    pygame.display.flip()

    clock.tick(10)




