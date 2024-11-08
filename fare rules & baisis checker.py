ask "Enter the Ticket Number:(With or Without TWD/TKT)" assign to TicketNumber

send "ig"
send "SRT" +TicketNumber
capture line:1, column:32, length:1 assign to ch1
capture line:1, column:33, length:1 assign to ch2
capture line:1, column:34, length:1 assign to ch3
capture line:1, column:35, length:1 assign to ch4
capture line:1, column:36, length:1 assign to ch5
capture line:1, column:37, length:1 assign to ch6
capture line:1, column:38, length:1 assign to ch7
capture line:1, column:39, length:1 assign to ch8
capture line:1, column:40, length:1 assign to ch9
capture line:1, column:41, length:1 assign to ch10
capture line:1, column:42, length:1 assign to ch11
capture line:1, column:43, length:1 assign to ch12
capture line:1, column:44, length:1 assign to ch13
capture line:1, column:45, length:1 assign to ch14
capture line:1, column:46, length:1 assign to ch15
capture line:1, column:47, length:1 assign to ch16
capture line:1, column:48, length:1 assign to ch17
capture line:1, column:49, length:1 assign to ch18
capture line:1, column:50, length:1 assign to ch19
capture line:1, column:51, length:1 assign to ch20
capture line:1, column:52, length:1 assign to ch21
capture line:1, column:53, length:1 assign to ch22
capture line:1, column:54, length:1 assign to ch23
capture line:1, column:55, length:1 assign to ch24
capture line:1, column:56, length:1 assign to ch25
capture line:1, column:57, length:1 assign to ch26
capture line:1, column:58, length:1 assign to ch27
capture line:1, column:59, length:1 assign to ch28
capture line:1, column:60, length:1 assign to ch29
capture line:1, column:61, length:1 assign to ch30

assign "" to tktNo
if (ch4 == "-"){
  append ch1 +ch2 +ch3 +ch4 +ch5 +ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 to tktNo
}
if (ch5 == "-"){
  append ch2 +ch3 +ch4 +ch5 +ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 to tktNo
}
if (ch6 == "-"){
  append ch3 +ch4 +ch5 +ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 to tktNo
}
if (ch7 == "-"){
  append ch4 +ch5 +ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 to tktNo
}
if (ch8 == "-"){
  append ch5 +ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 to tktNo
}
if (ch9 == "-"){
  append ch6 +ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 to tktNo
}
if (ch10 == "-"){
  append ch7 +ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 to tktNo
}
if (ch11 == "-"){
  append ch8 +ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 to tktNo
}
if (ch12 == "-"){
  append ch9 +ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 to tktNo
}
if (ch13 == "-"){
  append ch10 +ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 to tktNo
}
if (ch14 == "-"){
  append ch11 +ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 to tktNo
}
if (ch15 == "-"){
  append ch12 +ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 to tktNo
}
if (ch16 == "-"){
  append ch13 +ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 +ch26 to tktNo
}
if (ch17 == "-"){
  append ch14 +ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 +ch26 +ch27 to tktNo
}
if (ch18 == "-"){
  append ch15 +ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 +ch26 +ch27 +ch28 to tktNo
}
if (ch19 == "-"){
  append ch16 +ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 +ch26 +ch27 +ch28 +ch29 to tktNo
}
if (ch20 == "-"){
  append ch17 +ch18 +ch19 +ch20 +ch21 +ch22 +ch23 +ch24 +ch25 +ch26 +ch27 +ch28 +ch29 +ch30 to tktNo
}
send "TWD/TKT" +tktNo
if (TKTCheck !="TKT"){
  ask "Try again!" assign to qz5
  call "FQD&FQP"
}

capture line:1, column:5, length:1 assign to TKTP1
capture line:1, column:6, length:2 assign to TKTP2
capture line:1, column:8, length:10 assign to TKTP3

capture line:2, column:44, length:7 assign to DOI

capture line:4, column:4, length:1 assign to original1
capture line:4, column:5, length:3 assign to city1
capture line:4, column:9, length:2 assign to airline1
capture line:4, column:18, length:1 assign to class1
capture line:4, column:20, length:5 assign to travelDate1
capture line:4, column:30, length:2 assign to OK1
capture line:4, column:33, length:12 assign to fareBasis1
capture line:4, column:47, length:1 assign to status1

