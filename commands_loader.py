import os
import importlib


def load_modules():
    files = os.listdir('bot/commands')
    modules = filter(lambda x: x.endswith('.py'), files)
    for mdl in modules:
        importlib.import_module('commands.' + mdl[0:-3])
