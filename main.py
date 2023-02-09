import threading
import time
from queue import Queue
import random

kuyruk0 = Queue()
kuyruk1 = Queue()
kuyruk2 = Queue()
kuyruk3 = Queue()
kuyruk4 = Queue()
dizi0 = kuyruk0.queue
dizi1 = kuyruk1.queue
dizi2 = kuyruk2.queue
dizi3 = kuyruk3.queue
dizi4 = kuyruk4.queue
queue0 = 0
queue1 = 0
queue2 = 0
queue3 = 0
queue4 = 0
queue = [queue0,queue1,queue2,queue3,queue4]
all1 = 0
all2 = 0
all3 = 0
all4 = 0
kuyruk = [kuyruk0,kuyruk1,kuyruk2,kuyruk3,kuyruk4]
dizi = [dizi0,dizi1,dizi2,dizi3,dizi4]
totalactivate = 1
toplam = 0
exit_count = 0
activate1 = True
activate2 = False
activate3 = False
activate4 = False
activate5 = False
capacity = 10
inside1 = []
inside2 = []
inside3 = []
inside4 = []
inside5 = []
count_inside1 = 0
count_inside2 = 0
count_inside3 = 0
count_inside4 = 0
count_inside5 = 0
floor1 = 0
floor2 = 0
floor3 = 0
floor4 = 0
floor5 = 0
destination1 = 0
destination2 = 0
destination3 = 0
destination4 = 0
destination5 = 0
mode1 = "Working"
mode2 = "idle"
mode3 = "idle"
mode4 = "idle"
mode5 = "idle"
direction1 = "up"
direction2 = "up"
direction3 = "up"
direction4 = "up"
direction5 = "up"

def giristhread():
    global toplam
    global kuyruk0
    global queue0
    while(1):
        time.sleep(0.5)
        kisi = random.randint(1, 10)
        kat = random.randint(1, 4)
        queue[0] += kisi

        demet = (kisi,kat)
        kuyruk0.put(demet)
        toplam += kisi


def cikisthread():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global queue1
    global queue2
    global queue3
    global queue4
    while(1):
        time.sleep(1)
        kisi1 = random.randint(1, 5)
        kat1 = random.randint(1, 4)
        if kat1 == 1 and kisi1 > all1:
            continue
        if kat1 == 2 and kisi1 > all2:
            continue
        if kat1 == 3 and kisi1 > all3:
            continue
        if kat1 == 4 and kisi1 > all4:
            continue
        demet = (kisi1, 0)
        toplam += kisi1
        for i in range (1,5):
            if kat1 == i:
                kuyruk[i].put(demet)
                if i == 1:
                    all1-= kisi1
                    queue[1] += kisi1
                if i == 2:
                    all2-= kisi1
                    queue[2] += kisi1
                if i == 3:
                    all3-= kisi1
                    queue[3] += kisi1
                if i == 4:
                    all4-= kisi1
                    queue[4] += kisi1


def kontrolthread():
    global totalactivate
    global activate1
    global activate2
    global activate3
    global activate4
    global activate5
    global mode1
    global mode2
    global mode3
    global mode4
    global mode5
    global inside2
    global inside3
    global inside4
    global inside5

    t2 = threading.Thread(target=asansor2, args=())
    t3 = threading.Thread(target=asansor3, args=())
    t4 = threading.Thread(target=asansor4, args=())
    t5 = threading.Thread(target=asansor5, args=())
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    while(1):

        if toplam > totalactivate * 20 and totalactivate < 5:
            totalactivate += 1
            if totalactivate == 2 and activate2 == False:
                activate2 = True
                mode2 = "Working"
                event2.set()

            elif totalactivate == 3 and activate3 == False:
                activate3 = True
                mode3 = "Working"
                event3.set()

            elif totalactivate == 4 and activate4 == False:
                activate4 = True
                mode4 = "Working"
                event4.set()

            elif totalactivate == 5 and activate5 == False:
                activate5 = True
                mode5 = "Working"
                event5.set()

        elif toplam < totalactivate * 10 and totalactivate > 1:

            if totalactivate == 2 and activate2 == True and len(inside2) == 0:
                activate2 = False
                mode2 = "idle"
                event2.clear()

            elif totalactivate == 3 and activate3 == True:
                activate3 = False
                mode3 = "idle"
                event3.clear()

            elif totalactivate == 4 and activate4 == True:
                activate4 = False
                mode4 = "idle"
                event4.clear()

            elif totalactivate == 5 and activate5 == True:
                activate5 = False
                mode5 = "idle"
                event5.clear()

            totalactivate -= 1

