// for Cairo Office

//retrirval
mandatory ask "Enter the PNR: " assign to pnr
send "IG"
send "rt" +pnr

// Checking Airline(s) and Travel date and passenger count
send "RTA"

capture line:2, column:30, length:2 assign to HK1Test
if (HK1Test=="HK"){
  assign "1" to segmentsCount
  capture line:2, column:6, length:2 assign to Airline1
  capture line:2, column:15, length:5 assign to TravelDate
  capture line:2, column:23, length:3 assign to OriginCity
  capture line:2, column:32, length:1 assign to PassengerCount
  capture line:3, column:30, length:2 assign to HKnextTest
  if (HKnextTest=="HK"){
    assign "2" to segmentsCount
    capture line:4, column:30, length:2 assign to HK3Test
    if (HK3Test=="HK"){
      assign "3" to segmentsCount
      capture line:5, column:30, length:2 assign to HK4Test
      if (HK4Test=="HK"){
          assign "4" to segmentsCount
          capture line:6, column:30, length:2 assign to HK5Test
          if (HK5Test=="HK"){
            assign "5" to segmentsCount
            capture line:7, column:30, length:2 assign to HK6Test
            if (HK6Test=="HK"){
                assign "6" to segmentsCount
                capture line:8, column:30, length:2 assign to HK7Test
                if (HK7Test=="HK"){
                    send "SmartFlow now working on more than 6 segments"
                    ask "ignore?" assign to qz5
                    send "ig"
                    call "test1"
                }
            }
          }
      }
    }
  }

}
else{
capture line:3, column:30, length:2 assign to HK2Test
if (HK2Test=="HK"){
  assign "1" to segmentsCount
  capture line:3, column:6, length:2 assign to Airline1
  capture line:3, column:15, length:5 assign to TravelDate
  capture line:3, column:23, length:3 assign to OriginCity
  capture line:3, column:32, length:1 assign to PassengerCount
  capture line:4, column:30, length:2 assign to HKnextTest
      if (HKnextTest=="HK"){
        assign "2" to segmentsCount
        capture line:5, column:30, length:2 assign to HK3Test
        if (HK3Test=="HK"){
          assign "3" to segmentsCount
          capture line:6, column:30, length:2 assign to HK4Test
          if (HK4Test=="HK"){
              assign "4" to segmentsCount
              capture line:7, column:30, length:2 assign to HK5Test
              if (HK5Test=="HK"){
                assign "5" to segmentsCount
                capture line:8, column:30, length:2 assign to HK6Test
                if (HK6Test=="HK"){
                    assign "6" to segmentsCount
                    capture line:9, column:30, length:2 assign to HK7Test
                    if (HK7Test=="HK"){
                        send "SmartFlow now working on more than 6 segments"
                        ask "ignore?" assign to qz5
                        send "ig"
                        call "test1"
                    }
                }
              }
          }
        }
      }
}
else{
  send "Not Confirmed Segments please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
}
}

// ignore >4 segments or >6 passengers

// Checking the Airline

// Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
  if (Airline1=="A3") {
    send "A3 airline is non-voidable for (P,U,T,S) Classes"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="ER"){
    send "ER airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="H1"){
    send "H1 airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="NP"){
    send "NP airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="R5"){
    send "R5 airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="UK"){
    send "UK airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="NE"){
    send "NE airline is non-voidable (EX-EGY)"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="SV"){
    send "SV airline is non-voidable (EX-EGY)"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="XQ"){
    send "XQ airline is non-voidable (EX-EGY)"
    ask "Stop and Review" assign to qz5
    send "ig"
  }

if (OriginCity=="ASW"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="ATZ"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="CAI"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="DBB"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="HBE"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="HMB"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="HRG"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="LXR"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="RMF"){
  assign "TRUE" to EXEGYCheck
}
if (OriginCity=="SSH"){
  assign "TRUE" to EXEGYCheck
}

if (EXEGYCheck != "TRUE"){
    send "THIS's NOT EX EGY DEAL!"
    mandatory ask "PLease check the departure city again!" assign to qz5
}

  //Today dates aren't considered
  if (TravelDate == today){
    send  "No void for today flights"
    ask "Check again please!" assign to qz
    send "ig"
  }
// Checking Airline(s) and Travel date and passenger count//

      send "tqm"
         capture line:1, column:1, length:20 assign to emdTest

        if (emdTest != "NO TSM RECORD EXISTS"){
          send "EMD! Please stop and check."
          mandatory ask "Ignore!" assign to qz5 
          send "ig"
        }
            
