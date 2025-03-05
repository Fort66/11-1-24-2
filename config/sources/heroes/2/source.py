import pygame as pg
from pygame.transform import flip, scale_by
from pygame.image import load

from config.create_Objects import screen

pg.init()

SCALE_VALUE = .225

HERO = {
            'angle':{
                    0: {
                        'sprite': scale_by(load('images/Heroes/2/1.png').convert_alpha(), SCALE_VALUE),
                        'weapons': [[50, 15], [50, 10]]
                        },
                    22: {
                        'sprite': scale_by(load('images/Heroes/2/2.png').convert_alpha(), SCALE_VALUE),
                        'weapons': [[50, 15], [50, -8]]
                        },
                    45: {
                        'sprite': scale_by(load('images/Heroes/2/3.png').convert_alpha(), SCALE_VALUE),
                        'weapons': [[50, 15], [50, -15]]
                        },
                    67: {
                        'sprite': scale_by(load('images/Heroes/2/4.png').convert_alpha(), SCALE_VALUE),
                        'weapons': [[50, 20], [50, -15]]
                        },
                    90: {
                        'sprite': scale_by(load('images/Heroes/2/5.png').convert_alpha(), SCALE_VALUE),
                        'weapons': [[50, 20], [50, -20]]
                        },
                    112: {
                        'sprite': flip(scale_by(load('images/Heroes/2/4.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, 20], [50, -15]]
                        },
                    135: {
                        'sprite': flip(scale_by(load('images/Heroes/2/3.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, 15], [50, -15]]
                        },
                    157: {
                        'sprite': flip(scale_by(load('images/Heroes/2/2.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, 15], [50, -8]]
                        },
                    180: {
                        'sprite': flip(scale_by(load('images/Heroes/2/1.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, -15], [50, -10]]
                        },
                    202: {'sprite': flip(scale_by(load('images/Heroes/2/2.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, -10], [50, 0]]
                        },
                    225: {
                        'sprite': flip(scale_by(load('images/Heroes/2/3.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, -15], [50, 10]]
                        },
                    247: {'sprite': flip(scale_by(load('images/Heroes/2/4.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, -10], [50, 10]]
                        },
                    270: {
                        'sprite': flip(scale_by(load('images/Heroes/2/5.png').convert_alpha(), SCALE_VALUE), False, True),
                        'weapons': [[50, 15], [50, -15]]
                        },
                    292: {
                        'sprite': flip(flip(scale_by(load('images/Heroes/2/4.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                        'weapons': [[50, 20], [50, -15]]
                        },
                    315: {
                        'sprite': flip(flip(scale_by(load('images/Heroes/2/3.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                        'weapons': [[50, 15], [50, -15]]
                        },
                    337: {
                        'sprite': flip(flip(scale_by(load('images/Heroes/2/2.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                        'weapons': [[50, 15], [50, -8]]
                        },
                    359: {
                        'sprite': flip(flip(scale_by(load('images/Heroes/2/1.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                        'weapons': [[50, 15], [50, -5]]
                        },
                },
        'speed': 5,
        'rotation_speed': 10,
        'hp': 5
        }