def asansor1():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global activate1
    global mode1
    global floor1
    global destination1
    global direction1
    global capacity
    global count_inside1
    global inside1
    global exit_count
    global queue

    while(1):

        if kuyruk[floor1].empty() == False:

            while(kuyruk[floor1].qsize() > 0):
                demet = dizi[floor1][0]
                if demet[0] + count_inside1 <= capacity:
                    count_inside1 += demet[0]
                    inside1.append(demet)
                    kuyruk[floor1].get()
                    queue[floor1] -= demet[0]
                    toplam -= demet[0]
                else:
                    break
            if len(inside1) > 0:
                yedekdemet = inside1[0]
                destination1 = yedekdemet[1]
                for i in range(0, len(inside1)):
                    yedekdemet = inside1[i]
                    if destination1 > yedekdemet[1] and yedekdemet[1] != 0:
                        destination1 = yedekdemet[1]
            elif len(inside1) == 0:
                destination1 = 0


        else:
            if len(inside1) > 0:
                yedekdemet = inside1[0]
                destination1 = yedekdemet[1]
                for i in range (0,len(inside1)):
                    yedekdemet = inside1[i]
                    if destination1 > yedekdemet[1] and yedekdemet[1] != 0:
                        destination1 = yedekdemet[1]
            elif len(inside1) == 0 and floor1 == destination1:
                destination1 = 0


        while (floor1 != destination1):

            time.sleep(0.2)
            if floor1 > destination1:
                floor1 -= 1
                direction1 = "down"
            elif floor1 < destination1:
                floor1 += 1
                direction1 = "up"
            if kuyruk[floor1].empty() == False:
                while (kuyruk[floor1].qsize() > 0):
                    demet = dizi[floor1][0]
                    if demet[0] + count_inside1 <= capacity:
                        count_inside1 += demet[0]
                        inside1.append(demet)
                        kuyruk[floor1].get()
                        queue[floor1] -= demet[0]
                        toplam -= demet[0]
                    else:
                        break

        k = 0
        while ( k < len(inside1) ):

            yedekdemet = inside1[k]

            if yedekdemet[1] == destination1:
                if yedekdemet[1] == 0:
                    exit_count += yedekdemet[0]
                inside1.pop(k)
                k -=1
                count_inside1 -= yedekdemet[0]
                if destination1 == 1:
                    all1 += yedekdemet[0]
                elif destination1 == 2:
                    all2 += yedekdemet[0]
                elif destination1 == 3:
                    all3 += yedekdemet[0]
                elif destination1 == 4:
                    all4 += yedekdemet[0]
            k += 1

        for i in range (1,5):
            if kuyruk[i].empty() == False:
                destination1 = i

