import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (O0O00000OOOOOO00O ,O0O0O00OOOOOO000O ):#line:10
        print ("\nPasswords may not be changed using this notebook at present.")#line:14
ps =[]#line:18
wd =''#line:19
def a1 ():#line:36
    global ps #line:38
    OOO0OOO00OO0OO0OO =".a1_counter.npy"#line:41
    OO0OOO0O0OOOO00OO =np .zeros (1 ,dtype ='int8,bool')#line:42
    OOOO0OOOOOOOOO000 =0 #line:44
    O0O0O0O00OO0OOO00 =ps [0 ]#line:45
    OOO0000000O0OO0O0 =ps [1 ]#line:46
    if (waiter ()):#line:48
        while True :#line:49
            try :#line:50
                printmd ('**CA** (2%)')#line:51
                print (O0O0O0O00OO0OOO00 ,"+",OOO0000000O0OO0O0 )#line:52
                O0000OO0O00O0O00O =float (input ("Please enter your answer here: "))#line:53
                OOOO00O0O0OO0OO0O =O0O0O0O00OO0OOO00 +OOO0000000O0OO0O0 #line:54
                OOO00O0000OO0O0OO =np .isclose (O0000OO0O00O0O00O ,OOOO00O0O0OO0OO0O ,OOOO0OOOOOOOOO000 )#line:55
                if OOO00O0000OO0O0OO :#line:56
                    print ("Well done, right answer is ",OOOO00O0O0OO0OO0O )#line:57
                else :#line:58
                    print ("Not right yet. Take another look then run this cell again.")#line:59
                OO0OOO0O0OOOO00OO =trycount (OOO0OOO00OO0OO0OO ,OOO00O0000OO0O0OO )#line:61
                O0O00O0OO0O000O0O =100 -(OO0OOO0O0OOOO00OO [0 ]-1 )*10 #line:62
                if OO0OOO0O0OOOO00OO [1 ]:#line:63
                    print ("First success after ",OO0OOO0O0OOOO00OO [0 ]," tries, you have ",O0O00O0OO0O000O0O ,"% on this exercise.")#line:64
                else :#line:65
                    print ("You have had ",OO0OOO0O0OOOO00OO [0 ]," tries.")#line:66
                    print ("If next try is accepted you will achieve ",O0O00O0OO0O000O0O -10 ,"% on this exercise.")#line:67
                break #line:69
            except ValueError :#line:71
                print ("I didn't understand that.")#line:72
                continue #line:73
        return #line:75
def a2 (OO000O0O00OOOOO0O ):#line:84
    global ps #line:86
    OOOOOO0O0O00000OO =".a2_counter.npy"#line:89
    O00OOOOO000O0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:90
    O0000O00O0OOO0O00 =6 #line:93
    O000OOOO00OOO0OO0 =7 #line:94
    O0OOOOOO000OOOO0O =0 #line:96
    OOO0O000O0000O000 =(ps [O0000O00O0OOO0O00 ])%6 +1 #line:98
    OOOO00OOOO00OO000 =(ps [O000OOOO00OOO0OO0 ])%6 +1 #line:99
    while OOO0O000O0000O000 +OOOO00OOOO00OO000 ==7 or OOO0O000O0000O000 ==OOOO00OOOO00OO000 :#line:100
        OOOO00OOOO00OO000 +=1 #line:101
        OOOO00OOOO00OO000 =OOOO00OOOO00OO000 %6 +1 #line:102
    if (OO000O0O00OOOOO0O ):#line:104
        printmd ('**CA** (2%)')#line:105
        print ("Run your program (when you are happy it is working correctly) for a=",OOO0O000O0000O000 ," and b=",OOOO00OOOO00OO000 )#line:106
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:107
        return #line:108
    if (waiter ()):#line:110
        while True :#line:111
            try :#line:112
                print ("Enter your program's result for a=",OOO0O000O0000O000 ," and b=",OOOO00OOOO00OO000 )#line:113
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:114
                OO000O0OOOO0OO00O =float (input ("Please enter your answer here: "))#line:115
                OO000OOOOO000O000 =(3 *(OOO0O000O0000O000 **3 *OOOO00OOOO00OO000 -OOO0O000O0000O000 *OOOO00OOOO00OO000 **3 ))%7 #line:116
                OO0OOOOOOO0OOO0OO =np .isclose (OO000O0OOOO0OO00O ,OO000OOOOO000O000 ,O0OOOOOO000OOOO0O )#line:117
                if OO0OOOOOOO0OOO0OO :#line:118
                    print ("Well done, right answer is ",OO000OOOOO000O000 )#line:119
                else :#line:120
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:121
                O00OOOOO000O0OO0O =trycount (OOOOOO0O0O00000OO ,OO0OOOOOOO0OOO0OO )#line:123
                O00OOOOOO0OO0O0OO =100 -(O00OOOOO000O0OO0O [0 ]-1 )*10 #line:124
                if O00OOOOO000O0OO0O [1 ]:#line:125
                    print ("First success after ",O00OOOOO000O0OO0O [0 ]," tries, you have ",O00OOOOOO0OO0O0OO ,"% on this exercise.")#line:126
                else :#line:127
                    print ("You have had ",O00OOOOO000O0OO0O [0 ]," tries.")#line:128
                    print ("If next try is accepted you will achieve ",O00OOOOOO0OO0O0OO -10 ,"% on this exercise.")#line:129
                break #line:131
            except ValueError :#line:133
                print ("I didn't understand that.")#line:134
                continue #line:135
        return #line:137
def a3 (O00O0OO000OO0O0OO ):#line:146
    global ps #line:148
    O0O0O0OOO00O0OO0O =".a3_counter.npy"#line:151
    O00000O0OO0OO0OOO =np .zeros (1 ,dtype ='int8,bool')#line:152
    OOOOO0000OOOOO0O0 =23 #line:155
    O0OOOO0O00O000O0O =24 #line:156
    O000OO0O00O000OOO =(ps [OOOOO0000OOOOO0O0 ])%6 +1 #line:157
    OO0OOOOOO0OOOOOO0 =(ps [O0OOOO0O00O000O0O ])%6 +1 #line:158
    OOOOOOO0O00OO00O0 =0 #line:160
    O000OO0O00O000OOO =10 *O000OO0O00O000OOO +OO0OOOOOO0OOOOOO0 ;#line:162
    if (O00O0OO000OO0O0OO ):#line:164
        printmd ('**CA** (6%)')#line:165
        print ("Run your program for ",O000OO0O00O000OOO ,"people")#line:166
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:167
        return #line:168
    if (waiter ()):#line:170
        while True :#line:171
            try :#line:172
                print ("Enter your program's result for",O000OO0O00O000OOO ,"people")#line:173
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:174
                OOOO0O000O0O0000O =float (input ("Please enter your answer here: "))#line:175
                O0OOOO000O00O000O =O000OO0O00O000OOO +2 *O000OO0O00O000OOO +2 *O000OO0O00O000OOO +10 *O000OO0O00O000OOO #line:176
                OOO0O000O00O0O000 =np .isclose (OOOO0O000O0O0000O ,O0OOOO000O00O000O ,OOOOOOO0O00OO00O0 )#line:177
                if OOO0O000O00O0O000 :#line:178
                    print ("Well done, right answer is ",O0OOOO000O00O000O )#line:179
                else :#line:180
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:181
                O00000O0OO0OO0OOO =trycount (O0O0O0OOO00O0OO0O ,OOO0O000O00O0O000 )#line:183
                O0O0OOOO0OO0O00OO =100 -(O00000O0OO0OO0OOO [0 ]-1 )*10 #line:184
                if O00000O0OO0OO0OOO [1 ]:#line:185
                    print ("First success after ",O00000O0OO0OO0OOO [0 ]," tries, you have ",O0O0OOOO0OO0O00OO ,"% on this exercise.")#line:186
                else :#line:187
                    print ("You have had ",O00000O0OO0OO0OOO [0 ]," tries.")#line:188
                    print ("If next try is accepted you will achieve ",O0O0OOOO0OO0O00OO -10 ,"% on this exercise.")#line:189
                break #line:191
            except ValueError :#line:193
                print ("I didn't understand that.")#line:194
                continue #line:195
        return #line:197
