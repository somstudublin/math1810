import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (O00OOOO0000O0OOOO ,O00O0OO00OOO00OOO ):#line:11
        print ("\nPasswords may not be changed using this notebook at present.")#line:15
ps =[]#line:19
wd =''#line:20
rid =0 #line:21
encoff1 =34 #line:22
encoff2 =567 #line:23
def a1 ():#line:41
    global ps #line:43
    OO00O0OOO0OOOO0O0 =".a1_counter.npy"#line:46
    OO0O000000OOO00OO =np .zeros (1 ,dtype ='int8,bool')#line:47
    O00OOO000000O00OO =0 #line:49
    O00O0OO0OO0O0OO00 =ps [0 ]#line:50
    OO00OO0OOOO0OOOOO =ps [1 ]#line:51
    if (waiter ()):#line:53
        while True :#line:54
            try :#line:55
                printmd ('**CA** (2%)')#line:56
                print (O00O0OO0OO0O0OO00 ,"+",OO00OO0OOOO0OOOOO )#line:57
                print ('tester')#line:58
                OO0000OO0O0OOO0O0 =float (input ("Please enter your answer here: "))#line:59
                OO000OOO0O00000O0 =O00O0OO0OO0O0OO00 +OO00OO0OOOO0OOOOO #line:60
                OOO0OO0OOOO0O00O0 =np .isclose (OO0000OO0O0OOO0O0 ,OO000OOO0O00000O0 ,O00OOO000000O00OO )#line:61
                if OOO0OO0OOOO0O00O0 :#line:62
                    print ("Well done, right answer is ",OO000OOO0O00000O0 )#line:63
                else :#line:64
                    print ("Not right yet. Take another look then run this cell again.")#line:65
                OO0O000000OOO00OO =trycount (OO00O0OOO0OOOO0O0 ,OOO0OO0OOOO0O00O0 )#line:67
                O00OOOOO00000O0OO =100 -(OO0O000000OOO00OO [0 ]-1 )*10 #line:68
                if OO0O000000OOO00OO [1 ]:#line:69
                    print ("First success after ",OO0O000000OOO00OO [0 ]," tries, you have ",O00OOOOO00000O0OO ,"% on this exercise.")#line:70
                    print ("Enter this code into Brightspace:\n\n",genenc (1 +encoff1 ,O00OOOOO00000O0OO +encoff2 ),'\n')#line:71
                else :#line:72
                    print ("You have had ",OO0O000000OOO00OO [0 ]," tries.")#line:73
                    print ("If next try is accepted you will achieve ",O00OOOOO00000O0OO -10 ,"% on this exercise.")#line:74
                break #line:76
            except ValueError :#line:78
                print ("I didn't understand that.")#line:79
                continue #line:80
        return #line:82
def a2 (O00OOO0OOOOOOO00O ):#line:91
    global ps #line:93
    O00O0O00O00O0O0OO =".a2_counter.npy"#line:96
    OOOOO000OO0OO0OO0 =np .zeros (1 ,dtype ='int8,bool')#line:97
    O0O0OO00OO0OO0OOO =6 #line:100
    O0OO0O000OOO00OOO =7 #line:101
    OOOOOO0O0OOOOOO0O =0 #line:103
    O0000OO0OO0O0O000 =(ps [O0O0OO00OO0OO0OOO ])%6 +1 #line:105
    OOOO0O00OOO0000OO =(ps [O0OO0O000OOO00OOO ])%6 +1 #line:106
    while O0000OO0OO0O0O000 +OOOO0O00OOO0000OO ==7 or O0000OO0OO0O0O000 ==OOOO0O00OOO0000OO :#line:107
        OOOO0O00OOO0000OO +=1 #line:108
        OOOO0O00OOO0000OO =OOOO0O00OOO0000OO %6 +1 #line:109
    if (O00OOO0OOOOOOO00O ):#line:111
        printmd ('**CA** (2%)')#line:112
        print ("Run your program (when you are happy it is working correctly) for a=",O0000OO0OO0O0O000 ," and b=",OOOO0O00OOO0000OO )#line:113
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:114
        return #line:115
    if (waiter ()):#line:117
        while True :#line:118
            try :#line:119
                print ("Enter your program's result for a=",O0000OO0OO0O0O000 ," and b=",OOOO0O00OOO0000OO )#line:120
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:121
                O0O00000O0OO0OO00 =float (input ("Please enter your answer here: "))#line:122
                O0O0000OO00OO0000 =(3 *(O0000OO0OO0O0O000 **3 *OOOO0O00OOO0000OO -O0000OO0OO0O0O000 *OOOO0O00OOO0000OO **3 ))%7 #line:123
                O0OOOOO0000000OOO =np .isclose (O0O00000O0OO0OO00 ,O0O0000OO00OO0000 ,OOOOOO0O0OOOOOO0O )#line:124
                if O0OOOOO0000000OOO :#line:125
                    print ("Well done, right answer is ",O0O0000OO00OO0000 )#line:126
                else :#line:127
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:128
                OOOOO000OO0OO0OO0 =trycount (O00O0O00O00O0O0OO ,O0OOOOO0000000OOO )#line:130
                OOOOO000O00O00OOO =100 -(OOOOO000OO0OO0OO0 [0 ]-1 )*10 #line:131
                if OOOOO000OO0OO0OO0 [1 ]:#line:132
                    print ("First success after ",OOOOO000OO0OO0OO0 [0 ]," tries, you have ",OOOOO000O00O00OOO ,"% on this exercise.")#line:133
                    print ("Enter this code into Brightspace:\n\n",genenc (2 +encoff1 ,OOOOO000O00O00OOO +encoff2 ),'\n')#line:134
                else :#line:135
                    print ("You have had ",OOOOO000OO0OO0OO0 [0 ]," tries.")#line:136
                    print ("If next try is accepted you will achieve ",OOOOO000O00O00OOO -10 ,"% on this exercise.")#line:137
                break #line:139
            except ValueError :#line:141
                print ("I didn't understand that.")#line:142
                continue #line:143
        return #line:145
def a3 (O000000O0OOOOO00O ):#line:154
    global ps #line:156
    O00O000OOO00O00O0 =".a3_counter.npy"#line:159
    O000000OOO000OO0O =np .zeros (1 ,dtype ='int8,bool')#line:160
    OO0OO0OO00O0OOO0O =23 #line:163
    OO0000OO0O0OO0O00 =24 #line:164
    OO0O0O0O0O0OOO00O =(ps [OO0OO0OO00O0OOO0O ])%6 +1 #line:165
    OOOO00O00OO0O0000 =(ps [OO0000OO0O0OO0O00 ])%6 +1 #line:166
    OOO0O00O0O00OOOOO =0 #line:168
    OO0O0O0O0O0OOO00O =10 *OO0O0O0O0O0OOO00O +OOOO00O00OO0O0000 ;#line:170
    if (O000000O0OOOOO00O ):#line:172
        printmd ('**CA** (6%)')#line:173
        print ("Run your program for ",OO0O0O0O0O0OOO00O ,"people")#line:174
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:175
        return #line:176
    if (waiter ()):#line:178
        while True :#line:179
            try :#line:180
                print ("Enter your program's result for",OO0O0O0O0O0OOO00O ,"people")#line:181
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:182
                O0O0O000OO0O0O0OO =float (input ("Please enter your answer here: "))#line:183
                O0O0000OOOOOOO0O0 =OO0O0O0O0O0OOO00O +2 *OO0O0O0O0O0OOO00O +2 *OO0O0O0O0O0OOO00O +10 *OO0O0O0O0O0OOO00O #line:184
                O000O0OO000O000OO =np .isclose (O0O0O000OO0O0O0OO ,O0O0000OOOOOOO0O0 ,OOO0O00O0O00OOOOO )#line:185
                if O000O0OO000O000OO :#line:186
                    print ("Well done, right answer is ",O0O0000OOOOOOO0O0 )#line:187
                else :#line:188
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:189
                O000000OOO000OO0O =trycount (O00O000OOO00O00O0 ,O000O0OO000O000OO )#line:191
                O0000OOOOOO00O0OO =100 -(O000000OOO000OO0O [0 ]-1 )*10 #line:192
                if O000000OOO000OO0O [1 ]:#line:193
                    print ("First success after ",O000000OOO000OO0O [0 ]," tries, you have ",O0000OOOOOO00O0OO ,"% on this exercise.")#line:194
                    print ("Enter this code into Brightspace:\n\n",genenc (3 +encoff1 ,O0000OOOOOO00O0OO +encoff2 ),'\n')#line:195
                else :#line:196
                    print ("You have had ",O000000OOO000OO0O [0 ]," tries.")#line:197
                    print ("If next try is accepted you will achieve ",O0000OOOOOO00O0OO -10 ,"% on this exercise.")#line:198
                break #line:200
            except ValueError :#line:202
                print ("I didn't understand that.")#line:203
                continue #line:204
        return #line:206
