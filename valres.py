import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (O00OOOOOOOOOO00OO ,OO00OO0000000O000 ):#line:11
        print ("\nPasswords may not be changed using this notebook at present.")#line:15
ps =[]#line:19
wd =''#line:20
rid =0 #line:21
encoff1 =34 #line:22
encoff2 =567 #line:23
def a1 ():#line:41
    global ps #line:43
    O0O0OOOO000O0O0OO =".a1_counter.npy"#line:46
    O0O0O000O0000OO0O =np .zeros (1 ,dtype ='int8,bool')#line:47
    OOO00OOO0000OOOO0 =0 #line:49
    OO0O000000O00OO0O =ps [0 ]#line:50
    O0000OOOOO0O000O0 =ps [1 ]#line:51
    if (waiter ()):#line:53
        while True :#line:54
            try :#line:55
                printmd ('**CA** (2%)')#line:56
                print (OO0O000000O00OO0O ,"+",O0000OOOOO0O000O0 )#line:57
                print ('tester')#line:58
                O000O0OO0O0OOOOOO =float (input ("Please enter your answer here: "))#line:59
                OO00000OO0OOOOO00 =OO0O000000O00OO0O +O0000OOOOO0O000O0 #line:60
                OOO0O0OO00000000O =np .isclose (O000O0OO0O0OOOOOO ,OO00000OO0OOOOO00 ,OOO00OOO0000OOOO0 )#line:61
                if OOO0O0OO00000000O :#line:62
                    print ("Well done, right answer is ",OO00000OO0OOOOO00 )#line:63
                else :#line:64
                    print ("Not right yet. Take another look then run this cell again.")#line:65
                O0O0O000O0000OO0O =trycount (O0O0OOOO000O0O0OO ,OOO0O0OO00000000O )#line:67
                OO00OO0OO0OOOO00O =100 -(O0O0O000O0000OO0O [0 ]-1 )*10 #line:68
                if O0O0O000O0000OO0O [1 ]:#line:69
                    print ("First success after ",O0O0O000O0000OO0O [0 ]," tries, you have ",OO00OO0OO0OOOO00O ,"% on this exercise.")#line:70
                    print ("Enter this code into Brightspace:\n\n",genenc (1 +encoff1 ,OO00OO0OO0OOOO00O +encoff2 ),'\n')#line:71
                else :#line:72
                    print ("You have had ",O0O0O000O0000OO0O [0 ]," tries.")#line:73
                    print ("If next try is accepted you will achieve ",OO00OO0OO0OOOO00O -10 ,"% on this exercise.")#line:74
                break #line:76
            except ValueError :#line:78
                print ("I didn't understand that.")#line:79
                continue #line:80
        return #line:82
def a2_notlive (O0O00OO000OO000OO ):#line:91
    global ps #line:93
    O00O0O0OOOOO0O000 =".a2_counter.npy"#line:96
    OOO0OO0OOO00OOO0O =np .zeros (1 ,dtype ='int8,bool')#line:97
    O0OO00OOOOO00OO0O =6 #line:100
    O000O00000OOO0O0O =7 #line:101
    O0OO0OOOO0OOOOO0O =0 #line:103
    O0O0O000O00OOO0OO =(ps [O0OO00OOOOO00OO0O ])%6 +1 #line:105
    OOOO0000O00OOO0O0 =(ps [O000O00000OOO0O0O ])%6 +1 #line:106
    while O0O0O000O00OOO0OO +OOOO0000O00OOO0O0 ==7 or O0O0O000O00OOO0OO ==OOOO0000O00OOO0O0 :#line:107
        OOOO0000O00OOO0O0 +=1 #line:108
        OOOO0000O00OOO0O0 =OOOO0000O00OOO0O0 %6 +1 #line:109
    if (O0O00OO000OO000OO ):#line:111
        printmd ('**CA** (2%)')#line:112
        print ("Run your program (when you are happy it is working correctly) for a=",O0O0O000O00OOO0OO ," and b=",OOOO0000O00OOO0O0 )#line:113
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:114
        return #line:115
    if (waiter ()):#line:117
        while True :#line:118
            try :#line:119
                print ("Enter your program's result for a=",O0O0O000O00OOO0OO ," and b=",OOOO0000O00OOO0O0 )#line:120
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:121
                OO00OOO00O0O0O000 =float (input ("Please enter your answer here: "))#line:122
                O0O000000000OO0O0 =(3 *(O0O0O000O00OOO0OO **3 *OOOO0000O00OOO0O0 -O0O0O000O00OOO0OO *OOOO0000O00OOO0O0 **3 ))%7 #line:123
                O0OOOO0OO000O0OOO =np .isclose (OO00OOO00O0O0O000 ,O0O000000000OO0O0 ,O0OO0OOOO0OOOOO0O )#line:124
                if O0OOOO0OO000O0OOO :#line:125
                    print ("Well done, right answer is ",O0O000000000OO0O0 )#line:126
                else :#line:127
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:128
                OOO0OO0OOO00OOO0O =trycount (O00O0O0OOOOO0O000 ,O0OOOO0OO000O0OOO )#line:130
                OOO00OO00OOOOOOOO =100 -(OOO0OO0OOO00OOO0O [0 ]-1 )*10 #line:131
                if OOO0OO0OOO00OOO0O [1 ]:#line:132
                    print ("First success after ",OOO0OO0OOO00OOO0O [0 ]," tries, you have ",OOO00OO00OOOOOOOO ,"% on this exercise.")#line:133
                else :#line:134
                    print ("You have had ",OOO0OO0OOO00OOO0O [0 ]," tries.")#line:135
                    print ("If next try is accepted you will achieve ",OOO00OO00OOOOOOOO -10 ,"% on this exercise.")#line:136
                break #line:138
            except ValueError :#line:140
                print ("I didn't understand that.")#line:141
                continue #line:142
        return #line:144
def a3_notlive (OOOOO0000OO0OOOOO ):#line:153
    global ps #line:155
    O0O0OO00OOOO0OO0O =".a3_counter.npy"#line:158
    O000000000O00000O =np .zeros (1 ,dtype ='int8,bool')#line:159
    OOOOOO00OO00O00OO =23 #line:162
    O00OO00O0O0000OOO =24 #line:163
    OOOO0O00O0OOOO0OO =(ps [OOOOOO00OO00O00OO ])%6 +1 #line:164
    OOOOO00000000OO0O =(ps [O00OO00O0O0000OOO ])%6 +1 #line:165
    O00000O00O0000000 =0 #line:167
    OOOO0O00O0OOOO0OO =10 *OOOO0O00O0OOOO0OO +OOOOO00000000OO0O ;#line:169
    if (OOOOO0000OO0OOOOO ):#line:171
        printmd ('**CA** (6%)')#line:172
        print ("Run your program for ",OOOO0O00O0OOOO0OO ,"people")#line:173
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:174
        return #line:175
    if (waiter ()):#line:177
        while True :#line:178
            try :#line:179
                print ("Enter your program's result for",OOOO0O00O0OOOO0OO ,"people")#line:180
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:181
                O000OO00O0000OOOO =float (input ("Please enter your answer here: "))#line:182
                O00O0OOOOOOO0OO00 =OOOO0O00O0OOOO0OO +2 *OOOO0O00O0OOOO0OO +2 *OOOO0O00O0OOOO0OO +10 *OOOO0O00O0OOOO0OO #line:183
                OO0OOO00O0OO0000O =np .isclose (O000OO00O0000OOOO ,O00O0OOOOOOO0OO00 ,O00000O00O0000000 )#line:184
                if OO0OOO00O0OO0000O :#line:185
                    print ("Well done, right answer is ",O00O0OOOOOOO0OO00 )#line:186
                else :#line:187
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:188
                O000000000O00000O =trycount (O0O0OO00OOOO0OO0O ,OO0OOO00O0OO0000O )#line:190
                O0OO00OOO0000OO00 =100 -(O000000000O00000O [0 ]-1 )*10 #line:191
                if O000000000O00000O [1 ]:#line:192
                    print ("First success after ",O000000000O00000O [0 ]," tries, you have ",O0OO00OOO0000OO00 ,"% on this exercise.")#line:193
                else :#line:194
                    print ("You have had ",O000000000O00000O [0 ]," tries.")#line:195
                    print ("If next try is accepted you will achieve ",O0OO00OOO0000OO00 -10 ,"% on this exercise.")#line:196
                break #line:198
            except ValueError :#line:200
                print ("I didn't understand that.")#line:201
                continue #line:202
        return #line:204
