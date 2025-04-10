import pygame

class controller():
    def update(keys, left, right, up, down):
        rotation = 0
        if keys[left]:
            rotation = 2
        elif keys[right]:
            rotation = -2
        if keys[up]:
            print("test")
        if keys[down]:
            print("test")

        return rotation
