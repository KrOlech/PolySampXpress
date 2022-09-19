from screeninfo import get_monitors

if __name__ == '__main__':
    for m in get_monitors():
        print(str(m))