def a4_notlive (O0OO0OO0O0000OOO0 ):#line:215
        import random #line:217
        import requests #line:218
        global ps #line:220
        global wd #line:221
        OO0OO00O0OO00OO00 =".a4_counter.npy"#line:224
        OOO0OO0OOOOO0OOO0 =np .zeros (1 ,dtype ='int8,bool')#line:225
        O00OO0OO00OOO0O0O =60 #line:228
        O00O0O000O0O0OO0O =61 #line:229
        OO0000O0O00OO0OO0 =62 #line:230
        OOO000O000O0OOOO0 =63 #line:231
        O0OO0O000OO0O000O =64 #line:232
        OOO0OO00OOO0O0OO0 =0 #line:235
        if (O0OO0OO0O0000OOO0 ):#line:237
                OO0OO00O0OO00O0OO ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:239
                OOO0O0000OOO0OOOO =requests .get (OO0OO00O0OO00O0OO )#line:241
                OOO00OOOOOOOO0O0O =OOO0O0000OOO0OOOO .content .splitlines ()#line:242
                random .seed (10 *ps [62 ]+ps [63 ])#line:243
                O000O00000OOO0OOO =4 +(10 *ps [64 ]+ps [65 ])%4 #line:244
                OOOO000O0O000OO00 =True #line:245
                while OOOO000O0O000OO00 :#line:246
                        O0O0OOOO0O0OOOOOO =OOO00OOOOOOOO0O0O [random .randint (0 ,len (OOO00OOOOOOOO0O0O )-1 )].decode ("utf-8")#line:247
                        if len (O0O0OOOO0O0OOOOOO )>7 and len (O0O0OOOO0O0OOOOOO )<14 and O0O0OOOO0O0OOOOOO [0 ].islower ():#line:249
                                OOOO000O0O000OO00 =False #line:250
                                for OO0O0O0OO00O00OOO in O0O0OOOO0O0OOOOOO :#line:251
                                        if chr (ord (OO0O0O0OO00O00OOO )+O000O00000OOO0OOO )>'z':#line:252
                                                OOOO000O0O000OO00 =True #line:253
                OOOO0OOOO00OOOO0O =len (O0O0OOOO0O0OOOOOO )#line:255
                OO0000O0O0OO0O0OO =''#line:256
                for OO00O0OO00OO00O0O in range (0 ,OOOO0OOOO00OOOO0O ):#line:257
                        OO0000O0O0OO0O0OO +=chr (ord (O0O0OOOO0O0OOOOOO [OO00O0OO00OO00O0O ])+O000O00000OOO0OOO )#line:259
                print ('Your encoded word is',OO0000O0O0OO0O0OO )#line:261
                print ('Write your program in the cell below this one.\n')#line:262
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:264
                wd =O0O0OOOO0O0OOOOOO #line:265
                return #line:266
        if (waiter ()):#line:268
                while True :#line:269
                        try :#line:270
                                printmd ('**CA** (6%)')#line:271
                                OO00O0O0OOO00O00O =str (input ("Enter your DECODED word here: "))#line:272
                                OOOOOO0O0OO0OO000 =wd #line:273
                                O0OO0O0O0O00O0O00 =OO00O0O0OOO00O00O ==OOOOOO0O0OO0OO000 #line:274
                                if O0OO0O0O0O00O0O00 :#line:275
                                        print ("Well done, right answer is ",OOOOOO0O0OO0OO000 )#line:276
                                else :#line:277
                                        print ("Not right yet. Take another look then run this cell again.")#line:278
                                OOO0OO0OOOOO0OOO0 =trycount (OO0OO00O0OO00OO00 ,O0OO0O0O0O00O0O00 )#line:280
                                O000OO000OO0O000O =100 -(OOO0OO0OOOOO0OOO0 [0 ]-1 )*10 #line:281
                                if OOO0OO0OOOOO0OOO0 [1 ]:#line:282
                                        print ("First success after ",OOO0OO0OOOOO0OOO0 [0 ]," tries, you have ",O000OO000OO0O000O ,"% on this exercise.")#line:283
                                else :#line:284
                                        print ("You have had ",OOO0OO0OOOOO0OOO0 [0 ]," tries.")#line:285
                                        print ("If next try is accepted you will achieve ",O000OO000OO0O000O -10 ,"% on this exercise.")#line:286
                                break #line:287
                        except ValueError :#line:289
                                print ("I didn't understand that.")#line:290
                                continue #line:291
                return #line:293
def a5_notlive (O0000OOO0OOO00OO0 ):#line:303
        import random #line:305
        import requests #line:306
        global ps #line:308
        global P0 #line:309
        OO00OO00O0OOOOOOO =".a5_counter.npy"#line:313
        O0OO0OO00OOOOO000 =np .zeros (1 ,dtype ='int8,bool')#line:314
        OO0OOO00000O0000O =70 #line:317
        OOO000000O000O00O =71 #line:318
        O000O0OOOOO00OOOO =72 #line:319
        OO0O0O000O0OO000O =73 #line:320
        OOOOOOO0OOOO00OO0 =74 #line:321
        OO00000OOOOOOOO0O =0 #line:324
        if (O0000OOO0OOO00OO0 ):#line:326
                P0 =[]#line:327
                O0OOO0OOOO0OOOO00 =7 +(10 *ps [OO0OOO00000O0000O ]+ps [OOO000000O000O00O ])%4 #line:328
                for O0OOO0OO00O000OO0 in range (O0OOO0OOOO0OOOO00 ):#line:329
                        P0 .append (max (0 ,ps [O000O0OOOOO00OOOO +O0OOO0OO00O000OO0 ]-1 ))#line:330
                print ('Run your program for the list below:\n',P0 )#line:331
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:333
        elif (waiter ()):#line:335
                while True :#line:336
                        try :#line:337
                                printmd ('**CA** (6%)')#line:340
                                O0O00000O0O00OO0O =eval (input ("Enter your list here: "))#line:341
                                OOO0OOO0000000O0O =3 #line:346
                                OOO0OOOO00OO00O0O =P0 .copy ()#line:347
                                OOO0OOOO00OO00O0O .append (0 )#line:348
                                print (OOO0OOOO00OO00O0O )#line:349
                                O0OOO0OOOO0OOOO00 =len (P0 )#line:350
                                for OO00OOOO0O0O0OO00 in range (OOO0OOO0000000O0O ):#line:351
                                        for O0OOO0OO00O000OO0 in range (O0OOO0OOOO0OOOO00 ):#line:352
                                                OOO0OOOO00OO00O0O [O0OOO0OO00O000OO0 ]=OOO0OOOO00OO00O0O [O0OOO0OO00O000OO0 +1 ]*(O0OOO0OO00O000OO0 +1 )#line:354
                                OOO0OOOO00OO00O0O .pop ()#line:355
                                OOO00000O0OO00O00 =OOO0OOOO00OO00O0O #line:358
                                if not type (O0O00000O0O00OO0O )==type (OOO00000O0OO00O00 ):#line:360
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:361
                                elif not len (O0O00000O0O00OO0O )==len (OOO00000O0OO00O00 ):#line:362
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:363
                                else :#line:364
                                        O0O000OO000O0O00O =O0O00000O0O00OO0O ==OOO00000O0OO00O00 #line:365
                                        if O0O000OO000O0O00O :#line:366
                                                print ("Well done, right answer is ",OOO00000O0OO00O00 )#line:367
                                        else :#line:368
                                                print ("Not right yet. Take another look then run this cell again.")#line:369
                                        O0OO0OO00OOOOO000 =trycount (OO00OO00O0OOOOOOO ,O0O000OO000O0O00O )#line:371
                                        O00O0O00OO0OOOO00 =100 -(O0OO0OO00OOOOO000 [0 ]-1 )*10 #line:372
                                        if O0OO0OO00OOOOO000 [1 ]:#line:373
                                                print ("First success after ",O0OO0OO00OOOOO000 [0 ]," tries, you have ",O00O0O00OO0OOOO00 ,"% on this exercise.")#line:374
                                        else :#line:375
                                                print ("You have had ",O0OO0OO00OOOOO000 [0 ]," tries.")#line:376
                                                print ("If next try is accepted you will achieve ",O00O0O00OO0OOOO00 -10 ,"% on this exercise.")#line:377
                                        break #line:378
                                OOO0OOOO00OO00O0O =None #line:381
                                OOO00000O0OO00O00 =None #line:382
                        except ValueError :#line:383
                                print ("I didn't understand that.")#line:384
                                continue #line:385
        return #line:387