def a4 (O000O0OOOO00OOO00 ):#line:217
        import random #line:219
        import requests #line:220
        global ps #line:222
        global wd #line:223
        OOO0O0OOO0O00000O =".a4_counter.npy"#line:226
        O0OO0OOO0O0OO0OO0 =np .zeros (1 ,dtype ='int8,bool')#line:227
        OO0O0O0O0O000000O =60 #line:230
        O0000O0O0OO00O0O0 =61 #line:231
        OOO00OOO0O00O00OO =62 #line:232
        O00OO0O0O0OO000OO =63 #line:233
        OO000OO0O000OOOO0 =64 #line:234
        O0O00O00OO0O0OOOO =0 #line:237
        if (O000O0OOOO00OOO00 ):#line:239
                OO0O0O000O000O0O0 ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:241
                O000000O00O000000 =requests .get (OO0O0O000O000O0O0 )#line:243
                OO0OO00O0O000OO0O =O000000O00O000000 .content .splitlines ()#line:244
                random .seed (10 *ps [62 ]+ps [63 ])#line:245
                O0O00O000O0000000 =4 +(10 *ps [64 ]+ps [65 ])%4 #line:246
                OO00OO00O00000000 =True #line:247
                while OO00OO00O00000000 :#line:248
                        O0O00OOOO0O0O0O00 =OO0OO00O0O000OO0O [random .randint (0 ,len (OO0OO00O0O000OO0O )-1 )].decode ("utf-8")#line:249
                        if len (O0O00OOOO0O0O0O00 )>7 and len (O0O00OOOO0O0O0O00 )<14 and O0O00OOOO0O0O0O00 [0 ].islower ():#line:251
                                OO00OO00O00000000 =False #line:252
                                for O0O00O00OOOO0O000 in O0O00OOOO0O0O0O00 :#line:253
                                        if chr (ord (O0O00O00OOOO0O000 )+O0O00O000O0000000 )>'z':#line:254
                                                OO00OO00O00000000 =True #line:255
                O00OOOO0OOO0OO000 =len (O0O00OOOO0O0O0O00 )#line:257
                OOO0OO0OOOOOO00OO =''#line:258
                for O0000OO0O0OOO000O in range (0 ,O00OOOO0OOO0OO000 ):#line:259
                        OOO0OO0OOOOOO00OO +=chr (ord (O0O00OOOO0O0O0O00 [O0000OO0O0OOO000O ])+O0O00O000O0000000 )#line:261
                print ('Your encoded word is',OOO0OO0OOOOOO00OO )#line:263
                print ('Write your program in the cell below this one.\n')#line:264
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:266
                wd =O0O00OOOO0O0O0O00 #line:267
                return #line:268
        if (waiter ()):#line:270
                while True :#line:271
                        try :#line:272
                                printmd ('**CA** (6%)')#line:273
                                OOOOOO00OOO0OOOOO =str (input ("Enter your DECODED word here: "))#line:274
                                OOO00OO00OOOO0O00 =wd #line:275
                                O00O0000O0OOOO0O0 =OOOOOO00OOO0OOOOO ==OOO00OO00OOOO0O00 #line:276
                                if O00O0000O0OOOO0O0 :#line:277
                                        print ("Well done, right answer is ",OOO00OO00OOOO0O00 )#line:278
                                else :#line:279
                                        print ("Not right yet. Take another look then run this cell again.")#line:280
                                O0OO0OOO0O0OO0OO0 =trycount (OOO0O0OOO0O00000O ,O00O0000O0OOOO0O0 )#line:282
                                OO00OO0OO0OO0000O =100 -(O0OO0OOO0O0OO0OO0 [0 ]-1 )*10 #line:283
                                if O0OO0OOO0O0OO0OO0 [1 ]:#line:284
                                        print ("First success after ",O0OO0OOO0O0OO0OO0 [0 ]," tries, you have ",OO00OO0OO0OO0000O ,"% on this exercise.")#line:285
                                        print ("Enter this code into Brightspace:\n\n",genenc (4 +encoff1 ,OO00OO0OO0OO0000O +encoff2 ),'\n')#line:286
                                else :#line:287
                                        print ("You have had ",O0OO0OOO0O0OO0OO0 [0 ]," tries.")#line:288
                                        print ("If next try is accepted you will achieve ",OO00OO0OO0OO0000O -10 ,"% on this exercise.")#line:289
                                break #line:290
                        except ValueError :#line:292
                                print ("I didn't understand that.")#line:293
                                continue #line:294
                return #line:296
def a5 (O00OOO0O000OOOOOO ):#line:306
        import random #line:308
        import requests #line:309
        global ps #line:311
        global P0 #line:312
        O00O0OO0O0OOO00O0 =".a5_counter.npy"#line:316
        OOO000000O0O000O0 =np .zeros (1 ,dtype ='int8,bool')#line:317
        O00O0OOOOO000O0OO =70 #line:320
        OOOO0OO00OOOOO00O =71 #line:321
        O0O00OO00OO0OOOO0 =72 #line:322
        O00O0O0O0OO0O0O00 =73 #line:323
        OO0OOOO0OOO00O0OO =74 #line:324
        O0OO000OOOOO00O0O =0 #line:327
        if (O00OOO0O000OOOOOO ):#line:329
                P0 =[]#line:330
                O000000O00O0000O0 =7 +(10 *ps [O00O0OOOOO000O0OO ]+ps [OOOO0OO00OOOOO00O ])%4 #line:331
                for O0O0O00000O0O000O in range (O000000O00O0000O0 ):#line:332
                        P0 .append (max (0 ,ps [O0O00OO00OO0OOOO0 +O0O0O00000O0O000O ]-1 ))#line:333
                print ('Run your program for the list below:\n',P0 )#line:334
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:336
        elif (waiter ()):#line:338
                while True :#line:339
                        try :#line:340
                                printmd ('**CA** (6%)')#line:343
                                O00O00O0000OOOOO0 =eval (input ("Enter your list here: "))#line:344
                                O0O0000O0O00OO00O =3 #line:349
                                O00O0O00000O00O0O =P0 .copy ()#line:350
                                O00O0O00000O00O0O .append (0 )#line:351
                                print (O00O0O00000O00O0O )#line:352
                                O000000O00O0000O0 =len (P0 )#line:353
                                for OOOOOOOOO00OO000O in range (O0O0000O0O00OO00O ):#line:354
                                        for O0O0O00000O0O000O in range (O000000O00O0000O0 ):#line:355
                                                O00O0O00000O00O0O [O0O0O00000O0O000O ]=O00O0O00000O00O0O [O0O0O00000O0O000O +1 ]*(O0O0O00000O0O000O +1 )#line:357
                                O00O0O00000O00O0O .pop ()#line:358
                                OO00OOOOO0OO0OOOO =O00O0O00000O00O0O #line:361
                                if not type (O00O00O0000OOOOO0 )==type (OO00OOOOO0OO0OOOO ):#line:363
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:364
                                elif not len (O00O00O0000OOOOO0 )==len (OO00OOOOO0OO0OOOO ):#line:365
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:366
                                else :#line:367
                                        OOO0O0O0000000OOO =O00O00O0000OOOOO0 ==OO00OOOOO0OO0OOOO #line:368
                                        if OOO0O0O0000000OOO :#line:369
                                                print ("Well done, right answer is ",OO00OOOOO0OO0OOOO )#line:370
                                        else :#line:371
                                                print ("Not right yet. Take another look then run this cell again.")#line:372
                                        OOO000000O0O000O0 =trycount (O00O0OO0O0OOO00O0 ,OOO0O0O0000000OOO )#line:374
                                        O0OO0O0O00OO000OO =100 -(OOO000000O0O000O0 [0 ]-1 )*10 #line:375
                                        if OOO000000O0O000O0 [1 ]:#line:376
                                                print ("First success after ",OOO000000O0O000O0 [0 ]," tries, you have ",O0OO0O0O00OO000OO ,"% on this exercise.")#line:377
                                                print ("Enter this code into Brightspace:\n\n",genenc (5 +encoff1 ,O0OO0O0O00OO000OO +encoff2 ),'\n')#line:378
                                        else :#line:379
                                                print ("You have had ",OOO000000O0O000O0 [0 ]," tries.")#line:380
                                                print ("If next try is accepted you will achieve ",O0OO0O0O00OO000OO -10 ,"% on this exercise.")#line:381
                                        break #line:382
                                O00O0O00000O00O0O =None #line:385
                                OO00OOOOO0OO0OOOO =None #line:386
                        except ValueError :#line:387
                                print ("I didn't understand that.")#line:388
                                continue #line:389
        return #line:391
