import pygame

class controller():
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