def a6_notlive (OO0000OOO000000OO ):#line:396
        import random #line:398
        import requests #line:399
        global ps #line:401
        global P0 #line:402
        O0O0O0000OO00000O =".a6_counter.npy"#line:406
        OO0OO0OOO00OOO00O =np .zeros (1 ,dtype ='int8,bool')#line:407
        O0O00O00O0OO00OOO =11 #line:410
        OOO000OOO00OO00OO =16 #line:411
        O00OO0OO00O0O0OO0 =7 #line:412
        OOOO0O00O0O0OOOOO =33 #line:413
        O0O0O00O0O0OOO000 =21 #line:414
        OOOO0O0OOO000OOO0 =0 #line:417
        if (OO0000OOO000000OO ):#line:419
                OOOOOOOO0OOO0O000 =ps [O0O00O00O0OO00OOO ]+ps [OOO000OOO00OO00OO ]+ps [O00OO0OO00O0O0OO0 ]+ps [OOOO0O00O0O0OOOOO ]+ps [O0O0O00O0O0OOO000 ]#line:420
                random .seed (OOOOOOOO0OOO0O000 )#line:421
                P0 =random .randint (1000 ,2000 )#line:422
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:423
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:425
        elif (waiter ()):#line:427
                while True :#line:428
                        try :#line:429
                                printmd ('**CA** (6%)')#line:432
                                O0OO0O000OO0OOO0O =eval (input ("Enter your stopping number here: "))#line:433
                                OO0O00000O0O00O00 =P0 #line:437
                                OO00000O000OO0OO0 =[OO0O00000O0O00O00 ]#line:438
                                while not OO0O00000O0O00O00 ==1 :#line:439
                                        if OO0O00000O0O00O00 %2 :#line:440
                                                OO0O00000O0O00O00 =3 *OO0O00000O0O00O00 +1 #line:441
                                        else :#line:442
                                                OO0O00000O0O00O00 =OO0O00000O0O00O00 //2 #line:443
                                        OO00000O000OO0OO0 .append (OO0O00000O0O00O00 )#line:444
                                OO0O00OO000OO0OO0 =len (OO00000O000OO0OO0 )#line:445
                                O000O0OOOOO0O000O =OO0O00OO000OO0OO0 #line:449
                                if not type (O0OO0O000OO0OOO0O )==type (O000O0OOOOO0O000O ):#line:451
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:452
                                else :#line:455
                                        O0O0OOO0O0O0O00O0 =O0OO0O000OO0OOO0O ==O000O0OOOOO0O000O #line:456
                                        if O0O0OOO0O0O0O00O0 :#line:457
                                                print ("Well done, right answer is ",O000O0OOOOO0O000O )#line:458
                                        else :#line:459
                                                print ("Not right yet. Take another look then run this cell again.")#line:460
                                        OO0OO0OOO00OOO00O =trycount (O0O0O0000OO00000O ,O0O0OOO0O0O0O00O0 )#line:462
                                        O0OOO0O00O0OOOOOO =100 -(OO0OO0OOO00OOO00O [0 ]-1 )*10 #line:463
                                        if OO0OO0OOO00OOO00O [1 ]:#line:464
                                                print ("First success after ",OO0OO0OOO00OOO00O [0 ]," tries, you have ",O0OOO0O00O0OOOOOO ,"% on this exercise.")#line:465
                                        else :#line:466
                                                print ("You have had ",OO0OO0OOO00OOO00O [0 ]," tries.")#line:467
                                                print ("If next try is accepted you will achieve ",O0OOO0O00O0OOOOOO -10 ,"% on this exercise.")#line:468
                                        break #line:469
                                OO0O00OO000OO0OO0 =None #line:472
                                O000O0OOOOO0O000O =None #line:473
                        except ValueError :#line:474
                                print ("I didn't understand that.")#line:475
                                continue #line:476
        return #line:478
