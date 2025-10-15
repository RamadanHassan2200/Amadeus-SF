//z_ATC_Refund

capture line:1, column:5, length:1 assign to TKTP1
capture line:1, column:6, length:2 assign to TKTP2
capture line:1, column:8, length:10 assign to TKTP3
append TKTP1 + TKTP2 to AL_Code

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
  assign "True" to ignored_Refund
}
if (gov11 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov2 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov22 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov3 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov33 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov4 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov44 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov5 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov55 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov6 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov66 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov7 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov77 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov8 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov88 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov9 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov99 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov10 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1010 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov11 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1111 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov12 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1212 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov13 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1313 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov14 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1414 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov15 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1515 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov16 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
}
if (gov1616 =="GOV"){
  send "Governmental Ticket ignore it!"
  assign "True" to ignored_Refund
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

if (FO_Check == "/FC"){
  capture line:6, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:6, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:8, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:9, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:10, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:11, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:12, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:13, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:14, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:15, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:16, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:17, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:18, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:19, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:20, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:21, column:5, length:3 assign to FC_City
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
if (FO_Check == "/FC"){
  capture line:22, column:5, length:3 assign to FC_City
}

if (FOCheck == "True"){
  if (FC_City != city1){
    assign "True" to ignored_Refund
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
                        assign "True" to ignored_Refund
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
              assign "True" to ignored_Refund
            }
          }else{
            send "FO is Non-Refundable for 2 Years"
            assign "True" to ignored_Refund
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



if (ignored_Refund != "True"){
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
      assign "True" to ignored_Refund
    }
  }
  else{
    if (checkDOIDays > "728"){
      send "THIS TICKET IS NOT VALID FOR REFUND! Expired Ticket!"
      assign "True" to ignored_Refund
    }
  }

}
else{
  send "THIS TICKET IS NOT VALID FOR REFUND!, please void it!"
  assign "True" to ignored_Refund
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
    assign "True" to ignored_Refund
  }
}

