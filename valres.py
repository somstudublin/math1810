import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (OO00O0000OO0OO000 ,OOOO0O000O0O0000O ):#line:10
        print ("\nPasswords may not be changed using this notebook at present.")#line:14
ps =[]#line:18
wd =''#line:19
def a1 ():#line:36
    global ps #line:38
    O0000OOOOO0OOOOOO =".a1_counter.npy"#line:41
    O0OOOOOOO0OO0OO00 =np .zeros (1 ,dtype ='int8,bool')#line:42
    O00OOO0000OOOO00O =0 #line:44
    O0O0OOO0O0OOO00OO =ps [0 ]#line:45
    O00OO0OO00OOO00OO =ps [1 ]#line:46
    if (waiter ()):#line:48
        while True :#line:49
            try :#line:50
                printmd ('**CA** (2%)')#line:51
                print (O0O0OOO0O0OOO00OO ,"+",O00OO0OO00OOO00OO )#line:52
                OOOOO000000OO00O0 =float (input ("Please enter your answer here: "))#line:53
                O0O0OO0OOOOO0OOOO =O0O0OOO0O0OOO00OO +O00OO0OO00OOO00OO #line:54
                O0OO000OOOOO0O000 =np .isclose (OOOOO000000OO00O0 ,O0O0OO0OOOOO0OOOO ,O00OOO0000OOOO00O )#line:55
                if O0OO000OOOOO0O000 :#line:56
                    print ("Well done, right answer is ",O0O0OO0OOOOO0OOOO )#line:57
                else :#line:58
                    print ("Not right yet. Take another look then run this cell again.")#line:59
                O0OOOOOOO0OO0OO00 =trycount (O0000OOOOO0OOOOOO ,O0OO000OOOOO0O000 )#line:61
                O0OOOOOOOOO0OOOOO =100 -(O0OOOOOOO0OO0OO00 [0 ]-1 )*10 #line:62
                if O0OOOOOOO0OO0OO00 [1 ]:#line:63
                    print ("First success after ",O0OOOOOOO0OO0OO00 [0 ]," tries, you have ",O0OOOOOOOOO0OOOOO ,"% on this exercise.")#line:64
                else :#line:65
                    print ("You have had ",O0OOOOOOO0OO0OO00 [0 ]," tries.")#line:66
                    print ("If next try is accepted you will achieve ",O0OOOOOOOOO0OOOOO -10 ,"% on this exercise.")#line:67
                break #line:69
            except ValueError :#line:71
                print ("I didn't understand that.")#line:72
                continue #line:73
        return #line:75
def a2_notlive (O0O0OOO0OOO00O0O0 ):#line:84
    global ps #line:86
    OO0O0O0000OO000O0 =".a2_counter.npy"#line:89
    OO00O00O00OOO0000 =np .zeros (1 ,dtype ='int8,bool')#line:90
    O00OO0OOOOOO0OO0O =6 #line:93
    O00O00OO000O00000 =7 #line:94
    OO00OOOO0OO0O000O =0 #line:96
    O0OO000OO0OO000O0 =(ps [O00OO0OOOOOO0OO0O ])%6 +1 #line:98
    O0O000O0000OOO0OO =(ps [O00O00OO000O00000 ])%6 +1 #line:99
    while O0OO000OO0OO000O0 +O0O000O0000OOO0OO ==7 or O0OO000OO0OO000O0 ==O0O000O0000OOO0OO :#line:100
        O0O000O0000OOO0OO +=1 #line:101
        O0O000O0000OOO0OO =O0O000O0000OOO0OO %6 +1 #line:102
    if (O0O0OOO0OOO00O0O0 ):#line:104
        printmd ('**CA** (2%)')#line:105
        print ("Run your program (when you are happy it is working correctly) for a=",O0OO000OO0OO000O0 ," and b=",O0O000O0000OOO0OO )#line:106
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:107
        return #line:108
    if (waiter ()):#line:110
        while True :#line:111
            try :#line:112
                print ("Enter your program's result for a=",O0OO000OO0OO000O0 ," and b=",O0O000O0000OOO0OO )#line:113
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:114
                O00000000O000OO0O =float (input ("Please enter your answer here: "))#line:115
                OOO00OOOO0OO0O000 =(3 *(O0OO000OO0OO000O0 **3 *O0O000O0000OOO0OO -O0OO000OO0OO000O0 *O0O000O0000OOO0OO **3 ))%7 #line:116
                O0O00000OO0OO00O0 =np .isclose (O00000000O000OO0O ,OOO00OOOO0OO0O000 ,OO00OOOO0OO0O000O )#line:117
                if O0O00000OO0OO00O0 :#line:118
                    print ("Well done, right answer is ",OOO00OOOO0OO0O000 )#line:119
                else :#line:120
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:121
                OO00O00O00OOO0000 =trycount (OO0O0O0000OO000O0 ,O0O00000OO0OO00O0 )#line:123
                O0OO00OOO00O0O0OO =100 -(OO00O00O00OOO0000 [0 ]-1 )*10 #line:124
                if OO00O00O00OOO0000 [1 ]:#line:125
                    print ("First success after ",OO00O00O00OOO0000 [0 ]," tries, you have ",O0OO00OOO00O0O0OO ,"% on this exercise.")#line:126
                else :#line:127
                    print ("You have had ",OO00O00O00OOO0000 [0 ]," tries.")#line:128
                    print ("If next try is accepted you will achieve ",O0OO00OOO00O0O0OO -10 ,"% on this exercise.")#line:129
                break #line:131
            except ValueError :#line:133
                print ("I didn't understand that.")#line:134
                continue #line:135
        return #line:137
def a3_notlive (OOOO0OOO0O0OOOO00 ):#line:146
    global ps #line:148
    OO0O00OOO0O00OO0O =".a3_counter.npy"#line:151
    OOOOOO00O00OOOO0O =np .zeros (1 ,dtype ='int8,bool')#line:152
    O0OO00000OOO00O00 =23 #line:155
    O00O0O000O0OO0O0O =24 #line:156
    O0O0O000OOOOO0000 =(ps [O0OO00000OOO00O00 ])%6 +1 #line:157
    O00OO0O000OO0OOOO =(ps [O00O0O000O0OO0O0O ])%6 +1 #line:158
    OOO0OOOOOOO0OOOOO =0 #line:160
    O0O0O000OOOOO0000 =10 *O0O0O000OOOOO0000 +O00OO0O000OO0OOOO ;#line:162
    if (OOOO0OOO0O0OOOO00 ):#line:164
        printmd ('**CA** (6%)')#line:165
        print ("Run your program for ",O0O0O000OOOOO0000 ,"people")#line:166
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:167
        return #line:168
    if (waiter ()):#line:170
        while True :#line:171
            try :#line:172
                print ("Enter your program's result for",O0O0O000OOOOO0000 ,"people")#line:173
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:174
                O0OOO000OOOO00OO0 =float (input ("Please enter your answer here: "))#line:175
                OOO00OOO00000O000 =O0O0O000OOOOO0000 +2 *O0O0O000OOOOO0000 +2 *O0O0O000OOOOO0000 +10 *O0O0O000OOOOO0000 #line:176
                O0O0OO00O00OOOO0O =np .isclose (O0OOO000OOOO00OO0 ,OOO00OOO00000O000 ,OOO0OOOOOOO0OOOOO )#line:177
                if O0O0OO00O00OOOO0O :#line:178
                    print ("Well done, right answer is ",OOO00OOO00000O000 )#line:179
                else :#line:180
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:181
                OOOOOO00O00OOOO0O =trycount (OO0O00OOO0O00OO0O ,O0O0OO00O00OOOO0O )#line:183
                OO0O0000O0OO0O000 =100 -(OOOOOO00O00OOOO0O [0 ]-1 )*10 #line:184
                if OOOOOO00O00OOOO0O [1 ]:#line:185
                    print ("First success after ",OOOOOO00O00OOOO0O [0 ]," tries, you have ",OO0O0000O0OO0O000 ,"% on this exercise.")#line:186
                else :#line:187
                    print ("You have had ",OOOOOO00O00OOOO0O [0 ]," tries.")#line:188
                    print ("If next try is accepted you will achieve ",OO0O0000O0OO0O000 -10 ,"% on this exercise.")#line:189
                break #line:191
            except ValueError :#line:193
                print ("I didn't understand that.")#line:194
                continue #line:195
        return #line:197
