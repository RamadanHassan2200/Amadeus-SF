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

}

capture line:3, column:30, length:2 assign to HK2Test
if (HK2Test=="HK"){
  assign "1" to segmentsCount
  capture line:3, column:6, length:2 assign to Airline1
  capture line:3, column:15, length:5 assign to TravelDate
  capture line:3, column:23, length:3 assign to OriginCity
  capture line:3, column:32, length:1 assign to PassengerCount
}

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
                                                }
                                          }
                                    }
                              }
                        }
                  }
            }      
      }    
}



********************* SIGN IDENTIFICATION **********************                
     OFFICE                        - RUHAA2218                                  
     SIGN                          - 359292                                     
                                                                                
*********************** SECURITY PROFILE ***********************                
USN *   USER NAME                       - RAMADAN 13107017 ABDAL                
                                          LAH

capture line:3, column:30, length:2 assign to HK2Test
if (HK2Test=="HK"){
  assign "1" to segmentsCount
  capture line:3, column:6, length:2 assign to Airline1
  capture line:3, column:15, length:5 assign to TravelDate
  capture line:3, column:23, length:3 assign to OriginCity
  capture line:3, column:32, length:1 assign to PassengerCount
  
}

else{
  send "Not Confirmed Segemnts please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
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
    ask "Is it connected with AI (Air India)?" assign to qz1
  }
  if (Airline1=="NE"){
    send " NE airline is non-voidable within 24HRs"
    ask "Is it tomorrow?" assign to qz
    send "IR"
    ask "Is it tomorrow?" assign to qz3
  }
    
  //Today dates aren't considered
  if (TravelDate == today){
    send  "No void for today flights"
    ask "Check again please!" assign to qz
    send "ig"
  }
// Checking Airline(s) and Travel date and passenger count//

