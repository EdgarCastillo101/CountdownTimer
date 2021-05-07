// Edgar Barrera / Github: https://github.com/EdgarCastillo101/EdgarCastillo101
        
import time

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Timer is up.')

t = input('Enter the time in seconds: ')

countdown(int(t))
