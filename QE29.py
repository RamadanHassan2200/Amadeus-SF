
send "RTA"
    capture line:2, column:58, length:6 assign to PNR

    capture line:2, column:30, length:2 assign to HK1Test
    if (HK1Test=="HK"){
    assign "1" to segmentsCount
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
                        send "IR"
                        send "QN"
                        call "QE29"
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
    capture line:3, column:35, length:4 assign to TravelTime
    capture line:3, column:35, length:2 assign to TravelTime1
    capture line:3, column:37, length:2 assign to TravelTime2
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
                            send "IR"
                            send "QN"
                            call "QE29"
                        }
                    }
                }
            }
            }
        }
    }
    else{
        send "IR"
        send "QN"
        call "QE29"
    }
    }

    // ignore >4 segments or >6 passengers

    if (Airline1=="H1"){
        send "H1 airline is non-refundable"
        ask "Stop and Review" assign to qz5
        send "IR"
        send "QN"
    }
    if (Airline1=="R5"){
        send "R5 airline is non-refundable"
        ask "Stop and Review" assign to qz5
        send "IR"
        send "QN"
    }

    //Today dates aren't considered
    send  "DD" +OriginCity
    capture line:2, column:13, length:2 assign to OriginCityCurrentTime1
    capture line:2, column:15, length:2 assign to OriginCityCurrentTime2
    capture line:2, column:30, length:5 assign to OriginCityCurrentDate
    send "DD" +OriginCityCurrentDate +"/" + TravelDate
    capture line:2, column:1, length:1 assign to checkpast
    capture line:2, column:1, length:3 assign to checktoday
    if (checkpast == "-"){
        send "IR"
        send "QN"
        call "QE29"
    }
    if (checktoday == " 0 "){
        send "DF"  +TravelTime1 +"*60-" +TravelTime2 +"-" +OriginCityCurrentTime1 +"*60;" +OriginCityCurrentTime2 
        capture line:2, column:1, length:1 assign to checkTimePast
        capture line:2, column:1, length:5 assign to checkTimeDifference
        if (checkTimePast == "-"){
        send "IR"
        send "QN"
        call "QE29"
        }
        if (checkTimeDifference<= "120"){
        send "IR"
        send "QN"
        call "QE29"
        }
    }

    if (checktoday == " 1 "){
        send "IR"
        send "QN"
        call "QE29"
    }


    send "tqm"
            capture line:1, column:1, length:20 assign to emdTest
            if (emdTest != "NO TSM RECORD EXISTS"){
            send "IR"
            send "QN"
            call "QE29"
            }

    //getting the office IATA code
    send "PV"
    capture line:8, column:30, length:8 assign to thisOffice
    capture line:2, column:30, length:9 assign to thisOfficeName

        //opening the ticket:
    send "rttn"
    assign "" to FACount

    assign "FALSE" to FA_Check_TRUE_FALSE1
    assign "FALSE" to FA_Check_TRUE_FALSE2
    assign "FALSE" to FA_Check_TRUE_FALSE3
    assign "FALSE" to FA_Check_TRUE_FALSE4
    assign "FALSE" to FA_Check_TRUE_FALSE5
    assign "FALSE" to FA_Check_TRUE_FALSE6
    assign "FALSE" to FA_Check_TRUE_FALSE7
    assign "FALSE" to FA_Check_TRUE_FALSE8
    assign "FALSE" to FA_Check_TRUE_FALSE9
    assign "FALSE" to FA_Check_TRUE_FALSE10
    assign "FALSE" to FA_Check_TRUE_FALSE11
    assign "FALSE" to FA_Check_TRUE_FALSE12
    assign "FALSE" to FA_Check_TRUE_FALSE13
    assign "FALSE" to FA_Check_TRUE_FALSE14
    assign "FALSE" to FA_Check_TRUE_FALSE15
    assign "FALSE" to FA_Check_TRUE_FALSE16
    assign "FALSE" to FA_Check_TRUE_FALSE17
    assign "FALSE" to FA_Check_TRUE_FALSE18
    assign "FALSE" to FA_Check_TRUE_FALSE19

    capture line:2, column:5, length:3 assign to FA_Test
    capture line:2, column:26, length:3 assign to ET_TEST
    capture line:2, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE1
                    capture line:2, column:12, length:1 assign to Tn1FA1
                    capture line:2, column:13, length:13 assign to Tn1FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE1
                    capture line:2, column:12, length:1 assign to Tn1FA1
                    capture line:2, column:13, length:13 assign to Tn1FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE1
                capture line:2, column:13, length:1 assign to Tn1FA1
                capture line:2, column:14, length:13 assign to Tn1FA2
            }

            capture line:3, column:5, length:3 assign to FA_Test
            capture line:3, column:26, length:3 assign to ET_TEST
            capture line:3, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE2
                    capture line:3, column:12, length:1 assign to Tn2FA1
                    capture line:3, column:13, length:13 assign to Tn2FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE2
                    capture line:3, column:12, length:1 assign to Tn2FA1
                    capture line:3, column:13, length:13 assign to Tn2FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE2
                capture line:3, column:13, length:1 assign to Tn2FA1
                capture line:3, column:14, length:13 assign to Tn2FA2
            }

            capture line:4, column:5, length:3 assign to FA_Test
            capture line:4, column:26, length:3 assign to ET_TEST
            capture line:4, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE3
                    capture line:4, column:12, length:1 assign to Tn3FA1
                    capture line:4, column:13, length:13 assign to Tn3FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE3
                    capture line:4, column:12, length:1 assign to Tn3FA1
                    capture line:4, column:13, length:13 assign to Tn3FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE3
                capture line:4, column:13, length:1 assign to Tn3FA1
                capture line:4, column:14, length:13 assign to Tn3FA2
            }

            capture line:5, column:5, length:3 assign to FA_Test
            capture line:5, column:26, length:3 assign to ET_TEST
            capture line:5, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE4
                    capture line:5, column:12, length:1 assign to Tn4FA1
                    capture line:5, column:13, length:13 assign to Tn4FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE4
                    capture line:5, column:12, length:1 assign to Tn4FA1
                    capture line:5, column:13, length:13 assign to Tn4FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE4
                capture line:5, column:13, length:1 assign to Tn4FA1
                capture line:5, column:14, length:13 assign to Tn4FA2
            }

            capture line:6, column:5, length:3 assign to FA_Test
            capture line:6, column:26, length:3 assign to ET_TEST
            capture line:6, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE5
                    capture line:6, column:12, length:1 assign to Tn5FA1
                    capture line:6, column:13, length:13 assign to Tn5FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE5
                    capture line:6, column:12, length:1 assign to Tn5FA1
                    capture line:6, column:13, length:13 assign to Tn5FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE5
                capture line:6, column:13, length:1 assign to Tn5FA1
                capture line:6, column:14, length:13 assign to Tn5FA2
            }
            capture line:7, column:5, length:3 assign to FA_Test
            capture line:7, column:26, length:3 assign to ET_TEST
            capture line:7, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE6
                    capture line:7, column:12, length:1 assign to Tn6FA1
                    capture line:7, column:13, length:13 assign to Tn6FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE6
                    capture line:7, column:12, length:1 assign to Tn6FA1
                    capture line:7, column:13, length:13 assign to Tn6FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE6
                capture line:7, column:13, length:1 assign to Tn6FA1
                capture line:7, column:14, length:13 assign to Tn6FA2
            }

            capture line:8, column:5, length:3 assign to FA_Test
            capture line:8, column:26, length:3 assign to ET_TEST
            capture line:8, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE7
                    capture line:8, column:12, length:1 assign to Tn7FA1
                    capture line:8, column:13, length:13 assign to Tn7FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE7
                    capture line:8, column:12, length:1 assign to Tn7FA1
                    capture line:8, column:13, length:13 assign to Tn7FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE7
                capture line:8, column:13, length:1 assign to Tn7FA1
                capture line:8, column:14, length:13 assign to Tn7FA2
            }

            capture line:9, column:5, length:3 assign to FA_Test
            capture line:9, column:26, length:3 assign to ET_TEST
            capture line:9, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE8
                    capture line:9, column:12, length:1 assign to Tn8FA1
                    capture line:9, column:13, length:13 assign to Tn8FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE8
                    capture line:9, column:12, length:1 assign to Tn8FA1
                    capture line:9, column:13, length:13 assign to Tn8FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE8
                capture line:9, column:13, length:1 assign to Tn8FA1
                capture line:9, column:14, length:13 assign to Tn8FA2
            }
            
            capture line:10, column:5, length:3 assign to FA_Test
            capture line:10, column:26, length:3 assign to ET_TEST
            capture line:10, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE9
                    capture line:10, column:12, length:1 assign to Tn9FA1
                    capture line:10, column:13, length:13 assign to Tn9FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE9
                    capture line:10, column:12, length:1 assign to Tn9FA1
                    capture line:10, column:13, length:13 assign to Tn9FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE9
                capture line:10, column:13, length:1 assign to Tn9FA1
                capture line:10, column:14, length:13 assign to Tn9FA2
            }

            capture line:11, column:5, length:3 assign to FA_Test
            capture line:11, column:26, length:3 assign to ET_TEST
            capture line:11, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE10
                    capture line:11, column:12, length:1 assign to Tn10FA1
                    capture line:11, column:13, length:13 assign to Tn10FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE10
                    capture line:11, column:12, length:1 assign to Tn10FA1
                    capture line:11, column:13, length:13 assign to Tn10FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE10
                capture line:11, column:13, length:1 assign to Tn10FA1
                capture line:11, column:14, length:13 assign to Tn10FA2
            }

            capture line:12, column:5, length:3 assign to FA_Test
            capture line:12, column:26, length:3 assign to ET_TEST
            capture line:12, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE11
                    capture line:12, column:12, length:1 assign to Tn11FA1
                    capture line:12, column:13, length:13 assign to Tn11FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE11
                    capture line:12, column:12, length:1 assign to Tn11FA1
                    capture line:12, column:13, length:13 assign to Tn11FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE11
                capture line:12, column:13, length:1 assign to Tn11FA1
                capture line:12, column:14, length:13 assign to Tn11FA2
            }

            capture line:13, column:5, length:3 assign to FA_Test
            capture line:13, column:26, length:3 assign to ET_TEST
            capture line:13, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE12
                    capture line:13, column:12, length:1 assign to Tn12FA1
                    capture line:13, column:13, length:13 assign to Tn12FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE12
                    capture line:13, column:12, length:1 assign to Tn12FA1
                    capture line:13, column:13, length:13 assign to Tn12FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE12
                capture line:13, column:13, length:1 assign to Tn12FA1
                capture line:13, column:14, length:13 assign to Tn12FA2
            }

            capture line:14, column:5, length:3 assign to FA_Test
            capture line:14, column:26, length:3 assign to ET_TEST
            capture line:14, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE13
                    capture line:14, column:12, length:1 assign to Tn13FA1
                    capture line:14, column:13, length:13 assign to Tn13FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE13
                    capture line:14, column:12, length:1 assign to Tn13FA1
                    capture line:14, column:13, length:13 assign to Tn13FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE13
                capture line:14, column:13, length:1 assign to Tn13FA1
                capture line:14, column:14, length:13 assign to Tn13FA2
            }

            capture line:15, column:5, length:3 assign to FA_Test
            capture line:15, column:26, length:3 assign to ET_TEST
            capture line:15, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE14
                    capture line:15, column:12, length:1 assign to Tn14FA1
                    capture line:15, column:13, length:13 assign to Tn14FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE14
                    capture line:15, column:12, length:1 assign to Tn14FA1
                    capture line:15, column:13, length:13 assign to Tn14FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE14
                capture line:15, column:13, length:1 assign to Tn14FA1
                capture line:15, column:14, length:13 assign to Tn14FA2
            }

            capture line:16, column:5, length:3 assign to FA_Test
            capture line:16, column:26, length:3 assign to ET_TEST
            capture line:16, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE15
                    capture line:16, column:12, length:1 assign to Tn15FA1
                    capture line:16, column:13, length:13 assign to Tn15FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE15
                    capture line:16, column:12, length:1 assign to Tn15FA1
                    capture line:16, column:13, length:13 assign to Tn15FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE15
                capture line:16, column:13, length:1 assign to Tn15FA1
                capture line:16, column:14, length:13 assign to Tn15FA2
            }

            capture line:17, column:5, length:3 assign to FA_Test
            capture line:17, column:26, length:3 assign to ET_TEST
            capture line:17, column:29, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE16
                    capture line:17, column:12, length:1 assign to Tn16FA1
                    capture line:17, column:13, length:13 assign to Tn16FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE16
                    capture line:17, column:12, length:1 assign to Tn16FA1
                    capture line:17, column:13, length:13 assign to Tn16FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE16
                capture line:17, column:13, length:1 assign to Tn16FA1
                capture line:17, column:14, length:13 assign to Tn16FA2
            }

            capture line:18, column:5, length:3 assign to FA_Test
            capture line:18, column:26, length:3 assign to ET_TEST
            capture line:18, column:27, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE17
                    capture line:18, column:12, length:1 assign to Tn17FA1
                    capture line:18, column:13, length:13 assign to Tn17FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE17
                    capture line:18, column:12, length:1 assign to Tn17FA1
                    capture line:18, column:13, length:13 assign to Tn17FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE17
                capture line:18, column:13, length:1 assign to Tn17FA1
                capture line:18, column:14, length:13 assign to Tn17FA2
            }

            capture line:19, column:5, length:3 assign to FA_Test
            capture line:19, column:26, length:3 assign to ET_TEST
            capture line:19, column:27, length:3 assign to ET_TESTA
            if (FA_Test=="FA "){
                if (ET_TEST=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE18
                    capture line:19, column:12, length:1 assign to Tn18FA1
                    capture line:19, column:13, length:13 assign to Tn18FA2
                }
                if (ET_TESTA=="/ET"){
                    append "1" to FACount
                    assign "TRUE" to FA_Check_TRUE_FALSE18
                    capture line:19, column:12, length:1 assign to Tn18FA1
                    capture line:19, column:13, length:13 assign to Tn18FA2
                }
            }
            if (FA_Test=="FHE"){
                append "1" to FACount
                assign "TRUE" to FA_Check_TRUE_FALSE18
                capture line:19, column:13, length:1 assign to Tn18FA1
                capture line:19, column:14, length:13 assign to Tn18FA2
            }

    send "TWD/TKT" + Tn1FA1 + Tn1FA2
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        
    }
    capture line:1, column:1, length:14 assign to checkNextTKT
    if (checkNextTKT=="INVALID FORMAT"){
        send "TWD/TKT" + Tn2FA1 + Tn2FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" + Tn2FA1 + Tn2FA2
    }
    capture line:3, column:32, length:3 assign to PAXST
    if (PAXST=="INF"){
    send "TWD/TKT" +Tn2FA1 + Tn2FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" +Tn2FA1 + Tn2FA2
    }
    capture line:1, column:1, length:14 assign to checkNextTKT
    if (checkNextTKT=="INVALID FORMAT"){
        send "TWD/TKT" + Tn3FA1 + Tn3FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" + Tn3FA1 + Tn3FA2
    }
    capture line:3, column:32, length:3 assign to PAXST
    if (PAXST=="INF"){
    send "TWD/TKT" +Tn3FA1 + Tn3FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" +Tn3FA1 + Tn3FA2
    }
    capture line:1, column:1, length:14 assign to checkNextTKT
    if (checkNextTKT=="INVALID FORMAT"){
        send "TWD/TKT" + Tn4FA1 + Tn4FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" + Tn4FA1 + Tn4FA2
    }
    capture line:3, column:32, length:3 assign to PAXST
    if (PAXST=="INF"){
    send "TWD/TKT" +Tn4FA1 + Tn4FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" +Tn4FA1 + Tn4FA2
    }
    capture line:1, column:1, length:14 assign to checkNextTKT
    if (checkNextTKT=="INVALID FORMAT"){
        send "TWD/TKT" + Tn5FA1 + Tn6FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" + Tn5FA1 + Tn6FA2
    }
    capture line:3, column:32, length:3 assign to PAXST
    if (PAXST=="INF"){
    send "TWD/TKT" +Tn5FA1 + Tn5FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" +Tn5FA1 + Tn5FA2
    }
    capture line:1, column:1, length:14 assign to checkNextTKT
    if (checkNextTKT=="INVALID FORMAT"){
        send "TWD/TKT" + Tn6FA1 + Tn6FA2
    }
    capture line:1, column:1, length:16 assign to check_Timout
    if (check_Timout=="XX ETKT TIME OUT"){
        send "TWD/TKT" + Tn6FA1 + Tn6FA2
    }

    capture line:2, column:44, length:5 assign to DOITEST
        capture line:2, column:57, length:8 assign to ticketingOffice

    if (DOITEST==today){
        send "FXR/K"
        call "fast_search"
        send "IR"
        send "QN"
    }

    if (ticketingOffice!= thisOffice){
        send "FXR/K"
        call "fast_search"
        send "IR"
        send "QN"
    }

    capture line:4, column:47, length:1 assign to FST1
    if (FST1!="O"){
        if (FST1!="A"){
            send "Please check status!"
            ask "The CST checked in" assign to qz5
        }
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
            send "FXR/K"+ref62
            capture line:1, column:1, length:16 assign to check_Timout
            if (check_Timout=="XX ETKT TIME OUT"){
                send "FXR/K"+ref62
            }

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
            capture line:6, column:13, length:3 assign to checknewXT6
            capture line:7, column:13, length:3 assign to checknewXT7
            capture line:8, column:13, length:3 assign to checknewXT8
            capture line:9, column:13, length:3 assign to checknewXT9
            capture line:10, column:13, length:3 assign to checknewXT10
            capture line:11, column:13, length:3 assign to checknewXT11
            capture line:12, column:13, length:3 assign to checknewXT12
            capture line:13, column:13, length:3 assign to checknewXT13
            capture line:14, column:13, length:3 assign to checknewXT14
            capture line:15, column:13, length:3 assign to checknewXT15
            capture line:16, column:13, length:3 assign to checknewXT16
            capture line:17, column:13, length:3 assign to checknewXT17
            capture line:18, column:13, length:3 assign to checknewXT18
            capture line:19, column:13, length:3 assign to checknewXT19
            capture line:20, column:13, length:3 assign to checknewXT20
            capture line:21, column:13, length:3 assign to checknewXT21
            capture line:22, column:13, length:3 assign to checknewXT22

            if (checknewXT6 == "-XT"){
                capture line:7, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT7 == "-XT"){
                capture line:8, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT8 == "-XT"){
                capture line:9, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT9 == "-XT"){
                capture line:10, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT10 == "-XT"){
                capture line:11, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT11 == "-XT"){
                capture line:12, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT12 == "-XT"){
                capture line:13, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT13 == "-XT"){
                capture line:14, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT14 == "-XT"){
                capture line:15, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT15 == "-XT"){
                capture line:16, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT16 == "-XT"){
                capture line:17, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT17 == "-XT"){
                capture line:18, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT18 == "-XT"){
                capture line:19, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT19 == "-XT"){
                capture line:20, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT20 == "-XT"){
                capture line:21, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT21 == "-XT"){
                capture line:22, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT22 == "-XT"){
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
        ask "Continue with SBF?" assign to qz5

        send "FXR/K"+ref62 +"/SBF"
        assign "True" to SBF_Check


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
            capture line:6, column:13, length:3 assign to checknewXT6
            capture line:7, column:13, length:3 assign to checknewXT7
            capture line:8, column:13, length:3 assign to checknewXT8
            capture line:9, column:13, length:3 assign to checknewXT9
            capture line:10, column:13, length:3 assign to checknewXT10
            capture line:11, column:13, length:3 assign to checknewXT11
            capture line:12, column:13, length:3 assign to checknewXT12
            capture line:13, column:13, length:3 assign to checknewXT13
            capture line:14, column:13, length:3 assign to checknewXT14
            capture line:15, column:13, length:3 assign to checknewXT15
            capture line:16, column:13, length:3 assign to checknewXT16
            capture line:17, column:13, length:3 assign to checknewXT17
            capture line:18, column:13, length:3 assign to checknewXT18
            capture line:19, column:13, length:3 assign to checknewXT19
            capture line:20, column:13, length:3 assign to checknewXT20
            capture line:21, column:13, length:3 assign to checknewXT21
            capture line:22, column:13, length:3 assign to checknewXT22

            if (checknewXT6 == "-XT"){
                capture line:7, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT7 == "-XT"){
                capture line:8, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT8 == "-XT"){
                capture line:9, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT9 == "-XT"){
                capture line:10, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT10 == "-XT"){
                capture line:11, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT11 == "-XT"){
                capture line:12, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT12 == "-XT"){
                capture line:13, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT13 == "-XT"){
                capture line:14, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT14 == "-XT"){
                capture line:15, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT15 == "-XT"){
                capture line:16, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT16 == "-XT"){
                capture line:17, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT17 == "-XT"){
                capture line:18, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT18 == "-XT"){
                capture line:19, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT19 == "-XT"){
                capture line:20, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT20 == "-XT"){
                capture line:21, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT21 == "-XT"){
                capture line:22, column:4, length:10 assign to totalNewPrice
            }
            if (checknewXT22 == "-XT"){
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
        assign "True" to incorrect_Baggage
        }

        }//first baggage check

    assign "" to NPcheck
    if (thisOfficeName=="RUHAA2300"){
        assign "/T-NP"  to NPcheck
    }

    assign "0" to  totalRefundAmount
    if (FA_Check_TRUE_FALSE1 == "True"){
        send "TRFIG"
        send "TRF" +Tn1FA1 +" "+Tn1FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn1FA1 +" "+Tn1FA2 +"/ATC" +NPcheck  
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        

    }

    if (FA_Check_TRUE_FALSE2 == "True"){
        send "TRFIG"
        send "TRF" +Tn2FA1 +" "+Tn2FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn2FA1 +" "+Tn2FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE3 == "True"){
        send "TRFIG"
        send "TRF" +Tn3FA1 +" "+Tn3FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn3FA1 +" "+Tn3FA2 +"/ATC" +NPcheck   
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE4 == "True"){
        send "TRFIG"
        send "TRF" +Tn4FA1 +" "+Tn4FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn4FA1 +" "+Tn4FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        

    }

    if (FA_Check_TRUE_FALSE5 == "True"){
        send "TRFIG"
        send "TRF" +Tn5FA1 +" "+Tn5FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn5FA1 +" "+Tn5FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        

    }

    if (FA_Check_TRUE_FALSE6 == "True"){
        send "TRFIG"
        send "TRF" +Tn6FA1 +" "+Tn6FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn6FA1 +" "+Tn6FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE7 == "True"){
        send "TRFIG"
        send "TRF" +Tn7FA1 +" "+Tn7FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn7FA1 +" "+Tn7FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE8 == "True"){
        send "TRFIG"
        send "TRF" +Tn8FA1 +" "+Tn8FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn8FA1 +" "+Tn8FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE9 == "True"){
        send "TRFIG"
        send "TRF" +Tn9FA1 +" "+Tn9FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn9FA1 +" "+Tn9FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE10 == "True"){
        send "TRFIG"
        send "TRF" +Tn10FA1 +" "+Tn10FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn10FA1 +" "+Tn10FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE11 == "True"){
        send "TRFIG"
        send "TRF" +Tn11FA1 +" "+Tn11FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn11FA1 +" "+Tn11FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE12 == "True"){
        send "TRFIG"
        send "TRF" +Tn12FA1 +" "+Tn12FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn12FA1 +" "+Tn12FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE13 == "True"){
        send "TRFIG"
        send "TRF" +Tn13FA1 +" "+Tn13FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn13FA1 +" "+Tn13FA2 +"/ATC" +NPcheck 
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE14 == "True"){
        send "TRFIG"
        send "TRF" +Tn14FA1 +" "+Tn14FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn14FA1 +" "+Tn14FA2 +"/ATC" +NPcheck   
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE15 == "True"){
        send "TRFIG"
        send "TRF" +Tn15FA1 +" "+Tn15FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn15FA1 +" "+Tn15FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    if (FA_Check_TRUE_FALSE16 == "True"){
        send "TRFIG"
        send "TRF" +Tn16FA1 +" "+Tn16FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn16FA1 +" "+Tn16FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        

    }

    if (FA_Check_TRUE_FALSE17 == "True"){
        send "TRFIG"
        send "TRF" +Tn17FA1 +" "+Tn17FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn17FA1 +" "+Tn17FA2 +"/ATC" +NPcheck 
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }
        
    }

    if (FA_Check_TRUE_FALSE18 == "True"){
        send "TRFIG"
        send "TRF" +Tn18FA1 +" "+Tn18FA2 +"/ATC" +NPcheck
        capture line:1, column:1, length:16 assign to check_Timout
        if (check_Timout=="XX ETKT TIME OUT"){
            send "TRF" +Tn18FA1 +" "+Tn18FA2 +"/ATC" +NPcheck
        }
        capture line:1, column:58, length:1 assign to checkATC
        assign "Not Guranteed" to totalRefundEligibility
        if (checkATC =="C"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (checkATC =="U"){
            assign "Guranteed" to totalRefundEligibility 
        }
        if (totalRefundEligibility == "Guranteed"){
        capture line:10, column:5, length:12 assign to totalRefundcheck1
        capture line:11, column:5, length:12 assign to totalRefundcheck2
        capture line:12, column:5, length:12 assign to totalRefundcheck3
        if (totalRefundcheck1 == "REFUND TOTAL"){
            capture line:10, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck2 == "REFUND TOTAL"){
            capture line:11, column:33, length:10 assign to ticketRefundAmount
        }
        if (totalRefundcheck3 == "REFUND TOTAL"){
            capture line:12, column:33, length:10 assign to ticketRefundAmount
        }
        append ";" + ticketRefundAmount to totalRefundAmount
        }

    }

    send "DF" +totalRefundAmount 
    capture line:6, column:1, length:1 assign to dfnextcheck
    if (dfnextcheck == ">"){
        capture line:4, column:1, length:10 assign to totalRefundAmount
    }
    capture line:5, column:1, length:1 assign to dfnextcheck
    if (dfnextcheck == ">"){
        capture line:3, column:1, length:10 assign to totalRefundAmount
    }
    capture line:4, column:1, length:1 assign to dfnextcheck
    if (dfnextcheck == ">"){
        capture line:2, column:1, length:10 assign to totalRefundAmount
    }

    send "DF" +totalRefundAmount +"-" +totalNewPrice
    capture line:2, column:1, length:10 assign to totalDealAmount


    if (totalDealAmount >"0"){
        if (incorrect_Baggage == "True"){
            send "PNR: "+PNR + " - " +totalDealAmount + " - Baggage Issue: YES" 
        }
        else{
            send "PNR: "+PNR + " - " +totalDealAmount 
        }
        ask "Please continue with it in another tab," assign to qz6
        send "IR"
        send "QN"
        call "QE29"
    }
    else{
        send "IR"
        send "QN"
        call "QE29" 
    }