if (AL_Code =="072"){
  assign "True" to AL_Refundable
  if (segCount >= "1"){
    if (segment1_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "1"){
    if (segment2_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "2"){
    if (segment3_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "3"){
    if (segment4_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "4"){
    if (segment5_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "5"){
    if (segment6_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }

  if (AL_Refundable != "True"){
    assign "True" to ignored_Refund
  }
}

if (AL_Code =="077"){
  assign "True" to AL_Refundable
  if (segCount >= "1"){
    if (segment1_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "1"){
    if (segment2_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "2"){
    if (segment3_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "3"){
    if (segment4_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "4"){
    if (segment5_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "5"){
    if (segment6_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }

  if (AL_Refundable != "True"){
    assign "True" to ignored_Refund
  }
}

if (AL_Code =="079"){
  assign "True" to AL_Refundable
  if (segCount >= "1"){
    if (segment1_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "1"){
    if (segment2_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "2"){
    if (segment3_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "3"){
    if (segment4_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "4"){
    if (segment5_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "5"){
    if (segment6_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }

  if (AL_Refundable != "True"){
    assign "True" to ignored_Refund
  }
}

if (AL_Code =="381"){
  assign "True" to AL_Refundable
  if (segCount >= "1"){
    if (segment1_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "1"){
    if (segment2_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "2"){
    if (segment3_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "3"){
    if (segment4_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "4"){
    if (segment5_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "5"){
    if (segment6_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }

  if (AL_Refundable != "True"){
    assign "True" to ignored_Refund
  }
}

if (AL_Code =="607"){
  assign "True" to AL_Refundable
  if (segCount >= "1"){
    if (segment1_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "1"){
    if (segment2_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "2"){
    if (segment3_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "3"){
    if (segment4_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "4"){
    if (segment5_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }
  if (segCount > "5"){
    if (segment6_General_Status_Open != "True"){
      assign "false" to AL_Refundable
    }
  }

  if (AL_Refundable != "True"){
    assign "True" to ignored_Refund
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
    if (check_Before_After >= "0"){
      assign "True" to ignored_Refund
    }
  }

}

if (ignored_Refund != "True"){

  if (airline1 == "EY"){
    assign "True" to approved_AL
  }
  if (airline1 == "GF"){
    assign "True" to approved_AL
  }
  if (airline1 == "MS"){
    assign "True" to approved_AL
  }
  if (airline1 == "SM"){
    assign "True" to approved_AL
  }
  if (airline1 == "PR"){
    assign "True" to approved_AL
  }
  if (approved_AL == "True"){
     // Ghost Seg:

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
      send "1"
    }

    if (segCount > "1"){
      capture line:10, column:32, length:14 assign to FQQfareBasis2
      if (FQQfareBasis2 != fareBasis2){
        assign "False" to check_FareBasis_Compatibility
        send "2"
      }
    }

    if (segCount > "2"){
      capture line:11, column:32, length:14 assign to FQQfareBasis3
      if (FQQfareBasis3 != fareBasis3){
        assign "False" to check_FareBasis_Compatibility
        send "3"
      }
    }

    if (segCount > "3"){
      capture line:12, column:32, length:14 assign to FQQfareBasis4
      if (FQQfareBasis4 != fareBasis4){
        assign "False" to check_FareBasis_Compatibility
        send "4"
      }
    }

    if (segCount > "4"){
      capture line:13, column:32, length:14 assign to FQQfareBasis5
      if (FQQfareBasis5 != fareBasis5){
        assign "False" to check_FareBasis_Compatibility
        send "5"
      }
    }

    if (segCount > "5"){
      capture line:14, column:32, length:14 assign to FQQfareBasis6
      if (FQQfareBasis6 != fareBasis6){
        assign "False" to check_FareBasis_Compatibility
        send "6"
      }
    }

    if (check_FareBasis_Compatibility == "True"){
      assign "7" to FXXfareBasisNumber
      send "8"
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

  if (check_FareBasis_Compatibility != "False"){

 send "FQN" +FXXfareBasisNumber +"*PE"
 send "MD-CANCELLATIONS"
 call "FQN_Refund_Fetcher"
 send "RTR"
  capture line:4, column:25, length:3 assign to penalty_Currency
  capture line:4, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:4, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:4, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:4, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:4, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:4, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:4, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:4, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:4, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:4, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:4, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:4, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:4, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:4, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }
    assign totalNewPrice to no_Show_Penalty_Amount
  }

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
 send "RTR"
  capture line:7, column:25, length:3 assign to penalty_Currency
  capture line:7, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:7, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:7, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:7, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:7, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:7, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:7, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:7, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:7, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:7, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:7, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:7, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:7, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:7, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }

    assign totalNewPrice to no_Show_Penalty_Amount1
    if (no_Show_Penalty_Amount1 > no_Show_Penalty_Amount){
      assign no_Show_Penalty_Amount1 to no_Show_Penalty_Amount
    }
  }
  }
  if (Fares == "111"){
    send "FQN" +FXXfareBasisNumber +"-3*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
 send "RTR"
  capture line:10, column:25, length:3 assign to penalty_Currency
  capture line:10, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:10, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:10, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:10, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:10, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:10, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:10, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:10, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:10, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:10, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:10, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:10, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:10, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:10, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }

    assign totalNewPrice to no_Show_Penalty_Amount1
    if (no_Show_Penalty_Amount1 > no_Show_Penalty_Amount){
      assign no_Show_Penalty_Amount1 to no_Show_Penalty_Amount
    }
  }
  }
  if (Fares == "1111"){
    send "FQN" +FXXfareBasisNumber +"-4*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
 send "RTR"
  capture line:13, column:25, length:3 assign to penalty_Currency
  capture line:13, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:13, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:13, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:13, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:13, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:13, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:13, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:13, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:13, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:13, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:13, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:13, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:13, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:13, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }

    assign totalNewPrice to no_Show_Penalty_Amount1
    if (no_Show_Penalty_Amount1 > no_Show_Penalty_Amount){
      assign no_Show_Penalty_Amount1 to no_Show_Penalty_Amount
    }
  }
  }
  if (Fares == "11111"){
    send "FQN" +FXXfareBasisNumber +"-5*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
 send "RTR"
  capture line:16, column:25, length:3 assign to penalty_Currency
  capture line:16, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:16, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:16, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:16, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:16, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:16, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:16, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:16, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:16, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:16, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:16, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:16, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:16, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:16, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }

    assign totalNewPrice to no_Show_Penalty_Amount1
    if (no_Show_Penalty_Amount1 > no_Show_Penalty_Amount){
      assign no_Show_Penalty_Amount1 to no_Show_Penalty_Amount
    }
  }
  }
  if (Fares == "111111"){
    send "FQN" +FXXfareBasisNumber +"-6*PE"
    send "MD-CANCELLATIONS"
    call "FQN_Refund_Fetcher"
 send "RTR"
  capture line:19, column:25, length:3 assign to penalty_Currency
  capture line:19, column:29, length:10 assign to no_Show_Penalty_Original
  if (no_Show_Penalty_Original != "NON-REFUND"){
  capture line:19, column:29, length:1 assign to no_Show_Penalty_Original
    capture line:19, column:30, length:1 assign to no_Show_Penalty_p
    if (no_Show_Penalty_p != " "){
    if (no_Show_Penalty_p != ""){
      append no_Show_Penalty_p to no_Show_Penalty_Original
      capture line:19, column:31, length:1 assign to no_Show_Penalty_p
      if (no_Show_Penalty_p != " "){
      if (no_Show_Penalty_p != ""){
        append no_Show_Penalty_p to no_Show_Penalty_Original
        capture line:19, column:32, length:1 assign to no_Show_Penalty_p
        if (no_Show_Penalty_p != " "){
        if (no_Show_Penalty_p != ""){
            append no_Show_Penalty_p to no_Show_Penalty_Original
            capture line:19, column:33, length:1 assign to no_Show_Penalty_p
            if (no_Show_Penalty_p != " "){
            if (no_Show_Penalty_p != ""){
                append no_Show_Penalty_p to no_Show_Penalty_Original
                capture line:19, column:34, length:1 assign to no_Show_Penalty_p
                if (no_Show_Penalty_p != " "){
                if (no_Show_Penalty_p != ""){
                    append no_Show_Penalty_p to no_Show_Penalty_Original
                    capture line:19, column:35, length:1 assign to no_Show_Penalty_p
                    if (no_Show_Penalty_p != " "){
                    if (no_Show_Penalty_p != ""){
                      append no_Show_Penalty_p to no_Show_Penalty_Original
                      capture line:19, column:36, length:1 assign to no_Show_Penalty_p
                      if (no_Show_Penalty_p != " "){
                      if (no_Show_Penalty_p != ""){
                        append no_Show_Penalty_p to no_Show_Penalty_Original
                        capture line:19, column:36, length:1 assign to no_Show_Penalty_p
                        if (no_Show_Penalty_p != " "){
                        if (no_Show_Penalty_p != ""){
                          append no_Show_Penalty_p to no_Show_Penalty_Original
                          capture line:19, column:37, length:1 assign to no_Show_Penalty_p
                          if (no_Show_Penalty_p != " "){
                          if (no_Show_Penalty_p != ""){
                            append no_Show_Penalty_p to no_Show_Penalty_Original
                            capture line:19, column:38, length:1 assign to no_Show_Penalty_p
                            if (no_Show_Penalty_p != " "){
                            if (no_Show_Penalty_p != ""){
                              append no_Show_Penalty_p to no_Show_Penalty_Original
                              capture line:19, column:39, length:1 assign to no_Show_Penalty_p
                              if (no_Show_Penalty_p != " "){
                              if (no_Show_Penalty_p != ""){
                                append no_Show_Penalty_p to no_Show_Penalty_Original
                                capture line:19, column:40, length:1 assign to no_Show_Penalty_p
                                if (no_Show_Penalty_p != " "){
                                if (no_Show_Penalty_p != ""){
                                  append no_Show_Penalty_p to no_Show_Penalty_Original
                              
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
      }
    }
    }
  send "FQC" +no_Show_Penalty_Original +" " +penalty_Currency +"/" +DOI
  capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }

    assign totalNewPrice to no_Show_Penalty_Amount1
    if (no_Show_Penalty_Amount1 > no_Show_Penalty_Amount){
      assign no_Show_Penalty_Amount1 to no_Show_Penalty_Amount
    }
  }
  }

  assign "" to checkNP
if (PCC_ID =="71201675"){
  assign "/T-NP" to checkNP
}
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}
if (checkPending=="REFUND RECORD PENDING"){
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
}
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}
 

  send "TRFIG"
    assign "" to checkNP
if (PCC_ID =="71201675"){
  assign "/T-NP" to checkNP
}
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +checkNP
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}
if (checkPending=="REFUND RECORD PENDING"){
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +checkNP
}
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}

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
    if (PTC == "INF"){
        send "TRFU/U0"
        send "TRFU/CP0A"
        send "TRFU/RMNORMAL REFUND APPLIED BY SF"
    }
    else{
    if (no_Show_Penalty_Original == "NON-REFUND"){
      send "TRF"
      capture line:5, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:5, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:6, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:6, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:7, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:7, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:8, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:8, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:9, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:9, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:10, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:10, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:11, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:11, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:12, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:12, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:13, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:13, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
      send "TRFU/CP0A"
      send "TRFU/RMTAX REFUND APPLIED BY SF"
      assign "True" to tax_refund_eligible
    }
    else{
    send "DF" +totalRefundAmount +"-" +no_Show_Penalty_Amount
    capture line:1, column:1, length:7 assign to check_Refund_Eligibility
    if (check_Refund_Eligibility == "INVALID"){
      mandatory ask "Ignore and Report it please" assign to qz5
      send "TRFIG"
    }
    else{
    capture line:2, column:1, length:1 assign to negative_Sign
    capture line:2, column:1, length:2 assign to zer_Value
    if (negative_Sign == "-"){
      assign "True" to tax_refund_eligible
      if (AL_Code == "079"){
        assign "FALSE" to tax_refund_eligible
      }
      if (AL_Code == "077"){
        assign "FALSE" to tax_refund_eligible
      }
    }
    if (zer_Value == " 0"){
      assign "True" to tax_refund_eligible
      if (AL_Code == "079"){
        assign "FALSE" to tax_refund_eligible
      }
    }

    
    send "TRF"
    if (tax_refund_eligible == "True"){
      capture line:5, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:5, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:6, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:6, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:7, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:7, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:8, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:8, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:9, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:9, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:10, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:10, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:11, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:11, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:12, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:12, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
capture line:13, column:1, length:2 assign to fare_Paid
if (fare_Paid =="F "){
    capture line:13, column:31, length:12 assign to fare_Paid_Amount
    send "TRFU/U" + fare_Paid_Amount
}
      send "TRFU/CP0A"
      send "TRFU/RMTAX REFUND APPLIED BY SF"
      // YR & YQ Deletion


    }else{
      send "TRFU/U0"
      send "TRFU/CP" +no_Show_Penalty_Amount +"A"
      send "TRFU/RMNORMAL REFUND APPLIED BY SF"
    }
    }
    }
    }

      assign "True" to continue_Refund
      capture line:6, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:7, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:8, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:9, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:10, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:11, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:12, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:13, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:14, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:15, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:16, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:17, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:18, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:19, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:20, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:21, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:22, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }

    if (check_Refund_Eligibility != "INVALID"){
    if (tax_refund_eligible == "True"){
      if (AL_Code == "072"){
        send "FQC50USD" +"/" +DOI
        capture line:3, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:2 assign to totalNewPrice
    }
    capture line:3, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:3 assign to totalNewPrice
    }
    capture line:3, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:4 assign to totalNewPrice
    }
    capture line:3, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:5 assign to totalNewPrice
    }
    capture line:3, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:6 assign to totalNewPrice
    }
    capture line:3, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:7 assign to totalNewPrice
    }
    capture line:3, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:8 assign to totalNewPrice
    }
    capture line:3, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:9 assign to totalNewPrice
    }
    capture line:3, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:10 assign to totalNewPrice
    }
    capture line:3, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:11 assign to totalNewPrice
    }
    capture line:3, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:3, column:5, length:12 assign to totalNewPrice
    }
    assign totalNewPrice to tax_Penalty_Amount_GF
    send "TRFU/CP" +tax_Penalty_Amount_GF + "A"


        send "SRT2 YQYR"
      }
      if (AL_Code == "077"){
        send "TRFIG"
      }
      if (AL_Code == "079"){
        send "TRFIG"
      }
      if (AL_Code == "381"){
        send "SRT2 YQYR"
      }
      if (AL_Code == "607"){
        send "SRT2 YQYR"
      }
    }

    }

      call "TRFT_Deleter"
      capture line:6, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:7, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:8, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:9, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:10, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:11, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:12, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:13, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:14, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:15, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:16, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:17, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:18, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:19, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:20, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:21, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:22, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }

      if (AL_Code == "072"){
        send "SRT6 K3OAOBE3S4N9"
      }
      if (AL_Code == "077"){
        send "SRT9 CPE3S4XLQ7O7TNDZN9"
      }
      if (AL_Code == "079"){
        send "SRT6 E3S4K3N9OD6H"
      }
      if (AL_Code == "381"){
        send "SRT9 YQCPE3S4XLQ7O7TNDZ"
      }
      if (AL_Code == "607"){
        send "SRT15XPE3S4XLQ7O7TNDZN9PHYLUSK3ZPL8"
      }

      call "TRFT_Deleter"
      capture line:6, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:7, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:8, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:9, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:10, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:11, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:12, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:13, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:14, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:15, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:16, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:17, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:18, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:19, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:20, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:21, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }
      capture line:22, column:1, length:14 assign to negative_Refund
      if (negative_Refund == "INVALID UPDATE"){
        assign "False" to continue_Refund
      }
      if (negative_Refund == "INVALID CANCEL"){
        assign "False" to continue_Refund
      }

      if (continue_Refund == "True"){
        send "TRFU/NF"
        send "TRFP"
      }

  }// FARE RULES
  }
  else{ //ATC


assign "" to checkNP
if (PCC_ID =="71201675"){
  assign "/T-NP" to checkNP
}
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}
if (checkPending=="REFUND RECORD PENDING"){
send "TRFIG"
send "TRF" +TKTP1 +" " +TKTP2 +"-" +TKTP3 +"/ATC" +checkNP
}
capture line:1, column:1, length:21 assign to checkPending
if (checkPending=="NO FARE FOR BOOKING C"){
    send "TRFIG"
}
  
capture line:1, column:58, length:1 assign to checkATC
if (checkATC =="C"){

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
        capture line:1, column:1, length:24 assign to checkPending
        if (checkPending=="NEED ITINERARY INDICATOR"){
          send "TRFU/SI"
          send "TRFP"
        }
    }
    else{
      send "TRFU/FPA1" +totalRefundAmount
      send "TRFP"
      capture line:1, column:1, length:24 assign to checkPending
      if (checkPending=="NEED ITINERARY INDICATOR"){
          send "TRFU/SI"
          send "TRFP"
      }
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
        capture line:1, column:1, length:24 assign to checkPending
        if (checkPending=="NEED ITINERARY INDICATOR"){
          send "TRFU/SI"
          send "TRFP"
        }
    }
    else{
      send "TRFU/FPA1" +totalRefundAmount
      send "TRFP"
      capture line:1, column:1, length:24 assign to checkPending
      if (checkPending=="NEED ITINERARY INDICATOR"){
          send "TRFU/SI"
          send "TRFP"
      }
    }    
  }

}

}

}

send "TRFIG"
send "IG"