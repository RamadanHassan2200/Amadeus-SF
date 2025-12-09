    //After_VOID
    //retrirval
    mandatory ask "Enter the PNR: " assign to pnr
    send "IG"

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
        send "N0 After Void for today flights" +DOITEST
        ask "Ignore?" assign to qz5
        send "ig"
    }

    if (ticketingOffice!= thisOffice){
        send "PV/" +ticketingOffice
        mandatory ask "please continue in this office" assign to qz5
        send "ig"
    }

    capture line:4, column:47, length:1 assign to FST1
    if (FST1!="O"){
        if (FST1!="A"){
            send "Please check status!"
            ask "The CST checked in" assign to qz5
            send "ig"
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
            capture line:1, column:1, length:16 assign to check_Timout
            if (check_Timout=="XX ETKT TIME OUT"){
                send "FXR/K"+ref62 +FF_Statement
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
            capture line:11, column:10, length:1 assign to checkdot1
            capture line:12, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:11, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:12, column:10, length:1 assign to checkdot1
            capture line:13, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:12, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:13, column:10, length:1 assign to checkdot1
            capture line:14, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:13, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:14, column:10, length:1 assign to checkdot1
            capture line:15, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:14, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:15, column:10, length:1 assign to checkdot1
            capture line:16, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:15, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:16, column:10, length:1 assign to checkdot1
            capture line:17, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:16, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:17, column:10, length:1 assign to checkdot1
            capture line:18, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:17, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:18, column:10, length:1 assign to checkdot1
            capture line:19, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:18, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:19, column:10, length:1 assign to checkdot1
            capture line:20, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:19, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:20, column:10, length:1 assign to checkdot1
            capture line:21, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:20, column:4, length:10 assign to totalNewPrice
                }
            }
            capture line:21, column:10, length:1 assign to checkdot1
            capture line:22, column:10, length:1 assign to checkdot2
            if (checkdot1=="."){
                if (checkdot2!="."){
                    capture line:21, column:4, length:10 assign to totalNewPrice
                }
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

        send "FXR/K"+ref62 +FF_Statement +"/SBF"
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
        choose "Would you like to proceed with the refund?"{
            when ("Yes") {
                send "IR"
                send "RTJ"
                capture line:2, column:5, length:5 assign to apcheck2
                capture line:3, column:5, length:5 assign to apcheck3
                capture line:4, column:5, length:5 assign to apcheck4
                capture line:5, column:5, length:5 assign to apcheck5
                capture line:6, column:5, length:5 assign to apcheck6
                capture line:7, column:5, length:5 assign to apcheck7
                capture line:8, column:5, length:5 assign to apcheck8
                capture line:9, column:5, length:5 assign to apcheck9
                capture line:10, column:5, length:5 assign to apcheck10
                capture line:11, column:5, length:5 assign to apcheck11
                capture line:12, column:5, length:5 assign to apcheck12
                capture line:13, column:5, length:5 assign to apcheck13
                capture line:14, column:5, length:5 assign to apcheck14
                capture line:15, column:5, length:5 assign to apcheck15
                capture line:16, column:5, length:5 assign to apcheck16
                capture line:17, column:5, length:5 assign to apcheck17
                capture line:18, column:5, length:5 assign to apcheck18

                assign "" to APMDetails
                assign "0" to APM_Line
                assign "0" to APN_Line
                
                    if (apcheck2 == "APM +"){
                        assign "True" to VaildNo
                        capture line:2, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:2, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:2, column:10, length:12 assign to APMDetails
                        capture line:2, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck2 == "APN M"){
                        assign "True" to VaildNo
                        capture line:2, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:2, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:2, column:11, length:12 assign to APMDetails
                        capture line:2, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck3 == "APM +"){
                        assign "True" to VaildNo
                        capture line:3, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:3, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:3, column:10, length:12 assign to APMDetails
                        capture line:3, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck3 == "APN M"){
                        assign "True" to VaildNo
                        capture line:3, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:3, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:3, column:11, length:12 assign to APMDetails
                        capture line:3, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck4 == "APM +"){
                        assign "True" to VaildNo
                        capture line:4, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:4, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:4, column:10, length:12 assign to APMDetails
                        capture line:4, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck4 == "APN M"){
                        assign "True" to VaildNo
                        capture line:4, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:4, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:4, column:11, length:12 assign to APMDetails
                        capture line:4, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck5 == "APM +"){
                        assign "True" to VaildNo
                        capture line:5, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:5, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:5, column:10, length:12 assign to APMDetails
                        capture line:5, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck5 == "APN M"){
                        assign "True" to VaildNo
                        capture line:5, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:5, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:5, column:11, length:12 assign to APMDetails
                        capture line:5, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck6 == "APM +"){
                        assign "True" to VaildNo
                        capture line:6, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:6, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:6, column:10, length:12 assign to APMDetails
                        capture line:6, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck6 == "APN M"){
                        assign "True" to VaildNo
                        capture line:6, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:6, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:6, column:11, length:12 assign to APMDetails
                        capture line:6, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck7 == "APM +"){
                        assign "True" to VaildNo
                        capture line:7, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:7, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:7, column:10, length:12 assign to APMDetails
                        capture line:7, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck7 == "APN M"){
                        assign "True" to VaildNo
                        capture line:7, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:7, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:7, column:11, length:12 assign to APMDetails
                        capture line:7, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck8 == "APM +"){
                        assign "True" to VaildNo
                        capture line:8, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:8, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:8, column:10, length:12 assign to APMDetails
                        capture line:8, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck8 == "APN M"){
                        assign "True" to VaildNo
                        capture line:8, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:8, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:8, column:11, length:12 assign to APMDetails
                        capture line:8, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck9 == "APM +"){
                        assign "True" to VaildNo
                        capture line:9, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:9, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:9, column:10, length:12 assign to APMDetails
                        capture line:9, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck9 == "APN M"){
                        assign "True" to VaildNo
                        capture line:9, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:9, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:9, column:11, length:12 assign to APMDetails
                        capture line:9, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck10 == "APM +"){
                        assign "True" to VaildNo
                        capture line:10, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:10, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:10, column:10, length:12 assign to APMDetails
                        capture line:10, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck10 == "APN M"){
                        assign "True" to VaildNo
                        capture line:10, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:10, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:10, column:11, length:12 assign to APMDetails
                        capture line:10, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck11 == "APM +"){
                        assign "True" to VaildNo
                        capture line:11, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:11, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:11, column:10, length:12 assign to APMDetails
                        capture line:11, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck11 == "APN M"){
                        assign "True" to VaildNo
                        capture line:11, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:11, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:11, column:11, length:12 assign to APMDetails
                        capture line:11, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck12 == "APM +"){
                        assign "True" to VaildNo
                        capture line:12, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:12, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:12, column:10, length:12 assign to APMDetails
                        capture line:12, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck12 == "APN M"){
                        assign "True" to VaildNo
                        capture line:12, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:12, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:12, column:11, length:12 assign to APMDetails
                        capture line:12, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck13 == "APM +"){
                        assign "True" to VaildNo
                        capture line:13, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:13, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:13, column:10, length:12 assign to APMDetails
                        capture line:13, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck13 == "APN M"){
                        assign "True" to VaildNo
                        capture line:13, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:13, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:13, column:11, length:12 assign to APMDetails
                        capture line:13, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck14 == "APM +"){
                        assign "True" to VaildNo
                        capture line:14, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:14, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:14, column:10, length:12 assign to APMDetails
                        capture line:14, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck14 == "APN M"){
                        assign "True" to VaildNo
                        capture line:14, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:14, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:14, column:11, length:12 assign to APMDetails
                        capture line:14, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck15 == "APM +"){
                        assign "True" to VaildNo
                        capture line:15, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:15, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:15, column:10, length:12 assign to APMDetails
                        capture line:15, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck15 == "APN M"){
                        assign "True" to VaildNo
                        capture line:15, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:15, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:15, column:11, length:12 assign to APMDetails
                        capture line:15, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck16 == "APM +"){
                        assign "True" to VaildNo
                        capture line:16, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:16, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:16, column:10, length:12 assign to APMDetails
                        capture line:16, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck16 == "APN M"){
                        assign "True" to VaildNo
                        capture line:16, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:16, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:16, column:11, length:12 assign to APMDetails
                        capture line:16, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck17 == "APM +"){
                        assign "True" to VaildNo
                        capture line:17, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:17, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:17, column:10, length:12 assign to APMDetails
                        capture line:17, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck17 == "APN M"){
                        assign "True" to VaildNo
                        capture line:17, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:17, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:17, column:11, length:12 assign to APMDetails
                        capture line:17, column:1, length:3 assign to APN_Line
                    }

                    if (apcheck18 == "APM +"){
                        assign "True" to VaildNo
                        capture line:18, column:9, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:18, column:22, length:1 assign to apmNo
                        if (apmNo>="0"){
                            if (apmNo<="9"){
                                assign "False" to VaildNo
                            }
                        }

                        capture line:18, column:10, length:12 assign to APMDetails
                        capture line:18, column:1, length:3 assign to APM_Line
                    }

                    if (apcheck18 == "APN M"){
                        assign "True" to VaildNo
                        capture line:18, column:10, length:1 assign to apmNo
                        if (apmNo!="+"){
                            assign "False" to VaildNo
                        }
                        capture line:18, column:23, length:1 assign to apmNo
                        if (apmNo!="/"){
                            assign "False" to VaildNo
                        }

                        capture line:18, column:11, length:12 assign to APMDetails
                        capture line:18, column:1, length:3 assign to APN_Line
                    }

                    if (VaildNo== "False"){
                        ask "Please write the Mobile Number Correctly:" assign to APMDetails
                    }
                    if (APM_Line != "0"){
                        send "XE" +APM_Line 
                    }
                    if (APN_Line != "0"){
                        send "XE" +APN_Line
                    }
                    send "APM-+" +APMDetails
                    send "APN-M+" +APMDetails +"/AR/p1"

                send "rf" +agtName +";er"
                send "er"
                
                send "IR"
                send "TTE/all"
                if (SBF_Check == "True"){
                    send "FXB/K"+ref62 +FF_Statement +"/SBF"
                }
                else{
                    send "FXB/K"+ref62 +FF_Statement
                }
                
                send "rf" +agtName +";er"
                send "er"
                send "IG"

        if (FA_Check_TRUE_FALSE1 == "True"){
        send "TRFIG"
        send "TRF" +Tn1FA1 +" "+Tn1FA2 +"/ATC" +NPcheck    
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFig"
                    send "TRF" +Tn1FA1 +" "+Tn1FA2 +"/ATC" +NPcheck
                    send "TRFU/NF"
                    
                    call "TRFP"
                    capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }


    if (FA_Check_TRUE_FALSE2 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn2FA1 +" "+Tn2FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFig"
                    send "TRF" +Tn2FA1 +" "+Tn2FA2 +"/ATC" +NPcheck
                    send "TRFU/NF"
                    
                    call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE3 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn3FA1 +" "+Tn3FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE4 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn4FA1 +" "+Tn4FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE5 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn5FA1 +" "+Tn5FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE6 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn6FA1 +" "+Tn6FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE7 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn7FA1 +" "+Tn7FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE8 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn8FA1 +" "+Tn8FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE9 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn9FA1 +" "+Tn9FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE10 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn10FA1 +" "+Tn10FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE11 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn11FA1 +" "+Tn11FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE12 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn12FA1 +" "+Tn12FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE13 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn13FA1 +" "+Tn13FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE14 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn14FA1 +" "+Tn14FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }

    if (FA_Check_TRUE_FALSE15 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn15FA1 +" "+Tn15FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }


    if (FA_Check_TRUE_FALSE16 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn16FA1 +" "+Tn16FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }


    if (FA_Check_TRUE_FALSE17 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn17FA1 +" "+Tn17FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }
            }
            when ("No, ignore!") {

            }
        }
    }
    }


    if (FA_Check_TRUE_FALSE18 == "True"){
        ask "Do you want to continue with the next ticket?" assign to qz6
        send "TRFIG"
        send "TRF" +Tn18FA1 +" "+Tn18FA2 +"/ATC" +NPcheck
        capture line:1, column:58, length:1 assign to checkATC
    if (checkATC =="C"){
        send "TRFU/NF"
        
        call "TRFP"
        capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
    }
    else{
        choose "Do you want to refund?"{
            when ("Yes") {
                send "TRFU/NF"
                
                call "TRFP"
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                capture line:2, column:1, length:21 assign to checkRefundProcessed
                if (checkRefundProcessed != "OK - REFUND PROCESSED"){
                    send "TRFP"
                }
                }
            }
            when ("No, Update Needed!") {
                choose "Do you want to continue manually?" until "Done!"{
                    when ("input another command") {
                        ask "Enter command..." assign to command1
                        send command1
                    }
                }   
            }
            when ("No, ignore!") {

            }
        }
    }
    }
        
                send "RT" +pnr
                send "IR"
                send "IR"
                call "z_FOPCASH_DEL"
                send "FPCASH"
                send "FM0"
                call "z_RTTN_DEL"
                send "rf" +agtName +";er"
                send "er"
                call "Check HK Segment"

            }
            when ("No") {
                send "TRFIG"
                send "IG"
            }
        }
    }
    else{
        send "NO After-Void Deal (" +totalDealAmount +")"
        ask "Ignore?" assign to qz6
        send "TRFIG"
        send "IG"
    }
        call "After_VOID"