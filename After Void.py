//retrirval
mandatory ask "Enter the PNR: " assign to pnr
send "IG"
if (pnr =="U"){
    call "Updater"
}
if (pnr =="u"){
    call "Updater"
}

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
  send "Not Confirmed Segemnts please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
}
}

// ignore >4 segments or >6 passengers

// Non-refundable airlines: A3, ER, H1, NP, R5, UK with AI
  if (Airline1=="A3") {
    send "A3 airline is non-refundable for (P,U,T,S) Classes"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="H1"){
    send "H1 airline is non-refundable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
  if (Airline1=="R5"){
    send "R5 airline is non-refundable"
    ask "Stop and Review" assign to qz5
    send "ig"
  }
    
  //Today dates aren't considered
  if (TravelDate == today){
    send  "No refund/void for today flights!"
    ask "Check again please!" assign to qz
    send "ig"
  }

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
  assign "0" to FACount
  assign "0" to FACountStart
  capture line:2, column:5, length:2 assign to FA1
          if (FA1=="FA"){
            assign "1" to FACountStart
            assign "1" to FACount
            capture line:2, column:12, length:14 assign to TnFA1
          }
          if (FA1=="FH"){
            assign "1" to FACountStart
            assign "1" to FACount
            capture line:2, column:13, length:14 assign to TnFA1
          }
          capture line:3, column:5, length:2 assign to FA2
          if (FA2=="FA"){
              assign "2" to FACountStart
              if (FACount=="1"){
                  assign "2" to FACount
              }
              else {
                  assign "1" to FACount
              }
                capture line:3, column:12, length:14 assign to TnFA2
          }
          if (FA2=="FH"){
            assign "2" to FACountStart
            if (FACount=="1"){
                  assign "2" to FACount
              }
              else {
                  assign "1" to FACount
              }
                capture line:3, column:13, length:14 assign to TnFA2
          }
          capture line:4, column:5, length:2 assign to FA3
          if (FA3=="FA"){
              if (FACount=="2"){
                  assign "3" to FACount
              }
              else{
                  assign "2" to FACount
              }
                capture line:4, column:12, length:14 assign to TnFA3
          }
          if (FA3=="FH"){
            if (FACount=="2"){
                  assign "3" to FACount
              }
              else{
                  assign "2" to FACount
              }
                capture line:4, column:13, length:14 assign to TnFA3
          }
          capture line:5, column:5, length:2 assign to FA4
          if (FA4=="FA"){
                if (FACount=="3"){
                  assign "4" to FACount
                }
                else{
                  assign "3" to FACount
                }
                  capture line:5, column:12, length:14 assign to TnFA4
          }
          if (FA4=="FH"){
            if (FACount=="3"){
                  assign "4" to FACount
                }
                else{
                  assign "3" to FACount
                }
                capture line:5, column:13, length:14 assign to TnFA4
          }
          capture line:6, column:5, length:2 assign to FA5
          if (FA5=="FA"){
                if (FACount=="4"){
                  assign "5" to FACount
                }
                else{
                  assign "4" to FACount
                }
                    capture line:6, column:12, length:14 assign to TnFA5
          }
          if (FA5=="FH"){
            if (FACount=="4"){
                  assign "5" to FACount
                }
                else{
                  assign "4" to FACount
                }
                capture line:6, column:13, length:14 assign to TnFA5
          }
          capture line:7, column:5, length:2 assign to FA6
          if (FA6=="FA"){
                if (FACount=="5"){
                  assign "6" to FACount
                }
                else{
                  assign "5" to FACount
                }
                    capture line:7, column:12, length:14 assign to TnFA6
          }
          if (FA6=="FH"){
            if (FACount=="5"){
                  assign "6" to FACount
                }
                else{
                  assign "5" to FACount
                }
                      capture line:7, column:13, length:14 assign to TnFA6
          }
          capture line:8, column:5, length:2 assign to FA7
          if (FA7=="FA"){
                if (FACount=="6"){
                  assign "7" to FACount
                }
                else{
                  assign "6" to FACount
                }
                    capture line:8, column:12, length:14 assign to TnFA7
          }
          if (FA7=="FH"){
             if (FACount=="6"){
                  assign "7" to FACount
                }
                else{
                  assign "6" to FACount
                }
            capture line:8, column:13, length:14 assign to TnFA7
          }
          capture line:9, column:5, length:2 assign to FA8
          if (FA8=="FA"){
                if (FACount=="7"){
                    assign "8" to FACount
                }
                else{
                  assign "7" to FACount
                }
                    capture line:9, column:12, length:14 assign to TnFA8
          }
          if (FA8=="FH"){
            if (FACount=="7"){
                    assign "8" to FACount
                }
                else{
                  assign "7" to FACount
                }
            capture line:9, column:13, length:14 assign to TnFA8
          }
          capture line:10, column:5, length:2 assign to FA9
          if (FA9=="FA"){
              if (FACount=="8"){
                  assign "9" to FACount
              }
              else{
                assign "8" to FACount
              }
                 capture line:10, column:12, length:14 assign to TnFA9
          }
          if (FA9=="FH"){
            if (FACount=="8"){
                  assign "9" to FACount
              }
              else{
                assign "8" to FACount
              }
            capture line:10, column:13, length:14 assign to TnFA9
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
                 capture line:11, column:12, length:14 assign to TnFA10
          }
          if (FA10=="FH"){
            if (FACount=="9"){
                  send "More than 9 FA"
                  mandatory ask "Please continue manually as there're more than 9 FA(s)" assign to qz5
                  send "ig"
              }
              else{
                  assign "9" to FACount
              }
            capture line:11, column:13, length:14 assign to TnFA10
          }
          
          
assign TnFA1 to TFAOpen   
send "TWD/TKT" +TFAOpen

capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA2 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA3 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA4 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA5 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA6 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA7 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA8 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA9 to TFAOpen
  send "TWD/TKT" +TFAOpen
}
capture line:3, column:32, length:3 assign to PAXST
if (PAXST=="INF"){
  assign TnFA10 to TFAOpen
  send "TWD/TKT" +TFAOpen
}


    capture line:2, column:44, length:5 assign to DOITEST
  if (DOITEST == today){
    send "No refund today just Void!"
    mandatory ask "Please continue with FO SmartFlow" assign to qz5
  }
    capture line:2, column:57, length:8 assign to ticketingOffice

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

