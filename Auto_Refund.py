// Auto_Refund

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
capture line:1, column:1, length:3 assign to TKTCheck
if (TKTCheck !="TKT"){
  ask "Try again!" assign to qz5
  call "Auto_Refund"
}

capture line:1, column:5, length:1 assign to TKTP1
capture line:1, column:6, length:2 assign to TKTP2
capture line:1, column:8, length:10 assign to TKTP3

capture line:1, column:59, length:6 assign to Ticket_PNR

capture line:2, column:44, length:5 assign to DDMMM_DOI
capture line:2, column:49, length:2 assign to YY_DOI
capture line:2, column:57, length:8 assign to PCC_ID


capture line:3, column:6, length:25 assign to PAXNAME
capture line:3, column:31, length:1 assign to PAXNAME_ExtraCheck
capture line:3, column:32, length:3 assign to PTC

capture line:4, column:4, length:1 assign to original1
capture line:4, column:5, length:3 assign to city1
capture line:4, column:9, length:2 assign to airline1
capture line:4, column:11, length:4 assign to flightNo1
capture line:4, column:18, length:1 assign to class1
capture line:4, column:20, length:5 assign to travelDate1
capture line:4, column:30, length:2 assign to OK1
capture line:4, column:33, length:4 assign to fareBasis1_Shortcut
capture line:4, column:33, length:8 assign to fareBasis1
capture line:4, column:47, length:1 assign to status1

capture line:5, column:4, length:1 assign to original2  
capture line:5, column:5, length:3 assign to city2
capture line:5, column:9, length:2 assign to airline2
capture line:5, column:11, length:4 assign to flightNo2
capture line:5, column:18, length:1 assign to class2
capture line:5, column:20, length:5 assign to travelDate2
capture line:5, column:30, length:2 assign to OK2
capture line:5, column:33, length:8 assign to fareBasis2
capture line:5, column:47, length:1 assign to status2

capture line:6, column:4, length:1 assign to original3
capture line:6, column:5, length:3 assign to city3
capture line:6, column:9, length:2 assign to airline3
capture line:6, column:11, length:4 assign to flightNo3
capture line:6, column:18, length:1 assign to class3
capture line:6, column:20, length:5 assign to travelDate3
capture line:6, column:30, length:2 assign to OK3
capture line:6, column:33, length:8 assign to fareBasis3
capture line:6, column:47, length:1 assign to status3

capture line:7, column:4, length:1 assign to original4
capture line:7, column:5, length:3 assign to city4
capture line:7, column:9, length:2 assign to airline4
capture line:7, column:11, length:4 assign to flightNo4
capture line:7, column:18, length:1 assign to class4
capture line:7, column:20, length:5 assign to travelDate4
capture line:7, column:30, length:2 assign to OK4
capture line:7, column:33, length:8 assign to fareBasis4
capture line:7, column:47, length:1 assign to status4

capture line:8, column:4, length:1 assign to original5
capture line:8, column:5, length:3 assign to city5
capture line:8, column:9, length:2 assign to airline5
capture line:8, column:11, length:4 assign to flightNo5
capture line:8, column:18, length:1 assign to class5
capture line:8, column:20, length:5 assign to travelDate5
capture line:8, column:30, length:2 assign to OK5
capture line:8, column:33, length:8 assign to fareBasis5
capture line:8, column:47, length:1 assign to status5

capture line:9, column:4, length:1 assign to original6
capture line:9, column:5, length:3 assign to city6
capture line:9, column:9, length:2 assign to airline6
capture line:9, column:11, length:4 assign to flightNo6
capture line:9, column:18, length:1 assign to class6
capture line:9, column:20, length:5 assign to travelDate6
capture line:9, column:30, length:2 assign to OK6
capture line:9, column:33, length:8 assign to fareBasis6
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


ask "Continue?" assign to qz5

assign "" to checkNP
if (PCC_ID =="71201675"){
  assign "/T-NP" to checkNP
}

// Checking DOI that's not paased
send "DD" +today + "/" +DOI
capture line:2, column:1, length:1 assign to checkDOIDays
assign "True" to ticket_2_Years_Validity

//Segments counter
assign "1" to segCount
if (OK2 == "OK"){
  assign "2" to segCount
  if (OK3 == "OK"){
    assign "3" to segCount
    if (OK4 == "OK"){
      assign "4" to segCount
      if (OK5 == "OK"){
        assign "5" to segCount
        if (OK6 == "OK"){
          assign "6" to segCount
        }
      }
    }
  }
}

if (PTC =="INF"){
if (OK2 == "NS"){
  assign "2" to segCount
  if (OK3 == "NS"){
    assign "3" to segCount
    if (OK4 == "NS"){
      assign "4" to segCount
      if (OK5 == "NS"){
        assign "5" to segCount
        if (OK6 == "NS"){
          assign "6" to segCount
        }
      }
    }
  }
}
}

