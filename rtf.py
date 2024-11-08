ERROR DURING PROFILE TRANSFER
FP, 1: FARE ELEMENT ALREADY EXISTS FOR PASSENGER/SEGMENT (3671)

choose "what currency is this? "{
when ("SAR"){
send "fqc" +egp +"/SAR"
}
when ("KWD"){
send "fqc" +egp +"/KWD"
}
when ("AED"){
send "fqc" +egp +"/SAR"
}
}
-------------------------------------
RP/RUHAA28WH/RUHAA28WH            92/AS  19AUG24/1535Z   OWLQUX
 48 FA PAX 381-3707496807/EVSM/19AUG24/RUHAA2218/71213181/S4/P3
 49 FA PAX 381-3707496810/EVSM/19AUG24/RUHAA2218/71213181/S4/P1
 50 FA PAX 381-3707496811/EVSM/19AUG24/RUHAA2218/71213181/S4/P2
 51 FB PAX 0000000000 TTP/T3/RT OK ETICKET/S4/P3
 52 FB PAX 0000000000 TTP/T4/RT OK ETICKET/S4/P1-2
 53 FE PAX FEES FOR CHNG/REF/NO SHOW ANCILLARY IS NON REFUNDABL
       /S4/P3
 54 FE PAX FEES FOR CHNG/REF/NO SHOW ANCILLARY IS NON REFUNDABL
       /S4/P1-2
 55 FG PAX 0000000000 JED1A01TT/S4/P3
 56 FG PAX 0000000000 NCE1A85EM/S4/P3
 57 FG PAX 0000000000 JED1A01TT/S4/P1-2
 58 FG PAX 0000000000 NCE1A85EM/S4/P1-2
 59 FM PAX *F*0.00/S4/P1-2
 60 FM PAX *F*0.00/S4/P3
 61 FP CASH
 62 FT PAX *F*SERRA/S4/P3
 63 FT PAX *F*SERRA/S4/P1-2
 64 FV PAX *F*SM/S4/P3
 65 FV PAX *F*SM/S4/P1-2
 -------------------------------
 RP/RUHAA28WH/RUHAA28WH            GG/SU  19AUG24/1535Z   OWLQUX
 RUHAA28WH/9999WS/19AUG24
  47 FA PAX 381-3707496807/EVSM/19AUG24/RUHAA2218/71213181/S4/P3
  48 FA PAX 381-3707496810/EVSM/19AUG24/RUHAA2218/71213181/S4/P1
  49 FA PAX 381-3707496811/EVSM/19AUG24/RUHAA2218/71213181/S4/P2
  50 FB PAX 0000000000 TTP/T3/RT OK ETICKET/S4/P3
  51 FB PAX 0000000000 TTP/T4/RT OK ETICKET/S4/P1-2
  52 FE PAX FEES FOR CHNG/REF/NO SHOW ANCILLARY IS NON REFUNDABL
        /S4/P1-2
  53 FE PAX FEES FOR CHNG/REF/NO SHOW ANCILLARY IS NON REFUNDABL
        /S4/P3
  54 FG PAX 0000000000 JED1A01TT/S4/P3
  55 FG PAX 0000000000 NCE1A85EM/S4/P3
  56 FG PAX 0000000000 JED1A01TT/S4/P1-2
  57 FG PAX 0000000000 NCE1A85EM/S4/P1-2
  58 FP CASH
  59 FV PAX SM/S4/P1-2
  60 FV PAX SM/S4/P3
  -----------------------------
REQUESTED DISPLAY NOT SCROLLABLE
-------------------------------------
RP/RUHAA2218/RUHAA2218            GG/SU  19AUG24/1628Z   PRH93R
RUHAA2218/360404/19AUG24
 36 FHE PAX 381-3707500978/P1
 37 FHE PAX 381-3707500979/P2
 38 FE PAX FEES FOR CHNG/REF/NO SHOW ANCILLARY IS NON REFUNDABL
       /S3/P1-2
 39 FP CASH
 40 FV PAX SM/S3/P1-2
 ----------------------------------
 capture line:2, column:5, length:2 assign to FA1
 if (FA1=="FA"){
 capture line:2, column:2, length:2 assign to XFA1
  capture line:3, column:5, length:2 assign to FA2
  if (FA2=="FA"){
    capture line:4, column:5, length:2 assign to FA3
    
  }
 }
