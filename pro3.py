# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# 1 -> 95 
# 2 -> solar
#import pygame

import userChoice
import sqlite3
import datetime
import os
import identPl

def beepfn(y):
    os.system("echo -n '\a'; sleep 0.2;"*y)
    return()


print("Welcome to our Project's Demonstration" )
plate=identPl.identifyPlate("videoplayback")
if plate==0 :
    print("There is no car right now")
else :
    print("The licence plate is (?):",[plate])
    print("\n")
    print("Connecting to DataBase for knowing which  gas the car need")
    conn=sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute("SELECT GAS FROM CARS WHERE PLATE=(?)",[plate])
    conn.commit();
    #c.execute("CREATE T")
    #conn.commit()
    #c.execute("CREATE TABLE CARS(ID INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL,PLATE TEXT UNIQUE NOT NULL, GAS TEXT NOT NULL);")
    #c.execute("UPDATE INTO CARS where PLATE='6084879' 'SOLAR'" )
    #conn.commit();
    kindOfGas=c.fetchone()[0]
    print("The kind of Gas the driver need is :",kindOfGas )
    print("Now we have to make sure that the driver will no pick the wrong gas...")
    answer=userChoice.userChoice("videoplayback", kindOfGas)


    if answer==0 :
        #beepfn(20)
        # s=Sound()
        #s.read('Alarm Clock Beep.mp3')
        #s.play()
        print("Watch out!! You have the wrong gas in your hand!!")
        #   rnStart = str(datetime.datetime.now().time())
        #  rnStop=rnStart+
        # stop = False
        #while stop == False:
        #   rn = str(datetime.datetime.now().time())
        #  print(rn)
        # if rn == "18:00:00.000000":
            #    stop = True
            #   os.system("start BTS_House_Of_Cards.mp3")