def a7_notlive (OO0OO0OO000O0O000 ):#line:488
        O0OOO0000000O00OO =".a7_counter.npy"#line:492
        OOOOO00O00O0OOO0O =np .zeros (1 ,dtype ='int8,bool')#line:493
        def OO00OOOOO0O00OO0O ():#line:495
                pass #line:496
        O0O00OO00O00O00OO =[(30 ,10 )]#line:499
        O0O000O000OOO0OOO =1.0e-4 #line:502
        if (waiter ()):#line:505
                printmd ('**CA** (6%)')#line:507
                if not type (OO0OO0OO000O0O000 )==type (OO00OOOOO0O00OO0O ):#line:509
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:510
                else :#line:513
                        def O000OO0000OOO0O00 (OO0O000OO0O0O000O ,O0OO0OO0O00O0O00O ):#line:516
                                import math #line:517
                                O0O00OOOO0O0O0OO0 =9.81 #line:518
                                O000OO0000000OOOO =math .pi *O0OO0OO0O00O0O00O /180. #line:519
                                O000O0OOOO000O00O =OO0O000OO0O0O000O **2 *math .sin (2 *O000OO0000000OOOO )/O0O00OOOO0O0O0OO0 #line:520
                                O00O0OO0OO000OO00 =OO0O000OO0O0O000O **2 *(math .sin (O000OO0000000OOOO ))**2 /(2. *O0O00OOOO0O0O0OO0 )#line:521
                                return O000O0OOOO000O00O ,O00O0OO0OO000OO00 #line:522
                        import random as r #line:525
                        O0O00OO00O00O00OO =[]#line:526
                        O00000OO0OO0O0OO0 =False #line:527
                        O0O00OOOOO00OOO0O =[]#line:528
                        OO0O0OO0O0O0OOOOO =10 #line:529
                        O0OO0OOO0O000O000 =100 #line:530
                        OO00O0000OOOOO00O =5 #line:531
                        OO0OOOO00O0000O00 =85 #line:532
                        for OO000OOOO00O0OO00 in range (5 ):#line:533
                                O0O00OO00O00O00OO .append ((r .uniform (OO0O0OO0O0O0OOOOO ,O0OO0OOO0O000O000 ),r .uniform (OO00O0000OOOOO00O ,OO0OOOO00O0000O00 )))#line:534
                        for (OOOO000OOO0O00OO0 ,OOO0OO00OO000OOOO )in O0O00OO00O00O00OO :#line:535
                                print ('Testing:',OOOO000OOO0O00OO0 ,OOO0OO00OO000OOOO )#line:536
                                O00OOO0O0OOO000OO =OO0OO0OO000O0O000 (OOOO000OOO0O00OO0 ,OOO0OO00OO000OOOO )#line:537
                                print ('Output:',*O00OOO0O0OOO000OO )#line:538
                                OOO0O0OOO0OOOO0O0 =O000OO0000OOO0O00 (OOOO000OOO0O00OO0 ,OOO0OO00OO000OOOO )#line:539
                                print ('Actual:',*OOO0O0OOO0OOOO0O0 )#line:540
                                print ()#line:541
                                if (not type (O00OOO0O0OOO000OO )==type (OOO0O0OOO0OOOO0O0 ))or (not len (O00OOO0O0OOO000OO )==len (OOO0O0OOO0OOOO0O0 )):#line:542
                                        if O00000OO0OO0O0OO0 ==False :#line:543
                                           O00000OO0OO0O0OO0 =True #line:544
                                else :#line:545
                                        O0O00OOOOO00OOO0O .append (all (np .isclose (O00OOO0O0OOO000OO ,OOO0O0OOO0OOOO0O0 ,O0O000O000OOO0OOO )))#line:546
                        if O00000OO0OO0O0OO0 :#line:548
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:549
                        else :#line:551
                                O0O0OO000OOOO0OOO =all (O0O00OOOOO00OOO0O )#line:552
                                if O0O0OO000OOOO0OOO :#line:553
                                        print ("Well done, all correct.")#line:554
                                else :#line:555
                                        print ("Not right yet. Take another look then run this cell again.")#line:556
                                OOOOO00O00O0OOO0O =trycount (O0OOO0000000O00OO ,O0O0OO000OOOO0OOO )#line:558
                                OOOO0000000O00O0O =100 -(OOOOO00O00O0OOO0O [0 ]-1 )*10 #line:559
                                if OOOOO00O00O0OOO0O [1 ]:#line:560
                                        print ("First success after ",OOOOO00O00O0OOO0O [0 ]," tries, you have ",OOOO0000000O00O0O ,"% on this exercise.")#line:561
                                else :#line:562
                                        print ("You have had ",OOOOO00O00O0OOO0O [0 ]," tries.")#line:563
                                        print ("If next try is accepted you will achieve ",OOOO0000000O00O0O -10 ,"% on this exercise.")#line:564
                        OOO0O0OOO0OOOO0O0 =None #line:567
                        O000OO0000OOO0O00 =None #line:568
        return #line:570
def a8_notlive (OO0O0OO0O000O0O00 ):#line:580
        OO0OO00O0OO00OOO0 =".a8_counter.npy"#line:584
        OOO000O0000OO000O =np .zeros (1 ,dtype ='int8,bool')#line:585
        def O0OO00OOO00O00OO0 ():#line:587
                pass #line:588
        O0000O000OO0O0O00 =1.0e-4 #line:592
        if (waiter ()):#line:595
                printmd ('**CA** (6%)')#line:597
                if not type (OO0O0OO0O000O0O00 )==type (O0OO00OOO00O00OO0 ):#line:601
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:602
                else :#line:606
                        import inspect #line:609
                        OOO00O0OO0OOO00O0 =inspect .getsourcelines (OO0O0OO0O000O0O00 )#line:610
                        O0OOOOOOOO00O00OO =True #line:611
                        OO0O0OO0OOO00000O =[]#line:612
                        for OO0O00OO0OO0000OO ,O0O0000O00OO00000 in enumerate (OOO00O0OO0OOO00O0 [0 ]):#line:613
                                if 'for'in O0O0000O00OO00000 or 'while'in O0O0000O00OO00000 :#line:614
                                        O0OOOOOOOO00O00OO =False #line:616
                                        OO0O0OO0OOO00000O .append (OO0O00OO0OO0000OO )#line:617
                        if not O0OOOOOOOO00O00OO :#line:618
                                print ('Function needs to be written without loops (using NumPy), check lines',*OO0O0OO0OOO00000O )#line:619
                                print ('No marks lost for this attempt.')#line:620
                                return #line:621
                        def OO0OOOO00000O0O0O (OO0OOOO0OOO0OOOOO ):#line:624
                                OOOO00O00OO000O00 =np .vstack ((OO0OOOO0OOO0OOOOO ,OO0OOOO0OOO0OOOOO [0 ]))#line:625
                                OO0OOOO00OO00OO0O =sum (OOOO00O00OO000O00 [:-1 ,0 ]*OOOO00O00OO000O00 [1 :,1 ])#line:626
                                O0OO0000OOO00O0O0 =sum (OOOO00O00OO000O00 [:-1 ,1 ]*OOOO00O00OO000O00 [1 :,0 ])#line:627
                                return abs (OO0OOOO00OO00OO0O -O0OO0000OOO00O0O0 )/2 #line:628
                        import random as r #line:631
                        OOOOOO00OO000O0OO =r .randint (6 ,11 )#line:632
                        OO00000O0O0OOOO0O =np .ones ((OOOOOO00OO000O0OO ,2 ))#line:633
                        O0OO0OOO0OOO00OO0 =False #line:634
                        OO0O0O00O000OO0O0 =[]#line:635
                        OOO00O00OOO0OO0OO =1. #line:636
                        OOO0OOOO0O0O000OO =20. #line:637
                        O00O0000OOO00OOOO =OOO00O00OOO0OO0OO #line:638
                        O000O00OO000O00OO =OOO0OOOO0O0O000OO #line:639
                        for OO00OO0OO00000O00 in range (OOOOOO00OO000O0OO ):#line:640
                                OO00000O0O0OOOO0O [OO00OO0OO00000O00 ]=[r .uniform (OOO00O00OOO0OO0OO ,OOO0OOOO0O0O000OO ),r .uniform (O00O0000OOO00OOOO ,O000O00OO000O00OO )]#line:641
                        print ('Testing:',OO00000O0O0OOOO0O )#line:642
                        O0O0000OOO0OOO0OO =OO0O0OO0O000O0O00 (OO00000O0O0OOOO0O )#line:643
                        print ('Output:',O0O0000OOO0OOO0OO )#line:644
                        O000O0O00O0O0OO00 =OO0OOOO00000O0O0O (OO00000O0O0OOOO0O )#line:645
                        print ('Actual:',O000O0O00O0O0OO00 )#line:646
                        print ()#line:647
                        if not type (O0O0000OOO0OOO0OO )==type (O000O0O00O0O0OO00 ):#line:648
                                if O0OO0OOO0OOO00OO0 ==False :#line:649
                                        O0OO0OOO0OOO00OO0 =True #line:650
                        else :#line:651
                                OO0O0O00O000OO0O0 .append (np .isclose (O0O0000OOO0OOO0OO ,O000O0O00O0O0OO00 ,O0000O000OO0O0O00 ))#line:652
                        if O0OO0OOO0OOO00OO0 :#line:654
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:655
                        else :#line:657
                                OO0O0O0OOOOOOO0O0 =all (OO0O0O00O000OO0O0 )#line:658
                                if OO0O0O0OOOOOOO0O0 :#line:659
                                        print ("Well done, all correct.")#line:660
                                else :#line:661
                                        print ("Not right yet. Take another look then run this cell again.")#line:662
                                OOO000O0000OO000O =trycount (OO0OO00O0OO00OOO0 ,OO0O0O0OOOOOOO0O0 )#line:664
                                O0OOO0000OOOO0O00 =100 -(OOO000O0000OO000O [0 ]-1 )*10 #line:665
                                if OOO000O0000OO000O [1 ]:#line:666
                                        print ("First success after ",OOO000O0000OO000O [0 ]," tries, you have ",O0OOO0000OOOO0O00 ,"% on this exercise.")#line:667
                                else :#line:668
                                        print ("You have had ",OOO000O0000OO000O [0 ]," tries.")#line:669
                                        print ("If next try is accepted you will achieve ",O0OOO0000OOOO0O00 -10 ,"% on this exercise.")#line:670
                        O000O0O00O0O0OO00 =None #line:673
                        OO0OOOO00000O0O0O =None #line:674
        return #line:676
