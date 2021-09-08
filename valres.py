import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (OO0O00OOOO000O0O0 ,O0OO0OO0OO00OOOOO ):#line:10
        print ("\nPasswords may not be changed using this notebook at present.")#line:14
ps =[]#line:18
wd =''#line:19
def a1 ():#line:36
    global ps #line:38
    O00OO000000000O00 =".a1_counter.npy"#line:41
    OO0O00OOO0OOOOO0O =np .zeros (1 ,dtype ='int8,bool')#line:42
    O00OO0000O0OOO0O0 =0 #line:44
    O0OO0OO0O00000OOO =ps [0 ]#line:45
    OO000OOO0O0OO0000 =ps [1 ]#line:46
    if (waiter ()):#line:48
        while True :#line:49
            try :#line:50
                printmd ('**CA** (2%)')#line:51
                print (O0OO0OO0O00000OOO ,"+",OO000OOO0O0OO0000 )#line:52
                O0OOOOOOOO000O0OO =float (input ("Please enter your answer here: "))#line:53
                O000000OO0OO0O0O0 =O0OO0OO0O00000OOO +OO000OOO0O0OO0000 #line:54
                OO00O0O00OOOOOOO0 =np .isclose (O0OOOOOOOO000O0OO ,O000000OO0OO0O0O0 ,O00OO0000O0OOO0O0 )#line:55
                if OO00O0O00OOOOOOO0 :#line:56
                    print ("Well done, right answer is ",O000000OO0OO0O0O0 )#line:57
                else :#line:58
                    print ("Not right yet. Take another look then run this cell again.")#line:59
                OO0O00OOO0OOOOO0O =trycount (O00OO000000000O00 ,OO00O0O00OOOOOOO0 )#line:61
                O0O00O0O00OOOOO00 =100 -(OO0O00OOO0OOOOO0O [0 ]-1 )*10 #line:62
                if OO0O00OOO0OOOOO0O [1 ]:#line:63
                    print ("First success after ",OO0O00OOO0OOOOO0O [0 ]," tries, you have ",O0O00O0O00OOOOO00 ,"% on this exercise.")#line:64
                else :#line:65
                    print ("You have had ",OO0O00OOO0OOOOO0O [0 ]," tries.")#line:66
                    print ("If next try is accepted you will achieve ",O0O00O0O00OOOOO00 -10 ,"% on this exercise.")#line:67
                break #line:69
            except ValueError :#line:71
                print ("I didn't understand that.")#line:72
                continue #line:73
        return #line:75
def a2 (O0O0000O00OO00000 ):#line:84
    global ps #line:86
    O0O000O00OO0OO00O =".a2_counter.npy"#line:89
    O000O00OOOOO00OO0 =np .zeros (1 ,dtype ='int8,bool')#line:90
    OOOOO000O0O00OO0O =6 #line:93
    OOOO000O000O00O0O =7 #line:94
    O0O0O0O00OOOO00O0 =0 #line:96
    O0OO0O0O0OOO0000O =(ps [OOOOO000O0O00OO0O ])%6 +1 #line:98
    O00O00000O0O0OOO0 =(ps [OOOO000O000O00O0O ])%6 +1 #line:99
    while O0OO0O0O0OOO0000O +O00O00000O0O0OOO0 ==7 or O0OO0O0O0OOO0000O ==O00O00000O0O0OOO0 :#line:100
        O00O00000O0O0OOO0 +=1 #line:101
        O00O00000O0O0OOO0 =O00O00000O0O0OOO0 %6 +1 #line:102
    if (O0O0000O00OO00000 ):#line:104
        printmd ('**CA** (2%)')#line:105
        print ("Run your program (when you are happy it is working correctly) for a=",O0OO0O0O0OOO0000O ," and b=",O00O00000O0O0OOO0 )#line:106
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:107
        return #line:108
    if (waiter ()):#line:110
        while True :#line:111
            try :#line:112
                print ("Enter your program's result for a=",O0OO0O0O0OOO0000O ," and b=",O00O00000O0O0OOO0 )#line:113
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:114
                OO00000O00O00O000 =float (input ("Please enter your answer here: "))#line:115
                OOO0OO00OO0O00OOO =(3 *(O0OO0O0O0OOO0000O **3 *O00O00000O0O0OOO0 -O0OO0O0O0OOO0000O *O00O00000O0O0OOO0 **3 ))%7 #line:116
                OOOO000O0000OOOO0 =np .isclose (OO00000O00O00O000 ,OOO0OO00OO0O00OOO ,O0O0O0O00OOOO00O0 )#line:117
                if OOOO000O0000OOOO0 :#line:118
                    print ("Well done, right answer is ",OOO0OO00OO0O00OOO )#line:119
                else :#line:120
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:121
                O000O00OOOOO00OO0 =trycount (O0O000O00OO0OO00O ,OOOO000O0000OOOO0 )#line:123
                O000OOOOO0O00O00O =100 -(O000O00OOOOO00OO0 [0 ]-1 )*10 #line:124
                if O000O00OOOOO00OO0 [1 ]:#line:125
                    print ("First success after ",O000O00OOOOO00OO0 [0 ]," tries, you have ",O000OOOOO0O00O00O ,"% on this exercise.")#line:126
                else :#line:127
                    print ("You have had ",O000O00OOOOO00OO0 [0 ]," tries.")#line:128
                    print ("If next try is accepted you will achieve ",O000OOOOO0O00O00O -10 ,"% on this exercise.")#line:129
                break #line:131
            except ValueError :#line:133
                print ("I didn't understand that.")#line:134
                continue #line:135
        return #line:137
def a3_notlive (O0OO0OOOO000O0OO0 ):#line:146
    global ps #line:148
    OOO0O0O00000O0O00 =".a3_counter.npy"#line:151
    O0OOOO00OOOO0O0OO =np .zeros (1 ,dtype ='int8,bool')#line:152
    O00O00O00000000O0 =23 #line:155
    OO000OO00O0O0O00O =24 #line:156
    OO0000000O0O000OO =(ps [O00O00O00000000O0 ])%6 +1 #line:157
    OOO00OO0O0O0OOO0O =(ps [OO000OO00O0O0O00O ])%6 +1 #line:158
    OO00O000OO0O00O00 =0 #line:160
    OO0000000O0O000OO =10 *OO0000000O0O000OO +OOO00OO0O0O0OOO0O ;#line:162
    if (O0OO0OOOO000O0OO0 ):#line:164
        printmd ('**CA** (6%)')#line:165
        print ("Run your program for ",OO0000000O0O000OO ,"people")#line:166
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:167
        return #line:168
    if (waiter ()):#line:170
        while True :#line:171
            try :#line:172
                print ("Enter your program's result for",OO0000000O0O000OO ,"people")#line:173
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:174
                OOO00OOO000OO0O00 =float (input ("Please enter your answer here: "))#line:175
                O0O000O0O0OOOO0O0 =OO0000000O0O000OO +2 *OO0000000O0O000OO +2 *OO0000000O0O000OO +10 *OO0000000O0O000OO #line:176
                O0O00O0OOOO0O0OOO =np .isclose (OOO00OOO000OO0O00 ,O0O000O0O0OOOO0O0 ,OO00O000OO0O00O00 )#line:177
                if O0O00O0OOOO0O0OOO :#line:178
                    print ("Well done, right answer is ",O0O000O0O0OOOO0O0 )#line:179
                else :#line:180
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:181
                O0OOOO00OOOO0O0OO =trycount (OOO0O0O00000O0O00 ,O0O00O0OOOO0O0OOO )#line:183
                O0O0OOO00OO0OO00O =100 -(O0OOOO00OOOO0O0OO [0 ]-1 )*10 #line:184
                if O0OOOO00OOOO0O0OO [1 ]:#line:185
                    print ("First success after ",O0OOOO00OOOO0O0OO [0 ]," tries, you have ",O0O0OOO00OO0OO00O ,"% on this exercise.")#line:186
                else :#line:187
                    print ("You have had ",O0OOOO00OOOO0O0OO [0 ]," tries.")#line:188
                    print ("If next try is accepted you will achieve ",O0O0OOO00OO0OO00O -10 ,"% on this exercise.")#line:189
                break #line:191
            except ValueError :#line:193
                print ("I didn't understand that.")#line:194
                continue #line:195
        return #line:197