def a4 (O0O0O0O0OO00OO0OO ):#line:208
        import random #line:210
        import requests #line:211
        global ps #line:213
        global wd #line:214
        O0O000O0OOO0OO000 =".a4_counter.npy"#line:217
        O000O000O00OOOO00 =np .zeros (1 ,dtype ='int8,bool')#line:218
        OO0OOOO000O000OO0 =60 #line:221
        O00OO000O0O0O00O0 =61 #line:222
        OOOOOOO0OOO0O0OOO =62 #line:223
        O0000OOO0000OO0O0 =63 #line:224
        O00O0O0000000O0O0 =64 #line:225
        O0OOO000OO0O000O0 =0 #line:228
        if (O0O0O0O0OO00OO0OO ):#line:230
                O0OOOO00O00O0OOOO ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:232
                OO00O0O000OO0OO0O =requests .get (O0OOOO00O00O0OOOO )#line:234
                O00OOOO0OOOOO0O0O =OO00O0O000OO0OO0O .content .splitlines ()#line:235
                random .seed (10 *ps [62 ]+ps [63 ])#line:236
                OOOO0O0O0O00O0000 =4 +(10 *ps [64 ]+ps [65 ])%4 #line:237
                O0O00O0000000O00O =True #line:238
                while O0O00O0000000O00O :#line:239
                        O00O0O0OOO00O0OO0 =O00OOOO0OOOOO0O0O [random .randint (0 ,len (O00OOOO0OOOOO0O0O )-1 )].decode ("utf-8")#line:240
                        if len (O00O0O0OOO00O0OO0 )>7 and len (O00O0O0OOO00O0OO0 )<14 and O00O0O0OOO00O0OO0 [0 ].islower ():#line:242
                                O0O00O0000000O00O =False #line:243
                                for O0OO000OOO00OOO0O in O00O0O0OOO00O0OO0 :#line:244
                                        if chr (ord (O0OO000OOO00OOO0O )+OOOO0O0O0O00O0000 )>'z':#line:245
                                                O0O00O0000000O00O =True #line:246
                OOO000000OO0OOO0O =len (O00O0O0OOO00O0OO0 )#line:248
                O00000O00O000O00O =''#line:249
                for OO00OO0000OO0O0O0 in range (0 ,OOO000000OO0OOO0O ):#line:250
                        O00000O00O000O00O +=chr (ord (O00O0O0OOO00O0OO0 [OO00OO0000OO0O0O0 ])+OOOO0O0O0O00O0000 )#line:252
                print ('Your encoded word is',O00000O00O000O00O )#line:254
                print ('Write your program in the cell below this one.\n')#line:255
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:257
                wd =O00O0O0OOO00O0OO0 #line:258
                return #line:259
        if (waiter ()):#line:261
                while True :#line:262
                        try :#line:263
                                printmd ('**CA** (6%)')#line:264
                                OO0O00O0OO00OOO0O =str (input ("Enter your DECODED word here: "))#line:265
                                OO0O0O000OOO0O00O =wd #line:266
                                O0OO000OOOOOO0O00 =OO0O00O0OO00OOO0O ==OO0O0O000OOO0O00O #line:267
                                if O0OO000OOOOOO0O00 :#line:268
                                        print ("Well done, right answer is ",OO0O0O000OOO0O00O )#line:269
                                else :#line:270
                                        print ("Not right yet. Take another look then run this cell again.")#line:271
                                O000O000O00OOOO00 =trycount (O0O000O0OOO0OO000 ,O0OO000OOOOOO0O00 )#line:273
                                OO0000000000O00O0 =100 -(O000O000O00OOOO00 [0 ]-1 )*10 #line:274
                                if O000O000O00OOOO00 [1 ]:#line:275
                                        print ("First success after ",O000O000O00OOOO00 [0 ]," tries, you have ",OO0000000000O00O0 ,"% on this exercise.")#line:276
                                else :#line:277
                                        print ("You have had ",O000O000O00OOOO00 [0 ]," tries.")#line:278
                                        print ("If next try is accepted you will achieve ",OO0000000000O00O0 -10 ,"% on this exercise.")#line:279
                                break #line:280
                        except ValueError :#line:282
                                print ("I didn't understand that.")#line:283
                                continue #line:284
                return #line:286
def a5 (O00O00OO0O0OOOOOO ):#line:296
        import random #line:298
        import requests #line:299
        global ps #line:301
        global P0 #line:302
        OO00OOOO0OO0O0O0O =".a5_counter.npy"#line:306
        O00OOO0O000O0OOO0 =np .zeros (1 ,dtype ='int8,bool')#line:307
        OOOOO0000000OOOOO =70 #line:310
        O0OO00OO00000OOOO =71 #line:311
        O0000OOO0O0O000OO =72 #line:312
        OO0OO0OOO0O0O0O00 =73 #line:313
        OOO0OO0000OOOOO00 =74 #line:314
        O0O00000O0O00O0O0 =0 #line:317
        if (O00O00OO0O0OOOOOO ):#line:319
                P0 =[]#line:320
                OO00O000O0OOO0OOO =7 +(10 *ps [OOOOO0000000OOOOO ]+ps [O0OO00OO00000OOOO ])%4 #line:321
                for OO00000OOOOOOO0OO in range (OO00O000O0OOO0OOO ):#line:322
                        P0 .append (max (0 ,ps [O0000OOO0O0O000OO +OO00000OOOOOOO0OO ]-1 ))#line:323
                print ('Run your program for the list below:\n',P0 )#line:324
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:326
        elif (waiter ()):#line:328
                while True :#line:329
                        try :#line:330
                                printmd ('**CA** (6%)')#line:333
                                OO0OO00OO0OO000OO =eval (input ("Enter your list here: "))#line:334
                                OO0OOOO0OO0O0000O =3 #line:339
                                OOOOOO000OOOO000O =P0 .copy ()#line:340
                                OOOOOO000OOOO000O .append (0 )#line:341
                                print (OOOOOO000OOOO000O )#line:342
                                OO00O000O0OOO0OOO =len (P0 )#line:343
                                for O0OO0O0OOO00O00O0 in range (OO0OOOO0OO0O0000O ):#line:344
                                        for OO00000OOOOOOO0OO in range (OO00O000O0OOO0OOO ):#line:345
                                                OOOOOO000OOOO000O [OO00000OOOOOOO0OO ]=OOOOOO000OOOO000O [OO00000OOOOOOO0OO +1 ]*(OO00000OOOOOOO0OO +1 )#line:347
                                OOOOOO000OOOO000O .pop ()#line:348
                                OO00OO000OO00O0O0 =OOOOOO000OOOO000O #line:351
                                if not type (OO0OO00OO0OO000OO )==type (OO00OO000OO00O0O0 ):#line:353
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:354
                                elif not len (OO0OO00OO0OO000OO )==len (OO00OO000OO00O0O0 ):#line:355
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:356
                                else :#line:357
                                        OO0OO00OO0OO00OOO =OO0OO00OO0OO000OO ==OO00OO000OO00O0O0 #line:358
                                        if OO0OO00OO0OO00OOO :#line:359
                                                print ("Well done, right answer is ",OO00OO000OO00O0O0 )#line:360
                                        else :#line:361
                                                print ("Not right yet. Take another look then run this cell again.")#line:362
                                        O00OOO0O000O0OOO0 =trycount (OO00OOOO0OO0O0O0O ,OO0OO00OO0OO00OOO )#line:364
                                        OOO0O0000O0O0OO00 =100 -(O00OOO0O000O0OOO0 [0 ]-1 )*10 #line:365
                                        if O00OOO0O000O0OOO0 [1 ]:#line:366
                                                print ("First success after ",O00OOO0O000O0OOO0 [0 ]," tries, you have ",OOO0O0000O0O0OO00 ,"% on this exercise.")#line:367
                                        else :#line:368
                                                print ("You have had ",O00OOO0O000O0OOO0 [0 ]," tries.")#line:369
                                                print ("If next try is accepted you will achieve ",OOO0O0000O0O0OO00 -10 ,"% on this exercise.")#line:370
                                        break #line:371
                                OOOOOO000OOOO000O =None #line:374
                                OO00OO000OO00O0O0 =None #line:375
                        except ValueError :#line:376
                                print ("I didn't understand that.")#line:377
                                continue #line:378
        return #line:380