def asansor2():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global activate2
    global mode2
    global floor2
    global destination2
    global direction2
    global capacity
    global count_inside2
    global inside2
    global exit_count
    global queue
    event2.wait()
    while (1):

        if event2.is_set():

            if kuyruk[floor2].empty() == False:

                while (kuyruk[floor2].qsize() > 0):
                    demet = dizi[floor2][0]
                    if demet[0] + count_inside2 <= capacity:
                        count_inside2 += demet[0]
                        inside2.append(demet)
                        kuyruk[floor2].get()
                        queue[floor2] -= demet[0]
                        toplam -= demet[0]
                    else:
                        break
                if len(inside2) > 0:
                    yedekdemet = inside2[0]
                    destination2 = yedekdemet[1]
                    for i in range(0, len(inside2)):
                        yedekdemet = inside2[i]
                        if destination2 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination2 = yedekdemet[1]
                elif len(inside2) == 0:
                    destination2 = 0


            else:
                if len(inside2) > 0:
                    yedekdemet = inside2[0]
                    destination2 = yedekdemet[1]
                    for i in range(0, len(inside2)):
                        yedekdemet = inside2[i]
                        if destination2 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination2 = yedekdemet[1]
                elif len(inside2) == 0 and floor2 == destination2:
                    destination2 = 0

            while (floor2 != destination2):

                time.sleep(0.2)
                if floor2 > destination2:
                    floor2 -= 1
                    direction2 = "down"
                elif floor2 < destination2:
                    floor2 += 1
                    direction2 = "up"
                if kuyruk[floor2].empty() == False:
                    while (kuyruk[floor2].qsize() > 0):
                        demet = dizi[floor2][0]
                        if demet[0] + count_inside2 <= capacity:
                            count_inside2 += demet[0]
                            inside2.append(demet)
                            kuyruk[floor2].get()
                            queue[floor2] -= demet[0]
                            toplam -= demet[0]
                        else:
                            break

            k = 0
            while (k < len(inside2)):

                yedekdemet = inside2[k]

                if yedekdemet[1] == destination2:
                    if yedekdemet[1] == 0:
                        exit_count += yedekdemet[0]
                    inside2.pop(k)
                    k -= 1
                    count_inside2 -= yedekdemet[0]
                    if destination2 == 1:
                        all1 += yedekdemet[0]
                    elif destination2 == 2:
                        all2 += yedekdemet[0]
                    elif destination2 == 3:
                        all3 += yedekdemet[0]
                    elif destination2 == 4:
                        all4 += yedekdemet[0]
                k += 1

            for i in range(1, 5):
                if kuyruk[i].empty() == False:
                    destination2 = i

def asansor3():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global activate3
    global mode3
    global floor3
    global destination3
    global direction3
    global capacity
    global count_inside3
    global inside3
    global exit_count
    global queue
    event3.wait()

    while (1):

        if event2.is_set():

            if kuyruk[floor3].empty() == False:

                while (kuyruk[floor3].qsize() > 0):
                    demet = dizi[floor3][0]
                    if demet[0] + count_inside3 <= capacity:
                        count_inside3 += demet[0]
                        inside3.append(demet)
                        kuyruk[floor3].get()
                        queue[floor3] -= demet[0]
                        toplam -= demet[0]
                    else:
                        break
                if len(inside3) > 0:
                    yedekdemet = inside3[0]
                    destination3 = yedekdemet[1]
                    for i in range(0, len(inside3)):
                        yedekdemet = inside3[i]
                        if destination3 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination3 = yedekdemet[1]
                elif len(inside3) == 0:
                    destination3 = 0


            else:
                if len(inside3) > 0:
                    yedekdemet = inside3[0]
                    destination3 = yedekdemet[1]
                    for i in range(0, len(inside3)):
                        yedekdemet = inside3[i]
                        if destination3 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination3 = yedekdemet[1]
                elif len(inside3) == 0 and floor3 == destination3:
                    destination3 = 0

            while (floor3 != destination3):

                time.sleep(0.2)
                if floor3 > destination3:
                    floor3 -= 1
                    direction3 = "down"
                elif floor3 < destination3:
                    floor3 += 1
                    direction3 = "up"
                if kuyruk[floor3].empty() == False:
                    while (kuyruk[floor3].qsize() > 0):
                        demet = dizi[floor3][0]
                        if demet[0] + count_inside3 <= capacity:
                            count_inside3 += demet[0]
                            inside3.append(demet)
                            kuyruk[floor3].get()
                            queue[floor3] -= demet[0]
                            toplam -= demet[0]
                        else:
                            break

            k = 0
            while (k < len(inside3)):

                yedekdemet = inside3[k]

                if yedekdemet[1] == destination3:
                    if yedekdemet[1] == 0:
                        exit_count += yedekdemet[0]
                    inside3.pop(k)
                    k -= 1
                    count_inside3 -= yedekdemet[0]
                    if destination3 == 1:
                        all1 += yedekdemet[0]
                    elif destination3 == 2:
                        all2 += yedekdemet[0]
                    elif destination3 == 3:
                        all3 += yedekdemet[0]
                    elif destination3 == 4:
                        all4 += yedekdemet[0]
                k += 1

            for i in range(1, 5):
                if kuyruk[i].empty() == False:
                    destination3 = i