------------------------------
RP/RUHAA28WH/RUHAA28WH            GG/SU  19AUG24/1648Z   OOY9NN
RUHAA28WH/9999WS/19AUG24
 48 FA PAX 381-3707503343/EVSM/19AUG24/RUHAA2218/71213181/S6/P2
 49 FA PAX 381-3707503344/EVSM/19AUG24/RUHAA2218/71213181/S6/P3
 50 FA PAX 381-3707503345/EVSM/19AUG24/RUHAA2218/71213181/S6/P4
 51 FA PAX 381-3707503346/EVSM/19AUG24/RUHAA2218/71213181/S6/P1
 52 FA PAX 381-3707503347/EVSM/19AUG24/RUHAA2218/71213181/S6/P5
 53 FB PAX 0000000000 TTP/T7/RT OK ETICKET/S6/P2-4
 54 FB PAX 0000000000 TTP/T8/RT OK ETICKET/S6/P1,5
 55 FE PAX FEES FOR CHNG//NO SHOW/S6/P1,5
 56 FE PAX FEES FOR CHNG//NO SHOW/S6/P2-4
 57 FG PAX 0000000000 JED1A01TT/S6/P2-4
 58 FG PAX 0000000000 NCE1A85EM/S6/P2-4
 59 FG PAX 0000000000 JED1A01TT/S6/P1,5
 60 FG PAX 0000000000 NCE1A85EM/S6/P1,5
 61 FP CASH
 62 FV PAX SM/S6/P1,5
 63 FV PAX SM/S6/P2-4