def a6 (OOO0O0O000OOO0O0O ):#line:389
        import random #line:391
        import requests #line:392
        global ps #line:394
        global P0 #line:395
        OOOOO0OOOO0OOO0O0 =".a6_counter.npy"#line:399
        O0OO0000OOOOO000O =np .zeros (1 ,dtype ='int8,bool')#line:400
        O00O0O00O0000000O =11 #line:403
        OOO0OOOOO0OO0OO0O =16 #line:404
        OOO00OOOOO0O0OO0O =7 #line:405
        OOOO0OO00O00OO0O0 =33 #line:406
        O0O0000O0OOOOO00O =21 #line:407
        OO000000OOOOOOOOO =0 #line:410
        if (OOO0O0O000OOO0O0O ):#line:412
                OO0OO0OOO000OO0O0 =ps [O00O0O00O0000000O ]+ps [OOO0OOOOO0OO0OO0O ]+ps [OOO00OOOOO0O0OO0O ]+ps [OOOO0OO00O00OO0O0 ]+ps [O0O0000O0OOOOO00O ]#line:413
                random .seed (OO0OO0OOO000OO0O0 )#line:414
                P0 =random .randint (1000 ,2000 )#line:415
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:416
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:418
        elif (waiter ()):#line:420
                while True :#line:421
                        try :#line:422
                                printmd ('**CA** (6%)')#line:425
                                OOO0OOO0O00O0OOO0 =eval (input ("Enter your stopping number here: "))#line:426
                                O000OOO0O0OOOO0OO =P0 #line:430
                                O0000O0OOO0OO0000 =[O000OOO0O0OOOO0OO ]#line:431
                                while not O000OOO0O0OOOO0OO ==1 :#line:432
                                        if O000OOO0O0OOOO0OO %2 :#line:433
                                                O000OOO0O0OOOO0OO =3 *O000OOO0O0OOOO0OO +1 #line:434
                                        else :#line:435
                                                O000OOO0O0OOOO0OO =O000OOO0O0OOOO0OO //2 #line:436
                                        O0000O0OOO0OO0000 .append (O000OOO0O0OOOO0OO )#line:437
                                OO0OO00OO0O00OOO0 =len (O0000O0OOO0OO0000 )#line:438
                                O00OO0OOO0OO0O0O0 =OO0OO00OO0O00OOO0 #line:442
                                if not type (OOO0OOO0O00O0OOO0 )==type (O00OO0OOO0OO0O0O0 ):#line:444
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:445
                                else :#line:448
                                        O000OO0OOO0OOOO0O =OOO0OOO0O00O0OOO0 ==O00OO0OOO0OO0O0O0 #line:449
                                        if O000OO0OOO0OOOO0O :#line:450
                                                print ("Well done, right answer is ",O00OO0OOO0OO0O0O0 )#line:451
                                        else :#line:452
                                                print ("Not right yet. Take another look then run this cell again.")#line:453
                                        O0OO0000OOOOO000O =trycount (OOOOO0OOOO0OOO0O0 ,O000OO0OOO0OOOO0O )#line:455
                                        O0O00000OO000OOOO =100 -(O0OO0000OOOOO000O [0 ]-1 )*10 #line:456
                                        if O0OO0000OOOOO000O [1 ]:#line:457
                                                print ("First success after ",O0OO0000OOOOO000O [0 ]," tries, you have ",O0O00000OO000OOOO ,"% on this exercise.")#line:458
                                        else :#line:459
                                                print ("You have had ",O0OO0000OOOOO000O [0 ]," tries.")#line:460
                                                print ("If next try is accepted you will achieve ",O0O00000OO000OOOO -10 ,"% on this exercise.")#line:461
                                        break #line:462
                                OO0OO00OO0O00OOO0 =None #line:465
                                O00OO0OOO0OO0O0O0 =None #line:466
                        except ValueError :#line:467
                                print ("I didn't understand that.")#line:468
                                continue #line:469
        return #line:471
