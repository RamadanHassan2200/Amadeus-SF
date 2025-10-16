//retrirval
mandatory ask "Enter the PNR: " assign to pnr
send "IG"
if (pnr =="U"){
    call "Updater"
}
if (pnr =="u"){
    call "Updater"
}

send "JGD/USN"
capture line:8, column:43, length:1 assign to agtName
capture line:8, column:44, length:1 assign to agtNameChar2
capture line:8, column:45, length:1 assign to agtNameChar3
capture line:8, column:46, length:1 assign to agtNameChar4
capture line:8, column:47, length:1 assign to agtNameChar5
capture line:8, column:48, length:1 assign to agtNameChar6
capture line:8, column:49, length:1 assign to agtNameChar7
capture line:8, column:50, length:1 assign to agtNameChar8
capture line:8, column:51, length:1 assign to agtNameChar9
capture line:8, column:52, length:1 assign to agtNameChar10
capture line:8, column:53, length:1 assign to agtNameChar11
capture line:8, column:54, length:1 assign to agtNameChar12
capture line:8, column:55, length:1 assign to agtNameChar13
capture line:8, column:56, length:1 assign to agtNameChar14
capture line:8, column:57, length:1 assign to agtNameChar15
capture line:8, column:58, length:1 assign to agtNameChar16
capture line:8, column:59, length:1 assign to agtNameChar17
capture line:8, column:60, length:1 assign to agtNameChar18
capture line:8, column:61, length:1 assign to agtNameChar19
capture line:8, column:62, length:1 assign to agtNameChar20
capture line:8, column:63, length:1 assign to agtNameChar21
capture line:8, column:64, length:1 assign to agtNameChar22

if (agtNameChar2!=" "){
append agtNameChar2 to agtName
if (agtNameChar3!=" "){
append agtNameChar3 to agtName
if (agtNameChar4!=" "){
append agtNameChar4 to agtName
if (agtNameChar5!=" "){
append agtNameChar5 to agtName
if (agtNameChar6!=" "){
append agtNameChar6 to agtName
if (agtNameChar7!=" "){
append agtNameChar7 to agtName
if (agtNameChar8!=" "){
append agtNameChar8 to agtName
if (agtNameChar9!=" "){
append agtNameChar9 to agtName
if (agtNameChar10!=" "){
append agtNameChar10 to agtName
if (agtNameChar11!=" "){
append agtNameChar11 to agtName
if (agtNameChar12!=" "){
append agtNameChar12 to agtName
if (agtNameChar13!=" "){
append agtNameChar13 to agtName
if (agtNameChar14!=" "){
append agtNameChar14 to agtName
if (agtNameChar15!=" "){
append agtNameChar15 to agtName
if (agtNameChar16!=" "){
append agtNameChar16 to agtName
if (agtNameChar17!=" "){
append agtNameChar17 to agtName
if (agtNameChar18!=" "){
append agtNameChar18 to agtName
if (agtNameChar19!=" "){
append agtNameChar19 to agtName
if (agtNameChar20!=" "){
append agtNameChar20 to agtName
if (agtNameChar21!=" "){
append agtNameChar21 to agtName
if (agtNameChar22!=" "){
append agtNameChar22 to agtName
}}}}}}}}}}}}}}}}}}}}}//agtNameChar2

if (agtName == "GUEST"){
  assign "SF" to agtName
}

send "rt" +pnr