--------------------------------
RP/RUHAA28WH/RUHAA28WH            GG/SU  22AUG24/1603Z   J2S5I8
RUHAA28WH/9999WS/22AUG24
 33 FA PAX 077-3707567378/EVMS/SAR525.00/22AUG24/RUHAA28WH/71213
       181/S6/P1
 34 FA PAX 077-3707567379/EVMS/SAR525.00/22AUG24/RUHAA28WH/71213
       181/S6/P2
 35 FA PAX 077-3707567380/EVMS/SAR525.00/22AUG24/RUHAA28WH/71213
       181/S6/P5
 36 FA PAX 077-3707567381/EVMS/SAR509.00/22AUG24/RUHAA28WH/71213
       181/S6/P3
 37 FA PAX 077-3707567382/EVMS/SAR509.00/22AUG24/RUHAA28WH/71213
       181/S6/P4
 38 FB PAX 0000000000 TTP OK ETICKET NO PRINTERS DEFINED IN
       OFFICE PROFILE - PLEASE CALL HELP DESK/S6/P1-2,5
 39 FB PAX 0000000001 TTP OK ETICKET NO PRINTERS DEFINED IN
       OFFICE PROFILE - PLEASE CALL HELP DESK/S6/P3-4
 40 FE PAX BAG. BUSINESS 32KG/158CM BAG. ECONOMY 23KG/158CM HAVE
       A NICE TRIP/S6/P1-2,5
 41 FE PAX BAG. BUSINESS 32KG/158CM BAG. ECONOMY 23KG/158CM HAVE
       A NICE TRIP/S6/P3-4
 42 FG PAX 0000000000 JED1A01TT/S6/P1-2,5
 43 FG PAX 0000000000 NCE1A84NA/S6/P1-2,5
 44 FG PAX 0000000000 JED1A01TT/S6/P3-4
)>
--------------------------------------------------
RP/RUHAA28WH/RUHAA28WH            GG/SU  27AUG24/1902Z   KV9E3P
RUHAA28WH/9999WS/27AUG24
 37 FA PAX 077-3707675332/EVMS/27AUG24/RUHAA2218/71213181/S6/P1
 38 FA PAX 077-3707675333/EVMS/27AUG24/RUHAA2218/71213181/S6/P2
 39 FA PAX 077-3707675334/EVMS/27AUG24/RUHAA2218/71213181/S6/P4
 40 FA PAX 077-3707675335/EVMS/27AUG24/RUHAA2218/71213181/S6/P5
 41 FA PAX 077-3707675336/EVMS/27AUG24/RUHAA2218/71213181/S6/P3
 42 FB PAX 0000000000 TTP OK ETICKET/S6/P1-2,4-5
 43 FB PAX 0000000001 TTP OK ETICKET/S6/P3
 44 FE PAX BAG. BUSINESS 32KG/158CM BAG. ECONOMY 23KG/158CM
       DEPARTURE FRM SEASONALHALL/S6/P1-2,4-5
 45 FE PAX BAG. BUSINESS 32KG/158CM BAG. ECONOMY 23KG/158CM
       DEPARTURE FRM SEASONALHALL/S6/P3
 46 FG PAX 0000000000 JED1A01TT/S6/P1-2,4-5
 47 FG PAX 0000000000 NCE1A85EM/S6/P1-2,4-5
 48 FG PAX 0000000000 JED1A01TT/S6/P3
 49 FG PAX 0000000000 NCE1A85EM/S6/P3
 50 FM PAX *F*5.00/S6/P1-2,4-5
 51 FM PAX *F*5.00/S6/P3
 52 FP CASH
 53 FT PAX *F*SA88PROM/S6/P1-2,4-5
 54 FT PAX *F*SA88PROM/S6/P3
 55 FV PAX *F*MS/S6/P1-2,4-5
)>
---------------------------------------------------
capture line:2, column:29, length:3 assign to airlinex1
if (airlinex1=="MS/"){
       
}
else{
       if (airlinex1=="SM/"){
              
       }
       else{
              capture line:3, column:29, length:3 assign to airlinex1
              if (airlinex1=="MS/"){

              }
              else{
                     if (airlinex1=="SM/"){

                     }
                     else{

                     }
              }
       }
}
------------------------------------
//FOP DELETE FPCASH
capture line:1, column:5, length:7 assign to FOP1
if(FOP1=="FP CASH"){
       capture line:1, column:2, length:2 assign to FOPL1
       send "XE" +FOPL1
}
else{
capture line:2, column:5, length:7 assign to FOP2
if(FOP2=="FP CASH"){
       capture line:2, column:2, length:2 assign to FOPL2
       send "XE" +FOPL2
}
else{
capture line:3, column:5, length:7 assign to FOP3
if(FOP3=="FP CASH"){
       capture line:3, column:2, length:2 assign to FOPL3
       send "XE" +FOPL3
}
else{
capture line:4, column:5, length:7 assign to FOP4
if(FOP4=="FP CASH"){
       capture line:4, column:2, length:2 assign to FOPL4
       send "XE" +FOPL4
}
else{
capture line:5, column:5, length:7 assign to FOP5
if(FOP5=="FP CASH"){
       capture line:5, column:2, length:2 assign to FOPL5
       send "XE" +FOPL5
}
else{
capture line:6, column:5, length:7 assign to FOP6
if(FOP6=="FP CASH"){
       capture line:6, column:2, length:2 assign to FOPL6
       send "XE" +FOPL6
}
else{
capture line:7, column:5, length:7 assign to FOP7
if(FOP7=="FP CASH"){
       capture line:7, column:2, length:2 assign to FOPL7
       send "XE" +FOPL7
}
else{
capture line:8, column:5, length:7 assign to FOP8
if(FOP8=="FP CASH"){
       capture line:8, column:2, length:2 assign to FOPL8
       send "XE" +FOPL8
}
else{
capture line:9, column:5, length:7 assign to FOP9
if(FOP9=="FP CASH"){
       capture line:9, column:2, length:2 assign to FOPL9
       send "XE" +FOPL9
}
else{
capture line:10, column:5, length:7 assign to FOP10
if(FOP10=="FP CASH"){
       capture line:10, column:2, length:2 assign to FOPL10
       send "XE" +FOPL10
}
else{
capture line:11, column:5, length:7 assign to FOP11
if(FOP11=="FP CASH"){
       capture line:11, column:2, length:2 assign to FOPL11
       send "XE" +FOPL11
}
else{
capture line:12, column:5, length:7 assign to FOP12
if(FOP12=="FP CASH"){
       capture line:12, column:2, length:2 assign to FOPL12
       send "XE" +FOPL12
}
else{
capture line:13, column:5, length:7 assign to FOP13
if(FOP13=="FP CASH"){
       capture line:13, column:2, length:2 assign to FOPL13
       send "XE" +FOPL13
}
else{
capture line:14, column:5, length:7 assign to FOP14
if(FOP14=="FP CASH"){
       capture line:14, column:2, length:2 assign to FOPL14
       send "XE" +FOPL14
}
else{
capture line:15, column:5, length:7 assign to FOP15
if(FOP15=="FP CASH"){
       capture line:15, column:2, length:2 assign to FOPL15
       send "XE" +FOPL15
}
else{
capture line:16, column:5, length:7 assign to FOP16
if(FOP16=="FP CASH"){
       capture line:16, column:2, length:2 assign to FOPL16
       send "XE" +FOPL16
}
else{
capture line:17, column:5, length:7 assign to FOP17
if(FOP17=="FP CASH"){
       capture line:17, column:2, length:2 assign to FOPL17
       send "XE" +FOPL17
}
else{
capture line:18, column:5, length:7 assign to FOP18
if(FOP18=="FP CASH"){
       capture line:18, column:2, length:2 assign to FOPL18
       send "XE" +FOPL18
}
else{
capture line:19, column:5, length:7 assign to FOP19
if(FOP19=="FP CASH"){
       capture line:19, column:2, length:2 assign to FOPL19
       send "XE" +FOPL19
}
else{
capture line:20, column:5, length:7 assign to FOP20
if(FOP20=="FP CASH"){
       capture line:20, column:2, length:2 assign to FOPL20
       send "XE" +FOPL20
}
else{
capture line:21, column:5, length:7 assign to FOP21
if(FOP21=="FP CASH"){
       capture line:21, column:2, length:2 assign to FOPL21
       send "XE" +FOPL21
}
else{
capture line:22, column:5, length:7 assign to FOP22
if(FOP22=="FP CASH"){
       capture line:22, column:2, length:2 assign to FOPL22
       send "XE" +FOPL22
}
else{
capture line:23, column:5, length:7 assign to FOP23
if(FOP23=="FP CASH"){
       capture line:23, column:2, length:2 assign to FOPL23
       send "XE" +FOPL23
}
else{
       ask "What is the (FP CASH) line no?" assign to delFP
       send "XE" +delFP
}
}//23
}//22
}//21
}//20
}//19
}//18
}//17
}//16
}//15
}//14
}//13
}//12
}//11
}//10
}//9
}//8
}//7
}//6
}//5
}//4
}//3
}//2
----------------------------
FQC50000/EGP                                                                    
BSR CONVERSION OF SAR TO EGP                                                    
EGP 651086.00 - ROUNDED AS FARES                                                
EGP 651086.00 - ROUNDED AS OTHER CHARGES                                        
EGP 651085.45 - AMOUNT TRUNCATED                                                
BSR USED 1 SAR = 13.021709 EGP EFF 27AUG24 DISC 27AUG24                         

ROUNDING OF FARES UP TO 1.00 EGP                                                
ROUNDING OF OTHER CHARGES UP TO 1.00 EGP                                        

SAR - SAUDI RIYAL                                                               
EGP - EGYPTIAN POUND