def a4_notlive (OO0000O000OO0O0O0 ):#line:208
        import random #line:210
        import requests #line:211
        global ps #line:213
        global wd #line:214
        O0O00O00O00O0OOO0 =".a4_counter.npy"#line:217
        O00OOO00O000OOO0O =np .zeros (1 ,dtype ='int8,bool')#line:218
        O00O0OO0OO00OOOOO =60 #line:221
        O0O0O000O0O0O0000 =61 #line:222
        O0000O00OOOO00O0O =62 #line:223
        OO00OOOO0O000000O =63 #line:224
        O00000O0OO00000OO =64 #line:225
        OOO0O0OO00O0OO0OO =0 #line:228
        if (OO0000O000OO0O0O0 ):#line:230
                OOOO0OOO0O0OOOO0O ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:232
                O00O0000OO00O0O0O =requests .get (OOOO0OOO0O0OOOO0O )#line:234
                O0O00OOOOOOO000O0 =O00O0000OO00O0O0O .content .splitlines ()#line:235
                random .seed (10 *ps [62 ]+ps [63 ])#line:236
                O0OO0OOO00OO000OO =4 +(10 *ps [64 ]+ps [65 ])%4 #line:237
                O0O0O00OO00000OO0 =True #line:238
                while O0O0O00OO00000OO0 :#line:239
                        O00OOO0OO0OO000OO =O0O00OOOOOOO000O0 [random .randint (0 ,len (O0O00OOOOOOO000O0 )-1 )].decode ("utf-8")#line:240
                        if len (O00OOO0OO0OO000OO )>7 and len (O00OOO0OO0OO000OO )<14 and O00OOO0OO0OO000OO [0 ].islower ():#line:242
                                O0O0O00OO00000OO0 =False #line:243
                                for O000O000OO0O000O0 in O00OOO0OO0OO000OO :#line:244
                                        if chr (ord (O000O000OO0O000O0 )+O0OO0OOO00OO000OO )>'z':#line:245
                                                O0O0O00OO00000OO0 =True #line:246
                O0OO0O000OO0O0O00 =len (O00OOO0OO0OO000OO )#line:248
                OOOO0O0OO0O0OOO00 =''#line:249
                for O0O0OO00OOOO0O000 in range (0 ,O0OO0O000OO0O0O00 ):#line:250
                        OOOO0O0OO0O0OOO00 +=chr (ord (O00OOO0OO0OO000OO [O0O0OO00OOOO0O000 ])+O0OO0OOO00OO000OO )#line:252
                print ('Your encoded word is',OOOO0O0OO0O0OOO00 )#line:254
                print ('Write your program in the cell below this one.\n')#line:255
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:257
                wd =O00OOO0OO0OO000OO #line:258
                return #line:259
        if (waiter ()):#line:261
                while True :#line:262
                        try :#line:263
                                printmd ('**CA** (6%)')#line:264
                                O0O0OOOO0OOOOOO00 =str (input ("Enter your DECODED word here: "))#line:265
                                OO0000OO00OOOO0OO =wd #line:266
                                O0O0O0O0OO0000OOO =O0O0OOOO0OOOOOO00 ==OO0000OO00OOOO0OO #line:267
                                if O0O0O0O0OO0000OOO :#line:268
                                        print ("Well done, right answer is ",OO0000OO00OOOO0OO )#line:269
                                else :#line:270
                                        print ("Not right yet. Take another look then run this cell again.")#line:271
                                O00OOO00O000OOO0O =trycount (O0O00O00O00O0OOO0 ,O0O0O0O0OO0000OOO )#line:273
                                O0OO00000O00OO00O =100 -(O00OOO00O000OOO0O [0 ]-1 )*10 #line:274
                                if O00OOO00O000OOO0O [1 ]:#line:275
                                        print ("First success after ",O00OOO00O000OOO0O [0 ]," tries, you have ",O0OO00000O00OO00O ,"% on this exercise.")#line:276
                                else :#line:277
                                        print ("You have had ",O00OOO00O000OOO0O [0 ]," tries.")#line:278
                                        print ("If next try is accepted you will achieve ",O0OO00000O00OO00O -10 ,"% on this exercise.")#line:279
                                break #line:280
                        except ValueError :#line:282
                                print ("I didn't understand that.")#line:283
                                continue #line:284
                return #line:286
def a5_notlive (O0000OOO0OOOO0000 ):#line:296
        import random #line:298
        import requests #line:299
        global ps #line:301
        global P0 #line:302
        OOO00O0O0O00OO0O0 =".a5_counter.npy"#line:306
        OOOOO0000O0O0OO00 =np .zeros (1 ,dtype ='int8,bool')#line:307
        O000O0OO00O00000O =70 #line:310
        O000000OO000O0000 =71 #line:311
        O00O00OOO0O00O000 =72 #line:312
        O000O0O00OOOOOOO0 =73 #line:313
        O0000OO00O00O0O00 =74 #line:314
        O0OOOO0OO00O0OO0O =0 #line:317
        if (O0000OOO0OOOO0000 ):#line:319
                P0 =[]#line:320
                O0O0000O0OOO0OO00 =7 +(10 *ps [O000O0OO00O00000O ]+ps [O000000OO000O0000 ])%4 #line:321
                for OOOO0OOO0O000OO0O in range (O0O0000O0OOO0OO00 ):#line:322
                        P0 .append (max (0 ,ps [O00O00OOO0O00O000 +OOOO0OOO0O000OO0O ]-1 ))#line:323
                print ('Run your program for the list below:\n',P0 )#line:324
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:326
        elif (waiter ()):#line:328
                while True :#line:329
                        try :#line:330
                                printmd ('**CA** (6%)')#line:333
                                O0O000OO00O000OOO =eval (input ("Enter your list here: "))#line:334
                                OOO000O0OO0000OOO =3 #line:339
                                OOOOOO000OOO000OO =P0 .copy ()#line:340
                                OOOOOO000OOO000OO .append (0 )#line:341
                                print (OOOOOO000OOO000OO )#line:342
                                O0O0000O0OOO0OO00 =len (P0 )#line:343
                                for OO0O000O0OO00O0O0 in range (OOO000O0OO0000OOO ):#line:344
                                        for OOOO0OOO0O000OO0O in range (O0O0000O0OOO0OO00 ):#line:345
                                                OOOOOO000OOO000OO [OOOO0OOO0O000OO0O ]=OOOOOO000OOO000OO [OOOO0OOO0O000OO0O +1 ]*(OOOO0OOO0O000OO0O +1 )#line:347
                                OOOOOO000OOO000OO .pop ()#line:348
                                O0O0000OOOO0O0O0O =OOOOOO000OOO000OO #line:351
                                if not type (O0O000OO00O000OOO )==type (O0O0000OOOO0O0O0O ):#line:353
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:354
                                elif not len (O0O000OO00O000OOO )==len (O0O0000OOOO0O0O0O ):#line:355
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:356
                                else :#line:357
                                        O000O00OOOO0OO00O =O0O000OO00O000OOO ==O0O0000OOOO0O0O0O #line:358
                                        if O000O00OOOO0OO00O :#line:359
                                                print ("Well done, right answer is ",O0O0000OOOO0O0O0O )#line:360
                                        else :#line:361
                                                print ("Not right yet. Take another look then run this cell again.")#line:362
                                        OOOOO0000O0O0OO00 =trycount (OOO00O0O0O00OO0O0 ,O000O00OOOO0OO00O )#line:364
                                        OOO0OOO00O000OOOO =100 -(OOOOO0000O0O0OO00 [0 ]-1 )*10 #line:365
                                        if OOOOO0000O0O0OO00 [1 ]:#line:366
                                                print ("First success after ",OOOOO0000O0O0OO00 [0 ]," tries, you have ",OOO0OOO00O000OOOO ,"% on this exercise.")#line:367
                                        else :#line:368
                                                print ("You have had ",OOOOO0000O0O0OO00 [0 ]," tries.")#line:369
                                                print ("If next try is accepted you will achieve ",OOO0OOO00O000OOOO -10 ,"% on this exercise.")#line:370
                                        break #line:371
                                OOOOOO000OOO000OO =None #line:374
                                O0O0000OOOO0O0O0O =None #line:375
                        except ValueError :#line:376
                                print ("I didn't understand that.")#line:377
                                continue #line:378
        return #line:380