//confirming there's no EMD
    send "rttn"

        capture line:2, column:5, length:2 assign to FA1
          if (FA1=="FA"){
            assign "1" to FACount
            capture line:2, column:8, length:3 assign to PAXtest
            if (PAXtest=="PAX"){
            capture line:2, column:12, length:14 assign to TnFA1
            }
          }
          capture line:3, column:5, length:2 assign to FA2
          if (FA2=="FA"){
              if (FACount=="1"){
                  assign "2" to FACount
              }
              else {
                  assign "1" to FACount
              }
              capture line:3, column:8, length:3 assign to PAXtest    
              if (PAXtest=="PAX"){
                capture line:3, column:12, length:14 assign to TnFA1
              }
          }
          capture line:4, column:5, length:2 assign to FA3
          if (FA3=="FA"){
              if (FACount=="2"){
                  assign "3" to FACount
              }
              else{
                  assign "2" to FACount
              }
              capture line:4, column:8, length:3 assign to PAXtest
              if (PAXtest=="PAX"){
                capture line:4, column:12, length:14 assign to TnFA1
              }
          }
          capture line:5, column:5, length:2 assign to FA4
          if (FA4=="FA"){
                if (FACount=="3"){
                  assign "4" to FACount
                }
                else{
                  assign "3" to FACount
                }
                capture line:5, column:8, length:3 assign to PAXtest
                if (PAXtest=="PAX"){
                  capture line:5, column:12, length:14 assign to TnFA1
                }
          }
          capture line:6, column:5, length:2 assign to FA5
          if (FA5=="FA"){
                if (FACount=="4"){
                  assign "5" to FACount
                }
                else{
                  assign "4" to FACount
                }
                capture line:6, column:8, length:3 assign to PAXtest
                if (PAXtest=="PAX"){
                    capture line:6, column:12, length:14 assign to TnFA1
                }
          }
          capture line:7, column:5, length:2 assign to FA6
          if (FA6=="FA"){
                if (FACount=="5"){
                  assign "6" to FACount
                }
                else{
                  assign "5" to FACount
                }
                capture line:7, column:8, length:3 assign to PAXtest
                if (PAXtest=="PAX"){
                    capture line:7, column:12, length:14 assign to TnFA1
                }
          }
          capture line:8, column:5, length:2 assign to FA7
          if (FA7=="FA"){
                if (FACount=="6"){
                  assign "7" to FACount
                }
                else{
                  assign "6" to FACount
                }
                capture line:8, column:8, length:3 assign to PAXtest
                if (PAXtest=="PAX"){
                    capture line:8, column:12, length:14 assign to TnFA1
                }
          }
          capture line:9, column:5, length:2 assign to FA8
          if (FA8=="FA"){
                if (FACount=="7"){
                    assign "8" to FACount
                }
                else{
                  assign "7" to FACount
                }
                capture line:9, column:8, length:3 assign to PAXtest
                if (PAXtest=="PAX"){
                    capture line:9, column:12, length:14 assign to TnFA1
                }
          }
          capture line:10, column:5, length:2 assign to FA9
          if (FA9=="FA"){
              if (FACount=="8"){
                  assign "9" to FACount
              }
              else{
                assign "8" to FACount
              }
              capture line:10, column:8, length:3 assign to PAXtest
              if (PAXtest=="PAX"){
                 capture line:10, column:12, length:14 assign to TnFA1
              }
          }
          capture line:11, column:5, length:2 assign to FA10
          if (FA10=="FA"){
              if (FACount=="9"){
                  send "More than 9 FA"
                  mandatory ask "Please continue manually as there're more than 9 FA(s)" assign to qz5
                  send "ig"
              }
              else{
                  assign "9" to FACount
              }
              capture line:11, column:8, length:3 assign to PAXtest
              if (PAXtest=="PAX"){
                 capture line:11, column:12, length:14 assign to TnFA1
              }
          }
    //if (PassengerCount!=FACount){
      //  send "FA missing or they're separate, please continue manually"
        //ask "Continue?" assign to qz5
    //}
send "TWD/TKT" +TnFA1

