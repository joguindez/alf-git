import time

def greeting():
    return "Hello Python, the time is: " + time.ctime()


def main():
    print(greeting)

if __name__ == '__main__':
    main()