def a1_notlive ():#line:692
        print ('This CA test is not currently live.')#line:693
        return #line:694
def a2 (OO000O000OOO0O0O0 ):#line:702
        print ('This CA test is not currently live.')#line:703
        return #line:704
def a3 (O00OO0OO0OO0000O0 ):#line:712
        print ('This CA test is not currently live.')#line:713
        return #line:714
def a4 (OOO0OO000000OO0O0 ):#line:722
        print ('This CA test is not currently live.')#line:723
        return #line:724
def a5 (O0000OO000OOO0000 ):#line:732
        print ('This CA test is not currently live.')#line:733
        return #line:734
def a6 (O00OO0OOOO0OOO00O ):#line:742
        print ('This CA test is not currently live.')#line:743
        return #line:744
def a7 ():#line:752
        print ('This CA test is not currently live.')#line:753
        return #line:754
def a8 (O0OOOOOOOOOO0O00O ):#line:762
        print ('This CA test is not currently live.')#line:763
        return #line:764
def b1 ():#line:782
    global ps #line:784
    OOOO00000O0000OO0 =".b1_counter.npy"#line:787
    OO0OOO000O0000OOO =np .zeros (1 ,dtype ='int8,bool')#line:788
    O0000O0000000O0O0 =0.05 #line:790
    if (waiter ()):#line:792
        while True :#line:793
            try :#line:794
                printmd ('**CA**')#line:795
                O0OOOO0O0OO00O0O0 =eval (input ("Please enter your answer here in the format D,k: "))#line:796
                O000000OO0O0OOO00 =(0.025 ,2.0 )#line:797
                O0OO0OO0OO0OOO0OO =all (np .isclose (O0OOOO0O0OO00O0O0 ,O000000OO0O0OOO00 ,rtol =O0000O0000000O0O0 ))#line:798
                if O0OO0OO0OO0OOO0OO :#line:799
                    print ("Well done, reasonable estimate is ",O000000OO0O0OOO00 )#line:800
                else :#line:801
                    print ("Not right yet. Take another look then run this cell again.")#line:802
                OO0OOO000O0000OOO =trycount (OOOO00000O0000OO0 ,O0OO0OO0OO0OOO0OO )#line:804
                OO000OOO000O0O0OO =100 -(OO0OOO000O0000OOO [0 ]-1 )*10 #line:805
                if OO0OOO000O0000OOO [1 ]:#line:806
                    print ("First success after ",OO0OOO000O0000OOO [0 ]," tries, you have ",OO000OOO000O0O0OO ,"% on this exercise.")#line:807
                else :#line:808
                    print ("You have had ",OO0OOO000O0000OOO [0 ]," tries.")#line:809
                    print ("If next try is accepted you will achieve ",OO000OOO000O0O0OO -10 ,"% on this exercise.")#line:810
                break #line:812
            except ValueError :#line:814
                print ("I didn't understand that.")#line:815
                continue #line:816
        return #line:818