def a4_notlive (O00OOO0OOOO00000O ):#line:208
        import random #line:210
        import requests #line:211
        global ps #line:213
        global wd #line:214
        OO0O0O0OO0OO000OO =".a4_counter.npy"#line:217
        O00O0OO0OOOOOO0O0 =np .zeros (1 ,dtype ='int8,bool')#line:218
        O0OO0O0O000O0O00O =60 #line:221
        OOO0O0O000O0OOO00 =61 #line:222
        OOOO0OO0000O000OO =62 #line:223
        OOO00O0OOO00O0OOO =63 #line:224
        OO0O000O0OO0O0OO0 =64 #line:225
        O0O00OO00OOO00OO0 =0 #line:228
        if (O00OOO0OOOO00000O ):#line:230
                OOOOO0O0O0O00O00O ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:232
                O0OOO00OO00OO000O =requests .get (OOOOO0O0O0O00O00O )#line:234
                O00O00OOO0O00OO0O =O0OOO00OO00OO000O .content .splitlines ()#line:235
                random .seed (10 *ps [62 ]+ps [63 ])#line:236
                OOO0OOOO000000O00 =4 +(10 *ps [64 ]+ps [65 ])%4 #line:237
                O00OOOO00OOOO0000 =True #line:238
                while O00OOOO00OOOO0000 :#line:239
                        OO000O00O00O0O00O =O00O00OOO0O00OO0O [random .randint (0 ,len (O00O00OOO0O00OO0O )-1 )].decode ("utf-8")#line:240
                        if len (OO000O00O00O0O00O )>7 and len (OO000O00O00O0O00O )<14 and OO000O00O00O0O00O [0 ].islower ():#line:242
                                O00OOOO00OOOO0000 =False #line:243
                                for OO0OOO000O0000000 in OO000O00O00O0O00O :#line:244
                                        if chr (ord (OO0OOO000O0000000 )+OOO0OOOO000000O00 )>'z':#line:245
                                                O00OOOO00OOOO0000 =True #line:246
                O00OOOOO00O0OOO0O =len (OO000O00O00O0O00O )#line:248
                OO0O0OO0O000OO00O =''#line:249
                for OOO0OOO0O0O0OOO00 in range (0 ,O00OOOOO00O0OOO0O ):#line:250
                        OO0O0OO0O000OO00O +=chr (ord (OO000O00O00O0O00O [OOO0OOO0O0O0OOO00 ])+OOO0OOOO000000O00 )#line:252
                print ('Your encoded word is',OO0O0OO0O000OO00O )#line:254
                print ('Write your program in the cell below this one.\n')#line:255
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:257
                wd =OO000O00O00O0O00O #line:258
                return #line:259
        if (waiter ()):#line:261
                while True :#line:262
                        try :#line:263
                                printmd ('**CA** (6%)')#line:264
                                OO0OOOOOOO0000OOO =str (input ("Enter your DECODED word here: "))#line:265
                                OO000O00OO0OOO0OO =wd #line:266
                                OOOO00O0OOOOOOOOO =OO0OOOOOOO0000OOO ==OO000O00OO0OOO0OO #line:267
                                if OOOO00O0OOOOOOOOO :#line:268
                                        print ("Well done, right answer is ",OO000O00OO0OOO0OO )#line:269
                                else :#line:270
                                        print ("Not right yet. Take another look then run this cell again.")#line:271
                                O00O0OO0OOOOOO0O0 =trycount (OO0O0O0OO0OO000OO ,OOOO00O0OOOOOOOOO )#line:273
                                OOOOO00OO000O00OO =100 -(O00O0OO0OOOOOO0O0 [0 ]-1 )*10 #line:274
                                if O00O0OO0OOOOOO0O0 [1 ]:#line:275
                                        print ("First success after ",O00O0OO0OOOOOO0O0 [0 ]," tries, you have ",OOOOO00OO000O00OO ,"% on this exercise.")#line:276
                                else :#line:277
                                        print ("You have had ",O00O0OO0OOOOOO0O0 [0 ]," tries.")#line:278
                                        print ("If next try is accepted you will achieve ",OOOOO00OO000O00OO -10 ,"% on this exercise.")#line:279
                                break #line:280
                        except ValueError :#line:282
                                print ("I didn't understand that.")#line:283
                                continue #line:284
                return #line:286
def a5_notlive (OO00O0OO0O0OOO000 ):#line:296
        import random #line:298
        import requests #line:299
        global ps #line:301
        global P0 #line:302
        OOOO0OOO00O00O0OO =".a5_counter.npy"#line:306
        OO000O0OOO0O0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:307
        O00000OO0OO00O0OO =70 #line:310
        O000OOO00O0O0OOO0 =71 #line:311
        O0OO0O00OO0OO0O00 =72 #line:312
        OO0O00O0O0OO00O0O =73 #line:313
        OOOO0O0OO0O00000O =74 #line:314
        OOOOO0O0OO00OOOOO =0 #line:317
        if (OO00O0OO0O0OOO000 ):#line:319
                P0 =[]#line:320
                O0O00000OO0000000 =7 +(10 *ps [O00000OO0OO00O0OO ]+ps [O000OOO00O0O0OOO0 ])%4 #line:321
                for O00000O0OOOO00OOO in range (O0O00000OO0000000 ):#line:322
                        P0 .append (max (0 ,ps [O0OO0O00OO0OO0O00 +O00000O0OOOO00OOO ]-1 ))#line:323
                print ('Run your program for the list below:\n',P0 )#line:324
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:326
        elif (waiter ()):#line:328
                while True :#line:329
                        try :#line:330
                                printmd ('**CA** (6%)')#line:333
                                OOOO0O0O00000OOO0 =eval (input ("Enter your list here: "))#line:334
                                OO000OOO0OOO0O000 =3 #line:339
                                OO00O0O000O00OOO0 =P0 .copy ()#line:340
                                OO00O0O000O00OOO0 .append (0 )#line:341
                                print (OO00O0O000O00OOO0 )#line:342
                                O0O00000OO0000000 =len (P0 )#line:343
                                for O0000OOO0OO000O0O in range (OO000OOO0OOO0O000 ):#line:344
                                        for O00000O0OOOO00OOO in range (O0O00000OO0000000 ):#line:345
                                                OO00O0O000O00OOO0 [O00000O0OOOO00OOO ]=OO00O0O000O00OOO0 [O00000O0OOOO00OOO +1 ]*(O00000O0OOOO00OOO +1 )#line:347
                                OO00O0O000O00OOO0 .pop ()#line:348
                                O00O0O0O00OOOOO00 =OO00O0O000O00OOO0 #line:351
                                if not type (OOOO0O0O00000OOO0 )==type (O00O0O0O00OOOOO00 ):#line:353
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:354
                                elif not len (OOOO0O0O00000OOO0 )==len (O00O0O0O00OOOOO00 ):#line:355
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:356
                                else :#line:357
                                        O000O00OOO00OOO00 =OOOO0O0O00000OOO0 ==O00O0O0O00OOOOO00 #line:358
                                        if O000O00OOO00OOO00 :#line:359
                                                print ("Well done, right answer is ",O00O0O0O00OOOOO00 )#line:360
                                        else :#line:361
                                                print ("Not right yet. Take another look then run this cell again.")#line:362
                                        OO000O0OOO0O0OO0O =trycount (OOOO0OOO00O00O0OO ,O000O00OOO00OOO00 )#line:364
                                        OO00O00O00O00OO0O =100 -(OO000O0OOO0O0OO0O [0 ]-1 )*10 #line:365
                                        if OO000O0OOO0O0OO0O [1 ]:#line:366
                                                print ("First success after ",OO000O0OOO0O0OO0O [0 ]," tries, you have ",OO00O00O00O00OO0O ,"% on this exercise.")#line:367
                                        else :#line:368
                                                print ("You have had ",OO000O0OOO0O0OO0O [0 ]," tries.")#line:369
                                                print ("If next try is accepted you will achieve ",OO00O00O00O00OO0O -10 ,"% on this exercise.")#line:370
                                        break #line:371
                                OO00O0O000O00OOO0 =None #line:374
                                O00O0O0O00OOOOO00 =None #line:375
                        except ValueError :#line:376
                                print ("I didn't understand that.")#line:377
                                continue #line:378
        return #line:380
