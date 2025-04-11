''' Tarje Carlsen, Tristan Natvig '''

import pygame

class controller():
    '''Sets up player controlls and returning boolean for if the player is thrusting and integer value for rotation. Gets in what keys
    should be used in the arguments'''
    def update(keys, left, right, up, down):
        rotation = 0
        thrust_engaged = False
        if keys[left]:
            rotation = 2
        elif keys[right]:
            rotation = -2
        if keys[up]:
            thrust_engaged = True
        if keys[down]:
            print("test")

        return rotation, thrust_engaged
