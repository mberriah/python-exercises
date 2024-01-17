day = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

i = 0
d = 0

while(i < 25):
    i = i + 1
    d = i % 7   # values go from 1 to 7 each time
    print(i, ": ", day[d], sep='')