def a6_notlive (O0000OO0O00000O00 ):#line:389
        import random #line:391
        import requests #line:392
        global ps #line:394
        global P0 #line:395
        O0O0O0O000000O0O0 =".a6_counter.npy"#line:399
        OOO00000OO0O00000 =np .zeros (1 ,dtype ='int8,bool')#line:400
        O0OOO0O0O0OO0OOO0 =11 #line:403
        OOOO0000OO0OO00O0 =16 #line:404
        OO000O0OO0OOO000O =7 #line:405
        OOOOO00O0OO0O0O0O =33 #line:406
        OO0OO0O00O0O00000 =21 #line:407
        OO00OOO0O00O00O00 =0 #line:410
        if (O0000OO0O00000O00 ):#line:412
                O0000O0OOOOO000OO =ps [O0OOO0O0O0OO0OOO0 ]+ps [OOOO0000OO0OO00O0 ]+ps [OO000O0OO0OOO000O ]+ps [OOOOO00O0OO0O0O0O ]+ps [OO0OO0O00O0O00000 ]#line:413
                random .seed (O0000O0OOOOO000OO )#line:414
                P0 =random .randint (1000 ,2000 )#line:415
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:416
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:418
        elif (waiter ()):#line:420
                while True :#line:421
                        try :#line:422
                                printmd ('**CA** (6%)')#line:425
                                OO00O0O0O0O0O0OO0 =eval (input ("Enter your stopping number here: "))#line:426
                                O00000OO000O0OOO0 =P0 #line:430
                                O00OOOO0OOO0000O0 =[O00000OO000O0OOO0 ]#line:431
                                while not O00000OO000O0OOO0 ==1 :#line:432
                                        if O00000OO000O0OOO0 %2 :#line:433
                                                O00000OO000O0OOO0 =3 *O00000OO000O0OOO0 +1 #line:434
                                        else :#line:435
                                                O00000OO000O0OOO0 =O00000OO000O0OOO0 //2 #line:436
                                        O00OOOO0OOO0000O0 .append (O00000OO000O0OOO0 )#line:437
                                OOOOOOO0OOOO00O00 =len (O00OOOO0OOO0000O0 )#line:438
                                OO0O0OO00OOOO0OO0 =OOOOOOO0OOOO00O00 #line:442
                                if not type (OO00O0O0O0O0O0OO0 )==type (OO0O0OO00OOOO0OO0 ):#line:444
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:445
                                else :#line:448
                                        O0O0OOOO0OOOO0O00 =OO00O0O0O0O0O0OO0 ==OO0O0OO00OOOO0OO0 #line:449
                                        if O0O0OOOO0OOOO0O00 :#line:450
                                                print ("Well done, right answer is ",OO0O0OO00OOOO0OO0 )#line:451
                                        else :#line:452
                                                print ("Not right yet. Take another look then run this cell again.")#line:453
                                        OOO00000OO0O00000 =trycount (O0O0O0O000000O0O0 ,O0O0OOOO0OOOO0O00 )#line:455
                                        O0O0OOOOO0OO00O0O =100 -(OOO00000OO0O00000 [0 ]-1 )*10 #line:456
                                        if OOO00000OO0O00000 [1 ]:#line:457
                                                print ("First success after ",OOO00000OO0O00000 [0 ]," tries, you have ",O0O0OOOOO0OO00O0O ,"% on this exercise.")#line:458
                                        else :#line:459
                                                print ("You have had ",OOO00000OO0O00000 [0 ]," tries.")#line:460
                                                print ("If next try is accepted you will achieve ",O0O0OOOOO0OO00O0O -10 ,"% on this exercise.")#line:461
                                        break #line:462
                                OOOOOOO0OOOO00O00 =None #line:465
                                OO0O0OO00OOOO0OO0 =None #line:466
                        except ValueError :#line:467
                                print ("I didn't understand that.")#line:468
                                continue #line:469
        return #line:471