// Checking the possibilty to take EX-Egy deal
if (OriginCity=="ASW"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="ATZ"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="CAI"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="DBB"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="HBE"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="HMB"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="HRG"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="LXR"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="RMF"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
        send "EX-Egy deal is available..."
        mandatory ask "Continue..?" assign to qz4
      }
    }
  }
}
if (OriginCity=="SSH"){
  if (Airline1!="NE"){
    if (Airline1!="NP"){
      if (Airline1!="SV"){
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

if (Bg1 =="  "){
    assign "0p" to Bg1
}
if (Bg1 =="NO"){
    assign "0p" to Bg1
}
if (Bg1 =="0 "){
    assign "0P" to Bg1
}

if (Bg2 =="  "){
    assign "0p" to Bg2
}
if (Bg2 =="NO"){
    assign "0p" to Bg2
}
if (Bg2 =="0 "){
    assign "0P" to Bg2
}
    
if (Bg3 =="  "){
    assign "0p" to Bg3
}
if (Bg3 =="NO"){
    assign "0p" to Bg3
}
if (Bg3 =="0 "){
    assign "0P" to Bg3
}

if (Bg4 =="  "){
    assign "0p" to Bg4
}
if (Bg4 =="NO"){
    assign "0p" to Bg4
}
if (Bg4 =="0 "){
    assign "0P" to Bg4
}
        
if (Bg5 =="  "){
    assign "0p" to Bg5
}
if (Bg5 =="NO"){
    assign "0p" to Bg5
}
if (Bg5 =="0 "){
    assign "0P" to Bg5
}        

if (Bg6 =="  "){
    assign "0p" to Bg6
}
if (Bg6 =="NO"){
    assign "0p" to Bg6
}
if (Bg6 =="0 "){
    assign "0P" to Bg6
}

  send "tqt/t500"
  capture line:1, column:1, length:2 assign to testTST

  capture line:2, column:1, length:2 assign to TSTNo1
  capture line:2, column:35, length:3 assign to firstCurr
  capture line:2, column:41, length:10 assign to firstTSTPrice
  capture line:2, column:75, length:5 assign to firstSegments

  capture line:3, column:1, length:2 assign to TSTNo2
  capture line:3, column:35, length:3 assign to secondCurr
  capture line:3, column:41, length:10 assign to secondTSTPrice
  capture line:3, column:75, length:5 assign to secondSegments

  capture line:4, column:1, length:2 assign to TSTNo3
  capture line:4, column:35, length:3 assign to thirdCurr
  capture line:4, column:41, length:10 assign to thirdTSTPrice
  capture line:4, column:75, length:5 assign to thirdSegments

  capture line:5, column:1, length:2 assign to TSTNo4
  capture line:5, column:35, length:3 assign to fourthCurr
  capture line:5, column:41, length:10 assign to fourthTSTPrice
  capture line:5, column:75, length:5 assign to fourthSegments

  capture line:6, column:1, length:2 assign to TSTNo5
  capture line:6, column:35, length:3 assign to fifthCurr
  capture line:6, column:41, length:10 assign to fifthTSTPrice
  capture line:6, column:75, length:5 assign to fifthSegments

  capture line:7, column:1, length:2 assign to TSTNo6
  capture line:7, column:35, length:3 assign to sixthCurr
  capture line:7, column:41, length:10 assign to sixthTSTPrice
  capture line:7, column:75, length:5 assign to sixthSegments

  capture line:8, column:1, length:2 assign to TSTNo7
  capture line:8, column:35, length:3 assign to seventhCurr
  capture line:8, column:41, length:10 assign to seventhTSTPrice
  capture line:8, column:75, length:5 assign to seventhSegments

  capture line:9, column:1, length:2 assign to TSTNo8
  capture line:9, column:35, length:3 assign to eighthCurr
  capture line:9, column:41, length:10 assign to eighthTSTPrice
  capture line:9, column:75, length:5 assign to eighthSegments

  capture line:10, column:1, length:2 assign to TSTNo9
  capture line:10, column:35, length:3 assign to ninthCurr
  capture line:10, column:41, length:10 assign to ninthTSTPrice
  capture line:10, column:75, length:5 assign to ninthSegments

  capture line:11, column:1, length:2 assign to TSTNo10
  capture line:11, column:35, length:3 assign to tenthCurr
  capture line:11, column:41, length:10 assign to tenthTSTPrice
  capture line:11, column:75, length:5 assign to tenthSegments

  capture line:12, column:1, length:2 assign to TSTNo11
  capture line:12, column:35, length:3 assign to eleventhCurr
  capture line:12, column:41, length:10 assign to eleventhTSTPrice
  capture line:12, column:75, length:5 assign to eleventhSegments

  capture line:13, column:1, length:2 assign to TSTNo12
  capture line:13, column:35, length:3 assign to twelfthCurr
  capture line:13, column:41, length:10 assign to twelfthTSTPrice
  capture line:13, column:75, length:5 assign to twelfthSegments

  capture line:14, column:1, length:2 assign to TSTNo13
  capture line:14, column:35, length:3 assign to thirteenthCurr
  capture line:14, column:41, length:10 assign to thirteenthTSTPrice
  capture line:14, column:75, length:5 assign to thirteenthSegments

  capture line:15, column:1, length:2 assign to TSTNo14
  capture line:15, column:35, length:3 assign to fourteenthCurr
  capture line:15, column:41, length:10 assign to fourteenthTSTPrice
  capture line:15, column:75, length:5 assign to fourteenthSegments

  capture line:16, column:1, length:2 assign to TSTNo15
  capture line:16, column:35, length:3 assign to fifteenthCurr
  capture line:16, column:41, length:10 assign to fifteenthTSTPrice
  capture line:16, column:75, length:5 assign to fifteenthSegments

  capture line:17, column:1, length:2 assign to TSTNo16
  capture line:17, column:35, length:3 assign to sixteenthCurr
  capture line:17, column:41, length:10 assign to sixteenthTSTPrice
  capture line:17, column:75, length:5 assign to sixteenthSegments

  capture line:18, column:1, length:2 assign to TSTNo17
  capture line:18, column:35, length:3 assign to seventeenthCurr
  capture line:18, column:41, length:10 assign to seventeenthTSTPrice
  capture line:18, column:75, length:5 assign to seventeenthSegments

  capture line:19, column:1, length:2 assign to TSTNo18
  capture line:19, column:35, length:3 assign to eighteenthCurr
  capture line:19, column:41, length:10 assign to eighteenthTSTPrice
  capture line:19, column:75, length:5 assign to eighteenthSegments

    
  if (testTST != "T "){
    send "There're no TST"
    mandatory ask "Continue?" assign to qz5
  }

  if (secondCurr==firstCurr){
    if (secondSegments==firstSegments){
        assign "1" to TSTSegmentsCount
    }
    else{
        assign "2" to TSTSegmentsCount
    }
  }
  if (thirdCurr==firstCurr){
    if (thirdSegments==firstSegments){
      if (thirdSegments==secondSegments){
        assign "1" to TSTSegmentsCount
      }
    }
    else{
        
    }
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
          
          //FXR/k/r,up
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
     else{
          send "The new price(S) is not detected!"
          mandatory ask "Continue?" assign to qz5
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

if (fBg1 =="  "){
    assign "0p" to fBg1
}
if (fBg1 =="NO"){
    assign "0p" to fBg1
}
if (fBg1 =="0 "){
    assign "0P" to fBg1
}

if (fBg2 =="  "){
    assign "0p" to fBg2
}
if (fBg2 =="NO"){
    assign "0p" to fBg2
}
if (fBg2 =="0 "){
    assign "0P" to fBg2
}
    
if (fBg3 =="  "){
    assign "0p" to fBg3
}
if (fBg3 =="NO"){
    assign "0p" to fBg3
}
if (fBg3 =="0 "){
    assign "0P" to fBg3
}

if (fBg4 =="  "){
    assign "0p" to fBg4
}
if (fBg4 =="NO"){
    assign "0p" to fBg4
}
if (fBg4 =="0 "){
    assign "0P" to fBg4
}
        
if (fBg5 =="  "){
    assign "0p" to fBg5
}
if (fBg5 =="NO"){
    assign "0p" to fBg5
}
if (fBg5 =="0 "){
    assign "0P" to fBg5
}        

if (fBg6 =="  "){
    assign "0p" to fBg6
}
if (fBg6 =="NO"){
    assign "0p" to fBg6
}
if (fBg6 =="0 "){
    assign "0P" to fBg6
}

        if (fBg1 !=Bg1){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "fqq1"
            }
        if (segmetsCount=="2"){
            if (fBg2 !=Bg2){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
        }
        if (segmetsCount=="3"){
            if (fBg2 !=Bg2){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg3 !=Bg3){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
        }
        if (segmetsCount=="4"){
            if (fBg2 !=Bg2){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg3 !=Bg3){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg4 !=Bg4){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
        }
        if (segmetsCount=="5"){
            if (fBg2 !=Bg2){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg3 !=Bg3){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg4 !=Bg4){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg5 !=Bg5){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
        }
        if (segmetsCount=="6"){
            if (fBg2 !=Bg2){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg3 !=Bg3){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg4 !=Bg4){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg5 !=Bg5){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
            if (fBg6!=Bg6){
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
                send "Please check the baggage allownce!"
                ask "Continue?" assign to qz5
            }
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
                      send "ir"
                      send "trdc/all"
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
                          }//>1
                          
                          if (checkvoidedtickets=="0"){
                            ask "Are the tickets voided?" assign to qz5
                          }
                        
                      }
                      send "ir"
                      send "tte/all"
                      send "ir"
                      send "tte/all"
                      send "fxb/k/r,up"
                      send "rfRAMADAN;er"
                      send "er"
                      capture line:1, column: 1, length: 12 assign to CheckSM
                      if (CheckSM == "SIMULTANEOUS"){
                      send "ir"
                      send "tte/all"
                      send "fxb/k/r,up"
                      send "rfRAMADAN;er" 
                      send "er"
                      }

                      send "tth"
                      call "z_Deal Checker"
                      capture line:1, column:1, length:8 assign to fDealdiff
                      if (fDealdiff==diff){
                          send "FO has been successfully taken!"
                      }
                      else{
                        send "Plesae retry!"
                      }
                      choose "have you taken the deal?" until "yes"{
                           when ("No"){
                              send "ir"
                              send "tte/all"
                              send "fxb/k/r,up"
                              send "rfRAMADAN;er"
                              capture line:1, column:1, length:7 assign to Warning
                              if (Warning =="WARNING"){send "er"
                                  }
                              capture line:1, column: 1, length: 12 assign to CheckSM
                                  if (CheckSM == "SIMULTANEOUS"){
                                  send "ir"
                                  send "tte/all"
                                  send "fxb/k/r,up"
                                  send "rfRAMADAN;er" 
                                  send "er"
                                  }
                                  send "rfRAMADAN;er"
                                  send "er"
                                  send "tth"
                                  call "z_Deal Checker"
                          }
                      }
                      send "fpcash"
                      send "fm0"
                      call "z_RTTN_DEL"          
                      send "rfRAMADAN;er"
                      capture line:1, column:1, length:7 assign to Warning
                      if (Warning =="WARNING"){send "er"}
            //          if (thisOfficeName =="KWIKT2809"){
            //                   call "Check HK Segment"
            //          }
            //          if (thisOfficeName=="DXBAD31DO"){
            //                     call "Check HK Segment"
            //          }
            //          else{
            //                    send "QE/" +thisOfficeName +"/21c0"
            //          }

                    //   choose "Manual issuing or Queued?" {
                    //      when ("Queued"){
                        //      if (thisOfficeName =="KWIKT2809"){
                         //       call "Check HK Segment"
                        //      }
                       //       if (thisOfficeName=="DXBAD31DO"){
                      //           call "Check HK Segment"
                     //         }
                    //          else{
                      //          send "QE/" +thisOfficeName +"/21c0"
                    //          }
                      //    }
                    //      when ("manual"){
                              send "rm fresh issue"
                              send "rm skip hf"
                              send "rm amex"
                              send "rfRAMADAN;er"
                              send "er"
                              send "ttp/rt"
                              call "z_Name Sorter"
                              ask "continue?" assign to qz5
                              call "z_Deal Checker"
                            //  send "rttn"
                             // capture line:2, column:2, length:2 assign to LineNumber
                           //   send "TWD/l"+LineNumber
                         // }
                       //}    
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

call "test1"
