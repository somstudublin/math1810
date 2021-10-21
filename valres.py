import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (O0O00OOOOOO0OOOO0 ,OO0OOOO0OO0OO0000 ):#line:10
        print ("\nPasswords may not be changed using this notebook at present.")#line:14
ps =[]#line:18
wd =''#line:19
def a1 ():#line:36
    global ps #line:38
    OOOOOOO0OO0000OOO =".a1_counter.npy"#line:41
    OO00OO0OO00O0000O =np .zeros (1 ,dtype ='int8,bool')#line:42
    OO0O00OOOOO00O0OO =0 #line:44
    O0OOO0OOOOO0O00O0 =ps [0 ]#line:45
    O00000OO0O0000O00 =ps [1 ]#line:46
    if (waiter ()):#line:48
        while True :#line:49
            try :#line:50
                printmd ('**CA** (2%)')#line:51
                print (O0OOO0OOOOO0O00O0 ,"+",O00000OO0O0000O00 )#line:52
                O0O0000O00000OOOO =float (input ("Please enter your answer here: "))#line:53
                O00O0000OOOO0000O =O0OOO0OOOOO0O00O0 +O00000OO0O0000O00 #line:54
                OO0O00OOO0O00O000 =np .isclose (O0O0000O00000OOOO ,O00O0000OOOO0000O ,OO0O00OOOOO00O0OO )#line:55
                if OO0O00OOO0O00O000 :#line:56
                    print ("Well done, right answer is ",O00O0000OOOO0000O )#line:57
                else :#line:58
                    print ("Not right yet. Take another look then run this cell again.")#line:59
                OO00OO0OO00O0000O =trycount (OOOOOOO0OO0000OOO ,OO0O00OOO0O00O000 )#line:61
                OO0OO00O0O0000OOO =100 -(OO00OO0OO00O0000O [0 ]-1 )*10 #line:62
                if OO00OO0OO00O0000O [1 ]:#line:63
                    print ("First success after ",OO00OO0OO00O0000O [0 ]," tries, you have ",OO0OO00O0O0000OOO ,"% on this exercise.")#line:64
                else :#line:65
                    print ("You have had ",OO00OO0OO00O0000O [0 ]," tries.")#line:66
                    print ("If next try is accepted you will achieve ",OO0OO00O0O0000OOO -10 ,"% on this exercise.")#line:67
                break #line:69
            except ValueError :#line:71
                print ("I didn't understand that.")#line:72
                continue #line:73
        return #line:75
def a2_notlive (O0OO00OOO0OO0OO00 ):#line:84
    global ps #line:86
    OOOO0O0000O000O0O =".a2_counter.npy"#line:89
    O00O0OO00000000O0 =np .zeros (1 ,dtype ='int8,bool')#line:90
    O00O0OO0000O0OO00 =6 #line:93
    O000OO0OO00OO00OO =7 #line:94
    O000O0OO000OOO00O =0 #line:96
    OOOO0O0OO00000OO0 =(ps [O00O0OO0000O0OO00 ])%6 +1 #line:98
    O0OO00OO00OO00000 =(ps [O000OO0OO00OO00OO ])%6 +1 #line:99
    while OOOO0O0OO00000OO0 +O0OO00OO00OO00000 ==7 or OOOO0O0OO00000OO0 ==O0OO00OO00OO00000 :#line:100
        O0OO00OO00OO00000 +=1 #line:101
        O0OO00OO00OO00000 =O0OO00OO00OO00000 %6 +1 #line:102
    if (O0OO00OOO0OO0OO00 ):#line:104
        printmd ('**CA** (2%)')#line:105
        print ("Run your program (when you are happy it is working correctly) for a=",OOOO0O0OO00000OO0 ," and b=",O0OO00OO00OO00000 )#line:106
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:107
        return #line:108
    if (waiter ()):#line:110
        while True :#line:111
            try :#line:112
                print ("Enter your program's result for a=",OOOO0O0OO00000OO0 ," and b=",O0OO00OO00OO00000 )#line:113
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:114
                OOO00O00OO00OO000 =float (input ("Please enter your answer here: "))#line:115
                OOO0O00OO0O000O0O =(3 *(OOOO0O0OO00000OO0 **3 *O0OO00OO00OO00000 -OOOO0O0OO00000OO0 *O0OO00OO00OO00000 **3 ))%7 #line:116
                O0000O0O0O0O0OOO0 =np .isclose (OOO00O00OO00OO000 ,OOO0O00OO0O000O0O ,O000O0OO000OOO00O )#line:117
                if O0000O0O0O0O0OOO0 :#line:118
                    print ("Well done, right answer is ",OOO0O00OO0O000O0O )#line:119
                else :#line:120
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:121
                O00O0OO00000000O0 =trycount (OOOO0O0000O000O0O ,O0000O0O0O0O0OOO0 )#line:123
                O0000000O0O00O00O =100 -(O00O0OO00000000O0 [0 ]-1 )*10 #line:124
                if O00O0OO00000000O0 [1 ]:#line:125
                    print ("First success after ",O00O0OO00000000O0 [0 ]," tries, you have ",O0000000O0O00O00O ,"% on this exercise.")#line:126
                else :#line:127
                    print ("You have had ",O00O0OO00000000O0 [0 ]," tries.")#line:128
                    print ("If next try is accepted you will achieve ",O0000000O0O00O00O -10 ,"% on this exercise.")#line:129
                break #line:131
            except ValueError :#line:133
                print ("I didn't understand that.")#line:134
                continue #line:135
        return #line:137
def a3_notlive (O0O00O0OOOO00OO0O ):#line:146
    global ps #line:148
    O00OOOOO000OO0OOO =".a3_counter.npy"#line:151
    O0O0OO00OOOO0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:152
    O0OOO00OO000000O0 =23 #line:155
    OOO0OO0O0O0OO0O0O =24 #line:156
    O00OO0O00O0O00000 =(ps [O0OOO00OO000000O0 ])%6 +1 #line:157
    OO0OO00OOOO00000O =(ps [OOO0OO0O0O0OO0O0O ])%6 +1 #line:158
    O00000000O00O0000 =0 #line:160
    O00OO0O00O0O00000 =10 *O00OO0O00O0O00000 +OO0OO00OOOO00000O ;#line:162
    if (O0O00O0OOOO00OO0O ):#line:164
        printmd ('**CA** (6%)')#line:165
        print ("Run your program for ",O00OO0O00O0O00000 ,"people")#line:166
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:167
        return #line:168
    if (waiter ()):#line:170
        while True :#line:171
            try :#line:172
                print ("Enter your program's result for",O00OO0O00O0O00000 ,"people")#line:173
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:174
                OO0000O00OOOOOOO0 =float (input ("Please enter your answer here: "))#line:175
                O00O0O0O0O000OOOO =O00OO0O00O0O00000 +2 *O00OO0O00O0O00000 +2 *O00OO0O00O0O00000 +10 *O00OO0O00O0O00000 #line:176
                O0O00OOOOOO0O00O0 =np .isclose (OO0000O00OOOOOOO0 ,O00O0O0O0O000OOOO ,O00000000O00O0000 )#line:177
                if O0O00OOOOOO0O00O0 :#line:178
                    print ("Well done, right answer is ",O00O0O0O0O000OOOO )#line:179
                else :#line:180
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:181
                O0O0OO00OOOO0OO0O =trycount (O00OOOOO000OO0OOO ,O0O00OOOOOO0O00O0 )#line:183
                OOO0O000O00O000OO =100 -(O0O0OO00OOOO0OO0O [0 ]-1 )*10 #line:184
                if O0O0OO00OOOO0OO0O [1 ]:#line:185
                    print ("First success after ",O0O0OO00OOOO0OO0O [0 ]," tries, you have ",OOO0O000O00O000OO ,"% on this exercise.")#line:186
                else :#line:187
                    print ("You have had ",O0O0OO00OOOO0OO0O [0 ]," tries.")#line:188
                    print ("If next try is accepted you will achieve ",OOO0O000O00O000OO -10 ,"% on this exercise.")#line:189
                break #line:191
            except ValueError :#line:193
                print ("I didn't understand that.")#line:194
                continue #line:195
        return #line:197