def a7_notlive (OO000O0O000OO0000 ):#line:481
        O0O00OOOO00O0O0O0 =".a7_counter.npy"#line:485
        OO0OO0OO00O000OOO =np .zeros (1 ,dtype ='int8,bool')#line:486
        def OO00000OOO00000OO ():#line:488
                pass #line:489
        O00O000O0O000O000 =[(30 ,10 )]#line:492
        O0OOOOO0OOO0OOOOO =1.0e-4 #line:495
        if (waiter ()):#line:498
                printmd ('**CA** (6%)')#line:500
                if not type (OO000O0O000OO0000 )==type (OO00000OOO00000OO ):#line:502
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:503
                else :#line:506
                        def OO0O0O0O0OO000000 (O0O000O0O0000OO0O ,OO0000O000O00OOOO ):#line:509
                                import math #line:510
                                OO0OOO000OO0O0O00 =9.81 #line:511
                                OOO000OO00OOOO0O0 =math .pi *OO0000O000O00OOOO /180. #line:512
                                O000O0OO0O0OO0OOO =O0O000O0O0000OO0O **2 *math .sin (2 *OOO000OO00OOOO0O0 )/OO0OOO000OO0O0O00 #line:513
                                O00OOO0OOOOOOOOO0 =O0O000O0O0000OO0O **2 *(math .sin (OOO000OO00OOOO0O0 ))**2 /(2. *OO0OOO000OO0O0O00 )#line:514
                                return O000O0OO0O0OO0OOO ,O00OOO0OOOOOOOOO0 #line:515
                        import random as r #line:518
                        O00O000O0O000O000 =[]#line:519
                        O00O00OOO00O0OOO0 =False #line:520
                        O0O00O0OOOOOO0000 =[]#line:521
                        OO000OO0O000OO0OO =10 #line:522
                        OO0OOO0OO0O0O0O00 =100 #line:523
                        O0O000000OOOO0O00 =5 #line:524
                        O0OOO0OOOO00O00O0 =85 #line:525
                        for OO0O000O0O00O0OO0 in range (5 ):#line:526
                                O00O000O0O000O000 .append ((r .uniform (OO000OO0O000OO0OO ,OO0OOO0OO0O0O0O00 ),r .uniform (O0O000000OOOO0O00 ,O0OOO0OOOO00O00O0 )))#line:527
                        for (OOOOOOOO0O0O00000 ,OOO00000O0000O0O0 )in O00O000O0O000O000 :#line:528
                                print ('Testing:',OOOOOOOO0O0O00000 ,OOO00000O0000O0O0 )#line:529
                                OOO0O00O0O0O00OOO =OO000O0O000OO0000 (OOOOOOOO0O0O00000 ,OOO00000O0000O0O0 )#line:530
                                print ('Output:',*OOO0O00O0O0O00OOO )#line:531
                                OO00OO0O0O0O0OOO0 =OO0O0O0O0OO000000 (OOOOOOOO0O0O00000 ,OOO00000O0000O0O0 )#line:532
                                print ('Actual:',*OO00OO0O0O0O0OOO0 )#line:533
                                print ()#line:534
                                if (not type (OOO0O00O0O0O00OOO )==type (OO00OO0O0O0O0OOO0 ))or (not len (OOO0O00O0O0O00OOO )==len (OO00OO0O0O0O0OOO0 )):#line:535
                                        if O00O00OOO00O0OOO0 ==False :#line:536
                                           O00O00OOO00O0OOO0 =True #line:537
                                else :#line:538
                                        O0O00O0OOOOOO0000 .append (all (np .isclose (OOO0O00O0O0O00OOO ,OO00OO0O0O0O0OOO0 ,O0OOOOO0OOO0OOOOO )))#line:539
                        if O00O00OOO00O0OOO0 :#line:541
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:542
                        else :#line:544
                                O000O0OO000OOOO0O =all (O0O00O0OOOOOO0000 )#line:545
                                if O000O0OO000OOOO0O :#line:546
                                        print ("Well done, all correct.")#line:547
                                else :#line:548
                                        print ("Not right yet. Take another look then run this cell again.")#line:549
                                OO0OO0OO00O000OOO =trycount (O0O00OOOO00O0O0O0 ,O000O0OO000OOOO0O )#line:551
                                O00OO0OOO0OOOO0O0 =100 -(OO0OO0OO00O000OOO [0 ]-1 )*10 #line:552
                                if OO0OO0OO00O000OOO [1 ]:#line:553
                                        print ("First success after ",OO0OO0OO00O000OOO [0 ]," tries, you have ",O00OO0OOO0OOOO0O0 ,"% on this exercise.")#line:554
                                else :#line:555
                                        print ("You have had ",OO0OO0OO00O000OOO [0 ]," tries.")#line:556
                                        print ("If next try is accepted you will achieve ",O00OO0OOO0OOOO0O0 -10 ,"% on this exercise.")#line:557
                        OO00OO0O0O0O0OOO0 =None #line:560
                        OO0O0O0O0OO000000 =None #line:561
        return #line:563
def a8_notlive (O0000O0OOOO000OOO ):#line:573
        O00000OO0OOOO0OOO =".a8_counter.npy"#line:577
        O0O0OO0000OO0OO00 =np .zeros (1 ,dtype ='int8,bool')#line:578
        def O0OO00O0OOO0O0000 ():#line:580
                pass #line:581
        OOOOO0OOO0OOO0OO0 =1.0e-4 #line:585
        if (waiter ()):#line:588
                printmd ('**CA** (6%)')#line:590
                if not type (O0000O0OOOO000OOO )==type (O0OO00O0OOO0O0000 ):#line:594
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:595
                else :#line:599
                        import inspect #line:602
                        OOOO0OO0OOO0O0O0O =inspect .getsourcelines (O0000O0OOOO000OOO )#line:603
                        OOO00OO0OO0OOOOOO =True #line:604
                        O000O0000O0O000OO =[]#line:605
                        for OOOO0000OOOOO00OO ,OO000O00O0O0OO00O in enumerate (OOOO0OO0OOO0O0O0O [0 ]):#line:606
                                if 'for'in OO000O00O0O0OO00O or 'while'in OO000O00O0O0OO00O :#line:607
                                        OOO00OO0OO0OOOOOO =False #line:609
                                        O000O0000O0O000OO .append (OOOO0000OOOOO00OO )#line:610
                        if not OOO00OO0OO0OOOOOO :#line:611
                                print ('Function needs to be written without loops (using NumPy), check lines',*O000O0000O0O000OO )#line:612
                                print ('No marks lost for this attempt.')#line:613
                                return #line:614
                        def O0O00OO00OOO00O00 (OO0O000OO0O000OOO ):#line:617
                                OO0O00OOO0O0O0OO0 =np .vstack ((OO0O000OO0O000OOO ,OO0O000OO0O000OOO [0 ]))#line:618
                                O00O0O00OO0O0OOOO =sum (OO0O00OOO0O0O0OO0 [:-1 ,0 ]*OO0O00OOO0O0O0OO0 [1 :,1 ])#line:619
                                OOOO0O00O0O00O00O =sum (OO0O00OOO0O0O0OO0 [:-1 ,1 ]*OO0O00OOO0O0O0OO0 [1 :,0 ])#line:620
                                return abs (O00O0O00OO0O0OOOO -OOOO0O00O0O00O00O )/2 #line:621
                        import random as r #line:624
                        O0OO00O0O00OO00O0 =r .randint (6 ,11 )#line:625
                        OOOO0O000OO0OOO00 =np .ones ((O0OO00O0O00OO00O0 ,2 ))#line:626
                        OO0OO0OOOOOO00000 =False #line:627
                        O00O0O0OO000000O0 =[]#line:628
                        OOOO0OO0OO0OO0O0O =1. #line:629
                        OO0O0OO0O0O0OO000 =20. #line:630
                        O0OOO00O00OO0OO0O =OOOO0OO0OO0OO0O0O #line:631
                        OOOOO0O0O0OO0OO00 =OO0O0OO0O0O0OO000 #line:632
                        for O0000OOO000OOO00O in range (O0OO00O0O00OO00O0 ):#line:633
                                OOOO0O000OO0OOO00 [O0000OOO000OOO00O ]=[r .uniform (OOOO0OO0OO0OO0O0O ,OO0O0OO0O0O0OO000 ),r .uniform (O0OOO00O00OO0OO0O ,OOOOO0O0O0OO0OO00 )]#line:634
                        print ('Testing:',OOOO0O000OO0OOO00 )#line:635
                        OO00OOO000OO00O00 =O0000O0OOOO000OOO (OOOO0O000OO0OOO00 )#line:636
                        print ('Output:',OO00OOO000OO00O00 )#line:637
                        O0O00OOOOOO00OO0O =O0O00OO00OOO00O00 (OOOO0O000OO0OOO00 )#line:638
                        print ('Actual:',O0O00OOOOOO00OO0O )#line:639
                        print ()#line:640
                        if not type (OO00OOO000OO00O00 )==type (O0O00OOOOOO00OO0O ):#line:641
                                if OO0OO0OOOOOO00000 ==False :#line:642
                                        OO0OO0OOOOOO00000 =True #line:643
                        else :#line:644
                                O00O0O0OO000000O0 .append (np .isclose (OO00OOO000OO00O00 ,O0O00OOOOOO00OO0O ,OOOOO0OOO0OOO0OO0 ))#line:645
                        if OO0OO0OOOOOO00000 :#line:647
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:648
                        else :#line:650
                                OOO0O000OOO000O00 =all (O00O0O0OO000000O0 )#line:651
                                if OOO0O000OOO000O00 :#line:652
                                        print ("Well done, all correct.")#line:653
                                else :#line:654
                                        print ("Not right yet. Take another look then run this cell again.")#line:655
                                O0O0OO0000OO0OO00 =trycount (O00000OO0OOOO0OOO ,OOO0O000OOO000O00 )#line:657
                                O0O0OO0OO0O0O0O0O =100 -(O0O0OO0000OO0OO00 [0 ]-1 )*10 #line:658
                                if O0O0OO0000OO0OO00 [1 ]:#line:659
                                        print ("First success after ",O0O0OO0000OO0OO00 [0 ]," tries, you have ",O0O0OO0OO0O0O0O0O ,"% on this exercise.")#line:660
                                else :#line:661
                                        print ("You have had ",O0O0OO0000OO0OO00 [0 ]," tries.")#line:662
                                        print ("If next try is accepted you will achieve ",O0O0OO0OO0O0O0O0O -10 ,"% on this exercise.")#line:663
                        O0O00OOOOOO00OO0O =None #line:666
                        O0O00OO00OOO00O00 =None #line:667
        return #line:669