def a6_notlive (OO00OO0000O0O0OOO ):#line:389
        import random #line:391
        import requests #line:392
        global ps #line:394
        global P0 #line:395
        O0OO00O0O0OO0O000 =".a6_counter.npy"#line:399
        O00OOOO0OO0OO00OO =np .zeros (1 ,dtype ='int8,bool')#line:400
        O000O0OO000OOO000 =11 #line:403
        OOO000OO000O00O00 =16 #line:404
        O0000O00O0OO0OOOO =7 #line:405
        O00O00O0O0OOOOO00 =33 #line:406
        O000O0O0OO0O00O00 =21 #line:407
        O00O0O0OOO0OOOO00 =0 #line:410
        if (OO00OO0000O0O0OOO ):#line:412
                O0OO0OOOO0O0OOOO0 =ps [O000O0OO000OOO000 ]+ps [OOO000OO000O00O00 ]+ps [O0000O00O0OO0OOOO ]+ps [O00O00O0O0OOOOO00 ]+ps [O000O0O0OO0O00O00 ]#line:413
                random .seed (O0OO0OOOO0O0OOOO0 )#line:414
                P0 =random .randint (1000 ,2000 )#line:415
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:416
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:418
        elif (waiter ()):#line:420
                while True :#line:421
                        try :#line:422
                                printmd ('**CA** (6%)')#line:425
                                OOO0O0O00O0000OOO =eval (input ("Enter your stopping number here: "))#line:426
                                O0000O00000O00OOO =P0 #line:430
                                O0OOOOOO0OOO00OOO =[O0000O00000O00OOO ]#line:431
                                while not O0000O00000O00OOO ==1 :#line:432
                                        if O0000O00000O00OOO %2 :#line:433
                                                O0000O00000O00OOO =3 *O0000O00000O00OOO +1 #line:434
                                        else :#line:435
                                                O0000O00000O00OOO =O0000O00000O00OOO //2 #line:436
                                        O0OOOOOO0OOO00OOO .append (O0000O00000O00OOO )#line:437
                                OO0O0OOOO000000OO =len (O0OOOOOO0OOO00OOO )#line:438
                                OO0O00OOO000O0000 =OO0O0OOOO000000OO #line:442
                                if not type (OOO0O0O00O0000OOO )==type (OO0O00OOO000O0000 ):#line:444
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:445
                                else :#line:448
                                        OOOO00OOOOO0OO0OO =OOO0O0O00O0000OOO ==OO0O00OOO000O0000 #line:449
                                        if OOOO00OOOOO0OO0OO :#line:450
                                                print ("Well done, right answer is ",OO0O00OOO000O0000 )#line:451
                                        else :#line:452
                                                print ("Not right yet. Take another look then run this cell again.")#line:453
                                        O00OOOO0OO0OO00OO =trycount (O0OO00O0O0OO0O000 ,OOOO00OOOOO0OO0OO )#line:455
                                        O0O000000000OOO00 =100 -(O00OOOO0OO0OO00OO [0 ]-1 )*10 #line:456
                                        if O00OOOO0OO0OO00OO [1 ]:#line:457
                                                print ("First success after ",O00OOOO0OO0OO00OO [0 ]," tries, you have ",O0O000000000OOO00 ,"% on this exercise.")#line:458
                                        else :#line:459
                                                print ("You have had ",O00OOOO0OO0OO00OO [0 ]," tries.")#line:460
                                                print ("If next try is accepted you will achieve ",O0O000000000OOO00 -10 ,"% on this exercise.")#line:461
                                        break #line:462
                                OO0O0OOOO000000OO =None #line:465
                                OO0O00OOO000O0000 =None #line:466
                        except ValueError :#line:467
                                print ("I didn't understand that.")#line:468
                                continue #line:469
        return #line:471
