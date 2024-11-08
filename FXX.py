FXX/R,UP

 * FARE BASIS *  DISC    *  PSGR      * FARE<EGP>  * MSG  *T
01 LAOTEGF4   *          * P1         *  10838.80  *      *Y
02            * CH       * P2         *   8982.80  *      *Y
03            * IN       * P1         *   2632.80  *      *Y
04 LAOTEGC4   *          * P1         *   9471.80  *      *Y
05            * CH       * P2         *   7957.80  *      *Y
06            * IN       * P1         *   2482.80  *      *Y
07 LAOTEGB4   *          * P1         *   8054.80  *      *Y
08            * CH       * P2         *   6931.80  *      *Y
09            * IN       * P1         *   2299.80  *      *Y
*1-9*TICKET STOCK RESTRICTION
FARE FAMILIES:    (ENTER FQFn FOR DETAILS, FXY FOR UPSELL)
*1-3*FARE FAMILIES: NFLEXE
*4-6*FARE FAMILIES: NSEMIFLEXE
*7-9*FARE FAMILIES: NBASICE
>                                                 PAGE  1/ 1
--------------------------------------------------------------
// first line:
capture line:3, column:1, length:2 assign to TSTLine1
if (TSTLine1==TST1){
    capture line:3, column:28, length:5 assign to PaxCount1
}
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:5 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:5 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:5 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:5 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:5 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:5 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:5 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:5 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:5 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:5 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:5 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:5 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:5 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:5 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:5 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:5 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:5 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:5 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:5 assign to PaxCount3
      }
      
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  // There's a child
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/r,up"
      send "FXP/r,up"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/r,up"
      send "FXP/r,up"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  // There's a child
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/r,up"
      send "FXP/r,up"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/r,up"
      send "FXP/r,up"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}