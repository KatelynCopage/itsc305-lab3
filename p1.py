from gpiozero import LED
from time import sleep

#defining leds
a = LED(25)
b = LED(12)
c = LED(22)
d = LED(17)
e = LED(27)
f = LED(23)
g = LED(24)
#making output list
output = [a, b, c, d, e, f, g]

digit0 = [0,0,0,0,0,0,1]
digit1 = [1,0,0,1,1,1,1]
digit2 = [0,0,1,0,0,1,0]
digit3 = [0,0,0,0,1,1,0]
digit4 = [1,0,0,1,1,0,0]
digit5 = [0,1,0,0,1,0,0]
digit6 = [0,1,0,0,0,0,0]
digit7 = [0,0,0,1,1,1,1]
digit8 = [0,0,0,0,0,0,0]
digit9 = [0,0,0,0,1,0,0]

#putting digits into a master list
master_list = [digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9]

#looping
for n in range(10):
	for led in range(7):
		output[led].value = master_list[n][led]
	sleep(2)