// Checking Airline(s) and Travel date and passenger count
send "RTA"
    capture line:2, column:30, length:2 assign to HK1Test
    if (HK1Test=="HK"){
    assign "1" to segmentsCount
    capture line:2, column:2, length:2 assign to seg_No1
    capture line:2, column:6, length:2 assign to Airline1
    capture line:2, column:15, length:5 assign to TravelDate
    capture line:2, column:23, length:3 assign to OriginCity
    capture line:2, column:32, length:1 assign to PassengerCount
    capture line:3, column:30, length:2 assign to HKnextTest
    capture line:2, column:35, length:4 assign to TravelTime
    capture line:2, column:35, length:2 assign to TravelTime1
    capture line:2, column:37, length:2 assign to TravelTime2
    if (HKnextTest=="HK"){
        assign "2" to segmentsCount
        capture line:3, column:2, length:2 assign to seg_No2
        capture line:4, column:30, length:2 assign to HK3Test
        if (HK3Test=="HK"){
        assign "3" to segmentsCount
        capture line:4, column:2, length:2 assign to seg_No3
        capture line:5, column:30, length:2 assign to HK4Test
        if (HK4Test=="HK"){
            assign "4" to segmentsCount
            capture line:5, column:2, length:2 assign to seg_No4
            capture line:6, column:30, length:2 assign to HK5Test
            if (HK5Test=="HK"){
                assign "5" to segmentsCount
                capture line:6, column:2, length:2 assign to seg_No5
                capture line:7, column:30, length:2 assign to HK6Test
                if (HK6Test=="HK"){
                    assign "6" to segmentsCount
                    capture line:7, column:2, length:2 assign to seg_No6
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
    capture line:3, column:2, length:2 assign to seg_No1
    capture line:3, column:6, length:2 assign to Airline1
    capture line:3, column:15, length:5 assign to TravelDate
    capture line:3, column:23, length:3 assign to OriginCity
    capture line:3, column:32, length:1 assign to PassengerCount
    capture line:4, column:30, length:2 assign to HKnextTest
    capture line:3, column:35, length:4 assign to TravelTime
    capture line:3, column:35, length:2 assign to TravelTime1
    capture line:3, column:37, length:2 assign to TravelTime2
        if (HKnextTest=="HK"){
            assign "2" to segmentsCount
            capture line:4, column:2, length:2 assign to seg_No2
            capture line:5, column:30, length:2 assign to HK3Test
            if (HK3Test=="HK"){
            assign "3" to segmentsCount
            capture line:5, column:2, length:2 assign to seg_No3
            capture line:6, column:30, length:2 assign to HK4Test
            if (HK4Test=="HK"){
                assign "4" to segmentsCount
                capture line:6, column:2, length:2 assign to seg_No4
                capture line:7, column:30, length:2 assign to HK5Test
                if (HK5Test=="HK"){
                    assign "5" to segmentsCount
                    capture line:7, column:2, length:2 assign to seg_No5
                    capture line:8, column:30, length:2 assign to HK6Test
                    if (HK6Test=="HK"){
                        assign "6" to segmentsCount
                        capture line:8, column:2, length:2 assign to seg_No6
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
  send "Not Confirmed Segemnts please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
}
}

// ignore >4 segments or >6 passengers

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
  if (Airline1=="R5"){
    send "R5 airline is non-voidable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="UK"){
    ask "Is it connected with AI (Air India)?" assign to qz1
  }
  if (Airline1=="NE"){
    if (TravelDate == today){
        send "NE is non-voidable within 24 hrs."
        ask "Ignore!" assign to qz5
        send "ig"
    }
    else{
      send "DD" +today +"/1"
      capture line:2, column:4, length:5 assign to tomorrow
      if (TravelDate == tomorrow){
          send "DD" +OriginCity
          capture line:2, column:13, length:4 assign to OriginCityCurrentTime
          send "DF" +TravelTime +"-" +OriginCityCurrentTime
          capture line:2, column:1, length:5 assign to TimeDifference
          if (TravelTime <= OriginCityCurrentTime){
            send "NE is non-voidable within 24 hrs."
            ask "Ignore!" assign to qz5
            send "ig"
          }
      }
    }
  }
 if (Airline1=="NP"){
    if (TravelDate == today){
        send "NP is non-voidable within 24 hrs."
        ask "Ignore!" assign to qz5
        send "ig"
    }
    else{
      send "DD" +today +"/1"
      capture line:2, column:4, length:5 assign to tomorrow
      if (TravelDate == tomorrow){
          send "DD" +OriginCity
          capture line:2, column:13, length:4 assign to OriginCityCurrentTime
          send "DF" +TravelTime +"-" +OriginCityCurrentTime
          capture line:2, column:1, length:5 assign to TimeDifference
          if (TravelTime <= OriginCityCurrentTime){
            send "NP is non-voidable within 24 hrs."
            ask "Ignore!" assign to qz5
            send "ig"
          }
      }
    }
  }

  send  "DD" +OriginCity
  capture line:2, column:13, length:2 assign to OriginCityCurrentTime1
  capture line:2, column:15, length:2 assign to OriginCityCurrentTime2
  capture line:2, column:30, length:5 assign to OriginCityCurrentDate
  send "DD" +OriginCityCurrentDate +"/" + TravelDate
  capture line:2, column:1, length:1 assign to checkpast
  capture line:2, column:1, length:2 assign to checktoday
  if (checkpast == "-"){
        send "RTA"
        choose "Is flight in the past?" {
            when ("Yes"){
                send "Ig"
            }
            when ("No"){

            }
        }
    }
  if (checktoday == " 0"){
    send "DF"  +TravelTime1 +"*60-" +TravelTime2 +"-" +OriginCityCurrentTime1 +"*60;" +OriginCityCurrentTime2 
    capture line:2, column:1, length:1 assign to checkTimePast
    capture line:2, column:1, length:5 assign to checkTimeDifference
    if (checkTimePast == "-"){
      send "Flight Departed!"
      ask "Ignore!" assign to qz5
      send "ig"
    }
    if (checkTimeDifference<= "120"){
      send "Flight is within 2Hrs"
      ask "Continue?" assign to qz5
    }
  }

// Checking Airline(s) and Travel date and passenger count//

// Checking the possibilty to take EX-Egy deal
if (OriginCity=="ASW"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="ATZ"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="CAI"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="DBB"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="HBE"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="HMB"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="HRG"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="LXR"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="RMF"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}
if (OriginCity=="SSH"){
      if (Airline1!="SV"){
        if (Airline1!="NP"){
          if (Airline1!="NE"){
            send "EX-Egy deal is available..."
            mandatory ask "Continue..?" assign to qz4
          }
        }
      }
}

  //checking if there's an emd
  send "tqm"
          capture line:1, column:1, length:20 assign to emdTest
          if (emdTest != "NO TSM RECORD EXISTS"){
          send "EMD! Please stop and check."
          mandatory ask "Ignore" assign to qz5
          send "ig"
          }

  //getting the office IATA code
  send "PV"
  capture line:8, column:30, length:8 assign to thisOffice
  capture line:2, column:30, length:9 assign to thisOfficeName
 
    //opening the ticket:
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

    capture line:2, column:44, length:5 assign to DOITEST
    capture line:2, column:57, length:8 assign to ticketingOffice

  if (DOITEST!=today){
    send "N0 Void as DOI-" +DOITEST
    ask "Ignore?" assign to qz5
    send "ig"
  }

  if (ticketingOffice!= thisOffice){
      send "PV/" +ticketingOffice
      mandatory ask "please continue in this office" assign to qz5
      send "ig"
  }

capture line:4, column:47, length:1 assign to FST1
if (FST1=="C"){
           send "Please check status!"
           ask "The CST checked in" assign to qz5
           send "ig"
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

if (Bg1 ==""){
    assign "0p" to Bg1
}
if (Bg1 =="NO"){
    assign "0p" to Bg1
}
if (Bg1 =="0 "){
    assign "0P" to Bg1
}
if (Bg1 =="0K"){
    assign "0P" to Bg1
}

if (Bg2 ==""){
    assign "0p" to Bg2
}
if (Bg2 =="NO"){
    assign "0p" to Bg2
}
if (Bg2 =="0 "){
    assign "0P" to Bg2
}
if (Bg2 =="0K"){
    assign "0P" to Bg2
}

    
if (Bg3 ==""){
    assign "0p" to Bg3
}
if (Bg3 =="NO"){
    assign "0p" to Bg3
}
if (Bg3 =="0 "){
    assign "0P" to Bg3
}
if (Bg3 =="0K"){
    assign "0P" to Bg3
}

if (Bg4 ==""){
    assign "0p" to Bg4
}
if (Bg4 =="NO"){
    assign "0p" to Bg4
}
if (Bg4 =="0 "){
    assign "0P" to Bg4
}
if (Bg4 =="0K"){
    assign "0P" to Bg4
}
        
if (Bg5 ==""){
    assign "0p" to Bg5
}
if (Bg5 =="NO"){
    assign "0p" to Bg5
}
if (Bg5 =="0 "){
    assign "0P" to Bg5
} 
if (Bg5 =="0K"){
    assign "0P" to Bg5
}        

if (Bg6 ==""){
    assign "0p" to Bg6
}
if (Bg6 =="NO"){
    assign "0p" to Bg6
}
if (Bg6 =="0 "){
    assign "0P" to Bg6
}
if (Bg6 =="0K"){
    assign "0P" to Bg6
}

  send "TQT/T500"
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
          
    send "tth"
    capture line:1, column:7, length:9 assign to deletedTSTsTest
    if (deletedTSTsTest == "P/S  NAME"){
        call "z_Deal Checker"
        capture line:2, column:1, length:8 assign to previousTotalDeal
    }
    else{
        assign "0" to previousTotalDeal
    }

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

   send "TTH/T" +heighestTST

assign "" to FF_Statement
send "MD-AFF"
capture line:1, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
  assign "True" to FF_Exist
    capture line:1, column:10, length:1 assign to FF1
    capture line:1, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF1
        capture line:1, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF1
            capture line:1, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF1
                capture line:1, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF1
                    capture line:1, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF1
                        capture line:1, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF1
                            capture line:1, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF1
                                capture line:1, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF1
                                    capture line:1, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF1
                                        capture line:1, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF1
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

capture line:2, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
    capture line:2, column:10, length:1 assign to FF2
    capture line:2, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF2
        capture line:2, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF2
            capture line:2, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF2
                capture line:2, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF2
                    capture line:2, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF2
                        capture line:2, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF2
                            capture line:2, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF2
                                capture line:2, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF2
                                    capture line:2, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF2
                                        capture line:2, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF2
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

capture line:3, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
    capture line:3, column:10, length:1 assign to FF3
    capture line:3, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF3
        capture line:3, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF3
            capture line:3, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF3
                capture line:3, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF3
                    capture line:3, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF3
                        capture line:3, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF3
                            capture line:3, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF3
                                capture line:3, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF3
                                    capture line:3, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF3
                                        capture line:3, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF3
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

capture line:4, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
    capture line:4, column:10, length:1 assign to FF4
    capture line:4, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF4
        capture line:4, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF4
            capture line:4, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF4
                capture line:4, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF4
                    capture line:4, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF4
                        capture line:4, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF4
                            capture line:4, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF4
                                capture line:4, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF4
                                    capture line:4, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF4
                                        capture line:4, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF4
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

capture line:5, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
    capture line:5, column:10, length:1 assign to FF5
    capture line:5, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF5
        capture line:5, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF5
            capture line:5, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF5
                capture line:5, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF5
                    capture line:5, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF5
                        capture line:5, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF5
                            capture line:5, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF5
                                capture line:5, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF5
                                    capture line:5, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF5
                                        capture line:5, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF5
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

capture line:6, column:1, length:3 assign to check_AFF
if (check_AFF == "AFF"){
    capture line:6, column:10, length:1 assign to FF6
    capture line:6, column:11, length:1 assign to FF_check
    if (FF_check != " "){
        append FF_check to FF6
        capture line:6, column:12, length:1 assign to FF_check
        if (FF_check != " "){
            append FF_check to FF6
            capture line:6, column:13, length:1 assign to FF_check
            if (FF_check != " "){
                append FF_check to FF6
                capture line:6, column:14, length:1 assign to FF_check
                if (FF_check != " "){
                    append FF_check to FF6
                    capture line:6, column:15, length:1 assign to FF_check
                    if (FF_check != " "){
                        append FF_check to FF6
                        capture line:6, column:16, length:1 assign to FF_check
                        if (FF_check != " "){
                            append FF_check to FF6
                            capture line:6, column:17, length:1 assign to FF_check
                            if (FF_check != " "){
                                append FF_check to FF6
                                capture line:6, column:18, length:1 assign to FF_check
                                if (FF_check != " "){
                                    append FF_check to FF6
                                    capture line:6, column:19, length:1 assign to FF_check
                                    if (FF_check != " "){
                                        append FF_check to FF6
                                        capture line:6, column:20, length:1 assign to FF_check
                                        if (FF_check != " "){
                                            append FF_check to FF6
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
}

assign "True" to general_FF 
if (segmentsCount > "1"){
    if (FF1 != FF2){
        assign "False" to general_FF 
    }
}
if (segmentsCount > "2"){
    if (FF2 != FF3){
        assign "False" to general_FF 
    }
}
if (segmentsCount > "3"){
    if (FF3 != FF4){
        assign "False" to general_FF 
    }
}
if (segmentsCount > "4"){
    if (FF4 != FF5){
        assign "False" to general_FF 
    }
}
if (segmentsCount > "5"){
    if (FF5 != FF6){
        assign "False" to general_FF 
    }
}

if (general_FF != "True"){
    append seg_No1 to FF_Seg1
    append FF1 to FF_Seg1_FF
    assign "" to FF_Seg2
    assign "" to FF_Seg2_FF
    assign "" to FF_Seg3
    assign "" to FF_Seg3_FF
    assign "" to FF_Seg4
    assign "" to FF_Seg4_FF
    assign "" to FF_Seg5
    assign "" to FF_Seg5_FF
    assign "" to FF_Seg6
    assign "" to FF_Seg6_FF

    if (segmentsCount > "1"){
        if (FF1 != FF2){
            append seg_No2 to FF_Seg2
            append FF2 to FF_Seg2_FF
        }
    }
    if (segmentsCount > "2"){
        if (FF2 != FF3){
            append seg_No3 to FF_Seg3
            append FF3 to FF_Seg3_FF
        }
    }
    if (segmentsCount > "3"){
        if (FF3 != FF4){
            append seg_No4 to FF_Seg4
            append FF4 to FF_Seg4_FF
        }
    }
    if (segmentsCount > "4"){
        if (FF4 != FF5){
            append seg_No5 to FF_Seg5
            append FF5 to FF_Seg5_FF
        }
    }
    if (segmentsCount > "5"){
        if (FF5 != FF6){
            append seg_No6 to FF_Seg6
            append FF6 to FF_Seg6_FF
        }
    }
    append "/FF" to FF_Statement
    append FF_Seg1 +"-" +FF_Seg1_FF to FF_Statement
    if (FF_Seg2 != ""){
        append "/FF" +FF_Seg2 +"-" +FF_Seg2_FF to FF_Statement
    }
    if (FF_Seg3 != ""){
        append "/FF" +FF_Seg3 +"-" +FF_Seg3_FF to FF_Statement
    }
    if (FF_Seg4 != ""){
        append "/FF" +FF_Seg4 +"-" +FF_Seg4_FF to FF_Statement
    }
    if (FF_Seg5 != ""){
        append "/FF" +FF_Seg5 +"-" +FF_Seg5_FF to FF_Statement
    }
    if (FF_Seg6 != ""){
        append "/FF" +FF_Seg6 +"-" +FF_Seg6_FF to FF_Statement
    }
    
}
else{
  if (FF_Exist == "True"){
    append "/FF-" +FF1 to FF_Statement
  }
}
if (FF_Exist != "True"){
    assign ""  to FF_Statement
  }


          assign "/R,U,UP" to ref62
          //FXR/K
          if (Airline1 =="SM"){
            append ",U09" to ref62
          }
          if (Airline1 =="QR"){
            append ",U202201" to ref62
          }
          if (Airline1 == "SN"){
            append ",U385910,P" to ref62
          }
          if (Airline1 == "SV"){
            append ",U*MOS05" to ref62
          }
          if (Airline1 == "WY"){
            append ",U584562" to ref62
          }
          if (Airline1 == "PR"){
            append ",U*C5YQ" to ref62
          }
          
          if (thisOfficeName == "RUHAA2162"){
            append ",*RF" to ref62
          }

          if (thisOfficeName == "CAIEG3645"){
            assign " " to ref62
          }



          send "FXR/K"+ref62 +FF_Statement

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

          if (checknewCurr6 == firstCurr){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == firstCurr){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == firstCurr){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == firstCurr){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == firstCurr){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == firstCurr){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == firstCurr){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == firstCurr){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == firstCurr){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == firstCurr){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == firstCurr){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == firstCurr){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == firstCurr){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == firstCurr){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == firstCurr){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == firstCurr){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == firstCurr){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == firstCurr){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }
    
          
          send "FQQ1"

    capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
        }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
        }
    }

if (fBg1 ==""){
    assign "0p" to fBg1
}
if (fBg1 =="NO"){
    assign "0p" to fBg1
}
if (fBg1 =="0 "){
    assign "0P" to fBg1
}

if (fBg2 ==""){
    assign "0p" to fBg2
}
if (fBg2 =="NO"){
    assign "0p" to fBg2
}
if (fBg2 =="0 "){
    assign "0P" to fBg2
}
    
if (fBg3 ==""){
    assign "0p" to fBg3
}
if (fBg3 =="NO"){
    assign "0p" to fBg3
}
if (fBg3 =="0 "){
    assign "0P" to fBg3
}

if (fBg4 ==""){
    assign "0p" to fBg4
}
if (fBg4 =="NO"){
    assign "0p" to fBg4
}
if (fBg4 =="0 "){
    assign "0P" to fBg4
}
        
if (fBg5 ==""){
    assign "0p" to fBg5
}
if (fBg5 =="NO"){
    assign "0p" to fBg5
}
if (fBg5 =="0 "){
    assign "0P" to fBg5
}        

if (fBg6 ==""){
    assign "0p" to fBg6
}
if (fBg6 =="NO"){
    assign "0p" to fBg6
}
if (fBg6 =="0 "){
    assign "0P" to fBg6
}

      assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

        if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
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


          if (totalNewPrice<totalOldTSTPrice){
                  send "df" +totalOldTSTPrice +"-" +totalNewPrice
                  capture line:2, column:1, length:8 assign to diff
                  send "FO deal with: " +diff
          }
            
          assign " " to NPcheck
          if (thisOfficeName == "RUHAA2300"){
            assign "/T-NP" to NPcheck
          }
          //FXR SELECTION
          choose "Next Action..?" {
            when ("Proceed"){
              choose "Continue?"{
                  when ("Yes"){
                      send "IR"
                      send "trdc/all" +NPcheck
                      capture line:1, column:1, length:26 assign to Voidmsg
                      if (Voidmsg!="OK - DOCUMENT(S) CANCELLED"){
                          assign "1" to checkvoidedtickets
                          capture line:7, column:23, length:26 assign to Voidmsg1
                          capture line:8, column:23, length:26 assign to Voidmsg2
                          capture line:9, column:23, length:26 assign to Voidmsg3
                          capture line:10, column:23, length:26 assign to Voidmsg4
                          capture line:11, column:23, length:26 assign to Voidmsg5
                          capture line:12, column:23, length:26 assign to Voidmsg6
                          capture line:13, column:23, length:26 assign to Voidmsg7
                          capture line:14, column:23, length:26 assign to Voidmsg8
                          capture line:15, column:23, length:26 assign to Voidmsg9
                          capture line:16, column:23, length:26 assign to Voidmsg10
                          if (PassengerCount>"1"){
                              if (Voidmsg1!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                              }
                              if (Voidmsg2!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                              }
                              if (PassengerCount>"2"){
                                  if (Voidmsg3!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                                  }
                                  if (PassengerCount>"3"){
                                    if (Voidmsg4!="OK - DOCUMENT(S) CANCELLED"){
                                      assign "0" to checkvoidedtickets
                                    }
                                    if (PassengerCount>"4"){
                                        if (Voidmsg5!="OK - DOCUMENT(S) CANCELLED"){
                                          assign "0" to checkvoidedtickets
                                        }
                                        if (PassengerCount>"5"){
                                            if (Voidmsg6!="OK - DOCUMENT(S) CANCELLED"){
                                              assign "0" to checkvoidedtickets
                                            }
                                            if (PassengerCount>"6"){
                                                if (Voidmsg7!="OK - DOCUMENT(S) CANCELLED"){
                                                    assign "0" to checkvoidedtickets
                                                }
                                                if (PassengerCount>"7"){
                                                  if (Voidmsg8!="OK - DOCUMENT(S) CANCELLED"){
                                                    assign "0" to checkvoidedtickets
                                                  }
                                                  if (PassengerCount>"8"){
                                                      if (Voidmsg9!="OK - DOCUMENT(S) CANCELLED"){
                                                        assign "0" to checkvoidedtickets
                                                      }
                                                      if (Voidmsg10=="OK - DOCUMENT(S) CANCELLED"){
                                                        assign "0" to checkvoidedtickets
                                                      }
                                                  }//>8
                                                }//>7
                                            }//>6
                                        }//>5
                                    }//>4
                                  }//>3
                              }//>2
                          }
                          else {
                            assign "0" to checkvoidedtickets
                          }
                          
                          if (checkvoidedtickets=="0"){
                            ask "Are the tickets voided?" assign to qz5
                          }
                        
                      }
                      send "ir"
                      send "ir"
                      send "tte/all"              
                      send "FXB/K"+ref62 +FF_Statement
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

    
                      send "rf" +agtName +";er"
                      send "er"
                      capture line:1, column: 1, length: 12 assign to CheckSM
                      if (CheckSM == "SIMULTANEOUS"){
                      send "ir"
                      send "tte/all"
                      send "FXB/K"+ref62 +FF_Statement
                      send "rf" +agtName +";er" 
                      send "er"
                      }

                      send "tth"
                      call "z_Deal Checker"
                      capture line:2, column:1, length:8 assign to fDealdifference
                      send "df" +fDealdifference +"-" +previousTotalDeal
                      capture line:2, column:1, length:8 assign to fDealdiff
                      if (fDealdiff!=diff){
                      choose "have you taken the deal?" until "yes"{
                           when ("No"){
                              send "ir"
                              send "tte/all"
                              send "FXB/K"+ref62 +FF_Statement
                              send "rf" +agtName +";er"
                              capture line:1, column:1, length:7 assign to Warning
                              if (Warning =="WARNING"){send "er"
                                  }
                              capture line:1, column: 1, length: 12 assign to CheckSM
                                  if (CheckSM == "SIMULTANEOUS"){
                                  send "ir"
                                  send "tte/all"
                                  send "FXB/K"+ref62 +FF_Statement
                                  send "rf" +agtName +";er" 
                                  send "er"
                                  }
                                  send "rf" +agtName +";er"
                                  send "er"
                                  send "tth"
                                  call "z_Deal Checker"
                          }
                      }
                      }
                      send "ir"
                      send "ir"
                      send "fpcash"
                      send "fm0"
                      call "z_RTTN_DEL"          
                      send "rf" +agtName +";er"
                      capture line:1, column:1, length:7 assign to Warning
                      if (Warning =="WARNING"){send "er"}
                      if (thisOfficeName =="KWIKT2809"){
                               call "Check HK Segment"
                      }
                      if (thisOfficeName=="DXBAD31DO"){
                                call "Check HK Segment"
                      }
                      else{
                               send "QE/" +thisOfficeName +"/21c0"
                      }



//                        if (thisOfficeName == "KWIKT2809"){
  //                          send "RM FIRST ISSUE"
    //                        send "RM SKIP HF"
      //                      send "RM AMEX"
        //                }
          //              else{
            //                if (thisOfficeName == "DXBAD31DO"){
              //                  send "RM FIRST ISSUE"
                //                send "RM SKIP HF"
                  //              send "RM AMEX"
                    //        }
//                            else{
  //                              if (thisOfficeName != "CAIEG3645"){
    //                                send "RM FRESH ISSUE"
      //                              send "RM SKIP HF"
        //                            send "RM AMEX"
          //                      }
            //                }
              //          }
//
  //                           send "rf" +agtName +";er"
    //                         send "er"
      //                      capture line:1, column: 1, length: 12 assign to CheckSM
        //                    if (CheckSM == "SIMULTANEOUS"){
          //                      send "ir"
            //                    send "fpcash"
              //                  send "fm0"
                //                call "z_RTTN_DEL" 
                  //              
//                                if (thisOfficeName == "KWIKT2809"){
  //                          send "RM FIRST ISSUE"
    //                        send "RM SKIP HF"
      //                      send "RM AMEX"
        //                }
          //              else{
            //                if (thisOfficeName == "DXBAD31DO"){
              //                  send "RM FIRST ISSUE"
                //                send "RM SKIP HF"
                  //              send "RM AMEX"
                    //        }
//                            else{
  //                              if (thisOfficeName != "CAIEG3645"){
    //                                send "RM FRESH ISSUE"
      //                              send "RM SKIP HF"
        //                            send "RM AMEX"
          //                      }
            //                }
              //          }
//
  //                           send "rf" +agtName +";er"
    //                         send "er"
//
  //                          }
    //                         send "ttp/rt"
      //                       call "z_Name Sorter"
        //                     ask "continue?" assign to qz5
          //                   call "z_Deal Checker" 
                      }
                      when ("NO"){
                          send "ig"
                      }
                   }

              }
              when ("Try SBF"){
          
                     //FXR/K/SBF-1
          send "FXR/K" +ref62 +FF_Statement +"/SBF-1"

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

          if (checknewCurr6 == firstCurr){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == firstCurr){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == firstCurr){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == firstCurr){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == firstCurr){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == firstCurr){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == firstCurr){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == firstCurr){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == firstCurr){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == firstCurr){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == firstCurr){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == firstCurr){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == firstCurr){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == firstCurr){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == firstCurr){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == firstCurr){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == firstCurr){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == firstCurr){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }
    
          
          send "FQQ1"

    capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
        }
        if (segmetsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
        }
        if (segmetsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
        }
        if (segmetsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
        }
        if (segmetsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
        if (segmetsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
        }
        if (segmetsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
        }
        if (segmetsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
        }
        if (segmetsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
        }
        if (segmetsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
        if (segmetsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
        }
        if (segmetsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
        }
        if (segmetsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
        }
        if (segmetsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
        }
        if (segmetsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
        }
    }

if (fBg1 ==""){
    assign "0p" to fBg1
}
if (fBg1 =="NO"){
    assign "0p" to fBg1
}
if (fBg1 =="0 "){
    assign "0P" to fBg1
}

if (fBg2 ==""){
    assign "0p" to fBg2
}
if (fBg2 =="NO"){
    assign "0p" to fBg2
}
if (fBg2 =="0 "){
    assign "0P" to fBg2
}
    
if (fBg3 ==""){
    assign "0p" to fBg3
}
if (fBg3 =="NO"){
    assign "0p" to fBg3
}
if (fBg3 =="0 "){
    assign "0P" to fBg3
}

if (fBg4 ==""){
    assign "0p" to fBg4
}
if (fBg4 =="NO"){
    assign "0p" to fBg4
}
if (fBg4 =="0 "){
    assign "0P" to fBg4
}
        
if (fBg5 ==""){
    assign "0p" to fBg5
}
if (fBg5 =="NO"){
    assign "0p" to fBg5
}
if (fBg5 =="0 "){
    assign "0P" to fBg5
}        

if (fBg6 ==""){
    assign "0p" to fBg6
}
if (fBg6 =="NO"){
    assign "0p" to fBg6
}
if (fBg6 =="0 "){
    assign "0P" to fBg6
}

        assign "True" to BaggageChecker1
      assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

        if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmetsCount=="2"){
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmetsCount=="3"){
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmetsCount=="4"){
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
        if (segmetsCount=="5"){
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
        if (segmetsCount=="6"){
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
    

          if (totalNewPrice<totalOldTSTPrice){
                  send "df" +totalOldTSTPrice +"-" +totalNewPrice
                  capture line:2, column:1, length:8 assign to diff
                  send "FO deal with: " +diff
          }

    
          //FXR SELECTION
          choose "Next Action..?" {
            when ("Proceed"){
              choose "Continue?"{
                  when ("Yes"){
                      send "rf" +agtName +";er"
                      send "er"
                      send "ir"
                      send "trdc/all" +NPcheck
                      capture line:1, column:1, length:26 assign to Voidmsg
                      if (Voidmsg!="OK - DOCUMENT(S) CANCELLED"){
                          assign "1" to checkvoidedtickets
                          capture line:7, column:23, length:26 assign to Voidmsg1
                          capture line:8, column:23, length:26 assign to Voidmsg2
                          capture line:9, column:23, length:26 assign to Voidmsg3
                          capture line:10, column:23, length:26 assign to Voidmsg4
                          capture line:11, column:23, length:26 assign to Voidmsg5
                          capture line:12, column:23, length:26 assign to Voidmsg6
                          capture line:13, column:23, length:26 assign to Voidmsg7
                          capture line:14, column:23, length:26 assign to Voidmsg8
                          capture line:15, column:23, length:26 assign to Voidmsg9
                          capture line:16, column:23, length:26 assign to Voidmsg10
                          if (PassengerCount>"1"){
                              if (Voidmsg1!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                              }
                              if (Voidmsg2!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                              }
                              if (PassengerCount>"2"){
                                  if (Voidmsg3!="OK - DOCUMENT(S) CANCELLED"){
                                  assign "0" to checkvoidedtickets
                                  }
                                  if (PassengerCount>"3"){
                                    if (Voidmsg4!="OK - DOCUMENT(S) CANCELLED"){
                                      assign "0" to checkvoidedtickets
                                    }
                                    if (PassengerCount>"4"){
                                        if (Voidmsg5!="OK - DOCUMENT(S) CANCELLED"){
                                          assign "0" to checkvoidedtickets
                                        }
                                        if (PassengerCount>"5"){
                                            if (Voidmsg6!="OK - DOCUMENT(S) CANCELLED"){
                                              assign "0" to checkvoidedtickets
                                            }
                                            if (PassengerCount>"6"){
                                                if (Voidmsg7!="OK - DOCUMENT(S) CANCELLED"){
                                                    assign "0" to checkvoidedtickets
                                                }
                                                if (PassengerCount>"7"){
                                                  if (Voidmsg8!="OK - DOCUMENT(S) CANCELLED"){
                                                    assign "0" to checkvoidedtickets
                                                  }
                                                  if (PassengerCount>"8"){
                                                      if (Voidmsg9!="OK - DOCUMENT(S) CANCELLED"){
                                                        assign "0" to checkvoidedtickets
                                                      }
                                                      if (Voidmsg10=="OK - DOCUMENT(S) CANCELLED"){
                                                        assign "0" to checkvoidedtickets
                                                      }
                                                  }//>8
                                                }//>7
                                            }//>6
                                        }//>5
                                    }//>4
                                  }//>3
                              }//>2
                          }
                          else {
                            assign "0" to checkvoidedtickets
                          }
                          
                          if (checkvoidedtickets=="0"){
                            ask "Are the tickets voided?" assign to qz5
                          }
                        
                      }
                      send "ir"
                      send "tte/all"
                      send "ir"
                      send "ir"
                      send "tte/all"
                      send "FXB/K" +ref62 +FF_Statement +"/SBF-1"
                      send "rf" +agtName +";er"
                      send "er"
                      capture line:1, column: 1, length: 12 assign to CheckSM
                      if (CheckSM == "SIMULTANEOUS"){
                      send "ir"
                      send "tte/all"
                      send "FXB/K" +ref62 +FF_Statement +"/SBF-1"
                      send "rf" +agtName +";er" 
                      send "er"
                      }

                      send "tth"
                      call "z_Deal Checker"
                      capture line:2, column:1, length:8 assign to fDealdifference
                      send "df" +fDealdifference +"-" +previousTotalDeal
                      capture line:2, column:1, length:8 assign to fDealdiff
                      if (fDealdiff!=diff){
                      choose "have you taken the deal?" until "yes"{
                           when ("No"){
                              send "ir"
                              send "tte/all"
                              send "FXB/K" +ref62 +FF_Statement +"/SBF-1"
                              send "rf" +agtName +";er"
                              capture line:1, column:1, length:7 assign to Warning
                              if (Warning =="WARNING"){send "er"
                                  }
                              capture line:1, column: 1, length: 12 assign to CheckSM
                                  if (CheckSM == "SIMULTANEOUS"){
                                  send "ir"
                                  send "tte/all"
                                  send "FXB/K" +ref62 +FF_Statement +"/SBF-1"
                                  send "rf" +agtName +";er" 
                                  send "er"
                                  }
                                  send "rf" +agtName +";er"
                                  send "er"
                                  send "tth"
                                  call "z_Deal Checker"
                          }
                      }
                      }
                      send "ir"
                      send "ir"
                      send "fpcash"
                      send "fm0"
                      call "z_RTTN_DEL"          
                      send "rf" +agtName +";er"
                      capture line:1, column:1, length:7 assign to Warning
                      if (Warning =="WARNING"){send "er"}
                      if (thisOfficeName =="KWIKT2809"){
                             call "Check HK Segment"
                      }
                      if (thisOfficeName=="DXBAD31DO"){
                            call "Check HK Segment"
                      }
                      else{
                             send "QE/" +thisOfficeName +"/21c0"
                       }



    //                    if (thisOfficeName == "KWIKT2809"){
      //                      send "RM FIRST ISSUE"
        //                    send "RM SKIP HF"
          //                  send "RM AMEX"
            //            }
              //          else{
    //                        if (thisOfficeName == "DXBAD31DO"){
      //                          send "RM FIRST ISSUE"
        //                        send "RM SKIP HF"
          //                      send "RM AMEX"
            //                }
    //                        else{
      //                          if (thisOfficeName != "CAIEG3645"){
        //                            send "RM FRESH ISSUE"
          //                          send "RM SKIP HF"
            //                        send "RM AMEX"
              //                  }
                //            }
                  //      }

    //                         send "rf" +agtName +";er"
      //                       send "er"
        //                    capture line:1, column: 1, length: 12 assign to CheckSM
          //                  if (CheckSM == "SIMULTANEOUS"){
            //                    send "ir"
              //                  send "fpcash"
                //                send "fm0"
                  //              call "z_RTTN_DEL" 
    //                            
      //                          if (thisOfficeName == "KWIKT2809"){
        //                    send "RM FIRST ISSUE"
          //                  send "RM SKIP HF"
            //                send "RM AMEX"
              //          }
    //                    else{
      //                      if (thisOfficeName == "DXBAD31DO"){
        //                        send "RM FIRST ISSUE"
          //                      send "RM SKIP HF"
            //                    send "RM AMEX"
              //              }
                //            else{
    //                            if (thisOfficeName != "CAIEG3645"){
      //                              send "RM FRESH ISSUE"
        //                            send "RM SKIP HF"
          //                          send "RM AMEX"
            //                    }
              //              }
                //        }
    //
      //                       send "rf" +agtName +";er"
        //                     send "er"
//
  //                          }
    //                         send "ttp/rt"
      //                       call "z_Name Sorter"
        //                     ask "continue?" assign to qz5
          //                   call "z_Deal Checker" 
                      }
                      when ("NO"){
                          send "ig"
                      }
                   }

              }
              when ("Search with FXX"){    
                  call "FXX_TEST"
              }

              when ("Ignore"){
                  send "ig"
              }


      }


              }
              when ("Search with FXX"){    
                  call "FXX_TEST"
              }

              when ("Ignore"){
                  send "ig"
              }


      }

call "test1"





