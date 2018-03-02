import pygame as pg
from pygame.locals import *
from objects import *

alex = Subject('07', 'Alex', 'Nakagawa')


def test_subject():
    print('test_subject_no_id():')
    print(alex)


def test_variations():
    print('test_variations():')
    alex.new_variation()
    alex.new_variation()
    alex.new_variation()

    print('Variation dictionary:', alex.display_variations())
    print('First variation:', alex.variations[1])
    print('Second variation:', alex.variations[2])
    print('Third variation:', alex.variations[3])


def test_trials():
    vars = alex.variations
    for i in range(5):
        vars[i].new_trial()

if __name__ == '__main__':
    print('This is a test...\n')
    test_subject()
    test_variations()