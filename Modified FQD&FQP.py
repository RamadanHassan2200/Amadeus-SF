// Modified FQD&FQP

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
  call "Modified FQD&FQP"
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
capture line:2, column:44, length:7 assign to DOI
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
capture line:4, column:33, length:14 assign to fareBasis1
capture line:4, column:47, length:1 assign to status1
capture line:4, column:62, length:2 assign to pc1

capture line:5, column:4, length:1 assign to original2  
capture line:5, column:5, length:3 assign to city2
capture line:5, column:9, length:2 assign to airline2
capture line:5, column:11, length:4 assign to flightNo2
capture line:5, column:18, length:1 assign to class2
capture line:5, column:20, length:5 assign to travelDate2
capture line:5, column:30, length:2 assign to OK2
capture line:5, column:33, length:14 assign to fareBasis2
capture line:5, column:47, length:1 assign to status2
capture line:5, column:62, length:2 assign to pc2

capture line:6, column:4, length:1 assign to original3
capture line:6, column:5, length:3 assign to city3
capture line:6, column:9, length:2 assign to airline3
capture line:6, column:11, length:4 assign to flightNo3
capture line:6, column:18, length:1 assign to class3
capture line:6, column:20, length:5 assign to travelDate3
capture line:6, column:30, length:2 assign to OK3
capture line:6, column:33, length:14 assign to fareBasis3
capture line:6, column:47, length:1 assign to status3
capture line:6, column:62, length:2 assign to pc3

capture line:7, column:4, length:1 assign to original4
capture line:7, column:5, length:3 assign to city4
capture line:7, column:9, length:2 assign to airline4
capture line:7, column:11, length:4 assign to flightNo4
capture line:7, column:18, length:1 assign to class4
capture line:7, column:20, length:5 assign to travelDate4
capture line:7, column:30, length:2 assign to OK4
capture line:7, column:33, length:14 assign to fareBasis4
capture line:7, column:47, length:1 assign to status4
capture line:7, column:62, length:2 assign to pc4

capture line:8, column:4, length:1 assign to original5
capture line:8, column:5, length:3 assign to city5
capture line:8, column:9, length:2 assign to airline5
capture line:8, column:11, length:4 assign to flightNo5
capture line:8, column:18, length:1 assign to class5
capture line:8, column:20, length:5 assign to travelDate5
capture line:8, column:30, length:2 assign to OK5
capture line:8, column:33, length:14 assign to fareBasis5
capture line:8, column:47, length:1 assign to status5
capture line:8, column:62, length:2 assign to pc5

capture line:9, column:4, length:1 assign to original6
capture line:9, column:5, length:3 assign to city6
capture line:9, column:9, length:2 assign to airline6
capture line:9, column:11, length:4 assign to flightNo6
capture line:9, column:18, length:1 assign to class6
capture line:9, column:20, length:5 assign to travelDate6
capture line:9, column:30, length:2 assign to OK6
capture line:9, column:33, length:14 assign to fareBasis6
capture line:9, column:47, length:1 assign to status6
capture line:9, column:62, length:2 assign to pc6

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