def a1_notlive ():#line:685
        print ('This CA test is not currently live.')#line:686
        return #line:687
def a2 (O00O00OO0OOO000O0 ):#line:695
        print ('This CA test is not currently live.')#line:696
        return #line:697
def a3 (O0OOOOOOOO0OO000O ):#line:705
        print ('This CA test is not currently live.')#line:706
        return #line:707
def a4 (OO00O000000000O0O ):#line:715
        print ('This CA test is not currently live.')#line:716
        return #line:717
def a5 (O0OO0O0OOO00O0O0O ):#line:725
        print ('This CA test is not currently live.')#line:726
        return #line:727
def a6 (OOOOO00OOO0OO0OO0 ):#line:735
        print ('This CA test is not currently live.')#line:736
        return #line:737
def a7 ():#line:745
        print ('This CA test is not currently live.')#line:746
        return #line:747
def a8 (O0OOOO0O00OO00O00 ):#line:755
        print ('This CA test is not currently live.')#line:756
        return #line:757
def b1 ():#line:775
    global ps #line:777
    O00OOOO000000OOOO =".b1_counter.npy"#line:780
    OOOO0OOO00O000OOO =np .zeros (1 ,dtype ='int8,bool')#line:781
    OOOO0O0O0OOOO0OOO =0.05 #line:783
    if (waiter ()):#line:785
        while True :#line:786
            try :#line:787
                printmd ('**CA**')#line:788
                O0OO00O00O0000000 =eval (input ("Please enter your answer here in the format D,k: "))#line:789
                OOO0000OO0OO0O0OO =(0.025 ,2.0 )#line:790
                O0OOO00000O0OOOOO =all (np .isclose (O0OO00O00O0000000 ,OOO0000OO0OO0O0OO ,rtol =OOOO0O0O0OOOO0OOO ))#line:791
                if O0OOO00000O0OOOOO :#line:792
                    print ("Well done, reasonable estimate is ",OOO0000OO0OO0O0OO )#line:793
                else :#line:794
                    print ("Not right yet. Take another look then run this cell again.")#line:795
                OOOO0OOO00O000OOO =trycount (O00OOOO000000OOOO ,O0OOO00000O0OOOOO )#line:797
                OOOOO00O0000O0O0O =100 -(OOOO0OOO00O000OOO [0 ]-1 )*10 #line:798
                if OOOO0OOO00O000OOO [1 ]:#line:799
                    print ("First success after ",OOOO0OOO00O000OOO [0 ]," tries, you have ",OOOOO00O0000O0O0O ,"% on this exercise.")#line:800
                else :#line:801
                    print ("You have had ",OOOO0OOO00O000OOO [0 ]," tries.")#line:802
                    print ("If next try is accepted you will achieve ",OOOOO00O0000O0O0O -10 ,"% on this exercise.")#line:803
                break #line:805
            except ValueError :#line:807
                print ("I didn't understand that.")#line:808
                continue #line:809
        return #line:811
