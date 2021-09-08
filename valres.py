import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (OO0000OO0OO0OOOO0 ,OOOOOO0OOO0O00000 ):#line:10
        print ("\nPasswords may not be changed using this notebook at present.")#line:14
ps =[]#line:18
wd =''#line:19
def a1 ():#line:36
    global ps #line:38
    OOOOOO0O0OO0OO0O0 =".a1_counter.npy"#line:41
    O00O0O000O0O0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:42
    OO00O00O00O0OO0O0 =0 #line:44
    O0O000OO00O0OO00O =ps [0 ]#line:45
    OOOO00OO0000OOOOO =ps [1 ]#line:46
    if (waiter ()):#line:48
        while True :#line:49
            try :#line:50
                printmd ('**CA** (2%)')#line:51
                print (O0O000OO00O0OO00O ,"+",OOOO00OO0000OOOOO )#line:52
                O0O0O0000OOO0O0OO =float (input ("Please enter your answer here: "))#line:53
                OO0O000OOO00000OO =O0O000OO00O0OO00O +OOOO00OO0000OOOOO #line:54
                O0O0O000O000O0OOO =np .isclose (O0O0O0000OOO0O0OO ,OO0O000OOO00000OO ,OO00O00O00O0OO0O0 )#line:55
                if O0O0O000O000O0OOO :#line:56
                    print ("Well done, right answer is ",OO0O000OOO00000OO )#line:57
                else :#line:58
                    print ("Not right yet. Take another look then run this cell again.")#line:59
                O00O0O000O0O0OO0O =trycount (OOOOOO0O0OO0OO0O0 ,O0O0O000O000O0OOO )#line:61
                OOO0OO0O00O0O0000 =100 -(O00O0O000O0O0OO0O [0 ]-1 )*10 #line:62
                if O00O0O000O0O0OO0O [1 ]:#line:63
                    print ("First success after ",O00O0O000O0O0OO0O [0 ]," tries, you have ",OOO0OO0O00O0O0000 ,"% on this exercise.")#line:64
                else :#line:65
                    print ("You have had ",O00O0O000O0O0OO0O [0 ]," tries.")#line:66
                    print ("If next try is accepted you will achieve ",OOO0OO0O00O0O0000 -10 ,"% on this exercise.")#line:67
                break #line:69
            except ValueError :#line:71
                print ("I didn't understand that.")#line:72
                continue #line:73
        return #line:75
def a2_notlive (O0O0OOOO000OOOOOO ):#line:84
    global ps #line:86
    OO0OOOO00O0OOO0OO =".a2_counter.npy"#line:89
    OO0000O0OOOO0OOOO =np .zeros (1 ,dtype ='int8,bool')#line:90
    O00OOO0O0000OO0O0 =6 #line:93
    O0OO00O0O000OO000 =7 #line:94
    OO0OOOOO000000O00 =0 #line:96
    O000OOOOOO00OO000 =(ps [O00OOO0O0000OO0O0 ])%6 +1 #line:98
    O00OO0000O0000OO0 =(ps [O0OO00O0O000OO000 ])%6 +1 #line:99
    while O000OOOOOO00OO000 +O00OO0000O0000OO0 ==7 or O000OOOOOO00OO000 ==O00OO0000O0000OO0 :#line:100
        O00OO0000O0000OO0 +=1 #line:101
        O00OO0000O0000OO0 =O00OO0000O0000OO0 %6 +1 #line:102
    if (O0O0OOOO000OOOOOO ):#line:104
        printmd ('**CA** (2%)')#line:105
        print ("Run your program (when you are happy it is working correctly) for a=",O000OOOOOO00OO000 ," and b=",O00OO0000O0000OO0 )#line:106
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:107
        return #line:108
    if (waiter ()):#line:110
        while True :#line:111
            try :#line:112
                print ("Enter your program's result for a=",O000OOOOOO00OO000 ," and b=",O00OO0000O0000OO0 )#line:113
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:114
                OOOO0O00O0OO000O0 =float (input ("Please enter your answer here: "))#line:115
                OOOOOOOOOOOO00OOO =(3 *(O000OOOOOO00OO000 **3 *O00OO0000O0000OO0 -O000OOOOOO00OO000 *O00OO0000O0000OO0 **3 ))%7 #line:116
                OO0OOO0O000O00OO0 =np .isclose (OOOO0O00O0OO000O0 ,OOOOOOOOOOOO00OOO ,OO0OOOOO000000O00 )#line:117
                if OO0OOO0O000O00OO0 :#line:118
                    print ("Well done, right answer is ",OOOOOOOOOOOO00OOO )#line:119
                else :#line:120
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:121
                OO0000O0OOOO0OOOO =trycount (OO0OOOO00O0OOO0OO ,OO0OOO0O000O00OO0 )#line:123
                O00O000O0O000000O =100 -(OO0000O0OOOO0OOOO [0 ]-1 )*10 #line:124
                if OO0000O0OOOO0OOOO [1 ]:#line:125
                    print ("First success after ",OO0000O0OOOO0OOOO [0 ]," tries, you have ",O00O000O0O000000O ,"% on this exercise.")#line:126
                else :#line:127
                    print ("You have had ",OO0000O0OOOO0OOOO [0 ]," tries.")#line:128
                    print ("If next try is accepted you will achieve ",O00O000O0O000000O -10 ,"% on this exercise.")#line:129
                break #line:131
            except ValueError :#line:133
                print ("I didn't understand that.")#line:134
                continue #line:135
        return #line:137
def a3_notlive (O0OOO0OOOOOOO0OO0 ):#line:146
    global ps #line:148
    OOO00O000OO00O000 =".a3_counter.npy"#line:151
    O0OO00OOOO0000O00 =np .zeros (1 ,dtype ='int8,bool')#line:152
    O0OO0O00OO0000O00 =23 #line:155
    O0OO00O0O00OO0000 =24 #line:156
    O0O00OOO0OO00O0O0 =(ps [O0OO0O00OO0000O00 ])%6 +1 #line:157
    O00000O00OO0O000O =(ps [O0OO00O0O00OO0000 ])%6 +1 #line:158
    O0OOOO0OO000O0OOO =0 #line:160
    O0O00OOO0OO00O0O0 =10 *O0O00OOO0OO00O0O0 +O00000O00OO0O000O ;#line:162
    if (O0OOO0OOOOOOO0OO0 ):#line:164
        printmd ('**CA** (6%)')#line:165
        print ("Run your program for ",O0O00OOO0OO00O0O0 ,"people")#line:166
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:167
        return #line:168
    if (waiter ()):#line:170
        while True :#line:171
            try :#line:172
                print ("Enter your program's result for",O0O00OOO0OO00O0O0 ,"people")#line:173
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:174
                O00OO0O0OOO0000O0 =float (input ("Please enter your answer here: "))#line:175
                OOO00000000OO0O0O =O0O00OOO0OO00O0O0 +2 *O0O00OOO0OO00O0O0 +2 *O0O00OOO0OO00O0O0 +10 *O0O00OOO0OO00O0O0 #line:176
                OO0O0O0OO00O0O00O =np .isclose (O00OO0O0OOO0000O0 ,OOO00000000OO0O0O ,O0OOOO0OO000O0OOO )#line:177
                if OO0O0O0OO00O0O00O :#line:178
                    print ("Well done, right answer is ",OOO00000000OO0O0O )#line:179
                else :#line:180
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:181
                O0OO00OOOO0000O00 =trycount (OOO00O000OO00O000 ,OO0O0O0OO00O0O00O )#line:183
                O00000OO0OOOO000O =100 -(O0OO00OOOO0000O00 [0 ]-1 )*10 #line:184
                if O0OO00OOOO0000O00 [1 ]:#line:185
                    print ("First success after ",O0OO00OOOO0000O00 [0 ]," tries, you have ",O00000OO0OOOO000O ,"% on this exercise.")#line:186
                else :#line:187
                    print ("You have had ",O0OO00OOOO0000O00 [0 ]," tries.")#line:188
                    print ("If next try is accepted you will achieve ",O00000OO0OOOO000O -10 ,"% on this exercise.")#line:189
                break #line:191
            except ValueError :#line:193
                print ("I didn't understand that.")#line:194
                continue #line:195
        return #line:197