capture line:6, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:9, column:6, length:3 assign to original_Airline
      capture line:6, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:6, column:21, length:7 assign to FODate
      }
      capture line:6, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:6, column:24, length:7 assign to FODate
      }
}
capture line:7, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:7, column:4, length:3 assign to original_Airline
      capture line:7, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:7, column:21, length:7 assign to FODate
      }
      capture line:7, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:7, column:24, length:7 assign to FODate
      }
}
capture line:8, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:8, column:4, length:3 assign to original_Airline
      capture line:8, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:8, column:21, length:7 assign to FODate
      }
      capture line:8, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:8, column:24, length:7 assign to FODate
      }
}
capture line:9, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:9, column:4, length:3 assign to original_Airline
      capture line:9, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:9, column:21, length:7 assign to FODate
      }
      capture line:9, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:9, column:24, length:7 assign to FODate
      }
}
capture line:10, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:10, column:4, length:3 assign to original_Airline
      capture line:10, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:10, column:21, length:7 assign to FODate
      }
      capture line:10, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:10, column:24, length:7 assign to FODate
      }
}
capture line:11, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:11, column:4, length:3 assign to original_Airline
      capture line:11, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:11, column:21, length:7 assign to FODate
      }
      capture line:11, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:11, column:24, length:7 assign to FODate
      }
}
capture line:12, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:12, column:4, length:3 assign to original_Airline
      capture line:12, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:12, column:21, length:7 assign to FODate
      }
      capture line:12, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:12, column:24, length:7 assign to FODate
      }
}
capture line:13, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:13, column:4, length:3 assign to original_Airline
      capture line:13, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:13, column:21, length:7 assign to FODate
      }
      capture line:13, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:13, column:24, length:7 assign to FODate
      }
}
capture line:14, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:14, column:4, length:3 assign to original_Airline
      capture line:14, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:14, column:21, length:7 assign to FODate
      }
      capture line:14, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:14, column:24, length:7 assign to FODate
      }
}
capture line:15, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:15, column:4, length:3 assign to original_Airline
      capture line:15, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:15, column:21, length:7 assign to FODate
      }
      capture line:15, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:15, column:24, length:7 assign to FODate
      }
}
capture line:16, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:16, column:4, length:3 assign to original_Airline
      capture line:16, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:16, column:21, length:7 assign to FODate
      }
      capture line:16, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:16, column:24, length:7 assign to FODate
      }
}
capture line:17, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:17, column:4, length:3 assign to original_Airline
      capture line:17, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:17, column:21, length:7 assign to FODate
      }
      capture line:17, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:17, column:24, length:7 assign to FODate
      }
}
capture line:18, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:18, column:4, length:3 assign to original_Airline
      capture line:18, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:18, column:21, length:7 assign to FODate
      }
      capture line:18, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:18, column:24, length:7 assign to FODate
      }
}
capture line:19, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:19, column:4, length:3 assign to original_Airline
      capture line:19, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:19, column:21, length:7 assign to FODate
      }
      capture line:19, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:19, column:24, length:7 assign to FODate
      }
}
capture line:20, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:20, column:4, length:3 assign to original_Airline
      capture line:20, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:20, column:21, length:7 assign to FODate
      }
      capture line:20, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:20, column:24, length:7 assign to FODate
      }
}
capture line:21, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:21, column:4, length:3 assign to original_Airline
      capture line:21, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:21, column:21, length:7 assign to FODate
      }
      capture line:21, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:21, column:24, length:7 assign to FODate
      }
}
capture line:22, column:1, length:3 assign to FO_Check
if (FO_Check=="FO "){
      assign "True" to FOCheck
      capture line:22, column:4, length:3 assign to original_Airline
      capture line:22, column:28, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:22, column:21, length:7 assign to FODate
      }
      capture line:22, column:31, length:1 assign to FODate_check
      if (FODate_check == "/"){
        capture line:22, column:24, length:7 assign to FODate
      }
}



if (FOCheck == "True"){
        send "DD"
        capture line:2, column:33, length:7 assign to todayDate
        send "DD" +FODate +"/" +todayDate
        capture line:2, column:1, length:4 assign to dateDifference
        if (dateDifference >= "365"){
          // exclude 077, 125, 176, 220, 229, 235, 618
          assign "True" to FO_2_Years_Validity
          if (original_Airline != "077"){
            if (original_Airline != "125"){
              if (original_Airline != "176"){
                if (original_Airline != "220"){
                  if (original_Airline != "229"){
                    if (original_Airline != "235"){
                      if (original_Airline != "618"){
                        assign "False" to FO_2_Years_Validity
                      }
                    }
                  }
                }
              }
            }
          }
          if (FO_2_Years_Validity == "True"){
            if (dateDifference >= "730"){
              send "FO is Non-Refundable for 2 Years"
              ask "Ignore the Refund" assign to qz5
              call "Modified FQD&FQP"
            }
          }else{
            send "FO is Non-Refundable for 2 Years"
            ask "Ignore the Refund" assign to qz5
            call "Modified FQD&FQP"
          }
        }
}

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