def a7 (OO00OOO00000O00O0 ):#line:481
        OO00OO0OOO0O0OOO0 =".a7_counter.npy"#line:485
        OO0OOOO000O0OOOOO =np .zeros (1 ,dtype ='int8,bool')#line:486
        def O000OO00000OOOO0O ():#line:488
                pass #line:489
        OOO000O0OO0O00O00 =[(30 ,10 )]#line:492
        OOO000O0O0O000O0O =1.0e-4 #line:495
        if (waiter ()):#line:498
                printmd ('**CA** (6%)')#line:500
                if not type (OO00OOO00000O00O0 )==type (O000OO00000OOOO0O ):#line:502
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:503
                else :#line:506
                        def OO0O000000000O000 (O0O00O00O0OOO0OO0 ,O00000O00O0O0OO0O ):#line:509
                                import math #line:510
                                O0O00O00O00OOO0OO =9.81 #line:511
                                OO00O00OOO0OO000O =math .pi *O00000O00O0O0OO0O /180. #line:512
                                OOO000OOO00O0OO00 =O0O00O00O0OOO0OO0 **2 *math .sin (2 *OO00O00OOO0OO000O )/O0O00O00O00OOO0OO #line:513
                                OOOOOO0O00OOOO000 =O0O00O00O0OOO0OO0 **2 *(math .sin (OO00O00OOO0OO000O ))**2 /(2. *O0O00O00O00OOO0OO )#line:514
                                return OOO000OOO00O0OO00 ,OOOOOO0O00OOOO000 #line:515
                        import random as r #line:518
                        OOO000O0OO0O00O00 =[]#line:519
                        O0000OOO00OO00000 =False #line:520
                        OOO00O000O00O000O =[]#line:521
                        OOOO0OOO000O0OO00 =10 #line:522
                        OO00OO00OO00O0OOO =100 #line:523
                        O0O0O000O0OOOO0OO =5 #line:524
                        O000OOO00O00O000O =85 #line:525
                        for O000O0O00O0OO0O0O in range (5 ):#line:526
                                OOO000O0OO0O00O00 .append ((r .uniform (OOOO0OOO000O0OO00 ,OO00OO00OO00O0OOO ),r .uniform (O0O0O000O0OOOO0OO ,O000OOO00O00O000O )))#line:527
                        for (OOOOO00O00O0O0OO0 ,OOOO0O0O0OOOO0O00 )in OOO000O0OO0O00O00 :#line:528
                                print ('Testing:',OOOOO00O00O0O0OO0 ,OOOO0O0O0OOOO0O00 )#line:529
                                OOO00O0O0OO0000OO =OO00OOO00000O00O0 (OOOOO00O00O0O0OO0 ,OOOO0O0O0OOOO0O00 )#line:530
                                print ('Output:',*OOO00O0O0OO0000OO )#line:531
                                OOO0OOOOOO00O0OOO =OO0O000000000O000 (OOOOO00O00O0O0OO0 ,OOOO0O0O0OOOO0O00 )#line:532
                                print ('Actual:',*OOO0OOOOOO00O0OOO )#line:533
                                print ()#line:534
                                if (not type (OOO00O0O0OO0000OO )==type (OOO0OOOOOO00O0OOO ))or (not len (OOO00O0O0OO0000OO )==len (OOO0OOOOOO00O0OOO )):#line:535
                                        if O0000OOO00OO00000 ==False :#line:536
                                           O0000OOO00OO00000 =True #line:537
                                else :#line:538
                                        OOO00O000O00O000O .append (all (np .isclose (OOO00O0O0OO0000OO ,OOO0OOOOOO00O0OOO ,OOO000O0O0O000O0O )))#line:539
                        if O0000OOO00OO00000 :#line:541
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:542
                        else :#line:544
                                OO00O00O0OOOO0O00 =all (OOO00O000O00O000O )#line:545
                                if OO00O00O0OOOO0O00 :#line:546
                                        print ("Well done, all correct.")#line:547
                                else :#line:548
                                        print ("Not right yet. Take another look then run this cell again.")#line:549
                                OO0OOOO000O0OOOOO =trycount (OO00OO0OOO0O0OOO0 ,OO00O00O0OOOO0O00 )#line:551
                                OOOO0O00OOOOO000O =100 -(OO0OOOO000O0OOOOO [0 ]-1 )*10 #line:552
                                if OO0OOOO000O0OOOOO [1 ]:#line:553
                                        print ("First success after ",OO0OOOO000O0OOOOO [0 ]," tries, you have ",OOOO0O00OOOOO000O ,"% on this exercise.")#line:554
                                else :#line:555
                                        print ("You have had ",OO0OOOO000O0OOOOO [0 ]," tries.")#line:556
                                        print ("If next try is accepted you will achieve ",OOOO0O00OOOOO000O -10 ,"% on this exercise.")#line:557
                        OOO0OOOOOO00O0OOO =None #line:560
                        OO0O000000000O000 =None #line:561
        return #line:563
def a8 (O0OOOO0OO00O000O0 ):#line:573
        OO000O00000O0OOO0 =".a8_counter.npy"#line:577
        OOOO0O000OOOO0OO0 =np .zeros (1 ,dtype ='int8,bool')#line:578
        def OO00O0OO0OO0OO0O0 ():#line:580
                pass #line:581
        O000O00OOO000OO00 =1.0e-4 #line:585
        if (waiter ()):#line:588
                printmd ('**CA** (6%)')#line:590
                if not type (O0OOOO0OO00O000O0 )==type (OO00O0OO0OO0OO0O0 ):#line:594
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:595
                else :#line:599
                        import inspect #line:602
                        O0OOOO000O0O00OO0 =inspect .getsourcelines (O0OOOO0OO00O000O0 )#line:603
                        OO0O000OOOOOO0OOO =True #line:604
                        OOO00OOOO0O0OO0OO =[]#line:605
                        for O0O00O000000O00O0 ,OO00OO0OO00O00O00 in enumerate (O0OOOO000O0O00OO0 [0 ]):#line:606
                                if 'for'in OO00OO0OO00O00O00 or 'while'in OO00OO0OO00O00O00 :#line:607
                                        OO0O000OOOOOO0OOO =False #line:609
                                        OOO00OOOO0O0OO0OO .append (O0O00O000000O00O0 )#line:610
                        if not OO0O000OOOOOO0OOO :#line:611
                                print ('Function needs to be written without loops (using NumPy), check lines',*OOO00OOOO0O0OO0OO )#line:612
                                print ('No marks lost for this attempt.')#line:613
                                return #line:614
                        def OOOO0OO00OO00OO0O (OOO000O000O000OOO ):#line:617
                                OOOOOOO000000000O =np .vstack ((OOO000O000O000OOO ,OOO000O000O000OOO [0 ]))#line:618
                                OOO0O00O00O0O0O0O =sum (OOOOOOO000000000O [:-1 ,0 ]*OOOOOOO000000000O [1 :,1 ])#line:619
                                OO0OO0OOO0OO000O0 =sum (OOOOOOO000000000O [:-1 ,1 ]*OOOOOOO000000000O [1 :,0 ])#line:620
                                return abs (OOO0O00O00O0O0O0O -OO0OO0OOO0OO000O0 )/2 #line:621
                        import random as r #line:624
                        O0O0O0000O000OOOO =r .randint (6 ,11 )#line:625
                        OO0O0O0OO0OO00O00 =np .ones ((O0O0O0000O000OOOO ,2 ))#line:626
                        O00O000OOOOOOO000 =False #line:627
                        OOO0OOOOOOO000O00 =[]#line:628
                        OOOOOOO0OOO00OOOO =1. #line:629
                        O0O0OO0O0OO0OO00O =20. #line:630
                        O0O00000O0000O0OO =OOOOOOO0OOO00OOOO #line:631
                        OOO0OOOOOOO00OO0O =O0O0OO0O0OO0OO00O #line:632
                        for OOO00OOOO0OOO0OO0 in range (O0O0O0000O000OOOO ):#line:633
                                OO0O0O0OO0OO00O00 [OOO00OOOO0OOO0OO0 ]=[r .uniform (OOOOOOO0OOO00OOOO ,O0O0OO0O0OO0OO00O ),r .uniform (O0O00000O0000O0OO ,OOO0OOOOOOO00OO0O )]#line:634
                        print ('Testing:',OO0O0O0OO0OO00O00 )#line:635
                        O0OOO00OO000O00OO =O0OOOO0OO00O000O0 (OO0O0O0OO0OO00O00 )#line:636
                        print ('Output:',O0OOO00OO000O00OO )#line:637
                        O000O0OOOO000OOOO =OOOO0OO00OO00OO0O (OO0O0O0OO0OO00O00 )#line:638
                        print ('Actual:',O000O0OOOO000OOOO )#line:639
                        print ()#line:640
                        if not type (O0OOO00OO000O00OO )==type (O000O0OOOO000OOOO ):#line:641
                                if O00O000OOOOOOO000 ==False :#line:642
                                        O00O000OOOOOOO000 =True #line:643
                        else :#line:644
                                OOO0OOOOOOO000O00 .append (np .isclose (O0OOO00OO000O00OO ,O000O0OOOO000OOOO ,O000O00OOO000OO00 ))#line:645
                        if O00O000OOOOOOO000 :#line:647
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:648
                        else :#line:650
                                O000OO000000000O0 =all (OOO0OOOOOOO000O00 )#line:651
                                if O000OO000000000O0 :#line:652
                                        print ("Well done, all correct.")#line:653
                                else :#line:654
                                        print ("Not right yet. Take another look then run this cell again.")#line:655
                                OOOO0O000OOOO0OO0 =trycount (OO000O00000O0OOO0 ,O000OO000000000O0 )#line:657
                                O0OO0O00OOOO00O0O =100 -(OOOO0O000OOOO0OO0 [0 ]-1 )*10 #line:658
                                if OOOO0O000OOOO0OO0 [1 ]:#line:659
                                        print ("First success after ",OOOO0O000OOOO0OO0 [0 ]," tries, you have ",O0OO0O00OOOO00O0O ,"% on this exercise.")#line:660
                                else :#line:661
                                        print ("You have had ",OOOO0O000OOOO0OO0 [0 ]," tries.")#line:662
                                        print ("If next try is accepted you will achieve ",O0OO0O00OOOO00O0O -10 ,"% on this exercise.")#line:663
                        O000O0OOOO000OOOO =None #line:666
                        OOOO0OO00OO00OO0O =None #line:667
        return #line:669