def a7_notlive (O0O0000O00000O0O0 ):#line:481
        OO0OOO0000O00O000 =".a7_counter.npy"#line:485
        OO0O0O0O0000OOO0O =np .zeros (1 ,dtype ='int8,bool')#line:486
        def OO0OOOO00O0OOOOOO ():#line:488
                pass #line:489
        O00O0OO0OOOOOOOO0 =[(30 ,10 )]#line:492
        OOOO00O0O0OO00OOO =1.0e-4 #line:495
        if (waiter ()):#line:498
                printmd ('**CA** (6%)')#line:500
                if not type (O0O0000O00000O0O0 )==type (OO0OOOO00O0OOOOOO ):#line:502
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:503
                else :#line:506
                        def O0000OO0OO0000OOO (O00O00O00OO0O0OO0 ,OO00O00O00OO0OOOO ):#line:509
                                import math #line:510
                                O00O000O00OO00OO0 =9.81 #line:511
                                O0000000000OO0OO0 =math .pi *OO00O00O00OO0OOOO /180. #line:512
                                O0OO00O00OO0OOO00 =O00O00O00OO0O0OO0 **2 *math .sin (2 *O0000000000OO0OO0 )/O00O000O00OO00OO0 #line:513
                                OO0000OO00O0O000O =O00O00O00OO0O0OO0 **2 *(math .sin (O0000000000OO0OO0 ))**2 /(2. *O00O000O00OO00OO0 )#line:514
                                return O0OO00O00OO0OOO00 ,OO0000OO00O0O000O #line:515
                        import random as r #line:518
                        O00O0OO0OOOOOOOO0 =[]#line:519
                        OOOO0000OO000O0OO =False #line:520
                        OOOO000OO00O0000O =[]#line:521
                        O0OO0O00OOOOOO0OO =10 #line:522
                        O000O000O0O0OOO0O =100 #line:523
                        OOO00O00OO0OOO0OO =5 #line:524
                        O0O0OO0000O00OOO0 =85 #line:525
                        for OO0O0O00000O0OOOO in range (5 ):#line:526
                                O00O0OO0OOOOOOOO0 .append ((r .uniform (O0OO0O00OOOOOO0OO ,O000O000O0O0OOO0O ),r .uniform (OOO00O00OO0OOO0OO ,O0O0OO0000O00OOO0 )))#line:527
                        for (O0OO0OOOOO00OOO0O ,O00OOOOOO0OO0OOO0 )in O00O0OO0OOOOOOOO0 :#line:528
                                print ('Testing:',O0OO0OOOOO00OOO0O ,O00OOOOOO0OO0OOO0 )#line:529
                                O000OO00O0O0OO000 =O0O0000O00000O0O0 (O0OO0OOOOO00OOO0O ,O00OOOOOO0OO0OOO0 )#line:530
                                print ('Output:',*O000OO00O0O0OO000 )#line:531
                                OO00OO0000O00O000 =O0000OO0OO0000OOO (O0OO0OOOOO00OOO0O ,O00OOOOOO0OO0OOO0 )#line:532
                                print ('Actual:',*OO00OO0000O00O000 )#line:533
                                print ()#line:534
                                if (not type (O000OO00O0O0OO000 )==type (OO00OO0000O00O000 ))or (not len (O000OO00O0O0OO000 )==len (OO00OO0000O00O000 )):#line:535
                                        if OOOO0000OO000O0OO ==False :#line:536
                                           OOOO0000OO000O0OO =True #line:537
                                else :#line:538
                                        OOOO000OO00O0000O .append (all (np .isclose (O000OO00O0O0OO000 ,OO00OO0000O00O000 ,OOOO00O0O0OO00OOO )))#line:539
                        if OOOO0000OO000O0OO :#line:541
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:542
                        else :#line:544
                                OOOOOO0O0O000O0OO =all (OOOO000OO00O0000O )#line:545
                                if OOOOOO0O0O000O0OO :#line:546
                                        print ("Well done, all correct.")#line:547
                                else :#line:548
                                        print ("Not right yet. Take another look then run this cell again.")#line:549
                                OO0O0O0O0000OOO0O =trycount (OO0OOO0000O00O000 ,OOOOOO0O0O000O0OO )#line:551
                                O0O00O0O00OO0O000 =100 -(OO0O0O0O0000OOO0O [0 ]-1 )*10 #line:552
                                if OO0O0O0O0000OOO0O [1 ]:#line:553
                                        print ("First success after ",OO0O0O0O0000OOO0O [0 ]," tries, you have ",O0O00O0O00OO0O000 ,"% on this exercise.")#line:554
                                else :#line:555
                                        print ("You have had ",OO0O0O0O0000OOO0O [0 ]," tries.")#line:556
                                        print ("If next try is accepted you will achieve ",O0O00O0O00OO0O000 -10 ,"% on this exercise.")#line:557
                        OO00OO0000O00O000 =None #line:560
                        O0000OO0OO0000OOO =None #line:561
        return #line:563
def a8_notlive (OOOOO0OO0OO0O0000 ):#line:573
        O000O0O0O0OOO0000 =".a8_counter.npy"#line:577
        O0O00O000OO0O00O0 =np .zeros (1 ,dtype ='int8,bool')#line:578
        def OOO0O0O0OO0000000 ():#line:580
                pass #line:581
        OO0OOO0O0O000O0OO =1.0e-4 #line:585
        if (waiter ()):#line:588
                printmd ('**CA** (6%)')#line:590
                if not type (OOOOO0OO0OO0O0000 )==type (OOO0O0O0OO0000000 ):#line:594
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:595
                else :#line:599
                        import inspect #line:602
                        OOO00O0OO00OO00O0 =inspect .getsourcelines (OOOOO0OO0OO0O0000 )#line:603
                        OO0OO0OOOOOOO0O00 =True #line:604
                        O0O0O0O000OOO000O =[]#line:605
                        for OO0OO0OOO00OOOOOO ,O000OOO00O0O0OOO0 in enumerate (OOO00O0OO00OO00O0 [0 ]):#line:606
                                if 'for'in O000OOO00O0O0OOO0 or 'while'in O000OOO00O0O0OOO0 :#line:607
                                        OO0OO0OOOOOOO0O00 =False #line:609
                                        O0O0O0O000OOO000O .append (OO0OO0OOO00OOOOOO )#line:610
                        if not OO0OO0OOOOOOO0O00 :#line:611
                                print ('Function needs to be written without loops (using NumPy), check lines',*O0O0O0O000OOO000O )#line:612
                                print ('No marks lost for this attempt.')#line:613
                                return #line:614
                        def OO0OOO00OOOO0OOO0 (O0000O00OOOO0OOO0 ):#line:617
                                O0OO0OOOO0O000O00 =np .vstack ((O0000O00OOOO0OOO0 ,O0000O00OOOO0OOO0 [0 ]))#line:618
                                O0O0O0O00O00O0OOO =sum (O0OO0OOOO0O000O00 [:-1 ,0 ]*O0OO0OOOO0O000O00 [1 :,1 ])#line:619
                                OOO00OOO00OO0000O =sum (O0OO0OOOO0O000O00 [:-1 ,1 ]*O0OO0OOOO0O000O00 [1 :,0 ])#line:620
                                return abs (O0O0O0O00O00O0OOO -OOO00OOO00OO0000O )/2 #line:621
                        import random as r #line:624
                        O00OOOOOO0OO00OOO =r .randint (6 ,11 )#line:625
                        OOO000O0OOOOO000O =np .ones ((O00OOOOOO0OO00OOO ,2 ))#line:626
                        OOOO00OO00OO0OO0O =False #line:627
                        OO00O000OOO0O00OO =[]#line:628
                        O00OOO0O0OO00OOO0 =1. #line:629
                        O0O000OO0O00O0O00 =20. #line:630
                        O0OOOOO00O0OO00O0 =O00OOO0O0OO00OOO0 #line:631
                        OO0OOOO0O00O0O0OO =O0O000OO0O00O0O00 #line:632
                        for O000O000O0000O000 in range (O00OOOOOO0OO00OOO ):#line:633
                                OOO000O0OOOOO000O [O000O000O0000O000 ]=[r .uniform (O00OOO0O0OO00OOO0 ,O0O000OO0O00O0O00 ),r .uniform (O0OOOOO00O0OO00O0 ,OO0OOOO0O00O0O0OO )]#line:634
                        print ('Testing:',OOO000O0OOOOO000O )#line:635
                        O00O0O000O000000O =OOOOO0OO0OO0O0000 (OOO000O0OOOOO000O )#line:636
                        print ('Output:',O00O0O000O000000O )#line:637
                        O0O00OO000OOO0O0O =OO0OOO00OOOO0OOO0 (OOO000O0OOOOO000O )#line:638
                        print ('Actual:',O0O00OO000OOO0O0O )#line:639
                        print ()#line:640
                        if not type (O00O0O000O000000O )==type (O0O00OO000OOO0O0O ):#line:641
                                if OOOO00OO00OO0OO0O ==False :#line:642
                                        OOOO00OO00OO0OO0O =True #line:643
                        else :#line:644
                                OO00O000OOO0O00OO .append (np .isclose (O00O0O000O000000O ,O0O00OO000OOO0O0O ,OO0OOO0O0O000O0OO ))#line:645
                        if OOOO00OO00OO0OO0O :#line:647
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:648
                        else :#line:650
                                O0O0OOOOO00O0OO00 =all (OO00O000OOO0O00OO )#line:651
                                if O0O0OOOOO00O0OO00 :#line:652
                                        print ("Well done, all correct.")#line:653
                                else :#line:654
                                        print ("Not right yet. Take another look then run this cell again.")#line:655
                                O0O00O000OO0O00O0 =trycount (O000O0O0O0OOO0000 ,O0O0OOOOO00O0OO00 )#line:657
                                OOOO0O0OOO00OOOO0 =100 -(O0O00O000OO0O00O0 [0 ]-1 )*10 #line:658
                                if O0O00O000OO0O00O0 [1 ]:#line:659
                                        print ("First success after ",O0O00O000OO0O00O0 [0 ]," tries, you have ",OOOO0O0OOO00OOOO0 ,"% on this exercise.")#line:660
                                else :#line:661
                                        print ("You have had ",O0O00O000OO0O00O0 [0 ]," tries.")#line:662
                                        print ("If next try is accepted you will achieve ",OOOO0O0OOO00OOOO0 -10 ,"% on this exercise.")#line:663
                        O0O00OO000OOO0O0O =None #line:666
                        OO0OOO00OOOO0OOO0 =None #line:667
        return #line:669
