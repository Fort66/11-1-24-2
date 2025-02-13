'''
Класс SoundGame используется для управления звуковыми эффектами в игре.
Вот что делают каждый метод:
playBackgroundMusic(backMusic=None): Загружает и воспроизводит файл фоновой музыки с громкостью 0.2, повторяя его бесконечно, если указан путь к файлу.
playGameSound(sound=None): Загружает и воспроизводит звуковой эффект с громкостью 0.4, если указан путь к файлу.
'''


import pygame as pg

pg.init()

class SoundGame:
    def playBackgroundMusic(self, 
                            backMusic = None, 
                            volume = .2):
        if backMusic:
            self.backMusic = pg.mixer.music.load(backMusic)
            pg.mixer.music.set_volume(volume)
            pg.mixer.music.play(-1)
            
    def playGameSound(self, 
                      sound = None, 
                      volume = .4):
        if sound:
            self.sound = pg.mixer.Sound(sound)
            pg.mixer.Sound.set_volume(self.sound, volume)
            pg.mixer.Sound.play(self.sound)