def b2 (OO0O000O000OO0OOO ):#line:821
        O00OO000OO0000O0O =".b2_counter.npy"#line:825
        O0OO000OOO0OO00O0 =np .zeros (1 ,dtype ='int8,bool')#line:826
        def OO0OOOO00O0O00OO0 ():#line:828
                pass #line:829
        OOO0O000OO0O0O0O0 =1.0e-2 #line:832
        OOO000OO0O00OO00O =0.0 #line:833
        if (waiter ()):#line:835
                printmd ('**CA**')#line:837
                if not type (OO0O000O000OO0OOO )==type (OO0OOOO00O0O00OO0 ):#line:839
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:840
                else :#line:843
                        def O00O000O0O0000OO0 (O00OOO00O0O0O0000 ):#line:847
                                O000OOOOO0000OO0O =[]#line:848
                                OOOOOO0O00OO000O0 =20.0 #line:849
                                OOOOOOOOOOOOOO00O =58.1e-3 #line:850
                                OOO0O00000000OOO0 =9.81 #line:851
                                O00OO0OOO0OOOO00O =0.0 #line:852
                                OO0O0O0O00OOO00OO =0.0 #line:853
                                OO0000O00OO0O0O0O =0.0 #line:854
                                O0OOOO000O0000O00 =10 #line:855
                                OOOO0OO00O000O0OO =3.35e-2 #line:856
                                O00000O0000000OOO =0.51 #line:857
                                O0O0000O0O0O00O00 =1.25 #line:858
                                OO00O0O00OOO0O00O =math .pi *OOOO0OO00O000O0OO **2 #line:859
                                O00OOO0OOOO000000 =0.5 *O00000O0000000OOO *OO00O0O00OOO0O00O *O0O0000O0O0O00O00 #line:860
                                OO00OO00OOO000OO0 =100000 #line:862
                                O0OOOOOOOO00000O0 =np .zeros (OO00OO00OOO000OO0 ,float )#line:863
                                O00O00OO00OOO0OOO =np .zeros (OO00OO00OOO000OO0 ,float )#line:864
                                OOO0O00000000000O =np .zeros (OO00OO00OOO000OO0 ,float )#line:865
                                OOO0O00OOOOO0O000 =np .zeros (OO00OO00OOO000OO0 ,float )#line:866
                                OOO0O0O000O00OO0O =np .zeros (OO00OO00OOO000OO0 ,float )#line:867
                                OO00000O0O0O0OOOO =np .zeros (OO00OO00OOO000OO0 ,float )#line:868
                                O000000OOOOO00O00 =np .zeros (OO00OO00OOO000OO0 ,float )#line:869
                                O0OOOOOOOO00000O0 ,OOOO0OO000OO0O0O0 =np .linspace (OO0000O00OO0O0O0O ,O0OOOO000O0000O00 ,OO00OO00OOO000OO0 ,retstep =True )#line:870
                                for O000OO00OOO000000 in O00OOO00O0O0O0000 :#line:872
                                        OOOOO000O0000OOOO =OOOOOO0O00OO000O0 *math .cos (O000OO00OOO000000 )#line:873
                                        O0O0OO0OOOOOO00OO =OOOOOO0O00OO000O0 *math .sin (O000OO00OOO000000 )#line:874
                                        OO00000O0O0O0OOOO [0 ]=O00OO0OOO0OOOO00O #line:876
                                        O000000OOOOO00O00 [0 ]=OO0O0O0O00OOO00OO #line:877
                                        OOO0O00OOOOO0O000 [0 ]=OOOOO000O0000OOOO #line:878
                                        OOO0O0O000O00OO0O [0 ]=O0O0OO0OOOOOO00OO #line:879
                                        for O0O0OOOOOO0O0O0O0 in range (OO00OO00OOO000OO0 -1 ):#line:880
                                                O0OO00000OO0OOO00 =math .sqrt (OOO0O00OOOOO0O000 [O0O0OOOOOO0O0O0O0 ]**2 +OOO0O0O000O00OO0O [O0O0OOOOOO0O0O0O0 ]**2 )#line:881
                                                O00O00O00OO00O00O =-O00OOO0OOOO000000 *O0OO00000OO0OOO00 *OOO0O00OOOOO0O000 [O0O0OOOOOO0O0O0O0 ]#line:882
                                                O00O00OO00OOO0OOO [O0O0OOOOOO0O0O0O0 ]=O00O00O00OO00O00O /OOOOOOOOOOOOOO00O #line:883
                                                OOO0O00OOOOO0O000 [O0O0OOOOOO0O0O0O0 +1 ]=OOO0O00OOOOO0O000 [O0O0OOOOOO0O0O0O0 ]+O00O00OO00OOO0OOO [O0O0OOOOOO0O0O0O0 ]*OOOO0OO000OO0O0O0 #line:884
                                                OO00000O0O0O0OOOO [O0O0OOOOOO0O0O0O0 +1 ]=OO00000O0O0O0OOOO [O0O0OOOOOO0O0O0O0 ]+OOO0O00OOOOO0O000 [O0O0OOOOOO0O0O0O0 +1 ]*OOOO0OO000OO0O0O0 #line:885
                                                O00OOOOO00OO0O0O0 =-OOOOOOOOOOOOOO00O *OOO0O00000000OOO0 -O00OOO0OOOO000000 *O0OO00000OO0OOO00 *OOO0O0O000O00OO0O [O0O0OOOOOO0O0O0O0 ]#line:886
                                                OOO0O00000000000O [O0O0OOOOOO0O0O0O0 ]=O00OOOOO00OO0O0O0 /OOOOOOOOOOOOOO00O #line:887
                                                OOO0O0O000O00OO0O [O0O0OOOOOO0O0O0O0 +1 ]=OOO0O0O000O00OO0O [O0O0OOOOOO0O0O0O0 ]+OOO0O00000000000O [O0O0OOOOOO0O0O0O0 ]*OOOO0OO000OO0O0O0 #line:888
                                                O000000OOOOO00O00 [O0O0OOOOOO0O0O0O0 +1 ]=O000000OOOOO00O00 [O0O0OOOOOO0O0O0O0 ]+OOO0O0O000O00OO0O [O0O0OOOOOO0O0O0O0 +1 ]*OOOO0OO000OO0O0O0 #line:889
                                                if (O000000OOOOO00O00 [O0O0OOOOOO0O0O0O0 +1 ]<0 ):#line:890
                                                        break #line:891
                                        OOOOOOOOO0O000OO0 =O0O0OOOOOO0O0O0O0 #line:892
                                        O000OOOOO0000OO0O .append (OO00000O0O0O0OOOO [OOOOOOOOO0O000OO0 ])#line:893
                                return (O000OOOOO0000OO0O );#line:895
                        import random as r #line:898
                        O0O0O0O0O0O0O000O =[]#line:899
                        O0OOOO0O0OO00O000 =False #line:900
                        OOOO0OOO0O000OO0O =[]#line:901
                        OOOO0OOOO000O0000 =0.1 #line:902
                        OOO0OOOOO0O0O00OO =1.5 #line:903
                        for OOO0OOOOO0OOOOOO0 in range (5 ):#line:904
                                O0O0O0O0O0O0O000O .append (r .uniform (OOOO0OOOO000O0000 ,OOO0OOOOO0O0O00OO ))#line:905
                        O0O0O0O0O0O0O000O .sort ()#line:906
                        print ('Testing thetas=',O0O0O0O0O0O0O000O )#line:907
                        O00OOO0OOO0O00OO0 =OO0O000O000OO0OOO (O0O0O0O0O0O0O000O )#line:908
                        print ('Output ximpacts=',O00OOO0OOO0O00OO0 )#line:909
                        OOO0O0000O0OO0O00 =O00O000O0O0000OO0 (O0O0O0O0O0O0O000O )#line:910
                        print ('Actual ximpacts=',OOO0O0000O0OO0O00 )#line:911
                        print ()#line:912
                        if (not type (O00OOO0OOO0O00OO0 )==type (OOO0O0000O0OO0O00 ))or (not len (O00OOO0OOO0O00OO0 )==len (OOO0O0000O0OO0O00 )):#line:913
                                if O0OOOO0O0OO00O000 ==False :#line:914
                                        O0OOOO0O0OO00O000 =True #line:915
                        else :#line:916
                                OOOO0OOO0O000OO0O .append (all (np .isclose (O00OOO0OOO0O00OO0 ,OOO0O0000O0OO0O00 ,rtol =OOO0O000OO0O0O0O0 ,atol =OOO000OO0O00OO00O )))#line:917
                        if O0OOOO0O0OO00O000 :#line:919
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:920
                        else :#line:922
                                O00O00000O00000O0 =all (OOOO0OOO0O000OO0O )#line:923
                                if O00O00000O00000O0 :#line:924
                                        print ("Well done, all correct.")#line:925
                                else :#line:926
                                        print ("Not close enough. Take another look then run this cell again.")#line:927
                                O0OO000OOO0OO00O0 =trycount (O00OO000OO0000O0O ,O00O00000O00000O0 )#line:929
                                OOOO0O0O00O0O000O =100 -(O0OO000OOO0OO00O0 [0 ]-1 )*10 #line:930
                                if O0OO000OOO0OO00O0 [1 ]:#line:931
                                        print ("First success after ",O0OO000OOO0OO00O0 [0 ]," tries, you have ",OOOO0O0O00O0O000O ,"% on this exercise.")#line:932
                                else :#line:933
                                        print ("You have had ",O0OO000OOO0OO00O0 [0 ]," tries.")#line:934
                                        print ("If next try is accepted you will achieve ",OOOO0O0O00O0O000O -10 ,"% on this exercise.")#line:935
                        OOO0O0000O0OO0O00 =None #line:938
                        O00O000O0O0000OO0 =None #line:939
        return #line:941