capture line:5, column:4, length:1 assign to original2  
capture line:5, column:5, length:3 assign to city2
capture line:5, column:9, length:2 assign to airline2
capture line:5, column:18, length:1 assign to class2
capture line:5, column:20, length:5 assign to travelDate2
capture line:5, column:30, length:2 assign to OK2
capture line:5, column:33, length:12 assign to fareBasis2
capture line:5, column:47, length:1 assign to status2

capture line:6, column:4, length:1 assign to original3
capture line:6, column:5, length:3 assign to city3
capture line:6, column:9, length:2 assign to airline3
capture line:6, column:18, length:1 assign to class3
capture line:6, column:20, length:5 assign to travelDate3
capture line:6, column:30, length:2 assign to OK3
capture line:6, column:33, length:12 assign to fareBasis3
capture line:6, column:47, length:1 assign to status3

capture line:7, column:4, length:1 assign to original4
capture line:7, column:5, length:3 assign to city4
capture line:7, column:9, length:2 assign to airline4
capture line:7, column:18, length:1 assign to class4
capture line:7, column:20, length:5 assign to travelDate4
capture line:7, column:30, length:2 assign to OK4
capture line:7, column:33, length:12 assign to fareBasis4
capture line:7, column:47, length:1 assign to status4

capture line:8, column:4, length:1 assign to original5
capture line:8, column:5, length:3 assign to city5
capture line:8, column:9, length:2 assign to airline5
capture line:8, column:18, length:1 assign to class5
capture line:8, column:20, length:5 assign to travelDate5
capture line:8, column:30, length:2 assign to OK5
capture line:8, column:33, length:12 assign to fareBasis5
capture line:8, column:47, length:1 assign to status5

capture line:9, column:4, length:1 assign to original6
capture line:9, column:5, length:3 assign to city6
capture line:9, column:9, length:2 assign to airline6
capture line:9, column:18, length:1 assign to class6
capture line:9, column:20, length:5 assign to travelDate6
capture line:9, column:30, length:2 assign to OK6
capture line:9, column:33, length:12 assign to fareBasis6
capture line:9, column:47, length:1 assign to status6

capture line:10, column:5, length:3 assign to city7

// Searching for Gov
capture line:8, column:4, length:3 assign to gov1
capture line:8, column:5, length:3 assign to gov11
capture line:9, column:4, length:3 assign to gov2
capture line:9, column:5, length:3 assign to gov22
capture line:10, column:4, length:3 assign to gov3
capture line:10, column:5, length:3 assign to gov33
capture line:11, column:4, length:3 assign to gov4
capture line:11, column:5, length:3 assign to gov44
capture line:12, column:4, length:3 assign to gov5
capture line:12, column:5, length:3 assign to gov55
capture line:13, column:4, length:3 assign to gov6
capture line:13, column:5, length:3 assign to gov66
capture line:14, column:4, length:3 assign to gov7
capture line:14, column:5, length:3 assign to gov77
capture line:15, column:4, length:3 assign to gov8
capture line:15, column:5, length:3 assign to gov88
capture line:16, column:4, length:3 assign to gov9
capture line:16, column:5, length:3 assign to gov99
capture line:17, column:4, length:3 assign to gov10
capture line:17, column:5, length:3 assign to gov1010
capture line:18, column:4, length:3 assign to gov11
capture line:18, column:5, length:3 assign to gov1111
capture line:19, column:4, length:3 assign to gov12
capture line:19, column:5, length:3 assign to gov1212
capture line:20, column:4, length:3 assign to gov13
capture line:20, column:5, length:3 assign to gov1313
capture line:21, column:4, length:3 assign to gov14
capture line:21, column:5, length:3 assign to gov1414
capture line:22, column:4, length:3 assign to gov15
capture line:22, column:5, length:3 assign to gov1515
capture line:23, column:4, length:3 assign to gov16
capture line:23, column:5, length:3 assign to gov1616

