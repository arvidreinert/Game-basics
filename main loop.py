#an example of a button and a mainloop
from setup import *
from rectangle import Rectangle
#the rectangles position in the middle
x = Rectangle((width/5,height/15),(width/2,height/2),(250,0,0),False)
joysticks = []

while True:
    clock.tick(30)
    #event handler(button):
    mous_pos = pygame.mouse.get_pos()
    if x.get_point_colide(mous_pos):
        x.set_transparency(100)
    else:
        x.set_transparency(255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #here ia the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x.get_point_colide(mous_pos):
                print("click")
        #here is the controller manager can also be used by multiple controlers
        if pygame.joystick.get_count() >= 1 and joysticks == []:
            joy = pygame.joystick.Joystick(0)
            joy = (joy,joy.get_name())
            #call with [0]

            if len(joysticks) <= 1 and joy not in joysticks:
                print('controller added')
                joy = pygame.joystick.Joystick(0)
                joy.init()
                #feels like a litle punch:joy.rumble(1,1,8)
                joysticks.append(joy)

        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[0]
    # here the controller input is used:
    if joysticks[0].get_button(3) == 1:
        print("x")
        x0,y0 = x.get_pos()
        x1,y1 = mous_pos
        #<math.atan2(y1-y0,x1-x0)-(math.pi/2)
        x.set_rotation(1)


    #screen things and draw the button:
    screen.fill((0,0,0))
    x.update()
    pygame.display.update()