def a1_notlive ():#line:685
        print ('This CA test is not currently live.')#line:686
        return #line:687
def a2_notlive (O0OOOOO0OOO00OO0O ):#line:695
        print ('This CA test is not currently live.')#line:696
        return #line:697
def a3_notlive (OO0000O0000O0O000 ):#line:705
        print ('This CA test is not currently live.')#line:706
        return #line:707
def a4_notlive (OOO0000O0OOO00O00 ):#line:715
        print ('This CA test is not currently live.')#line:716
        return #line:717
def a5_notlive (OO0OOO0OO00O00O0O ):#line:725
        print ('This CA test is not currently live.')#line:726
        return #line:727
def a6_notlive (O000000OO0OOO0OO0 ):#line:735
        print ('This CA test is not currently live.')#line:736
        return #line:737
def a7_notlive ():#line:745
        print ('This CA test is not currently live.')#line:746
        return #line:747
def a8_notlive (OO0OOO0000000OOO0 ):#line:755
        print ('This CA test is not currently live.')#line:756
        return #line:757
def b1 ():#line:775
    global ps #line:777
    O00000O0OO000OO0O =".b1_counter.npy"#line:780
    O00OO0O00OO0000OO =np .zeros (1 ,dtype ='int8,bool')#line:781
    OOO0O00O00OO0O0OO =0.05 #line:783
    if (waiter ()):#line:785
        while True :#line:786
            try :#line:787
                printmd ('**CA**')#line:788
                OOOOOO0OO0OO0O00O =eval (input ("Please enter your answer here in the format D,k: "))#line:789
                OOOOO00OOOO0O00OO =(0.025 ,2.0 )#line:790
                O00O00O00O0O0O0OO =all (np .isclose (OOOOOO0OO0OO0O00O ,OOOOO00OOOO0O00OO ,rtol =OOO0O00O00OO0O0OO ))#line:791
                if O00O00O00O0O0O0OO :#line:792
                    print ("Well done, reasonable estimate is ",OOOOO00OOOO0O00OO )#line:793
                else :#line:794
                    print ("Not right yet. Take another look then run this cell again.")#line:795
                O00OO0O00OO0000OO =trycount (O00000O0OO000OO0O ,O00O00O00O0O0O0OO )#line:797
                O00O0O0O0O00OO00O =100 -(O00OO0O00OO0000OO [0 ]-1 )*10 #line:798
                if O00OO0O00OO0000OO [1 ]:#line:799
                    print ("First success after ",O00OO0O00OO0000OO [0 ]," tries, you have ",O00O0O0O0O00OO00O ,"% on this exercise.")#line:800
                else :#line:801
                    print ("You have had ",O00OO0O00OO0000OO [0 ]," tries.")#line:802
                    print ("If next try is accepted you will achieve ",O00O0O0O0O00OO00O -10 ,"% on this exercise.")#line:803
                break #line:805
            except ValueError :#line:807
                print ("I didn't understand that.")#line:808
                continue #line:809
        return #line:811
