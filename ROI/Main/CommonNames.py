from abc import ABCMeta


class CommonNames:
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