def a4_notlive (OO0OO000O00OO000O ):#line:208
        import random #line:210
        import requests #line:211
        global ps #line:213
        global wd #line:214
        OO0000OOO0000OO0O =".a4_counter.npy"#line:217
        OO0O00O0O0OOOOOO0 =np .zeros (1 ,dtype ='int8,bool')#line:218
        O000OOO0O0O00OOOO =60 #line:221
        O0O0O0O00O0OO0O0O =61 #line:222
        O0OOOO0O00O000O00 =62 #line:223
        OOO0OO00000000O00 =63 #line:224
        O00000OO00OOOO000 =64 #line:225
        OO0OOOO0OO0000O0O =0 #line:228
        if (OO0OO000O00OO000O ):#line:230
                OOO0OOOOOOO0O0000 ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:232
                OOOOO0000O00OOO0O =requests .get (OOO0OOOOOOO0O0000 )#line:234
                OO0O0O0OOO0000OO0 =OOOOO0000O00OOO0O .content .splitlines ()#line:235
                random .seed (10 *ps [62 ]+ps [63 ])#line:236
                OO00OOO00OOO0O0O0 =4 +(10 *ps [64 ]+ps [65 ])%4 #line:237
                OOOO00O00OOO00O0O =True #line:238
                while OOOO00O00OOO00O0O :#line:239
                        OOO00O00O0OOO0O0O =OO0O0O0OOO0000OO0 [random .randint (0 ,len (OO0O0O0OOO0000OO0 )-1 )].decode ("utf-8")#line:240
                        if len (OOO00O00O0OOO0O0O )>7 and len (OOO00O00O0OOO0O0O )<14 and OOO00O00O0OOO0O0O [0 ].islower ():#line:242
                                OOOO00O00OOO00O0O =False #line:243
                                for OO0O0OO000O0OO0OO in OOO00O00O0OOO0O0O :#line:244
                                        if chr (ord (OO0O0OO000O0OO0OO )+OO00OOO00OOO0O0O0 )>'z':#line:245
                                                OOOO00O00OOO00O0O =True #line:246
                O0O000OOOO0O0OO0O =len (OOO00O00O0OOO0O0O )#line:248
                O0000OOOOO00OO0OO =''#line:249
                for OOOO00OO00O0O00O0 in range (0 ,O0O000OOOO0O0OO0O ):#line:250
                        O0000OOOOO00OO0OO +=chr (ord (OOO00O00O0OOO0O0O [OOOO00OO00O0O00O0 ])+OO00OOO00OOO0O0O0 )#line:252
                print ('Your encoded word is',O0000OOOOO00OO0OO )#line:254
                print ('Write your program in the cell below this one.\n')#line:255
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:257
                wd =OOO00O00O0OOO0O0O #line:258
                return #line:259
        if (waiter ()):#line:261
                while True :#line:262
                        try :#line:263
                                printmd ('**CA** (6%)')#line:264
                                OOOO000O00OOOO0OO =str (input ("Enter your DECODED word here: "))#line:265
                                O00O0O0OOO0OOO000 =wd #line:266
                                OOOO0OO0OOO0O000O =OOOO000O00OOOO0OO ==O00O0O0OOO0OOO000 #line:267
                                if OOOO0OO0OOO0O000O :#line:268
                                        print ("Well done, right answer is ",O00O0O0OOO0OOO000 )#line:269
                                else :#line:270
                                        print ("Not right yet. Take another look then run this cell again.")#line:271
                                OO0O00O0O0OOOOOO0 =trycount (OO0000OOO0000OO0O ,OOOO0OO0OOO0O000O )#line:273
                                O0O000OOO0OOOOOO0 =100 -(OO0O00O0O0OOOOOO0 [0 ]-1 )*10 #line:274
                                if OO0O00O0O0OOOOOO0 [1 ]:#line:275
                                        print ("First success after ",OO0O00O0O0OOOOOO0 [0 ]," tries, you have ",O0O000OOO0OOOOOO0 ,"% on this exercise.")#line:276
                                else :#line:277
                                        print ("You have had ",OO0O00O0O0OOOOOO0 [0 ]," tries.")#line:278
                                        print ("If next try is accepted you will achieve ",O0O000OOO0OOOOOO0 -10 ,"% on this exercise.")#line:279
                                break #line:280
                        except ValueError :#line:282
                                print ("I didn't understand that.")#line:283
                                continue #line:284
                return #line:286
def a5_notlive (OO0O0O0OO0OOO000O ):#line:296
        import random #line:298
        import requests #line:299
        global ps #line:301
        global P0 #line:302
        OOO0O00OOO00O0000 =".a5_counter.npy"#line:306
        O0O00O0O0OOO00OO0 =np .zeros (1 ,dtype ='int8,bool')#line:307
        O0000O0OO0000OOOO =70 #line:310
        O0O000O000OO000OO =71 #line:311
        O0OO0OO00O0OOO0OO =72 #line:312
        OOOOOOO00O00O00O0 =73 #line:313
        O0O00O0O00000000O =74 #line:314
        O00OOOO00O00O0OO0 =0 #line:317
        if (OO0O0O0OO0OOO000O ):#line:319
                P0 =[]#line:320
                O0O00O00O0OO0O0O0 =7 +(10 *ps [O0000O0OO0000OOOO ]+ps [O0O000O000OO000OO ])%4 #line:321
                for O0000O0O0O0O0OO0O in range (O0O00O00O0OO0O0O0 ):#line:322
                        P0 .append (max (0 ,ps [O0OO0OO00O0OOO0OO +O0000O0O0O0O0OO0O ]-1 ))#line:323
                print ('Run your program for the list below:\n',P0 )#line:324
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:326
        elif (waiter ()):#line:328
                while True :#line:329
                        try :#line:330
                                printmd ('**CA** (6%)')#line:333
                                O00O000OO0OOO0000 =eval (input ("Enter your list here: "))#line:334
                                OO00OOOO0OOO00O0O =3 #line:339
                                OO000OO00OOOO000O =P0 .copy ()#line:340
                                OO000OO00OOOO000O .append (0 )#line:341
                                print (OO000OO00OOOO000O )#line:342
                                O0O00O00O0OO0O0O0 =len (P0 )#line:343
                                for O000O00O0O00OOOO0 in range (OO00OOOO0OOO00O0O ):#line:344
                                        for O0000O0O0O0O0OO0O in range (O0O00O00O0OO0O0O0 ):#line:345
                                                OO000OO00OOOO000O [O0000O0O0O0O0OO0O ]=OO000OO00OOOO000O [O0000O0O0O0O0OO0O +1 ]*(O0000O0O0O0O0OO0O +1 )#line:347
                                OO000OO00OOOO000O .pop ()#line:348
                                OOO00OOO00OO000OO =OO000OO00OOOO000O #line:351
                                if not type (O00O000OO0OOO0000 )==type (OOO00OOO00OO000OO ):#line:353
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:354
                                elif not len (O00O000OO0OOO0000 )==len (OOO00OOO00OO000OO ):#line:355
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:356
                                else :#line:357
                                        OO000O0O0OO000OO0 =O00O000OO0OOO0000 ==OOO00OOO00OO000OO #line:358
                                        if OO000O0O0OO000OO0 :#line:359
                                                print ("Well done, right answer is ",OOO00OOO00OO000OO )#line:360
                                        else :#line:361
                                                print ("Not right yet. Take another look then run this cell again.")#line:362
                                        O0O00O0O0OOO00OO0 =trycount (OOO0O00OOO00O0000 ,OO000O0O0OO000OO0 )#line:364
                                        O0OOO00OOO00000OO =100 -(O0O00O0O0OOO00OO0 [0 ]-1 )*10 #line:365
                                        if O0O00O0O0OOO00OO0 [1 ]:#line:366
                                                print ("First success after ",O0O00O0O0OOO00OO0 [0 ]," tries, you have ",O0OOO00OOO00000OO ,"% on this exercise.")#line:367
                                        else :#line:368
                                                print ("You have had ",O0O00O0O0OOO00OO0 [0 ]," tries.")#line:369
                                                print ("If next try is accepted you will achieve ",O0OOO00OOO00000OO -10 ,"% on this exercise.")#line:370
                                        break #line:371
                                OO000OO00OOOO000O =None #line:374
                                OOO00OOO00OO000OO =None #line:375
                        except ValueError :#line:376
                                print ("I didn't understand that.")#line:377
                                continue #line:378
        return #line:380