def a4_notlive (OOO0O0OOOO0O000OO ):#line:208
        import random #line:210
        import requests #line:211
        global ps #line:213
        global wd #line:214
        O0OOO00O0O0OO0OO0 =".a4_counter.npy"#line:217
        O000O00000OO00O0O =np .zeros (1 ,dtype ='int8,bool')#line:218
        OO0O0000000000000 =60 #line:221
        O0OO000O000O00O00 =61 #line:222
        O0OOOO00O0O0000OO =62 #line:223
        OO00O0OO0OO00O0OO =63 #line:224
        O00O0O00O00O0OO0O =64 #line:225
        O0O000O0O000O000O =0 #line:228
        if (OOO0O0OOOO0O000OO ):#line:230
                OO00O00OO00000OO0 ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:232
                OO00000OO0OO00000 =requests .get (OO00O00OO00000OO0 )#line:234
                OOOOOOOOOO0OOOOOO =OO00000OO0OO00000 .content .splitlines ()#line:235
                random .seed (10 *ps [62 ]+ps [63 ])#line:236
                O0OO000O0O00O00O0 =4 +(10 *ps [64 ]+ps [65 ])%4 #line:237
                O0O0O00O000OO00O0 =True #line:238
                while O0O0O00O000OO00O0 :#line:239
                        O00OO0O0000O0000O =OOOOOOOOOO0OOOOOO [random .randint (0 ,len (OOOOOOOOOO0OOOOOO )-1 )].decode ("utf-8")#line:240
                        if len (O00OO0O0000O0000O )>7 and len (O00OO0O0000O0000O )<14 and O00OO0O0000O0000O [0 ].islower ():#line:242
                                O0O0O00O000OO00O0 =False #line:243
                                for OO0OO00OOO00OO00O in O00OO0O0000O0000O :#line:244
                                        if chr (ord (OO0OO00OOO00OO00O )+O0OO000O0O00O00O0 )>'z':#line:245
                                                O0O0O00O000OO00O0 =True #line:246
                OO0OO0OO0O0O0000O =len (O00OO0O0000O0000O )#line:248
                O0OOOO00OOO0O0O00 =''#line:249
                for OO0OOO000OOO0O000 in range (0 ,OO0OO0OO0O0O0000O ):#line:250
                        O0OOOO00OOO0O0O00 +=chr (ord (O00OO0O0000O0000O [OO0OOO000OOO0O000 ])+O0OO000O0O00O00O0 )#line:252
                print ('Your encoded word is',O0OOOO00OOO0O0O00 )#line:254
                print ('Write your program in the cell below this one.\n')#line:255
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:257
                wd =O00OO0O0000O0000O #line:258
                return #line:259
        if (waiter ()):#line:261
                while True :#line:262
                        try :#line:263
                                printmd ('**CA** (6%)')#line:264
                                OO0O0OOOO0O0O0OO0 =str (input ("Enter your DECODED word here: "))#line:265
                                O0O0O00OO0OO0O00O =wd #line:266
                                OOOOOO00000000000 =OO0O0OOOO0O0O0OO0 ==O0O0O00OO0OO0O00O #line:267
                                if OOOOOO00000000000 :#line:268
                                        print ("Well done, right answer is ",O0O0O00OO0OO0O00O )#line:269
                                else :#line:270
                                        print ("Not right yet. Take another look then run this cell again.")#line:271
                                O000O00000OO00O0O =trycount (O0OOO00O0O0OO0OO0 ,OOOOOO00000000000 )#line:273
                                O00O00OOO00OO000O =100 -(O000O00000OO00O0O [0 ]-1 )*10 #line:274
                                if O000O00000OO00O0O [1 ]:#line:275
                                        print ("First success after ",O000O00000OO00O0O [0 ]," tries, you have ",O00O00OOO00OO000O ,"% on this exercise.")#line:276
                                else :#line:277
                                        print ("You have had ",O000O00000OO00O0O [0 ]," tries.")#line:278
                                        print ("If next try is accepted you will achieve ",O00O00OOO00OO000O -10 ,"% on this exercise.")#line:279
                                break #line:280
                        except ValueError :#line:282
                                print ("I didn't understand that.")#line:283
                                continue #line:284
                return #line:286
def a5_notlive (O0OO00O00000O0000 ):#line:296
        import random #line:298
        import requests #line:299
        global ps #line:301
        global P0 #line:302
        O00OO0O0O00OO0O0O =".a5_counter.npy"#line:306
        OO0OO0O0O0000O0OO =np .zeros (1 ,dtype ='int8,bool')#line:307
        OO0OO00000000000O =70 #line:310
        OOO00OO0O0OO0O0O0 =71 #line:311
        O0OOOO00O0000O000 =72 #line:312
        O0O0OO000O0O0O0O0 =73 #line:313
        O000OO00O0OOOOOOO =74 #line:314
        O0OOO0O0OOO00O00O =0 #line:317
        if (O0OO00O00000O0000 ):#line:319
                P0 =[]#line:320
                O0000OO00O00O0OOO =7 +(10 *ps [OO0OO00000000000O ]+ps [OOO00OO0O0OO0O0O0 ])%4 #line:321
                for O00O0O0O00000O00O in range (O0000OO00O00O0OOO ):#line:322
                        P0 .append (max (0 ,ps [O0OOOO00O0000O000 +O00O0O0O00000O00O ]-1 ))#line:323
                print ('Run your program for the list below:\n',P0 )#line:324
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:326
        elif (waiter ()):#line:328
                while True :#line:329
                        try :#line:330
                                printmd ('**CA** (6%)')#line:333
                                O00000O000000OO0O =eval (input ("Enter your list here: "))#line:334
                                O0000OO0000OOOOO0 =3 #line:339
                                OO0O0O000OO000OOO =P0 .copy ()#line:340
                                OO0O0O000OO000OOO .append (0 )#line:341
                                print (OO0O0O000OO000OOO )#line:342
                                O0000OO00O00O0OOO =len (P0 )#line:343
                                for OOOO000O0OOOO000O in range (O0000OO0000OOOOO0 ):#line:344
                                        for O00O0O0O00000O00O in range (O0000OO00O00O0OOO ):#line:345
                                                OO0O0O000OO000OOO [O00O0O0O00000O00O ]=OO0O0O000OO000OOO [O00O0O0O00000O00O +1 ]*(O00O0O0O00000O00O +1 )#line:347
                                OO0O0O000OO000OOO .pop ()#line:348
                                O0O000O00O00OOO00 =OO0O0O000OO000OOO #line:351
                                if not type (O00000O000000OO0O )==type (O0O000O00O00OOO00 ):#line:353
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:354
                                elif not len (O00000O000000OO0O )==len (O0O000O00O00OOO00 ):#line:355
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:356
                                else :#line:357
                                        O00OO00OO0OO0OOO0 =O00000O000000OO0O ==O0O000O00O00OOO00 #line:358
                                        if O00OO00OO0OO0OOO0 :#line:359
                                                print ("Well done, right answer is ",O0O000O00O00OOO00 )#line:360
                                        else :#line:361
                                                print ("Not right yet. Take another look then run this cell again.")#line:362
                                        OO0OO0O0O0000O0OO =trycount (O00OO0O0O00OO0O0O ,O00OO00OO0OO0OOO0 )#line:364
                                        OO0O0OOOO0OOOO000 =100 -(OO0OO0O0O0000O0OO [0 ]-1 )*10 #line:365
                                        if OO0OO0O0O0000O0OO [1 ]:#line:366
                                                print ("First success after ",OO0OO0O0O0000O0OO [0 ]," tries, you have ",OO0O0OOOO0OOOO000 ,"% on this exercise.")#line:367
                                        else :#line:368
                                                print ("You have had ",OO0OO0O0O0000O0OO [0 ]," tries.")#line:369
                                                print ("If next try is accepted you will achieve ",OO0O0OOOO0OOOO000 -10 ,"% on this exercise.")#line:370
                                        break #line:371
                                OO0O0O000OO000OOO =None #line:374
                                O0O000O00O00OOO00 =None #line:375
                        except ValueError :#line:376
                                print ("I didn't understand that.")#line:377
                                continue #line:378
        return #line:380