def b2 (O0OOO0OOOO0OOO000 ):#line:821
        O0OOO0O0OOO00O00O =".b2_counter.npy"#line:825
        OO0000O000OO00O0O =np .zeros (1 ,dtype ='int8,bool')#line:826
        def OO00O0OOOOOOO00O0 ():#line:828
                pass #line:829
        O00OOO0O0000OOO00 =1.0e-2 #line:832
        OO0O0OOO0OO0OO0OO =0.0 #line:833
        if (waiter ()):#line:835
                printmd ('**CA**')#line:837
                if not type (O0OOO0OOOO0OOO000 )==type (OO00O0OOOOOOO00O0 ):#line:839
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:840
                else :#line:843
                        def O00OO0000O00OOOO0 (OOOOOOOO000O00OO0 ):#line:847
                                O00OO0OOOO00000OO =[]#line:848
                                O0000O000O0000OOO =20.0 #line:849
                                OO0OOO00OO0O0O0O0 =58.1e-3 #line:850
                                O0O0O0O000O0OOO00 =9.81 #line:851
                                O0O000O00OO00OO00 =0.0 #line:852
                                O0O0O00000000O000 =0.0 #line:853
                                OOOO0OOOO00O0OOO0 =0.0 #line:854
                                OOOOO0O0O00OOOOOO =10 #line:855
                                OOOO0O0O0O00O0O00 =3.35e-2 #line:856
                                O00000OOO0OO0OOOO =0.51 #line:857
                                O0OO000O0O00O00OO =1.25 #line:858
                                O0OO00O0O0OO00OO0 =math .pi *OOOO0O0O0O00O0O00 **2 #line:859
                                OO0O0OOO000O00O0O =0.5 *O00000OOO0OO0OOOO *O0OO00O0O0OO00OO0 *O0OO000O0O00O00OO #line:860
                                O0O0000O0OOOO0O00 =100000 #line:862
                                OO0OOOO00O00OO000 =np .zeros (O0O0000O0OOOO0O00 ,float )#line:863
                                OOO0O0OOO000OOO00 =np .zeros (O0O0000O0OOOO0O00 ,float )#line:864
                                O0O0OOO0OOOO00O0O =np .zeros (O0O0000O0OOOO0O00 ,float )#line:865
                                OO00O0O00O00O00OO =np .zeros (O0O0000O0OOOO0O00 ,float )#line:866
                                O0000000OO00O00OO =np .zeros (O0O0000O0OOOO0O00 ,float )#line:867
                                O00O00OOO0OOO0OOO =np .zeros (O0O0000O0OOOO0O00 ,float )#line:868
                                O000O0OO0O0O0O0O0 =np .zeros (O0O0000O0OOOO0O00 ,float )#line:869
                                OO0OOOO00O00OO000 ,OO0000O0OO0OO0OOO =np .linspace (OOOO0OOOO00O0OOO0 ,OOOOO0O0O00OOOOOO ,O0O0000O0OOOO0O00 ,retstep =True )#line:870
                                for O0000O0O00OOOO000 in OOOOOOOO000O00OO0 :#line:872
                                        O0OO0O0000O00O0O0 =O0000O000O0000OOO *math .cos (O0000O0O00OOOO000 )#line:873
                                        O00000O00O0000OOO =O0000O000O0000OOO *math .sin (O0000O0O00OOOO000 )#line:874
                                        O00O00OOO0OOO0OOO [0 ]=O0O000O00OO00OO00 #line:876
                                        O000O0OO0O0O0O0O0 [0 ]=O0O0O00000000O000 #line:877
                                        OO00O0O00O00O00OO [0 ]=O0OO0O0000O00O0O0 #line:878
                                        O0000000OO00O00OO [0 ]=O00000O00O0000OOO #line:879
                                        for O00O00O0O0O0OOOO0 in range (O0O0000O0OOOO0O00 -1 ):#line:880
                                                O0O0O0000OO00OOO0 =math .sqrt (OO00O0O00O00O00OO [O00O00O0O0O0OOOO0 ]**2 +O0000000OO00O00OO [O00O00O0O0O0OOOO0 ]**2 )#line:881
                                                O0OOOOOOO00O00O0O =-OO0O0OOO000O00O0O *O0O0O0000OO00OOO0 *OO00O0O00O00O00OO [O00O00O0O0O0OOOO0 ]#line:882
                                                OOO0O0OOO000OOO00 [O00O00O0O0O0OOOO0 ]=O0OOOOOOO00O00O0O /OO0OOO00OO0O0O0O0 #line:883
                                                OO00O0O00O00O00OO [O00O00O0O0O0OOOO0 +1 ]=OO00O0O00O00O00OO [O00O00O0O0O0OOOO0 ]+OOO0O0OOO000OOO00 [O00O00O0O0O0OOOO0 ]*OO0000O0OO0OO0OOO #line:884
                                                O00O00OOO0OOO0OOO [O00O00O0O0O0OOOO0 +1 ]=O00O00OOO0OOO0OOO [O00O00O0O0O0OOOO0 ]+OO00O0O00O00O00OO [O00O00O0O0O0OOOO0 +1 ]*OO0000O0OO0OO0OOO #line:885
                                                OOO0000OOOOOO0OOO =-OO0OOO00OO0O0O0O0 *O0O0O0O000O0OOO00 -OO0O0OOO000O00O0O *O0O0O0000OO00OOO0 *O0000000OO00O00OO [O00O00O0O0O0OOOO0 ]#line:886
                                                O0O0OOO0OOOO00O0O [O00O00O0O0O0OOOO0 ]=OOO0000OOOOOO0OOO /OO0OOO00OO0O0O0O0 #line:887
                                                O0000000OO00O00OO [O00O00O0O0O0OOOO0 +1 ]=O0000000OO00O00OO [O00O00O0O0O0OOOO0 ]+O0O0OOO0OOOO00O0O [O00O00O0O0O0OOOO0 ]*OO0000O0OO0OO0OOO #line:888
                                                O000O0OO0O0O0O0O0 [O00O00O0O0O0OOOO0 +1 ]=O000O0OO0O0O0O0O0 [O00O00O0O0O0OOOO0 ]+O0000000OO00O00OO [O00O00O0O0O0OOOO0 +1 ]*OO0000O0OO0OO0OOO #line:889
                                                if (O000O0OO0O0O0O0O0 [O00O00O0O0O0OOOO0 +1 ]<0 ):#line:890
                                                        break #line:891
                                        O0O0000O0O00O0O00 =O00O00O0O0O0OOOO0 #line:892
                                        O00OO0OOOO00000OO .append (O00O00OOO0OOO0OOO [O0O0000O0O00O0O00 ])#line:893
                                return (O00OO0OOOO00000OO );#line:895
                        import random as r #line:898
                        OOOO0O0000OO0000O =[]#line:899
                        OO0OOO0O0OO0OO00O =False #line:900
                        OOOO0O0OO00O0000O =[]#line:901
                        O0OO0OO00000O0OO0 =0.1 #line:902
                        O0OO0O0O0O0OO0O0O =1.5 #line:903
                        for OOOO00OO00O000000 in range (5 ):#line:904
                                OOOO0O0000OO0000O .append (r .uniform (O0OO0OO00000O0OO0 ,O0OO0O0O0O0OO0O0O ))#line:905
                        OOOO0O0000OO0000O .sort ()#line:906
                        print ('Testing thetas=',OOOO0O0000OO0000O )#line:907
                        OO000O000OOOO00O0 =O0OOO0OOOO0OOO000 (OOOO0O0000OO0000O )#line:908
                        print ('Output ximpacts=',OO000O000OOOO00O0 )#line:909
                        O00000OO0O00OOO00 =O00OO0000O00OOOO0 (OOOO0O0000OO0000O )#line:910
                        print ('Actual ximpacts=',O00000OO0O00OOO00 )#line:911
                        print ()#line:912
                        if (not type (OO000O000OOOO00O0 )==type (O00000OO0O00OOO00 ))or (not len (OO000O000OOOO00O0 )==len (O00000OO0O00OOO00 )):#line:913
                                if OO0OOO0O0OO0OO00O ==False :#line:914
                                        OO0OOO0O0OO0OO00O =True #line:915
                        else :#line:916
                                OOOO0O0OO00O0000O .append (all (np .isclose (OO000O000OOOO00O0 ,O00000OO0O00OOO00 ,rtol =O00OOO0O0000OOO00 ,atol =OO0O0OOO0OO0OO0OO )))#line:917
                        if OO0OOO0O0OO0OO00O :#line:919
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:920
                        else :#line:922
                                OOOOOO0OOO0O000OO =all (OOOO0O0OO00O0000O )#line:923
                                if OOOOOO0OOO0O000OO :#line:924
                                        print ("Well done, all correct.")#line:925
                                else :#line:926
                                        print ("Not close enough. Take another look then run this cell again.")#line:927
                                OO0000O000OO00O0O =trycount (O0OOO0O0OOO00O00O ,OOOOOO0OOO0O000OO )#line:929
                                O00O00O0OOO0O000O =100 -(OO0000O000OO00O0O [0 ]-1 )*10 #line:930
                                if OO0000O000OO00O0O [1 ]:#line:931
                                        print ("First success after ",OO0000O000OO00O0O [0 ]," tries, you have ",O00O00O0OOO0O000O ,"% on this exercise.")#line:932
                                else :#line:933
                                        print ("You have had ",OO0000O000OO00O0O [0 ]," tries.")#line:934
                                        print ("If next try is accepted you will achieve ",O00O00O0OOO0O000O -10 ,"% on this exercise.")#line:935
                        O00000OO0O00OOO00 =None #line:938
                        O00OO0000O00OOOO0 =None #line:939
        return #line:941