if (gov1 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov11 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov2 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov22 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov3 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov33 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov4 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov44 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov5 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov55 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov6 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov66 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov7 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov77 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov8 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov88 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov9 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov99 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov10 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1010 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov11 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1111 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov12 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1212 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov13 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1313 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov14 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1414 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov15 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1515 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov16 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}
if (gov1616 =="GOV"){
  send "Governmental Ticket ignore it!"
  mandatory ask "Ignore?" assign to qz5
}

  
choose "FQP or FQD?"{
  when ("FQD"){
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC"
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="REFUND RECORD PENDING"){
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC"
}
capture line:1, column:34, length:3 assign to checkRFND
if (checkRFND!="AGT"){
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3
}

if (OK1 =="OK"){
  if (status1=="O"){
    if (original1=="O"){
      assign "TRUE" to checkOpen1
    }
  }
  if (status1=="S"){
    if (original1=="O"){
      assign "TRUE" to checkOpen1
    }
  }
  assign "1" to segCount
}

if (OK2 =="OK"){
  if (status2=="O"){
    if (original2=="O"){
      assign "TRUE" to checkOpen2
    }
  }
  if (status2=="S"){
    if (original2=="O"){
      assign "TRUE" to checkOpen2
    }
  }
  assign "2" to segCount
}

if (OK3 =="OK"){
  if (status3=="O"){
    if (original3=="O"){
      assign "TRUE" to checkOpen3
    }
  }
  if (status3=="S"){
    if (original3=="O"){
      assign "TRUE" to checkOpen3
    }
  }
  assign "3" to segCount
}

if (OK4 =="OK"){
  if (status4=="O"){
    if (original4=="O"){
      assign "TRUE" to checkOpen4
    }
  }
  if (status4=="S"){
    if (original4=="O"){
      assign "TRUE" to checkOpen4
    }
  }
  assign "4" to segCount
}

if (OK5 =="OK"){
  if (status5=="O"){
    if (original5=="O"){
      assign "TRUE" to checkOpen5
    }
  }
  if (status5=="S"){
    if (original5=="O"){
      assign "TRUE" to checkOpen5
    }
  }
  assign "5" to segCount
}

if (OK6 =="OK"){
  if (status6=="O"){
    if (original6="O"){
      assign "TRUE" to checkOpen6
    }
  }
  if (status6=="S"){
    if (original6=="O"){
      assign "TRUE" to checkOpen6
    }
  }
  assign "6" to segCount
}

if (segCount=="6"){
    if (checkOpen6=="TRUE"){
      append "" +city6 +"/A" +airline1 +"/C" +class6 to FQDCommand
      assign fareBasis6 to fareBasis
    }
    else{
        if (checkOpen5=="TRUE"){
          append "" +city5 +"/A" +airline1 +"/C" +class5 to FQDCommand
          assign fareBasis5 to fareBasis
        }
        else{
          if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline1 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline1 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline1 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city7 +"/A" +airline1 +"/C" +class1 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
        }
    }
}

if (segCount=="5"){
  if (checkOpen5=="TRUE"){
          append "" +city5 +"/A" +airline1 +"/C" +class5 to FQDCommand
          assign fareBasis5 to fareBasis
        }
        else{
          if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline1 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline1 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline1 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city7 +"/A" +airline1 +"/C" +class1 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
     }
    
}

if (segCount=="4"){
    if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline1 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline1 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline1 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city5 +"/A" +airline1 +"/C" +class1 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
}

if (segCount=="3"){
   if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline1 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline1 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city4 +"/A" +airline1 +"/C" +class1 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
         }
    
}

if (segCount=="2"){
     if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline1 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city3 +"/A" +airline1 +"/C" +class1 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
}