def b2 (O00OO000OO0OO00O0 ):#line:828
        O00OOOO0OO0OOO0OO =".b2_counter.npy"#line:832
        O0OO00OO000O0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:833
        def OO0OO0OOOO000O00O ():#line:835
                pass #line:836
        OO0O0O0O0OOOO00O0 =1.0e-2 #line:839
        O0O00000O00OO0000 =0.0 #line:840
        if (waiter ()):#line:842
                printmd ('**CA**')#line:844
                if not type (O00OO000OO0OO00O0 )==type (OO0OO0OOOO000O00O ):#line:846
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:847
                else :#line:850
                        def O0OO0O0OOOO0O0OOO (O00OO0O00O0000O0O ):#line:854
                                O0O0O0O00O00O0OOO =[]#line:855
                                OOO000OOO0000OOO0 =20.0 #line:856
                                OO0O000OOO00OOOOO =58.1e-3 #line:857
                                OO000000O000O0O0O =9.81 #line:858
                                O000000000OOO0OOO =0.0 #line:859
                                OO0000OO0O00OOOOO =0.0 #line:860
                                OO00O00O00OO00OO0 =0.0 #line:861
                                O0OOOO00OO0O0O00O =10 #line:862
                                O0OO0O00OO0000OOO =3.35e-2 #line:863
                                OOO00O00OO000OOO0 =0.51 #line:864
                                O0OOOOO0000OO0000 =1.25 #line:865
                                OOO0OOOOO0OO0O0O0 =math .pi *O0OO0O00OO0000OOO **2 #line:866
                                O00O000OO00O0O00O =0.5 *OOO00O00OO000OOO0 *OOO0OOOOO0OO0O0O0 *O0OOOOO0000OO0000 #line:867
                                OOO0OOO0O0O0OO0O0 =100000 #line:869
                                O0OO0O0OOOO00O00O =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:870
                                O00OOOOOOO000OOOO =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:871
                                OO0OO00O0000O0OOO =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:872
                                OO0O0OO00OO00O000 =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:873
                                OOOO0O00O00000OO0 =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:874
                                O0OOOOOOO0000O000 =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:875
                                O00OOO0OOO0000O00 =np .zeros (OOO0OOO0O0O0OO0O0 ,float )#line:876
                                O0OO0O0OOOO00O00O ,O0OOOO00O0OOO0OO0 =np .linspace (OO00O00O00OO00OO0 ,O0OOOO00OO0O0O00O ,OOO0OOO0O0O0OO0O0 ,retstep =True )#line:877
                                for OO00O0O00000OO00O in O00OO0O00O0000O0O :#line:879
                                        OO000O0O00OOO000O =OOO000OOO0000OOO0 *math .cos (OO00O0O00000OO00O )#line:880
                                        O000OO00OO0O0O00O =OOO000OOO0000OOO0 *math .sin (OO00O0O00000OO00O )#line:881
                                        O0OOOOOOO0000O000 [0 ]=O000000000OOO0OOO #line:883
                                        O00OOO0OOO0000O00 [0 ]=OO0000OO0O00OOOOO #line:884
                                        OO0O0OO00OO00O000 [0 ]=OO000O0O00OOO000O #line:885
                                        OOOO0O00O00000OO0 [0 ]=O000OO00OO0O0O00O #line:886
                                        for O0O0OO000000OOO0O in range (OOO0OOO0O0O0OO0O0 -1 ):#line:887
                                                OOO000OOOOOOO0O0O =math .sqrt (OO0O0OO00OO00O000 [O0O0OO000000OOO0O ]**2 +OOOO0O00O00000OO0 [O0O0OO000000OOO0O ]**2 )#line:888
                                                OO0000O00OOOO0O0O =-O00O000OO00O0O00O *OOO000OOOOOOO0O0O *OO0O0OO00OO00O000 [O0O0OO000000OOO0O ]#line:889
                                                O00OOOOOOO000OOOO [O0O0OO000000OOO0O ]=OO0000O00OOOO0O0O /OO0O000OOO00OOOOO #line:890
                                                OO0O0OO00OO00O000 [O0O0OO000000OOO0O +1 ]=OO0O0OO00OO00O000 [O0O0OO000000OOO0O ]+O00OOOOOOO000OOOO [O0O0OO000000OOO0O ]*O0OOOO00O0OOO0OO0 #line:891
                                                O0OOOOOOO0000O000 [O0O0OO000000OOO0O +1 ]=O0OOOOOOO0000O000 [O0O0OO000000OOO0O ]+OO0O0OO00OO00O000 [O0O0OO000000OOO0O +1 ]*O0OOOO00O0OOO0OO0 #line:892
                                                OOO0000O0O00OO0OO =-OO0O000OOO00OOOOO *OO000000O000O0O0O -O00O000OO00O0O00O *OOO000OOOOOOO0O0O *OOOO0O00O00000OO0 [O0O0OO000000OOO0O ]#line:893
                                                OO0OO00O0000O0OOO [O0O0OO000000OOO0O ]=OOO0000O0O00OO0OO /OO0O000OOO00OOOOO #line:894
                                                OOOO0O00O00000OO0 [O0O0OO000000OOO0O +1 ]=OOOO0O00O00000OO0 [O0O0OO000000OOO0O ]+OO0OO00O0000O0OOO [O0O0OO000000OOO0O ]*O0OOOO00O0OOO0OO0 #line:895
                                                O00OOO0OOO0000O00 [O0O0OO000000OOO0O +1 ]=O00OOO0OOO0000O00 [O0O0OO000000OOO0O ]+OOOO0O00O00000OO0 [O0O0OO000000OOO0O +1 ]*O0OOOO00O0OOO0OO0 #line:896
                                                if (O00OOO0OOO0000O00 [O0O0OO000000OOO0O +1 ]<0 ):#line:897
                                                        break #line:898
                                        O000O0O00OOO0OO00 =O0O0OO000000OOO0O #line:899
                                        O0O0O0O00O00O0OOO .append (O0OOOOOOO0000O000 [O000O0O00OOO0OO00 ])#line:900
                                return (O0O0O0O00O00O0OOO );#line:902
                        import random as r #line:905
                        O0O0OO00O0OO0O00O =[]#line:906
                        O00O00O000O0OOOO0 =False #line:907
                        OO0O0OO00O0OO0O0O =[]#line:908
                        O0OO0O0OOO0OO00OO =0.1 #line:909
                        O0O0O000OO0000OOO =1.5 #line:910
                        for O0000O0OOOO00OO0O in range (5 ):#line:911
                                O0O0OO00O0OO0O00O .append (r .uniform (O0OO0O0OOO0OO00OO ,O0O0O000OO0000OOO ))#line:912
                        O0O0OO00O0OO0O00O .sort ()#line:913
                        print ('Testing thetas=',O0O0OO00O0OO0O00O )#line:914
                        OOOO0OOO0000O000O =O00OO000OO0OO00O0 (O0O0OO00O0OO0O00O )#line:915
                        print ('Output ximpacts=',OOOO0OOO0000O000O )#line:916
                        O00OOO0O0OO0OOOO0 =O0OO0O0OOOO0O0OOO (O0O0OO00O0OO0O00O )#line:917
                        print ('Actual ximpacts=',O00OOO0O0OO0OOOO0 )#line:918
                        print ()#line:919
                        if (not type (OOOO0OOO0000O000O )==type (O00OOO0O0OO0OOOO0 ))or (not len (OOOO0OOO0000O000O )==len (O00OOO0O0OO0OOOO0 )):#line:920
                                if O00O00O000O0OOOO0 ==False :#line:921
                                        O00O00O000O0OOOO0 =True #line:922
                        else :#line:923
                                OO0O0OO00O0OO0O0O .append (all (np .isclose (OOOO0OOO0000O000O ,O00OOO0O0OO0OOOO0 ,rtol =OO0O0O0O0OOOO00O0 ,atol =O0O00000O00OO0000 )))#line:924
                        if O00O00O000O0OOOO0 :#line:926
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:927
                        else :#line:929
                                O00OOO0OOOOO0000O =all (OO0O0OO00O0OO0O0O )#line:930
                                if O00OOO0OOOOO0000O :#line:931
                                        print ("Well done, all correct.")#line:932
                                else :#line:933
                                        print ("Not close enough. Take another look then run this cell again.")#line:934
                                O0OO00OO000O0OO0O =trycount (O00OOOO0OO0OOO0OO ,O00OOO0OOOOO0000O )#line:936
                                O0O0OOOOO00O00000 =100 -(O0OO00OO000O0OO0O [0 ]-1 )*10 #line:937
                                if O0OO00OO000O0OO0O [1 ]:#line:938
                                        print ("First success after ",O0OO00OO000O0OO0O [0 ]," tries, you have ",O0O0OOOOO00O00000 ,"% on this exercise.")#line:939
                                else :#line:940
                                        print ("You have had ",O0OO00OO000O0OO0O [0 ]," tries.")#line:941
                                        print ("If next try is accepted you will achieve ",O0O0OOOOO00O00000 -10 ,"% on this exercise.")#line:942
                        O00OOO0O0OO0OOOO0 =None #line:945
                        O0OO0O0OOOO0O0OOO =None #line:946
        return #line:948
def b3 ():#line:958
    global ps #line:960
    O00O0OOOOO0O0O00O =".b3_counter.npy"#line:963
    OO0O0000000O00O0O =np .zeros (1 ,dtype ='int8,bool')#line:964
    O0O0OOOOO000OO00O =0.01 #line:967
    if (waiter ()):#line:969
        while True :#line:970
            try :#line:971
                printmd ('**CA**')#line:972
                O0O00O000O00O0O00 =float (input ("Enter a real number here: "))#line:973
                OOOOO0OOO0O000O00 =0.5 #line:974
                OOOOOO0OO00000000 =np .isclose (O0O00O000O00O0O00 ,OOOOO0OOO0O000O00 ,atol =O0O0OOOOO000OO00O )#line:975
                if OOOOOO0OO00000000 :#line:976
                    print ("Well done. Actual value is ",OOOOO0OOO0O000O00 )#line:977
                else :#line:978
                    print ("Not right yet. Take another look then run this cell again.")#line:979
                OO0O0000000O00O0O =trycount (O00O0OOOOO0O0O00O ,OOOOOO0OO00000000 )#line:981
                O0O0OOO00OO0OO000 =100 -(OO0O0000000O00O0O [0 ]-1 )*10 #line:982
                if OO0O0000000O00O0O [1 ]:#line:983
                    print ("First success after ",OO0O0000000O00O0O [0 ]," tries, you have ",O0O0OOO00OO0OO000 ,"% on this exercise.")#line:984
                else :#line:985
                    print ("You have had ",OO0O0000000O00O0O [0 ]," tries.")#line:986
                    print ("If next try is accepted you will achieve ",O0O0OOO00OO0OO000 -10 ,"% on this exercise.")#line:987
                break #line:989
            except ValueError :#line:991
                print ("I didn't understand that.")#line:992
                continue #line:993
        return #line:995
def b1_notlive ():#line:1007
        print ('This CA test is not currently live.')#line:1008
        return #line:1009
