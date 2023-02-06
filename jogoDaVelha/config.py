import os

import toml

PATH = os.path.dirname(__file__)


def read(file_name):
    path = f'{PATH}\\config\\{file_name}.toml'
    return toml.load(path)


colors = read('colors')
window = read('window')
images = read('images')