//Exclude NRF classes , NE(N,S)

if (airline1 == "NE"){
 assign "True" to NE_Refundable
  if (class1 == "N"){
    assign "False" to NE_Refundable
  }
  if (class1 == "S"){
    assign "False" to NE_Refundable
  }

  if (segCount >= "2"){
   if (class2 == "N"){
    assign "False" to NE_Refundable
  }
  if (class2 == "S"){
    assign "False" to NE_Refundable
  }
  }

  if (segCount >= "3"){
  if (class3 == "N"){
    assign "False" to NE_Refundable
  }
  if (class3 == "S"){
    assign "False" to NE_Refundable
  }
  }

  if (segCount >= "4"){
  if (class4 == "N"){
    assign "False" to NE_Refundable
  }
  if (class4 == "S"){
    assign "False" to NE_Refundable
  }
  }

  if (segCount >= "5"){
  if (class5 == "N"){
    assign "False" to NE_Refundable
  }
  if (class5 == "S"){
    assign "False" to NE_Refundable
  }
  }

  if (segCount >= "6"){
   if (class6 == "N"){
    assign "False" to NE_Refundable
  }
  if (class6 == "S"){
    assign "False" to NE_Refundable
  }
  }

  if (NE_Refundable != "True"){
   send "NE is Non-Refundable for N,S Classes"
   ask "Ignore the Refund" assign to qz5
   call "Modified FQD&FQP"
  }


}

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
  if (segCount > "0"){
  if (airline1 != "MS"){
    if (airline1 != "EK"){
      if (airline1 != "LH"){
        if (airline1 != "BA"){
          if (airline1 != "TK"){
            if (airline1 != "SQ"){
              if (airline1 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount > "1"){
  if (airline2 != "MS"){
    if (airline2 != "EK"){
      if (airline2 != "LH"){
        if (airline2 != "BA"){
          if (airline2 != "TK"){
            if (airline2 != "SQ"){
              if (airline2 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount > "2"){
  if (airline3 != "MS"){
    if (airline3 != "EK"){
      if (airline3 != "LH"){
        if (airline3 != "BA"){
          if (airline3 != "TK"){
            if (airline3 != "SQ"){
              if (airline3 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount > "3"){
  if (airline4 != "MS"){
    if (airline4 != "EK"){
      if (airline4 != "LH"){
        if (airline4 != "BA"){
          if (airline4 != "TK"){
            if (airline4 != "SQ"){
              if (airline4 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount > "4"){
  if (airline5 != "MS"){
    if (airline5 != "EK"){
      if (airline5 != "LH"){
        if (airline5 != "BA"){
          if (airline5 != "TK"){
            if (airline5 != "SQ"){
              if (airline5 != "KU"){
                assign "False" to ticket_2_Years_Validity
              }
            }
          }
        }
      }
    }
  }
  }

  if (segCount > "5"){
  if (airline6 != "MS"){
    if (airline6 != "EK"){
      if (airline6 != "LH"){
        if (airline6 != "BA"){
          if (airline6 != "TK"){
            if (airline6 != "SQ"){
              if (airline6 != "KU"){
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
      mandatory ask "The Ticket is not valid for auto refund!" assign to qz5
      call "Modified FQD&FQP"
    }
  }
  else{
    if (checkDOIDays > "728"){
      send "THIS TICKET IS NOT VALID FOR REFUND! Expired Ticket!"
      mandatory ask "The Ticket is not valid for auto refund!" assign to qz5
      call "Modified FQD&FQP"
    }
  }

}
else{
  send "THIS TICKET IS NOT VALID FOR REFUND!, please void it!"
  mandatory ask "The Ticket is not valid for auto refund!, Please void it" assign to qz5
  call "Modified FQD&FQP"
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

if (segCount >"1"){
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

if (segCount >"2"){
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

if (segCount > "3"){
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

if (segCount > "4"){
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

if (segCount > "5"){
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

if (airline1 =="KU"){
  assign "True" to KU_Refundable
  if (segCount == "1"){
    if (segment1_General_Status_Open == "True"){
      assign "false" to KU_Refundable
    }
  }
  if (segCount == "2"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        assign "false" to KU_Refundable
      }
    }
  }
  if (segCount == "3"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          assign "false" to KU_Refundable
        }
      }
    }
  }
  if (segCount == "4"){
    if (segment1_General_Status_Open == "True"){
      if (segment2_General_Status_Open == "True"){
        if (segment3_General_Status_Open == "True"){
          if (segment4_General_Status_Open == "True"){
            assign "false" to KU_Refundable
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
              assign "false" to KU_Refundable
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
                assign "false" to KU_Refundable
              }
            }
          }
        }
      }
    }
  }
  if (KU_Refundable != "True"){
    send "KU is Non-Refundable, Fully Unused"
    ask "Ignore the Refund" assign to qz5
    call "Modified FQD&FQP"
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
        when ("No"){}
      }
      assign "False" to status_NoShow
    }
    else{
      choose "This Ticket is within No-Show, Do you want to continue as:"{
        when ("No-Show"){}
        when ("Normal"){assign "Normal" to status_NoShow}
      }
    }
  }

  // Check Out Of Sequence Scenarios & Origanl destinations
  assign "TRUE" to Out_of_Sequence
  assign "False" to Originals
  assign "" to first_Open_Segment
    // Acceppted Scenarios
    // O 
    // OO - FO
    // OOO - FOO - FFO
    // OOOO - FOOO - FFOO - FFFO
    // OOOOO - FOOOO - FFOOO - FFFOO - FFFFO
    // OOOOOO - FOOOOO - FFOOOO - FFFOOO - FFFFOO - FFFFFO

    if (segment1_General_Status_Open == "True"){
      append "1" to first_Open_Segment
      if (original1 == "O"){
        assign "True" to Originals
      }
    }
    if (segment2_General_Status_Open == "True"){
      append "2" to first_Open_Segment
      if (original2 == "O"){
        assign "True" to Originals
      }
    }
    if (segment3_General_Status_Open == "True"){
      append "3" to first_Open_Segment
      if (original3 == "O"){
        assign "True" to Originals
      }
    }
    if (segment4_General_Status_Open == "True"){
      append "4" to first_Open_Segment
      if (original4 == "O"){
        assign "True" to Originals
      }
    }
    if (segment5_General_Status_Open == "True"){
      append "5" to first_Open_Segment
      if (original5 == "O"){
        assign "True" to Originals
      }
    }
    if (segment6_General_Status_Open == "True"){
      append "6" to first_Open_Segment
      if (original6 == "O"){
        assign "True" to Originals
      }
    }

    if (segCount == "1"){
      if (first_Open_Segment == "1"){
        assign "False" to Out_of_Sequence
      }
    }
    if (segCount == "2"){
      if (first_Open_Segment == "12"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "2"){
        assign "False" to Out_of_Sequence
      }
    }
    if (segCount == "3"){
      if (first_Open_Segment == "123"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "23"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "3"){
        assign "False" to Out_of_Sequence
      }
    }
    if (segCount == "4"){
      if (first_Open_Segment == "1234"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "234"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "34"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "4"){
        assign "False" to Out_of_Sequence
      }
    }
    if (segCount == "5"){
      if (first_Open_Segment == "12345"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "2345"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "345"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "45"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "5"){
        assign "False" to Out_of_Sequence
      }
    }
    if (segCount == "6"){
      if (first_Open_Segment == "123456"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "23456"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "3456"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "456"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "56"){
        assign "False" to Out_of_Sequence
      }
      if (first_Open_Segment == "6"){
        assign "False" to Out_of_Sequence
      }
    }
  


if (Out_of_Sequence == "True"){
  if (Originals == "True"){
    send "THIS TICKET IS NOT VALID FOR REFUND! Out of Sequence!"
    mandatory ask "The Ticket is not valid for auto refund!, Please Ignore it" assign to qz5
    call "Modified FQD&FQP"
  }
}

assign "" to checkNP
if (PCC_ID =="71201675"){
  assign "/T-NP" to checkNP
}
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    ask "Continue?" assign to qz5
}
if (checkPending=="REFUND RECORD PENDING"){
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
}
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    ask "Continue?" assign to qz5
}
capture line:1, column:34, length:3 assign to checkRFND
if (checkRFND!="AGT"){
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3
}
  
capture line:1, column:58, length:1 assign to checkATC
if (checkATC =="C"){

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

    send "TRFU/NF"
    capture line:9, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:9, column:33, length:10 assign to totalRefundAmount
    }
    capture line:10, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:10, column:33, length:10 assign to totalRefundAmount
    }
    capture line:11, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:11, column:33, length:10 assign to totalRefundAmount
    }
    capture line:12, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:12, column:33, length:10 assign to totalRefundAmount
    }
    capture line:13, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:13, column:33, length:10 assign to totalRefundAmount
    }


    capture line: 11, column:1, length:3 assign to check_FP1
    if (check_FP1 == "FP1"){
      capture line:11, column:33, length:10 assign to FP_Amount
    }
    capture line: 12, column:1, length:3 assign to check_FP2
    if (check_FP2 == "FP1"){
      capture line:12, column:33, length:10 assign to FP_Amount
    }
    capture line: 13, column:1, length:3 assign to check_FP3
    if (check_FP3 == "FP1"){
      capture line:13, column:33, length:10 assign to FP_Amount
    }
    capture line: 14, column:1, length:3 assign to check_FP4
    if (check_FP4 == "FP1"){
      capture line:14, column:33, length:10 assign to FP_Amount
    }
    capture line: 15, column:1, length:3 assign to check_FP5
    if (check_FP5 == "FP1"){
      capture line:15, column:33, length:10 assign to FP_Amount
    }


    if (totalRefundAmount == FP_Amount){
        send "TRFP"
    }
    else{
      send "TRFU/FPA1" +totalRefundAmount
      send "TRFP"
    }
    capture line:2, column:1, length:21 assign to refundedTicketCheck
    if (refundedTicketCheck == "OK - REFUND PROCESSED"){
        send ":" +totalRefundAmount +"  " +refundCurrency
        call "Modified FQD&FQP"
    }
}

if (checkATC =="P"){
  capture line:14, column:28, length:16 assign to check_GDS1
  capture line:15, column:28, length:16 assign to check_GDS2
  capture line:16, column:28, length:16 assign to check_GDS3
  capture line:17, column:28, length:16 assign to check_GDS4
  capture line:18, column:28, length:16 assign to check_GDS5

  if (check_GDS1 == "OTHER GDS TICKET"){
    assign "True" to travelport_Galileo
  }
  if (check_GDS2 == "OTHER GDS TICKET"){
    assign "True" to travelport_Galileo
  }
  if (check_GDS3 == "OTHER GDS TICKET"){
    assign "True" to travelport_Galileo
  }
  if (check_GDS4 == "OTHER GDS TICKET"){
    assign "True" to travelport_Galileo
  }
  if (check_GDS5 == "OTHER GDS TICKET"){
    assign "True" to travelport_Galileo
  }

  if (travelport_Galileo == "True"){
    send "TRFU/NF"
    
    capture line:9, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:9, column:33, length:10 assign to totalRefundAmount
    }
    capture line:10, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:10, column:33, length:10 assign to totalRefundAmount
    }
    capture line:11, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:11, column:33, length:10 assign to totalRefundAmount
    }
    capture line:12, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:12, column:33, length:10 assign to totalRefundAmount
    }
    capture line:13, column:5, length:12 assign to check_Total_Refund
    if (check_Total_Refund == "REFUND TOTAL"){
      capture line:13, column:33, length:10 assign to totalRefundAmount
    }


    capture line: 11, column:1, length:3 assign to check_FP1
    if (check_FP1 == "FP1"){
      capture line:11, column:33, length:10 assign to FP_Amount
    }
    capture line: 12, column:1, length:3 assign to check_FP2
    if (check_FP2 == "FP1"){
      capture line:12, column:33, length:10 assign to FP_Amount
    }
    capture line: 13, column:1, length:3 assign to check_FP3
    if (check_FP3 == "FP1"){
      capture line:13, column:33, length:10 assign to FP_Amount
    }
    capture line: 14, column:1, length:3 assign to check_FP4
    if (check_FP4 == "FP1"){
      capture line:14, column:33, length:10 assign to FP_Amount
    }
    capture line: 15, column:1, length:3 assign to check_FP5
    if (check_FP5 == "FP1"){
      capture line:15, column:33, length:10 assign to FP_Amount
    }

    if (totalRefundAmount == FP_Amount){
        send "TRFP"
    }
    else{
      send "TRFU/FPA1" +totalRefundAmount
      send "TRFP"
    }    
  }
  capture line:2, column:1, length:21 assign to refundedTicketCheck
    if (refundedTicketCheck == "OK - REFUND PROCESSED"){
        send ":" +totalRefundAmount +"  " +refundCurrency
        call "Modified FQD&FQP"
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

assign "P" to airline_TourCode
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
  assign "" to ptc_ID
  if (PTC == "CHD"){
    assign "CH" to ptc_ID
  }
  if (PTC == "INF"){
    assign "IN" to ptc_ID
  }

  send "FXX/R" +ptc_ID +"," +DOI +",UP,U," +airline_TourCode
  
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
    
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN1 
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN1 
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN2 
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN2 
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN3 
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN3 
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN4
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN4
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN5
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN5
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN6
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN6
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN7
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN7
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN8
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN8
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN9
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN9
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN10
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN10
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN11
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN11
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN12
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN12
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN14
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN14
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN15
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN15
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN16
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN16
    } 

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN17
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXXN17
    }

    capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXX_test_FareRule_Number
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXX_test_FareRule_Number
    }

  capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
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

    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXX_test_FareRule_Number
    }
    capture line:3, column:1, length:14 assign to check_FQQ_Opened
    if (check_FQQ_Opened == "ENTRY REQUIRES"){
      send "FQQ" +FXX_test_FareRule_Number
    }

  capture line:9, column:32, length:14 assign to FQQfareBasis1
    if (FQQfareBasis1 != fareBasis1){
      assign "False" to check_FareBasis_Compatibility
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign FXX_test_FareRule_Number to FXXfareBasisNumber
    }
 }

  if (check_FareBasis_Compatibility == "False"){
    send "Can't Find The Fare Rule!"
    ask "Please Continue manually!" assign to fq5
    call "FQD&FQP"
 }

 send "FQN" +FXXfareBasisNumber +"*PE"
 send "MD-CANCELLATIONS"
 call "FQN_Refund_Fetcher"

 

  assign "1" to Fares
  if (segCount > "1"){
    if (fareBasis1 != fareBasis2){
      append "1" to Fares
    }
  }
  if (segCount > "2"){
    if (fareBasis2 != fareBasis3){
      append "1" to Fares
    }
  }
  if (segCount > "3"){
    if (fareBasis3 != fareBasis4){
      append "1" to Fares
    }
  }
  if (segCount > "4"){
    if (fareBasis4 != fareBasis5){
      append "1" to Fares
    }
  }
  if (segCount > "5"){
    if (fareBasis5 != fareBasis6){
      append "1" to Fares
    }
  }

  if (Fares == "11"){
    send "FQN" +FXXfareBasisNumber +"-2*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
  }
  if (Fares == "111"){
    send "FQN" +FXXfareBasisNumber +"-3*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
  }
  if (Fares == "1111"){
    send "FQN" +FXXfareBasisNumber +"-4*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
  }
  if (Fares == "11111"){
    send "FQN" +FXXfareBasisNumber +"-5*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
  }
  if (Fares == "111111"){
    send "FQN" +FXXfareBasisNumber +"-6*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
  }