def a6_notlive (O0OO00OO00OOOO000 ):#line:389
        import random #line:391
        import requests #line:392
        global ps #line:394
        global P0 #line:395
        OOO00OOOO0OO0O0OO =".a6_counter.npy"#line:399
        O00O0000O000O0O00 =np .zeros (1 ,dtype ='int8,bool')#line:400
        OOO00O0OO0O0OOOOO =11 #line:403
        O00000OO00O00OO0O =16 #line:404
        OOOO000OO0OO0OO0O =7 #line:405
        O0O0000OO0OO00000 =33 #line:406
        OO0O0OOO00O00O00O =21 #line:407
        OOOOOOOOOOO0OO0O0 =0 #line:410
        if (O0OO00OO00OOOO000 ):#line:412
                O00OOO00O000OOO0O =ps [OOO00O0OO0O0OOOOO ]+ps [O00000OO00O00OO0O ]+ps [OOOO000OO0OO0OO0O ]+ps [O0O0000OO0OO00000 ]+ps [OO0O0OOO00O00O00O ]#line:413
                random .seed (O00OOO00O000OOO0O )#line:414
                P0 =random .randint (1000 ,2000 )#line:415
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:416
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:418
        elif (waiter ()):#line:420
                while True :#line:421
                        try :#line:422
                                printmd ('**CA** (6%)')#line:425
                                OOO0O00OOOOO0O0O0 =eval (input ("Enter your stopping number here: "))#line:426
                                O0O0OOOOOO0O0OO0O =P0 #line:430
                                O0OOOO0OO00O0O00O =[O0O0OOOOOO0O0OO0O ]#line:431
                                while not O0O0OOOOOO0O0OO0O ==1 :#line:432
                                        if O0O0OOOOOO0O0OO0O %2 :#line:433
                                                O0O0OOOOOO0O0OO0O =3 *O0O0OOOOOO0O0OO0O +1 #line:434
                                        else :#line:435
                                                O0O0OOOOOO0O0OO0O =O0O0OOOOOO0O0OO0O //2 #line:436
                                        O0OOOO0OO00O0O00O .append (O0O0OOOOOO0O0OO0O )#line:437
                                O00O00O0O0000O000 =len (O0OOOO0OO00O0O00O )#line:438
                                O0O00000O0O0O0O0O =O00O00O0O0000O000 #line:442
                                if not type (OOO0O00OOOOO0O0O0 )==type (O0O00000O0O0O0O0O ):#line:444
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:445
                                else :#line:448
                                        OO0OOOO0OOO0O0O00 =OOO0O00OOOOO0O0O0 ==O0O00000O0O0O0O0O #line:449
                                        if OO0OOOO0OOO0O0O00 :#line:450
                                                print ("Well done, right answer is ",O0O00000O0O0O0O0O )#line:451
                                        else :#line:452
                                                print ("Not right yet. Take another look then run this cell again.")#line:453
                                        O00O0000O000O0O00 =trycount (OOO00OOOO0OO0O0OO ,OO0OOOO0OOO0O0O00 )#line:455
                                        O0OO0O00OO00000OO =100 -(O00O0000O000O0O00 [0 ]-1 )*10 #line:456
                                        if O00O0000O000O0O00 [1 ]:#line:457
                                                print ("First success after ",O00O0000O000O0O00 [0 ]," tries, you have ",O0OO0O00OO00000OO ,"% on this exercise.")#line:458
                                        else :#line:459
                                                print ("You have had ",O00O0000O000O0O00 [0 ]," tries.")#line:460
                                                print ("If next try is accepted you will achieve ",O0OO0O00OO00000OO -10 ,"% on this exercise.")#line:461
                                        break #line:462
                                O00O00O0O0000O000 =None #line:465
                                O0O00000O0O0O0O0O =None #line:466
                        except ValueError :#line:467
                                print ("I didn't understand that.")#line:468
                                continue #line:469
        return #line:471