def a6 (OOO0OOO000OOOO00O ):#line:400
        import random #line:402
        import requests #line:403
        global ps #line:405
        global P0 #line:406
        OO0OOOOO0000OOOOO =".a6_counter.npy"#line:410
        O000OOOO0OOOOOOO0 =np .zeros (1 ,dtype ='int8,bool')#line:411
        OOOOO000O0O00OOO0 =11 #line:414
        OOOOOO00OO0O00O0O =16 #line:415
        O0OO00OOO00O0OOO0 =7 #line:416
        OOO0OOOOO00OOO000 =33 #line:417
        O0OOOO00O00OO0OO0 =21 #line:418
        O0OOOOO0OO0OOOO0O =0 #line:421
        if (OOO0OOO000OOOO00O ):#line:423
                OOO0O0O0000OO00O0 =ps [OOOOO000O0O00OOO0 ]+ps [OOOOOO00OO0O00O0O ]+ps [O0OO00OOO00O0OOO0 ]+ps [OOO0OOOOO00OOO000 ]+ps [O0OOOO00O00OO0OO0 ]#line:424
                random .seed (OOO0O0O0000OO00O0 )#line:425
                P0 =random .randint (1000 ,2000 )#line:426
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:427
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:429
        elif (waiter ()):#line:431
                while True :#line:432
                        try :#line:433
                                printmd ('**CA** (6%)')#line:436
                                OO0000OOOO00O0O0O =eval (input ("Enter your stopping number here: "))#line:437
                                OO0O0OO0O00O0OOO0 =P0 #line:441
                                OOO000OO0OO0O00O0 =[OO0O0OO0O00O0OOO0 ]#line:442
                                while not OO0O0OO0O00O0OOO0 ==1 :#line:443
                                        if OO0O0OO0O00O0OOO0 %2 :#line:444
                                                OO0O0OO0O00O0OOO0 =3 *OO0O0OO0O00O0OOO0 +1 #line:445
                                        else :#line:446
                                                OO0O0OO0O00O0OOO0 =OO0O0OO0O00O0OOO0 //2 #line:447
                                        OOO000OO0OO0O00O0 .append (OO0O0OO0O00O0OOO0 )#line:448
                                O0O0OO000OO000000 =len (OOO000OO0OO0O00O0 )#line:449
                                O00000OO0O0OO0O0O =O0O0OO000OO000000 #line:453
                                if not type (OO0000OOOO00O0O0O )==type (O00000OO0O0OO0O0O ):#line:455
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:456
                                else :#line:459
                                        O0OO0O00OO00O000O =OO0000OOOO00O0O0O ==O00000OO0O0OO0O0O #line:460
                                        if O0OO0O00OO00O000O :#line:461
                                                print ("Well done, right answer is ",O00000OO0O0OO0O0O )#line:462
                                        else :#line:463
                                                print ("Not right yet. Take another look then run this cell again.")#line:464
                                        O000OOOO0OOOOOOO0 =trycount (OO0OOOOO0000OOOOO ,O0OO0O00OO00O000O )#line:466
                                        OOO0O0OOO00OO000O =100 -(O000OOOO0OOOOOOO0 [0 ]-1 )*10 #line:467
                                        if O000OOOO0OOOOOOO0 [1 ]:#line:468
                                                print ("First success after ",O000OOOO0OOOOOOO0 [0 ]," tries, you have ",OOO0O0OOO00OO000O ,"% on this exercise.")#line:469
                                                print ("Enter this code into Brightspace:\n\n",genenc (6 +encoff1 ,OOO0O0OOO00OO000O +encoff2 ),'\n')#line:470
                                        else :#line:471
                                                print ("You have had ",O000OOOO0OOOOOOO0 [0 ]," tries.")#line:472
                                                print ("If next try is accepted you will achieve ",OOO0O0OOO00OO000O -10 ,"% on this exercise.")#line:473
                                        break #line:474
                                O0O0OO000OO000000 =None #line:477
                                O00000OO0O0OO0O0O =None #line:478
                        except ValueError :#line:479
                                print ("I didn't understand that.")#line:480
                                continue #line:481
        return #line:483