def a1_notlive ():#line:685
        print ('This CA test is not currently live.')#line:686
        return #line:687
def a2_notlive (OO0O0OOOOO0000OOO ):#line:695
        print ('This CA test is not currently live.')#line:696
        return #line:697
def a3 (OOO00O00O0OOO0OOO ):#line:705
        print ('This CA test is not currently live.')#line:706
        return #line:707
def a4 (OO00O000O00OOO0O0 ):#line:715
        print ('This CA test is not currently live.')#line:716
        return #line:717
def a5 (O0O00OO0O00OOOOOO ):#line:725
        print ('This CA test is not currently live.')#line:726
        return #line:727
def a6 (O0O0000OO0OO00O0O ):#line:735
        print ('This CA test is not currently live.')#line:736
        return #line:737
def a7 ():#line:745
        print ('This CA test is not currently live.')#line:746
        return #line:747
def a8 (OO0OO0000OO000OOO ):#line:755
        print ('This CA test is not currently live.')#line:756
        return #line:757
def b1 ():#line:775
    global ps #line:777
    OO0000OOOOO0OO0OO =".b1_counter.npy"#line:780
    OOOOO0O00OOO00O00 =np .zeros (1 ,dtype ='int8,bool')#line:781
    OOO0OOO0OO00OO00O =0.05 #line:783
    if (waiter ()):#line:785
        while True :#line:786
            try :#line:787
                printmd ('**CA**')#line:788
                OOO00OO0O00O00O0O =eval (input ("Please enter your answer here in the format D,k: "))#line:789
                O000OO00OOO0OO0OO =(0.025 ,2.0 )#line:790
                OO000O00O00O000O0 =all (np .isclose (OOO00OO0O00O00O0O ,O000OO00OOO0OO0OO ,rtol =OOO0OOO0OO00OO00O ))#line:791
                if OO000O00O00O000O0 :#line:792
                    print ("Well done, reasonable estimate is ",O000OO00OOO0OO0OO )#line:793
                else :#line:794
                    print ("Not right yet. Take another look then run this cell again.")#line:795
                OOOOO0O00OOO00O00 =trycount (OO0000OOOOO0OO0OO ,OO000O00O00O000O0 )#line:797
                OO000000O0O0OO0O0 =100 -(OOOOO0O00OOO00O00 [0 ]-1 )*10 #line:798
                if OOOOO0O00OOO00O00 [1 ]:#line:799
                    print ("First success after ",OOOOO0O00OOO00O00 [0 ]," tries, you have ",OO000000O0O0OO0O0 ,"% on this exercise.")#line:800
                else :#line:801
                    print ("You have had ",OOOOO0O00OOO00O00 [0 ]," tries.")#line:802
                    print ("If next try is accepted you will achieve ",OO000000O0O0OO0O0 -10 ,"% on this exercise.")#line:803
                break #line:805
            except ValueError :#line:807
                print ("I didn't understand that.")#line:808
                continue #line:809
        return #line:811