def a6_notlive (O0OOO000OOO0OO00O ):#line:389
        import random #line:391
        import requests #line:392
        global ps #line:394
        global P0 #line:395
        OO0OO0O0OO0OO0000 =".a6_counter.npy"#line:399
        O0OOOOO00OO0OO00O =np .zeros (1 ,dtype ='int8,bool')#line:400
        OOO0O00OOO000O00O =11 #line:403
        OO00OO000O00O00OO =16 #line:404
        O0000OOO00O000000 =7 #line:405
        OO0OO00O0O0O0O00O =33 #line:406
        OOOO00O0OOO0O0OO0 =21 #line:407
        O0OO00OO0O0OOOO0O =0 #line:410
        if (O0OOO000OOO0OO00O ):#line:412
                OOOOOOOO000OO00O0 =ps [OOO0O00OOO000O00O ]+ps [OO00OO000O00O00OO ]+ps [O0000OOO00O000000 ]+ps [OO0OO00O0O0O0O00O ]+ps [OOOO00O0OOO0O0OO0 ]#line:413
                random .seed (OOOOOOOO000OO00O0 )#line:414
                P0 =random .randint (1000 ,2000 )#line:415
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:416
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:418
        elif (waiter ()):#line:420
                while True :#line:421
                        try :#line:422
                                printmd ('**CA** (6%)')#line:425
                                O0000O0O0OO0OOOOO =eval (input ("Enter your stopping number here: "))#line:426
                                OO0OOOO00OOOOO0OO =P0 #line:430
                                OO000O00O0OOOO00O =[OO0OOOO00OOOOO0OO ]#line:431
                                while not OO0OOOO00OOOOO0OO ==1 :#line:432
                                        if OO0OOOO00OOOOO0OO %2 :#line:433
                                                OO0OOOO00OOOOO0OO =3 *OO0OOOO00OOOOO0OO +1 #line:434
                                        else :#line:435
                                                OO0OOOO00OOOOO0OO =OO0OOOO00OOOOO0OO //2 #line:436
                                        OO000O00O0OOOO00O .append (OO0OOOO00OOOOO0OO )#line:437
                                O00O0OO0O00O0OO00 =len (OO000O00O0OOOO00O )#line:438
                                O0OO00O00O0O0OOOO =O00O0OO0O00O0OO00 #line:442
                                if not type (O0000O0O0OO0OOOOO )==type (O0OO00O00O0O0OOOO ):#line:444
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:445
                                else :#line:448
                                        OOO0O0O00O0O00000 =O0000O0O0OO0OOOOO ==O0OO00O00O0O0OOOO #line:449
                                        if OOO0O0O00O0O00000 :#line:450
                                                print ("Well done, right answer is ",O0OO00O00O0O0OOOO )#line:451
                                        else :#line:452
                                                print ("Not right yet. Take another look then run this cell again.")#line:453
                                        O0OOOOO00OO0OO00O =trycount (OO0OO0O0OO0OO0000 ,OOO0O0O00O0O00000 )#line:455
                                        OOOO0O0OOOO0O0OOO =100 -(O0OOOOO00OO0OO00O [0 ]-1 )*10 #line:456
                                        if O0OOOOO00OO0OO00O [1 ]:#line:457
                                                print ("First success after ",O0OOOOO00OO0OO00O [0 ]," tries, you have ",OOOO0O0OOOO0O0OOO ,"% on this exercise.")#line:458
                                        else :#line:459
                                                print ("You have had ",O0OOOOO00OO0OO00O [0 ]," tries.")#line:460
                                                print ("If next try is accepted you will achieve ",OOOO0O0OOOO0O0OOO -10 ,"% on this exercise.")#line:461
                                        break #line:462
                                O00O0OO0O00O0OO00 =None #line:465
                                O0OO00O00O0O0OOOO =None #line:466
                        except ValueError :#line:467
                                print ("I didn't understand that.")#line:468
                                continue #line:469
        return #line:471