def a7 (OO00O00OO00O00O0O ):#line:493
        OOOOOO0OO0O0O0000 =".a7_counter.npy"#line:497
        OO0O000OO0OO000OO =np .zeros (1 ,dtype ='int8,bool')#line:498
        def OO000OOO00OO0O0O0 ():#line:500
                pass #line:501
        O0000000O00000OOO =[(30 ,10 )]#line:504
        O000OOO0000OOO0O0 =1.0e-4 #line:507
        if (waiter ()):#line:510
                printmd ('**CA** (6%)')#line:512
                if not type (OO00O00OO00O00O0O )==type (OO000OOO00OO0O0O0 ):#line:514
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:515
                else :#line:518
                        def O00OOO0O00O000OO0 (O00OO00OO00OOO0OO ,O000000000OO0OO00 ):#line:521
                                import math #line:522
                                OOO0OOOOOOOOO0O0O =9.81 #line:523
                                O0O0OO0OOO000000O =math .pi *O000000000OO0OO00 /180. #line:524
                                O00O0O0O0OO00OOO0 =O00OO00OO00OOO0OO **2 *math .sin (2 *O0O0OO0OOO000000O )/OOO0OOOOOOOOO0O0O #line:525
                                O0OO0OO0OO00O00O0 =O00OO00OO00OOO0OO **2 *(math .sin (O0O0OO0OOO000000O ))**2 /(2. *OOO0OOOOOOOOO0O0O )#line:526
                                return O00O0O0O0OO00OOO0 ,O0OO0OO0OO00O00O0 #line:527
                        import random as r #line:530
                        O0000000O00000OOO =[]#line:531
                        OO0000O0OOO00OO0O =False #line:532
                        O00OO0OOOO0O00O00 =[]#line:533
                        O000O000000OO00O0 =10 #line:534
                        O00O0O00O0OO0OO0O =100 #line:535
                        OOOOOO0OOO0OO0000 =5 #line:536
                        OO0O0OO0OO0O0O0OO =85 #line:537
                        for O0O00OOO00O00OO00 in range (5 ):#line:538
                                O0000000O00000OOO .append ((r .uniform (O000O000000OO00O0 ,O00O0O00O0OO0OO0O ),r .uniform (OOOOOO0OOO0OO0000 ,OO0O0OO0OO0O0O0OO )))#line:539
                        for (O0O00O0000O000OO0 ,OOO000000OO00000O )in O0000000O00000OOO :#line:540
                                print ('Testing:',O0O00O0000O000OO0 ,OOO000000OO00000O )#line:541
                                OOO00OOO00O0OO0OO =OO00O00OO00O00O0O (O0O00O0000O000OO0 ,OOO000000OO00000O )#line:542
                                print ('Output:',*OOO00OOO00O0OO0OO )#line:543
                                OOO0O0O000OOOO000 =O00OOO0O00O000OO0 (O0O00O0000O000OO0 ,OOO000000OO00000O )#line:544
                                print ('Actual:',*OOO0O0O000OOOO000 )#line:545
                                print ()#line:546
                                if (not type (OOO00OOO00O0OO0OO )==type (OOO0O0O000OOOO000 ))or (not len (OOO00OOO00O0OO0OO )==len (OOO0O0O000OOOO000 )):#line:547
                                        if OO0000O0OOO00OO0O ==False :#line:548
                                           OO0000O0OOO00OO0O =True #line:549
                                else :#line:550
                                        O00OO0OOOO0O00O00 .append (all (np .isclose (OOO00OOO00O0OO0OO ,OOO0O0O000OOOO000 ,O000OOO0000OOO0O0 )))#line:551
                        if OO0000O0OOO00OO0O :#line:553
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:554
                        else :#line:556
                                OOOO00000OO0O00O0 =all (O00OO0OOOO0O00O00 )#line:557
                                if OOOO00000OO0O00O0 :#line:558
                                        print ("Well done, all correct.")#line:559
                                else :#line:560
                                        print ("Not right yet. Take another look then run this cell again.")#line:561
                                OO0O000OO0OO000OO =trycount (OOOOOO0OO0O0O0000 ,OOOO00000OO0O00O0 )#line:563
                                O0000O00O00O000O0 =100 -(OO0O000OO0OO000OO [0 ]-1 )*10 #line:564
                                if OO0O000OO0OO000OO [1 ]:#line:565
                                        print ("First success after ",OO0O000OO0OO000OO [0 ]," tries, you have ",O0000O00O00O000O0 ,"% on this exercise.")#line:566
                                        print ("Enter this code into Brightspace:\n\n",genenc (7 +encoff1 ,O0000O00O00O000O0 +encoff2 ),'\n')#line:567
                                else :#line:568
                                        print ("You have had ",OO0O000OO0OO000OO [0 ]," tries.")#line:569
                                        print ("If next try is accepted you will achieve ",O0000O00O00O000O0 -10 ,"% on this exercise.")#line:570
                        OOO0O0O000OOOO000 =None #line:573
                        O00OOO0O00O000OO0 =None #line:574
        return #line:576
def a8 (OO0O00O0OOO000O00 ):#line:586
        O0O00000O00OO00OO =".a8_counter.npy"#line:590
        OO000OOO0O00O0000 =np .zeros (1 ,dtype ='int8,bool')#line:591
        def O00OOO00O0000O00O ():#line:593
                pass #line:594
        O0OO0O00O00OOO0O0 =1.0e-4 #line:598
        if (waiter ()):#line:601
                printmd ('**CA** (6%)')#line:603
                if not type (OO0O00O0OOO000O00 )==type (O00OOO00O0000O00O ):#line:607
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:608
                else :#line:612
                        import inspect #line:615
                        O00O00O00O0OOO00O =inspect .getsourcelines (OO0O00O0OOO000O00 )#line:616
                        O0O0000OOO0000OOO =True #line:617
                        OO0O0O0000000O0OO =[]#line:618
                        for OO0OO0OO00OOO0000 ,OO000O000OOO0OOOO in enumerate (O00O00O00O0OOO00O [0 ]):#line:619
                                if 'for'in OO000O000OOO0OOOO or 'while'in OO000O000OOO0OOOO :#line:620
                                        O0O0000OOO0000OOO =False #line:622
                                        OO0O0O0000000O0OO .append (OO0OO0OO00OOO0000 )#line:623
                        if not O0O0000OOO0000OOO :#line:624
                                print ('Function needs to be written without loops (using NumPy), check lines',*OO0O0O0000000O0OO )#line:625
                                print ('No marks lost for this attempt.')#line:626
                                return #line:627
                        def OO00OOOOO0O000OOO (OOOOO0O0OO0OOOOOO ):#line:630
                                O00OOOO0O00000OOO =np .vstack ((OOOOO0O0OO0OOOOOO ,OOOOO0O0OO0OOOOOO [0 ]))#line:631
                                O0O0O00OOOO0OO0O0 =sum (O00OOOO0O00000OOO [:-1 ,0 ]*O00OOOO0O00000OOO [1 :,1 ])#line:632
                                OO0OOO0OOO00O0O0O =sum (O00OOOO0O00000OOO [:-1 ,1 ]*O00OOOO0O00000OOO [1 :,0 ])#line:633
                                return abs (O0O0O00OOOO0OO0O0 -OO0OOO0OOO00O0O0O )/2 #line:634
                        import random as r #line:637
                        O0O00OOOOO0O0O000 =r .randint (6 ,11 )#line:638
                        OOOO000000OO00O00 =np .ones ((O0O00OOOOO0O0O000 ,2 ))#line:639
                        O0OOO0OOOO00O000O =False #line:640
                        OOOO0OO0000O00OOO =[]#line:641
                        OOO0O0OO0O000O0OO =1. #line:642
                        OOO0000O00O00O000 =20. #line:643
                        O0OOOO0OO00O0OO00 =OOO0O0OO0O000O0OO #line:644
                        O00OOO0O0000O0OO0 =OOO0000O00O00O000 #line:645
                        for O0O0OOOOO0O00OO00 in range (O0O00OOOOO0O0O000 ):#line:646
                                OOOO000000OO00O00 [O0O0OOOOO0O00OO00 ]=[r .uniform (OOO0O0OO0O000O0OO ,OOO0000O00O00O000 ),r .uniform (O0OOOO0OO00O0OO00 ,O00OOO0O0000O0OO0 )]#line:647
                        print ('Testing:',OOOO000000OO00O00 )#line:648
                        O000OOO0OOO0OOOOO =OO0O00O0OOO000O00 (OOOO000000OO00O00 )#line:649
                        print ('Output:',O000OOO0OOO0OOOOO )#line:650
                        OO0O0OOO0000OOOO0 =OO00OOOOO0O000OOO (OOOO000000OO00O00 )#line:651
                        print ('Actual:',OO0O0OOO0000OOOO0 )#line:652
                        print ()#line:653
                        if not type (O000OOO0OOO0OOOOO )==type (OO0O0OOO0000OOOO0 ):#line:654
                                if O0OOO0OOOO00O000O ==False :#line:655
                                        O0OOO0OOOO00O000O =True #line:656
                        else :#line:657
                                OOOO0OO0000O00OOO .append (np .isclose (O000OOO0OOO0OOOOO ,OO0O0OOO0000OOOO0 ,O0OO0O00O00OOO0O0 ))#line:658
                        if O0OOO0OOOO00O000O :#line:660
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:661
                        else :#line:663
                                OO0OO00O0OO0OOOOO =all (OOOO0OO0000O00OOO )#line:664
                                if OO0OO00O0OO0OOOOO :#line:665
                                        print ("Well done, all correct.")#line:666
                                else :#line:667
                                        print ("Not right yet. Take another look then run this cell again.")#line:668
                                OO000OOO0O00O0000 =trycount (O0O00000O00OO00OO ,OO0OO00O0OO0OOOOO )#line:670
                                O0OO0000OOOOO0O00 =100 -(OO000OOO0O00O0000 [0 ]-1 )*10 #line:671
                                if OO000OOO0O00O0000 [1 ]:#line:672
                                        print ("First success after ",OO000OOO0O00O0000 [0 ]," tries, you have ",O0OO0000OOOOO0O00 ,"% on this exercise.")#line:673
                                        print ("Enter this code into Brightspace:\n\n",genenc (8 +encoff1 ,O0OO0000OOOOO0O00 +encoff2 ),'\n')#line:674
                                else :#line:675
                                        print ("You have had ",OO000OOO0O00O0000 [0 ]," tries.")#line:676
                                        print ("If next try is accepted you will achieve ",O0OO0000OOOOO0O00 -10 ,"% on this exercise.")#line:677
                        OO0O0OOO0000OOOO0 =None #line:680
                        OO00OOOOO0O000OOO =None #line:681
        return #line:683