def b3 ():#line:951
    global ps #line:953
    OO00000000OO0OOOO =".b3_counter.npy"#line:956
    OOOOO00OO0000O0OO =np .zeros (1 ,dtype ='int8,bool')#line:957
    OO0OOO00O00O00OOO =0.01 #line:960
    if (waiter ()):#line:962
        while True :#line:963
            try :#line:964
                printmd ('**CA**')#line:965
                OOOOOOOOOOOO0O0O0 =float (input ("Enter a real number here: "))#line:966
                OO000O0OO0O0OOOOO =0.5 #line:967
                O0O000OO00O0O000O =np .isclose (OOOOOOOOOOOO0O0O0 ,OO000O0OO0O0OOOOO ,atol =OO0OOO00O00O00OOO )#line:968
                if O0O000OO00O0O000O :#line:969
                    print ("Well done. Actual value is ",OO000O0OO0O0OOOOO )#line:970
                else :#line:971
                    print ("Not right yet. Take another look then run this cell again.")#line:972
                OOOOO00OO0000O0OO =trycount (OO00000000OO0OOOO ,O0O000OO00O0O000O )#line:974
                OO00OO0O0O0O0OOOO =100 -(OOOOO00OO0000O0OO [0 ]-1 )*10 #line:975
                if OOOOO00OO0000O0OO [1 ]:#line:976
                    print ("First success after ",OOOOO00OO0000O0OO [0 ]," tries, you have ",OO00OO0O0O0O0OOOO ,"% on this exercise.")#line:977
                else :#line:978
                    print ("You have had ",OOOOO00OO0000O0OO [0 ]," tries.")#line:979
                    print ("If next try is accepted you will achieve ",OO00OO0O0O0O0OOOO -10 ,"% on this exercise.")#line:980
                break #line:982
            except ValueError :#line:984
                print ("I didn't understand that.")#line:985
                continue #line:986
        return #line:988
def b1_notlive ():#line:1000
        print ('This CA test is not currently live.')#line:1001
        return #line:1002
def b2_notlive (O0O00O00000OOO000 ):#line:1012
        print ('This CA test is not currently live.')#line:1013
        return #line:1014
def b3_notlive ():#line:1021
        print ('This CA test is not currently live.')#line:1022
        return #line:1023
def printmd (OO0O0O0O00O0O000O ):#line:1033
    display (Markdown (OO0O0O0O00O0O000O ))#line:1034