def a7_notlive (O0000000O0O00OO00 ):#line:481
        O0O0OOOOO0O000OOO =".a7_counter.npy"#line:485
        OOOO00000OOOOOOOO =np .zeros (1 ,dtype ='int8,bool')#line:486
        def O0OOOO000OO0O0O0O ():#line:488
                pass #line:489
        OO0OO0OOO00O0O0OO =[(30 ,10 )]#line:492
        O00OOO00O00O00O00 =1.0e-4 #line:495
        if (waiter ()):#line:498
                printmd ('**CA** (6%)')#line:500
                if not type (O0000000O0O00OO00 )==type (O0OOOO000OO0O0O0O ):#line:502
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:503
                else :#line:506
                        def O0OOOO000O0000O00 (O0O000OO0O000OOOO ,O0OO000OO0O0OOO0O ):#line:509
                                import math #line:510
                                OO0OOO0O0O0OOO0O0 =9.81 #line:511
                                O0O0OO00000000OO0 =math .pi *O0OO000OO0O0OOO0O /180. #line:512
                                O00OOO0000OO0O0O0 =O0O000OO0O000OOOO **2 *math .sin (2 *O0O0OO00000000OO0 )/OO0OOO0O0O0OOO0O0 #line:513
                                OO000OO0OO0000O0O =O0O000OO0O000OOOO **2 *(math .sin (O0O0OO00000000OO0 ))**2 /(2. *OO0OOO0O0O0OOO0O0 )#line:514
                                return O00OOO0000OO0O0O0 ,OO000OO0OO0000O0O #line:515
                        import random as r #line:518
                        OO0OO0OOO00O0O0OO =[]#line:519
                        O0O00O0000OOO0O00 =False #line:520
                        OOO0OOOO00000O000 =[]#line:521
                        OO0OOO00O0OO000OO =10 #line:522
                        O0O0OOO00O0OO0OO0 =100 #line:523
                        OO0O0000O0OO0OO00 =5 #line:524
                        OO0OO0OO0OO0OO0OO =85 #line:525
                        for OO0O000000OOO0OO0 in range (5 ):#line:526
                                OO0OO0OOO00O0O0OO .append ((r .uniform (OO0OOO00O0OO000OO ,O0O0OOO00O0OO0OO0 ),r .uniform (OO0O0000O0OO0OO00 ,OO0OO0OO0OO0OO0OO )))#line:527
                        for (O000OO000OOOO0O0O ,OO0000OOOO0O000O0 )in OO0OO0OOO00O0O0OO :#line:528
                                print ('Testing:',O000OO000OOOO0O0O ,OO0000OOOO0O000O0 )#line:529
                                O0O0O0O000O000O00 =O0000000O0O00OO00 (O000OO000OOOO0O0O ,OO0000OOOO0O000O0 )#line:530
                                print ('Output:',*O0O0O0O000O000O00 )#line:531
                                OO0OO0O000OO000OO =O0OOOO000O0000O00 (O000OO000OOOO0O0O ,OO0000OOOO0O000O0 )#line:532
                                print ('Actual:',*OO0OO0O000OO000OO )#line:533
                                print ()#line:534
                                if (not type (O0O0O0O000O000O00 )==type (OO0OO0O000OO000OO ))or (not len (O0O0O0O000O000O00 )==len (OO0OO0O000OO000OO )):#line:535
                                        if O0O00O0000OOO0O00 ==False :#line:536
                                           O0O00O0000OOO0O00 =True #line:537
                                else :#line:538
                                        OOO0OOOO00000O000 .append (all (np .isclose (O0O0O0O000O000O00 ,OO0OO0O000OO000OO ,O00OOO00O00O00O00 )))#line:539
                        if O0O00O0000OOO0O00 :#line:541
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:542
                        else :#line:544
                                OO000000O00O00OOO =all (OOO0OOOO00000O000 )#line:545
                                if OO000000O00O00OOO :#line:546
                                        print ("Well done, all correct.")#line:547
                                else :#line:548
                                        print ("Not right yet. Take another look then run this cell again.")#line:549
                                OOOO00000OOOOOOOO =trycount (O0O0OOOOO0O000OOO ,OO000000O00O00OOO )#line:551
                                O0O0OOOO0O0O0OO00 =100 -(OOOO00000OOOOOOOO [0 ]-1 )*10 #line:552
                                if OOOO00000OOOOOOOO [1 ]:#line:553
                                        print ("First success after ",OOOO00000OOOOOOOO [0 ]," tries, you have ",O0O0OOOO0O0O0OO00 ,"% on this exercise.")#line:554
                                else :#line:555
                                        print ("You have had ",OOOO00000OOOOOOOO [0 ]," tries.")#line:556
                                        print ("If next try is accepted you will achieve ",O0O0OOOO0O0O0OO00 -10 ,"% on this exercise.")#line:557
                        OO0OO0O000OO000OO =None #line:560
                        O0OOOO000O0000O00 =None #line:561
        return #line:563
def a8_notlive (O0OOOO0OOO0OO0O00 ):#line:573
        OO00000O00000OO00 =".a8_counter.npy"#line:577
        OO0OO0000OO0O00O0 =np .zeros (1 ,dtype ='int8,bool')#line:578
        def O0OOOOO0OOO00OOOO ():#line:580
                pass #line:581
        OO00000OO0O0OOOO0 =1.0e-4 #line:585
        if (waiter ()):#line:588
                printmd ('**CA** (6%)')#line:590
                if not type (O0OOOO0OOO0OO0O00 )==type (O0OOOOO0OOO00OOOO ):#line:594
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:595
                else :#line:599
                        import inspect #line:602
                        OO00OOOO00OO000OO =inspect .getsourcelines (O0OOOO0OOO0OO0O00 )#line:603
                        O0O0OO0O000O00OO0 =True #line:604
                        O000OOO0OO0OO00OO =[]#line:605
                        for OO000O00O0O0O0000 ,OO00O000OO000O00O in enumerate (OO00OOOO00OO000OO [0 ]):#line:606
                                if 'for'in OO00O000OO000O00O or 'while'in OO00O000OO000O00O :#line:607
                                        O0O0OO0O000O00OO0 =False #line:609
                                        O000OOO0OO0OO00OO .append (OO000O00O0O0O0000 )#line:610
                        if not O0O0OO0O000O00OO0 :#line:611
                                print ('Function needs to be written without loops (using NumPy), check lines',*O000OOO0OO0OO00OO )#line:612
                                print ('No marks lost for this attempt.')#line:613
                                return #line:614
                        def OO000OOOO0000OO0O (OO0OOOO00OO00O0O0 ):#line:617
                                OOO0000O00O0000O0 =np .vstack ((OO0OOOO00OO00O0O0 ,OO0OOOO00OO00O0O0 [0 ]))#line:618
                                O000OOOO0O00OOO00 =sum (OOO0000O00O0000O0 [:-1 ,0 ]*OOO0000O00O0000O0 [1 :,1 ])#line:619
                                OOO00O000OO00O00O =sum (OOO0000O00O0000O0 [:-1 ,1 ]*OOO0000O00O0000O0 [1 :,0 ])#line:620
                                return abs (O000OOOO0O00OOO00 -OOO00O000OO00O00O )/2 #line:621
                        import random as r #line:624
                        OOOOOOOO000O00O00 =r .randint (6 ,11 )#line:625
                        OOOO00O0OOOOOOOO0 =np .ones ((OOOOOOOO000O00O00 ,2 ))#line:626
                        O00O0O0000O0OO000 =False #line:627
                        OO00O0O0OO0O0OO00 =[]#line:628
                        OOOOO00000O000O0O =1. #line:629
                        OOO0OO0000O00OOOO =20. #line:630
                        OOO00OOOO0000OOO0 =OOOOO00000O000O0O #line:631
                        OO00OO0OOOOO0OOO0 =OOO0OO0000O00OOOO #line:632
                        for O0O0O0O0OO000O000 in range (OOOOOOOO000O00O00 ):#line:633
                                OOOO00O0OOOOOOOO0 [O0O0O0O0OO000O000 ]=[r .uniform (OOOOO00000O000O0O ,OOO0OO0000O00OOOO ),r .uniform (OOO00OOOO0000OOO0 ,OO00OO0OOOOO0OOO0 )]#line:634
                        print ('Testing:',OOOO00O0OOOOOOOO0 )#line:635
                        OOO0000O0OO0O00OO =O0OOOO0OOO0OO0O00 (OOOO00O0OOOOOOOO0 )#line:636
                        print ('Output:',OOO0000O0OO0O00OO )#line:637
                        OO0OOOOO0OO0OO000 =OO000OOOO0000OO0O (OOOO00O0OOOOOOOO0 )#line:638
                        print ('Actual:',OO0OOOOO0OO0OO000 )#line:639
                        print ()#line:640
                        if not type (OOO0000O0OO0O00OO )==type (OO0OOOOO0OO0OO000 ):#line:641
                                if O00O0O0000O0OO000 ==False :#line:642
                                        O00O0O0000O0OO000 =True #line:643
                        else :#line:644
                                OO00O0O0OO0O0OO00 .append (np .isclose (OOO0000O0OO0O00OO ,OO0OOOOO0OO0OO000 ,OO00000OO0O0OOOO0 ))#line:645
                        if O00O0O0000O0OO000 :#line:647
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:648
                        else :#line:650
                                O00O0O00OOO0O0O0O =all (OO00O0O0OO0O0OO00 )#line:651
                                if O00O0O00OOO0O0O0O :#line:652
                                        print ("Well done, all correct.")#line:653
                                else :#line:654
                                        print ("Not right yet. Take another look then run this cell again.")#line:655
                                OO0OO0000OO0O00O0 =trycount (OO00000O00000OO00 ,O00O0O00OOO0O0O0O )#line:657
                                O00000OOO00O0OO00 =100 -(OO0OO0000OO0O00O0 [0 ]-1 )*10 #line:658
                                if OO0OO0000OO0O00O0 [1 ]:#line:659
                                        print ("First success after ",OO0OO0000OO0O00O0 [0 ]," tries, you have ",O00000OOO00O0OO00 ,"% on this exercise.")#line:660
                                else :#line:661
                                        print ("You have had ",OO0OO0000OO0O00O0 [0 ]," tries.")#line:662
                                        print ("If next try is accepted you will achieve ",O00000OOO00O0OO00 -10 ,"% on this exercise.")#line:663
                        OO0OOOOO0OO0OO000 =None #line:666
                        OO000OOOO0000OO0O =None #line:667
        return #line:669