def a7_notlive (OO0OOO0OOO00O00OO ):#line:481
        O0O0000O00OO000OO =".a7_counter.npy"#line:485
        O0O00O000OOO0OOO0 =np .zeros (1 ,dtype ='int8,bool')#line:486
        def O0OOO0O0O0OO0O000 ():#line:488
                pass #line:489
        O0O0OO0OO0O0OOO0O =[(30 ,10 )]#line:492
        O00OOOOO0O00O00O0 =1.0e-4 #line:495
        if (waiter ()):#line:498
                printmd ('**CA** (6%)')#line:500
                if not type (OO0OOO0OOO00O00OO )==type (O0OOO0O0O0OO0O000 ):#line:502
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:503
                else :#line:506
                        def O0OOOOOOOO000OOO0 (O0O00O0O0O0OO0000 ,OO00OO0OO0O00OOOO ):#line:509
                                import math #line:510
                                OO00O0O0O00O00OO0 =9.81 #line:511
                                OO0OOOO0000O00O00 =math .pi *OO00OO0OO0O00OOOO /180. #line:512
                                O0OOO00O0O0OOO0OO =O0O00O0O0O0OO0000 **2 *math .sin (2 *OO0OOOO0000O00O00 )/OO00O0O0O00O00OO0 #line:513
                                O0OOO000O0O00OOO0 =O0O00O0O0O0OO0000 **2 *(math .sin (OO0OOOO0000O00O00 ))**2 /(2. *OO00O0O0O00O00OO0 )#line:514
                                return O0OOO00O0O0OOO0OO ,O0OOO000O0O00OOO0 #line:515
                        import random as r #line:518
                        O0O0OO0OO0O0OOO0O =[]#line:519
                        OOO00OO00OO00O0OO =False #line:520
                        OOO0000O000OO0000 =[]#line:521
                        OO0OOOO00O0000O0O =10 #line:522
                        OOO0O0OOO0000O00O =100 #line:523
                        OOO0O00O0000O0OOO =5 #line:524
                        O0O000OO00OO0000O =85 #line:525
                        for O00O0O0O0OO000OO0 in range (5 ):#line:526
                                O0O0OO0OO0O0OOO0O .append ((r .uniform (OO0OOOO00O0000O0O ,OOO0O0OOO0000O00O ),r .uniform (OOO0O00O0000O0OOO ,O0O000OO00OO0000O )))#line:527
                        for (O0000OO00O0O0O00O ,O00O0O000O00O0OOO )in O0O0OO0OO0O0OOO0O :#line:528
                                print ('Testing:',O0000OO00O0O0O00O ,O00O0O000O00O0OOO )#line:529
                                OOO00000O00OOO000 =OO0OOO0OOO00O00OO (O0000OO00O0O0O00O ,O00O0O000O00O0OOO )#line:530
                                print ('Output:',*OOO00000O00OOO000 )#line:531
                                O0O0OOOO0O0O000OO =O0OOOOOOOO000OOO0 (O0000OO00O0O0O00O ,O00O0O000O00O0OOO )#line:532
                                print ('Actual:',*O0O0OOOO0O0O000OO )#line:533
                                print ()#line:534
                                if (not type (OOO00000O00OOO000 )==type (O0O0OOOO0O0O000OO ))or (not len (OOO00000O00OOO000 )==len (O0O0OOOO0O0O000OO )):#line:535
                                        if OOO00OO00OO00O0OO ==False :#line:536
                                           OOO00OO00OO00O0OO =True #line:537
                                else :#line:538
                                        OOO0000O000OO0000 .append (all (np .isclose (OOO00000O00OOO000 ,O0O0OOOO0O0O000OO ,O00OOOOO0O00O00O0 )))#line:539
                        if OOO00OO00OO00O0OO :#line:541
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:542
                        else :#line:544
                                OO0OOO00OOO0000O0 =all (OOO0000O000OO0000 )#line:545
                                if OO0OOO00OOO0000O0 :#line:546
                                        print ("Well done, all correct.")#line:547
                                else :#line:548
                                        print ("Not right yet. Take another look then run this cell again.")#line:549
                                O0O00O000OOO0OOO0 =trycount (O0O0000O00OO000OO ,OO0OOO00OOO0000O0 )#line:551
                                OO0OO0O0OOOOOOO0O =100 -(O0O00O000OOO0OOO0 [0 ]-1 )*10 #line:552
                                if O0O00O000OOO0OOO0 [1 ]:#line:553
                                        print ("First success after ",O0O00O000OOO0OOO0 [0 ]," tries, you have ",OO0OO0O0OOOOOOO0O ,"% on this exercise.")#line:554
                                else :#line:555
                                        print ("You have had ",O0O00O000OOO0OOO0 [0 ]," tries.")#line:556
                                        print ("If next try is accepted you will achieve ",OO0OO0O0OOOOOOO0O -10 ,"% on this exercise.")#line:557
                        O0O0OOOO0O0O000OO =None #line:560
                        O0OOOOOOOO000OOO0 =None #line:561
        return #line:563
def a8_notlive (OO0OOOO0O0O0O0OOO ):#line:573
        O0OO000O000OO0O00 =".a8_counter.npy"#line:577
        O0OO000O00O0O00O0 =np .zeros (1 ,dtype ='int8,bool')#line:578
        def O000000OO00O0O000 ():#line:580
                pass #line:581
        O0O00OOO00O00OOOO =1.0e-4 #line:585
        if (waiter ()):#line:588
                printmd ('**CA** (6%)')#line:590
                if not type (OO0OOOO0O0O0O0OOO )==type (O000000OO00O0O000 ):#line:594
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:595
                else :#line:599
                        import inspect #line:602
                        OO0000O00OO0000O0 =inspect .getsourcelines (OO0OOOO0O0O0O0OOO )#line:603
                        O000O00O0O0OO0000 =True #line:604
                        OO0OO0O00O0OOO00O =[]#line:605
                        for OO00O00OOOOOO00OO ,OOO0O000O0O000O0O in enumerate (OO0000O00OO0000O0 [0 ]):#line:606
                                if 'for'in OOO0O000O0O000O0O or 'while'in OOO0O000O0O000O0O :#line:607
                                        O000O00O0O0OO0000 =False #line:609
                                        OO0OO0O00O0OOO00O .append (OO00O00OOOOOO00OO )#line:610
                        if not O000O00O0O0OO0000 :#line:611
                                print ('Function needs to be written without loops (using NumPy), check lines',*OO0OO0O00O0OOO00O )#line:612
                                print ('No marks lost for this attempt.')#line:613
                                return #line:614
                        def OO00O0O00OO0OOO00 (OOO0OOOO0O0O000O0 ):#line:617
                                OO0O0O0000O0OOOO0 =np .vstack ((OOO0OOOO0O0O000O0 ,OOO0OOOO0O0O000O0 [0 ]))#line:618
                                O0000000000O0OO0O =sum (OO0O0O0000O0OOOO0 [:-1 ,0 ]*OO0O0O0000O0OOOO0 [1 :,1 ])#line:619
                                OOO00000O00O0OO00 =sum (OO0O0O0000O0OOOO0 [:-1 ,1 ]*OO0O0O0000O0OOOO0 [1 :,0 ])#line:620
                                return abs (O0000000000O0OO0O -OOO00000O00O0OO00 )/2 #line:621
                        import random as r #line:624
                        O00O0000OOOOOO0O0 =r .randint (6 ,11 )#line:625
                        OOO0O00OO00OOOO00 =np .ones ((O00O0000OOOOOO0O0 ,2 ))#line:626
                        OO0O00O0OO00O0000 =False #line:627
                        OO0O000O00OOOOO00 =[]#line:628
                        O0O0OO00OOO0000O0 =1. #line:629
                        O0OO0OOO0OOOO0O00 =20. #line:630
                        O00O0O0OO000O0O0O =O0O0OO00OOO0000O0 #line:631
                        O00OO0O00OO00O0OO =O0OO0OOO0OOOO0O00 #line:632
                        for O0O000O0O00O00000 in range (O00O0000OOOOOO0O0 ):#line:633
                                OOO0O00OO00OOOO00 [O0O000O0O00O00000 ]=[r .uniform (O0O0OO00OOO0000O0 ,O0OO0OOO0OOOO0O00 ),r .uniform (O00O0O0OO000O0O0O ,O00OO0O00OO00O0OO )]#line:634
                        print ('Testing:',OOO0O00OO00OOOO00 )#line:635
                        OOOOOOOO00O0O000O =OO0OOOO0O0O0O0OOO (OOO0O00OO00OOOO00 )#line:636
                        print ('Output:',OOOOOOOO00O0O000O )#line:637
                        OOO0O000O00OO0000 =OO00O0O00OO0OOO00 (OOO0O00OO00OOOO00 )#line:638
                        print ('Actual:',OOO0O000O00OO0000 )#line:639
                        print ()#line:640
                        if not type (OOOOOOOO00O0O000O )==type (OOO0O000O00OO0000 ):#line:641
                                if OO0O00O0OO00O0000 ==False :#line:642
                                        OO0O00O0OO00O0000 =True #line:643
                        else :#line:644
                                OO0O000O00OOOOO00 .append (np .isclose (OOOOOOOO00O0O000O ,OOO0O000O00OO0000 ,O0O00OOO00O00OOOO ))#line:645
                        if OO0O00O0OO00O0000 :#line:647
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:648
                        else :#line:650
                                OO00OO000000O0OOO =all (OO0O000O00OOOOO00 )#line:651
                                if OO00OO000000O0OOO :#line:652
                                        print ("Well done, all correct.")#line:653
                                else :#line:654
                                        print ("Not right yet. Take another look then run this cell again.")#line:655
                                O0OO000O00O0O00O0 =trycount (O0OO000O000OO0O00 ,OO00OO000000O0OOO )#line:657
                                OOOO00000OOO00OOO =100 -(O0OO000O00O0O00O0 [0 ]-1 )*10 #line:658
                                if O0OO000O00O0O00O0 [1 ]:#line:659
                                        print ("First success after ",O0OO000O00O0O00O0 [0 ]," tries, you have ",OOOO00000OOO00OOO ,"% on this exercise.")#line:660
                                else :#line:661
                                        print ("You have had ",O0OO000O00O0O00O0 [0 ]," tries.")#line:662
                                        print ("If next try is accepted you will achieve ",OOOO00000OOO00OOO -10 ,"% on this exercise.")#line:663
                        OOO0O000O00OO0000 =None #line:666
                        OO00O0O00OO0OOO00 =None #line:667
        return #line:669