if (Bg2 ==""){
    assign "0p" to Bg2
}
if (Bg2 =="NO"){
    assign "0p" to Bg2
}
if (Bg2 =="0 "){
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

if (Bg4 ==""){
    assign "0p" to Bg4
}
if (Bg4 =="NO"){
    assign "0p" to Bg4
}
if (Bg4 =="0 "){
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

if (Bg6 ==""){
    assign "0p" to Bg6
}
if (Bg6 =="NO"){
    assign "0p" to Bg6
}
if (Bg6 =="0 "){
    assign "0P" to Bg6
}

assign " " to ref62
          //FXR/k/R,U,UP,U*SEE24,U*MOS05
          if (thisOfficeName == "RUHAA2162"){
            assign ",*RF" to ref62
          }
          if (Airline1 =="SM"){
            append ",U09" to ref62
          }
          send "FXR/K/R,U,UP,U*SEE24,U*MOS05"+ref62

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

if (FACountStart =="0"){
      send "There's no FA!"
      mandatory ask "please continue manually!" assign to qz5
}
if (FACountStart =="1"){
    if (FACount>0){
        send "SRT" +TnFA1
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA1
    }
    if (FACount>1){
        send "SRT" +TnFA2
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA2
    }
    if (FACount>2){
        send "SRT" +TnFA3
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA3
    }
    if (FACount>3){
        send "SRT" +TnFA4
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA4
    }
    if (FACount>4){
        send "SRT" +TnFA5
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA5
    }
    if (FACount>5){
        send "SRT" +TnFA6
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA6
    }
    if (FACount>6){
        send "SRT" +TnFA7
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA7
    }
    if (FACount>7){
        send "SRT" +TnFA8
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA8
    }
    if (FACount>8){
        send "SRT" +TnFA9
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA9
    }
}
if (FACountStart =="2"){
    if (FACount>0){
        send "SRT" +TnFA2
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA2
    }
    if (FACount>1){
        send "SRT" +TnFA3
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA3
    }
    if (FACount>2){
        send "SRT" +TnFA4
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA4
    }
    if (FACount>3){
        send "SRT" +TnFA5
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA5
    }
    if (FACount>4){
        send "SRT" +TnFA6
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA6
    }
    if (FACount>5){
        send "SRT" +TnFA7
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA7
    }
    if (FACount>6){
        send "SRT" +TnFA8
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA8
    }
    if (FACount>7){
        send "SRT" +TnFA9
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA9
    }
    if (FACount>8){
        send "SRT" +TnFA10
        call "z_After_Void_RF"
        capture line:1, column:32, length:10 assign to TRFA10
    }
}

if (FACountStart =="1"){
    assign "" to Count
    if (FACount>0){
      append TRFA1 to Count
    }
    if (FACount>1){
      append ";" +TRFA2 to Count
    }
    if (FACount>2){
      append ";" +TRFA3 to Count
    }
    if (FACount>3){
      append ";" +TRFA4 to Count
    }
    if (FACount>4){
      append ";" +TRFA5 to Count
    }
    if (FACount>5){
      append ";" +TRFA6 to Count
    }
    if (FACount>6){
      append ";" +TRFA7 to Count
    }
    if (FACount>7){
      append ";" +TRFA8 to Count
    }
    if (FACount>8){
      append ";" +TRFA9 to Count
    }
}
if (FACountStart =="2"){
    assign "" to Count
    if (FACount>0){
        append TRFA2 to Count
    }
    if (FACount>1){
      append ";" +TRFA3 to Count
    }
    if (FACount>2){
       append ";" +TRFA4 to Count
    }
    if (FACount>3){
        append ";" +TRFA5 to Count
    }
    if (FACount>4){
        append ";" +TRFA6 to Count
    }
    if (FACount>5){
        append ";" +TRFA7 to Count
    }
    if (FACount>6){
        append ";" +TRFA8 to Count
    }
    if (FACount>7){
        append ";" +TRFA9 to Count
    }
    if (FACount>8){
        append ";" +TRFA10 to Count
    }
}
send "" +TnFA1 +";" +TnFA2 +";" +TnFA3 +";" +TnFA4
send "" +FACount +";" +FACountStart
send "df" +Count +"-" +totalNewPrice