def a1_notlive ():#line:685
        print ('This CA test is not currently live.')#line:686
        return #line:687
def a2 (O0OOOO0OO00OOO00O ):#line:695
        print ('This CA test is not currently live.')#line:696
        return #line:697
def a3 (OO0000000O0O0O00O ):#line:705
        print ('This CA test is not currently live.')#line:706
        return #line:707
def a4 (OOO0O0OO0OOOOOOOO ):#line:715
        print ('This CA test is not currently live.')#line:716
        return #line:717
def a5 (OO000O00OOO00OO00 ):#line:725
        print ('This CA test is not currently live.')#line:726
        return #line:727
def a6 (OOO0O0OOO0O000OOO ):#line:735
        print ('This CA test is not currently live.')#line:736
        return #line:737
def a7 ():#line:745
        print ('This CA test is not currently live.')#line:746
        return #line:747
def a8 (O0OO0O00O0OO00O00 ):#line:755
        print ('This CA test is not currently live.')#line:756
        return #line:757
def b1 ():#line:775
    global ps #line:777
    OOO00OOOOOOO00O0O =".b1_counter.npy"#line:780
    OO00OOO0OO000O00O =np .zeros (1 ,dtype ='int8,bool')#line:781
    O0O0O0OOOOOO0000O =0.05 #line:783
    if (waiter ()):#line:785
        while True :#line:786
            try :#line:787
                printmd ('**CA**')#line:788
                OOO0O00O0OO00OOO0 =eval (input ("Please enter your answer here in the format D,k: "))#line:789
                OOO0OO00O0O00O00O =(0.025 ,2.0 )#line:790
                OOOOOOOO0OOOOO0O0 =all (np .isclose (OOO0O00O0OO00OOO0 ,OOO0OO00O0O00O00O ,rtol =O0O0O0OOOOOO0000O ))#line:791
                if OOOOOOOO0OOOOO0O0 :#line:792
                    print ("Well done, reasonable estimate is ",OOO0OO00O0O00O00O )#line:793
                else :#line:794
                    print ("Not right yet. Take another look then run this cell again.")#line:795
                OO00OOO0OO000O00O =trycount (OOO00OOOOOOO00O0O ,OOOOOOOO0OOOOO0O0 )#line:797
                O0000OOO0000OOOO0 =100 -(OO00OOO0OO000O00O [0 ]-1 )*10 #line:798
                if OO00OOO0OO000O00O [1 ]:#line:799
                    print ("First success after ",OO00OOO0OO000O00O [0 ]," tries, you have ",O0000OOO0000OOOO0 ,"% on this exercise.")#line:800
                else :#line:801
                    print ("You have had ",OO00OOO0OO000O00O [0 ]," tries.")#line:802
                    print ("If next try is accepted you will achieve ",O0000OOO0000OOOO0 -10 ,"% on this exercise.")#line:803
                break #line:805
            except ValueError :#line:807
                print ("I didn't understand that.")#line:808
                continue #line:809
        return #line:811