capture line:1, column:1, length:22 assign to checkticketopenness
if (checkticketopenness=="SECURED ETKT RECORD(S)"){
  send "tqt/t500"
  capture line:2, column:1, length:3 assign to TQTNumber1
  capture line:2, column:42, length:10 assign to TQTPrice1
  capture line:3, column:1, length:3 assign to TQTNumber2
  capture line:3, column:42, length:10 assign to TQTPrice2
  capture line:4, column:1, length:3 assign to TQTNumber3
  capture line:4, column:42, length:10 assign to TQTPrice3
  capture line:5, column:1, length:3 assign to TQTNumber4
  capture line:5, column:42, length:10 assign to TQTPrice4
  capture line:6, column:1, length:3 assign to TQTNumber5
  capture line:6, column:42, length:10 assign to TQTPrice5
  capture line:7, column:1, length:3 assign to TQTNumber6
  capture line:7, column:42, length:10 assign to TQTPrice6
  capture line:8, column:1, length:3 assign to TQTNumber7
  capture line:8, column:42, length:10 assign to TQTPrice7
  capture line:9, column:1, length:3 assign to TQTNumber8
  capture line:9, column:42, length:10 assign to TQTPrice8
  capture line:10, column:1, length:3 assign to TQTNumber9
  capture line:10, column:42, length:10 assign to TQTPrice9
  capture line:11, column:1, length:3 assign to TQTNumber10
  capture line:11, column:42, length:10 assign to TQTPrice10
  capture line:12, column:1, length:3 assign to TQTNumber11
  capture line:12, column:42, length:10 assign to TQTPrice11
  capture line:13, column:1, length:3 assign to TQTNumber12
  capture line:13, column:42, length:10 assign to TQTPrice12
  capture line:14, column:1, length:3 assign to TQTNumber13
  capture line:14, column:42, length:10 assign to TQTPrice13
  capture line:15, column:1, length:3 assign to TQTNumber14
  capture line:15, column:42, length:10 assign to TQTPrice14
  capture line:16, column:1, length:3 assign to TQTNumber15
  capture line:16, column:42, length:10 assign to TQTPrice15
  capture line:17, column:1, length:3 assign to TQTNumber16
  capture line:17, column:42, length:10 assign to TQTPrice16
  capture line:18, column:1, length:3 assign to TQTNumber17
  capture line:18, column:42, length:10 assign to TQTPrice17
  capture line:19, column:1, length:3 assign to TQTNumber18
  capture line:19, column:42, length:10 assign to TQTPrice18

  assign "0" to heighestTST
  if (TQTNumber1=="DEL"){
    assign "0" to TQTNumber1
  } 
  if (TQTNumber1==""){
    assign "0" to TQTNumber1
  }
  if (TQTNumber2=="DEL"){
    assign "0" to TQTNumber2
  } 
  if (TQTNumber2==""){
    assign "0" to TQTNumber2
  }
  if (TQTNumber3=="DEL"){
    assign "0" to TQTNumber3
  } 
  if (TQTNumber3==""){
    assign "0" to TQTNumber3
  }
  if (TQTNumber4=="DEL"){
    assign "0" to TQTNumber4
  } 
  if (TQTNumber4==""){
    assign "0" to TQTNumber4
  }
  if (TQTNumber5=="DEL"){
    assign "0" to TQTNumber5
  } 
  if (TQTNumber5==""){
    assign "0" to TQTNumber5
  }
  if (TQTNumber6=="DEL"){
    assign "0" to TQTNumber6
  } 
  if (TQTNumber6==""){
    assign "0" to TQTNumber6
  }
  if (TQTNumber7=="DEL"){
    assign "0" to TQTNumber7
  } 
  if (TQTNumber7==""){
    assign "0" to TQTNumber7
  }
  if (TQTNumber8=="DEL"){
    assign "0" to TQTNumber8
  } 
  if (TQTNumber8==""){
    assign "0" to TQTNumber8
  }
  if (TQTNumber9=="DEL"){
    assign "0" to TQTNumber9
  } 
  if (TQTNumber9==""){
    assign "0" to TQTNumber9
  }
  if (TQTNumber10=="DEL"){
    assign "0" to TQTNumber10
  } 
  if (TQTNumber10==""){
    assign "0" to TQTNumber10
  }
  if (TQTNumber11=="DEL"){
    assign "0" to TQTNumber11
  } 
  if (TQTNumber11==""){
    assign "0" to TQTNumber11
  }
  if (TQTNumber12=="DEL"){
    assign "0" to TQTNumber12
  } 
  if (TQTNumber12==""){
    assign "0" to TQTNumber12
  }
  if (TQTNumber13=="DEL"){
    assign "0" to TQTNumber13
  } 
  if (TQTNumber13==""){
    assign "0" to TQTNumber13
  }
  if (TQTNumber14=="DEL"){
    assign "0" to TQTNumber14
  } 
  if (TQTNumber14==""){
    assign "0" to TQTNumber14
  }
  if (TQTNumber15=="DEL"){
    assign "0" to TQTNumber15
  } 
  if (TQTNumber15==""){
    assign "0" to TQTNumber15
  }
  if (TQTNumber16=="DEL"){
    assign "0" to TQTNumber16
  } 
  if (TQTNumber16==""){
    assign "0" to TQTNumber16
  }
  if (TQTNumber17=="DEL"){
    assign "0" to TQTNumber17
  } 
  if (TQTNumber17==""){
    assign "0" to TQTNumber17
  }
  if (TQTNumber18=="DEL"){
    assign "0" to TQTNumber18
  } 
  if (TQTNumber18==""){
    assign "0" to TQTNumber18
  }

  if (TQTPrice1 =="E TTH     "){
      assign "0" to TQTPrice1
  }
  if (TQTPrice2 =="E TTH     "){
      assign "0" to TQTPrice2
  }
  if (TQTPrice3 =="E TTH     "){
      assign "0" to TQTPrice3
  }
  if (TQTPrice4 =="E TTH     "){
      assign "0" to TQTPrice4
  }
  if (TQTPrice5 =="E TTH     "){
      assign "0" to TQTPrice5
  }
  if (TQTPrice6 =="E TTH     "){
      assign "0" to TQTPrice6
  }
  if (TQTPrice7 =="E TTH     "){
      assign "0" to TQTPrice7
  }
  if (TQTPrice8 =="E TTH     "){
      assign "0" to TQTPrice8
  }
  if (TQTPrice9 =="E TTH     "){
      assign "0" to TQTPrice9
  }
  if (TQTPrice10 =="E TTH     "){
      assign "0" to TQTPrice10
  }
  if (TQTPrice11 =="E TTH     "){
      assign "0" to TQTPrice11
  }
  if (TQTPrice12 =="E TTH     "){
      assign "0" to TQTPrice12
  }
  if (TQTPrice13 =="E TTH     "){
      assign "0" to TQTPrice13
  }
  if (TQTPrice14 =="E TTH     "){
      assign "0" to TQTPrice14
  }
  if (TQTPrice15 =="E TTH     "){
      assign "0" to TQTPrice15
  }
  if (TQTPrice16 =="E TTH     "){
      assign "0" to TQTPrice16
  }
  if (TQTPrice17 =="E TTH     "){
      assign "0" to TQTPrice17
  }
  if (TQTPrice18 =="E TTH     "){
      assign "0" to TQTPrice18
  }

  assign "0" to heighestPrice
        
  if (TQTNumber1!="0"){
    if (TQTPrice1>heighestPrice){
      assign TQTNumber1 to heighestTST
      assign TQTPrice1 to heighestPrice
    }
  }
  if (TQTNumber2!="0"){
    if (TQTPrice2>heighestPrice){
      assign TQTNumber2 to heighestTST
      assign TQTPrice2 to heighestPrice
    }
  }
  if (TQTNumber3!="0"){
    if (TQTPrice3>heighestPrice){
      assign TQTNumber3 to heighestTST
      assign TQTPrice3 to heighestPrice
    }
  }
  if (TQTNumber4!="0"){
    if (TQTPrice4>heighestPrice){
      assign TQTNumber4 to heighestTST
      assign TQTPrice4 to heighestPrice
    }
  }
  if (TQTNumber5!="0"){
    if (TQTPrice5>heighestPrice){
      assign TQTNumber5 to heighestTST
      assign TQTPrice5 to heighestPrice
    }
  }
  if (TQTNumber6!="0"){
    if (TQTPrice6>heighestPrice){
      assign TQTNumber6 to heighestTST
      assign TQTPrice6 to heighestPrice
    }
  }
  if (TQTNumber7!="0"){
    if (TQTPrice7>heighestPrice){
      assign TQTNumber7 to heighestTST
      assign TQTPrice7 to heighestPrice
    }
  }
  if (TQTNumber8!="0"){
    if (TQTPrice8>heighestPrice){
      assign TQTNumber8 to heighestTST
      assign TQTPrice8 to heighestPrice
    }
  }
  if (TQTNumber9!="0"){
    if (TQTPrice9>heighestPrice){
      assign TQTNumber9 to heighestTST
      assign TQTPrice9 to heighestPrice
    }
  }
  if (TQTNumber10!="0"){
    if (TQTPrice10>heighestPrice){
      assign TQTNumber10 to heighestTST
      assign TQTPrice10 to heighestPrice
    }
  }
  if (TQTNumber11!="0"){
    if (TQTPrice11>heighestPrice){
      assign TQTNumber11 to heighestTST
      assign TQTPrice11 to heighestPrice
    }
  }
  if (TQTNumber12!="0"){
    if (TQTPrice12>heighestPrice){
      assign TQTNumber12 to heighestTST
      assign TQTPrice12 to heighestPrice
    }
  }
  if (TQTNumber13!="0"){
    if (TQTPrice13>heighestPrice){
      assign TQTNumber13 to heighestTST
      assign TQTPrice13 to heighestPrice
    }
  }
  if (TQTNumber14!="0"){
    if (TQTPrice14>heighestPrice){
      assign TQTNumber14 to heighestTST
      assign TQTPrice14 to heighestPrice
    }
  }
  if (TQTNumber15!="0"){
    if (TQTPrice15>heighestPrice){
      assign TQTNumber15 to heighestTST
      assign TQTPrice15 to heighestPrice
    }
  }
  if (TQTNumber16!="0"){
    if (TQTPrice16>heighestPrice){
      assign TQTNumber16 to heighestTST
      assign TQTPrice16 to heighestPrice
    }
  }
  if (TQTNumber17!="0"){
    if (TQTPrice17>heighestPrice){
      assign TQTNumber17 to heighestTST
      assign TQTPrice17 to heighestPrice
    }
  }
  if (TQTNumber18!="0"){
    if (TQTPrice18>heighestPrice){
      assign TQTNumber18 to heighestTST
      assign TQTPrice18 to heighestPrice
    }
  }

  send "TQT/T" +heighestTST

  capture line:5, column:32, length:2 assign to TQTOK1
  capture line:6, column:32, length:2 assign to TQTOK2
  capture line:7, column:32, length:2 assign to TQTOK3
  capture line:8, column:32, length:2 assign to TQTOK4
  capture line:9, column:32, length:2 assign to TQTOK5
  capture line:10, column:32, length:2 assign to TQTOK6
  capture line:11, column:32, length:2 assign to TQTOK7
  capture line:12, column:32, length:2 assign to TQTOK8
  capture line:13, column:32, length:2 assign to TQTOK9
  capture line:14, column:32, length:2 assign to TQTOK10
  capture line:15, column:32, length:2 assign to TQTOK11
  capture line:16, column:32, length:2 assign to TQTOK12
  capture line:17, column:32, length:2 assign to TQTOK13
  capture line:18, column:32, length:2 assign to TQTOK14
  capture line:19, column:32, length:2 assign to TQTOK15

  assign "0" to TQTSegmentNo
  if (TQTOK1=="OK"){
    capture line:5, column:62, length:2 assign to Bg1
    assign "1" to TQTSegmentNo
  }
  if (TQTOK2=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:6, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:6, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
  }
  if (TQTOK3=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:7, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:7, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:7, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
  }
  if (TQTOK4=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:8, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:8, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:8, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:8, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
  }
  if (TQTOK5=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:9, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:9, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:9, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:9, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:9, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
  }
  if (TQTOK6=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:10, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:10, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:10, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:10, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:10, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:10, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK7=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:11, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:11, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:11, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:11, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:11, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:11, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK8=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:12, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:12, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:12, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:12, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:12, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:12, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK9=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:13, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:13, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:13, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:13, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:13, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:13, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK10=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:14, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:14, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:14, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:14, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:14, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:14, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK11=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:15, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:15, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:15, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:15, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:15, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:15, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK12=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:16, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:16, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:16, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:16, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:16, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:16, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK13=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:17, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:17, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:17, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:17, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:17, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:17, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK14=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:18, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:18, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:18, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:18, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:18, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:18, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK15=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:19, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:19, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:19, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:19, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:19, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:19, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
}

else{

    capture line:2, column:44, length:5 assign to DOITEST
    capture line:2, column:57, length:8 assign to ticketingOffice

  if (DOITEST!=today){
    send "N0 Void as DOI-" +DOITEST
    ask "Ignore?" assign to qz5
    send "ig"
  }

capture line:4, column:47, length:1 assign to FST1
if (FST1=="C"){
           send "Please check status!"
           ask "The CST checked in" assign to qz5
           send "ig"
}
if (FST1=="V"){
           send "Please check status!"
           ask "The Ticket is Voided, Continue?" assign to qz5
}

if (segmentsCount=="1"){
       capture line:4, column:62, length:2 assign to Bg1
}

if (segmentsCount=="2"){
    capture line:4, column:62, length:2 assign to Bg1
    capture line:5, column:30, length:2 assign to OK2
    if (OK2=="OK"){
        capture line:5, column:62, length:2 assign to Bg2
    }
    else{
        capture line:6, column:62, length:2 assign to Bg2
    }
}

if (segmentsCount=="3"){
    capture line:4, column:62, length:2 assign to Bg1
    capture line:5, column:30, length:2 assign to OK2
    if (OK2=="OK"){
        capture line:5, column:62, length:2 assign to Bg2
    }
    else{
        capture line:6, column:62, length:2 assign to Bg2
    }
    capture line:6, column:30, length:2 assign to OK3
    if (OK3=="OK"){
        capture line:6, column:62, length:2 assign to Bg3
    }
    else{
        capture line:7, column:62, length:2 assign to Bg3
    }
    
}

if (segmentsCount=="4"){
    capture line:4, column:62, length:2 assign to Bg1
    capture line:5, column:30, length:2 assign to OK2
    if (OK2=="OK"){
        capture line:5, column:62, length:2 assign to Bg2
    }
    else{
        capture line:6, column:62, length:2 assign to Bg2
    }
    capture line:6, column:30, length:2 assign to OK3
    if (OK3=="OK"){
        capture line:6, column:62, length:2 assign to Bg3
    }
    else{
        capture line:7, column:62, length:2 assign to Bg3
    }
    capture line:7, column:30, length:2 assign to OK4
    if (OK4=="OK"){
        capture line:7, column:62, length:2 assign to Bg4
    }
    else{
        capture line:8, column:62, length:2 assign to Bg4
    }
}

if (segmentsCount=="5"){
    capture line:4, column:62, length:2 assign to Bg1
    capture line:5, column:30, length:2 assign to OK2
    if (OK2=="OK"){
        capture line:5, column:62, length:2 assign to Bg2
    }
    else{
        capture line:6, column:62, length:2 assign to Bg2
    }
    capture line:6, column:30, length:2 assign to OK3
    if (OK3=="OK"){
        capture line:6, column:62, length:2 assign to Bg3
    }
    else{
        capture line:7, column:62, length:2 assign to Bg3
    }
    capture line:7, column:30, length:2 assign to OK4
    if (OK4=="OK"){
        capture line:7, column:62, length:2 assign to Bg4
    }
    else{
        capture line:8, column:62, length:2 assign to Bg4
    }
    capture line:8, column:30, length:2 assign to OK5
    if (OK5=="OK"){
        capture line:8, column:62, length:2 assign to Bg5
    }
    else{
        capture line:9, column:62, length:2 assign to Bg5
    }
}

if (segmentsCount=="6"){
    capture line:4, column:62, length:2 assign to Bg1
    capture line:5, column:30, length:2 assign to OK2
    if (OK2=="OK"){
        capture line:5, column:62, length:2 assign to Bg2
    }
    else{
        capture line:6, column:62, length:2 assign to Bg2
    }
    capture line:6, column:30, length:2 assign to OK3
    if (OK3=="OK"){
        capture line:6, column:62, length:2 assign to Bg3
    }
    else{
        capture line:7, column:62, length:2 assign to Bg3
    }
    capture line:7, column:30, length:2 assign to OK4
    if (OK4=="OK"){
        capture line:7, column:62, length:2 assign to Bg4
    }
    else{
        capture line:8, column:62, length:2 assign to Bg4
    }
    capture line:8, column:30, length:2 assign to OK5
    if (OK5=="OK"){
        capture line:8, column:62, length:2 assign to Bg5
    }
    else{
        capture line:9, column:62, length:2 assign to Bg5
    }
    capture line:9, column:30, length:2 assign to OK6
    if (OK6=="OK"){
        capture line:9, column:62, length:2 assign to Bg6
    }
    else{
        capture line:10, column:62, length:2 assign to Bg6
    }
}

}

if (Bg1 =="  "){
    assign "0p" to Bg1
}
if (Bg1 =="NO"){
    assign "0p" to Bg1
}

if (Bg2 =="  "){
    assign "0p" to Bg2
}
if (Bg2 =="NO"){
    assign "0p" to Bg2
}

if (Bg3 =="  "){
    assign "0p" to Bg3
}
if (Bg3 =="NO"){
    assign "0p" to Bg3
}

if (Bg4 =="  "){
    assign "0p" to Bg4
}
if (Bg4 =="NO"){
    assign "0p" to Bg4
}

if (Bg5 =="  "){
    assign "0p" to Bg5
}
if (Bg5 =="NO"){
    assign "0p" to Bg5
}

if (Bg6 =="  "){
    assign "0p" to Bg6
}
if (Bg6 =="NO"){
    assign "0p" to Bg6
}



send "tqt/t500"
  capture line:1, column:1, length:2 assign to testTST
    
  capture line:2, column:35, length:3 assign to firstCurr
  capture line:2, column:41, length:10 assign to firstTSTPrice
  capture line:3, column:35, length:3 assign to secondCurr
  capture line:3, column:41, length:10 assign to secondTSTPrice
  capture line:4, column:35, length:3 assign to thirdCurr
  capture line:4, column:41, length:10 assign to thirdTSTPrice
  capture line:5, column:35, length:3 assign to fourthCurr
  capture line:5, column:41, length:10 assign to fourthTSTPrice
  capture line:6, column:35, length:3 assign to fifthCurr
  capture line:6, column:41, length:10 assign to fifthTSTPrice
  capture line:7, column:35, length:3 assign to sixthCurr
  capture line:7, column:41, length:10 assign to sixthTSTPrice
  capture line:8, column:35, length:3 assign to seventhCurr
  capture line:8, column:41, length:10 assign to seventhTSTPrice
  capture line:9, column:35, length:3 assign to eighthCurr
  capture line:9, column:41, length:10 assign to eighthTSTPrice
  capture line:10, column:35, length:3 assign to ninthCurr
  capture line:10, column:41, length:10 assign to ninthTSTPrice
    
  if (testTST != "T "){
    send "There're no TST"
    mandatory ask "Continue?" assign to qz5
  }
  if (ninthCurr == firstCurr){
    send "df" +ninthTSTPrice +";" +eighthTSTPrice +";" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
  if (eighthCurr == firstCurr){
      send "df"  +eighthTSTPrice +";" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (seventhCurr == firstCurr){
       send "df" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (sixthCurr == firstCurr){
      send "df"   +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (fifthCurr == firstCurr){
        send "df"   +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (fourthCurr == firstCurr){
        send "df"   +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (thirdCurr == firstCurr){
          send "df"   +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (secondCurr == firstCurr){
          send "df"   +secondTSTPrice +";" +firstTSTPrice
}
else{
  send "df"   +firstTSTPrice
}//1
}//2
}//3
}//4
}//5
}//6
}//7
}//8
capture line:2, column:1, length:10 assign to totalOldTSTPrice

send "FXR/K"
capture line:1, column:1, length:8 assign to checkAttn
if (checkAttn=="**ATTN**"){
    mandatory ask "There's unavailable class(es)!" assign to qz5
}

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
     
     if (PassengerCount=="1"){
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

            

send "fqq1"


      assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
      send "" +baggageCheckerStatment + " Segment(s)"
      mandatory ask "Continue?" assign to qz5
    }

    send "FQC" +totalNewPrice +"EGP/" +firstCurr
            if (firstCurr=="AED"){
           capture line:4, column:4, length:5 assign to curr2deal
          }
          else {
           capture line:4, column:4, length:8 assign to curr2deal
          }
          send "df" +totalOldTSTPrice +"-" +curr2deal
                 capture line:2, column:1, length:11 assign to diff
                 send "df" + curr2deal +"*0.04;" +diff
                capture line:2, column:1, length:10 assign to egy1deal

                  // send "Void the ticket(s)!"
                    choose "Have you void the ticket(s)?" until "Yes"{
                        when ("No"){
                        }
                    }
                    send "ir"
                    send "tte/all"
                    send "rfRAMADAN;er"
                    send "ir"
                    send "tte/all"
                    send "FXB/K"
                    send "fqq1"

            assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
      send "" +baggageCheckerStatment + " Segment(s)"
      mandatory ask "Continue?" assign to qz5
    }

    
                    send "rfRAMADAN;er"
                    capture line:1, column:1, length:7 assign to Warning
                        if (Warning =="WARNING"){
                            send "er"
                        }
                    capture line:1, column: 1, length: 12 assign to CheckSM
                        if (CheckSM == "SIMULTANEOUS"){ //1
                            send "ir"
                            send "tte/all"
                    send "FXB/K"                            send "rfRAMADAN;er"
                    capture line:1, column:1, length:7 assign to Warning
                        if (Warning =="WARNING"){
                            send "er"
                        }
                    capture line:1, column: 1, length: 12 assign to CheckSM
                        if (CheckSM == "SIMULTANEOUS"){ //2
                            send "ir"
                            send "tte/all"
                    send "FXB/K"                            send "rfRAMADAN;er"
                            capture line:1, column:1, length:7 assign to Warning
                            if (Warning =="WARNING"){
                                send "er"
                            }
                            capture line:1, column: 1, length: 12 assign to CheckSM
                            if (CheckSM == "SIMULTANEOUS"){ //3
                                send "ir"
                                send "tte/all"
                    send "FXB/K"                                send "rfRAMADAN;er"
                            capture line:1, column:1, length:7 assign to Warning
                            if (Warning =="WARNING"){
                                send "er"
                            }
                            capture line:1, column: 1, length: 12 assign to CheckSM
                            if (CheckSM == "SIMULTANEOUS"){ //4
                                send "ir"
                                send "tte/all"
                    send "FXB/K"                                send "rfRAMADAN;er"
                                capture line:1, column:1, length:7 assign to Warning
                                if (Warning =="WARNING"){
                                    send "er"
                                }
                                capture line:1, column: 1, length: 12 assign to CheckSM
                                if (CheckSM == "SIMULTANEOUS"){ //5
                                 send "ir"
                                 send "tte/all"
                    send "FXB/K"                                 send "rfRAMADAN;er"
                                 }//5
                                }//4
                              }//3
                            }//2
                          }//1

                          send "er"
                            call "z_Deal Checker"
                            capture line:2, column:1, length:10 assign to egy2deal
                            if (egy2deal != egy1deal){
    
                    choose "Have you taken the deal?" {
                        when ("Yes"){}
                        when ("No"){
                            send "ir"
                            send "tte/all"
                    send "FXB/K"                            send "rfRAMADAN;er"
                            send "er"
                            call "z_Deal Checker"

                        choose "Have you taken the deal?" {
                        when ("Yes"){}
                        when ("No"){
                            send "ir"
                            send "tte/all"
                    send "FXB/K"                            send "fqq1"
        assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
      send "" +baggageCheckerStatment + " Segment(s)"
      mandatory ask "Continue?" assign to qz5
    }
                            send "rfRAMADAN;er"
                            send "er"
                            call "z_Deal Checker"
                            capture line:1, column:1, length:10 assign to egy1deal
                            if (egy1deal!= egy2deal){

                            choose "Have you taken the deal?" {
                        when ("Yes"){}
                        when ("No"){
                            send "ir"
                            send "tte/all"
                    send "FXB/K"                            
                    send "rfRAMADAN;er"
                            send "er"
                            call "z_Deal Checker"
                        }
                    }
                            }

                            }
                        }
                    }
                        }
                    }