def a1_notlive ():#line:685
        print ('This CA test is not currently live.')#line:686
        return #line:687
def a2 (OO0O00O00OOOOOOO0 ):#line:695
        print ('This CA test is not currently live.')#line:696
        return #line:697
def a3 (O00OO0000000O0000 ):#line:705
        print ('This CA test is not currently live.')#line:706
        return #line:707
def a4 (O000OO0OO00O000OO ):#line:715
        print ('This CA test is not currently live.')#line:716
        return #line:717
def a5 (OO0OO0000000OO0OO ):#line:725
        print ('This CA test is not currently live.')#line:726
        return #line:727
def a6 (OO0O0OOO000000OO0 ):#line:735
        print ('This CA test is not currently live.')#line:736
        return #line:737
def a7 ():#line:745
        print ('This CA test is not currently live.')#line:746
        return #line:747
def a8 (O0OO0O0O0O0OOOOO0 ):#line:755
        print ('This CA test is not currently live.')#line:756
        return #line:757
def b1 ():#line:775
    global ps #line:777
    OO0OO0O00O0O0OOOO =".b1_counter.npy"#line:780
    O000OOOO0O0000OOO =np .zeros (1 ,dtype ='int8,bool')#line:781
    O00O00O0O0OOO0O00 =0.05 #line:783
    if (waiter ()):#line:785
        while True :#line:786
            try :#line:787
                printmd ('**CA**')#line:788
                O000O0O0000OOO00O =eval (input ("Please enter your answer here in the format D,k: "))#line:789
                OOOO00OOO0O00OOOO =(0.025 ,2.0 )#line:790
                O0OO0OO000O00O0OO =all (np .isclose (O000O0O0000OOO00O ,OOOO00OOO0O00OOOO ,rtol =O00O00O0O0OOO0O00 ))#line:791
                if O0OO0OO000O00O0OO :#line:792
                    print ("Well done, reasonable estimate is ",OOOO00OOO0O00OOOO )#line:793
                else :#line:794
                    print ("Not right yet. Take another look then run this cell again.")#line:795
                O000OOOO0O0000OOO =trycount (OO0OO0O00O0O0OOOO ,O0OO0OO000O00O0OO )#line:797
                OOOO0000O0OO0O00O =100 -(O000OOOO0O0000OOO [0 ]-1 )*10 #line:798
                if O000OOOO0O0000OOO [1 ]:#line:799
                    print ("First success after ",O000OOOO0O0000OOO [0 ]," tries, you have ",OOOO0000O0OO0O00O ,"% on this exercise.")#line:800
                else :#line:801
                    print ("You have had ",O000OOOO0O0000OOO [0 ]," tries.")#line:802
                    print ("If next try is accepted you will achieve ",OOOO0000O0OO0O00O -10 ,"% on this exercise.")#line:803
                break #line:805
            except ValueError :#line:807
                print ("I didn't understand that.")#line:808
                continue #line:809
        return #line:811
