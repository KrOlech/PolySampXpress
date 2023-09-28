from abc import ABCMeta

from src.Python.BaseClass.Logger.Logger import Loger


class CommonNames(Loger):
    __metaclass__ = ABCMeta
    firstPress = False

    top = False
    bottom = False
    left = False
    right = False

    leftTop = False
    rightTop = False
    leftBottom = False
    rightBottom = False

    move = False

    pressPrecision = 50