def b2 (O00O000O00OOOO0O0 ):#line:821
        OOO000O0000O0O0O0 =".b2_counter.npy"#line:825
        OOO00O0000O0O000O =np .zeros (1 ,dtype ='int8,bool')#line:826
        def OOOOOO0OO0O0O0O0O ():#line:828
                pass #line:829
        O0OOO0000O0O0O000 =1.0e-2 #line:832
        OO00O00OOOOOO0OOO =0.0 #line:833
        if (waiter ()):#line:835
                printmd ('**CA**')#line:837
                if not type (O00O000O00OOOO0O0 )==type (OOOOOO0OO0O0O0O0O ):#line:839
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:840
                else :#line:843
                        def O0O0OO0OOOOO0O0O0 (O00OOO00OOO0O0O0O ):#line:847
                                OOOOO00O0OOO0OOOO =[]#line:848
                                OOOO000O0OOO0OO0O =20.0 #line:849
                                OOO000OOO00000O00 =58.1e-3 #line:850
                                O0O00000000OO0000 =9.81 #line:851
                                O000OOO0OO000O0O0 =0.0 #line:852
                                OO00OOO0OOOOOOO00 =0.0 #line:853
                                O0O00OO0OOO0O0O00 =0.0 #line:854
                                O0OO00000000O00OO =10 #line:855
                                OOO0O0O000OO000O0 =3.35e-2 #line:856
                                OOO00000O00O000OO =0.51 #line:857
                                OOO0000OOO0O0000O =1.25 #line:858
                                OOO0O00O00O0O0000 =math .pi *OOO0O0O000OO000O0 **2 #line:859
                                O00O00O0OOOO0OOOO =0.5 *OOO00000O00O000OO *OOO0O00O00O0O0000 *OOO0000OOO0O0000O #line:860
                                O0OO0O000O00000OO =100000 #line:862
                                O000O00OOOO0OO000 =np .zeros (O0OO0O000O00000OO ,float )#line:863
                                OO0O0OO000O000000 =np .zeros (O0OO0O000O00000OO ,float )#line:864
                                OOO0OOOOOO00000O0 =np .zeros (O0OO0O000O00000OO ,float )#line:865
                                O0OO0OO00O0OO000O =np .zeros (O0OO0O000O00000OO ,float )#line:866
                                OO00O0OO0O0OO0O0O =np .zeros (O0OO0O000O00000OO ,float )#line:867
                                OO0O0000OOOO000OO =np .zeros (O0OO0O000O00000OO ,float )#line:868
                                OO0OOOO000OOOO0O0 =np .zeros (O0OO0O000O00000OO ,float )#line:869
                                O000O00OOOO0OO000 ,OO0O0000O0000OO0O =np .linspace (O0O00OO0OOO0O0O00 ,O0OO00000000O00OO ,O0OO0O000O00000OO ,retstep =True )#line:870
                                for OOO00000O00O00OOO in O00OOO00OOO0O0O0O :#line:872
                                        OO00000000OO0O0OO =OOOO000O0OOO0OO0O *math .cos (OOO00000O00O00OOO )#line:873
                                        OO0OOOO0000O00O0O =OOOO000O0OOO0OO0O *math .sin (OOO00000O00O00OOO )#line:874
                                        OO0O0000OOOO000OO [0 ]=O000OOO0OO000O0O0 #line:876
                                        OO0OOOO000OOOO0O0 [0 ]=OO00OOO0OOOOOOO00 #line:877
                                        O0OO0OO00O0OO000O [0 ]=OO00000000OO0O0OO #line:878
                                        OO00O0OO0O0OO0O0O [0 ]=OO0OOOO0000O00O0O #line:879
                                        for O000000OO0O0000OO in range (O0OO0O000O00000OO -1 ):#line:880
                                                O0O0OO00O00OOO0OO =math .sqrt (O0OO0OO00O0OO000O [O000000OO0O0000OO ]**2 +OO00O0OO0O0OO0O0O [O000000OO0O0000OO ]**2 )#line:881
                                                O0O0000O0OO0OO00O =-O00O00O0OOOO0OOOO *O0O0OO00O00OOO0OO *O0OO0OO00O0OO000O [O000000OO0O0000OO ]#line:882
                                                OO0O0OO000O000000 [O000000OO0O0000OO ]=O0O0000O0OO0OO00O /OOO000OOO00000O00 #line:883
                                                O0OO0OO00O0OO000O [O000000OO0O0000OO +1 ]=O0OO0OO00O0OO000O [O000000OO0O0000OO ]+OO0O0OO000O000000 [O000000OO0O0000OO ]*OO0O0000O0000OO0O #line:884
                                                OO0O0000OOOO000OO [O000000OO0O0000OO +1 ]=OO0O0000OOOO000OO [O000000OO0O0000OO ]+O0OO0OO00O0OO000O [O000000OO0O0000OO +1 ]*OO0O0000O0000OO0O #line:885
                                                OOOOO0O0O00OOO0OO =-OOO000OOO00000O00 *O0O00000000OO0000 -O00O00O0OOOO0OOOO *O0O0OO00O00OOO0OO *OO00O0OO0O0OO0O0O [O000000OO0O0000OO ]#line:886
                                                OOO0OOOOOO00000O0 [O000000OO0O0000OO ]=OOOOO0O0O00OOO0OO /OOO000OOO00000O00 #line:887
                                                OO00O0OO0O0OO0O0O [O000000OO0O0000OO +1 ]=OO00O0OO0O0OO0O0O [O000000OO0O0000OO ]+OOO0OOOOOO00000O0 [O000000OO0O0000OO ]*OO0O0000O0000OO0O #line:888
                                                OO0OOOO000OOOO0O0 [O000000OO0O0000OO +1 ]=OO0OOOO000OOOO0O0 [O000000OO0O0000OO ]+OO00O0OO0O0OO0O0O [O000000OO0O0000OO +1 ]*OO0O0000O0000OO0O #line:889
                                                if (OO0OOOO000OOOO0O0 [O000000OO0O0000OO +1 ]<0 ):#line:890
                                                        break #line:891
                                        OOOO000O0OOOO0O0O =O000000OO0O0000OO #line:892
                                        OOOOO00O0OOO0OOOO .append (OO0O0000OOOO000OO [OOOO000O0OOOO0O0O ])#line:893
                                return (OOOOO00O0OOO0OOOO );#line:895
                        import random as r #line:898
                        OO0OO00OOOOO0O0O0 =[]#line:899
                        O00O0OO00O0OO0O00 =False #line:900
                        OOOOO0O0OOOO0OOO0 =[]#line:901
                        OOOOO00O000O00000 =0.1 #line:902
                        O0OOO00O0O0OO000O =1.5 #line:903
                        for O0O000O00O00O000O in range (5 ):#line:904
                                OO0OO00OOOOO0O0O0 .append (r .uniform (OOOOO00O000O00000 ,O0OOO00O0O0OO000O ))#line:905
                        OO0OO00OOOOO0O0O0 .sort ()#line:906
                        print ('Testing thetas=',OO0OO00OOOOO0O0O0 )#line:907
                        OOOO00000OO00O0O0 =O00O000O00OOOO0O0 (OO0OO00OOOOO0O0O0 )#line:908
                        print ('Output ximpacts=',OOOO00000OO00O0O0 )#line:909
                        O0000O00OOOOO0O0O =O0O0OO0OOOOO0O0O0 (OO0OO00OOOOO0O0O0 )#line:910
                        print ('Actual ximpacts=',O0000O00OOOOO0O0O )#line:911
                        print ()#line:912
                        if (not type (OOOO00000OO00O0O0 )==type (O0000O00OOOOO0O0O ))or (not len (OOOO00000OO00O0O0 )==len (O0000O00OOOOO0O0O )):#line:913
                                if O00O0OO00O0OO0O00 ==False :#line:914
                                        O00O0OO00O0OO0O00 =True #line:915
                        else :#line:916
                                OOOOO0O0OOOO0OOO0 .append (all (np .isclose (OOOO00000OO00O0O0 ,O0000O00OOOOO0O0O ,rtol =O0OOO0000O0O0O000 ,atol =OO00O00OOOOOO0OOO )))#line:917
                        if O00O0OO00O0OO0O00 :#line:919
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:920
                        else :#line:922
                                O0OOO0OO0O0OO00OO =all (OOOOO0O0OOOO0OOO0 )#line:923
                                if O0OOO0OO0O0OO00OO :#line:924
                                        print ("Well done, all correct.")#line:925
                                else :#line:926
                                        print ("Not close enough. Take another look then run this cell again.")#line:927
                                OOO00O0000O0O000O =trycount (OOO000O0000O0O0O0 ,O0OOO0OO0O0OO00OO )#line:929
                                OO0OO0OO000O00OOO =100 -(OOO00O0000O0O000O [0 ]-1 )*10 #line:930
                                if OOO00O0000O0O000O [1 ]:#line:931
                                        print ("First success after ",OOO00O0000O0O000O [0 ]," tries, you have ",OO0OO0OO000O00OOO ,"% on this exercise.")#line:932
                                else :#line:933
                                        print ("You have had ",OOO00O0000O0O000O [0 ]," tries.")#line:934
                                        print ("If next try is accepted you will achieve ",OO0OO0OO000O00OOO -10 ,"% on this exercise.")#line:935
                        O0000O00OOOOO0O0O =None #line:938
                        O0O0OO0OOOOO0O0O0 =None #line:939
        return #line:941