def b2 (O0O00O000O0OOO0OO ):#line:821
        OO0OOO0O0O0O0O00O =".b2_counter.npy"#line:825
        OO0O0OOOO0OO00OOO =np .zeros (1 ,dtype ='int8,bool')#line:826
        def O000O0OOO0O000000 ():#line:828
                pass #line:829
        O00O0OOOO000OO00O =1.0e-2 #line:832
        OOO000O0O000OO0O0 =0.0 #line:833
        if (waiter ()):#line:835
                printmd ('**CA**')#line:837
                if not type (O0O00O000O0OOO0OO )==type (O000O0OOO0O000000 ):#line:839
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:840
                else :#line:843
                        def OOO00OOO0O0OO00OO (O00O0OO0OO0O00OO0 ):#line:847
                                O0O0OOOO0OO00OOO0 =[]#line:848
                                OOO0O0O00O00O000O =20.0 #line:849
                                OO0OO0000OOOO00O0 =58.1e-3 #line:850
                                OO0OO0O00000O0000 =9.81 #line:851
                                OOO0OOOOO000OOOOO =0.0 #line:852
                                O0O00OO0OOO00O0O0 =0.0 #line:853
                                O0OO00O00O0000O00 =0.0 #line:854
                                O0O000OOOO00OO0OO =10 #line:855
                                OO0OOO0OOO0OO0O00 =3.35e-2 #line:856
                                O00OOOOOO0O0O0O0O =0.51 #line:857
                                OOOO00OO0O00O0000 =1.25 #line:858
                                OOO00O000OO0O000O =math .pi *OO0OOO0OOO0OO0O00 **2 #line:859
                                OO000OO0000O0O00O =0.5 *O00OOOOOO0O0O0O0O *OOO00O000OO0O000O *OOOO00OO0O00O0000 #line:860
                                OOO0OOOOO0000O00O =100000 #line:862
                                OO0OO0000000O0OO0 =np .zeros (OOO0OOOOO0000O00O ,float )#line:863
                                O000OOOOOOOOOOO00 =np .zeros (OOO0OOOOO0000O00O ,float )#line:864
                                OOOO0OOO0O00O0OO0 =np .zeros (OOO0OOOOO0000O00O ,float )#line:865
                                OO0000OOO0OO0O0OO =np .zeros (OOO0OOOOO0000O00O ,float )#line:866
                                O00OOOOOOOO00OO0O =np .zeros (OOO0OOOOO0000O00O ,float )#line:867
                                OO0O0000OO0OOOO00 =np .zeros (OOO0OOOOO0000O00O ,float )#line:868
                                O0O00O000OO0000O0 =np .zeros (OOO0OOOOO0000O00O ,float )#line:869
                                OO0OO0000000O0OO0 ,OO0000O00O00O00OO =np .linspace (O0OO00O00O0000O00 ,O0O000OOOO00OO0OO ,OOO0OOOOO0000O00O ,retstep =True )#line:870
                                for O0OOOO0000OO000O0 in O00O0OO0OO0O00OO0 :#line:872
                                        OO00OO0O0OOO0OO00 =OOO0O0O00O00O000O *math .cos (O0OOOO0000OO000O0 )#line:873
                                        O00O0OOO0O000O0OO =OOO0O0O00O00O000O *math .sin (O0OOOO0000OO000O0 )#line:874
                                        OO0O0000OO0OOOO00 [0 ]=OOO0OOOOO000OOOOO #line:876
                                        O0O00O000OO0000O0 [0 ]=O0O00OO0OOO00O0O0 #line:877
                                        OO0000OOO0OO0O0OO [0 ]=OO00OO0O0OOO0OO00 #line:878
                                        O00OOOOOOOO00OO0O [0 ]=O00O0OOO0O000O0OO #line:879
                                        for O00000O0O0OOO0OOO in range (OOO0OOOOO0000O00O -1 ):#line:880
                                                OOO0000O000O0OO0O =math .sqrt (OO0000OOO0OO0O0OO [O00000O0O0OOO0OOO ]**2 +O00OOOOOOOO00OO0O [O00000O0O0OOO0OOO ]**2 )#line:881
                                                OO00O00000O00OO00 =-OO000OO0000O0O00O *OOO0000O000O0OO0O *OO0000OOO0OO0O0OO [O00000O0O0OOO0OOO ]#line:882
                                                O000OOOOOOOOOOO00 [O00000O0O0OOO0OOO ]=OO00O00000O00OO00 /OO0OO0000OOOO00O0 #line:883
                                                OO0000OOO0OO0O0OO [O00000O0O0OOO0OOO +1 ]=OO0000OOO0OO0O0OO [O00000O0O0OOO0OOO ]+O000OOOOOOOOOOO00 [O00000O0O0OOO0OOO ]*OO0000O00O00O00OO #line:884
                                                OO0O0000OO0OOOO00 [O00000O0O0OOO0OOO +1 ]=OO0O0000OO0OOOO00 [O00000O0O0OOO0OOO ]+OO0000OOO0OO0O0OO [O00000O0O0OOO0OOO +1 ]*OO0000O00O00O00OO #line:885
                                                OOO0OO0O00O0000O0 =-OO0OO0000OOOO00O0 *OO0OO0O00000O0000 -OO000OO0000O0O00O *OOO0000O000O0OO0O *O00OOOOOOOO00OO0O [O00000O0O0OOO0OOO ]#line:886
                                                OOOO0OOO0O00O0OO0 [O00000O0O0OOO0OOO ]=OOO0OO0O00O0000O0 /OO0OO0000OOOO00O0 #line:887
                                                O00OOOOOOOO00OO0O [O00000O0O0OOO0OOO +1 ]=O00OOOOOOOO00OO0O [O00000O0O0OOO0OOO ]+OOOO0OOO0O00O0OO0 [O00000O0O0OOO0OOO ]*OO0000O00O00O00OO #line:888
                                                O0O00O000OO0000O0 [O00000O0O0OOO0OOO +1 ]=O0O00O000OO0000O0 [O00000O0O0OOO0OOO ]+O00OOOOOOOO00OO0O [O00000O0O0OOO0OOO +1 ]*OO0000O00O00O00OO #line:889
                                                if (O0O00O000OO0000O0 [O00000O0O0OOO0OOO +1 ]<0 ):#line:890
                                                        break #line:891
                                        OOOO0O0OO0000O0O0 =O00000O0O0OOO0OOO #line:892
                                        O0O0OOOO0OO00OOO0 .append (OO0O0000OO0OOOO00 [OOOO0O0OO0000O0O0 ])#line:893
                                return (O0O0OOOO0OO00OOO0 );#line:895
                        import random as r #line:898
                        OOO0000OOO0O0000O =[]#line:899
                        OOO0OOO0OOO000O0O =False #line:900
                        O0OOOO0O00OO00000 =[]#line:901
                        O0OOO00O00O0O0OOO =0.1 #line:902
                        O000O0OO00000OOOO =1.5 #line:903
                        for OO00O00OO00000000 in range (5 ):#line:904
                                OOO0000OOO0O0000O .append (r .uniform (O0OOO00O00O0O0OOO ,O000O0OO00000OOOO ))#line:905
                        OOO0000OOO0O0000O .sort ()#line:906
                        print ('Testing thetas=',OOO0000OOO0O0000O )#line:907
                        OO0O0000O00000OO0 =O0O00O000O0OOO0OO (OOO0000OOO0O0000O )#line:908
                        print ('Output ximpacts=',OO0O0000O00000OO0 )#line:909
                        OO0OO0O000O000OO0 =OOO00OOO0O0OO00OO (OOO0000OOO0O0000O )#line:910
                        print ('Actual ximpacts=',OO0OO0O000O000OO0 )#line:911
                        print ()#line:912
                        if (not type (OO0O0000O00000OO0 )==type (OO0OO0O000O000OO0 ))or (not len (OO0O0000O00000OO0 )==len (OO0OO0O000O000OO0 )):#line:913
                                if OOO0OOO0OOO000O0O ==False :#line:914
                                        OOO0OOO0OOO000O0O =True #line:915
                        else :#line:916
                                O0OOOO0O00OO00000 .append (all (np .isclose (OO0O0000O00000OO0 ,OO0OO0O000O000OO0 ,rtol =O00O0OOOO000OO00O ,atol =OOO000O0O000OO0O0 )))#line:917
                        if OOO0OOO0OOO000O0O :#line:919
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:920
                        else :#line:922
                                O0OOOOOOOOO0O0O00 =all (O0OOOO0O00OO00000 )#line:923
                                if O0OOOOOOOOO0O0O00 :#line:924
                                        print ("Well done, all correct.")#line:925
                                else :#line:926
                                        print ("Not close enough. Take another look then run this cell again.")#line:927
                                OO0O0OOOO0OO00OOO =trycount (OO0OOO0O0O0O0O00O ,O0OOOOOOOOO0O0O00 )#line:929
                                O0O000O000O0O0000 =100 -(OO0O0OOOO0OO00OOO [0 ]-1 )*10 #line:930
                                if OO0O0OOOO0OO00OOO [1 ]:#line:931
                                        print ("First success after ",OO0O0OOOO0OO00OOO [0 ]," tries, you have ",O0O000O000O0O0000 ,"% on this exercise.")#line:932
                                else :#line:933
                                        print ("You have had ",OO0O0OOOO0OO00OOO [0 ]," tries.")#line:934
                                        print ("If next try is accepted you will achieve ",O0O000O000O0O0000 -10 ,"% on this exercise.")#line:935
                        OO0OO0O000O000OO0 =None #line:938
                        OOO00OOO0O0OO00OO =None #line:939
        return #line:941
