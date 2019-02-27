# update()はどんな時に記載しなくてはいけないのか???
# If there are actions is going on at window,have to write update().
import pygame
pygame.init()

# pygame.display.set_mode - display描写用のウィンドウやスクリーンを初期化する。
win = pygame.display.set_mode((500,480))
# pygame.displayモジュールのset_captionメソッド（ゲームタイトルの設定）
pygame.display.set_caption("First Game")

# 変数walkRight　=　[pygame.imageモジュールのloadメソッド(画像)]
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# 変数bg = モジュールのloadメソッド(背景)
bg = pygame.image.load('bg.jpg')
# 変数char = モジュールのloadメソッド(正面画像)
char = pygame.image.load('standing.png')
# タイム計測を助けるclock()メソッド
clock = pygame.time.Clock()

# 多重継承：複数の基底クラスを引き継ぐこと
# class クラス名(基底クラス名1,基底クラス名2,・・・)
# playerクラス（objectクラス）
class player(object):
    def __init__(self,x,y,width,height):
        # ｘ、ｙは最初の立ち位置
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # velはスピード
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        # walkcountは距離
        self.walkCount = 0
        self.jumpCount = 10
    
    # drawは、pygameの図形描写用モジュールのクラス
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            # blitメソッド(bgイメージ画像[(walicount変数（距離）/３)],(x,y)position)
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))


# redrawGameWindowは???
def redrawGameWindow():
    # blit() :これはある絵からべつの絵にピクセルを複写する
    # blitは既に定義(bgイメーシ, (0,0)position)
    win.blit(bg, (0,0))
    # drawは、pygameの図形描写用モジュールのクラス
    # manオブジェクト.personクラスのdrawメソッド(win引数)
    man.draw(win)
    
    pygame.display.update()


#mainloop
# 変数man = playerクラス
man = player(200, 410, 64,64)
# run変数(走るという行為のオブジェクト)
run = True
while run:
    # clock.tick()関数　または　モジュール
    clock.tick(27)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()