def a1_notlive ():#line:699
        print ('This CA test is not currently live.')#line:700
        return #line:701
def a2_notlive (OOOO0O0OO0O0OOO0O ):#line:709
        print ('This CA test is not currently live.')#line:710
        return #line:711
def a3_notlive (OOO0OO00OOO0OO00O ):#line:719
        print ('This CA test is not currently live.')#line:720
        return #line:721
def a4_notlive (O00OO000O000O0000 ):#line:729
        print ('This CA test is not currently live.')#line:730
        return #line:731
def a5_notlive (OOO000OO0O00O0OO0 ):#line:739
        print ('This CA test is not currently live.')#line:740
        return #line:741
def a6_notlive (O0000OOO00OO0OO0O ):#line:749
        print ('This CA test is not currently live.')#line:750
        return #line:751
def a7_notlive ():#line:759
        print ('This CA test is not currently live.')#line:760
        return #line:761
def a8_notlive (OOO0O00OOOO0O00OO ):#line:769
        print ('This CA test is not currently live.')#line:770
        return #line:771
def b1 ():#line:789
    global ps #line:791
    OO0OOOOOO0O0O0000 =".b1_counter.npy"#line:794
    OOOOO00O0O0OO0O0O =np .zeros (1 ,dtype ='int8,bool')#line:795
    OOOO0OOOOOO000O00 =0.05 #line:797
    if (waiter ()):#line:799
        while True :#line:800
            try :#line:801
                printmd ('**CA**')#line:802
                OOO0OOO0O000OO0O0 =eval (input ("Please enter your answer here in the format D,k: "))#line:803
                O0OOOOO000OOO0OO0 =(0.025 ,2.0 )#line:804
                OO0000O0O0OO000O0 =all (np .isclose (OOO0OOO0O000OO0O0 ,O0OOOOO000OOO0OO0 ,rtol =OOOO0OOOOOO000O00 ))#line:805
                if OO0000O0O0OO000O0 :#line:806
                    print ("Well done, reasonable estimate is ",O0OOOOO000OOO0OO0 )#line:807
                else :#line:808
                    print ("Not right yet. Take another look then run this cell again.")#line:809
                OOOOO00O0O0OO0O0O =trycount (OO0OOOOOO0O0O0000 ,OO0000O0O0OO000O0 )#line:811
                O00000OOO000O00O0 =100 -(OOOOO00O0O0OO0O0O [0 ]-1 )*10 #line:812
                if OOOOO00O0O0OO0O0O [1 ]:#line:813
                    print ("First success after ",OOOOO00O0O0OO0O0O [0 ]," tries, you have ",O00000OOO000O00O0 ,"% on this exercise.")#line:814
                    print ("Enter this code into Brightspace:\n\n",genenc (1 +encoff1 ,O00000OOO000O00O0 +encoff2 ),'\n')#line:815
                else :#line:816
                    print ("You have had ",OOOOO00O0O0OO0O0O [0 ]," tries.")#line:817
                    print ("If next try is accepted you will achieve ",O00000OOO000O00O0 -10 ,"% on this exercise.")#line:818
                break #line:820
            except ValueError :#line:822
                print ("I didn't understand that.")#line:823
                continue #line:824
        return #line:826
