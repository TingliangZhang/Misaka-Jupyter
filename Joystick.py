import pygame
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

pygame.joystick.Joystick(0).get_axis(3)