def b3 ():#line:951
    global ps #line:953
    O0O0OO000OOO00O00 =".b3_counter.npy"#line:956
    O00OO0O0000OO00O0 =np .zeros (1 ,dtype ='int8,bool')#line:957
    OOO00OO0O0OO0O0O0 =0.01 #line:960
    if (waiter ()):#line:962
        while True :#line:963
            try :#line:964
                printmd ('**CA**')#line:965
                OOOOO0O000O0000O0 =float (input ("Enter a real number here: "))#line:966
                OOO000OO0OOO00O00 =0.5 #line:967
                O0O0OO0OO00O0OOOO =np .isclose (OOOOO0O000O0000O0 ,OOO000OO0OOO00O00 ,atol =OOO00OO0O0OO0O0O0 )#line:968
                if O0O0OO0OO00O0OOOO :#line:969
                    print ("Well done. Actual value is ",OOO000OO0OOO00O00 )#line:970
                else :#line:971
                    print ("Not right yet. Take another look then run this cell again.")#line:972
                O00OO0O0000OO00O0 =trycount (O0O0OO000OOO00O00 ,O0O0OO0OO00O0OOOO )#line:974
                O00O000O0O0O0O0OO =100 -(O00OO0O0000OO00O0 [0 ]-1 )*10 #line:975
                if O00OO0O0000OO00O0 [1 ]:#line:976
                    print ("First success after ",O00OO0O0000OO00O0 [0 ]," tries, you have ",O00O000O0O0O0O0OO ,"% on this exercise.")#line:977
                else :#line:978
                    print ("You have had ",O00OO0O0000OO00O0 [0 ]," tries.")#line:979
                    print ("If next try is accepted you will achieve ",O00O000O0O0O0O0OO -10 ,"% on this exercise.")#line:980
                break #line:982
            except ValueError :#line:984
                print ("I didn't understand that.")#line:985
                continue #line:986
        return #line:988
def b1_notlive ():#line:1000
        print ('This CA test is not currently live.')#line:1001
        return #line:1002
def b2_notlive (O0000O0O0O00O0000 ):#line:1012
        print ('This CA test is not currently live.')#line:1013
        return #line:1014
def b3_notlive ():#line:1021
        print ('This CA test is not currently live.')#line:1022
        return #line:1023
def printmd (OO0000O0OO00O00O0 ):#line:1033
    display (Markdown (OO0000O0OO00O00O0 ))#line:1034