if (segCount=="1"){
    append "" +city2 +"/A" +airline1 +"/C" +class1 to FQDCommand
    assign fareBasis1 to fareBasis
}

  send "FQD" +city1 +FQDCommand +"/R," +DOI +",U*SRG01,UP,P"


  capture line:4, column:1, length:2 assign to FQDN1
  capture line:5, column:1, length:2 assign to FQDN2
  capture line:6, column:1, length:2 assign to FQDN3
  capture line:7, column:1, length:2 assign to FQDN4
  capture line:8, column:1, length:2 assign to FQDN5
  capture line:9, column:1, length:2 assign to FQDN6
  capture line:10, column:1, length:2 assign to FQDN7
  capture line:11, column:1, length:2 assign to FQDN8
  capture line:12, column:1, length:2 assign to FQDN9
  capture line:13, column:1, length:2 assign to FQDN10
  capture line:14, column:1, length:2 assign to FQDN11
  capture line:15, column:1, length:2 assign to FQDN12
  capture line:16, column:1, length:2 assign to FQDN13
  capture line:17, column:1, length:2 assign to FQDN14
  capture line:18, column:1, length:2 assign to FQDN15
  capture line:19, column:1, length:2 assign to FQDN16
  capture line:20, column:1, length:2 assign to FQDN17

  capture line:4, column:4, length:12 assign to FQDFareRule1
  capture line:5, column:4, length:12 assign to FQDFareRule2
  capture line:6, column:4, length:12 assign to FQDFareRule3
  capture line:7, column:4, length:12 assign to FQDFareRule4
  capture line:8, column:4, length:12 assign to FQDFareRule5
  capture line:9, column:4, length:12 assign to FQDFareRule6
  capture line:10, column:4, length:12 assign to FQDFareRule7
  capture line:11, column:4, length:12 assign to FQDFareRule8
  capture line:12, column:4, length:12 assign to FQDFareRule9
  capture line:13, column:4, length:12 assign to FQDFareRule10
  capture line:14, column:4, length:12 assign to FQDFareRule11
  capture line:15, column:4, length:12 assign to FQDFareRule12
  capture line:16, column:4, length:12 assign to FQDFareRule13
  capture line:17, column:4, length:12 assign to FQDFareRule14
  capture line:18, column:4, length:12 assign to FQDFareRule15
  capture line:19, column:4, length:12 assign to FQDFareRule16
  capture line:20, column:4, length:12 assign to FQDFareRule17
  
  if (FQDFareRule1==fareBasis){
    send "FQN" +FQDN1 +"*PE"
  }
  if (FQDFareRule2==fareBasis){
    send "FQN" +FQDN2 +"*PE"
  }
  if (FQDFareRule3==fareBasis){
    send "FQN" +FQDN3 +"*PE"
  }
  if (FQDFareRule4==fareBasis){
    send "FQN" +FQDN4 +"*PE"
  }
  if (FQDFareRule5==fareBasis){
    send "FQN" +FQDN5 +"*PE"
  }
  if (FQDFareRule6==fareBasis){
    send "FQN" +FQDN6 +"*PE"
  }
  if (FQDFareRule7==fareBasis){
    send "FQN" +FQDN7 +"*PE"
  }
  if (FQDFareRule8==fareBasis){
    send "FQN" +FQDN8 +"*PE"
  }
  if (FQDFareRule9==fareBasis){
    send "FQN" +FQDN9 +"*PE"
  }
  if (FQDFareRule10==fareBasis){
    send "FQN" +FQDN10 +"*PE"
  }
  if (FQDFareRule11==fareBasis){
    send "FQN" +FQDN11 +"*PE"
  }
  if (FQDFareRule12==fareBasis){
    send "FQN" +FQDN12 +"*PE"
  }
  if (FQDFareRule13==fareBasis){
    send "FQN" +FQDN13 +"*PE"
  }
  if (FQDFareRule14==fareBasis){
    send "FQN" +FQDN14 +"*PE"
  }
  if (FQDFareRule15==fareBasis){
    send "FQN" +FQDN15 +"*PE"
  }
  if (FQDFareRule16==fareBasis){
    send "FQN" +FQDN16 +"*PE"
  }
  if (FQDFareRule17==fareBasis){
    send "FQN" +FQDN17 +"*PE"
  }

  }
  when ("FQP"){
    if (OK1=="OK"){
     if (status1!="O"){
      append "" +city1 +"/A" +airline1 +"/C" +class1 +"/D" +travelDate1 +city2  to FQPCommand
    }
    }
    if (OK2=="OK"){
    if (status2!="O"){
        append "/A" +airline2 +"/C" +class2 +"/D" +travelDate2 +city3 to FQPCommand
    }
    }
    if (OK3=="OK"){
    if (status3!="O"){
        append "/A" +airline3 +"/C" +class3 +"/D" +travelDate3 +city4 to FQPCommand
    }
    }
    if (OK4=="OK"){
    if (status4!="O"){
        append "/A" +airline4 +"/C" +class4 +"/D" +travelDate4 +city5 to FQPCommand
    }
    }
    if (OK5=="OK"){
    if (status5!="O"){
        append "/A" +airline5 +"/C" +class5 +"/D" +travelDate5 +city6 to FQPCommand
    }
    }
    if (OK6=="OK"){
    if (status6!="O"){
        append "/A" +airline6 +"/C" +class6 +"/D" +travelDate6 +city7 to FQPCommand
    }
    }

    send "FQP" +FQPCommand +"/R," +DOI +",U*SRG01,UP"
    
        
  }
}
  