send "ir"
assign "TRUE" to checkCardFund
if (checkCardFund != "FALSE"){
send "rtf"
if (Airline1=="MS"){
   call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
if (Airline1=="SM"){
    call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
    send "FPcash"
}
}

}
if (Airline1=="TK"){ 
    send "fm1"
}
else{
    if (Airline1=="AT"){
        send "fm5"
    }
    else{
        if (Airline1=="HU"){
            send "fm5"
        }
        else{
            send "fm0"
        }
    }
}
    
call "z_RTTN_DEL"

send "rfRAMADAN;er"
capture line:1, column: 1, length: 12 assign to CheckSM
if (CheckSM == "SIMULTANEOUS"){
send "ir"      
if (checkCardFund != "FALSE"){
send "rtf"
if (Airline1=="MS"){
   call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
if (Airline1=="SM"){
    call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
    send "FPcash"
}
}
}

if (Airline1=="TK"){ 
    send "fm1"
}
else{
    if (Airline1=="AT"){
        send "fm5"
    }
    else{
        if (Airline1=="HU"){
            send "fm5"
        }
        else{
            send "fm0"
        }
    }
}
    
call "z_RTTN_DEL"
send "rfRAMADAN;er"
}
send "er"

send "ttp/rt"
capture line:1, column: 1, length: 12 assign to CheckSM2
if (CheckSM2 == "SIMULTANEOUS"){
send "ir"
if (checkCardFund != "FALSE"){
send "rtf"
if (Airline1=="MS"){
   call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
if (Airline1=="SM"){
    call "z_FOPCASH_DEL"  
    send "pdy"
    send "pt*1"
}
else{
    send "FPcash"
}
}
}

if (Airline1=="TK"){ 
    send "fm1"
}
else{
    if (Airline1=="AT"){
        send "fm5"
    }
    else{
        if (Airline1=="HU"){
            send "fm5"
        }
        else{
            send "fm0"
        }
    }
}
    
call "z_RTTN_DEL"
send "rfRAMADAN;er"
send "er"

send "ttp/rt"
}

call "z_Name Sorter"
ask "ok?" assign to qz5
call "z_Deal Checker"      

call "EX_CAI"