def b2 (O0O0O0O00000000OO ):#line:821
        OOO0O0OO000OOOOOO =".b2_counter.npy"#line:825
        OOOO00OOO0OO00000 =np .zeros (1 ,dtype ='int8,bool')#line:826
        def OOOO0OO00O0OOO000 ():#line:828
                pass #line:829
        O0O0OOO0OO0OO0OOO =1.0e-2 #line:832
        OOOO000O00O0O00OO =0.0 #line:833
        if (waiter ()):#line:835
                printmd ('**CA**')#line:837
                if not type (O0O0O0O00000000OO )==type (OOOO0OO00O0OOO000 ):#line:839
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:840
                else :#line:843
                        def OO0O000O0O0OOOO00 (O00O0O00O00O0000O ):#line:847
                                O0OOOOO0O00OOO00O =[]#line:848
                                O000O00OOO0OOO0OO =20.0 #line:849
                                OOO000O0O0OO00OO0 =58.1e-3 #line:850
                                O0000O00O0O00O0OO =9.81 #line:851
                                O0O000O0O0OO00OOO =0.0 #line:852
                                O000OOOO0O0OOO00O =0.0 #line:853
                                OOO000OOO0000OO00 =0.0 #line:854
                                OOO0OOO00OO0000OO =10 #line:855
                                O00OOOOO0O0OOO000 =3.35e-2 #line:856
                                O00OOOO0O0OO0OO0O =0.51 #line:857
                                O0OOO00OOOO0OOOOO =1.25 #line:858
                                OO0000O0OO0O00O0O =math .pi *O00OOOOO0O0OOO000 **2 #line:859
                                O0O0OO00OO0O00O0O =0.5 *O00OOOO0O0OO0OO0O *OO0000O0OO0O00O0O *O0OOO00OOOO0OOOOO #line:860
                                OOOO0OOO00O00OO0O =100000 #line:862
                                OO00000OOO0000000 =np .zeros (OOOO0OOO00O00OO0O ,float )#line:863
                                OOOO00O0OO00OOOOO =np .zeros (OOOO0OOO00O00OO0O ,float )#line:864
                                O000OO00OO000O0OO =np .zeros (OOOO0OOO00O00OO0O ,float )#line:865
                                O0O0O00OO000OO0O0 =np .zeros (OOOO0OOO00O00OO0O ,float )#line:866
                                OOO0OO0000000O000 =np .zeros (OOOO0OOO00O00OO0O ,float )#line:867
                                O00OOO0O00O0O0OO0 =np .zeros (OOOO0OOO00O00OO0O ,float )#line:868
                                O00O0O0000OO0OOO0 =np .zeros (OOOO0OOO00O00OO0O ,float )#line:869
                                OO00000OOO0000000 ,OOOO0O0OOOO00O00O =np .linspace (OOO000OOO0000OO00 ,OOO0OOO00OO0000OO ,OOOO0OOO00O00OO0O ,retstep =True )#line:870
                                for OO00O0O0O00OO0O00 in O00O0O00O00O0000O :#line:872
                                        O0000OOOOOO0000OO =O000O00OOO0OOO0OO *math .cos (OO00O0O0O00OO0O00 )#line:873
                                        OOO0O00OOO0OO00O0 =O000O00OOO0OOO0OO *math .sin (OO00O0O0O00OO0O00 )#line:874
                                        O00OOO0O00O0O0OO0 [0 ]=O0O000O0O0OO00OOO #line:876
                                        O00O0O0000OO0OOO0 [0 ]=O000OOOO0O0OOO00O #line:877
                                        O0O0O00OO000OO0O0 [0 ]=O0000OOOOOO0000OO #line:878
                                        OOO0OO0000000O000 [0 ]=OOO0O00OOO0OO00O0 #line:879
                                        for O00OO0OOO0O00OOOO in range (OOOO0OOO00O00OO0O -1 ):#line:880
                                                OO0OO0O000000OOOO =math .sqrt (O0O0O00OO000OO0O0 [O00OO0OOO0O00OOOO ]**2 +OOO0OO0000000O000 [O00OO0OOO0O00OOOO ]**2 )#line:881
                                                O0OO0OO0000000O0O =-O0O0OO00OO0O00O0O *OO0OO0O000000OOOO *O0O0O00OO000OO0O0 [O00OO0OOO0O00OOOO ]#line:882
                                                OOOO00O0OO00OOOOO [O00OO0OOO0O00OOOO ]=O0OO0OO0000000O0O /OOO000O0O0OO00OO0 #line:883
                                                O0O0O00OO000OO0O0 [O00OO0OOO0O00OOOO +1 ]=O0O0O00OO000OO0O0 [O00OO0OOO0O00OOOO ]+OOOO00O0OO00OOOOO [O00OO0OOO0O00OOOO ]*OOOO0O0OOOO00O00O #line:884
                                                O00OOO0O00O0O0OO0 [O00OO0OOO0O00OOOO +1 ]=O00OOO0O00O0O0OO0 [O00OO0OOO0O00OOOO ]+O0O0O00OO000OO0O0 [O00OO0OOO0O00OOOO +1 ]*OOOO0O0OOOO00O00O #line:885
                                                OO0000O00O0O00OO0 =-OOO000O0O0OO00OO0 *O0000O00O0O00O0OO -O0O0OO00OO0O00O0O *OO0OO0O000000OOOO *OOO0OO0000000O000 [O00OO0OOO0O00OOOO ]#line:886
                                                O000OO00OO000O0OO [O00OO0OOO0O00OOOO ]=OO0000O00O0O00OO0 /OOO000O0O0OO00OO0 #line:887
                                                OOO0OO0000000O000 [O00OO0OOO0O00OOOO +1 ]=OOO0OO0000000O000 [O00OO0OOO0O00OOOO ]+O000OO00OO000O0OO [O00OO0OOO0O00OOOO ]*OOOO0O0OOOO00O00O #line:888
                                                O00O0O0000OO0OOO0 [O00OO0OOO0O00OOOO +1 ]=O00O0O0000OO0OOO0 [O00OO0OOO0O00OOOO ]+OOO0OO0000000O000 [O00OO0OOO0O00OOOO +1 ]*OOOO0O0OOOO00O00O #line:889
                                                if (O00O0O0000OO0OOO0 [O00OO0OOO0O00OOOO +1 ]<0 ):#line:890
                                                        break #line:891
                                        OOO0000OOO000O000 =O00OO0OOO0O00OOOO #line:892
                                        O0OOOOO0O00OOO00O .append (O00OOO0O00O0O0OO0 [OOO0000OOO000O000 ])#line:893
                                return (O0OOOOO0O00OOO00O );#line:895
                        import random as r #line:898
                        O0O00000O0OOOOOOO =[]#line:899
                        OOOOOO0O00O0OOO0O =False #line:900
                        OOO0000O00OOO0OO0 =[]#line:901
                        OO00O0OO0OOO0O000 =0.1 #line:902
                        OO00OOO000O0O0OO0 =1.5 #line:903
                        for O0OO0OOOO00OOO000 in range (5 ):#line:904
                                O0O00000O0OOOOOOO .append (r .uniform (OO00O0OO0OOO0O000 ,OO00OOO000O0O0OO0 ))#line:905
                        O0O00000O0OOOOOOO .sort ()#line:906
                        print ('Testing thetas=',O0O00000O0OOOOOOO )#line:907
                        O0000000O000O0O00 =O0O0O0O00000000OO (O0O00000O0OOOOOOO )#line:908
                        print ('Output ximpacts=',O0000000O000O0O00 )#line:909
                        O0O00O0O0O0OO00O0 =OO0O000O0O0OOOO00 (O0O00000O0OOOOOOO )#line:910
                        print ('Actual ximpacts=',O0O00O0O0O0OO00O0 )#line:911
                        print ()#line:912
                        if (not type (O0000000O000O0O00 )==type (O0O00O0O0O0OO00O0 ))or (not len (O0000000O000O0O00 )==len (O0O00O0O0O0OO00O0 )):#line:913
                                if OOOOOO0O00O0OOO0O ==False :#line:914
                                        OOOOOO0O00O0OOO0O =True #line:915
                        else :#line:916
                                OOO0000O00OOO0OO0 .append (all (np .isclose (O0000000O000O0O00 ,O0O00O0O0O0OO00O0 ,rtol =O0O0OOO0OO0OO0OOO ,atol =OOOO000O00O0O00OO )))#line:917
                        if OOOOOO0O00O0OOO0O :#line:919
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:920
                        else :#line:922
                                OOO00OOOO00OOO000 =all (OOO0000O00OOO0OO0 )#line:923
                                if OOO00OOOO00OOO000 :#line:924
                                        print ("Well done, all correct.")#line:925
                                else :#line:926
                                        print ("Not close enough. Take another look then run this cell again.")#line:927
                                OOOO00OOO0OO00000 =trycount (OOO0O0OO000OOOOOO ,OOO00OOOO00OOO000 )#line:929
                                O00OO00OOO0OOO00O =100 -(OOOO00OOO0OO00000 [0 ]-1 )*10 #line:930
                                if OOOO00OOO0OO00000 [1 ]:#line:931
                                        print ("First success after ",OOOO00OOO0OO00000 [0 ]," tries, you have ",O00OO00OOO0OOO00O ,"% on this exercise.")#line:932
                                else :#line:933
                                        print ("You have had ",OOOO00OOO0OO00000 [0 ]," tries.")#line:934
                                        print ("If next try is accepted you will achieve ",O00OO00OOO0OOO00O -10 ,"% on this exercise.")#line:935
                        O0O00O0O0O0OO00O0 =None #line:938
                        OO0O000O0O0OOOO00 =None #line:939
        return #line:941
