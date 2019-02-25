# pygameモジュールの活用
import pygame
# インポートした全てのpygameモジュールを初期化。
pygame.init()

# 変数（オブジェクト）= pygame.displayモジュールのset_modeメソッド（サイズ）
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
# 変数clock = pygame.timeモジュールのClockメソッド()
clock = pygame.time.Clock()

# x.yは初期の立ち位置に関しての数字
x = 200
y = 40
# キャラクターの大きさ
width = 64
height = 64
# velsotyの略でスピード
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
# 右に１０で右に１０進む　１０pixel
walkCount = 0

# redrawGameWindowメソッドを定義
def redrawGameWindow():
    # global変数 walkCount
    global walkCount
    # blitは既に定義(bgイメーシ, (0,0)position)
    win.blit(bg, (0,0))
    
    if walkCount + 1 >= 27:
        walkCount = 0
    # *walkLeftはメソッドの１種類
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        win.blit(char, (x,y))
    
    pygame.display.update()


#mainloop
# 変数run
run = True

while run:
    # clock.tickメソッド
    clock.tick(27)

    # pygame.eventモジュールのgetメソッド()
    # ※getメソッドの補足
    # 辞書オブジェクトのget()メソッドを使うと、
    # キーが存在しない場合にエラーを発生させずに任意の値（デフォルト値）を取得できる。
    for event in pygame.event.get():
        # type QUITは？？？
        if event.type == pygame.QUIT:
            run = False

# 　　ボタンを押すことに関してのget_pressed()メソッド
    keys = pygame.key.get_pressed()
    # K_LEFTは定義されていないが
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        # keys変数[]はlist　
        # K_SPACEはスペースバー

        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            # negはマイナスの意味
            # マイナスのときは上に進む、プラスのときは下に進む
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # redrawGameWindow()で始まり、同じもので終わらせるのが決まり
    redrawGameWindow()

pygame.quit()


