from setup import *
from rectangle import Rectangle
button1 = Rectangle((width/5,height/15),(width/2,height/2),(0,0,0),"button.png")
rect2 = Rectangle((50,50),(300,300),(255,255,255),False)

while True:
    clock.tick(30)
    mous_pos = pygame.mouse.get_pos()
    rect2.rect_rect.center = mous_pos
    print(mous_pos,rect2.rect_rect.center)
    print(rect2.get_colliding_with(button1))
    if button1.get_point_colide(mous_pos):
        button1.set_transparency(100)
    else:
        button1.set_transparency(255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #here ia the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.get_point_colide(mous_pos):
                print("click")
    screen.fill((0,0,0))
    rect2.update()
    button1.update()
    pygame.display.update()