def b3 ():#line:951
    global ps #line:953
    O00OOO0O0OOO00OOO =".b3_counter.npy"#line:956
    OO0OO0O0OOOOOO00O =np .zeros (1 ,dtype ='int8,bool')#line:957
    O0000O00O000OOOO0 =0.01 #line:960
    if (waiter ()):#line:962
        while True :#line:963
            try :#line:964
                printmd ('**CA**')#line:965
                O00OOOO00OOOOOOO0 =float (input ("Enter a real number here: "))#line:966
                OO0O0O00OOOOO0OOO =0.5 #line:967
                OO00OO0OO0000000O =np .isclose (O00OOOO00OOOOOOO0 ,OO0O0O00OOOOO0OOO ,atol =O0000O00O000OOOO0 )#line:968
                if OO00OO0OO0000000O :#line:969
                    print ("Well done. Actual value is ",OO0O0O00OOOOO0OOO )#line:970
                else :#line:971
                    print ("Not right yet. Take another look then run this cell again.")#line:972
                OO0OO0O0OOOOOO00O =trycount (O00OOO0O0OOO00OOO ,OO00OO0OO0000000O )#line:974
                O0O0000O0OO0O0OOO =100 -(OO0OO0O0OOOOOO00O [0 ]-1 )*10 #line:975
                if OO0OO0O0OOOOOO00O [1 ]:#line:976
                    print ("First success after ",OO0OO0O0OOOOOO00O [0 ]," tries, you have ",O0O0000O0OO0O0OOO ,"% on this exercise.")#line:977
                else :#line:978
                    print ("You have had ",OO0OO0O0OOOOOO00O [0 ]," tries.")#line:979
                    print ("If next try is accepted you will achieve ",O0O0000O0OO0O0OOO -10 ,"% on this exercise.")#line:980
                break #line:982
            except ValueError :#line:984
                print ("I didn't understand that.")#line:985
                continue #line:986
        return #line:988
def b1_notlive ():#line:1000
        print ('This CA test is not currently live.')#line:1001
        return #line:1002
def b2_notlive (O00OO00O0O00O00O0 ):#line:1012
        print ('This CA test is not currently live.')#line:1013
        return #line:1014
def b3_notlive ():#line:1021
        print ('This CA test is not currently live.')#line:1022
        return #line:1023
def printmd (OOOO0O00O0OOO0000 ):#line:1033
    display (Markdown (OOOO0O00O0OOO0000 ))#line:1034