def repeat_to_length (O00O00O0OO0000000 ,OOO0OOOO0OO0OOO0O ):#line:1036
   return (O00O00O0OO0000000 *((OOO0OOOO0OO0OOO0O //len (O00O00O0OO0000000 ))+1 ))[:OOO0OOOO0OO0OOO0O ]#line:1037
def getco (OOOOOOOOOOO00000O ):#line:1039
    global ps #line:1040
    OOO0000OO00OO0000 =getpass .getuser ()#line:1041
    OO000OOO0O0000OOO =int .from_bytes (OOO0000OO00OO0000 .encode (),'little')#line:1042
    O0O00OO00000O0OOO =str (OO000OOO0O0000OOO )#line:1043
    OOOO00OOOOOOOO00O =repeat_to_length (O0O00OO00000O0OOO ,OOOOOOOOOOO00000O )#line:1044
    ps =[int (OO0O0O00OOOOO00O0 )+1 for OO0O0O00OOOOO00O0 in OOOO00OOOOOOOO00O ]#line:1045
def waiter ():#line:1047
    O0OO0000OO0O0OO0O =20 #line:1050
    OOOO00O0O0O000OO0 =".ts1.txt"#line:1052
    if os .path .isfile (OOOO00O0O0O000OO0 ):#line:1053
        OOOO00O0O0O0O0O00 =np .loadtxt (OOOO00O0O0O000OO0 )#line:1054
    else :#line:1056
        OOOO00O0O0O0O0O00 =0.0 #line:1057
    O00000O0O0O00O0O0 =time .time ()#line:1060
    OOO0O0000O000O0O0 =O00000O0O0O00O0O0 -OOOO00O0O0O0O0O00 #line:1061
    if (OOO0O0000O000O0O0 <O0OO0000OO0O0OO0O ):#line:1063
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(OOO0O0000O000O0O0 ,O0OO0000OO0O0OO0O ))#line:1064
        return False #line:1065
    else :#line:1066
        OO0O0O0OOOOOO000O =open (OOOO00O0O0O000OO0 ,'w')#line:1067
        OO0O0O0OOOOOO000O .write (str (O00000O0O0O00O0O0 ))#line:1068
        OO0O0O0OOOOOO000O .close ()#line:1069
        return True #line:1070
def trycount (OO000O00O00O0O0O0 ,OO0OO0O0OOOO0OO0O ):#line:1072
    if os .path .isfile (OO000O00O00O0O0O0 ):#line:1074
        O0O00O0000000O000 =np .load (OO000O00O00O0O0O0 )#line:1075
    else :#line:1077
        O0O00O0000000O000 =np .zeros (1 ,dtype ='int8,bool')#line:1078
        O0O00O0000000O000 =[0 ,False ]#line:1079
    if not O0O00O0000000O000 [1 ]:#line:1082
        O0O00O0000000O000 [0 ]+=1 #line:1083
        O0O00O0000000O000 [1 ]=OO0OO0O0OOOO0OO0O #line:1084
        np .save (OO000O00O00O0O0O0 ,O0O00O0000000O000 )#line:1086
    return O0O00O0000000O000 #line:1088
def valdho (O000OO0000000O00O ,OOOOO000O0000O00O ):#line:1096
    OOOO000OOOOOOOO00 =".dho_counter.npy"#line:1100
    O00OO000OOOO0O00O =np .zeros (1 ,dtype ='int8,bool')#line:1102
    if (waiter ()):#line:1104
        while True :#line:1105
            try :#line:1106
                OO00O0O0O0O000OOO =float (input ("Please enter your estimate here: "))#line:1107
                O000OO00OOOO0OO0O =2 *np .sqrt (O000OO0000000O00O *OOOOO000O0000O00O )#line:1108
                OOO00O00OO0O0OOO0 =np .isclose (OO00O0O0O0O000OOO ,O000OO00OOOO0OO0O ,0.2 )#line:1109
                if OOO00O00OO0O0OOO0 :#line:1110
                    print ("Well done, that is close to the critical damping value ",O000OO00OOOO0OO0O )#line:1111
                else :#line:1112
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1113
                O00OO000OOOO0O00O =trycount (OOOO000OOOOOOOO00 ,OOO00O00OO0O0OOO0 )#line:1115
                O0O0OO000OO0000O0 =100 -(O00OO000OOOO0O00O [0 ]-1 )*10 #line:1116
                if O00OO000OOOO0O00O [1 ]:#line:1117
                    print ("First success after ",O00OO000OOOO0O00O [0 ]," tries, you have ",O0O0OO000OO0000O0 ,"% on this exercise.")#line:1118
                else :#line:1119
                    print ("You have had ",O00OO000OOOO0O00O [0 ]," tries.")#line:1120
                    print ("If next try is accepted you will achieve ",O0O0OO000OO0000O0 -10 ,"% on this exercise.")#line:1121
                break #line:1123
            except ValueError :#line:1125
                print ("I didn't understand that.")#line:1126
                continue #line:1127
        return #line:1130
def valdrivendho (OO00O00O0O00000OO ,OOO0O0O0O0O0O00OO ):#line:1140
    OOOO0O000OOO0OOOO =".drivendho_counter.npy"#line:1144
    OOOO00OOOOO000O00 =np .zeros (1 ,dtype ='int8,bool')#line:1146
    if (waiter ()):#line:1148
        while True :#line:1149
            try :#line:1150
                O0OO000O000OO0OO0 =float (input ("Please enter your estimate here: "))#line:1151
                O0000000O00O00OO0 =np .sqrt (OO00O00O0O00000OO **2 -2 *OOO0O0O0O0O0O00OO **2 )#line:1152
                OO0OO0O0O00OOOOOO =np .isclose (O0OO000O000OO0OO0 ,O0000000O00O00OO0 ,0.2 )#line:1153
                if OO0OO0O0O00OOOOOO :#line:1154
                    print ("Well done, that is close to the resonance value ",O0000000O00O00OO0 )#line:1155
                else :#line:1156
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1157
                OOOO00OOOOO000O00 =trycount (OOOO0O000OOO0OOOO ,OO0OO0O0O00OOOOOO )#line:1159
                O00OOOOO00O0000O0 =100 -(OOOO00OOOOO000O00 [0 ]-1 )*10 #line:1160
                if OOOO00OOOOO000O00 [1 ]:#line:1161
                    print ("First success after ",OOOO00OOOOO000O00 [0 ]," tries, you have ",O00OOOOO00O0000O0 ,"% on this exercise.")#line:1162
                else :#line:1163
                    print ("You have had ",OOOO00OOOOO000O00 [0 ]," tries.")#line:1164
                    print ("If next try is accepted you will achieve ",O00OOOOO00O0000O0 -10 ,"% on this exercise.")#line:1165
                break #line:1167
            except ValueError :#line:1169
                print ("I didn't understand that.")#line:1170
                continue #line:1171
        return #line:1174
import ipywidgets as widgets #line:1189
import sys #line:1190
from IPython .display import display #line:1191
from IPython .display import clear_output #line:1192
def create_multipleChoice_widget (O0OO00OO00OOOOO00 ,O00OO0OO000O0000O ,OO0O00OO0000OOOO0 ,OO00OO00000O00OOO ):#line:1194
    O00OOO0OOOOOO0000 ='.q{:d}_counter.npy'.format (O0OO00OO00OOOOO00 )#line:1195
    OOOOOO00O000000O0 =np .zeros (1 ,dtype ='int8,bool')#line:1196
    O0O00OO0O000O000O =len (OO0O00OO0000OOOO0 )#line:1198
    if OO00OO00000O00OOO not in OO0O00OO0000OOOO0 :#line:1199
        OO0O00OO0000OOOO0 .append (OO00OO00000O00OOO )#line:1200
    O0OOO0OO00OO00000 =OO0O00OO0000OOOO0 .index (OO00OO00000O00OOO )#line:1202
    O00000O00O000000O =[(O00000OO0O00O00O0 ,OOO00OOOO0O0O000O )for OOO00OOOO0O0O000O ,O00000OO0O00O00O0 in enumerate (OO0O00OO0000OOOO0 )]#line:1204
    OO0OO0OO0OOO00O0O =widgets .RadioButtons (options =O00000O00O000000O ,description ='',disabled =False )#line:1209
    O00O00O0O000O0000 =widgets .Output ()#line:1211
    with O00O00O0O000O0000 :#line:1212
        print (O00OO0OO000O0000O )#line:1213
    O0O00O0000O0000O0 =widgets .Output ()#line:1215
    def OO000O0O00OO0000O (O000OOO0O0000O000 ):#line:1217
        OOOOOOO0000OO00O0 =int (OO0OO0OO0OOO00O0O .value )#line:1219
        O0O0O00000O00O0O0 =OOOOOOO0000OO00O0 ==O0OOO0OO00OO00000 #line:1221
        O00OO0000OO0O0000 =trycount (O00OOO0OOOOOO0000 ,O0O0O00000O00O0O0 )#line:1222
        OOOOO0OOOOO0OO0OO =max (0 ,100 -(O00OO0000OO0O0000 [0 ]-1 )*100 /O0O00OO0O000O000O )#line:1223
        OO00000O0OOO00O00 =OO0OO0OO0OOO00O0O .options [OOOOOOO0000OO00O0 ][0 ]#line:1224
        if O0O0O00000O00O0O0 :#line:1225
            OO00000O0OOO00O00 +=' correct\n'#line:1226
        else :#line:1227
            OO00000O0OOO00O00 +=' incorrect\n'#line:1228
        if O00OO0000OO0O0000 [1 ]:#line:1229
            OO00000O0OOO00O00 +='{:.0f}% on try {:d}'.format (OOOOO0OOOOO0OO0OO ,O00OO0000OO0O0000 [0 ])#line:1230
        else :#line:1231
            OO00000O0OOO00O00 +='{:.0f}% remaining'.format (max (0 ,OOOOO0OOOOO0OO0OO -100 /O0O00OO0O000O000O ))#line:1232
        with O0O00O0000O0000O0 :#line:1234
            clear_output ()#line:1235
            print (OO00000O0OOO00O00 )#line:1236
        return #line:1237
    OO00OOOOO00OO000O =widgets .Button (description ="submit")#line:1239
    OO00OOOOO00OO000O .on_click (OO000O0O00OO0000O )#line:1240
    return widgets .VBox ([O00O00O0O000O0000 ,OO0OO0OO0OOO00O0O ,OO00OOOOO00OO000O ,O0O00O0000O0000O0 ])#line:1241
def runq1 ():#line:1248
    O0OOO0O0OO000000O =1 #line:1249
    OO000O00OO00OOO00 =create_multipleChoice_widget (O0OOO0O0OO000000O ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1250
    display (OO000O00OO00OOO00 )#line:1251
def runQ1 ():#line:1261
    OOO0000OO0O000000 =1 #line:1262
    O00OOO0O000000O00 =create_multipleChoice_widget (OOO0000OO0O000000 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1263
    display (O00OOO0O000000O00 )#line:1264
def runQ2x ():#line:1273
    O00O0OOO000000O00 =2 #line:1274
    O000OO00O0OO00O0O =create_multipleChoice_widget (O00O0OOO000000O00 ,'',['centred','backwards','forwards'],'centred')#line:1275
    display (O000OO00O0OO00O0O )#line:1276
def runQ3x ():#line:1284
    OOOO00OO0OO00O0OO =3 #line:1285
    OO0O0OO0O0O0OOO0O =create_multipleChoice_widget (OOOO00OO0OO00O0OO ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1286
    display (OO0O0OO0O0O0OOO0O )#line:1287
def runQ4x ():#line:1296
    O000O0OOO00OO000O =4 #line:1297
    O0000O00OO00O0OO0 =create_multipleChoice_widget (O000O0OOO00OO000O ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1298
    display (O0000O00OO00O0OO0 )#line:1299
def runQ5x ():#line:1309
    OO000OOO000O00OO0 =5 #line:1310
    OOO000OOOOO000000 =create_multipleChoice_widget (OO000OOO000O00OO0 ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1311
    display (OOO000OOOOO000000 )#line:1312
def runQ6x ():#line:1321
    O0O0O0O0OO0000O00 =6 #line:1322
    OOO000OOO00OO00O0 =create_multipleChoice_widget (O0O0O0O0OO0000O00 ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1323
    display (OOO000OOO00OO00O0 )#line:1324
def runQ7x ():#line:1333
    O000O000OOO0OO0O0 =7 #line:1334
    O0OOOOOOOOO0OOO00 =create_multipleChoice_widget (O000O000OOO0OO0O0 ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1335
    display (O0OOOOOOOOO0OOO00 )#line:1336