if (checkDOIDays == "-"){
  capture line:2, column:2, length:4 assign to checkDOIDays
  assign "True" to ticket_2_Years_Validity
  if (segCount == "1"){
  if (Airline1 != "MS"){
    if (Airline1 != "EK"){
      if (Airline1 != "LH"){
        if (Airline1 != "BA"){
          if (Airline1 != "TK"){
            if (Airline1 != "SQ"){
              if (Airline1 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount == "2"){
  if (Airline2 != "MS"){
    if (Airline2 != "EK"){
      if (Airline2 != "LH"){
        if (Airline2 != "BA"){
          if (Airline2 != "TK"){
            if (Airline2 != "SQ"){
              if (Airline2 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount == "3"){
  if (Airline3 != "MS"){
    if (Airline3 != "EK"){
      if (Airline3 != "LH"){
        if (Airline3 != "BA"){
          if (Airline3 != "TK"){
            if (Airline3 != "SQ"){
              if (Airline3 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount == "4"){
  if (Airline4 != "MS"){
    if (Airline4 != "EK"){
      if (Airline4 != "LH"){
        if (Airline4 != "BA"){
          if (Airline4 != "TK"){
            if (Airline4 != "SQ"){
              if (Airline4 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount == "5"){
  if (Airline5 != "MS"){
    if (Airline5 != "EK"){
      if (Airline5 != "LH"){
        if (Airline5 != "BA"){
          if (Airline5 != "TK"){
            if (Airline5 != "SQ"){
              if (Airline5 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount == "6"){
  if (Airline6 != "MS"){
    if (Airline6 != "EK"){
      if (Airline6 != "LH"){
        if (Airline6 != "BA"){
          if (Airline6 != "TK"){
            if (Airline6 != "SQ"){
              if (Airline6 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }
  
  if (ticket_2_Years_Validity != "True"){
    if (checkDOIDays > "364"){
      send "THIS TICKET IS NOT VALID FOR REFUND! Expired Ticket!"
      mandatory ask "The Ticket is not valid for auto refund!, Please void it" assign to qz5
      call "Auro_refund"
    }
  }
  else{
    if (checkDOIDays > "728"){
      send "THIS TICKET IS NOT VALID FOR REFUND! Expired Ticket!"
      mandatory ask "The Ticket is not valid for auto refund!, Please void it" assign to qz5
      call "Auro_refund"
    }
  }

}
else{
  send "THIS TICKET IS NOT VALID FOR REFUND!, please void it!"
  mandatory ask "The Ticket is not valid for auto refund!, Please void it" assign to qz5
  call "Auro_refund"
}


// Check each sgement status
assign "True" to segment1_General_Status_Open
if (status1 != "O"){
  if (status1 != "A"){
    if (status1 != "S"){
      if (status1 != "U"){
        assign "False" to segment1_General_Status_Open
      }
    }
  }
}

if (segCount =="2"){
assign "True" to segment2_General_Status_Open
if (status2 != "O"){
  if (status2 != "A"){
    if (status2 != "S"){
      if (status2 != "U"){
        assign "False" to segment2_General_Status_Open
      }
    }
  }
}
}

if (segCount =="3"){
assign "True" to segment3_General_Status_Open
if (status3 != "O"){
  if (status3 != "A"){
    if (status3 != "S"){
      if (status3 != "U"){
        assign "False" to segment3_General_Status_Open
      }
    }
  }
}
}

if (segCount =="4"){
assign "True" to segment4_General_Status_Open
if (status4 != "O"){
  if (status4 != "A"){
    if (status4 != "S"){
      if (status4 != "U"){
        assign "False" to segment4_General_Status_Open
      }
    }
  }
}
}

if (segCount =="5"){
assign "True" to segment5_General_Status_Open
if (status5 != "O"){
  if (status5 != "A"){
    if (status5 != "S"){
      if (status5 != "U"){
        assign "False" to segment5_General_Status_Open
      }
    }
  }
}
}

if (segCount =="6"){
assign "True" to segment6_General_Status_Open
if (status6 != "O"){
  if (status6 != "A"){
    if (status6 != "S"){
      if (status6 != "U"){
        assign "False" to segment6_General_Status_Open
      }
    }
  }
}
}



//check No-Show for each segment
assign "True" to status_NoShow

if (segment1_General_Status_Open == "True"){
  if (travelDate1 != ""){
  assign travelDate1 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM 
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }

  }
}else{
  if (segCount > "1"){
  if (segment2_General_Status_Open == "True"){
  if (travelDate2 != ""){
  assign travelDate2 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }

  }
}else{
  if (segCount > "2"){
  if (segment3_General_Status_Open == "True"){
  if (travelDate3 != ""){
  assign travelDate3 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  
  }
}else{
  if (segCount > "3"){
  if (segment4_General_Status_Open == "True"){
  if (travelDate4 != ""){
  assign travelDate4 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  
  }
}else{
  if (segCount > "4"){
  if (segment5_General_Status_Open == "True"){
  if (travelDate5 != ""){
  assign travelDate5 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  
  }
}else{
  if (segCount > "5"){
  if (segment6_General_Status_Open == "True"){
  if (travelDate6 != ""){
  assign travelDate6 to open_TravelDDMMM
  send "DD" +DDMMM_DOI +"/" +open_TravelDDMMM
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
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

 send "DD" +today +"/" +open_TravelDDMMM +travelYY
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After != "-"){
    capture line:2, column:2, length:3 assign to check_Before_After
    if (check_Before_After > "2"){
      choose "This is a Future Ticket, Do you want to continue?" until "Yes" {
        when "No"{}
      }
      assign "False" to status_NoShow
    }
    else{
      choose "This Ticket is within No-Show, Do you want to continue as:"{
        when "No-Show"{}
        when "Normal"{assign "Normal" to status_NoShow}
      }
    }
  }

  // Check Out Of Sequence Scenarios & Origanl destinations
  assign "True" to Out_of_Sequence
  assign "False" to Originals
  if (segCount == "1"){
    if (segment1_General_Status_Open == "True"){
      if (original1 == "O"){
        assign "False" to Out_of_Sequence
        assign "True" to Originals
      }
    }  
  }

  if (segCount == "2"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (original1 == "O"){
          assign "False" to Out_of_Sequence
          assign "True" to Originals
        }
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open == "True"){
        if (original2 == "O"){
          assign "False" to Out_of_Sequence
          assign "True" to Originals
        }
      }
    }
  }

  if (segCount == "3"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (original1 == "O"){
            assign "False" to Out_of_Sequence
            assign "True" to Originals
          }
          else{
            if (original2 == "O"){
              assign "False" to Out_of_Sequence
              assign "True" to Originals
            }
            else {
              if (original3 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
            }
          }
        }
      }
      if (segment1_General_Status_Open != "True"){
        if (segment2_General_Status_Open == "True"){
          if (segment3_General_Status_Open == "True"){
            if (original2 == "O"){
              assign "False" to Out_of_Sequence
              assign "True" to Originals
            }
            else {
              if (original3 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
            }
          }
        }
      }
      if (segment1_General_Status_Open != "True"){
        if (segment2_General_Status_Open != "True"){
          if (segment3_General_Status_Open == "True"){
            if (original3 == "O"){
              assign "False" to Out_of_Sequence
              assign "True" to Originals
            }
          }
        }
      }
    }
  }

  if (segCount == "4"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (original1 == "O"){
              assign "False" to Out_of_Sequence
              assign "True" to Originals
            }
            else{
              if (original2 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
              else {
                if (original3 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original4 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                  }
                }
              }
            }
          }
        }
      }
    }
        if (segment1_General_Status_Open != "True"){
          if (segment2_General_Status_Open == "True"){
            if (segment3_General_Status_Open == "True"){
              if (segment4_General_Status_Open == "True"){
                if (original2 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original3 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original4 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                  }
                }
              }
            }
          }
        } 
        if (segment1_General_Status_Open != "True"){
          if (segment2_General_Status_Open != "True"){
            if (segment3_General_Status_Open == "True"){
              if (segment4_General_Status_Open == "True"){
                if (original3 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original4 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                }
              } 
            } 
          } 
        } 
      if (segment1_General_Status_Open != "True"){
        if (segment2_General_Status_Open != "True"){
          if (segment3_General_Status_Open != "True"){
            if (segment4_General_Status_Open == "True"){
              if (original4 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
            } 
          } 
        } 
      }
  }

  if (segCount == "5"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (original1 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
              else{
                if (original2 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original3 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original4 == "O"){
                      assign "False" to Out_of_Sequence
                    assign "True" to Originals
                    }
                    else {
                      if (original5 == "O"){
                        assign "False" to Out_of_Sequence
                        assign "True" to Originals
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
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (original2 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
              else {
                if (original3 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original4 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original5 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (original3 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
              else {
                if (original4 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original5 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                }
              }
            } 
          } 
        } 
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open != "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (original4 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
              else {
                if (original5 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
              }
            } 
          } 
        } 
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open != "True"){
          if (segment4_General_Status_Open != "True"){
            if (segment5_General_Status_Open == "True"){
              if (original5 == "O"){
                assign "False" to Out_of_Sequence
                assign "True" to Originals
              }
            } 
          } 
        } 
      }
    }
  }

  if (segCount == "6"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (segment6_General_Status_Open == "True"){
                if (original1 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else{
                  if (original2 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original3 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                    else {
                      if (original4 == "O"){
                        assign "False" to Out_of_Sequence
                        assign "True" to Originals
                      }
                      else {
                        if (original5 == "O"){
                          assign "False" to Out_of_Sequence
                          assign "True" to Originals
                        }
                        else {
                          if (original6 == "O"){
                            assign "False" to Out_of_Sequence
                            assign "True" to Originals
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
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (segment6_General_Status_Open == "True"){
                if (original2 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original3 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original4 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                    else {
                      if (original5 == "O"){
                        assign "False" to Out_of_Sequence
                        assign "True" to Originals
                      }
                      else {
                        if (original6 == "O"){
                          assign "False" to Out_of_Sequence
                          assign "True" to Originals
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
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (segment6_General_Status_Open == "True"){
                if (original3 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original4 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original5 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                    else {
                      if (original6 == "O"){
                        assign "False" to Out_of_Sequence
                        assign "True" to Originals
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
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open != "True"){
          if (segment4_General_Status_Open == "True"){
            if (segment5_General_Status_Open == "True"){
              if (segment6_General_Status_Open == "True"){
                if (original4 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original5 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                  else {
                    if (original6 == "O"){
                      assign "False" to Out_of_Sequence
                      assign "True" to Originals
                    }
                  }
                }
              } 
            } 
          } 
        } 
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open != "True"){
          if (segment4_General_Status_Open != "True"){
            if (segment5_General_Status_Open == "True"){
              if (segment6_General_Status_Open == "True"){
                if (original5 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
                else {
                  if (original6 == "O"){
                    assign "False" to Out_of_Sequence
                    assign "True" to Originals
                  }
                }
              } 
            } 
          } 
        } 
      }
    }
    if (segment1_General_Status_Open != "True"){
      if (segment2_General_Status_Open != "True"){
        if (segment3_General_Status_Open != "True"){
          if (segment4_General_Status_Open != "True"){
            if (segment5_General_Status_Open != "True"){
              if (segment6_General_Status_Open == "True"){
                if (original6 == "O"){
                  assign "False" to Out_of_Sequence
                  assign "True" to Originals
                }
              } 
            } 
          } 
        } 
      }
    }
  }


if (Out_of_Sequence == "True"){
  send "THIS TICKET IS NOT VALID FOR REFUND! Out of Sequence!"
  mandatory ask "The Ticket is not valid for auto refund!, Please Ignore it" assign to qz5
  call "Auto_Refund"
}



// Check if the ticket is  valid for ATC-refund
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC"

capture line:1, column:34, length:3 assign to checkRFND
capture line:1, column:58, length:1 assign to checkATC
assign "False" to ATC_Refund_Eligible
if (checkRFND=="AGT"){
  if (checkATC =="C"){
    assign "True" to ATC_Refund_Eligible
  }
  if (checkATC =="N"){
    assign "True" to ATC_Refund_Eligible
  }
}

if (ATC_Refund_Eligible =="True"){

    capture line:15, column:1, length:2 assign to FOCheck1
    capture line:16, column:1, length:2 assign to FOCheck2
    capture line:17, column:1, length:2 assign to FOCheck3

    if (FOCheck1=="FO"){
      assign "True" to FOCheck
      capture line:15, column:28, length:7 assign to FODate
    }
    if (FOCheck2=="FO"){
      assign "True" to FOCheck
      capture line:16, column:28, length:7 assign to FODate
    }
    if (FOCheck3=="FO"){
      assign "True" to FOCheck
      capture line:17, column:28, length:7 assign to FODate
    }

    capture line:10, column:5, length:12 assign to totalRefundcheck1
    capture line:11, column:5, length:12 assign to totalRefundcheck2
    capture line:12, column:5, length:12 assign to totalRefundcheck3

    if (totalRefundcheck1 == "REFUND TOTAL"){
        capture line:10, column:5, length:40 assign to totalRefundAmount
        capture line:10, column:30, length:13 assign to amountRefunded
    }
    if (totalRefundcheck2 == "REFUND TOTAL"){
        capture line:11, column:5, length:40 assign to totalRefundAmount
        capture line:11, column:30, length:13 assign to amountRefunded
    }
    if (totalRefundcheck3 == "REFUND TOTAL"){
        capture line:12, column:5, length:40 assign to totalRefundAmount
        capture line:12, column:30, length:13 assign to amountRefunded
    }
    capture line:6, column:28, length:3 assign to refundCurrency

    capture line:11, column:5, length:10 assign to checkCommission1
    capture line:12, column:5, length:10 assign to checkCommission2
    capture line:13, column:5, length:10 assign to checkCommission3

    assign  "         0.00" to commissionAmount

    if (checkCommission1 == "COMMISSION"){
        capture line:11, column:30, length:13 assign to commissionAmount
    }
    if (checkCommission2 == "COMMISSION"){
        capture line:12, column:30, length:13 assign to commissionAmount
    }
    if (checkCommission3 == "COMMISSION"){
        capture line:13, column:30, length:13 assign to commissionAmount
    }

    if (commissionAmount !="         0.00"){
      send "TRFU/FM0"
    }

    if (FOCheck == "True"){
        send "DD"
        capture line:2, column:33, length:7 assign to todayDate
        send "DD" +FODate +"/" +todayDate
        capture line:2, column:1, length:4 assign to dateDifference
        if (dateDifference >= "365"){
          mandatory ask "Original Ticket is Expired!" assign to qz5
          call "Auto_Refund"
        }
    }

    send "TRFU/NF"
    send "TRFP"
    capture line:2, column:1, length:21 assign to refundedTicketCheck
    if (refundedTicketCheck == "OK - REFUND PROCESSED"){
        send ":" +totalRefundAmount +"  " +refundCurrency
        call "Auto_Refund"
    }
    else{
        send "THIS TICKET IS NOT VALID FOR REFUND!"
        mandatory ask "The Ticket is not valid for auto refund!, Please Recheck it" assign to qz5
        call "Auto_Refund"
    }
}


// Working with Ghost Segments

  send "DD" +DDMMM_DOI +"/" +travelDate1
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }

 send "ss" +airline1 +flightNo1 +class1 +travelDate1 +travelYY +city1 +city2 +"GK1/0000 0200/RECLOC"


if (segCount > "1"){
  send "DD" +DDMMM_DOI +"/" +travelDate2
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  send "ss" +airline2 +flightNo2 +class2 +travelDate2 +travelYY +city2 +city3 +"GK1/0230 0500/RECLOC"
}

if (segCount > "2"){
  send "DD" +DDMMM_DOI +"/" +travelDate3
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  send "ss" +airline3 +flightNo3 +class3 +travelDate3 +travelYY +city3 +city4 +"GK1/0600 0900/RECLOC"
}

if (segCount > "3"){
  send "DD" +DDMMM_DOI +"/" +travelDate4
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  send "ss" +airline4 +flightNo4 +class4 +travelDate4 +travelYY +city4 +city5 +"GK1/0930 1200/RECLOC"
}

if (segCount > "4"){
  send "DD" +DDMMM_DOI +"/" +travelDate5
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  send "ss" +airline5 +flightNo5 +class5 +travelDate5 +travelYY +city5 +city6 +"GK1/1300 1600/RECLOC"
}

if (segCount > "5"){
  send "DD" +DDMMM_DOI +"/" +travelDate6
  capture line:2, column:1, length:1 assign to check_Before_After
  if (check_Before_After == "-"){
    send "DF" +YY_DOI +";1"
    capture line:2, column:1, length:2 assign to travelYY
  }
  else{
      assign YY_DOI to travelYY
  }
  send "ss" +airline6 +flightNo6 +class6 +travelDate6 +travelYY +city6 +city7 +"GK1/1700 2000/RECLOC"
}

assign "" to airline_TourCode
if (airline1 == "PR"){
  assign "U*C5YQ" to airline_TourCode
}
if (airline1 == "QR"){
  assign "U202201" to airline_TourCode
}
if (airline1 == "SM"){
  assign "U09" to airline_TourCode
}
if (airline1 == "SN"){
  assign "U385910" to airline_TourCode
}
if (airline1 == "SV"){
  assign "U*SEE24,U*MOS05" to airline_TourCode
}
if (airline1 == "WY"){
  assign "U584562" to airline_TourCode
}

  send "FXX/R," +DOI +",UP,U,P," +airline_TourCode
  
  capture line:4, column:1, length:2 assign to FXXN1
  capture line:5, column:1, length:2 assign to FXXN2
  capture line:6, column:1, length:2 assign to FXXN3
  capture line:7, column:1, length:2 assign to FXXN4
  capture line:8, column:1, length:2 assign to FXXN5
  capture line:9, column:1, length:2 assign to FXXN6
  capture line:10, column:1, length:2 assign to FXXN7
  capture line:11, column:1, length:2 assign to FXXN8
  capture line:12, column:1, length:2 assign to FXXN9
  capture line:13, column:1, length:2 assign to FXXN10
  capture line:14, column:1, length:2 assign to FXXN11
  capture line:15, column:1, length:2 assign to FXXN12
  capture line:16, column:1, length:2 assign to FXXN13
  capture line:17, column:1, length:2 assign to FXXN14
  capture line:18, column:1, length:2 assign to FXXN15
  capture line:19, column:1, length:2 assign to FXXN16
  capture line:20, column:1, length:2 assign to FXXN17

  capture line:4, column:4, length:4 assign to FXXFareRule1
  capture line:5, column:4, length:4 assign to FXXFareRule2
  capture line:6, column:4, length:4 assign to FXXFareRule3
  capture line:7, column:4, length:4 assign to FXXFareRule4
  capture line:8, column:4, length:4 assign to FXXFareRule5
  capture line:9, column:4, length:4 assign to FXXFareRule6
  capture line:10, column:4, length:4 assign to FXXFareRule7
  capture line:11, column:4, length:4 assign to FXXFareRule8
  capture line:12, column:4, length:4 assign to FXXFareRule9
  capture line:13, column:4, length:4 assign to FXXFareRule10
  capture line:14, column:4, length:4 assign to FXXFareRule11
  capture line:15, column:4, length:4 assign to FXXFareRule12
  capture line:16, column:4, length:4 assign to FXXFareRule13
  capture line:17, column:4, length:4 assign to FXXFareRule14
  capture line:18, column:4, length:4 assign to FXXFareRule15
  capture line:19, column:4, length:4 assign to FXXFareRule16
  capture line:20, column:4, length:4 assign to FXXFareRule17

  assign "False" to check_FareBasis_Compatibility
  if (FXXFareRule1 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN1 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "1" to FXXfareBasisNumber
    }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule2 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN2 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "2" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule3 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN3 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "3" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule4 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN4 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "4" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule5 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN5 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "5" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule6 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN6 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "6" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule7 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN7 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "7" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule8 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN8 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "8" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule9 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN9 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "9" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule10 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN10

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "10" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule11 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN11 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "11" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule12 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN12 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "12" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule13 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN13 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "13" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule14 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN14 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "14" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule15 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN15

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "15" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule16 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN16 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "16" to FXXfareBasisNumber
    }
  }
  }

  if (check_FareBasis_Compatibility == "False"){
    if (FXXFareRule17 == fareBasis1_Shortcut){
    assign "True" to check_FareBasis_Compatibility
    send "FQQ" +FXXN17 

    capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "17" to FXXfareBasisNumber
    }
  }
  }

 if (check_FareBasis_Compatibility == "False"){
  mandatory ask "Please Enter The FareRule No:" assign to FXX_test_FareRule_Number
  send "FQQ" +FXX_test_FareRule_Number
  capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign FXX_test_FareRule_Number to FXXfareBasisNumber
    }
 }

 if (check_FareBasis_Compatibility == "False"){
  mandatory ask "Please Enter The FareRule No:" assign to FXX_test_FareRule_Number
  send "FQQ" +FXX_test_FareRule_Number
  capture line:#, column:#, length:# assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:#, column:#, length:# assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:#, column:#, length:# assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:#, column:#, length:# assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:#, column:#, length:# assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:#, column:#, length:# assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "17" to FXXfareBasisNumber
    }
 }

  if (check_FareBasis_Compatibility == "False"){
    send "Can't Find The Fare Rule!"
    ask "Please Continue manually!" assign to fq5
  ``call "Auto_Refund"
 }

 // Supported Airlines (A3, AF, AH, AI, AT, BA, CX, DL, EK, ER, ET, EY, GF, J2, KL, KQ, KU, ME, MH, MS, MU, MS, NE, NP, PC, 
                    //  PK, PR, QR, RJ, SM, SQ, SV, TG, TK, TU, UJ, UL, VF, WY)

if (airline1 == "A3"){
 assign "True" to A3_Refundable
  if (class1 == "P"){
    assign "False" to A3_Refundable
  }
  if (class1 == "U"){
    assign "False" to A3_Refundable
  }
  if (class1 == "T"){
    assign "False" to A3_Refundable
  }
  if (class1 == "S"){
    assign "False" to A3_Refundable
  }

  if (segCount == "2"){
   if (class2 == "P"){
    assign "False" to A3_Refundable
  }
  if (class2 == "U"){
    assign "False" to A3_Refundable
  }
  if (class2 == "T"){
    assign "False" to A3_Refundable
  }
  if (class2 == "S"){
    assign "False" to A3_Refundable
  }
  }

  if (segCount == "3"){
  if (class3 == "P"){
    assign "False" to A3_Refundable
  }
  if (class3 == "U"){
    assign "False" to A3_Refundable
  }
  if (class3 == "T"){
    assign "False" to A3_Refundable
  }
  if (class3 == "S"){
    assign "False" to A3_Refundable
  }
  }

  if (segCount == "4"){
  if (class4 == "P"){
    assign "False" to A3_Refundable
  }
  if (class4 == "U"){
    assign "False" to A3_Refundable
  }
  if (class4 == "T"){
    assign "False" to A3_Refundable
  }
  if (class4 == "S"){
    assign "False" to A3_Refundable
  }
  }

  if (segCount == "5"){
  if (class5 == "P"){
    assign "False" to A3_Refundable
  }
  if (class5 == "U"){
    assign "False" to A3_Refundable
  }
  if (class5 == "T"){
    assign "False" to A3_Refundable
  }
  if (class5 == "S"){
    assign "False" to A3_Refundable
  }
  }

  if (segCount == "6"){
   if (class6 == "P"){
    assign "False" to A3_Refundable
  }
  if (class6 == "U"){
    assign "False" to A3_Refundable
  }
  if (class6 == "T"){
    assign "False" to A3_Refundable
  }
  if (class6 == "S"){
    assign "False" to A3_Refundable
  }
  }

  if (A3_Refundable == )
}



  when ("FQD"){
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
    if (original6=="O"){
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
      append "" +city6 +"/A" +airline6 +"/C" +class6 to FQDCommand
      assign fareBasis6 to fareBasis
    }
    else{
        if (checkOpen5=="TRUE"){
          append "" +city5 +"/A" +airline5 +"/C" +class5 to FQDCommand
          assign fareBasis5 to fareBasis
        }
        else{
          if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline4 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline3 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline2 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city7 +"/A" +airline6 +"/C" +class6 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
        }
    }
}

if (segCount=="5"){
  if (checkOpen5=="TRUE"){
          append "" +city5 +"/A" +airline5 +"/C" +class5 to FQDCommand
          assign fareBasis5 to fareBasis
        }
        else{
          if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline4 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline3 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline2 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city6 +"/A" +airline5 +"/C" +class5 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
     }
    
}

if (segCount=="4"){
    if (checkOpen4=="TRUE"){
            append "" +city4 +"/A" +airline4 +"/C" +class4 to FQDCommand
            assign fareBasis4 to fareBasis
          }
          else{
              if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline3 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline2 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city5 +"/A" +airline4 +"/C" +class4 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
              }
          }
}

if (segCount=="3"){
   if (checkOpen3=="TRUE"){
                append "" +city3 +"/A" +airline3 +"/C" +class3 to FQDCommand
                assign fareBasis3 to fareBasis
              }
              else{
                  if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline2 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city4 +"/A" +airline3 +"/C" +class3 to FQDCommand
                      assign fareBasis1 to fareBasis
                  }
         }
    
}

if (segCount=="2"){
     if (checkOpen2=="TRUE"){
                    append "" +city2 +"/A" +airline2 +"/C" +class2 to FQDCommand
                    assign fareBasis2 to fareBasis
                  }
                  else{
                      append "" +city3 +"/A" +airline2 +"/C" +class2 to FQDCommand
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

  capture line:4, column:4, length:8 assign to FQDFareRule1
  capture line:5, column:4, length:8 assign to FQDFareRule2
  capture line:6, column:4, length:8 assign to FQDFareRule3
  capture line:7, column:4, length:8 assign to FQDFareRule4
  capture line:8, column:4, length:8 assign to FQDFareRule5
  capture line:9, column:4, length:8 assign to FQDFareRule6
  capture line:10, column:4, length:8 assign to FQDFareRule7
  capture line:11, column:4, length:8 assign to FQDFareRule8
  capture line:12, column:4, length:8 assign to FQDFareRule9
  capture line:13, column:4, length:8 assign to FQDFareRule10
  capture line:14, column:4, length:8 assign to FQDFareRule11
  capture line:15, column:4, length:8 assign to FQDFareRule12
  capture line:16, column:4, length:8 assign to FQDFareRule13
  capture line:17, column:4, length:8 assign to FQDFareRule14
  capture line:18, column:4, length:8 assign to FQDFareRule15
  capture line:19, column:4, length:8 assign to FQDFareRule16
  capture line:20, column:4, length:8 assign to FQDFareRule17
  
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

    send "FQP" +FQPCommand +"/R," +DOI +",U*SRG01,UP,P/L-"  
    
        
  }
  when ("Create EMD"){
  if (status1 == "S"){
    if (airline1 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status1 == "U"){
    if (airline1 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline1 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status2 == "S"){
    if (airline2 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status2 == "U"){
    if (airline2 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline2 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status3 == "S"){
    if (airline3 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status3 == "U"){
    if (airline3 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline3 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status4 == "S"){
    if (airline4 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status4 == "U"){
    if (airline4 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline4 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status5 == "S"){
    if (airline5 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status5 == "U"){
    if (airline5 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline5 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status6 == "S"){
    if (airline6 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }
  if (status6 == "U"){
    if (airline6 == "UL"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "ME"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "SV"){
      assign "TRUE" to EMDEligible
    }
    if (airline6 == "RJ"){
      assign "TRUE" to EMDEligible
    }
  }


  
  if (EMDEligible == "TRUE"){
    assign "" to EMDOrigin
    assign "" to EMDDestination
    assign "" to EMDAirline
    if (OK1=="OK"){
     if (status1=="S"){
      assign airline1 to EMDAirline
      assign city1 to EMDOrigin
      assign city2 to EMDDestination
    }
    if (status1=="U"){
      assign airline1 to EMDAirline
      assign city1 to EMDOrigin
      assign city2 to EMDDestination
    }
    }
    if (OK2=="OK"){
    if (status2=="S"){
      assign airline2 to EMDAirline
        if (EMDOrigin ==""){
          assign city2 to EMDOrigin
        }
        assign city3 to EMDDestination
    }
    if (status2=="U"){
      assign airline2 to EMDAirline
        if (EMDOrigin ==""){
          assign city2 to EMDOrigin
        }
        assign city3 to EMDDestination
    }
    }
    if (OK3=="OK"){
    if (status3=="S"){
      assign airline3 to EMDAirline
        if (EMDOrigin ==""){
          assign city3 to EMDOrigin
        }
        assign city4 to EMDDestination
    }
    if (status3=="U"){
      assign airline3 to EMDAirline
        if (EMDOrigin ==""){
          assign city3 to EMDOrigin
        }
        assign city4 to EMDDestination
    }
    }
    if (OK4=="OK"){
    if (status4!="S"){
      assign airline4 to EMDAirline
        if (EMDOrigin ==""){
          assign city4 to EMDOrigin
        }
        assign city5 to EMDDestination
    }
    if (status4!="U"){
      assign airline4 to EMDAirline
        if (EMDOrigin ==""){
          assign city4 to EMDOrigin
        }
        assign city5 to EMDDestination
    }
    }
    if (OK5=="OK"){
    if (status5!="S"){
      assign airline5 to EMDAirline
        if (EMDOrigin ==""){
          assign city5 to EMDOrigin
        }
        assign city6 to EMDDestination
    }
    if (status5!="U"){
      assign airline5 to EMDAirline
        if (EMDOrigin ==""){
          assign city5 to EMDOrigin
        }
        assign city6 to EMDDestination
    }
    }
    if (OK6=="OK"){
    if (status6!="S"){
      assign airline6 to EMDAirline
        if (EMDOrigin ==""){
          assign city6 to EMDOrigin
        }
        assign city7 to EMDDestination
    }
    if (status6!="U"){
      assign airline6 to EMDAirline
        if (EMDOrigin ==""){
          assign city6 to EMDOrigin
        }
        assign city7 to EMDDestination
    }
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

    if (PAXNAME_ExtraCheck!=""){
      if (PAXNAME_ExtraCheck!=" "){
        send "RT" + Ticket_PNR
        mandatory ask "Get the Pax Name..." assign to PAXNAME
      }
    }

    send "NM1" + PAXNAME
    send "EGSD/V" +EMDAirline
    mandatory ask "Type the Penalty Code:" assign to EMDCode
    send "IU" +EMDAirline +"NN1" +EMDCode +EMDOrigin +EMDDestination +"/" +today 
    send "APE-A@Gmail.com"
    send "TKOK"
    send "RF" +agtName +";ER"
    send "TMC/V" +EMDAirline
    send "TMI/IC-TKT"+TKTP1 +TKTP2 +TKTP3
    mandatory ask "What is the Penalty Amount?" assign to EMDPenalty
    send "TMI/CV-" +EMDPenalty +"/F" +EMDPenalty
    send "TMI/FP-CASH"
    send "RF" +agtName +";ER"
    send ": EMD READY!, Before printing please reconfirm the (ROUTE) on it."
  }
  else{
    send "This isn't an EMD Airline!"
  }
}

when ("Create Ghost segments"){
  send "SRT" +DOI
  capture line:1, column:37, length:2 assign to travelYear
  send "DD" +DOI +"/" +travelDate1 +travelYear
  capture line:2, column:1, length:1 assign to checkyear
  if (checkyear =="-"){
  send "DF" +travelYear +";1"
  capture line:2, column:1, length:2 assign to travelYear
  }
  
  if (OK1=="OK"){
      send "ss" +airline1 +flightNo1 +class1 +travelDate1 +travelYear +city1 +city2 +"GK1/0000 0200/RECLOC"
  }
    if (OK2=="OK"){
      send "ss" +airline2 +flightNo2 +class2 +travelDate2 +travelYear +city2 +city3 +"GK1/0230 0500/RECLOC"
    }
    if (OK3=="OK"){
      send "ss" +airline3 +flightNo3 +class3 +travelDate3 +travelYear +city3 +city4 +"GK1/0600 0900/RECLOC"
    }
    if (OK4=="OK"){
      send "ss" +airline4 +flightNo4 +class4 +travelDate4 +travelYear +city4 +city5 +"GK1/0930 1200/RECLOC"
    }
    if (OK5=="OK"){
      send "ss" +airline5 +flightNo5 +class5 +travelDate5 +travelYear +city5 +city6 +"GK1/1300 1600/RECLOC"
    }
    if (OK6=="OK"){
     send "ss" +airline6 +flightNo6 +class6 +travelDate6 +travelYear +city6 +city7 +"GK1/1700 2000/RECLOC"
    }

    send "FXX/R," + DOI
    capture line:4, column:4, length:8 assign to checkfare1
    if (checkfare1==fareBasis1){
      capture line:4, column:1, length:2 assign to fare1No
      send "FQN" + fare1No +"*PE"
    }
    capture line:5, column:4, length:8 assign to checkfare1
    if (checkfare1==fareBasis1){
      capture line:5, column:1, length:2 assign to fare1No
      send "FQN" + fare1No +"*PE"
    }
    capture line:6, column:4, length:8 assign to checkfare1
    if (checkfare1==fareBasis1){
      capture line:6, column:1, length:2 assign to fare1No
      send "FQN" + fare1No +"*PE"
    }
    capture line:7, column:4, length:8 assign to checkfare1
    if (checkfare1==fareBasis1){
      capture line:7, column:1, length:2 assign to fare1No
      send "FQN" + fare1No +"*PE"
    }
    capture line:8, column:4, length:8 assign to checkfare1
    if (checkfare1==fareBasis1){
      capture line:8, column:1, length:2 assign to fare1No
      send "FQN" + fare1No +"*PE"
    }
    
}

}