def repeat_to_length (OO0O000OOOO00O0O0 ,O0OO00O0000OOOOOO ):#line:1036
   return (OO0O000OOOO00O0O0 *((O0OO00O0000OOOOOO //len (OO0O000OOOO00O0O0 ))+1 ))[:O0OO00O0000OOOOOO ]#line:1037
def getco (O00OOOOO00OOOO0O0 ):#line:1039
    global ps #line:1040
    O0OO0OO0O00000O00 =getpass .getuser ()#line:1041
    OOO00OO0OO0OOOOOO =int .from_bytes (O0OO0OO0O00000O00 .encode (),'little')#line:1042
    OO0O00OOOO000OOOO =str (OOO00OO0OO0OOOOOO )#line:1043
    OOO0OO0O0OO00O000 =repeat_to_length (OO0O00OOOO000OOOO ,O00OOOOO00OOOO0O0 )#line:1044
    ps =[int (O00OOOO0OO000O00O )+1 for O00OOOO0OO000O00O in OOO0OO0O0OO00O000 ]#line:1045
def waiter ():#line:1047
    O0O00OOOO00000OOO =20 #line:1050
    OOOOO0000000OOOO0 =".ts1.txt"#line:1052
    if os .path .isfile (OOOOO0000000OOOO0 ):#line:1053
        O000000O0000OO0OO =np .loadtxt (OOOOO0000000OOOO0 )#line:1054
    else :#line:1056
        O000000O0000OO0OO =0.0 #line:1057
    O00O0OOO000O0O0O0 =time .time ()#line:1060
    O0000OOOO0000000O =O00O0OOO000O0O0O0 -O000000O0000OO0OO #line:1061
    if (O0000OOOO0000000O <O0O00OOOO00000OOO ):#line:1063
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O0000OOOO0000000O ,O0O00OOOO00000OOO ))#line:1064
        return False #line:1065
    else :#line:1066
        O0O00O000O0O0O000 =open (OOOOO0000000OOOO0 ,'w')#line:1067
        O0O00O000O0O0O000 .write (str (O00O0OOO000O0O0O0 ))#line:1068
        O0O00O000O0O0O000 .close ()#line:1069
        return True #line:1070
def trycount (OOO0OO0O0OO0OO0O0 ,OO00O0O000OO00OOO ):#line:1072
    if os .path .isfile (OOO0OO0O0OO0OO0O0 ):#line:1074
        OO00OO0OOOOO0O0O0 =np .load (OOO0OO0O0OO0OO0O0 )#line:1075
    else :#line:1077
        OO00OO0OOOOO0O0O0 =np .zeros (1 ,dtype ='int8,bool')#line:1078
        OO00OO0OOOOO0O0O0 =[0 ,False ]#line:1079
    if not OO00OO0OOOOO0O0O0 [1 ]:#line:1082
        OO00OO0OOOOO0O0O0 [0 ]+=1 #line:1083
        OO00OO0OOOOO0O0O0 [1 ]=OO00O0O000OO00OOO #line:1084
        np .save (OOO0OO0O0OO0OO0O0 ,OO00OO0OOOOO0O0O0 )#line:1086
    return OO00OO0OOOOO0O0O0 #line:1088
def valdho (O00OOOO0O00OO00OO ,O0OO0O00OO0O0OO0O ):#line:1096
    OO000O0O00O00OOOO =".dho_counter.npy"#line:1100
    O0000OOO0O000O0O0 =np .zeros (1 ,dtype ='int8,bool')#line:1102
    if (waiter ()):#line:1104
        while True :#line:1105
            try :#line:1106
                OO000O0OO0O0O00OO =float (input ("Please enter your estimate here: "))#line:1107
                O000OO000O0OO0O0O =2 *np .sqrt (O00OOOO0O00OO00OO *O0OO0O00OO0O0OO0O )#line:1108
                OO0OO00OOOO000OO0 =np .isclose (OO000O0OO0O0O00OO ,O000OO000O0OO0O0O ,0.2 )#line:1109
                if OO0OO00OOOO000OO0 :#line:1110
                    print ("Well done, that is close to the critical damping value ",O000OO000O0OO0O0O )#line:1111
                else :#line:1112
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1113
                O0000OOO0O000O0O0 =trycount (OO000O0O00O00OOOO ,OO0OO00OOOO000OO0 )#line:1115
                OOOO000000O000O00 =100 -(O0000OOO0O000O0O0 [0 ]-1 )*10 #line:1116
                if O0000OOO0O000O0O0 [1 ]:#line:1117
                    print ("First success after ",O0000OOO0O000O0O0 [0 ]," tries, you have ",OOOO000000O000O00 ,"% on this exercise.")#line:1118
                else :#line:1119
                    print ("You have had ",O0000OOO0O000O0O0 [0 ]," tries.")#line:1120
                    print ("If next try is accepted you will achieve ",OOOO000000O000O00 -10 ,"% on this exercise.")#line:1121
                break #line:1123
            except ValueError :#line:1125
                print ("I didn't understand that.")#line:1126
                continue #line:1127
        return #line:1130
def valdrivendho (O0OO000O00O0O0OO0 ,O000OO0O00000O000 ):#line:1140
    OOO00OOO00000O00O =".drivendho_counter.npy"#line:1144
    OO000OO00O00OO00O =np .zeros (1 ,dtype ='int8,bool')#line:1146
    if (waiter ()):#line:1148
        while True :#line:1149
            try :#line:1150
                OO0OOOOO00OOO00OO =float (input ("Please enter your estimate here: "))#line:1151
                O0000OO00OOOOOO0O =np .sqrt (O0OO000O00O0O0OO0 **2 -2 *O000OO0O00000O000 **2 )#line:1152
                OOO0O0OOOO00O0OO0 =np .isclose (OO0OOOOO00OOO00OO ,O0000OO00OOOOOO0O ,0.2 )#line:1153
                if OOO0O0OOOO00O0OO0 :#line:1154
                    print ("Well done, that is close to the resonance value ",O0000OO00OOOOOO0O )#line:1155
                else :#line:1156
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1157
                OO000OO00O00OO00O =trycount (OOO00OOO00000O00O ,OOO0O0OOOO00O0OO0 )#line:1159
                O00O0OOO00OO0OO00 =100 -(OO000OO00O00OO00O [0 ]-1 )*10 #line:1160
                if OO000OO00O00OO00O [1 ]:#line:1161
                    print ("First success after ",OO000OO00O00OO00O [0 ]," tries, you have ",O00O0OOO00OO0OO00 ,"% on this exercise.")#line:1162
                else :#line:1163
                    print ("You have had ",OO000OO00O00OO00O [0 ]," tries.")#line:1164
                    print ("If next try is accepted you will achieve ",O00O0OOO00OO0OO00 -10 ,"% on this exercise.")#line:1165
                break #line:1167
            except ValueError :#line:1169
                print ("I didn't understand that.")#line:1170
                continue #line:1171
        return #line:1174
import ipywidgets as widgets #line:1189
import sys #line:1190
from IPython .display import display #line:1191
from IPython .display import clear_output #line:1192
def create_multipleChoice_widget (O0OOO0OO0OO00OO0O ,OOO0O00O000O000OO ,O0O0000O0O0OO00O0 ,O0000O000O0O0O000 ):#line:1194
    OOOOOO00O0O000000 ='.q{:d}_counter.npy'.format (O0OOO0OO0OO00OO0O )#line:1195
    OO00O0O00OOOO0OO0 =np .zeros (1 ,dtype ='int8,bool')#line:1196
    O0OO00O0O0O00O0OO =len (O0O0000O0O0OO00O0 )#line:1198
    if O0000O000O0O0O000 not in O0O0000O0O0OO00O0 :#line:1199
        O0O0000O0O0OO00O0 .append (O0000O000O0O0O000 )#line:1200
    OOOO0O0000OOOOOOO =O0O0000O0O0OO00O0 .index (O0000O000O0O0O000 )#line:1202
    O0O00000OO00OOO00 =[(OO00000O0OOOOOO0O ,OOOOOO0OOO000O00O )for OOOOOO0OOO000O00O ,OO00000O0OOOOOO0O in enumerate (O0O0000O0O0OO00O0 )]#line:1204
    O0OO0O0O0000O0OO0 =widgets .RadioButtons (options =O0O00000OO00OOO00 ,description ='',disabled =False )#line:1209
    O0OOO0OOO00OOOO00 =widgets .Output ()#line:1211
    with O0OOO0OOO00OOOO00 :#line:1212
        print (OOO0O00O000O000OO )#line:1213
    O000OOOO0O0O00O00 =widgets .Output ()#line:1215
    def O0O0OO0O0OO0O00O0 (O0O0O0O0OOOO00OO0 ):#line:1217
        OOO00O000O0O00OO0 =int (O0OO0O0O0000O0OO0 .value )#line:1219
        O00O0O0OO0OO00O00 =OOO00O000O0O00OO0 ==OOOO0O0000OOOOOOO #line:1221
        OOO00OOOOOOOO0O0O =trycount (OOOOOO00O0O000000 ,O00O0O0OO0OO00O00 )#line:1222
        OOOOOOO0O0O00O000 =max (0 ,100 -(OOO00OOOOOOOO0O0O [0 ]-1 )*100 /O0OO00O0O0O00O0OO )#line:1223
        O00O0O0OO00O0000O =O0OO0O0O0000O0OO0 .options [OOO00O000O0O00OO0 ][0 ]#line:1224
        if O00O0O0OO0OO00O00 :#line:1225
            O00O0O0OO00O0000O +=' correct\n'#line:1226
        else :#line:1227
            O00O0O0OO00O0000O +=' incorrect\n'#line:1228
        if OOO00OOOOOOOO0O0O [1 ]:#line:1229
            O00O0O0OO00O0000O +='{:.0f}% on try {:d}'.format (OOOOOOO0O0O00O000 ,OOO00OOOOOOOO0O0O [0 ])#line:1230
        else :#line:1231
            O00O0O0OO00O0000O +='{:.0f}% remaining'.format (max (0 ,OOOOOOO0O0O00O000 -100 /O0OO00O0O0O00O0OO ))#line:1232
        with O000OOOO0O0O00O00 :#line:1234
            clear_output ()#line:1235
            print (O00O0O0OO00O0000O )#line:1236
        return #line:1237
    O00O0OO0OO0O0O000 =widgets .Button (description ="submit")#line:1239
    O00O0OO0OO0O0O000 .on_click (O0O0OO0O0OO0O00O0 )#line:1240
    return widgets .VBox ([O0OOO0OOO00OOOO00 ,O0OO0O0O0000O0OO0 ,O00O0OO0OO0O0O000 ,O000OOOO0O0O00O00 ])#line:1241
def runq1 ():#line:1248
    O0O0O0O00O00OO0O0 =1 #line:1249
    OO0OOOO0O00O00O0O =create_multipleChoice_widget (O0O0O0O00O00OO0O0 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1250
    display (OO0OOOO0O00O00O0O )#line:1251
def runQ1 ():#line:1261
    O0000OOO0OO0OO0O0 =1 #line:1262
    O00OOOO000OOOOOO0 =create_multipleChoice_widget (O0000OOO0OO0OO0O0 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1263
    display (O00OOOO000OOOOOO0 )#line:1264
def runQ2x ():#line:1273
    OO000O00O0O0OO0OO =2 #line:1274
    O00OO000O0O0O0O0O =create_multipleChoice_widget (OO000O00O0O0OO0OO ,'',['centred','backwards','forwards'],'centred')#line:1275
    display (O00OO000O0O0O0O0O )#line:1276
def runQ3x ():#line:1284
    O0OO0OO000OO00000 =3 #line:1285
    OOO0000OO0OOO0O00 =create_multipleChoice_widget (O0OO0OO000OO00000 ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1286
    display (OOO0000OO0OOO0O00 )#line:1287
def runQ4x ():#line:1296
    O00O0O0O000O00OOO =4 #line:1297
    O0O0O000OO0O0O0O0 =create_multipleChoice_widget (O00O0O0O000O00OOO ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1298
    display (O0O0O000OO0O0O0O0 )#line:1299
def runQ5x ():#line:1309
    OO00O000O0O00OO00 =5 #line:1310
    O00O00O0O00OOO0O0 =create_multipleChoice_widget (OO00O000O0O00OO00 ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1311
    display (O00O00O0O00OOO0O0 )#line:1312
def runQ6x ():#line:1321
    OO0000O000000O0O0 =6 #line:1322
    O0000OO00O0OO0O00 =create_multipleChoice_widget (OO0000O000000O0O0 ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1323
    display (O0000OO00O0OO0O00 )#line:1324
def runQ7x ():#line:1333
    O00O0O00O0OO0O0O0 =7 #line:1334
    OO0000OOO0OOO0OOO =create_multipleChoice_widget (O00O0O00O0OO0O0O0 ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1335
    display (OO0000OOO0OOO0OOO )#line:1336