def b2 (OOO0O0OO0000OOO00 ):#line:836
        O00OOO00OO00O0O0O =".b2_counter.npy"#line:840
        OOOO0OOO0OO0O0OO0 =np .zeros (1 ,dtype ='int8,bool')#line:841
        def OOO00O0O0O0OOOO0O ():#line:843
                pass #line:844
        O00OO0O0OO0OOOOO0 =1.0e-2 #line:847
        OO00OOOOOOOO0O0O0 =0.0 #line:848
        if (waiter ()):#line:850
                printmd ('**CA**')#line:852
                if not type (OOO0O0OO0000OOO00 )==type (OOO00O0O0O0OOOO0O ):#line:854
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:855
                else :#line:858
                        def OO00O000OO000O0O0 (O00OO000OO00OO0O0 ):#line:862
                                OOO00OOOOO00O0OO0 =[]#line:863
                                O00O00O0000OOO0O0 =20.0 #line:864
                                O0O00O0000OOO0000 =58.1e-3 #line:865
                                OOOO0O00OOOO00OOO =9.81 #line:866
                                O0O0000O0OOO00OOO =0.0 #line:867
                                OOO0000000OO0OOO0 =0.0 #line:868
                                OO0OOOO00OOO0OO0O =0.0 #line:869
                                OO000OOOO0O00000O =10 #line:870
                                O00O0OOO0O00O0O0O =3.35e-2 #line:871
                                OOO00O00OOO0O0OO0 =0.51 #line:872
                                O0OOOO00OOOO00O00 =1.25 #line:873
                                OOO0O000OOOOO0O0O =math .pi *O00O0OOO0O00O0O0O **2 #line:874
                                OOOO000O00O00O0O0 =0.5 *OOO00O00OOO0O0OO0 *OOO0O000OOOOO0O0O *O0OOOO00OOOO00O00 #line:875
                                OOOOO000000OO00OO =100000 #line:877
                                OO0O0O00O00OO0O0O =np .zeros (OOOOO000000OO00OO ,float )#line:878
                                O00OO0O000O00O0O0 =np .zeros (OOOOO000000OO00OO ,float )#line:879
                                O0OO0OOO0O0O00OO0 =np .zeros (OOOOO000000OO00OO ,float )#line:880
                                O00O00OO00O00OO0O =np .zeros (OOOOO000000OO00OO ,float )#line:881
                                O0O0000O000O0OO00 =np .zeros (OOOOO000000OO00OO ,float )#line:882
                                O0OOO0000O000OO00 =np .zeros (OOOOO000000OO00OO ,float )#line:883
                                O0OO00OO0O000O0O0 =np .zeros (OOOOO000000OO00OO ,float )#line:884
                                OO0O0O00O00OO0O0O ,O0O0000O0O0OO0O0O =np .linspace (OO0OOOO00OOO0OO0O ,OO000OOOO0O00000O ,OOOOO000000OO00OO ,retstep =True )#line:885
                                for OO0O0O0O0OO000O00 in O00OO000OO00OO0O0 :#line:887
                                        OOOOO0000O0OOO00O =O00O00O0000OOO0O0 *math .cos (OO0O0O0O0OO000O00 )#line:888
                                        OOOO000O000OO0OOO =O00O00O0000OOO0O0 *math .sin (OO0O0O0O0OO000O00 )#line:889
                                        O0OOO0000O000OO00 [0 ]=O0O0000O0OOO00OOO #line:891
                                        O0OO00OO0O000O0O0 [0 ]=OOO0000000OO0OOO0 #line:892
                                        O00O00OO00O00OO0O [0 ]=OOOOO0000O0OOO00O #line:893
                                        O0O0000O000O0OO00 [0 ]=OOOO000O000OO0OOO #line:894
                                        for OO000O000000O000O in range (OOOOO000000OO00OO -1 ):#line:895
                                                O0O000OO0OOO00OO0 =math .sqrt (O00O00OO00O00OO0O [OO000O000000O000O ]**2 +O0O0000O000O0OO00 [OO000O000000O000O ]**2 )#line:896
                                                O000O00O0000OO000 =-OOOO000O00O00O0O0 *O0O000OO0OOO00OO0 *O00O00OO00O00OO0O [OO000O000000O000O ]#line:897
                                                O00OO0O000O00O0O0 [OO000O000000O000O ]=O000O00O0000OO000 /O0O00O0000OOO0000 #line:898
                                                O00O00OO00O00OO0O [OO000O000000O000O +1 ]=O00O00OO00O00OO0O [OO000O000000O000O ]+O00OO0O000O00O0O0 [OO000O000000O000O ]*O0O0000O0O0OO0O0O #line:899
                                                O0OOO0000O000OO00 [OO000O000000O000O +1 ]=O0OOO0000O000OO00 [OO000O000000O000O ]+O00O00OO00O00OO0O [OO000O000000O000O +1 ]*O0O0000O0O0OO0O0O #line:900
                                                O0OO0OO0O0O00O0O0 =-O0O00O0000OOO0000 *OOOO0O00OOOO00OOO -OOOO000O00O00O0O0 *O0O000OO0OOO00OO0 *O0O0000O000O0OO00 [OO000O000000O000O ]#line:901
                                                O0OO0OOO0O0O00OO0 [OO000O000000O000O ]=O0OO0OO0O0O00O0O0 /O0O00O0000OOO0000 #line:902
                                                O0O0000O000O0OO00 [OO000O000000O000O +1 ]=O0O0000O000O0OO00 [OO000O000000O000O ]+O0OO0OOO0O0O00OO0 [OO000O000000O000O ]*O0O0000O0O0OO0O0O #line:903
                                                O0OO00OO0O000O0O0 [OO000O000000O000O +1 ]=O0OO00OO0O000O0O0 [OO000O000000O000O ]+O0O0000O000O0OO00 [OO000O000000O000O +1 ]*O0O0000O0O0OO0O0O #line:904
                                                if (O0OO00OO0O000O0O0 [OO000O000000O000O +1 ]<0 ):#line:905
                                                        break #line:906
                                        O000OOO0O0OO00OO0 =OO000O000000O000O #line:907
                                        OOO00OOOOO00O0OO0 .append (O0OOO0000O000OO00 [O000OOO0O0OO00OO0 ])#line:908
                                return (OOO00OOOOO00O0OO0 );#line:910
                        import random as r #line:913
                        O0OO00000O00O0OO0 =[]#line:914
                        OOO000OO0O0OOOOO0 =False #line:915
                        O0O0OOO000000OO0O =[]#line:916
                        OO0000OO0O0OO0O0O =0.1 #line:917
                        O0000OO00O00OO0O0 =1.5 #line:918
                        for OO0O0OOOOO0O000O0 in range (5 ):#line:919
                                O0OO00000O00O0OO0 .append (r .uniform (OO0000OO0O0OO0O0O ,O0000OO00O00OO0O0 ))#line:920
                        O0OO00000O00O0OO0 .sort ()#line:921
                        print ('Testing thetas=',O0OO00000O00O0OO0 )#line:922
                        O0OOOOOO000O00000 =OOO0O0OO0000OOO00 (O0OO00000O00O0OO0 )#line:923
                        print ('Output ximpacts=',O0OOOOOO000O00000 )#line:924
                        O0O00OO0OO00OOOOO =OO00O000OO000O0O0 (O0OO00000O00O0OO0 )#line:925
                        print ('Actual ximpacts=',O0O00OO0OO00OOOOO )#line:926
                        print ()#line:927
                        if (not type (O0OOOOOO000O00000 )==type (O0O00OO0OO00OOOOO ))or (not len (O0OOOOOO000O00000 )==len (O0O00OO0OO00OOOOO )):#line:928
                                if OOO000OO0O0OOOOO0 ==False :#line:929
                                        OOO000OO0O0OOOOO0 =True #line:930
                        else :#line:931
                                O0O0OOO000000OO0O .append (all (np .isclose (O0OOOOOO000O00000 ,O0O00OO0OO00OOOOO ,rtol =O00OO0O0OO0OOOOO0 ,atol =OO00OOOOOOOO0O0O0 )))#line:932
                        if OOO000OO0O0OOOOO0 :#line:934
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:935
                        else :#line:937
                                O0O0O000O00OOOO00 =all (O0O0OOO000000OO0O )#line:938
                                if O0O0O000O00OOOO00 :#line:939
                                        print ("Well done, all correct.")#line:940
                                else :#line:941
                                        print ("Not close enough. Take another look then run this cell again.")#line:942
                                OOOO0OOO0OO0O0OO0 =trycount (O00OOO00OO00O0O0O ,O0O0O000O00OOOO00 )#line:944
                                O00OOO0O00OOO0O00 =100 -(OOOO0OOO0OO0O0OO0 [0 ]-1 )*10 #line:945
                                if OOOO0OOO0OO0O0OO0 [1 ]:#line:946
                                        print ("First success after ",OOOO0OOO0OO0O0OO0 [0 ]," tries, you have ",O00OOO0O00OOO0O00 ,"% on this exercise.")#line:947
                                        print ("Enter this code into Brightspace:\n\n",genenc (2 +encoff1 ,O00OOO0O00OOO0O00 +encoff2 ),'\n')#line:948
                                else :#line:949
                                        print ("You have had ",OOOO0OOO0OO0O0OO0 [0 ]," tries.")#line:950
                                        print ("If next try is accepted you will achieve ",O00OOO0O00OOO0O00 -10 ,"% on this exercise.")#line:951
                        O0O00OO0OO00OOOOO =None #line:954
                        OO00O000OO000O0O0 =None #line:955
        return #line:957
def b3 ():#line:967
    global ps #line:969
    OOO0OO0O00O00000O =".b3_counter.npy"#line:972
    OO00000O00OO00OO0 =np .zeros (1 ,dtype ='int8,bool')#line:973
    O0O0O0O0O0OO00000 =0.01 #line:976
    if (waiter ()):#line:978
        while True :#line:979
            try :#line:980
                printmd ('**CA**')#line:981
                OOOO0O000000O0O0O =float (input ("Enter a real number here: "))#line:982
                O0OOO0O000O000O00 =0.5 #line:983
                OO00OO0O0OO0O00OO =np .isclose (OOOO0O000000O0O0O ,O0OOO0O000O000O00 ,atol =O0O0O0O0O0OO00000 )#line:984
                if OO00OO0O0OO0O00OO :#line:985
                    print ("Well done. Actual value is ",O0OOO0O000O000O00 )#line:986
                else :#line:987
                    print ("Not right yet. Take another look then run this cell again.")#line:988
                OO00000O00OO00OO0 =trycount (OOO0OO0O00O00000O ,OO00OO0O0OO0O00OO )#line:990
                OOOOOO000000O00O0 =100 -(OO00000O00OO00OO0 [0 ]-1 )*10 #line:991
                if OO00000O00OO00OO0 [1 ]:#line:992
                    print ("First success after ",OO00000O00OO00OO0 [0 ]," tries, you have ",OOOOOO000000O00O0 ,"% on this exercise.")#line:993
                    print ("Enter this code into Brightspace:\n\n",genenc (3 +encoff1 ,OOOOOO000000O00O0 +encoff2 ),'\n')#line:994
                else :#line:995
                    print ("You have had ",OO00000O00OO00OO0 [0 ]," tries.")#line:996
                    print ("If next try is accepted you will achieve ",OOOOOO000000O00O0 -10 ,"% on this exercise.")#line:997
                break #line:999
            except ValueError :#line:1001
                print ("I didn't understand that.")#line:1002
                continue #line:1003
        return #line:1005
