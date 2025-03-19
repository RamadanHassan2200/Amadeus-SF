//z_Deal Checker

send "RTA"
capture line:2, column:4, length:2 assign to checkAirline
if (checkAirline == "  "){
     capture line:2, column:6, length:2 assign to Airline1
     capture line:2, column:32, length:1 assign to PassengerCount
}
else{
  capture line:3, column:6, length:2 assign to Airline1
  capture line:3, column:32, length:1 assign to PassengerCount
}

send "TTH"
capture line:2, column:35, length:3 assign to curr1

if(curr1=="EGP"){
     assign "0P" to airlinePercentage
if (Airline1 == "SM"){
    assign "3" to airlinePercentage
}
if (Airline1 == "MS"){
    assign "4" to airlinePercentage
}
if (Airline1 == "EK"){
    assign "3" to airlinePercentage
}
if (Airline1 == "QR"){
    assign "3" to airlinePercentage
}
if (Airline1 == "GF"){
    assign "7" to airlinePercentage
}
if (Airline1 == "KU"){
    assign "6" to airlinePercentage
}
if (Airline1 == "EY"){
    assign "2" to airlinePercentage
}
if (Airline1 == "WY"){
    assign "3" to airlinePercentage
}
if (Airline1 == "AT"){
    assign "5" to airlinePercentage
}
if (Airline1 == "BA"){
    assign "5" to airlinePercentage
}
if (Airline1 == "TU"){
    assign "3P" to airlinePercentage
}
if (Airline1 == "NE"){
    assign "2" to airlinePercentage
}
if (Airline1 == "NP"){
    assign "2" to airlinePercentage
}

send "FXR/K/R,UP/ZO-" +airlinePercentage +"P"
capture line:1, column:1, length:8 assign to checkAttn
if (checkAttn=="**ATTN**"){
    mandatory ask "There's unavailable class(es)!" assign to qz5
}

capture line:3, column:1, length:17 assign to checkError
if (checkError=="TICKET DESIGNATOR"){
send "FXR/K/R,UP"
capture line:6, column:20, length:6 assign to totals6
capture line:7, column:20, length:6 assign to totals7
capture line:8, column:20, length:6 assign to totals8
capture line:9, column:20, length:6 assign to totals9
capture line:10, column:20, length:6 assign to totals10
capture line:11, column:20, length:6 assign to totals11
capture line:12, column:20, length:6 assign to totals12
capture line:13, column:20, length:6 assign to totals13
capture line:14, column:20, length:6 assign to totals14
capture line:15, column:20, length:6 assign to totals15
capture line:16, column:20, length:6 assign to totals16

assign "0" to totalNewFare
assign "0" to totalNewPrice
if (totals6=="TOTALS"){
     capture line:6, column:32, length:10 assign to totalNewFare
     capture line:6, column:51, length:10 assign to totalNewPrice
}
if (totals7=="TOTALS"){
     capture line:7, column:32, length:10 assign to totalNewFare
     capture line:7, column:51, length:10 assign to totalNewPrice
}
if (totals8=="TOTALS"){
     capture line:8, column:32, length:10 assign to totalNewFare
     capture line:8, column:51, length:10 assign to totalNewPrice
}
if (totals9=="TOTALS"){
     capture line:9, column:32, length:10 assign to totalNewFare
     capture line:9, column:51, length:10 assign to totalNewPrice     
}
if (totals10=="TOTALS"){
     capture line:10, column:32, length:10 assign to totalNewFare
     capture line:10, column:51, length:10 assign to totalNewPrice
}
if (totals11=="TOTALS"){
     capture line:11, column:32, length:10 assign to totalNewFare
     capture line:11, column:51, length:10 assign to totalNewPrice
}
if (totals12=="TOTALS"){
     capture line:12, column:32, length:10 assign to totalNewFare
     capture line:12, column:51, length:10 assign to totalNewPrice
}
if (totals13=="TOTALS"){
     capture line:13, column:32, length:10 assign to totalNewFare
     capture line:13, column:51, length:10 assign to totalNewPrice
}
if (totals14=="TOTALS"){
     capture line:14, column:32, length:10 assign to totalNewFare
     capture line:14, column:51, length:10 assign to totalNewPrice
}
if (totals15=="TOTALS"){
     capture line:15, column:32, length:10 assign to totalNewFare
     capture line:15, column:51, length:10 assign to totalNewPrice
}
if (totals16=="TOTALS"){
     capture line:16, column:32, length:10 assign to totalNewFare
     capture line:16, column:51, length:10 assign to totalNewPrice
}
     
     if (totalNewPrice=="0"){
          capture line:6, column:1, length:3 assign to checknewCurr6
          capture line:7, column:1, length:3 assign to checknewCurr7
          capture line:8, column:1, length:3 assign to checknewCurr8
          capture line:9, column:1, length:3 assign to checknewCurr9
          capture line:10, column:1, length:3 assign to checknewCurr10
          capture line:11, column:1, length:3 assign to checknewCurr11
          capture line:12, column:1, length:3 assign to checknewCurr12
          capture line:13, column:1, length:3 assign to checknewCurr13
          capture line:14, column:1, length:3 assign to checknewCurr14
          capture line:15, column:1, length:3 assign to checknewCurr15
          capture line:16, column:1, length:3 assign to checknewCurr16
          capture line:17, column:1, length:3 assign to checknewCurr17
          capture line:18, column:1, length:3 assign to checknewCurr18
          capture line:19, column:1, length:3 assign to checknewCurr19
          capture line:20, column:1, length:3 assign to checknewCurr20
          capture line:21, column:1, length:3 assign to checknewCurr21
          capture line:22, column:1, length:3 assign to checknewCurr22
          capture line:23, column:1, length:3 assign to checknewCurr23
          
          if (checknewCurr6 == "EGP"){
                if (totalNewFare =="0"){
                    capture line:6, column:4, length:10 assign to totalNewFare
                }
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == "EGP"){
            if (totalNewFare =="0"){
                capture line:7, column:4, length:10 assign to totalNewFare
            }
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == "EGP"){
            if (totalNewFare =="0"){
                capture line:8, column:4, length:10 assign to totalNewFare
            }
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == "EGP"){
            if (totalNewFare =="0"){
                capture line:9, column:4, length:10 assign to totalNewFare
            }
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == "EGP"){
            if (totalNewFare =="0"){
                capture line:10, column:4, length:10 assign to totalNewFare
            }
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == "EGP"){
            if (totalNewFare =="0"){
                capture line:11, column:4, length:10 assign to totalNewFare
            }
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == "EGP"){
            if (totalNewFare =="0"){
                capture line:12, column:4, length:10 assign to totalNewFare
            }
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == "EGP"){
            if (totalNewFare =="0"){
                capture line:13, column:4, length:10 assign to totalNewFare
            }
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == "EGP"){
            if (totalNewFare =="0"){
                capture line:14, column:4, length:10 assign to totalNewFare
            }
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == "EGP"){
            if (totalNewFare =="0"){
                capture line:15, column:4, length:10 assign to totalNewFare
            }
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == "EGP"){
            if (totalNewFare =="0"){
                capture line:16, column:4, length:10 assign to totalNewFare
            }
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == "EGP"){
            if (totalNewFare =="0"){
                capture line:17, column:4, length:10 assign to totalNewFare
            }
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == "EGP"){
            if (totalNewFare =="0"){
                capture line:18, column:4, length:10 assign to totalNewFare
            }
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == "EGP"){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == "EGP"){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == "EGP"){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == "EGP"){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == "EGP"){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }
     
     // check if lower class exists:
     send "Fqq1"
  capture line:9, column:17, length:1 assign to firstSeg
  capture line:10, column:17, length:1 assign to secondSeg
  capture line:11, column:17, length:1 assign to thirdSeg
  capture line:12, column:17, length:1 assign to fourthSeg
  capture line:13, column:17, length:1 assign to fifthSeg
  capture line:14, column:17, length:1 assign to sixthSeg
  capture line:15, column:17, length:1 assign to seventhSeg
  capture line:16, column:17, length:1 assign to eighthSeg

  if (firstSeg == "*"){
    send "Star!"
  }
  if (secondSeg == "*"){
    send "Star!"
  }
  if (thirdSeg == "*"){
    send "Star!"
  }
  if (fourthSeg == "*"){
    send "Star!"
  }
  if (fifthSeg == "*"){
    send "Star!"
  }
  if (sixthSeg == "*"){
    send "Star!"
  }
  if (seventhSeg == "*"){
    send "Star!"
  }
  if (eighthSeg == "*"){
    send "Star!"
  }

     send "DF" + totalNewFare + "*0.0" +airlinePercentage
     capture line:2, column:1, length:10 assign to NewFarePercentage
     send "DF" + totalNewPrice +"-" +NewFarePercentage
     capture line:2, column:1, length:10 assign to totalNewPrice

}
else{
capture line:6, column:20, length:6 assign to totals6
capture line:7, column:20, length:6 assign to totals7
capture line:8, column:20, length:6 assign to totals8
capture line:9, column:20, length:6 assign to totals9
capture line:10, column:20, length:6 assign to totals10
capture line:11, column:20, length:6 assign to totals11
capture line:12, column:20, length:6 assign to totals12
capture line:13, column:20, length:6 assign to totals13
capture line:14, column:20, length:6 assign to totals14
capture line:15, column:20, length:6 assign to totals15
capture line:16, column:20, length:6 assign to totals16

assign "0" to totalNewPrice
if (totals6=="TOTALS"){
     capture line:6, column:51, length:10 assign to totalNewPrice
}
if (totals7=="TOTALS"){
     capture line:7, column:51, length:10 assign to totalNewPrice
}
if (totals8=="TOTALS"){
     capture line:8, column:51, length:10 assign to totalNewPrice
}
if (totals9=="TOTALS"){
     capture line:9, column:51, length:10 assign to totalNewPrice     
}
if (totals10=="TOTALS"){
     capture line:10, column:51, length:10 assign to totalNewPrice
}
if (totals11=="TOTALS"){
     capture line:11, column:51, length:10 assign to totalNewPrice
}
if (totals12=="TOTALS"){
     capture line:12, column:51, length:10 assign to totalNewPrice
}
if (totals13=="TOTALS"){
     capture line:13, column:51, length:10 assign to totalNewPrice
}
if (totals14=="TOTALS"){
     capture line:14, column:51, length:10 assign to totalNewPrice
}
if (totals15=="TOTALS"){
     capture line:15, column:51, length:10 assign to totalNewPrice
}
if (totals16=="TOTALS"){
     capture line:16, column:51, length:10 assign to totalNewPrice
}
     
     if (totalNewPrice=="0"){
          capture line:6, column:1, length:3 assign to checknewCurr6
          capture line:7, column:1, length:3 assign to checknewCurr7
          capture line:8, column:1, length:3 assign to checknewCurr8
          capture line:9, column:1, length:3 assign to checknewCurr9
          capture line:10, column:1, length:3 assign to checknewCurr10
          capture line:11, column:1, length:3 assign to checknewCurr11
          capture line:12, column:1, length:3 assign to checknewCurr12
          capture line:13, column:1, length:3 assign to checknewCurr13
          capture line:14, column:1, length:3 assign to checknewCurr14
          capture line:15, column:1, length:3 assign to checknewCurr15
          capture line:16, column:1, length:3 assign to checknewCurr16
          capture line:17, column:1, length:3 assign to checknewCurr17
          capture line:18, column:1, length:3 assign to checknewCurr18
          capture line:19, column:1, length:3 assign to checknewCurr19
          capture line:20, column:1, length:3 assign to checknewCurr20
          capture line:21, column:1, length:3 assign to checknewCurr21
          capture line:22, column:1, length:3 assign to checknewCurr22
          capture line:23, column:1, length:3 assign to checknewCurr23

          if (checknewCurr6 == "EGP"){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == "EGP"){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == "EGP"){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == "EGP"){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == "EGP"){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == "EGP"){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == "EGP"){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == "EGP"){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == "EGP"){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == "EGP"){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == "EGP"){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == "EGP"){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == "EGP"){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == "EGP"){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == "EGP"){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == "EGP"){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == "EGP"){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == "EGP"){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }
     send "Fqq1"
  capture line:9, column:17, length:1 assign to firstSeg
  capture line:10, column:17, length:1 assign to secondSeg
  capture line:11, column:17, length:1 assign to thirdSeg
  capture line:12, column:17, length:1 assign to fourthSeg
  capture line:13, column:17, length:1 assign to fifthSeg
  capture line:14, column:17, length:1 assign to sixthSeg
  capture line:15, column:17, length:1 assign to seventhSeg
  capture line:16, column:17, length:1 assign to eighthSeg

  if (firstSeg == "*"){
    send "Star!"
  }
  if (secondSeg == "*"){
    send "Star!"
  }
  if (thirdSeg == "*"){
    send "Star!"
  }
  if (fourthSeg == "*"){
    send "Star!"
  }
  if (fifthSeg == "*"){
    send "Star!"
  }
  if (sixthSeg == "*"){
    send "Star!"
  }
  if (seventhSeg == "*"){
    send "Star!"
  }
  if (eighthSeg == "*"){
    send "Star!"
  }
}
}

if (curr1 == "PKR"){
     assign "0.033" to airlinePKPercentage

if (Airline1 == "GF"){
    assign "0.035" to airlinePKPercentage
}
if (Airline1 == "WY"){
    assign "0.035" to airlinePKPercentage
}
if (Airline1 == "UL"){
    assign "0.035" to airlinePKPercentage
}
if (Airline1 == "FZ"){
    assign "0.03" to airlinePKPercentage
}
if (Airline1 == "EY"){
    assign "0.03" to airlinePKPercentage
}
if (Airline1 == "EK"){
    assign "0.025" to airlinePKPercentage
}
if (Airline1 == "QR"){
    assign "0.025" to airlinePKPercentage
}
if (Airline1 == "TK"){
    assign "0.04" to airlinePKPercentage
}
if (Airline1 == "TG"){
    assign "0.03" to airlinePKPercentage
}
if (Airline1 == "UL"){
    assign "0.04" to airlinePKPercentage
}
if (Airline1 == "OD"){
    assign "0.04" to airlinePKPercentage
}
if (Airline1 == "SQ"){
    assign "0.025" to airlinePKPercentage
}
if (Airline1 == "PR"){
    assign "0.025" to airlinePKPercentage
}
if (Airline1 == "ET"){
    assign "0.025" to airlinePKPercentage
}
if (Airline1 == "CA"){
    assign "0.03" to airlinePKPercentage
}
}

send "TTH"
capture line:1, column:1, length:1 assign to newTSTs
if (newTSTs=="T"){
  capture line:2, column:35, length:3 assign to curr1
  capture line:2, column:41, length:10 assign to firstTST
  capture line:5, column:1, length:1 assign to checkSec2
  if (checkSec2 =="D"){
        assign "2" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
    }
  capture line:6, column:1, length:1 assign to checkSec3
  if (checkSec3 =="D"){
        assign "3" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
    }
  capture line:7, column:1, length:1 assign to checkSec4
  if (checkSec4 =="D"){
        assign "4" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
  }
  capture line:8, column:1, length:1 assign to checkSec5
  if (checkSec5 =="D"){
        assign "5" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
  }
  capture line:9, column:1, length:1 assign to checkSec6
  if (checkSec6 =="D"){
        assign "6" to TSTCount
       capture line:3, column:41, length:10 assign to secondTST
       capture line:4, column:41, length:10 assign to thirdTST 
       capture line:5, column:41, length:10 assign to fourthTST
       capture line:6, column:41, length:10 assign to fifthTST
       capture line:7, column:41, length:10 assign to sixthTST
  }
}
if (TSTCount=="6"){
       capture line:10, column:35, length:3 assign to curr2
       capture line:10, column:40, length:10 assign to TST1
       capture line:11, column:40, length:10 assign to TST2
       capture line:12, column:40, length:10 assign to TST3
       capture line:13, column:40, length:10 assign to TST4
       capture line:14, column:40, length:10 assign to TST5
       capture line:15, column:40, length:10 assign to TST6
       if(curr1=="EGP"){
          send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +";" +TST6 +"-" +curr2deal     
       }
       if(curr1=="PKR"){
          send "DF" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST +";" +fifthTST +";" +sixthTST
          capture line:3, column:1, length:1 assign to checkDFnextLine
          if (checkDFnextLine == ">"){
               capture line:2, column:1, length:10 assign to totalNewPrice
          }
          else{
               capture line:4, column:1, length:1 assign to checkDFnextLine
               if (checkDFnextLine == ">"){
                    capture line:3, column:1, length:10 assign to totalNewPrice
               }
          }
          send "FQC" + totalNewPrice + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +";" +TST6 +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST +";" +TST6 +"-" +sixthTST 
          }
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
          send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +"-" +curr2deal 
         }
         if(curr1=="PKR"){
          send "DF" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST +";" +fifthTST 
          capture line:3, column:1, length:1 assign to checkDFnextLine
          if (checkDFnextLine == ">"){
               capture line:2, column:1, length:10 assign to totalNewPrice
          }
          else{
               capture line:4, column:1, length:1 assign to checkDFnextLine
               if (checkDFnextLine == ">"){
                    capture line:3, column:1, length:10 assign to totalNewPrice
               }
          }
          send "FQC" + totalNewPrice + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +";" +TST5 +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST +";" +TST5 +"-" +fifthTST 
          }
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
     send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +"-" +curr2deal  
  }
  if(curr1=="PKR"){
          send "DF" +firstTST +";" +secondTST +";" +thirdTST +";" +fourthTST 
          capture line:3, column:1, length:1 assign to checkDFnextLine
          if (checkDFnextLine == ">"){
               capture line:2, column:1, length:10 assign to totalNewPrice
          }
          else{
               capture line:4, column:1, length:1 assign to checkDFnextLine
               if (checkDFnextLine == ">"){
                    capture line:3, column:1, length:10 assign to totalNewPrice
               }
          }
          send "FQC" + totalNewPrice + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3 +";" +TST4 +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST +";" +TST4 +"-" +fourthTST 
          }
       }
}
else{
if (TSTCount=="3"){
       capture line:7, column:35, length:3 assign to curr2
       capture line:7, column:40, length:10 assign to TST1
       capture line:8, column:40, length:10 assign to TST2
       capture line:9, column:40, length:10 assign to TST3

if(curr1=="EGP"){
     send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +";" +TST2 +";" +TST3 +"-" +curr2deal 
  }
  if(curr1=="PKR"){
          send "DF" +firstTST +";" +secondTST +";" +thirdTST 
          capture line:3, column:1, length:1 assign to checkDFnextLine
          if (checkDFnextLine == ">"){
               capture line:2, column:1, length:10 assign to totalNewPrice
          }
          else{
               capture line:4, column:1, length:1 assign to checkDFnextLine
               if (checkDFnextLine == ">"){
                    capture line:3, column:1, length:10 assign to totalNewPrice
               }
          }
          send "FQC" + totalNewPrice + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2 +";" +TST3  +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST +";" +TST3 +"-" +thirdTST 
          }
       }
}
else{
if (TSTCount=="2"){
       capture line:6, column:35, length:3 assign to curr2
       capture line:6, column:40, length:10 assign to TST1
       capture line:7, column:40, length:10 assign to TST2

if(curr1=="EGP"){
     send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +";" +TST2 +"-" +curr2deal 
  }
  if(curr1=="PKR"){
          send "DF" +firstTST +";" +secondTST 
          capture line:2, column:1, length:10 assign to totalNewPrice
          send "FQC" + totalNewPrice + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +";" +TST2  +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST +";" +TST2 +"-" +secondTST 
          }
       }
}
else{
if (firstTST<="9999999"){
       capture line:5, column:35, length:3 assign to curr2
       capture line:5, column:40, length:10 assign to TST1
if(curr1=="EGP"){
    send "FQC" +totalNewPrice +"EGP/AED"
          capture line:4, column:4, length:5 assign to AEDdeal
          send "FQC" +AEDdeal +"AED/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }

          send "df" +TST1 +"-" +curr2deal 
  }
  if(curr1=="PKR"){
          send "FQC" + firstTST + "PKR/" +curr2
          if (curr2=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +TST1 +"-" +curr2deal + ";" +curr2deal +"*" +airlinePKPercentage
       }
       if (curr1!="PKR"){
          if (curr1!="EGP"){
               send "df" +TST1 +"-" +firstTST 
          }
       }
}

}//1
}//2
}//3
}//4
}//5