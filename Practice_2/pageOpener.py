import time
import webbrowser

i = 5
while i > 0:
    webbrowser.open("https://www.ultimate-guitar.com/", new=2)
    time.sleep(5)
    i -= 1