def b1_notlive ():#line:1017
        print ('This CA test is not currently live.')#line:1018
        return #line:1019
def b2_notlive (O00O0OOO00O0OO00O ):#line:1029
        print ('This CA test is not currently live.')#line:1030
        return #line:1031
def b3_notlive ():#line:1038
        print ('This CA test is not currently live.')#line:1039
        return #line:1040
def printmd (OOOOOOO00000OOOOO ):#line:1050
    display (Markdown (OOOOOOO00000OOOOO ))#line:1051
def repeat_to_length (OOOOOO0OOO0000OOO ,O00OO00O00O000OOO ):#line:1053
   return (OOOOOO0OOO0000OOO *((O00OO00O00O000OOO //len (OOOOOO0OOO0000OOO ))+1 ))[:O00OO00O00O000OOO ]#line:1054
def getco (OOO00O00OOO0O0OOO ):#line:1056
    global ps #line:1057
    OOOO00000000O0O00 =getpass .getuser ()#line:1058
    OO0OOOOOOOOO0O000 =int .from_bytes (OOOO00000000O0O00 .encode (),'little')#line:1059
    O00O00O00OO00OO00 =str (OO0OOOOOOOOO0O000 )#line:1060
    O0OOOOO00000O0O00 =repeat_to_length (O00O00O00OO00OO00 ,OOO00O00OOO0O0OOO )#line:1061
    ps =[int (O0OOOOO0OO000OOO0 )+1 for O0OOOOO0OO000OOO0 in O0OOOOO00000O0O00 ]#line:1062
def waiter ():#line:1065
    OO0000OO00OOOO0O0 =20 #line:1068
    O0O0OO0O0O0OO000O =".ts1.txt"#line:1070
    if os .path .isfile (O0O0OO0O0O0OO000O ):#line:1071
        O000O0OO0O000O0O0 =np .loadtxt (O0O0OO0O0O0OO000O )#line:1072
    else :#line:1074
        O000O0OO0O000O0O0 =0.0 #line:1075
    OOOO0OO00OOO0OO00 =time .time ()#line:1078
    OOOO0O0O0O00O000O =OOOO0OO00OOO0OO00 -O000O0OO0O000O0O0 #line:1079
    if (OOOO0O0O0O00O000O <OO0000OO00OOOO0O0 ):#line:1081
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(OOOO0O0O0O00O000O ,OO0000OO00OOOO0O0 ))#line:1082
        return False #line:1083
    else :#line:1084
        O00OO000OO0000O00 =open (O0O0OO0O0O0OO000O ,'w')#line:1085
        O00OO000OO0000O00 .write (str (OOOO0OO00OOO0OO00 ))#line:1086
        O00OO000OO0000O00 .close ()#line:1087
        return True #line:1088
def trycount (OOOO00000OOO00OO0 ,O0O0OO0O0O00OO000 ):#line:1090
    if os .path .isfile (OOOO00000OOO00OO0 ):#line:1092
        OOO0OO00OOO00000O =np .load (OOOO00000OOO00OO0 )#line:1093
    else :#line:1095
        OOO0OO00OOO00000O =np .zeros (1 ,dtype ='int8,bool')#line:1096
        OOO0OO00OOO00000O =[0 ,False ]#line:1097
    if not OOO0OO00OOO00000O [1 ]:#line:1100
        OOO0OO00OOO00000O [0 ]+=1 #line:1101
        OOO0OO00OOO00000O [1 ]=O0O0OO0O0O00OO000 #line:1102
        np .save (OOOO00000OOO00OO0 ,OOO0OO00OOO00000O )#line:1104
    return OOO0OO00OOO00000O #line:1106
def valdho (OO0O00O0O000OOO0O ,OO0O0O0O0O00O00O0 ):#line:1114
    O00O000O000OOO0OO =".dho_counter.npy"#line:1118
    OO0000OOO00OOOOOO =np .zeros (1 ,dtype ='int8,bool')#line:1120
    if (waiter ()):#line:1122
        while True :#line:1123
            try :#line:1124
                O0000OOO0O000OO00 =float (input ("Please enter your estimate here: "))#line:1125
                OO0O0O0OO0OO0O00O =2 *np .sqrt (OO0O00O0O000OOO0O *OO0O0O0O0O00O00O0 )#line:1126
                OOO0O0OOO0OO0OO0O =np .isclose (O0000OOO0O000OO00 ,OO0O0O0OO0OO0O00O ,0.2 )#line:1127
                if OOO0O0OOO0OO0OO0O :#line:1128
                    print ("Well done, that is close to the critical damping value ",OO0O0O0OO0OO0O00O )#line:1129
                else :#line:1130
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1131
                OO0000OOO00OOOOOO =trycount (O00O000O000OOO0OO ,OOO0O0OOO0OO0OO0O )#line:1133
                O00O000O00000OO0O =100 -(OO0000OOO00OOOOOO [0 ]-1 )*10 #line:1134
                if OO0000OOO00OOOOOO [1 ]:#line:1135
                    print ("First success after ",OO0000OOO00OOOOOO [0 ]," tries, you have ",O00O000O00000OO0O ,"% on this exercise.")#line:1136
                    print ("Enter this code into Brightspace:\n\n",genenc (4 +encoff1 ,O00O000O00000OO0O +encoff2 ),'\n')#line:1137
                else :#line:1138
                    print ("You have had ",OO0000OOO00OOOOOO [0 ]," tries.")#line:1139
                    print ("If next try is accepted you will achieve ",O00O000O00000OO0O -10 ,"% on this exercise.")#line:1140
                break #line:1142
            except ValueError :#line:1144
                print ("I didn't understand that.")#line:1145
                continue #line:1146
        return #line:1149
def valdrivendho (OO00O00OOOO00OOOO ,O00OOO00OOOOOOO00 ):#line:1159
    O0O00O000OO0OOOO0 =".drivendho_counter.npy"#line:1163
    OO0O00O0OOOO0O000 =np .zeros (1 ,dtype ='int8,bool')#line:1165
    if (waiter ()):#line:1167
        while True :#line:1168
            try :#line:1169
                O00O00OO0OO0000O0 =float (input ("Please enter your estimate here: "))#line:1170
                OOOOO000OOO0O0000 =np .sqrt (OO00O00OOOO00OOOO **2 -2 *O00OOO00OOOOOOO00 **2 )#line:1171
                OOO0OO0OO000000O0 =np .isclose (O00O00OO0OO0000O0 ,OOOOO000OOO0O0000 ,0.2 )#line:1172
                if OOO0OO0OO000000O0 :#line:1173
                    print ("Well done, that is close to the resonance value ",OOOOO000OOO0O0000 )#line:1174
                else :#line:1175
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1176
                OO0O00O0OOOO0O000 =trycount (O0O00O000OO0OOOO0 ,OOO0OO0OO000000O0 )#line:1178
                OO00O00000OOO0000 =100 -(OO0O00O0OOOO0O000 [0 ]-1 )*10 #line:1179
                if OO0O00O0OOOO0O000 [1 ]:#line:1180
                    print ("First success after ",OO0O00O0OOOO0O000 [0 ]," tries, you have ",OO00O00000OOO0000 ,"% on this exercise.")#line:1181
                    print ("Enter this code into Brightspace:\n\n",genenc (5 +encoff1 ,OO00O00000OOO0000 +encoff2 ),'\n')#line:1182
                else :#line:1183
                    print ("You have had ",OO0O00O0OOOO0O000 [0 ]," tries.")#line:1184
                    print ("If next try is accepted you will achieve ",OO00O00000OOO0000 -10 ,"% on this exercise.")#line:1185
                break #line:1187
            except ValueError :#line:1189
                print ("I didn't understand that.")#line:1190
                continue #line:1191
        return #line:1194
import ipywidgets as widgets #line:1209
import sys #line:1210
from IPython .display import display #line:1211
from IPython .display import clear_output #line:1212
def create_multipleChoice_widget (O0000OOO0O0O0OOO0 ,O00OOO0OO000000OO ,O0O0O00O00OO0O0O0 ,O000000O000OOOOO0 ):#line:1214
    O000O0OOO00O000O0 ='.q{:d}_counter.npy'.format (O0000OOO0O0O0OOO0 )#line:1215
    O00O000O00O000000 =np .zeros (1 ,dtype ='int8,bool')#line:1216
    OO0OO0O000O0O0OOO =len (O0O0O00O00OO0O0O0 )#line:1218
    if O000000O000OOOOO0 not in O0O0O00O00OO0O0O0 :#line:1219
        O0O0O00O00OO0O0O0 .append (O000000O000OOOOO0 )#line:1220
    O0OO0000OOOOO000O =O0O0O00O00OO0O0O0 .index (O000000O000OOOOO0 )#line:1222
    OO0O0O0O0OOOO000O =[(OOO0OO0OO00O0OOO0 ,OOO0O00O00O0O00OO )for OOO0O00O00O0O00OO ,OOO0OO0OO00O0OOO0 in enumerate (O0O0O00O00OO0O0O0 )]#line:1224
    OOO00OO0000OOOOO0 =widgets .RadioButtons (options =OO0O0O0O0OOOO000O ,description ='',disabled =False )#line:1229
    O00O0O000OO00OOO0 =widgets .Output ()#line:1231
    with O00O0O000OO00OOO0 :#line:1232
        print (O00OOO0OO000000OO )#line:1233
    O00OOO000OO0OOOO0 =widgets .Output ()#line:1235
    def OO0OO000OO00OO000 (O0000000OO00O0000 ):#line:1237
        O00OOO0O00O00O0OO =int (OOO00OO0000OOOOO0 .value )#line:1239
        O000OOOO00O000000 =O00OOO0O00O00O0OO ==O0OO0000OOOOO000O #line:1241
        OO0O0O000O00OOO0O =trycount (O000O0OOO00O000O0 ,O000OOOO00O000000 )#line:1242
        O00OO0O0O0O00OO0O =max (0 ,100 -(OO0O0O000O00OOO0O [0 ]-1 )*100 /OO0OO0O000O0O0OOO )#line:1243
        O00OO0OOO000OO0O0 =OOO00OO0000OOOOO0 .options [O00OOO0O00O00O0OO ][0 ]#line:1244
        if O000OOOO00O000000 :#line:1245
            O00OO0OOO000OO0O0 +=' correct\n'#line:1246
        else :#line:1247
            O00OO0OOO000OO0O0 +=' incorrect\n'#line:1248
        if OO0O0O000O00OOO0O [1 ]:#line:1249
            O00OO0OOO000OO0O0 +='{:.0f}% on try {:d}'.format (O00OO0O0O0O00OO0O ,OO0O0O000O00OOO0O [0 ])#line:1250
        else :#line:1251
            O00OO0OOO000OO0O0 +='{:.0f}% remaining'.format (max (0 ,O00OO0O0O0O00OO0O -100 /OO0OO0O000O0O0OOO ))#line:1252
        with O00OOO000OO0OOOO0 :#line:1254
            clear_output ()#line:1255
            print (O00OO0OOO000OO0O0 )#line:1256
        return #line:1257
    O0O000000O00OO0O0 =widgets .Button (description ="submit")#line:1259
    O0O000000O00OO0O0 .on_click (OO0OO000OO00OO000 )#line:1260
    return widgets .VBox ([O00O0O000OO00OOO0 ,OOO00OO0000OOOOO0 ,O0O000000O00OO0O0 ,O00OOO000OO0OOOO0 ])#line:1261
def runq1 ():#line:1268
    O00OO0O000OO0O0OO =1 #line:1269
    OOOO0OOOOOO0O00O0 =create_multipleChoice_widget (O00OO0O000OO0O0OO ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1270
    display (OOOO0OOOOOO0O00O0 )#line:1271
def runQ1 ():#line:1281
    OO0OOO00000OOO000 =1 #line:1282
    OOO0OOOO0O0OOO00O =create_multipleChoice_widget (OO0OOO00000OOO000 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1283
    display (OOO0OOOO0O0OOO00O )#line:1284
def runQ2x ():#line:1293
    O0O0O0OOO000OOO00 =2 #line:1294
    OOO0OO0OOOO0OOO0O =create_multipleChoice_widget (O0O0O0OOO000OOO00 ,'',['centred','backwards','forwards'],'centred')#line:1295
    display (OOO0OO0OOOO0OOO0O )#line:1296
def runQ3x ():#line:1304
    OOO00O0O0OO00O0OO =3 #line:1305
    OOOO0O0O0000OO0O0 =create_multipleChoice_widget (OOO00O0O0OO00O0OO ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1306
    display (OOOO0O0O0000OO0O0 )#line:1307
def runQ4x ():#line:1316
    OOOO0O0OO0OO0OO00 =4 #line:1317
    OO0OOO0O00OOO00O0 =create_multipleChoice_widget (OOOO0O0OO0OO0OO00 ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1318
    display (OO0OOO0O00OOO00O0 )#line:1319
def runQ5x ():#line:1329
    OO000O0OOO0O00O00 =5 #line:1330
    OO0O0000O0O00000O =create_multipleChoice_widget (OO000O0OOO0O00O00 ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1331
    display (OO0O0000O0O00000O )#line:1332
def runQ6x ():#line:1341
    O0OO00000O00OOO00 =6 #line:1342
    O0OO0O0000000000O =create_multipleChoice_widget (O0OO00000O00OOO00 ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1343
    display (O0OO0O0000000000O )#line:1344
def runQ7x ():#line:1353
    OOOOOO0OO000000OO =7 #line:1354
    OO0O0O0000OOO0OOO =create_multipleChoice_widget (OOOOOO0OO000000OO ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1355
    display (OO0O0O0000OOO0OOO )#line:1356
pk =(283355 ,839329 )#line:1376
def getrid ():#line:1379
    import random #line:1380
    global rid #line:1381
    rid =random .randint (100000 ,999999 )#line:1382
def encrypt (O0O000O00O0OOO000 ):#line:1385
    O000OO00O0OOO0O00 ,OO000O0O00OOOOO0O =pk #line:1386
    O0O00O0OO00000000 =len (str (OO000O0O00OOOOO0O ))#line:1387
    if O0O00O0OO00000000 !=6 :#line:1388
        print ('Chunk length hardcoded in format conversion to 6 characters.\n May need to adjust here and in getrid range.\n Exiting.\n')#line:1389
    O00000O0OOO000O00 =['{:06d}'.format ((int (O0OOOO0OO0O000O0O )**O000OO00O0OOO0O00 )%OO000O0O00OOOOO0O )for O0OOOO0OO0O000O0O in str (O0O000O00O0OOO000 )]#line:1392
    return ''.join (O00000O0OOO000O00 )#line:1395
def genenc (O0000OO0000O00O00 ,O0OOOO000OOOO0000 ):#line:1398
    global rid #line:1399
    O0O00O0O0O000O00O ='{:06d}'.format (rid )#line:1400
    OO0OO000OOOOOOO00 ='{:02d}'.format (O0000OO0000O00O00 )#line:1401
    OOO00O0O0OOOOO0O0 ='{:03d}'.format (O0OOOO000OOOO0000 )#line:1402
    OOO0000OO0OOO000O =O0O00O0O0O000O00O +OO0OO000OOOOOOO00 +OOO00O0O0OOOOO0O0 #line:1404
    O0OO00O00O0O000O0 ='#'+encrypt (OOO0000OO0OOO000O )+'#'#line:1406
    print ("Your encrypted message is: ",O0OO00O00O0O000O0 )#line:1407
    return O0OO00O00O0O000O0 #line:1408