def asansor4():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global activate4
    global mode4
    global floor4
    global destination4
    global direction4
    global capacity
    global count_inside4
    global inside4
    global exit_count
    global queue
    event4.wait()

    while (1):
        if event4.is_set():
            if kuyruk[floor4].empty() == False:

                while (kuyruk[floor4].qsize() > 0):
                    demet = dizi[floor4][0]
                    if demet[0] + count_inside4 <= capacity:
                        count_inside4 += demet[0]
                        inside2.append(demet)
                        kuyruk[floor4].get()
                        queue[floor4] -= demet[0]
                        toplam -= demet[0]
                    else:
                        break
                if len(inside2) > 0:
                    yedekdemet = inside2[0]
                    destination4 = yedekdemet[1]
                    for i in range(0, len(inside2)):
                        yedekdemet = inside2[i]
                        if destination4 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination4 = yedekdemet[1]
                elif len(inside2) == 0:
                    destination4 = 0


            else:
                if len(inside2) > 0:
                    yedekdemet = inside2[0]
                    destination4 = yedekdemet[1]
                    for i in range(0, len(inside2)):
                        yedekdemet = inside2[i]
                        if destination4 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination4 = yedekdemet[1]
                elif len(inside2) == 0 and floor4 == destination4:
                    destination4 = 0

            while (floor4 != destination4):

                time.sleep(0.2)
                if floor4 > destination4:
                    floor4 -= 1
                    direction4 = "down"
                elif floor4 < destination4:
                    floor4 += 1
                    direction4 = "up"
                if kuyruk[floor4].empty() == False:
                    while (kuyruk[floor4].qsize() > 0):
                        demet = dizi[floor4][0]
                        if demet[0] + count_inside4 <= capacity:
                            count_inside4 += demet[0]
                            inside2.append(demet)
                            kuyruk[floor4].get()
                            queue[floor4] -= demet[0]
                            toplam -= demet[0]
                        else:
                            break

            k = 0
            while (k < len(inside2)):

                yedekdemet = inside2[k]

                if yedekdemet[1] == destination4:
                    if yedekdemet[1] == 0:
                        exit_count += yedekdemet[0]
                    inside2.pop(k)
                    k -= 1
                    count_inside4 -= yedekdemet[0]
                    if destination4 == 1:
                        all1 += yedekdemet[0]
                    elif destination4 == 2:
                        all2 += yedekdemet[0]
                    elif destination4 == 3:
                        all3 += yedekdemet[0]
                    elif destination4 == 4:
                        all4 += yedekdemet[0]
                k += 1

            for i in range(1, 5):
                if kuyruk[i].empty() == False:
                    destination4 = i

def asansor5():
    global kuyruk
    global toplam
    global all1
    global all2
    global all3
    global all4
    global activate5
    global mode5
    global floor5
    global destination5
    global direction5
    global capacity
    global count_inside5
    global inside5
    global exit_count

    event5.wait()

    while (1):
        global queue
        if event5.is_set():

            if kuyruk[floor5].empty() == False:

                while (kuyruk[floor5].qsize() > 0):
                    demet = dizi[floor5][0]
                    if demet[0] + count_inside5 <= capacity:
                        count_inside5 += demet[0]
                        inside5.append(demet)
                        kuyruk[floor5].get()
                        queue[floor5] -= demet[0]
                        toplam -= demet[0]
                    else:
                        break
                if len(inside5) > 0:
                    yedekdemet = inside5[0]
                    destination5 = yedekdemet[1]
                    for i in range(0, len(inside5)):
                        yedekdemet = inside5[i]
                        if destination5 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination5 = yedekdemet[1]
                elif len(inside5) == 0:
                    destination5 = 0


            else:
                if len(inside5) > 0:
                    yedekdemet = inside5[0]
                    destination5 = yedekdemet[1]
                    for i in range(0, len(inside5)):
                        yedekdemet = inside5[i]
                        if destination5 > yedekdemet[1] and yedekdemet[1] != 0:
                            destination5 = yedekdemet[1]
                elif len(inside5) == 0 and floor5 == destination5:
                    destination5 = 0

            while (floor5 != destination5):

                time.sleep(0.2)
                if floor5 > destination5:
                    floor5 -= 1
                    direction5 = "down"
                elif floor5 < destination5:
                    floor5 += 1
                    direction5 = "up"
                if kuyruk[floor5].empty() == False:
                    while (kuyruk[floor5].qsize() > 0):
                        demet = dizi[floor5][0]
                        if demet[0] + count_inside5 <= capacity:
                            count_inside5 += demet[0]
                            inside5.append(demet)
                            kuyruk[floor5].get()
                            queue[floor5] -= demet[0]
                            toplam -= demet[0]
                        else:
                            break

            k = 0
            while (k < len(inside5)):

                yedekdemet = inside5[k]

                if yedekdemet[1] == destination5:
                    if yedekdemet[1] == 0:
                        exit_count += yedekdemet[0]
                    inside5.pop(k)
                    k -= 1
                    count_inside5 -= yedekdemet[0]
                    if destination5 == 1:
                        all1 += yedekdemet[0]
                    elif destination5 == 2:
                        all2 += yedekdemet[0]
                    elif destination5 == 3:
                        all3 += yedekdemet[0]
                    elif destination5 == 4:
                        all4 += yedekdemet[0]
                k += 1

            for i in range(1, 5):
                if kuyruk[i].empty() == False:
                    destination5 = i

