''' Tarje Carlsen, Tristan Natvig '''

import pygame

class Rotatable(object):
    '''Rotates a object with inheritence from object class. Sets the angle to be += angle. Sets image to rotate with the pygame.transform.rotate() method
    sets the new rect of the rotated object.'''
    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)