def b2_notlive (O0O00O0OOOOO0OOOO ):#line:1019
        print ('This CA test is not currently live.')#line:1020
        return #line:1021
def b3_notlive ():#line:1028
        print ('This CA test is not currently live.')#line:1029
        return #line:1030
def printmd (O00OO00O00OO0000O ):#line:1040
    display (Markdown (O00OO00O00OO0000O ))#line:1041
def repeat_to_length (O0OO0OOOOO0000O0O ,O00000OOOOOO0O0O0 ):#line:1043
   return (O0OO0OOOOO0000O0O *((O00000OOOOOO0O0O0 //len (O0OO0OOOOO0000O0O ))+1 ))[:O00000OOOOOO0O0O0 ]#line:1044
def getco (OO0OOOO0O0OO0O0OO ):#line:1046
    global ps #line:1047
    O0OOOOOO00000OO00 =getpass .getuser ()#line:1048
    O000O000O00O000OO =int .from_bytes (O0OOOOOO00000OO00 .encode (),'little')#line:1049
    OOO00O00000OOO000 =str (O000O000O00O000OO )#line:1050
    OOOO0OOO0O00O0O00 =repeat_to_length (OOO00O00000OOO000 ,OO0OOOO0O0OO0O0OO )#line:1051
    ps =[int (O00000OOOO0000O0O )+1 for O00000OOOO0000O0O in OOOO0OOO0O00O0O00 ]#line:1052
def waiter ():#line:1055
    O00OOOOO0O0OOOO00 =20 #line:1058
    OOOO00O0000O000OO =".ts1.txt"#line:1060
    if os .path .isfile (OOOO00O0000O000OO ):#line:1061
        O0OOOO000OOO0O00O =np .loadtxt (OOOO00O0000O000OO )#line:1062
    else :#line:1064
        O0OOOO000OOO0O00O =0.0 #line:1065
    OO000O00OO0OO0OOO =time .time ()#line:1068
    O00O0O0O00000O0O0 =OO000O00OO0OO0OOO -O0OOOO000OOO0O00O #line:1069
    if (O00O0O0O00000O0O0 <O00OOOOO0O0OOOO00 ):#line:1071
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O00O0O0O00000O0O0 ,O00OOOOO0O0OOOO00 ))#line:1072
        return False #line:1073
    else :#line:1074
        O000000O0OOO000OO =open (OOOO00O0000O000OO ,'w')#line:1075
        O000000O0OOO000OO .write (str (OO000O00OO0OO0OOO ))#line:1076
        O000000O0OOO000OO .close ()#line:1077
        return True #line:1078
def trycount (OOOOO000000000O0O ,OOO00OOOOO0O0OO0O ):#line:1080
    if os .path .isfile (OOOOO000000000O0O ):#line:1082
        OO00OO000000O0OOO =np .load (OOOOO000000000O0O )#line:1083
    else :#line:1085
        OO00OO000000O0OOO =np .zeros (1 ,dtype ='int8,bool')#line:1086
        OO00OO000000O0OOO =[0 ,False ]#line:1087
    if not OO00OO000000O0OOO [1 ]:#line:1090
        OO00OO000000O0OOO [0 ]+=1 #line:1091
        OO00OO000000O0OOO [1 ]=OOO00OOOOO0O0OO0O #line:1092
        np .save (OOOOO000000000O0O ,OO00OO000000O0OOO )#line:1094
    return OO00OO000000O0OOO #line:1096
def valdho (OO0O0000OOO0OO0O0 ,O00000O00O000OO0O ):#line:1104
    O0OOO0000O0OO0OOO =".dho_counter.npy"#line:1108
    OO00OOOO0OOO0O000 =np .zeros (1 ,dtype ='int8,bool')#line:1110
    if (waiter ()):#line:1112
        while True :#line:1113
            try :#line:1114
                OOO00O0O0OO0OOO0O =float (input ("Please enter your estimate here: "))#line:1115
                OO000O000OOO0OOO0 =2 *np .sqrt (OO0O0000OOO0OO0O0 *O00000O00O000OO0O )#line:1116
                O0O0O00O0OO000000 =np .isclose (OOO00O0O0OO0OOO0O ,OO000O000OOO0OOO0 ,0.2 )#line:1117
                if O0O0O00O0OO000000 :#line:1118
                    print ("Well done, that is close to the critical damping value ",OO000O000OOO0OOO0 )#line:1119
                else :#line:1120
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1121
                OO00OOOO0OOO0O000 =trycount (O0OOO0000O0OO0OOO ,O0O0O00O0OO000000 )#line:1123
                O0OO0O0O0000O0O00 =100 -(OO00OOOO0OOO0O000 [0 ]-1 )*10 #line:1124
                if OO00OOOO0OOO0O000 [1 ]:#line:1125
                    print ("First success after ",OO00OOOO0OOO0O000 [0 ]," tries, you have ",O0OO0O0O0000O0O00 ,"% on this exercise.")#line:1126
                else :#line:1127
                    print ("You have had ",OO00OOOO0OOO0O000 [0 ]," tries.")#line:1128
                    print ("If next try is accepted you will achieve ",O0OO0O0O0000O0O00 -10 ,"% on this exercise.")#line:1129
                break #line:1131
            except ValueError :#line:1133
                print ("I didn't understand that.")#line:1134
                continue #line:1135
        return #line:1138
def valdrivendho (O0O0O0000O00OOOOO ,OO0000OOO00O0OOOO ):#line:1148
    O00OO0OOOO0O0OOOO =".drivendho_counter.npy"#line:1152
    OO00OO0O00OOOO0OO =np .zeros (1 ,dtype ='int8,bool')#line:1154
    if (waiter ()):#line:1156
        while True :#line:1157
            try :#line:1158
                OO0000OO00O00OO00 =float (input ("Please enter your estimate here: "))#line:1159
                O00OO00OO00OOO00O =np .sqrt (O0O0O0000O00OOOOO **2 -2 *OO0000OOO00O0OOOO **2 )#line:1160
                O0OO00OOO0O0O0000 =np .isclose (OO0000OO00O00OO00 ,O00OO00OO00OOO00O ,0.2 )#line:1161
                if O0OO00OOO0O0O0000 :#line:1162
                    print ("Well done, that is close to the resonance value ",O00OO00OO00OOO00O )#line:1163
                else :#line:1164
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1165
                OO00OO0O00OOOO0OO =trycount (O00OO0OOOO0O0OOOO ,O0OO00OOO0O0O0000 )#line:1167
                OO00O0O0OO0O0OOOO =100 -(OO00OO0O00OOOO0OO [0 ]-1 )*10 #line:1168
                if OO00OO0O00OOOO0OO [1 ]:#line:1169
                    print ("First success after ",OO00OO0O00OOOO0OO [0 ]," tries, you have ",OO00O0O0OO0O0OOOO ,"% on this exercise.")#line:1170
                else :#line:1171
                    print ("You have had ",OO00OO0O00OOOO0OO [0 ]," tries.")#line:1172
                    print ("If next try is accepted you will achieve ",OO00O0O0OO0O0OOOO -10 ,"% on this exercise.")#line:1173
                break #line:1175
            except ValueError :#line:1177
                print ("I didn't understand that.")#line:1178
                continue #line:1179
        return #line:1182
import ipywidgets as widgets #line:1197
import sys #line:1198
from IPython .display import display #line:1199
from IPython .display import clear_output #line:1200
def create_multipleChoice_widget (O0O0OO000000OOO00 ,O0O00OOO00OO00000 ,OOOOO000O00OOOOOO ,O0000O0OO00O0O0O0 ):#line:1202
    O0OOO0OO0O0000O00 ='.q{:d}_counter.npy'.format (O0O0OO000000OOO00 )#line:1203
    OOOO0OOOOOOOOO0O0 =np .zeros (1 ,dtype ='int8,bool')#line:1204
    O0O0O0OOO0000O00O =len (OOOOO000O00OOOOOO )#line:1206
    if O0000O0OO00O0O0O0 not in OOOOO000O00OOOOOO :#line:1207
        OOOOO000O00OOOOOO .append (O0000O0OO00O0O0O0 )#line:1208
    O0OOOOO0OOOO0000O =OOOOO000O00OOOOOO .index (O0000O0OO00O0O0O0 )#line:1210
    O00OO000OOO0OO0OO =[(OOOOO0O0O0OOOOO00 ,OO0O0OOO0OOOO0000 )for OO0O0OOO0OOOO0000 ,OOOOO0O0O0OOOOO00 in enumerate (OOOOO000O00OOOOOO )]#line:1212
    OO000O0O0OO00OO00 =widgets .RadioButtons (options =O00OO000OOO0OO0OO ,description ='',disabled =False )#line:1217
    OOO000OO00O000OO0 =widgets .Output ()#line:1219
    with OOO000OO00O000OO0 :#line:1220
        print (O0O00OOO00OO00000 )#line:1221
    OOOOOO0OO0O00O00O =widgets .Output ()#line:1223
    def O00O00O0OO00OO000 (OO0OO000O000OOOO0 ):#line:1225
        OO00OOOO0OO000000 =int (OO000O0O0OO00OO00 .value )#line:1227
        O0OO0OOO0OO0OOOOO =OO00OOOO0OO000000 ==O0OOOOO0OOOO0000O #line:1229
        OOOOOO0OOO00O0OOO =trycount (O0OOO0OO0O0000O00 ,O0OO0OOO0OO0OOOOO )#line:1230
        OO0O00O0O0OO0OOO0 =max (0 ,100 -(OOOOOO0OOO00O0OOO [0 ]-1 )*100 /O0O0O0OOO0000O00O )#line:1231
        OOOO00O000O0O000O =OO000O0O0OO00OO00 .options [OO00OOOO0OO000000 ][0 ]#line:1232
        if O0OO0OOO0OO0OOOOO :#line:1233
            OOOO00O000O0O000O +=' correct\n'#line:1234
        else :#line:1235
            OOOO00O000O0O000O +=' incorrect\n'#line:1236
        if OOOOOO0OOO00O0OOO [1 ]:#line:1237
            OOOO00O000O0O000O +='{:.0f}% on try {:d}'.format (OO0O00O0O0OO0OOO0 ,OOOOOO0OOO00O0OOO [0 ])#line:1238
        else :#line:1239
            OOOO00O000O0O000O +='{:.0f}% remaining'.format (max (0 ,OO0O00O0O0OO0OOO0 -100 /O0O0O0OOO0000O00O ))#line:1240
        with OOOOOO0OO0O00O00O :#line:1242
            clear_output ()#line:1243
            print (OOOO00O000O0O000O )#line:1244
        return #line:1245
    OO00OOO0OOOOOO00O =widgets .Button (description ="submit")#line:1247
    OO00OOO0OOOOOO00O .on_click (O00O00O0OO00OO000 )#line:1248
    return widgets .VBox ([OOO000OO00O000OO0 ,OO000O0O0OO00OO00 ,OO00OOO0OOOOOO00O ,OOOOOO0OO0O00O00O ])#line:1249
def runq1 ():#line:1256
    OOOO0OOOOO0OO0000 =1 #line:1257
    O00OO000O0O0O0OOO =create_multipleChoice_widget (OOOO0OOOOO0OO0000 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1258
    display (O00OO000O0O0O0OOO )#line:1259
def runQ1 ():#line:1269
    OOO00O0000000OO0O =1 #line:1270
    OOOOOO00O0OOOOO0O =create_multipleChoice_widget (OOO00O0000000OO0O ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1271
    display (OOOOOO00O0OOOOO0O )#line:1272
def runQ2x ():#line:1281
    OOO00O0O00OO0O00O =2 #line:1282
    OOOOO0O000OOOO0O0 =create_multipleChoice_widget (OOO00O0O00OO0O00O ,'',['centred','backwards','forwards'],'centred')#line:1283
    display (OOOOO0O000OOOO0O0 )#line:1284
def runQ3x ():#line:1292
    OOOO0OO0O00OOO0OO =3 #line:1293
    O00O0OOO00OOO000O =create_multipleChoice_widget (OOOO0OO0O00OOO0OO ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1294
    display (O00O0OOO00OOO000O )#line:1295
def runQ4x ():#line:1304
    O00O00OO0000O000O =4 #line:1305
    O00OOO00OO0O0OO00 =create_multipleChoice_widget (O00O00OO0000O000O ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1306
    display (O00OOO00OO0O0OO00 )#line:1307
def runQ5x ():#line:1317
    O0O000OO0O00O000O =5 #line:1318
    OO0O00OO0OO000O0O =create_multipleChoice_widget (O0O000OO0O00O000O ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1319
    display (OO0O00OO0OO000O0O )#line:1320
def runQ6x ():#line:1329
    O0OO0OO0O0O00O0O0 =6 #line:1330
    OO00OOO00OOO00OOO =create_multipleChoice_widget (O0OO0OO0O0O00O0O0 ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1331
    display (OO00OOO00OOO00OOO )#line:1332
def runQ7x ():#line:1341
    OO0000OO00O00O000 =7 #line:1342
    O0000O0O000000000 =create_multipleChoice_widget (OO0000OO00O00O000 ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1343
    display (O0000O0O000000000 )#line:1344
pk =(283355 ,839329 )#line:1364
def getrid ():#line:1367
    import random #line:1368
    global rid #line:1369
    rid =random .randint (100000 ,999999 )#line:1370
def encrypt (OO0O000O000000O00 ):#line:1373
    O000OO0OOO0000O00 ,O000O0O0OO00O000O =pk #line:1374
    O0OO00OO00OO0O00O =len (str (O000O0O0OO00O000O ))#line:1375
    if O0OO00OO00OO0O00O !=6 :#line:1376
        print ('Chunk length hardcoded in format conversion to 6 characters.\n May need to adjust here and in getrid range.\n Exiting.\n')#line:1377
    O0OOOOOO0O0O0O000 =['{:06d}'.format ((int (OO0OOOO0OOO0O00OO )**O000OO0OOO0000O00 )%O000O0O0OO00O000O )for OO0OOOO0OOO0O00OO in str (OO0O000O000000O00 )]#line:1380
    return ''.join (O0OOOOOO0O0O0O000 )#line:1383
def genenc (O0OO0O00OOO0OO0OO ,O00OOOOOO0OOOO00O ):#line:1386
    global rid #line:1387
    O00OOO000O00O00OO ='{:06d}'.format (rid )#line:1388
    OOOO0OOO00OOOOO0O ='{:02d}'.format (O0OO0O00OOO0OO0OO )#line:1389
    O000O0OO000OOO00O ='{:03d}'.format (O00OOOOOO0OOOO00O )#line:1390
    OOO000000OOO0O000 =O00OOO000O00O00OO +OOOO0OOO00OOOOO0O +O000O0OO000OOO00O #line:1392
    O0000OO0OOO0OO0O0 ='#'+encrypt (OOO000000OOO0O000 )+'#'#line:1394
    print ("Your encrypted message is: ",O0000OO0OOO0OO0O0 )#line:1395
    return O0000OO0OOO0OO0O0 #line:1396