def repeat_to_length (O000OO0O0OO00OOO0 ,OO0OO0O0OOOO0OO0O ):#line:1036
   return (O000OO0O0OO00OOO0 *((OO0OO0O0OOOO0OO0O //len (O000OO0O0OO00OOO0 ))+1 ))[:OO0OO0O0OOOO0OO0O ]#line:1037
def getco (O00OOO0O00OOO0OO0 ):#line:1039
    global ps #line:1040
    import random #line:1046
    OO0OO0O0OOO0O000O =str (random .randint (1e6 ,1e7 ))#line:1047
    OOO000O00O0O00O0O =int .from_bytes (OO0OO0O0OOO0O000O .encode (),'little')#line:1051
    OOOOOOOOO0OO0O000 =str (OOO000O00O0O00O0O )#line:1052
    OO00OOO00O00O000O =repeat_to_length (OOOOOOOOO0OO0O000 ,O00OOO0O00OOO0OO0 )#line:1053
    ps =[int (O0000OOO00OOOO0O0 )+1 for O0000OOO00OOOO0O0 in OO00OOO00O00O000O ]#line:1054
def waiter ():#line:1056
    OOOO0O0O0O0O00000 =20 #line:1059
    OO000O0OO00O0000O =".ts1.txt"#line:1061
    if os .path .isfile (OO000O0OO00O0000O ):#line:1062
        O00OO0000O0OO0O0O =np .loadtxt (OO000O0OO00O0000O )#line:1063
    else :#line:1065
        O00OO0000O0OO0O0O =0.0 #line:1066
    OO0O0O000O0000OOO =time .time ()#line:1069
    O000O0OO0000OO0OO =OO0O0O000O0000OOO -O00OO0000O0OO0O0O #line:1070
    if (O000O0OO0000OO0OO <OOOO0O0O0O0O00000 ):#line:1072
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O000O0OO0000OO0OO ,OOOO0O0O0O0O00000 ))#line:1073
        return False #line:1074
    else :#line:1075
        O0O00OOO00O0O00OO =open (OO000O0OO00O0000O ,'w')#line:1076
        O0O00OOO00O0O00OO .write (str (OO0O0O000O0000OOO ))#line:1077
        O0O00OOO00O0O00OO .close ()#line:1078
        return True #line:1079
def trycount (OO0O0O0OOOOOOO000 ,O0000OOOO0OOO0O0O ):#line:1081
    if os .path .isfile (OO0O0O0OOOOOOO000 ):#line:1083
        OO000OO0O0OO0OO00 =np .load (OO0O0O0OOOOOOO000 )#line:1084
    else :#line:1086
        OO000OO0O0OO0OO00 =np .zeros (1 ,dtype ='int8,bool')#line:1087
        OO000OO0O0OO0OO00 =[0 ,False ]#line:1088
    if not OO000OO0O0OO0OO00 [1 ]:#line:1091
        OO000OO0O0OO0OO00 [0 ]+=1 #line:1092
        OO000OO0O0OO0OO00 [1 ]=O0000OOOO0OOO0O0O #line:1093
        np .save (OO0O0O0OOOOOOO000 ,OO000OO0O0OO0OO00 )#line:1095
    return OO000OO0O0OO0OO00 #line:1097
def valdho (OOO0OO00OOOO0O00O ,O0O00O00OOO0OOOO0 ):#line:1105
    OOO0O0O000000OO0O =".dho_counter.npy"#line:1109
    O0OO00OO00OO0O000 =np .zeros (1 ,dtype ='int8,bool')#line:1111
    if (waiter ()):#line:1113
        while True :#line:1114
            try :#line:1115
                OOO0O0O0O00OO000O =float (input ("Please enter your estimate here: "))#line:1116
                OOO0000O00O000OO0 =2 *np .sqrt (OOO0OO00OOOO0O00O *O0O00O00OOO0OOOO0 )#line:1117
                OOOOOO0OOO000000O =np .isclose (OOO0O0O0O00OO000O ,OOO0000O00O000OO0 ,0.2 )#line:1118
                if OOOOOO0OOO000000O :#line:1119
                    print ("Well done, that is close to the critical damping value ",OOO0000O00O000OO0 )#line:1120
                else :#line:1121
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1122
                O0OO00OO00OO0O000 =trycount (OOO0O0O000000OO0O ,OOOOOO0OOO000000O )#line:1124
                O000OOO0O0OO00O00 =100 -(O0OO00OO00OO0O000 [0 ]-1 )*10 #line:1125
                if O0OO00OO00OO0O000 [1 ]:#line:1126
                    print ("First success after ",O0OO00OO00OO0O000 [0 ]," tries, you have ",O000OOO0O0OO00O00 ,"% on this exercise.")#line:1127
                else :#line:1128
                    print ("You have had ",O0OO00OO00OO0O000 [0 ]," tries.")#line:1129
                    print ("If next try is accepted you will achieve ",O000OOO0O0OO00O00 -10 ,"% on this exercise.")#line:1130
                break #line:1132
            except ValueError :#line:1134
                print ("I didn't understand that.")#line:1135
                continue #line:1136
        return #line:1139
def valdrivendho (OOO0O0OO0OO00OOO0 ,O0OOOO0O0O0O0OO00 ):#line:1149
    O00OOOO0000OO0OOO =".drivendho_counter.npy"#line:1153
    OO0OO00O000OOOO00 =np .zeros (1 ,dtype ='int8,bool')#line:1155
    if (waiter ()):#line:1157
        while True :#line:1158
            try :#line:1159
                OOOOOOO000O00O000 =float (input ("Please enter your estimate here: "))#line:1160
                O0O000000O0OO0O00 =np .sqrt (OOO0O0OO0OO00OOO0 **2 -2 *O0OOOO0O0O0O0OO00 **2 )#line:1161
                O0OOO00O0000OOO00 =np .isclose (OOOOOOO000O00O000 ,O0O000000O0OO0O00 ,0.2 )#line:1162
                if O0OOO00O0000OOO00 :#line:1163
                    print ("Well done, that is close to the resonance value ",O0O000000O0OO0O00 )#line:1164
                else :#line:1165
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1166
                OO0OO00O000OOOO00 =trycount (O00OOOO0000OO0OOO ,O0OOO00O0000OOO00 )#line:1168
                O00O000OO00OOOOOO =100 -(OO0OO00O000OOOO00 [0 ]-1 )*10 #line:1169
                if OO0OO00O000OOOO00 [1 ]:#line:1170
                    print ("First success after ",OO0OO00O000OOOO00 [0 ]," tries, you have ",O00O000OO00OOOOOO ,"% on this exercise.")#line:1171
                else :#line:1172
                    print ("You have had ",OO0OO00O000OOOO00 [0 ]," tries.")#line:1173
                    print ("If next try is accepted you will achieve ",O00O000OO00OOOOOO -10 ,"% on this exercise.")#line:1174
                break #line:1176
            except ValueError :#line:1178
                print ("I didn't understand that.")#line:1179
                continue #line:1180
        return #line:1183
import ipywidgets as widgets #line:1198
import sys #line:1199
from IPython .display import display #line:1200
from IPython .display import clear_output #line:1201
def create_multipleChoice_widget (OO000O0O0OOO0O000 ,OOOOOO0O000OO00OO ,OOO0OOO0OOO000OOO ,OOO00OOOOOO0OOOO0 ):#line:1203
    O000O0O0000O0OOO0 ='.q{:d}_counter.npy'.format (OO000O0O0OOO0O000 )#line:1204
    OO0000OOOOOO00O0O =np .zeros (1 ,dtype ='int8,bool')#line:1205
    OO0OO00O0O0OO000O =len (OOO0OOO0OOO000OOO )#line:1207
    if OOO00OOOOOO0OOOO0 not in OOO0OOO0OOO000OOO :#line:1208
        OOO0OOO0OOO000OOO .append (OOO00OOOOOO0OOOO0 )#line:1209
    OO0O0OOO0000OO0OO =OOO0OOO0OOO000OOO .index (OOO00OOOOOO0OOOO0 )#line:1211
    O00O00O0OOOO00O0O =[(O0OO0O00OOO0O00O0 ,O00O0OO00O0OO0000 )for O00O0OO00O0OO0000 ,O0OO0O00OOO0O00O0 in enumerate (OOO0OOO0OOO000OOO )]#line:1213
    O0OO00OOOO0OOOO0O =widgets .RadioButtons (options =O00O00O0OOOO00O0O ,description ='',disabled =False )#line:1218
    O000000O0O0O00O0O =widgets .Output ()#line:1220
    with O000000O0O0O00O0O :#line:1221
        print (OOOOOO0O000OO00OO )#line:1222
    O00OO00000O0O0OOO =widgets .Output ()#line:1224
    def OO0O00000O0O000OO (O0OOOO00O00OOOO0O ):#line:1226
        OO0O00OOOO00OOO00 =int (O0OO00OOOO0OOOO0O .value )#line:1228
        OOO0000OO0OO0O00O =OO0O00OOOO00OOO00 ==OO0O0OOO0000OO0OO #line:1230
        O00OO0000OOO0O00O =trycount (O000O0O0000O0OOO0 ,OOO0000OO0OO0O00O )#line:1231
        OOOOO00OOOO0OOOO0 =max (0 ,100 -(O00OO0000OOO0O00O [0 ]-1 )*100 /OO0OO00O0O0OO000O )#line:1232
        O0O000O00OO0OO0O0 =O0OO00OOOO0OOOO0O .options [OO0O00OOOO00OOO00 ][0 ]#line:1233
        if OOO0000OO0OO0O00O :#line:1234
            O0O000O00OO0OO0O0 +=' correct\n'#line:1235
        else :#line:1236
            O0O000O00OO0OO0O0 +=' incorrect\n'#line:1237
        if O00OO0000OOO0O00O [1 ]:#line:1238
            O0O000O00OO0OO0O0 +='{:.0f}% on try {:d}'.format (OOOOO00OOOO0OOOO0 ,O00OO0000OOO0O00O [0 ])#line:1239
        else :#line:1240
            O0O000O00OO0OO0O0 +='{:.0f}% remaining'.format (max (0 ,OOOOO00OOOO0OOOO0 -100 /OO0OO00O0O0OO000O ))#line:1241
        with O00OO00000O0O0OOO :#line:1243
            clear_output ()#line:1244
            print (O0O000O00OO0OO0O0 )#line:1245
        return #line:1246
    OO0O00O000O000000 =widgets .Button (description ="submit")#line:1248
    OO0O00O000O000000 .on_click (OO0O00000O0O000OO )#line:1249
    return widgets .VBox ([O000000O0O0O00O0O ,O0OO00OOOO0OOOO0O ,OO0O00O000O000000 ,O00OO00000O0O0OOO ])#line:1250
def runq1 ():#line:1257
    OO0OOO00O0O0000O0 =1 #line:1258
    O00O0OOOOO0O00OOO =create_multipleChoice_widget (OO0OOO00O0O0000O0 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1259
    display (O00O0OOOOO0O00OOO )#line:1260
def runQ1 ():#line:1270
    OO0OOO00OO00O0OO0 =1 #line:1271
    O00OO00OO0000O0OO =create_multipleChoice_widget (OO0OOO00OO00O0OO0 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1272
    display (O00OO00OO0000O0OO )#line:1273
def runQ2x ():#line:1282
    O000000OO0OOO000O =2 #line:1283
    O0OO0O0OOO0000O0O =create_multipleChoice_widget (O000000OO0OOO000O ,'',['centred','backwards','forwards'],'centred')#line:1284
    display (O0OO0O0OOO0000O0O )#line:1285
def runQ3x ():#line:1293
    OO0O0O0O00000OO00 =3 #line:1294
    O0O000O0OO000O0OO =create_multipleChoice_widget (OO0O0O0O00000OO00 ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1295
    display (O0O000O0OO000O0OO )#line:1296
def runQ4x ():#line:1305
    O00OO00O00OOO0000 =4 #line:1306
    OOOOOOOOO0OOOOO0O =create_multipleChoice_widget (O00OO00O00OOO0000 ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1307
    display (OOOOOOOOO0OOOOO0O )#line:1308
def runQ5x ():#line:1318
    O00O000OO0OO0O000 =5 #line:1319
    OOO000OO0OOO0O000 =create_multipleChoice_widget (O00O000OO0OO0O000 ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1320
    display (OOO000OO0OOO0O000 )#line:1321
def runQ6x ():#line:1330
    O0OO0OOOO0OO0000O =6 #line:1331
    O00000OOO0OOOOO0O =create_multipleChoice_widget (O0OO0OOOO0OO0000O ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1332
    display (O00000OOO0OOOOO0O )#line:1333
def runQ7x ():#line:1342
    O0O0OO00O0000O0OO =7 #line:1343
    O0000OO0OO0O0000O =create_multipleChoice_widget (O0O0OO00O0000O0OO ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1344
    display (O0000OO0OO0O0000O )#line:1345