def b3 ():#line:951
    global ps #line:953
    O00OO0O000O00OO00 =".b3_counter.npy"#line:956
    O0O0O0OOOOOO0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:957
    O0000OO0O0OO0O000 =0.01 #line:960
    if (waiter ()):#line:962
        while True :#line:963
            try :#line:964
                printmd ('**CA**')#line:965
                OO00O0OOO0O0O0O00 =float (input ("Enter a real number here: "))#line:966
                OOO0000O0000O0O00 =0.5 #line:967
                OOO00O00O000O00OO =np .isclose (OO00O0OOO0O0O0O00 ,OOO0000O0000O0O00 ,atol =O0000OO0O0OO0O000 )#line:968
                if OOO00O00O000O00OO :#line:969
                    print ("Well done. Actual value is ",OOO0000O0000O0O00 )#line:970
                else :#line:971
                    print ("Not right yet. Take another look then run this cell again.")#line:972
                O0O0O0OOOOOO0OO0O =trycount (O00OO0O000O00OO00 ,OOO00O00O000O00OO )#line:974
                OOOO0000OOOO0O0O0 =100 -(O0O0O0OOOOOO0OO0O [0 ]-1 )*10 #line:975
                if O0O0O0OOOOOO0OO0O [1 ]:#line:976
                    print ("First success after ",O0O0O0OOOOOO0OO0O [0 ]," tries, you have ",OOOO0000OOOO0O0O0 ,"% on this exercise.")#line:977
                else :#line:978
                    print ("You have had ",O0O0O0OOOOOO0OO0O [0 ]," tries.")#line:979
                    print ("If next try is accepted you will achieve ",OOOO0000OOOO0O0O0 -10 ,"% on this exercise.")#line:980
                break #line:982
            except ValueError :#line:984
                print ("I didn't understand that.")#line:985
                continue #line:986
        return #line:988
def b1_notlive ():#line:1000
        print ('This CA test is not currently live.')#line:1001
        return #line:1002
def b2_notlive (OOOOO0O00OO00OO00 ):#line:1012
        print ('This CA test is not currently live.')#line:1013
        return #line:1014
def b3_notlive ():#line:1021
        print ('This CA test is not currently live.')#line:1022
        return #line:1023
def printmd (O00OOO0000O0O00OO ):#line:1033
    display (Markdown (O00OOO0000O0O00OO ))#line:1034
