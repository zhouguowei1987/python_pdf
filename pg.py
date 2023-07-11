# 导入所需的模块
import sys
import pygame

# 使用pygame之前必须初始化
pygame.init()
# 设置主屏窗口
screen = pygame.display.set_mode((500, 500))

# 填充主窗口的背景颜色，参数值RGB（颜色元组）
# screen.fill((156, 156, 156))
# screen.fill('white')

# 设置窗口的标题，即游戏名称
pygame.display.set_caption('hello world')

# # 获取以毫秒为单位的时间
# t = pygame.time.get_ticks()  # 该时间指的从pygame初始化后开始计算，到调用该函数为止
# print(t)
# t1 = pygame.time.wait(3000)  # 暂停游戏3000毫秒
# print(t1)

# # 获取以毫秒为单位的时间
# t = pygame.time.get_ticks()  # 该时间指的从pygame初始化后开始计算，到调用该函数为止
# t1 = pygame.time.delay(3000)  # 暂停游戏3000毫秒
# print(t1)

# # 引入字体类型
# f = pygame.font.Font('./simsun.ttf', 50)
# # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
# # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
# text = f.render("C语言中文网", True, (255, 0, 0), (0, 0, 0))
# # 获得显示对象的rect区域坐标
# textRect = text.get_rect()
# # 设置显示对象居中
# textRect.center = (200, 200)
# # 将准备好的文本信息，绘制到主屏幕 Screen 上。
# screen.blit(text, textRect)

# # 创建一个 50*50 的图像,并优化显示
# face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
# # 填充颜色
# face.fill(color='pink')

# 加载一张图片
image_surface = pygame.image.load("./logo.png").convert()
rect1 = pygame.Rect(50, 0, 100, 50)
# 在原图的基础上创建一个新的子图（surface对象）
image_child = image_surface.subsurface(rect1)
rect2 = image_child.get_rect()
# 输出的矩形大小为 100*50
print(rect2)

# image_new = pygame.transform.scale(image_surface, (300, 300))
# # 对新生成的图像进行旋转至45度
# image_1 = pygame.transform.rotate(image_new, 45)
# # 使用rotozoom() 旋转 0 度，将图像缩小0.5倍
# image_2 = pygame.transform.rotozoom(image_1, 0, 1)
# rect(left,top,width,height)指定图片上某个区域
# special_flags功能标志位,指定颜色混合模式，默认为 0 表示用纯色填充
# image_2.fill((0, 0, 0), rect=(100, 100, 100, 50), special_flags=0)
# 200,100 表示图像在水平、垂直方向上的偏移量，以左上角为坐标原点
# image_2.scroll(100, 50)

# 创建时钟对象（控制游戏的FPS）
clock = pygame.time.Clock()

# 固定代码段，实现点击"X"号退出界面的功能，几乎所有的pygame都会使用该段代码
# i = 0
while True:
    # print(i)
    # i = i + 1
    # 通过时钟对象，指定循环频率，每秒循环60次
    clock.tick(60)
    # 循环获取事件，监听事件状态
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 终止程序，确保退出程序
            sys.exit()
    # 将绘制的图像添加到主屏幕上，(100,100)是位置坐标，显示屏的左上角为坐标系的(0,0)原点
    # screen.blit(face, (100, 100))
    # 将图像放置在主屏幕上
    # screen.blit(image_2, (0, 0))
    screen.blit(image_child, rect1)
    pygame.display.flip()  # 更新屏幕内容
