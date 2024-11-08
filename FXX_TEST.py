      send "fxx/R,U,UP,U*SEE24,U*MOS05"
      ask "Enter number of ticket pricing to display" assign to FQQ1
      send "fqq" +FQQ1
      choose "is it ok?"{
        when ("Yes, Proceed!"){
        ask "Are You sure to take line number?" assign to T
        send "rfRAMADAN;er"
        send "er"
        send "trdc/all"
        capture line:1, column:1, length:26 assign to Voidmsg
        if (Voidmsg!="OK - DOCUMENT(S) CANCELLED"){
            ask "Is it voided?" assign to trdcr
        }
        send "ir"
          send "tte/all"
          send "rfRAMADAN;er"
          send "er"
          send "ir"
          send "tte/all"
          send "rfRAMADAN;er"
          send "er"
          send "ir"
          send "tte/all"
          send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
        send "fxp/R,U,UP,U*SEE24,U*MOS05"
group{
       mandatory ask "ENTER the Adult TST line ( Please take 01 insstead of 1" assign to TST1
       ask "ENTER the Child TST line" assign to TST2
       ask "ENTER the Infant TST line" assign to TST3
}
// first line:
capture line:3, column:1, length:2 assign to TSTLine1
if (TSTLine1==TST1){
    capture line:3, column:28, length:8 assign to PaxCount1
}
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:8 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:8 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:8 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:8 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:8 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:8 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:8 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:8 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:8 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:8 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:8 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:8 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:8 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:8 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:8 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:8 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:8 assign to PaxCount3
      }
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}
    

          send "rfRAMADAN;er"
          send "er"
          send "tth"
          call "z_Deal Checker"
          choose "Have you taken the deal?" until "yes"{
            when ("no"){
            send "ir"
            send "tte/all"
            send "rfRAMADAN;er"
            send "er"
            send "ir"
            send "tte/all"
            send "fxp/R,U,UP,U*SEE24,U*MOS05"
            // first line:
            capture line:3, column:1, length:2 assign to TSTLine1
            if (TSTLine1==TST1){
            capture line:3, column:28, length:8 assign to PaxCount1
            }
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:8 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:8 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:8 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:8 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:8 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:8 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:8 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:8 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:8 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:8 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:8 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:8 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:8 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:8 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:8 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:8 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:8 assign to PaxCount3
      }
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}
          send "rfRAMADAN;er"
          send "er"
          send "tth"
          call "z_Deal Checker"
          choose "Have you taken the deal?" until "yes"{
            when ("no"){
              send "ir"
            send "tte/all"
            send "rfRAMADAN;er"
            send "er"
            send "ir"
            send "tte/all"
            send "fxp/R,U,UP,U*SEE24,U*MOS05"
            // first line:
            capture line:3, column:1, length:2 assign to TSTLine1
            if (TSTLine1==TST1){
            capture line:3, column:28, length:8 assign to PaxCount1
            }
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:8 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:8 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:8 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:8 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:8 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:8 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:8 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:8 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:8 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:8 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:8 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:8 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:8 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:8 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:8 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:8 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:8 assign to PaxCount3
      }
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
      send "FXP/R,U,UP,U*SEE24,U*MOS05"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}
          send "rfRAMADAN;er"
          send "er"
            }
          }
            
            }
            
          }
          send "fpcash"
          send "fm0"
          call "z_RTTN_DEL"          
          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"}
  send "PV"
  capture line:2, column:30, length:9 assign to thisOfficeName
                      if (thisOfficeName == "KWIKT2809"){
                            send "RM FIRST ISSUE"
                            send "RM SKIP HF"
                            send "RM AMEX"
                        }
                        else{
                            if (thisOfficeName == "DXBAD31DO"){
                                send "RM FIRST ISSUE"
                                send "RM SKIP HF"
                                send "RM AMEX"
                            }
                            else{
                                if (thisOfficeName != "CAIEG3645"){
                                    send "RM FRESH ISSUE"
                                    send "RM SKIP HF"
                                    send "RM AMEX"
                                }
                            }
                        }

                        
                             send "rfRAMADAN;er"
                             send "er"
                             send "ttp/rt"
                             call "z_Name Sorter"
                             ask "continue?" assign to qz5
                             call "z_Deal Checker" 
                  
          
        }

        when ("NO, retry"){
          ask "PLease Enter The Next Fair Basis line no." assign to fqqno1
                  send "FQQ" +fqqno1
                  choose "Have you got the deal?" until "YES"{
                    when ("NO"){
                        ask "PLease Enter The Next Fair Basis line no." assign to fqqno2
                        send "FQQ" +fqqno2
                    }
                    when ("CALL FXR"){
                        send "fxr/k/R,U,UP,U*SEE24,U*MOS05"
                        call "FXX_TEST"
                    }
                  }
                  call "FXX_TEST"
  }
        when ("No, Ignore"){
          send "IG"  
        }
      }    