def repeat_to_length (O0OO0000O000O0OOO ,OOOOO0000O00OOO00 ):#line:1036
   return (O0OO0000O000O0OOO *((OOOOO0000O00OOO00 //len (O0OO0000O000O0OOO ))+1 ))[:OOOOO0000O00OOO00 ]#line:1037
def getco (O00OOO00O0O0O000O ):#line:1039
    global ps #line:1040
    O00OOOO0O0OO00OOO =getpass .getuser ()#line:1041
    O0OO0OOOOO00OO000 =int .from_bytes (O00OOOO0O0OO00OOO .encode (),'little')#line:1042
    OO0O0O00000OOO000 =str (O0OO0OOOOO00OO000 )#line:1043
    OOOO000000000O00O =repeat_to_length (OO0O0O00000OOO000 ,O00OOO00O0O0O000O )#line:1044
    ps =[int (O000O000O0OO0O000 )+1 for O000O000O0OO0O000 in OOOO000000000O00O ]#line:1045
def waiter ():#line:1047
    O0OOO00OOOO00OO00 =20 #line:1050
    O0O00000OO000OO0O =".ts1.txt"#line:1052
    if os .path .isfile (O0O00000OO000OO0O ):#line:1053
        O0O000O000OOO0000 =np .loadtxt (O0O00000OO000OO0O )#line:1054
    else :#line:1056
        O0O000O000OOO0000 =0.0 #line:1057
    OO0OO00O00O0OOO0O =time .time ()#line:1060
    O0OO000O0O00O0000 =OO0OO00O00O0OOO0O -O0O000O000OOO0000 #line:1061
    if (O0OO000O0O00O0000 <O0OOO00OOOO00OO00 ):#line:1063
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O0OO000O0O00O0000 ,O0OOO00OOOO00OO00 ))#line:1064
        return False #line:1065
    else :#line:1066
        OO0O000O0OO000O0O =open (O0O00000OO000OO0O ,'w')#line:1067
        OO0O000O0OO000O0O .write (str (OO0OO00O00O0OOO0O ))#line:1068
        OO0O000O0OO000O0O .close ()#line:1069
        return True #line:1070
def trycount (O000OOOOOO0O00OO0 ,O0O0O00O0OO0OOOOO ):#line:1072
    if os .path .isfile (O000OOOOOO0O00OO0 ):#line:1074
        O000O000O0O0OO00O =np .load (O000OOOOOO0O00OO0 )#line:1075
    else :#line:1077
        O000O000O0O0OO00O =np .zeros (1 ,dtype ='int8,bool')#line:1078
        O000O000O0O0OO00O =[0 ,False ]#line:1079
    if not O000O000O0O0OO00O [1 ]:#line:1082
        O000O000O0O0OO00O [0 ]+=1 #line:1083
        O000O000O0O0OO00O [1 ]=O0O0O00O0OO0OOOOO #line:1084
        np .save (O000OOOOOO0O00OO0 ,O000O000O0O0OO00O )#line:1086
    return O000O000O0O0OO00O #line:1088
def valdho (O000OO0OO00O000OO ,OOOOOOOO0OO0OOO0O ):#line:1096
    O0OO0OO0OO0OO0O00 =".dho_counter.npy"#line:1100
    O0000OO00O0000O0O =np .zeros (1 ,dtype ='int8,bool')#line:1102
    if (waiter ()):#line:1104
        while True :#line:1105
            try :#line:1106
                O0O0O0OO0OOO0O00O =float (input ("Please enter your estimate here: "))#line:1107
                OOOO0OOO0OOOO00O0 =2 *np .sqrt (O000OO0OO00O000OO *OOOOOOOO0OO0OOO0O )#line:1108
                O0O00OOO0OOOOO0O0 =np .isclose (O0O0O0OO0OOO0O00O ,OOOO0OOO0OOOO00O0 ,0.2 )#line:1109
                if O0O00OOO0OOOOO0O0 :#line:1110
                    print ("Well done, that is close to the critical damping value ",OOOO0OOO0OOOO00O0 )#line:1111
                else :#line:1112
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1113
                O0000OO00O0000O0O =trycount (O0OO0OO0OO0OO0O00 ,O0O00OOO0OOOOO0O0 )#line:1115
                OO0O00OOO0000OOO0 =100 -(O0000OO00O0000O0O [0 ]-1 )*10 #line:1116
                if O0000OO00O0000O0O [1 ]:#line:1117
                    print ("First success after ",O0000OO00O0000O0O [0 ]," tries, you have ",OO0O00OOO0000OOO0 ,"% on this exercise.")#line:1118
                else :#line:1119
                    print ("You have had ",O0000OO00O0000O0O [0 ]," tries.")#line:1120
                    print ("If next try is accepted you will achieve ",OO0O00OOO0000OOO0 -10 ,"% on this exercise.")#line:1121
                break #line:1123
            except ValueError :#line:1125
                print ("I didn't understand that.")#line:1126
                continue #line:1127
        return #line:1130
def valdrivendho (O0O0OO00OOOO0OO00 ,O0O0O0OO00OO00O0O ):#line:1140
    OOOOOOOO00OOOOOO0 =".drivendho_counter.npy"#line:1144
    O000OO0OOO0O0000O =np .zeros (1 ,dtype ='int8,bool')#line:1146
    if (waiter ()):#line:1148
        while True :#line:1149
            try :#line:1150
                O0O0OOOOOO00OOOO0 =float (input ("Please enter your estimate here: "))#line:1151
                OOOOOOO00OOOO0OO0 =np .sqrt (O0O0OO00OOOO0OO00 **2 -2 *O0O0O0OO00OO00O0O **2 )#line:1152
                O00O00OOO0OO00O00 =np .isclose (O0O0OOOOOO00OOOO0 ,OOOOOOO00OOOO0OO0 ,0.2 )#line:1153
                if O00O00OOO0OO00O00 :#line:1154
                    print ("Well done, that is close to the resonance value ",OOOOOOO00OOOO0OO0 )#line:1155
                else :#line:1156
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1157
                O000OO0OOO0O0000O =trycount (OOOOOOOO00OOOOOO0 ,O00O00OOO0OO00O00 )#line:1159
                OO00O0OOO00O000OO =100 -(O000OO0OOO0O0000O [0 ]-1 )*10 #line:1160
                if O000OO0OOO0O0000O [1 ]:#line:1161
                    print ("First success after ",O000OO0OOO0O0000O [0 ]," tries, you have ",OO00O0OOO00O000OO ,"% on this exercise.")#line:1162
                else :#line:1163
                    print ("You have had ",O000OO0OOO0O0000O [0 ]," tries.")#line:1164
                    print ("If next try is accepted you will achieve ",OO00O0OOO00O000OO -10 ,"% on this exercise.")#line:1165
                break #line:1167
            except ValueError :#line:1169
                print ("I didn't understand that.")#line:1170
                continue #line:1171
        return #line:1174
import ipywidgets as widgets #line:1189
import sys #line:1190
from IPython .display import display #line:1191
from IPython .display import clear_output #line:1192
def create_multipleChoice_widget (O0O0O0O0O00OOO00O ,OOO0O000O00OO00OO ,OOOO0OOOO00000OOO ,O0OOOO00OO00OOO0O ):#line:1194
    O0OOOOOOOO00OOOOO ='.q{:d}_counter.npy'.format (O0O0O0O0O00OOO00O )#line:1195
    O000OO0OOOOO0000O =np .zeros (1 ,dtype ='int8,bool')#line:1196
    O00OOO0O00000O000 =len (OOOO0OOOO00000OOO )#line:1198
    if O0OOOO00OO00OOO0O not in OOOO0OOOO00000OOO :#line:1199
        OOOO0OOOO00000OOO .append (O0OOOO00OO00OOO0O )#line:1200
    O00000OO0OOO00OOO =OOOO0OOOO00000OOO .index (O0OOOO00OO00OOO0O )#line:1202
    O00O0O0OO0OO0OOOO =[(OO000O0OOO00O0000 ,OOOO0OOOOOOOOOO0O )for OOOO0OOOOOOOOOO0O ,OO000O0OOO00O0000 in enumerate (OOOO0OOOO00000OOO )]#line:1204
    OOO0O00000OO00000 =widgets .RadioButtons (options =O00O0O0OO0OO0OOOO ,description ='',disabled =False )#line:1209
    OOOOOOOO0O0O0O0O0 =widgets .Output ()#line:1211
    with OOOOOOOO0O0O0O0O0 :#line:1212
        print (OOO0O000O00OO00OO )#line:1213
    OO0000O00O0OO0OOO =widgets .Output ()#line:1215
    def OOOO00000O000O0OO (O00OO00O0OOO0O00O ):#line:1217
        O0OO0OO00O0O00OO0 =int (OOO0O00000OO00000 .value )#line:1219
        O00OOO00O0O000000 =O0OO0OO00O0O00OO0 ==O00000OO0OOO00OOO #line:1221
        O00OO0OO00OO0OOOO =trycount (O0OOOOOOOO00OOOOO ,O00OOO00O0O000000 )#line:1222
        O0O000OO0OOO0OOOO =max (0 ,100 -(O00OO0OO00OO0OOOO [0 ]-1 )*100 /O00OOO0O00000O000 )#line:1223
        O0OO0OO0OO0O00O0O =OOO0O00000OO00000 .options [O0OO0OO00O0O00OO0 ][0 ]#line:1224
        if O00OOO00O0O000000 :#line:1225
            O0OO0OO0OO0O00O0O +=' correct\n'#line:1226
        else :#line:1227
            O0OO0OO0OO0O00O0O +=' incorrect\n'#line:1228
        if O00OO0OO00OO0OOOO [1 ]:#line:1229
            O0OO0OO0OO0O00O0O +='{:.0f}% on try {:d}'.format (O0O000OO0OOO0OOOO ,O00OO0OO00OO0OOOO [0 ])#line:1230
        else :#line:1231
            O0OO0OO0OO0O00O0O +='{:.0f}% remaining'.format (max (0 ,O0O000OO0OOO0OOOO -100 /O00OOO0O00000O000 ))#line:1232
        with OO0000O00O0OO0OOO :#line:1234
            clear_output ()#line:1235
            print (O0OO0OO0OO0O00O0O )#line:1236
        return #line:1237
    OOOO0OOOOO0OOO000 =widgets .Button (description ="submit")#line:1239
    OOOO0OOOOO0OOO000 .on_click (OOOO00000O000O0OO )#line:1240
    return widgets .VBox ([OOOOOOOO0O0O0O0O0 ,OOO0O00000OO00000 ,OOOO0OOOOO0OOO000 ,OO0000O00O0OO0OOO ])#line:1241
def runq1 ():#line:1248
    OO0OOOO0000OO0O00 =1 #line:1249
    O0O0OO0OOOO0O0OO0 =create_multipleChoice_widget (OO0OOOO0000OO0O00 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1250
    display (O0O0OO0OOOO0O0OO0 )#line:1251
def runQ1 ():#line:1261
    O0O0000O0OOO0000O =1 #line:1262
    O0O0OO000OO0O00O0 =create_multipleChoice_widget (O0O0000O0OOO0000O ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1263
    display (O0O0OO000OO0O00O0 )#line:1264
def runQ2x ():#line:1273
    O0000OOO0O0O00O00 =2 #line:1274
    O00000O000O0O00O0 =create_multipleChoice_widget (O0000OOO0O0O00O00 ,'',['centred','backwards','forwards'],'centred')#line:1275
    display (O00000O000O0O00O0 )#line:1276
def runQ3x ():#line:1284
    O00O0O00OO0000O0O =3 #line:1285
    O00OOO000O0O00O00 =create_multipleChoice_widget (O00O0O00OO0000O0O ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1286
    display (O00OOO000O0O00O00 )#line:1287
def runQ4x ():#line:1296
    OOOOO0OOOO000O00O =4 #line:1297
    OO000OO0O0O0OO0O0 =create_multipleChoice_widget (OOOOO0OOOO000O00O ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1298
    display (OO000OO0O0O0OO0O0 )#line:1299
def runQ5x ():#line:1309
    OO00OOOOO000O0O0O =5 #line:1310
    O00O0000O00OOOO0O =create_multipleChoice_widget (OO00OOOOO000O0O0O ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1311
    display (O00O0000O00OOOO0O )#line:1312
def runQ6x ():#line:1321
    O0O000OOOO0O0O0OO =6 #line:1322
    OOOOOO00O0O00O00O =create_multipleChoice_widget (O0O000OOOO0O0O0OO ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1323
    display (OOOOOO00O0O00O00O )#line:1324
def runQ7x ():#line:1333
    OOOOO0000OO00O0OO =7 #line:1334
    O0O0O000000OOOO0O =create_multipleChoice_widget (OOOOO0000OO00O0OO ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1335
    display (O0O0O000000OOOO0O )#line:1336
