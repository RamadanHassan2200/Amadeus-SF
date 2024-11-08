RP/RUHAA28WH/RUHAA28WH            WS/SU  10SEP24/1314Z   LS8UUE
 45 FA PAX 512-6200949335/ETRJ/10SEP24/RUHAA2218/71213181
       /S3-4/P1
 46 FA PAX 512-6200949338/ETRJ/10SEP24/RUHAA2218/71213181
       /S3-4/P2
>tth
T     P/S  NAME                   TOTAL            FOP                 SEGMENTS 
5    .1  TALASUAD/FARAKH M        SAR       884.00 CCAXXXXXXXXXXXX0001/09+3-4   
6    .2  TSHAMMAA/MOKHAMMAD       SAR       779.00 CCAXXXXXXXXXXXX0001/09+3-4   

DELETED TSTS                                                                    
1         ALASUAD/FARAKH M        SAR    1239.00                                
2         SHAMMAA/MOKHAMMAD       SAR    1045.00                                
3         ALASUAD/FARAKH M        SAR    1239.00                                
4         SHAMMAA/MOKHAMMAD       SAR    1045.00 

-----------------------------------------------------
//for FA use RTTN
------------------------------
//for price diff
capture line:1, column:1, length:3 assign to newTSTs
if (newTSTs=="T  "){
  capture line:2, column:35, length:3 assign to curr
  capture line:2, column:41, length:10 assign to firstTST
  capture line:3, column:1, length:1 assign to checkSec2
  if (checkSec2 !=" "){
       capture line:3, column:41, length:10 assign to secondTST
  }
  capture line:4, column:1, length:1 assign to checkSec3
  if (checkSec3 !=" "){
       capture line:4, column:41, length:10 assign to thirdTST   
  }
  capture line:5, column:1, length:1 assign to checkSec4
  if (checkSec4 !=" "){
       capture line:5, column:41, length:10 assign to fourthTST
  }
  capture line:6, column:1, length:1 assign to checkSec5
  if (checkSec5 !=" "){
       capture line:6, column:41, length:10 assign to fifthTST
  }
  capture line:7, column:1, length:1 assign to checkSec6
  if (checkSec6 !=" "){
       capture line:7, column:41, length:10 assign to sixthTST
  }               
}
if (sixthTST!=""){
       capture line:10, column:40, length:10 assign to TST1
       capture line:11, column:40, length:10 assign to TST2
       capture line:12, column:40, length:10 assign to TST3
       capture line:13, column:40, length:10 assign to TST4
       capture line:14, column:40, length:10 assign to TST5
       capture line:15, column:40, length:10 assign to TST6

       send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST +";" +TST6 +"-" +sixthTST 
}
else{
if (fifthTST!=""){
       capture line:9, column:40, length:10 assign to TST1
       capture line:10, column:40, length:10 assign to TST2
       capture line:11, column:40, length:10 assign to TST3
       capture line:12, column:40, length:10 assign to TST4
       capture line:13, column:40, length:10 assign to TST5

       send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST 
}
else{
if (fourthTST!=""){
       capture line:8, column:40, length:10 assign to TST1
       capture line:9, column:40, length:10 assign to TST2
       capture line:10, column:40, length:10 assign to TST3
       capture line:11, column:40, length:10 assign to TST4

       send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST
}
else{
if (thirdTST!=""){
       capture line:7, column:40, length:10 assign to TST1
       capture line:8, column:40, length:10 assign to TST2
       capture line:9, column:40, length:10 assign to TST3

       send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST
}
else{
if (secondTST!=""){
       capture line:6, column:40, length:10 assign to TST1
       capture line:7, column:40, length:10 assign to TST2

       send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST 
}
else{
if (firstTST!=""){
       capture line:5, column:40, length:10 assign to TST1
       send "df" +TST1 +"-" +firstTST 
}

}//1
}//2
}//3
}//4
}//5