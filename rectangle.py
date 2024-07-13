from setup import *
class Rectangle():
    def __init__(self, size, position, color, image):
        self.image = image
        self.rotation = 0
        self.is_updating = True
        self.size = size
        self.position = position
        self.transparency = 255
        self.color = color
        if not image:
            self.rect = pygame.Surface(size)
            self.rect.fill(self.color)
            self.position = self.position[0] - self.size[0] / 2, self.position[1] - self.size[1] / 2
            self.rect_rect = self.rect.get_rect()
            self.rect_rect.center = position
        else:
            self.position = self.position[0] - self.size[0] / 2, self.position[1] - self.size[1] / 2
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, size)
            self.image_rect = self.image.get_rect()
            self.image_rect.center = position
        

    def update(self):
        if self.is_updating:
            surface.fill((0, 0, 0, 0))  # Clear the surface
            #some transforming:
            col = list(self.color)
            col.append(self.transparency)
            col = tuple(col)
            surface.set_alpha(self.transparency)
            if self.image != False:
                surface.blit(self.image, (self.image_rect.x,self.image_rect.y))
            else:
                surface.blit(self.rect, (self.rect_rect.x,self.rect_rect.y))
            screen.blit(surface, (0, 0))

    def set_transparency(self, transparency):
        self.transparency = transparency

    def change_position(self, xc, yc):
        if self.image == False:
            self.rect_rect.x += xc
            self.rect_rect.y += yc 
        else:
            self.image_rect.x += xc
            self.image_rect.y += yc

    def kill(self):
        self.is_updating = False

    def set_rotation(self, rot):
        if self.image == False:
            self.rect = pygame.transform.rotate(self.rect, rot)
        else:
            self.image = pygame.transform.rotate(self.image, rot)
    
    def get_pos(self):
        if self.image == False:
            return self.rect_rect.center
        else:
            return self.image_rect.center

    def get_point_colide(self,point):
        if self.image != False:
            return self.image_rect.collidepoint(point)
        else:
            return self.rect_rect.collidepoint(point)