send "TTH"
capture line:1, column:1, length:1 assign to newTSTs

assign "0" to TSTCount
if (newTSTs=="T"){
  assign "1" to TSTCount

  capture line:2, column:11, length:20 assign to PName1
  capture line:3, column:11, length:20 assign to PName2
  capture line:4, column:11, length:20 assign to PName3
  capture line:5, column:11, length:20 assign to PName4
  capture line:6, column:11, length:20 assign to PName5
  capture line:7, column:11, length:20 assign to PName6
  capture line:8, column:11, length:20 assign to PName7
  capture line:9, column:11, length:20 assign to PName8
  capture line:10, column:11, length:20 assign to PName9
  capture line:11, column:11, length:20 assign to PName10
  capture line:12, column:11, length:20 assign to PName11
  capture line:13, column:11, length:20 assign to PName12
  capture line:14, column:11, length:20 assign to PName13
  capture line:15, column:11, length:20 assign to PName14
  capture line:16, column:11, length:20 assign to PName15
  capture line:17, column:11, length:20 assign to PName16
  capture line:18, column:11, length:20 assign to PName17
  capture line:19, column:11, length:20 assign to PName18
  capture line:20, column:11, length:20 assign to PName19
  capture line:21, column:11, length:20 assign to PName20
  capture line:22, column:11, length:20 assign to PName21
  capture line:23, column:11, length:20 assign to PName22
  
  capture line:2, column:40, length:11 assign to newTSTPrice1
  capture line:3, column:40, length:11 assign to newTSTPrice2
  capture line:4, column:40, length:11 assign to newTSTPrice3
  capture line:5, column:40, length:11 assign to newTSTPrice4
  capture line:6, column:40, length:11 assign to newTSTPrice5
  capture line:7, column:40, length:11 assign to newTSTPrice6
  capture line:8, column:40, length:11 assign to newTSTPrice7
  capture line:9, column:40, length:11 assign to newTSTPrice8
  capture line:10, column:40, length:11 assign to newTSTPrice9
  capture line:11, column:40, length:11 assign to newTSTPrice10
  capture line:12, column:40, length:11 assign to newTSTPrice11
  capture line:13, column:40, length:11 assign to newTSTPrice12
  capture line:14, column:40, length:11 assign to newTSTPrice13
  capture line:15, column:40, length:11 assign to newTSTPrice14
  capture line:16, column:40, length:11 assign to newTSTPrice15
  capture line:17, column:40, length:11 assign to newTSTPrice16
  capture line:18, column:40, length:11 assign to newTSTPrice17
  capture line:19, column:40, length:11 assign to newTSTPrice18
  capture line:20, column:40, length:11 assign to newTSTPrice19
  capture line:21, column:40, length:11 assign to newTSTPrice20
  capture line:22, column:40, length:11 assign to newTSTPrice21
  capture line:23, column:40, length:11 assign to newTSTPrice22

  capture line:2, column:35, length:3 assign to TSTcurr1
  capture line:3, column:35, length:3 assign to TSTcurr2
  capture line:4, column:35, length:3 assign to TSTcurr3
  capture line:5, column:35, length:3 assign to TSTcurr4
  capture line:6, column:35, length:3 assign to TSTcurr5
  capture line:7, column:35, length:3 assign to TSTcurr6
  capture line:8, column:35, length:3 assign to TSTcurr7
  capture line:9, column:35, length:3 assign to TSTcurr8
  capture line:10, column:35, length:3 assign to TSTcurr9
  capture line:11, column:35, length:3 assign to TSTcurr10
  capture line:12, column:35, length:3 assign to TSTcurr11
  capture line:13, column:35, length:3 assign to TSTcurr12
  capture line:14, column:35, length:3 assign to TSTcurr13
  capture line:15, column:35, length:3 assign to TSTcurr14
  capture line:16, column:35, length:3 assign to TSTcurr15
  capture line:17, column:35, length:3 assign to TSTcurr16
  capture line:18, column:35, length:3 assign to TSTcurr17
  capture line:19, column:35, length:3 assign to TSTcurr18
  capture line:20, column:35, length:3 assign to TSTcurr19
  capture line:21, column:35, length:3 assign to TSTcurr20
  capture line:22, column:35, length:3 assign to TSTcurr21
  capture line:23, column:35, length:3 assign to TSTcurr22

  capture line:23, column:1, length:48 assign to LastLine1

  capture line:24, column:1, length:2 assign to CheckMD
  if (CheckMD==")>"){
    send "MD"
    assign "TRUE" to moreTSTs
  }

  if (moreTSTs=="TRUE"){
    capture line:1, column:1, length:48 assign to checkRep1
    capture line:2, column:1, length:48 assign to checkRep2
    capture line:3, column:1, length:48 assign to checkRep3
    
  }
  
  
    
  capture line:4, column:1, length:1 assign to checkSec
  if (checkSec ==" "){
    assign "2" to TSTCount
  }
  else {
    capture line:5, column:1, length:1 assign to checkSec
    if (checkSec ==" "){
    assign "3" to TSTCount
    }
    else{
      capture line:6, column:1, length:1 assign to checkSec
      if (checkSec ==" "){
        assign "4" to TSTCount
      }
      else{
        capture line:7, column:1, length:1 assign to checkSec
        if (checkSec ==" "){
          assign "5" to TSTCount
        }
        else{
          capture line:8, column:1, length:1 assign to checkSec
          if (checkSec ==" "){
            assign "6" to TSTCount
          }
          else{
            capture line:9, column:1, length:1 assign to checkSec
            if (checkSec ==" "){
              assign "7" to TSTCount
            }
            else{
              capture line:10, column:1, length:1 assign to checkSec
              if (checkSec ==" "){
                assign "8" to TSTCount
              }
              else{
                capture line:11, column:1, length:1 assign to checkSec
                if (checkSec ==" "){
                  assign "9" to TSTCount
                }
                else{
                  capture line:12, column:1, length:1 assign to checkSec
                  if (checkSec ==" "){
                    assign "10" to TSTCount
                  }
                  else{
                    capture line:13, column:1, length:1 assign to checkSec
                    if (checkSec ==" "){
                      assign "11" to TSTCount
                    }
                    else{
                      capture line:14, column:1, length:1 assign to checkSec
                      if (checkSec ==" "){
                        assign "12" to TSTCount
                      }
                      else{
                        capture line:15, column:1, length:1 assign to checkSec
                        if (checkSec ==" "){
                          assign "13" to TSTCount
                        }
                        else{
                          capture line:16, column:1, length:1 assign to checkSec
                          if (checkSec ==" "){
                            assign "14" to TSTCount
                          }
                          else{
                            capture line:17, column:1, length:1 assign to checkSec
                            if (checkSec ==" "){
                              assign "15" to TSTCount
                            }
                            else{
                              capture line:18, column:1, length:1 assign to checkSec
                              if (checkSec ==" "){
                                assign "16" to TSTCount
                              }
                              else{
                                capture line:19, column:1, length:1 assign to checkSec
                                if (checkSec ==" "){
                                  assign "17" to TSTCount
                                }
                                else{
                                  capture line:20, column:1, length:1 assign to checkSec
                                  if (checkSec ==" "){
                                    assign "18" to TSTCount
                                  }
                                  else{
                                    ask "More Than 18 TSTs!" assign to qz5
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

  if (TSTCount=="0"){
    ask "There's no Active TST!" assign to qz5
  } 
  if (TSTCount=="1"){
    
  }

}
else{
  ask "There's no Active TST!" assign to qz5
}