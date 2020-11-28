import time
import pyautogui as pya

time.sleep(5)

distance = 100
i=1

while distance:
    pya.dragRel(distance, 0, duration=0.1)
    distance = distance - 5
    pya.dragRel(0, distance, duration=0.1)
    pya.dragRel(0, distance, duration=0.1)
    pya.dragRel(-distance, 0, duration=0.1)
    distance = distance - 5
    pya.dragRel(0, -distance, duration=0.1)
    distance = 100 + 200 * ((i%2)*-1)
    i+=1
    if i==10:
        distance = 100
        #pya.drag(20)
    if(i==20):
        break