def b3 ():#line:951
    global ps #line:953
    OO0O0OOO00OO0O000 =".b3_counter.npy"#line:956
    OOO0O000000O000O0 =np .zeros (1 ,dtype ='int8,bool')#line:957
    OO0O000O00O0O00O0 =0.01 #line:960
    if (waiter ()):#line:962
        while True :#line:963
            try :#line:964
                printmd ('**CA**')#line:965
                O0O0OO0OOO0OO0000 =float (input ("Enter a real number here: "))#line:966
                O0OO00000000O0OOO =0.5 #line:967
                OOOOOOOOOOOO000OO =np .isclose (O0O0OO0OOO0OO0000 ,O0OO00000000O0OOO ,atol =OO0O000O00O0O00O0 )#line:968
                if OOOOOOOOOOOO000OO :#line:969
                    print ("Well done. Actual value is ",O0OO00000000O0OOO )#line:970
                else :#line:971
                    print ("Not right yet. Take another look then run this cell again.")#line:972
                OOO0O000000O000O0 =trycount (OO0O0OOO00OO0O000 ,OOOOOOOOOOOO000OO )#line:974
                OO000O0OOOO00O0O0 =100 -(OOO0O000000O000O0 [0 ]-1 )*10 #line:975
                if OOO0O000000O000O0 [1 ]:#line:976
                    print ("First success after ",OOO0O000000O000O0 [0 ]," tries, you have ",OO000O0OOOO00O0O0 ,"% on this exercise.")#line:977
                else :#line:978
                    print ("You have had ",OOO0O000000O000O0 [0 ]," tries.")#line:979
                    print ("If next try is accepted you will achieve ",OO000O0OOOO00O0O0 -10 ,"% on this exercise.")#line:980
                break #line:982
            except ValueError :#line:984
                print ("I didn't understand that.")#line:985
                continue #line:986
        return #line:988
def b1_notlive ():#line:1000
        print ('This CA test is not currently live.')#line:1001
        return #line:1002
def b2_notlive (OOO000000O0000OO0 ):#line:1012
        print ('This CA test is not currently live.')#line:1013
        return #line:1014
def b3_notlive ():#line:1021
        print ('This CA test is not currently live.')#line:1022
        return #line:1023
def printmd (O0OO000000O00OOOO ):#line:1033
    display (Markdown (O0OO000000O00OOOO ))#line:1034
