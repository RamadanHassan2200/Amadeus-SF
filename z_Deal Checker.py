//for price diff
send "TTH"
capture line:1, column:1, length:1 assign to newTSTs
assign "0" to TSTCount
if (newTSTs=="T"){
  assign "1" to TSTCount
  capture line:2, column:35, length:3 assign to curr1
  capture line:2, column:41, length:10 assign to firstTST
  capture line:4, column:1, length:1 assign to checkSec2
  if (checkSec2 ==" "){
        assign "2" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
  }
  capture line:5, column:1, length:1 assign to checkSec3
  if (checkSec3 ==" "){
        assign "3" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
  }
  capture line:6, column:1, length:1 assign to checkSec4
  if (checkSec4 ==" "){
        assign "4" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
  }
  capture line:7, column:1, length:1 assign to checkSec5
  if (checkSec5 ==" "){
        assign "5" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
  }
  capture line:8, column:1, length:1 assign to checkSec6
  if (checkSec6 ==" "){
        assign "6" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
       capture line:7, column:41, length:10 assign to sixthTST
  }
  capture line:9, column:1, length:1 assign to checkSec7
  if (checkSec7 ==" "){
       assign "7" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
       capture line:7, column:41, length:10 assign to sixthTST
       capture line:8, column:41, length:10 assign to seventhTST
  }
  capture line:10, column:1, length:1 assign to checkSec8
  if (checkSec8 ==" "){
       assign "8" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
       capture line:7, column:41, length:10 assign to sixthTST
       capture line:8, column:41, length:10 assign to seventhTST
       capture line:9, column:41, length:10 assign to eighthTST
  }
  capture line:11, column:1, length:1 assign to checkSec9
  if (checkSec9 ==" "){
       assign "9" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
       capture line:7, column:41, length:10 assign to sixthTST
       capture line:8, column:41, length:10 assign to seventhTST
       capture line:9, column:41, length:10 assign to eighthTST
       capture line:10, column:41, length:10 assign to ninthTST
  }
}

assign "0" to TST1
assign "0" to TST2
assign "0" to TST3
assign "0" to TST4
assign "0" to TST5
assign "0" to TST6
assign "0" to TST7
assign "0" to TST8
assign "0" to TST9

if (TSTCount=="0"){
  ask "No Active TST Found!" assign to qz5
}
if (TST)




if (TSTCount=="6"){
       capture line:10, column:35, length:3 assign to curr2
       capture line:10, column:40, length:10 assign to TST1
       capture line:11, column:40, length:10 assign to TST2
       capture line:12, column:40, length:10 assign to TST3
       capture line:13, column:40, length:10 assign to TST4
       capture line:14, column:40, length:10 assign to TST5
       capture line:15, column:40, length:10 assign to TST6
       if(curr1=="EGP"){
          send "df" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST +";" +fifthTST +";" +sixthTST
              capture line:2, column:1, length:11 assign to egydeal
        
          send "FQC" +egydeal +"EGP/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +";" +TST6 +"-" +curr2deal
              capture line:2, column:1, length:11 assign to diff
              send "df" + curr2deal +"*0.04;" +diff
       }
       else{
          send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST +";" +TST6 +"-" +sixthTST 
       }
}
else{
if (TSTCount=="5"){
       capture line:9, column:35, length:3 assign to curr2
       capture line:9, column:40, length:10 assign to TST1
       capture line:10, column:40, length:10 assign to TST2
       capture line:11, column:40, length:10 assign to TST3
       capture line:12, column:40, length:10 assign to TST4
       capture line:13, column:40, length:10 assign to TST5
       if(curr1=="EGP"){
            send "df" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST +";" +fifthTST 
            capture line:2, column:1, length:11 assign to egydeal
            send "FQC" +egydeal +"EGP/" +curr2
            if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +"-" +curr2deal
                 capture line:2, column:1, length:11 assign to diff
                 send "df" + curr2deal +"*0.04;" +diff
         }
         else{
            send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST
         }
}
else{
if (TSTCount=="4"){
       capture line:8, column:35, length:3 assign to curr2
       capture line:8, column:40, length:10 assign to TST1
       capture line:9, column:40, length:10 assign to TST2
       capture line:10, column:40, length:10 assign to TST3
       capture line:11, column:40, length:10 assign to TST4

if(curr1=="EGP"){
     send "df" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST 
    capture line:2, column:1, length:11 assign to egydeal
     send "FQC" +egydeal +"EGP/" +curr2
     if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4  +"-" +curr2deal
         capture line:2, column:1, length:11 assign to diff
          send "df" + curr2deal +"*0.04;" +diff
  }
  else{
     send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST  
  }
}
else{
if (TSTCount=="3"){
       capture line:7, column:35, length:3 assign to curr2
       capture line:7, column:40, length:10 assign to TST1
       capture line:8, column:40, length:10 assign to TST2
       capture line:9, column:40, length:10 assign to TST3

if(curr1=="EGP"){
     send "df" +firstTST +";" +secondTST +";" +thirdTST 
    capture line:2, column:1, length:11 assign to egydeal
     send "FQC" +egydeal +"EGP/" +curr2
      if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +"-" +curr2deal
          capture line:2, column:1, length:11 assign to diff
          send "df" + curr2deal +"*0.04;" +diff
  }
  else{
     send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST 
  }
}
else{
if (TSTCount=="2"){
       capture line:6, column:35, length:3 assign to curr2
       capture line:6, column:40, length:10 assign to TST1
       capture line:7, column:40, length:10 assign to TST2

if(curr1=="EGP"){
     send "df" +firstTST +";" +secondTST 
     capture line:2, column:1, length:11 assign to egydeal
     send "FQC" +egydeal +"EGP/" +curr2
     if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +"-" +curr2deal
          capture line:2, column:1, length:11 assign to diff
          send "df" + curr2deal +"*0.04;" +diff
  }
  else{
     send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST 
  } 
}
else{
if (firstTST<="9999999"){
       capture line:5, column:35, length:3 assign to curr2
       capture line:5, column:40, length:10 assign to TST1
if(curr1=="EGP"){
     send "FQC" +firstTST +"EGP/" +curr2
    if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1  +"-" +curr2deal
          capture line:2, column:1, length:11 assign to diff
          send "df" + curr2deal +"*0.04;" +diff
  }
  else{
     send "df" +TST1 +"-" +firstTST
  }
}

}//1
}//2
}//3
}//4
}//5