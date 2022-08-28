

class InvalidSpeed(Exception):
    def __init__(self):
        super().__init__("[WARNING] - Invalid speed")



if __name__ == '__main__':
    try:
        raise InvalidSpeed()
    except InvalidSpeed as e:
        print(e)