def repeat_to_length (OO0O0000000O0O000 ,OO00O000OOO00OOOO ):#line:1036
   return (OO0O0000000O0O000 *((OO00O000OOO00OOOO //len (OO0O0000000O0O000 ))+1 ))[:OO00O000OOO00OOOO ]#line:1037
def getco (OO00OO00OOO00O00O ):#line:1039
    global ps #line:1040
    import random #line:1046
    OOO0000O0000OOO00 =str (random .randint (1e6 ,1e7 ))#line:1047
    OOOO000O00OO00O00 =int .from_bytes (OOO0000O0000OOO00 .encode (),'little')#line:1051
    O0O000OOO000OOOO0 =str (OOOO000O00OO00O00 )#line:1052
    O00O00O0OO0OOO00O =repeat_to_length (O0O000OOO000OOOO0 ,OO00OO00OOO00O00O )#line:1053
    ps =[int (O0O0OO0OOO0OO00O0 )+1 for O0O0OO0OOO0OO00O0 in O00O00O0OO0OOO00O ]#line:1054
def waiter ():#line:1056
    OOO0OO00OO0O00OOO =20 #line:1059
    OO0OO0O0000O00O00 =".ts1.txt"#line:1061
    if os .path .isfile (OO0OO0O0000O00O00 ):#line:1062
        O00O00O0OO0OO0000 =np .loadtxt (OO0OO0O0000O00O00 )#line:1063
    else :#line:1065
        O00O00O0OO0OO0000 =0.0 #line:1066
    OO000OOOOOOO00OO0 =time .time ()#line:1069
    O0OO0OOO0OO00O0O0 =OO000OOOOOOO00OO0 -O00O00O0OO0OO0000 #line:1070
    if (O0OO0OOO0OO00O0O0 <OOO0OO00OO0O00OOO ):#line:1072
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O0OO0OOO0OO00O0O0 ,OOO0OO00OO0O00OOO ))#line:1073
        return False #line:1074
    else :#line:1075
        OO00O0O00OOO0O00O =open (OO0OO0O0000O00O00 ,'w')#line:1076
        OO00O0O00OOO0O00O .write (str (OO000OOOOOOO00OO0 ))#line:1077
        OO00O0O00OOO0O00O .close ()#line:1078
        return True #line:1079
def trycount (O0OOO0O00O0O0OOO0 ,OO000OOOOO000O00O ):#line:1081
    if os .path .isfile (O0OOO0O00O0O0OOO0 ):#line:1083
        OOO00O00OOO000O0O =np .load (O0OOO0O00O0O0OOO0 )#line:1084
    else :#line:1086
        OOO00O00OOO000O0O =np .zeros (1 ,dtype ='int8,bool')#line:1087
        OOO00O00OOO000O0O =[0 ,False ]#line:1088
    if not OOO00O00OOO000O0O [1 ]:#line:1091
        OOO00O00OOO000O0O [0 ]+=1 #line:1092
        OOO00O00OOO000O0O [1 ]=OO000OOOOO000O00O #line:1093
        np .save (O0OOO0O00O0O0OOO0 ,OOO00O00OOO000O0O )#line:1095
    return OOO00O00OOO000O0O #line:1097
def valdho (O0O0O0OOOOO000OO0 ,OOO0000O0O0000000 ):#line:1105
    OOOO0O0O0OO00OOOO =".dho_counter.npy"#line:1109
    OO0O0OO00O0O0O0OO =np .zeros (1 ,dtype ='int8,bool')#line:1111
    if (waiter ()):#line:1113
        while True :#line:1114
            try :#line:1115
                O0O0OO0OOOO000OOO =float (input ("Please enter your estimate here: "))#line:1116
                OOOOOO00O0O000O00 =2 *np .sqrt (O0O0O0OOOOO000OO0 *OOO0000O0O0000000 )#line:1117
                OOO0OO00OOO0OOO0O =np .isclose (O0O0OO0OOOO000OOO ,OOOOOO00O0O000O00 ,0.2 )#line:1118
                if OOO0OO00OOO0OOO0O :#line:1119
                    print ("Well done, that is close to the critical damping value ",OOOOOO00O0O000O00 )#line:1120
                else :#line:1121
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1122
                OO0O0OO00O0O0O0OO =trycount (OOOO0O0O0OO00OOOO ,OOO0OO00OOO0OOO0O )#line:1124
                OOOOOO0O00000OO0O =100 -(OO0O0OO00O0O0O0OO [0 ]-1 )*10 #line:1125
                if OO0O0OO00O0O0O0OO [1 ]:#line:1126
                    print ("First success after ",OO0O0OO00O0O0O0OO [0 ]," tries, you have ",OOOOOO0O00000OO0O ,"% on this exercise.")#line:1127
                else :#line:1128
                    print ("You have had ",OO0O0OO00O0O0O0OO [0 ]," tries.")#line:1129
                    print ("If next try is accepted you will achieve ",OOOOOO0O00000OO0O -10 ,"% on this exercise.")#line:1130
                break #line:1132
            except ValueError :#line:1134
                print ("I didn't understand that.")#line:1135
                continue #line:1136
        return #line:1139
def valdrivendho (O0O0OO0OOOOO00000 ,O0O0O0O0OOO0O0O00 ):#line:1149
    OO0000OO0000O000O =".drivendho_counter.npy"#line:1153
    O0OO0O000O0OO00O0 =np .zeros (1 ,dtype ='int8,bool')#line:1155
    if (waiter ()):#line:1157
        while True :#line:1158
            try :#line:1159
                OO00O00OOO0O0O000 =float (input ("Please enter your estimate here: "))#line:1160
                O00O0O0OOO00O0O00 =np .sqrt (O0O0OO0OOOOO00000 **2 -2 *O0O0O0O0OOO0O0O00 **2 )#line:1161
                OOO0OOOO0O0O00000 =np .isclose (OO00O00OOO0O0O000 ,O00O0O0OOO00O0O00 ,0.2 )#line:1162
                if OOO0OOOO0O0O00000 :#line:1163
                    print ("Well done, that is close to the resonance value ",O00O0O0OOO00O0O00 )#line:1164
                else :#line:1165
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1166
                O0OO0O000O0OO00O0 =trycount (OO0000OO0000O000O ,OOO0OOOO0O0O00000 )#line:1168
                O0OOO0OO0OOOOO0OO =100 -(O0OO0O000O0OO00O0 [0 ]-1 )*10 #line:1169
                if O0OO0O000O0OO00O0 [1 ]:#line:1170
                    print ("First success after ",O0OO0O000O0OO00O0 [0 ]," tries, you have ",O0OOO0OO0OOOOO0OO ,"% on this exercise.")#line:1171
                else :#line:1172
                    print ("You have had ",O0OO0O000O0OO00O0 [0 ]," tries.")#line:1173
                    print ("If next try is accepted you will achieve ",O0OOO0OO0OOOOO0OO -10 ,"% on this exercise.")#line:1174
                break #line:1176
            except ValueError :#line:1178
                print ("I didn't understand that.")#line:1179
                continue #line:1180
        return #line:1183
import ipywidgets as widgets #line:1198
import sys #line:1199
from IPython .display import display #line:1200
from IPython .display import clear_output #line:1201
def create_multipleChoice_widget (O0O00OO0O0O0OOOO0 ,OOOO0O000O0O0OOO0 ,O0000OOO0OO00O0OO ,O0OOOO0000OOOOOOO ):#line:1203
    O00OO0O0OOOO0OOOO ='.q{:d}_counter.npy'.format (O0O00OO0O0O0OOOO0 )#line:1204
    O000O000OO0OO0O0O =np .zeros (1 ,dtype ='int8,bool')#line:1205
    O0OO00O00OO0O0O0O =len (O0000OOO0OO00O0OO )#line:1207
    if O0OOOO0000OOOOOOO not in O0000OOO0OO00O0OO :#line:1208
        O0000OOO0OO00O0OO .append (O0OOOO0000OOOOOOO )#line:1209
    O0OO00OOOO0O000O0 =O0000OOO0OO00O0OO .index (O0OOOO0000OOOOOOO )#line:1211
    O0OO00000000O0O0O =[(O00OOOO0O00OO00O0 ,OOO00O000O000O000 )for OOO00O000O000O000 ,O00OOOO0O00OO00O0 in enumerate (O0000OOO0OO00O0OO )]#line:1213
    OO000O0OOOOOO000O =widgets .RadioButtons (options =O0OO00000000O0O0O ,description ='',disabled =False )#line:1218
    OO0OOO000O00O0OOO =widgets .Output ()#line:1220
    with OO0OOO000O00O0OOO :#line:1221
        print (OOOO0O000O0O0OOO0 )#line:1222
    O0OOO0000O0O0OO00 =widgets .Output ()#line:1224
    def O0OOOO00O00OOOO0O (O0000OO00O0O0O000 ):#line:1226
        OOOOO0OOO0O0O00OO =int (OO000O0OOOOOO000O .value )#line:1228
        OOOO00O00O0OOOO00 =OOOOO0OOO0O0O00OO ==O0OO00OOOO0O000O0 #line:1230
        OO000O000O0OOO00O =trycount (O00OO0O0OOOO0OOOO ,OOOO00O00O0OOOO00 )#line:1231
        O00O0O0OOO0OO0O00 =max (0 ,100 -(OO000O000O0OOO00O [0 ]-1 )*100 /O0OO00O00OO0O0O0O )#line:1232
        O000O00OO00O0O0OO =OO000O0OOOOOO000O .options [OOOOO0OOO0O0O00OO ][0 ]#line:1233
        if OOOO00O00O0OOOO00 :#line:1234
            O000O00OO00O0O0OO +=' correct\n'#line:1235
        else :#line:1236
            O000O00OO00O0O0OO +=' incorrect\n'#line:1237
        if OO000O000O0OOO00O [1 ]:#line:1238
            O000O00OO00O0O0OO +='{:.0f}% on try {:d}'.format (O00O0O0OOO0OO0O00 ,OO000O000O0OOO00O [0 ])#line:1239
        else :#line:1240
            O000O00OO00O0O0OO +='{:.0f}% remaining'.format (max (0 ,O00O0O0OOO0OO0O00 -100 /O0OO00O00OO0O0O0O ))#line:1241
        with O0OOO0000O0O0OO00 :#line:1243
            clear_output ()#line:1244
            print (O000O00OO00O0O0OO )#line:1245
        return #line:1246
    OO0O0000O000O000O =widgets .Button (description ="submit")#line:1248
    OO0O0000O000O000O .on_click (O0OOOO00O00OOOO0O )#line:1249
    return widgets .VBox ([OO0OOO000O00O0OOO ,OO000O0OOOOOO000O ,OO0O0000O000O000O ,O0OOO0000O0O0OO00 ])#line:1250
def runq1 ():#line:1257
    OO0OOOOO00000O0O0 =1 #line:1258
    O0OOO00OO0OOO00OO =create_multipleChoice_widget (OO0OOOOO00000O0O0 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1259
    display (O0OOO00OO0OOO00OO )#line:1260
def runQ1 ():#line:1270
    OO0O000000OOOOO00 =1 #line:1271
    OO00000O0OOO00O0O =create_multipleChoice_widget (OO0O000000OOOOO00 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1272
    display (OO00000O0OOO00O0O )#line:1273
def runQ2x ():#line:1282
    O0OO0OOOOO0OOO0OO =2 #line:1283
    OOO0OOO0O0O00OO00 =create_multipleChoice_widget (O0OO0OOOOO0OOO0OO ,'',['centred','backwards','forwards'],'centred')#line:1284
    display (OOO0OOO0O0O00OO00 )#line:1285
def runQ3x ():#line:1293
    OOO0O0OO000O00O0O =3 #line:1294
    OO0OOOO0O00O00O0O =create_multipleChoice_widget (OOO0O0OO000O00O0O ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1295
    display (OO0OOOO0O00O00O0O )#line:1296
def runQ4x ():#line:1305
    O0O0OOOOOOO0000O0 =4 #line:1306
    O000OO00OO0OOO0OO =create_multipleChoice_widget (O0O0OOOOOOO0000O0 ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1307
    display (O000OO00OO0OOO0OO )#line:1308
def runQ5x ():#line:1318
    O00000OO00000OOOO =5 #line:1319
    OO0OO000OO0OOO000 =create_multipleChoice_widget (O00000OO00000OOOO ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1320
    display (OO0OO000OO0OOO000 )#line:1321
def runQ6x ():#line:1330
    OO0O0O0OO0OO0O00O =6 #line:1331
    OO0OO00OO00O00OO0 =create_multipleChoice_widget (OO0O0O0OO0OO0O00O ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1332
    display (OO0OO00OO00O00OO0 )#line:1333
def runQ7x ():#line:1342
    OOO00000000O00000 =7 #line:1343
    O00000OO0O0OO0O00 =create_multipleChoice_widget (OOO00000000O00000 ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1344
    display (O00000OO0O0OO0O00 )#line:1345
