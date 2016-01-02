import random
import os


def get_background():
    img = random.choice(os.listdir('static/img/bg/'))
    return img