def Yazdir():

    while(1):

        print("*****************************************************************")
        print("0. kat: queue:", queue[0])
        print("1. kat: All:", all1 ," queue:", queue[1])
        print("2. kat: All:", all2 ," queue:", queue[2])
        print("3. kat: All:", all3 ," queue:", queue[3])
        print("4. kat: All:", all4 ," queue:", queue[4])
        print("Exit Count:",exit_count)

        print("Activate:",activate1)
        print("\t\t\tMode:",mode1)
        print("\t\t\tFloor:", floor1)
        print("\t\t\tDestination:", destination1)
        print("\t\t\tDirection:", direction1)
        print("\t\t\tCapacity:", capacity)
        print("\t\t\tCount_inside:", count_inside1)
        print("\t\t\tİnside:", inside1)

        print("Activate:", activate2)
        print("\t\t\tMode:", mode2)
        print("\t\t\tFloor:", floor2)
        print("\t\t\tDestination:", destination2)
        print("\t\t\tDirection:", direction2)
        print("\t\t\tCapacity:", capacity)
        print("\t\t\tCount_inside:", count_inside2)
        print("\t\t\tİnside:", inside2)

        print("Activate:", activate3)
        print("\t\t\tMode:", mode3)
        print("\t\t\tFloor:", floor3)
        print("\t\t\tDestination:", destination3)
        print("\t\t\tDirection:", direction3)
        print("\t\t\tCapacity:", capacity)
        print("\t\t\tCount_inside:", count_inside3)
        print("\t\t\tİnside:", inside3)

        print("Activate:", activate4)
        print("\t\t\tMode:", mode4)
        print("\t\t\tFloor:", floor4)
        print("\t\t\tDestination:", destination4)
        print("\t\t\tDirection:", direction4)
        print("\t\t\tCapacity:", capacity)
        print("\t\t\tCount_inside:", count_inside4)
        print("\t\t\tİnside:", inside4)

        print("Activate:", activate5)
        print("\t\t\tMode:", mode5)
        print("\t\t\tFloor:", floor5)
        print("\t\t\tDestination:", destination5)
        print("\t\t\tDirection:", direction5)
        print("\t\t\tCapacity:", capacity)
        print("\t\t\tCount_inside:", count_inside5)
        print("\t\t\tİnside:", inside5)

        print("0. kat: ", dizi[0])
        print("1. kat: ", dizi[1])
        print("2. kat: ", dizi[2])
        print("3. kat: ", dizi[3])
        print("4. kat: ", dizi[4])

        time.sleep(0.15)

event = threading.Event()
event2 = threading.Event()
event3 = threading.Event()
event4 = threading.Event()
event5 = threading.Event()

giris = threading.Thread( target = giristhread , args=() )
giris.start()
cikis = threading.Thread( target = cikisthread , args=() )
cikis.start()
kontrol = threading.Thread( target = kontrolthread , args=() )
kontrol.start()
birinci = threading.Thread( target = asansor1 , args=() )
birinci.start()
yazdir = threading.Thread( target = Yazdir , args=() )
yazdir.start()




