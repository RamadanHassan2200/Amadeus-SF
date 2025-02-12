ask "where is pnr?" assign to pnr
        send "rt" + pnr
        send "rttn"

        ask "Enter the Ticket Number" assign to TicketNumber
        ask "where is tourcode" assign to tourcode
       assign  "" to tourcode1
        if (tourcode != "" ){
            if ( tourcode != " "){
                append "," + tourcode to tourcode1
            }
        }
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
    }

    capture line:1, column:5, length:1 assign to TKTP1
    capture line:1, column:6, length:2 assign to TKTP2
    capture line:1, column:8, length:10 assign to TKTP3

    capture line:2, column:44, length:7 assign to DOI

    capture line:3, column:6, length:26 assign to PAXNAME

    capture line:4, column:4, length:1 assign to original1
    capture line:4, column:5, length:3 assign to city1
    capture line:4, column:9, length:2 assign to airline1
    capture line:4, column:11, length:4 assign to flightNo1
    capture line:4, column:18, length:1 assign to class1
    capture line:4, column:20, length:5 assign to travelDate1
    capture line:4, column:30, length:2 assign to OK1
    capture line:4, column:33, length:12 assign to fareBasis1
    capture line:4, column:47, length:1 assign to status1

    capture line:5, column:4, length:1 assign to original2  
    capture line:5, column:5, length:3 assign to city2
    capture line:5, column:9, length:2 assign to airline2
    capture line:5, column:11, length:4 assign to flightNo2
    capture line:5, column:18, length:1 assign to class2
    capture line:5, column:20, length:5 assign to travelDate2
    capture line:5, column:30, length:2 assign to OK2
    capture line:5, column:33, length:12 assign to fareBasis2
    capture line:5, column:47, length:1 assign to status2

    capture line:6, column:4, length:1 assign to original3
    capture line:6, column:5, length:3 assign to city3
    capture line:6, column:9, length:2 assign to airline3
    capture line:6, column:11, length:4 assign to flightNo3
    capture line:6, column:18, length:1 assign to class3
    capture line:6, column:20, length:5 assign to travelDate3
    capture line:6, column:30, length:2 assign to OK3
    capture line:6, column:33, length:12 assign to fareBasis3
    capture line:6, column:47, length:1 assign to status3

    capture line:7, column:4, length:1 assign to original4
    capture line:7, column:5, length:3 assign to city4
    capture line:7, column:9, length:2 assign to airline4
    capture line:7, column:11, length:4 assign to flightNo4
    capture line:7, column:18, length:1 assign to class4
    capture line:7, column:20, length:5 assign to travelDate4
    capture line:7, column:30, length:2 assign to OK4
    capture line:7, column:33, length:12 assign to fareBasis4
    capture line:7, column:47, length:1 assign to status4

    capture line:8, column:4, length:1 assign to original5
    capture line:8, column:5, length:3 assign to city5
    capture line:8, column:9, length:2 assign to airline5
    capture line:8, column:11, length:4 assign to flightNo5
    capture line:8, column:18, length:1 assign to class5
    capture line:8, column:20, length:5 assign to travelDate5
    capture line:8, column:30, length:2 assign to OK5
    capture line:8, column:33, length:12 assign to fareBasis5
    capture line:8, column:47, length:1 assign to status5

    capture line:9, column:4, length:1 assign to original6
    capture line:9, column:5, length:3 assign to city6
    capture line:9, column:9, length:2 assign to airline6
    capture line:9, column:11, length:4 assign to flightNo6
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
    if (OK1=="OK"){
        if (status1!=""){
        append "" +city1 +"/A" +airline1 +"/C" +class1 +"/D" +travelDate1 +city2  to FQPCommand
        }
        }
        if (OK2=="OK"){
        if (status2!=""){
            append "/A" +airline2 +"/C" +class2 +"/D" +travelDate2 +city3 to FQPCommand
        }
        }
        if (OK3=="OK"){
        if (status3!=""){
            append "/A" +airline3 +"/C" +class3 +"/D" +travelDate3 +city4 to FQPCommand
        }
        }
        if (OK4=="OK"){
        if (status4!=""){
            append "/A" +airline4 +"/C" +class4 +"/D" +travelDate4 +city5 to FQPCommand
        }
        }
        if (OK5=="OK"){
        if (status5!=""){
            append "/A" +airline5 +"/C" +class5 +"/D" +travelDate5 +city6 to FQPCommand
        }
        }
        if (OK6=="OK"){
        if (status6!=""){
            append "/A" +airline6 +"/C" +class6 +"/D" +travelDate6 +city7 to FQPCommand
        }
        }
    send "TWD/TKT" +tktNo


    //firstfare
    //capturefareletters
        capture line:4, column:33, length:1 assign to fb1
        capture line:4, column:34, length:1 assign to fb2
        capture line:4, column:35, length:1 assign to fb3
        capture line:4, column:36, length:1 assign to fb4
        capture line:4, column:37, length:1 assign to fb5
        capture line:4, column:38, length:1 assign to fb6
        capture line:4, column:39, length:1 assign to fb7
        capture line:4, column:40, length:1 assign to fb8
        capture line:4, column:41, length:1 assign to fb9
        capture line:4, column:42, length:1 assign to fb10
        capture line:4, column:43, length:1 assign to fb11
        capture line:4, column:44, length:1 assign to fb12
        capture line:4, column:45, length:1 assign to fb13
        capture line:4, column:46, length:1 assign to fb14

        assign "" to fb1check
                 
                
                if (fb1 != " "){ 
                if (fb2 == " "){   
                    append fb1 to fb1check
                }
                }
                
                if (fb2 != " "){   
                if (fb3 == " "){ 
                    append fb1 + fb2 to fb1check
                }
                }
                
                if (fb3 != " "){  
                if (fb4 == " "){     
                    append fb1 + fb2 + fb3 to fb1check 
                } 
                }
                
                if (fb4 != " "){  
                if (fb5 == " "){ 
                    append fb1 + fb2 + fb3 + fb4 to fb1check
                }
                }
                
                if (fb5 != " "){   
                if (fb6 == " "){ 
                    append fb1 + fb2 + fb3 + fb4 + fb5 to fb1check
                }
                }
                
                if (fb6 != " "){   
                if (fb7 == " "){
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 to fb1check
                }
                }
                
                if (fb7 != " "){
                if (fb8 == " "){   
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 to fb1check
                }
                }
                
                if (fb8 != " "){  
                if (fb9 == " "){ 
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 to fb1check
                }
                }
                
                if (fb9 != " "){  
                if (fb10 == " "){ 
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 + fb9  to fb1check
                }
                }
                
                if (fb10 != " "){   
                if (fb11 == " "){
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 + fb9 + fb10 to fb1check
                }
                }
                
                if (fb11 != " "){ 
                if (fb12 == " "){  
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 + fb9 + fb10 + fb11 to fb1check
                }
                }
                
                if (fb12 != " "){   
                if (fb13 == " "){
                append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 + fb9 + fb10 + fb11 + fb12 + fb13 to fb1check
                }
                }
                
                if (fb13 != " "){
                if (fb14 == " "){  
                    append fb1 + fb2 + fb3 + fb4 + fb5 + fb6 + fb7 + fb8 + fb9 + fb10 + fb11 + fb12 + fb13 + fb14 to fb1check
                }
                }else{
                    send "TWD/TKT" +tktNo
                
                // secondfare
                capture line:5, column:33, length:1 assign to fbb1
                capture line:5, column:34, length:1 assign to fbb2
                capture line:5, column:35, length:1 assign to fbb3
                capture line:5, column:36, length:1 assign to fbb4
                capture line:5, column:37, length:1 assign to fbb5
                capture line:5, column:38, length:1 assign to fbb6
                capture line:5, column:39, length:1 assign to fbb7
                capture line:5, column:40, length:1 assign to fbb8
                capture line:5, column:41, length:1 assign to fbb9
                capture line:5, column:42, length:1 assign to fbb10
                capture line:5, column:43, length:1 assign to fbb11
                capture line:5, column:44, length:1 assign to fbb12
                capture line:5, column:45, length:1 assign to fbb13
                capture line:5, column:46, length:1 assign to fbb14
                }
                
                if (OK2=="OK"){
                if (fbb1 != " "){
                if (fbb2 == " "){
                    assign "" to fb2check
                   append fbb1 to fb2check
                }
                }
                if (fbb2 != " "){
                if (fbb3 == " "){    
                    append fbb1 + fbb2 to fb2check
                }
                }
                if (fbb3 != " "){
                if (fbb4 == " "){
                    append fbb1 + fbb2 + fbb3 to fb2check
                }
                }
                if (fbb4 != " "){
                if (fbb5 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 to fb2check
                }
                }
                if (fbb5 != " "){
                if (fbb6 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 to fb2check
                }
                }
                if (fbb6 != " "){
                if (fbb7 == " "){
                append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 to fb2check  
                }
                } 
                if (fbb7 != " "){
                if (fbb8 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 to fb2check
                }
                }
                if (fbb8 != " "){
                if (fbb9 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 to fb2check
                }
                }
                if (fbb9 != " "){
                if (fbb10 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 + fbb9 to fb2check
                }
                }
                if (fbb10 != " "){
                if (fbb11 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 + fbb9 + fbb10 to fb2check
                }
                }
                if (fbb11 != " "){
                if (fbb12 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 + fbb9 + fbb10 + fbb11 to fb2check
                }
                }
                if (fbb12 != " "){
                if (fbb2 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 + fbb9 + fbb10 + fbb11 + fbb12 to fb2check
                }
                }
                if (fbb13!= " "){
                if (fbb14 == " "){
                    append fbb1 + fbb2 + fbb3 + fbb4 + fbb5 + fbb6 + fbb7 + fbb8 + fbb9 + fbb10 + fbb11 + fbb12 + fbb13 to fb2check
                }
                }
                }else{
                    send "TWD/TKT" +tktNo
                

                // thirdfare
                capture line:6, column:33, length:1 assign to fbbb1
                capture line:6, column:34, length:1 assign to fbbb2
                capture line:6, column:35, length:1 assign to fbbb3
                capture line:6, column:36, length:1 assign to fbbb4
                capture line:6, column:37, length:1 assign to fbbb5
                capture line:6, column:38, length:1 assign to fbbb6
                capture line:6, column:39, length:1 assign to fbbb7
                capture line:6, column:40, length:1 assign to fbbb8
                capture line:6, column:41, length:1 assign to fbbb9
                capture line:6, column:42, length:1 assign to fbbb10
                capture line:6, column:43, length:1 assign to fbbb11
                capture line:6, column:44, length:1 assign to fbbb12
                capture line:6, column:45, length:1 assign to fbbb13
                capture line:6, column:46, length:1 assign to fbbb14
                }
                if (OK3=="OK"){
                if (fbbb1 != " "){
                if (fbb2 == " "){  
                 assign "" to fb3check
                    append fbbb1 to fb3check
                }
                }
                if (fbbb2 != " "){
                if (fbb3 == " "){
                    append fbbb1 + fbbb2 to fb3check
                }
                }
                if (fbbb3 != " "){
                if (fbb4 == " "){
                    append fbbb1 + fbbb2 + fbbb3 to fb3check
                }
                }
                if (fbbb4 != " "){
                if (fbb5 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 to fb3check
                }
                }
                if (fbbb5 != " "){
                if (fbb6 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 to fb3check
                }
                }
                if (fbbb6 != " "){
                if (fbb7 == " "){
                    append fbbb1 + fbbb2 +fbbb3 + fbbb4 + fbbb5 + fbbb6 to fb3check
                }
                }
                if (fbbb7 != " "){
                if (fbb2 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 to fb3check
                }
                }
                if (fbbb8 != " "){
                if (fbb9 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 to fb3check
                }
                }
                if (fbbb9 != " "){
                if (fbb2 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 + fbbb9 to fb3check
                }
                }
                if (fbbb10 != " "){
                if (fbb11 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 + fbbb9 + fbbb10 to fb3check
                }
                }
                if (fbbb11 != " "){
                if (fbb12 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 + fbbb9 + fbbb10 + fbbb11 to fb3check
                }
                }
                if (fbbb12 != " "){
                if (fbb13 == " "){
                append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 + fbbb9 + fbbb10 + fbbb11 + fbbb12 to fb3check   
                }
                }
                if (fbbb13!= " "){
                if (fbb14 == " "){
                    append fbbb1 + fbbb2 + fbbb3 + fbbb4 + fbbb5 + fbbb6 + fbbb7 + fbbb8 + fbbb9 + fbbb10 + fbbb11 + fbbb12 + fbbb13 to fb3check
                }
                }
                }else{
                    send "TWD/TKT" +tktNo
                

                // fourthfare
                capture line:7, column:33, length:1 assign to fbbbb1
                capture line:7, column:34, length:1 assign to fbbbb2
                capture line:7, column:35, length:1 assign to fbbbb3
                capture line:7, column:36, length:1 assign to fbbbb4
                capture line:7, column:37, length:1 assign to fbbbb5
                capture line:7, column:38, length:1 assign to fbbbb6
                capture line:7, column:39, length:1 assign to fbbbb7
                capture line:7, column:40, length:1 assign to fbbbb8
                capture line:7, column:41, length:1 assign to fbbbb9
                capture line:7, column:42, length:1 assign to fbbbb10
                capture line:7, column:43, length:1 assign to fbbbb11
                capture line:7, column:44, length:1 assign to fbbbb12
                capture line:7, column:45, length:1 assign to fbbbb13
                capture line:7, column:46, length:1 assign to fbbbb14
                }
                if (OK4=="OK"){
                if (fbbbb1 != " "){
                if (fbbbb2 == " "){
                  assign "" to fb4check
                append fbbbb1 to fb4check
                }
                }
                if (fbbbb2 != " "){
                if (fbbbb3 == " "){
                append fbbbb1 + fbbbb2 to fb4check
                }
                }
                if (fbbbb3 != " "){
                if (fbbbb4 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 to fb4check
                }
                }
                if (fbbbb4 != " "){
                if (fbbbb5 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 to fb4check
                }
                }
                if (fbbbb5 != " "){
                if (fbbbb6 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 to fb4check
                }
                }
                if (fbbbb6 != " "){
                if (fbbbb7 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 to fb4check
                }
                }
                if (fbbbb7 != " "){
                if (fbbbb8 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 to fb4check
                }
                }
                if (fbbbb8 != " "){
                if (fbbbb9 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 to fb4check
                }
                }
                if (fbbbb9 != " "){
                if (fbbbb10 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 + fbbbb9 to fb4check
                }
                }
                if (fbbbb10 != " "){
                if (fbbbb11 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 + fbbbb9 + fbbbb10 to fb4check
                }
                }
                if (fbbbb11 != " "){
                if (fbbbb12 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 + fbbbb9 + fbbbb10 + fbbbb11 to fb4check
                }
                }
                if (fbbbb12 != " "){
                if (fbbbb13 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 + fbbbb9 + fbbbb10 + fbbbb11 + fbbbb12 to fb4check
                }
                }
                if (fbbbb13!= " "){
                if (fbbbb14 == " "){
                    append fbbbb1 + fbbbb2 + fbbbb3 + fbbbb4 + fbbbb5 + fbbbb6 + fbbbb7 + fbbbb8 + fbbbb9 + fbbbb10 + fbbbb11 + fbbbb12 + fbbbb13 to fb4check
                }
                }
                }else{
                    send "TWD/TKT" +tktNo
                



                // fifthfare
                capture line:8, column:33, length:1 assign to fbbbbbb1
                capture line:8, column:34, length:1 assign to fbbbbbb2
                capture line:8, column:35, length:1 assign to fbbbbbb3
                capture line:8, column:36, length:1 assign to fbbbbbb4
                capture line:8, column:37, length:1 assign to fbbbbbb5
                capture line:8, column:38, length:1 assign to fbbbbbb6
                capture line:8, column:39, length:1 assign to fbbbbbb7
                capture line:8, column:40, length:1 assign to fbbbbbb8
                capture line:8, column:41, length:1 assign to fbbbbbb9
                capture line:8, column:42, length:1 assign to fbbbbbb10
                capture line:8, column:43, length:1 assign to fbbbbbb11
                capture line:8, column:44, length:1 assign to fbbbbbb12
                capture line:8, column:45, length:1 assign to fbbbbbb13
                capture line:8, column:46, length:1 assign to fbbbbbb14
                }
                if (OK5=="OK"){
                if (fbbbbb1 != " "){
                if (fbbbbb2 == " "){
                    assign "" to fb5check
                append fbbbbb1 to fb5check
                }
                }
                if (fbbbbb2 != " "){
                if (fbbbbb3 == " "){
                    append fbbbbb1 + fbbbbb2 to fb5check
                }
                }
                if (fbbbbb3 != " "){
                if (fbbbbb4 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 to fb5check
                }
                }
                if (fbbbbb4 != " "){
                if (fbbbbb5 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 to fb5check
                }
                }
                if (fbbbbb5 != " "){
                if (fbbbbb6 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 to fb5check
                }
                }
                if (fbbbbb6 != " "){
                if (fbbbbb7 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 to fb5check
                }
                }
                if (fbbbbb7 != " "){
                if (fbbbbb2 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 to fb5check
                }
                }
                if (fbbbbb8 != " "){
                if (fbbbbb9 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbb8 to fb5check
                }
                }
                if (fbbbbb9 != " "){
                if (fbbbbb10 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbb8 + fbbbbb9 to fb5check
                }
                }
                if (fbbbbb10 != " "){
                if (fbbbbb11 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbb8 + fbbbbb9 + fbbbbb10 to fb5check
                }
                }
                if (fbbbbb11 != " "){
                if (fbbbbb12 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbb8 + fbbbbb9 + fbbbbb10 + fbbbbb11 to fb5check
                }
                }
                if (fbbbbb12 != " "){
                if (fbbbbb13 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbbb8 + fbbbbb9 + fbbbbb10 + fbbbbb11 + fbbbbb12 to fb5check
                }
                }
                if (fbbbbb13!= " "){
                if (fbbbbb14 == " "){
                    append fbbbbb1 + fbbbbb2 + fbbbbb3 + fbbbbb4 + fbbbbb5 + fbbbbb6 + fbbbbb7 + fbbbbb8 + fbbbbb9 + fbbbbb10 + fbbbbb11 + fbbbbb12 + fbbbbb13 to fb5check
                }
                }
                }else{
                    send "TWD/TKT" +tktNo
                



                // sixthfare
                capture line:9, column:33, length:1 assign to fbbbbbbb1
                capture line:9, column:34, length:1 assign to fbbbbbbb2
                capture line:9, column:35, length:1 assign to fbbbbbbb3
                capture line:9, column:36, length:1 assign to fbbbbbbb4
                capture line:9, column:37, length:1 assign to fbbbbbbb5
                capture line:9, column:38, length:1 assign to fbbbbbbb6
                capture line:9, column:39, length:1 assign to fbbbbbbb7
                capture line:9, column:40, length:1 assign to fbbbbbbb8
                capture line:9, column:41, length:1 assign to fbbbbbbb9
                capture line:9, column:42, length:1 assign to fbbbbbbb10
                capture line:9, column:43, length:1 assign to fbbbbbbb11
                capture line:9, column:44, length:1 assign to fbbbbbbb12
                capture line:9, column:45, length:1 assign to fbbbbbbb13
                capture line:9, column:46, length:1 assign to fbbbbbbb14
                }
                if (OK6=="OK"){
                if (fbbbbbb1 != " "){
                if (fbbbbbb2 == " "){
                    assign "" to fb6check
                    append fbbbbbb1 to fb6check
                }
                }
                if (fbbbbbb2 != " "){
                if (fbbbbbb3 == " "){
                    append fbbbbbb1 + fbbbbbb2 to fb6check
                }
                }
                if (fbbbbbb3 != " "){
                if (fbbbbbb4 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 to fb6check
                }
                }
                if (fbbbbbb4 != " "){
                if (fbbbbbb5 == " "){
                append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 to fb6check
                }
                }
                if (fbbbbbb5 != " "){
                if (fbbbbbb6 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 to fb6check
                }
                }
                if (fbbbbbb6 != " "){
                if (fbbbbbb7 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 to fb6check
                }
                }
                if (fbbbbbb7 != " "){
                if (fbbbbbb8 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 to fb6check
                }
                }
                if (fbbbbbb8 != " "){
                if (fbbbbbb9 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 to fb6check
                }
                }
                if (fbbbbbb9 != " "){
                if (fbbbbbb10 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 + fbbbbbb9 to fb6check
                }
                }
                if (fbbbbbb10 != " "){
                if (fbbbbbb2 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 + fbbbbbb9 + fbbbbbb10 to fb6check
                }
                }
                if (fbbbbbb11 != " "){
                if (fbbbbbb12 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 + fbbbbbb9 + fbbbbbb10 + fbbbbbb11 to fb6check
                }
                }
                if (fbbbbbb12 != " "){
                if (fbbbbbb13 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 + fbbbbbb9 + fbbbbbb10 + fbbbbbb11 + fbbbbbb12 to fb6check
                }
                }
                if (fbbbbbb13!= " "){
                if (fbbbbbb14 == " "){
                    append fbbbbbb1 + fbbbbbb2 + fbbbbbb3 + fbbbbbb4 + fbbbbbb5 + fbbbbbb6 + fbbbbbb7 + fbbbbbb8 + fbbbbbb9 + fbbbbbb10 + fbbbbbb11 + fbbbbbb12 + fbbbbbb13 to fb6check
                }
                }
                }else{
                    send "TWD/TKT" +tktNo
                }
                // fb1check + fb2check + fb3check + fb4check + fb5check + fb6check
                //fare name catch done fare1 to fare6


                send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq01"
                    // checkfarmatch
                capture line:9, column:32, length:1 assign to fq1
                capture line:9, column:33, length:1 assign to fq2
                capture line:9, column:34, length:1 assign to fq3
                capture line:9, column:35, length:1 assign to fq4
                capture line:9, column:36, length:1 assign to fq5
                capture line:9, column:37, length:1 assign to fq6
                capture line:9, column:38, length:1 assign to fq7
                capture line:9, column:39, length:1 assign to fq8
                capture line:9, column:40, length:1 assign to fq9
                capture line:9, column:41, length:1 assign to fq10
                capture line:9, column:42, length:1 assign to fq11
                capture line:9, column:43, length:1 assign to fq12
                capture line:9, column:44, length:1 assign to fq13
                capture line:9, column:45, length:1 assign to fq14
                capture line:9, column:46, length:1 assign to fq15
                // first fqq01-1 catched
                assign "" to first
                if (fq1 != " ") {
                if (fq2 == " ") {
                 append fq1 to first
                }
                }
                 if (fq2 != " ") {
                 if (fq3 == " ") {
                 append fq1 + fq2 to first
                 }
                 }
                 if (fq2 != " ") {
                 if (fq4 == " ") {
                 append fq1 + fq2 to first
                 }
                 }
                 if (fq3 != " ") {
                 if (fq4 == " ") {
                 append fq1 + fq2 + fq3 to first
                 }
                 }
                 if (fq4 != " ") {
                 if (fq5 == " ") {
                 append fq1 + fq2 + fq3 + fq4 to first
                 }
                 }
                 if (fq5 != " ") {
                 if (fq6 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 to first
                 }
                 }
                 if (fq6 != " ") {
                 if (fq7 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 to first
                 }
                 }
                 if (fq7 != " ") {
                 if (fq8 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 to first
                 }
                 }
                 if (fq8 != " ") {
                 if (fq9 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 to first
                 }
                 }
                 if (fq9 != " ") {
                 if (fq10 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 to first
                 }
                 }
                 if (fq10 != " ") {
                 if (fq11 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 + fq10 to first
                 }
                 }
                 if (fq11 != " ") {
                 if (fq12 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 + fq10 + fq11 to first
                 }
                 }
                 if (fq12 != " ") {
                 if (fq13 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 + fq10 + fq11 + fq12 to first
                 }
                 }
                 if (fq13 != " ") {
                 if (fq14 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 + fq10 + fq11 + fq12 + fq13 to first
                 }
                 }
                 if (fq14 != " ") {
                 if (fq15 == " ") {
                 append fq1 + fq2 + fq3 + fq4 + fq5 + fq6 + fq7 + fq8 + fq9 + fq10 + fq11 + fq12 + fq13 + fq14 to first
                 }
                 }else {
                send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq01"
                             
                


                    // first fare base , fqq1-1 check complete 
                 // 2nd fqq1-2 check

                // check fqq01-2 to catch 
                capture line:10, column:32, length:1 assign to fqq1
                capture line:10, column:33, length:1 assign to fqq2
                capture line:10, column:34, length:1 assign to fqq3
                capture line:10, column:35, length:1 assign to fqq4
                capture line:10, column:36, length:1 assign to fqq5
                capture line:10, column:37, length:1 assign to fqq6
                capture line:10, column:38, length:1 assign to fqq7
                capture line:10, column:39, length:1 assign to fqq8
                capture line:10, column:40, length:1 assign to fqq9
                capture line:10, column:41, length:1 assign to fqq10
                capture line:10, column:42, length:1 assign to fqq11
                capture line:10, column:43, length:1 assign to fqq12
                capture line:10, column:44, length:1 assign to fqq13
                capture line:10, column:45, length:1 assign to fqq14
                capture line:10, column:46, length:1 assign to fqq15
                assign "" to first1
                // first fqq01-2 catched
                 }
                
                 if (OK2 == "OK"){
                 if (fqq1 != " ") {
                 if (fqq2 == " ") {
                 
                 append fqq1 to firs1
                 }
                 }
                 if (fqq2 != " ") {
                 if (fqq3 == " ") {
                 append fqq1 + fqq2 to first1
                 }
                 }
                 if (fqq3 != " ") {
                 if (fqq4 == " ") {
                 append fqq1 + fqq2 + fqq3 to first1
                 }
                 }
                if (fqq4 != " ") {
                if (fqq5 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 to first1
                }
                }
                if (fqq5 != " ") {
                if (fqq6 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 to first1
                }
                }
                if (fqq6 != " ") {
                if (fqq7 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 to first1
                }
                }
                if (fqq7 != " ") {
                if (fqq8 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 to first1
                }
                }
                if (fqq8 != " ") {
                if (fqq9 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8  to first1
                }
                }
                if (fqq9 != " ") {
                if (fqq10 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9  to first1
                }
                }
                if (fqq10 != " ") {
                if (fqq11 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9 + fqq10 to first1
                }
                }
                if (fqq11 != " ") {
                if (fqq12 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9 + fqq10 + fqq11 to first1
                }
                }
                if (fqq12 != " ") {
                if (fqq13 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9 + fqq10 + fqq11 + fqq12 to first1
                }
                }
                if (fqq13 != " ") {
                 if (fqq14 == " ") {
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9 + fqq10 + fqq11 + fqq12 + fqq13 to first1
                 }
                }
                if (fqq14 != " ") {
                if (fqq15 == " ") {    
                    append fqq1 + fqq2 + fqq3 + fqq4 + fqq5 + fqq6 + fqq7 + fqq8 + fqq9 + fqq10 + fqq11 + fqq12 + fqq13 + fqq14 to first1
                }
                }else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq01"
                    
                


                
                // check fqq01-3 to catch
                capture line:11, column:32, length:1 assign to fqqq1
                capture line:11, column:33, length:1 assign to fqqq2
                capture line:11, column:34, length:1 assign to fqqq3
                capture line:11, column:35, length:1 assign to fqqq4
                capture line:11, column:36, length:1 assign to fqqq5
                capture line:11, column:37, length:1 assign to fqqq6
                capture line:11, column:38, length:1 assign to fqqq7
                capture line:11, column:39, length:1 assign to fqqq8
                capture line:11, column:40, length:1 assign to fqqq9
                capture line:11, column:41, length:1 assign to fqqq10
                capture line:11, column:42, length:1 assign to fqqq11
                capture line:11, column:43, length:1 assign to fqqq12
                capture line:11, column:44, length:1 assign to fqqq13
                capture line:11, column:45, length:1 assign to fqqq14
                capture line:11, column:46, length:1 assign to fqqq15
                assign "" to first2
                }
                // first fqq01-3 catched
                
                if (OK3 == "OK"){
                if (fqqq1 != " ") {
                if (fqqq2 == " ") {
                    
                    append fqqq1 to first2
                }
                }
                if (fqqq2 != " ") {
                if (fqqq3 == " ") {
                    append fqqq1 + fqqq2 to first2
                }
                }
                if (fqqq3 != " ") {
                if (fqqq4 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 to first2
                }
                }
                if (fqqq4 != " ") {
                if (fqqq5 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 to first2
                }
                }
                if (fqqq5 != " ") {
                if (fqqq6 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 to first2
                }
                }
                if (fqqq6 != " ") {
                if (fqqq7 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 to first2
                }
                }
                if (fqqq7 != " ") {
                if (fqqq8 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 to first2
                }
                }
                if (fqqq8 != " ") {
                if (fqqq9 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8 to first2
                }
                }
                if (fqqq9 != " ") {
                if (fqqq10 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8 + fqqq9 to first2
                }
                }
                if (fqqq10 != " ") {
                    if (fqqq11 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8  + fqqq9 + fqqq10 to first2
                    }
                }
                if (fqqq11 != " ") {
                if (fqqq12 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8  + fqqq9 + fqqq10 + fqqq11 to first2
                }
                }
                if (fqqq12 != " ") {
                if (fqqq13 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8  + fqqq9 + fqqq10 + fqqq11 + fqqq12 to first2
                }
                }
                if (fqqq13 != " ") {
                if (fqqq14 == " ") {
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8  + fqqq9 + fqqq10 + fqqq11 + fqqq12 + fqqq13 to first2
                }
                }
                if (fqqq14 != " ") {
                if (fqqq15 == " ") {   
                    append fqqq1 + fqqq2 + fqqq3 + fqqq4 + fqqq5 + fqqq6 + fqqq7 + fqqq8  + fqqq9 + fqqq10 + fqqq11 + fqqq12 + fqqq13 + fqqq14 to first2
                }
                }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq01"
                    
                
                // check fqq01-4 to catch
                capture line:12, column:32, length:1 assign to fqqqq1
                capture line:12, column:33, length:1 assign to fqqqq2
                capture line:12, column:34, length:1 assign to fqqqq3
                capture line:12, column:35, length:1 assign to fqqqq4
                capture line:12, column:36, length:1 assign to fqqqq5
                capture line:12, column:37, length:1 assign to fqqqq6
                capture line:12, column:38, length:1 assign to fqqqq7
                capture line:12, column:39, length:1 assign to fqqqq8
                capture line:12, column:40, length:1 assign to fqqqq9
                capture line:12, column:41, length:1 assign to fqqqq10
                capture line:12, column:42, length:1 assign to fqqqq11
                capture line:12, column:43, length:1 assign to fqqqq12
                capture line:12, column:44, length:1 assign to fqqqq13
                capture line:12, column:45, length:1 assign to fqqqq14
                capture line:12, column:46, length:1 assign to fqqqq15
                assign "" to first4
                }
                // first fqq01-4 catched
                
                if (OK4=="OK"){
                if (fqqqq1 != " ") {
                if (fqqqq2 == " ") {
                    
                    append fqqqq1 to first4
                }
                }
                if (fqqqq2 != " ") {
                if (fqqqq3 == " ") {
                    append fqqqq1 + fqqqq2 to first4
                }
                }
                if (fqqqq3 != " ") {
                if (fqqqq4 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 to first4
                    }
                }
                if (fqqqq4 != " ") {
                if (fqqqq5 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 to first4
                    }
                }
                if (fqqqq5 != " ") {
                if (fqqqq6 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 to first4
                    }
                }
                if (fqqqq6 != " ") {
                if (fqqqq7 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 to first4
                    }
                }
                if (fqqqq7 != " ") {
                if (fqqqq8 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 to first4
                    }
                }
                if (fqqqq8 != " ") {
                if (fqqqq9 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 to first4
                    }
                }
                if (fqqqq9 != " ") {
                if (fqqqq10 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 to first4
                    }
                }
                if (fqqqq10 != " ") {
                if (fqqqq11 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 + fqqqq10 to first4
                    }
                }
                if (fqqqq11 != " ") {
                if (fqqqq12 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 + fqqqq10 + fqqqq11 to first4
                    }
                }
                if (fqqqq12 != " ") {
                if (fqqqq13 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 + fqqqq10 + fqqqq11 + fqqqq12  to first4
                    }
                }
                if (fqqqq13 != " ") {
                if (fqqqq14 == " ") {
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 + fqqqq10 + fqqqq11 + fqqqq12 + fqqqq13  to first4
                }
                }
                if (fqqqq14 != " ") {
                if (fqqqq15 == " ") {   
                    append fqqqq1 + fqqqq2 + fqqqq3 + fqqqq4 + fqqqq5 + fqqqq6 + fqqqq7 + fqqqq8 + fqqqq9 + fqqqq10 + fqqqq11 + fqqqq12 + fqqqq13 + fqqqq14 to first4
                
                }
                } else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq01"
                


                // check fqq01-5 to catch
                capture line:13, column:32, length:1 assign to fqqqqq1
                capture line:13, column:33, length:1 assign to fqqqqq2
                capture line:13, column:34, length:1 assign to fqqqqq3
                capture line:13, column:35, length:1 assign to fqqqqq4
                capture line:13, column:36, length:1 assign to fqqqqq5
                capture line:13, column:37, length:1 assign to fqqqqq6
                capture line:13, column:38, length:1 assign to fqqqqq7
                capture line:13, column:39, length:1 assign to fqqqqq8
                capture line:13, column:40, length:1 assign to fqqqqq9
                capture line:13, column:41, length:1 assign to fqqqqq10
                capture line:13, column:42, length:1 assign to fqqqqq11
                capture line:13, column:43, length:1 assign to fqqqqq12
                capture line:13, column:44, length:1 assign to fqqqqq13
                capture line:13, column:45, length:1 assign to fqqqqq14
                capture line:13, column:46, length:1 assign to fqqqqq15
                assign "" to first5
                }
                // first fqq01-5 catched

                
                if (OK5=="OK"){
                if (fqqqqq1 != " ") {
                if (fqqqq2 == " ") {
                 append fqqqqq1 to first5
                }
                }
                if (fqqqqq2 != " ") {
                if (fqqqq3 == " ") {
                    append fqqqqq1 + fqqqqq2 to first5
                }
                }
                if (fqqqqq3 != " ") {
                if (fqqqq4 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 to first5
                }
                }
                if (fqqqqq4 != " ") {
                if (fqqqq5 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 to first5
                }
                }
                if (fqqqqq5 != " ") {
                if (fqqqq6 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 to first5
                }
                }
                if (fqqqqq6 != " ") {
                if (fqqqq7 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 to first5
                }
                }
                if (fqqqqq7 != " ") {
                if (fqqqq8 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7  to first5
                }
                }
                if (fqqqqq8 != " ") {
                if (fqqqq9 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8  to first5
                }
                }
                if (fqqqqq9 != " ") {
                if (fqqqq10 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 to first5
                }
                }
                if (fqqqqq10 != " ") {
                if (fqqqq11 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 + fqqqqq10 to first5
                }
                }
                if (fqqqqq11 != " ") {
                if (fqqqq12 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 + fqqqqq10 + fqqqqq11 to first5
                }
                }
                if (fqqqqq12 != " ") {
                if (fqqqq13 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 + fqqqqq10 + fqqqqq11 + fqqqqq12 to first5
                }
                }
                if (fqqqqq13 != " ") {
                if (fqqqq14 == " ") {
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 + fqqqqq10 + fqqqqq11 + fqqqqq12 + fqqqqq13 to first5
                }
                }
                if (fqqqqq14 != " ") {
                if (fqqqq15 == " ") {   
                    append fqqqqq1 + fqqqqq2 + fqqqqq3 + fqqqqq4 + fqqqqq5 + fqqqqq6 + fqqqqq7 + fqqqqq8 + fqqqqq9 + fqqqqq10 + fqqqqq11 + fqqqqq12 + fqqqqq13 + fqqqqq14  to first5
                }
                } else {
                send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq01"
                


                // check fqq01-6 to catch
                capture line:14, column:32, length:1 assign to fqqqqqq1
                capture line:14, column:33, length:1 assign to fqqqqqq2
                capture line:14, column:34, length:1 assign to fqqqqqq3
                capture line:14, column:35, length:1 assign to fqqqqqq4
                capture line:14, column:36, length:1 assign to fqqqqqq5
                capture line:14, column:37, length:1 assign to fqqqqqq6
                capture line:14, column:38, length:1 assign to fqqqqqq7
                capture line:14, column:39, length:1 assign to fqqqqqq8
                capture line:14, column:40, length:1 assign to fqqqqqq9
                capture line:14, column:41, length:1 assign to fqqqqqq10
                capture line:14, column:42, length:1 assign to fqqqqqq11
                capture line:14, column:43, length:1 assign to fqqqqqq12
                capture line:14, column:44, length:1 assign to fqqqqqq13
                capture line:14, column:45, length:1 assign to fqqqqqq14
                capture line:14, column:46, length:1 assign to fqqqqqq15
                assign "" to first6
                }
                 // first fqq01-6 catched
                    if (OK6 == "OK"){
                 if (fqqqqqq1 != " ") {
                 if (fqqqqqq2 == " ") {
                    
                 append fqqqqqq1 to first6
                }
                }
            
                if (fqqqqqq2 != " ") {
                if (fqqqqqq3 == " ") {
                    append fqqqqqq1 + fqqqqqq2 to first6
                }
                }
                if (fqqqqqq3 != " ") {
                if (fqqqqqq4 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 to first6
                }
                }
                if (fqqqqqq4 != " ") {
                if (fqqqqqq5 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 to first6
                }
                }
                if (fqqqqqq5 != " ") {
                if (fqqqqqq6 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 to first6
                }
                }
                if (fqqqqqq6 != " ") {
                if (fqqqqqq7 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6   to first6
                }
                }
                if (fqqqqqq7 != " ") {
                if (fqqqqqq8 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7   to first6
                }
                }
                if (fqqqqqq8 != " ") {
                if (fqqqqqq9 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 to first6
                }
                }
                if (fqqqqqq9 != " ") {
                if (fqqqqqq10 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 to first6
                }
                }
                if (fqqqqqq10 != " ") {
                if (fqqqqqq11 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 + fqqqqqq10 to first6
                }
                }
                if (fqqqqqq11 != " ") {
                if (fqqqqqq12 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 + fqqqqqq10 + fqqqqqq11 to first6
                }
                }
                if (fqqqqqq12 != " ") {
                if (fqqqqqq13 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 + fqqqqqq10 + fqqqqqq11 + fqqqqqq12 to first6
                }
                }
                if (fqqqqqq13 != " ") {
                if (fqqqqqq14 == " ") {
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 + fqqqqqq10 + fqqqqqq11 + fqqqqqq12 +  fqqqqqq13 to first6
                }
                }
                if (fqqqqqq14 != " ") {
                if (fqqqqqq15 == " ") {    
                    append fqqqqqq1 + fqqqqqq2 + fqqqqqq3 + fqqqqqq4 + fqqqqqq5 + fqqqqqq6 + fqqqqqq7 + fqqqqqq8 + fqqqqqq9 + fqqqqqq10 + fqqqqqq11 + fqqqqqq12 +  fqqqqqq13 + fqqqqqq14 to first6
                
                }
                }
                }
                }
                }
                }
                } else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq02"
                capture line:3, column:1, length:5 assign to check2
                }
                //----------------------------------------------------------------------------------------------------------------
                if (check2 != "CHECK"){
            // checkfarmatch
            // 1st farecheck
         // fqq02-1
                capture line:9, column:32, length:1 assign to ffq1
                capture line:9, column:33, length:1 assign to ffq2
                capture line:9, column:34, length:1 assign to ffq3
                capture line:9, column:35, length:1 assign to ffq4
                capture line:9, column:36, length:1 assign to ffq5
                capture line:9, column:37, length:1 assign to ffq6
                capture line:9, column:38, length:1 assign to ffq7
                capture line:9, column:39, length:1 assign to ffq8
                capture line:9, column:40, length:1 assign to ffq9
                capture line:9, column:41, length:1 assign to ffq10
                capture line:9, column:42, length:1 assign to ffq11
                capture line:9, column:43, length:1 assign to ffq12
                capture line:9, column:44, length:1 assign to ffq13
                capture line:9, column:45, length:1 assign to ffq14
                capture line:9, column:46, length:1 assign to ffq15
                // first fare base , ffqq2-1 check complete

            assign "" to firstffq

            if (ffq1 != " ") {
            if (ffq2 == " ") {    
                    append ffq1 to firstffq
                }
                }
                if (ffq2 != " ") {
                if (ffq3 != " ") {    
                    append ffq1 + ffq2 to firstffq
                }
                }    
                if (ffq3 != " ") {
                if (ffq4 != " ") {    
                    append ffq1 + ffq2 + ffq3 to firstffq
                }
                }
                if (ffq4 != " ") {
                if (ffq5 != " ") {  
                    append ffq1 + ffq2 + ffq3 + ffq4 to firstffq
                }
                }
                if (ffq5 != " ") {
                if (ffq6 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 to firstffq
                }
                }
                if (ffq6 != " ") {
                if (ffq7 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 to firstffq
                }
                }
                if (ffq7 != " ") {
                if (ffq8 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 to firstffq
                }
                }
                if (ffq8 != " ") {
                if (ffq9 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 to firstffq
                }
                }
                if (ffq9 != " ") {
                if (ffq10 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 to firstffq
                }
                }
                if (ffq10 != " ") {
                if (ffq11 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 + ffq10 to firstffq
                }
                }
                if (ffq11 != " ") {
                if (ffq12 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 + ffq10 + ffq11 to firstffq
                }
                }
                if (ffq12 != " ") {
                if (ffq13 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 + ffq10 + ffq11 + ffq12 to firstffq
                }
                }
                if (ffq13 != " ") {
                if (ffq14 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 + ffq10 + ffq11 + ffq12 + ffq13 to firstffq
                }
                }
                if (ffq14 != " ") {
                if (ffq15 != " ") {
                    append ffq1 + ffq2 + ffq3 + ffq4 + ffq5 + ffq6 + ffq7 + ffq8 + ffq9 + ffq10 + ffq11 + ffq12 + ffq13 + ffq14 to firstffq
                }
                } else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq02"
                

        // checkfarmatch fqq02
                    // 2nd fqq2-2 check
                capture line:10, column:32, length:1 assign to fffqq1
                capture line:10, column:33, length:1 assign to fffqq2
                capture line:10, column:34, length:1 assign to fffqq3
                capture line:10, column:35, length:1 assign to fffqq4
                capture line:10, column:36, length:1 assign to fffqq5
                capture line:10, column:37, length:1 assign to fffqq6
                capture line:10, column:38, length:1 assign to fffqq7
                capture line:10, column:39, length:1 assign to fffqq8
                capture line:10, column:40, length:1 assign to fffqq9
                capture line:10, column:41, length:1 assign to fffqq10
                capture line:10, column:42, length:1 assign to fffqq11
                capture line:10, column:43, length:1 assign to fffqq12
                capture line:10, column:44, length:1 assign to fffqq13
                capture line:10, column:45, length:1 assign to fffqq14
                capture line:10, column:46, length:1 assign to fffqq15
                // 2nd fqq2-2 check complete
                

                 
        
        assign "" to first1ffq
                }
 if (OK2 == "OK"){
 if (fffqq1 != " ") {
 if (fffqq2 == " ") {
 append fffqq1 to first1ffq
 }
 }
if (fffqq2 != " ") {
    if (fffqq3 == " ") {
        append fffqq1 + fffqq2 to first1ffq
    }
}
if (fffqq3 != " ") {
    if (fffqq4 == " ") {
        append fffqq1 + fffqq2 + fffqq3 to first1ffq
    }
}
if (fffqq4 != " ") {
    if (fffqq5 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 to first1ffq
    }
}
if (fffqq5 != " ") {
    if (fffqq6 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 to first1ffq
    }
}
if (fffqq6 != " ") {
    if (fffqq7 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 to first1ffq
    }
}
if (fffqq7 != " ") {
    if (fffqq8 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 to first1ffq
    }
}
if (fffqq8 != " ") {
    if (fffqq9 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 to first1ffq
    }
}
if (fffqq9 != " ") {
    if (fffqq10 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 to first1ffq
    }
}
if (fffqq10 != " ") {
    if (fffqq11 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 + fffqq10 to first1ffq
    }
}
if (fffqq11 != " ") {
    if (fffqq12 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 + fffqq10 + fffqq11 to first1ffq
    }
}
if (fffqq12 != " ") {
    if (fffqq13 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 + fffqq10 + fffqq11 + fffqq12 to first1ffq
    }
}
if (fffqq13 != " ") {
    if (fffqq14 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 + fffqq10 + fffqq11 + fffqq12 + fffqq13 to first1ffq
    }
}
if (fffqq14 != " ") {
    if (fffqq15 == " ") {
        append fffqq1 + fffqq2 + fffqq3 + fffqq4 + fffqq5 + fffqq6 + fffqq7 + fffqq8 + fffqq9 + fffqq10 + fffqq11 + fffqq12 + fffqq13 + fffqq14 to first1ffq
    }
} else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq02"
                
                // 3rd fqq2-3 check
                capture line:11, column:32, length:1 assign to ffffqqq1
                capture line:11, column:33, length:1 assign to ffffqqq2
                capture line:11, column:34, length:1 assign to ffffqqq3
                capture line:11, column:35, length:1 assign to ffffqqq4
                capture line:11, column:36, length:1 assign to ffffqqq5
                capture line:11, column:37, length:1 assign to ffffqqq6
                capture line:11, column:38, length:1 assign to ffffqqq7
                capture line:11, column:39, length:1 assign to ffffqqq8
                capture line:11, column:40, length:1 assign to ffffqqq9
                capture line:11, column:41, length:1 assign to ffffqqq10
                capture line:11, column:42, length:1 assign to ffffqqq11
                capture line:11, column:43, length:1 assign to ffffqqq12
                capture line:11, column:44, length:1 assign to ffffqqq13
                capture line:11, column:45, length:1 assign to ffffqqq14
                capture line:11, column:46, length:1 assign to ffffqqq15
                // 3th fqq2-3 check complete
                

                 assign "" to first2ffq
}
   if (OK3 == "OK"){
  if (ffffqqq1 != " ") {
    if (ffffqqq2 == " ") {
        append ffffqqq1 to first2ffq
}
}
if (ffffqqq2 != " ") {
    if (ffffqqq3 == " ") {
        append ffffqqq1 + ffffqqq2 to first2ffq
    }
}
if (ffffqqq3 != " ") {
    if (ffffqqq4 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 to first2ffq
    }
}
if (ffffqqq4 != " ") {
    if (ffffqqq5 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 to first2ffq
    }
}
if (ffffqqq5 != " ") {
    if (ffffqqq6 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 to first2ffq
    }
}
if (ffffqqq6 != " ") {
    if (ffffqqq7 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 to first2ffq
    }
}
if (ffffqqq7 != " ") {
    if (ffffqqq8 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 to first2ffq
    }
}
if (ffffqqq8 != " ") {
    if (ffffqqq9 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 to first2ffq
    }
}
if (ffffqqq9 != " ") {
    if (ffffqqq10 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 + ffffqqq9 to first2ffq
    }
}
if (ffffqqq10 != " ") {
    if (ffffqqq11 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 + ffffqqq9 + ffffqqq10 to first2ffq
    }
}
if (ffffqqq11 != " ") {
    if (ffffqqq12 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 + ffffqqq9 + ffffqqq10 + ffffqqq11 to first2ffq
    }
}
if (ffffqqq12 != " ") {
    if (ffffqqq13 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 + ffffqqq9 + ffffqqq10 + ffffqqq11 + ffffqqq12 to first2ffq
    }
}
if (ffffqqq13 != " ") {
    if (ffffqqq14 == " ") {
        append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8 + ffffqqq9 + ffffqqq10 + ffffqqq11 + ffffqqq12 + ffffqqq13 to first2ffq
    }
}
                if (ffffqqq14 != " ") {
                if (ffffqqq15 == " ") {
                    append ffffqqq1 + ffffqqq2 + ffffqqq3 + ffffqqq4 + ffffqqq5 + ffffqqq6 + ffffqqq7 + ffffqqq8  + ffffqqq9 + ffffqqq10 + ffffqqq11 + ffffqqq12 + ffffqqq13 + ffffqqq14 to first2ffq
               }
               }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq02"
                  
                


                //4th fqq2-4 check
                capture line:12, column:32, length:1 assign to fffffqqqq1
                capture line:12, column:33, length:1 assign to fffffqqqq2
                capture line:12, column:34, length:1 assign to fffffqqqq3
                capture line:12, column:35, length:1 assign to fffffqqqq4
                capture line:12, column:36, length:1 assign to fffffqqqq5
                capture line:12, column:37, length:1 assign to fffffqqqq6
                capture line:12, column:38, length:1 assign to fffffqqqq7
                capture line:12, column:39, length:1 assign to fffffqqqq8
                capture line:12, column:40, length:1 assign to fffffqqqq9
                capture line:12, column:41, length:1 assign to fffffqqqq10
                capture line:12, column:42, length:1 assign to fffffqqqq11
                capture line:12, column:43, length:1 assign to fffffqqqq12
                capture line:12, column:44, length:1 assign to fffffqqqq13
                capture line:12, column:45, length:1 assign to fffffqqqq14
                capture line:12, column:46, length:1 assign to fffffqqqq15
                // 4th fqq2-4 check complete

                assign "" to first3ffq
               }
if (ok4 == "OK"){
 if (fffffqqqq1 != " ") {
if (fffffqqqq2 == " ") {
append fffffqqqq1 to first3ffq
}
}
if (fffffqqqq2 != " ") {
    if (fffffqqqq3 == " ") {
        append fffffqqqq1 + fffffqqqq2 to first3ffq
    }
}
if (fffffqqqq3 != " ") {
    if (fffffqqqq4 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 to first3ffq
    }
}
if (fffffqqqq4 != " ") {
    if (fffffqqqq5 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 to first3ffq
    }
}
if (fffffqqqq5 != " ") {
    if (fffffqqqq6 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 to first3ffq
    }
}
if (fffffqqqq6 != " ") {
    if (fffffqqqq7 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 to first3ffq
    }
}
if (fffffqqqq7 != " ") {
    if (fffffqqqq8 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 to first3ffq
    }
}
if (fffffqqqq8 != " ") {
    if (fffffqqqq9 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 to first3ffq
    }
}
if (fffffqqqq9 != " ") {
    if (fffffqqqq10 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 to first3ffq
    }
}
if (fffffqqqq10 != " ") {
    if (fffffqqqq11 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 + fffffqqqq10 to first3ffq
    }
}
if (fffffqqqq11 != " ") {
    if (fffffqqqq12 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 + fffffqqqq10 + fffffqqqq11 to first3ffq
    }
}
if (fffffqqqq12 != " ") {
    if (fffffqqqq13 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 + fffffqqqq10 + fffffqqqq11 + fffffqqqq12 to first3ffq
    }
}
if (fffffqqqq13 != " ") {
    if (fffffqqqq14 == " ") {
        append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 + fffffqqqq10 + fffffqqqq11 + fffffqqqq12 + fffffqqqq13 to first3ffq
    }
}
if (fffffqqqq14 != " ") {
if (fffffqqqq15 == " ") {
    append fffffqqqq1 + fffffqqqq2 + fffffqqqq3 + fffffqqqq4 + fffffqqqq5 + fffffqqqq6 + fffffqqqq7 + fffffqqqq8 + fffffqqqq9 + fffffqqqq10 + fffffqqqq11 + fffffqqqq12 + fffffqqqq13 + fffffqqqq14 to first3ffq
}
}else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq02"
                 
                



                // 5th fqq2-5 check
                capture line:13, column:32, length:1 assign to ffffffqqqqq1
                capture line:13, column:33, length:1 assign to ffffffqqqqq2
                capture line:13, column:34, length:1 assign to ffffffqqqqq3
                capture line:13, column:35, length:1 assign to ffffffqqqqq4
                capture line:13, column:36, length:1 assign to ffffffqqqqq5
                capture line:13, column:37, length:1 assign to ffffffqqqqq6
                capture line:13, column:38, length:1 assign to ffffffqqqqq7
                capture line:13, column:39, length:1 assign to ffffffqqqqq8
                capture line:13, column:40, length:1 assign to ffffffqqqqq9
                capture line:13, column:41, length:1 assign to ffffffqqqqq10
                capture line:13, column:42, length:1 assign to ffffffqqqqq11
                capture line:13, column:43, length:1 assign to ffffffqqqqq12
                capture line:13, column:44, length:1 assign to ffffffqqqqq13
                capture line:13, column:45, length:1 assign to ffffffqqqqq14
                capture line:13, column:46, length:1 assign to ffffffqqqqq15
                // 5th fqq2-5 check complete

                assign "" to first4ffq
}
 if (ok5 == "OK"){
if (ffffffqqqqq1 != " ") {
 if (ffffffqqqqq2 == " ") {
        append ffffffqqqqq1 to first4ffq
    }
}
if (ffffffqqqqq2 != " ") {
    if (ffffffqqqqq3 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 to first4ffq
    }
}
if (ffffffqqqqq3 != " ") {
    if (ffffffqqqqq4 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 to first4ffq
    }
}
if (ffffffqqqqq4 != " ") {
    if (ffffffqqqqq5 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 to first4ffq
    }
}
if (ffffffqqqqq5 != " ") {
    if (ffffffqqqqq6 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 to first4ffq
    }
}
if (ffffffqqqqq6 != " ") {
    if (ffffffqqqqq7 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 to first4ffq
    }
}
if (ffffffqqqqq7 != " ") {
    if (ffffffqqqqq8 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 to first4ffq
    }
}
if (ffffffqqqqq8 != " ") {
    if (ffffffqqqqq9 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 to first4ffq
    }
}
if (ffffffqqqqq9 != " ") {
    if (ffffffqqqqq10 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 to first4ffq
    }
}
if (ffffffqqqqq10 != " ") {
    if (ffffffqqqqq11 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 + ffffffqqqqq10 to first4ffq
    }
}
if (ffffffqqqqq11 != " ") {
    if (ffffffqqqqq12 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 + ffffffqqqqq10 + ffffffqqqqq11 to first4ffq
    }
}
if (ffffffqqqqq12 != " ") {
    if (ffffffqqqqq13 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 + ffffffqqqqq10 + ffffffqqqqq11 + ffffffqqqqq12 to first4ffq
    }
}
if (ffffffqqqqq13 != " ") {
    if (ffffffqqqqq14 == " ") {
        append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 + ffffffqqqqq10 + ffffffqqqqq11 + ffffffqqqqq12 + ffffffqqqqq13 to first4ffq
    }
}
if (ffffffqqqqq14 != " ") {
if (ffffffqqqqq15 == " ") {
    append ffffffqqqqq1 + ffffffqqqqq2 + ffffffqqqqq3 + ffffffqqqqq4 + ffffffqqqqq5 + ffffffqqqqq6 + ffffffqqqqq7 + ffffffqqqqq8 + ffffffqqqqq9 + ffffffqqqqq10 + ffffffqqqqq11 + ffffffqqqqq12 + ffffffqqqqq13 + ffffffqqqqq14 to first4ffq
}
} else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq02"
                




                // 6th fqq2-6 check
                capture line:14, column:32, length:1 assign to fffffffqqqqqq1
                capture line:14, column:33, length:1 assign to fffffffqqqqqq2
                capture line:14, column:34, length:1 assign to fffffffqqqqqq3
                capture line:14, column:35, length:1 assign to fffffffqqqqqq4
                capture line:14, column:36, length:1 assign to fffffffqqqqqq5
                capture line:14, column:37, length:1 assign to fffffffqqqqqq6
                capture line:14, column:38, length:1 assign to fffffffqqqqqq7
                capture line:14, column:39, length:1 assign to fffffffqqqqqq8
                capture line:14, column:40, length:1 assign to fffffffqqqqqq9
                capture line:14, column:41, length:1 assign to fffffffqqqqqq10
                capture line:14, column:42, length:1 assign to fffffffqqqqqq11
                capture line:14, column:43, length:1 assign to fffffffqqqqqq12
                capture line:14, column:44, length:1 assign to fffffffqqqqqq13
                capture line:14, column:45, length:1 assign to fffffffqqqqqq14
                capture line:14, column:46, length:1 assign to fffffffqqqqqq15
                // 6th fqq2-6 check complete
                // second fqq02-6 catched
                assign "" to first4ffq
}

  if (ok6 == "OK"){              
 if (fffffffqqqqqq1 != " ") {
    if (fffffffqqqqqq2 == " ") {
        append fffffffqqqqqq1 to first5ffq
    }
}
if (fffffffqqqqqq2 != " ") {
    if (fffffffqqqqqq3 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 to first5ffq
    }
}
if (fffffffqqqqqq3 != " ") {
    if (fffffffqqqqqq4 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 to first5ffq
    }
}
if (fffffffqqqqqq4 != " ") {
    if (fffffffqqqqqq5 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 to first5ffq
    }
}
if (fffffffqqqqqq5 != " ") {
    if (fffffffqqqqqq6 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 to first5ffq
    }
}
if (fffffffqqqqqq6 != " ") {
    if (fffffffqqqqqq7 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 to first5ffq
    }
}
if (fffffffqqqqqq7 != " ") {
    if (fffffffqqqqqq8 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 to first5ffq
    }
}
if (fffffffqqqqqq8 != " ") {
    if (fffffffqqqqqq9 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 to first5ffq
    }
}
if (fffffffqqqqqq9 != " ") {
    if (fffffffqqqqqq10 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 to first5ffq
    }
}
if (fffffffqqqqqq10 != " ") {
    if (fffffffqqqqqq11 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 + fffffffqqqqqq10 to first5ffq
    }
}
if (fffffffqqqqqq11 != " ") {
    if (fffffffqqqqqq12 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 + fffffffqqqqqq10 + fffffffqqqqqq11 to first5ffq
    }
}
if (fffffffqqqqqq12 != " ") {
    if (fffffffqqqqqq13 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 + fffffffqqqqqq10 + fffffffqqqqqq11 + fffffffqqqqqq12 to first5ffq
    }
}
if (fffffffqqqqqq13 != " ") {
    if (fffffffqqqqqq14 == " ") {
        append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 + fffffffqqqqqq10 + fffffffqqqqqq11 + fffffffqqqqqq12 + fffffffqqqqqq13 to first5ffq
    }
}
if (fffffffqqqqqq14 != " ") {
if (fffffffqqqqqq15 == " ") {
    append fffffffqqqqqq1 + fffffffqqqqqq2 + fffffffqqqqqq3 + fffffffqqqqqq4 + fffffffqqqqqq5 + fffffffqqqqqq6 + fffffffqqqqqq7 + fffffffqqqqqq8 + fffffffqqqqqq9 + fffffffqqqqqq10 + fffffffqqqqqq11 + fffffffqqqqqq12 + fffffffqqqqqq13 + fffffffqqqqqq14 to first5ffq
}
}
}
}
}
}
}
else {
                 // fqq02 completed
                //------------------------------------------------------------------------------------------------------------------
                // check fqq03
                send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                send "fqq03" 
                
                
            capture line:3, column:1, length:5 assign to check3
}
     if (check3 != "check"){
        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
        send "fqq03"
     

     // 1st farecheck fqq03-1 capture
                capture line:9, column:32, length:1 assign to f1q1
                capture line:9, column:33, length:1 assign to f1q2
                capture line:9, column:34, length:1 assign to f1q3
                capture line:9, column:35, length:1 assign to f1q4
                capture line:9, column:36, length:1 assign to f1q5
                capture line:9, column:37, length:1 assign to f1q6
                capture line:9, column:38, length:1 assign to f1q7
                capture line:9, column:39, length:1 assign to f1q8
                capture line:9, column:40, length:1 assign to f1q9
                capture line:9, column:41, length:1 assign to f1q10
                capture line:9, column:42, length:1 assign to f1q11
                capture line:9, column:43, length:1 assign to f1q12
                capture line:9, column:44, length:1 assign to f1q13
                capture line:9, column:45, length:1 assign to f1q14
                capture line:9, column:46, length:1 assign to f1q15
                // first fare base , ffqq3-1 capture complete 
   if (f1q1 != " ") {
    if (f1q2 == " ") {
        append f1q1 to firstf1q
    }
}
if (f1q2 != " ") {
    if (f1q3 == " ") {
        append f1q1 + f1q2 to firstf1q
    }
}
if (f1q3 != " ") {
    if (f1q4 == " ") {
        append f1q1 + f1q2 + f1q3 to firstf1q
    }
}
if (f1q4 != " ") {
    if (f1q5 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 to firstf1q
    }
}
if (f1q5 != " ") {
    if (f1q6 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 to firstf1q
    }
}

if (f1q6 != " ") {
    if (f1q7 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 to firstf1q
    }
}
if (f1q7 != " ") {
    if (f1q8 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 to firstf1q
    }
}
if (f1q8 != " ") {
    if (f1q9 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 to firstf1q
    }
}
if (f1q9 != " ") {
    if (f1q10 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 to firstf1q
    }
}
if (f1q10 != " ") {
    if (f1q11 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 + f1q10 to firstf1q
    }
}
if (f1q11 != " ") {
    if (f1q12 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 + f1q10 + f1q11 to firstf1q
    }
}
if (f1q12 != " ") {
    if (f1q13 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 + f1q10 + f1q11 + f1q12 to firstf1q
    }
}
if (f1q13 != " ") {
    if (f1q14 == " ") {
        append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 + f1q10 + f1q11 + f1q12 + f1q13 to firstf1q
    }
}
if (f1q14 != " ") {
 if (f1q15 == " ") {   
    append f1q1 + f1q2 + f1q3 + f1q4 + f1q5 + f1q6 + f1q7 + f1q8 + f1q9 + f1q10 + f1q11 + f1q12 + f1q13 + f1q14 to firstf1q
}

                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq03"
                



                // 2nd fqq03-2 capture
                capture line:10, column:32, length:1 assign to f2q1
                capture line:10, column:33, length:1 assign to f2q2
                capture line:10, column:34, length:1 assign to f2q3
                capture line:10, column:35, length:1 assign to f2q4
                capture line:10, column:36, length:1 assign to f2q5
                capture line:10, column:37, length:1 assign to f2q6
                capture line:10, column:38, length:1 assign to f2q7
                capture line:10, column:39, length:1 assign to f2q8
                capture line:10, column:40, length:1 assign to f2q9
                capture line:10, column:41, length:1 assign to f2q10
                capture line:10, column:42, length:1 assign to f2q11
                capture line:10, column:43, length:1 assign to f2q12
                capture line:10, column:44, length:1 assign to f2q13
                capture line:10, column:45, length:1 assign to f2q14
                capture line:10, column:46, length:1 assign to f2q15
                // 2nd fqq03-2 capture complete
                assign "" to firstf2q
                }
 if (ok2 == "OK"){
 if (f2q1 != " ") {
    if (f2q2 == " ") {
        append f2q1 to firstf2q
    }
}
if (f2q2 != " ") {
    if (f2q3 == " ") {
        append f2q1 + f2q2 to firstf2q
    }
}
if (f2q3 != " ") {
    if (f2q4 == " ") {
        append f2q1 + f2q2 + f2q3 to firstf2q
    }
}
if (f2q4 != " ") {
    if (f2q5 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 to firstf2q
    }
}
if (f2q5 != " ") {
    if (f2q6 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 to firstf2q
    }
}
if (f2q6 != " ") {
    if (f2q7 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 to firstf2q
    }
}
if (f2q7 != " ") {
    if (f2q8 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 to firstf2q
    }
}
if (f2q8 != " ") {
    if (f2q9 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 to firstf2q
    }
}
if (f2q9 != " ") {
    if (f2q10 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 to firstf2q
    }
}
if (f2q10 != " ") {
    if (f2q11 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 + f2q10 to firstf2q
    }
}
if (f2q11 != " ") {
    if (f2q12 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 + f2q10 + f2q11 to firstf2q
    }
}
if (f2q12 != " ") {
    if (f2q13 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 + f2q10 + f2q11 + f2q12 to firstf2q
    }
}
if (f2q13 != " ") {
    if (f2q14 == " ") {
        append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 + f2q10 + f2q11 + f2q12 + f2q13 to firstf2q
    }
}
if (f2q14 != " ") {
    if (f2q15 == " ") {
    append f2q1 + f2q2 + f2q3 + f2q4 + f2q5 + f2q6 + f2q7 + f2q8 + f2q9 + f2q10 + f2q11 + f2q12 + f2q13 + f2q14 to firstf2q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq03"
                






                 // 3rd fqq03-3 capture
                capture line:11, column:32, length:1 assign to f3q1
                capture line:11, column:33, length:1 assign to f3q2
                capture line:11, column:34, length:1 assign to f3q3
                capture line:11, column:35, length:1 assign to f3q4
                capture line:11, column:36, length:1 assign to f3q5
                capture line:11, column:37, length:1 assign to f3q6
                capture line:11, column:38, length:1 assign to f3q7
                capture line:11, column:39, length:1 assign to f3q8
                capture line:11, column:40, length:1 assign to f3q9
                capture line:11, column:41, length:1 assign to f3q10
                capture line:11, column:42, length:1 assign to f3q11
                capture line:11, column:43, length:1 assign to f3q12
                capture line:11, column:44, length:1 assign to f3q13
                capture line:11, column:45, length:1 assign to f3q14
                capture line:11, column:46, length:1 assign to f3q15
                // 3th fqq03-3 capture complete

                assign "" to firstf3q
                }
                if (ok3 == "OK"){
                    if (f3q1 != " ") {
    if (f3q2 == " ") {
        append f3q1 to firstf3q
    }
}
if (f3q2 != " ") {
    if (f3q3 == " ") {
        append f3q1 + f3q2 to firstf3q
    }
}
if (f3q3 != " ") {
    if (f3q4 == " ") {
        append f3q1 + f3q2 + f3q3 to firstf3q
    }
}
if (f3q4 != " ") {
    if (f3q5 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 to firstf3q
    }
}
if (f3q5 != " ") {
    if (f3q6 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 to firstf3q
    }
}
if (f3q6 != " ") {
    if (f3q7 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 to firstf3q
    }
}
if (f3q7 != " ") {
    if (f3q8 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 to firstf3q
    }
}
if (f3q8 != " ") {
    if (f3q9 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 to firstf3q
    }
}
if (f3q9 != " ") {
    if (f3q10 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 to firstf3q
    }
}
if (f3q10 != " ") {
    if (f3q11 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 + f3q10 to firstf3q
    }
}
if (f3q11 != " ") {
    if (f3q12 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 + f3q10 + f3q11 to firstf3q
    }
}
if (f3q12 != " ") {
    if (f3q13 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 + f3q10 + f3q11 + f3q12 to firstf3q
    }
}
if (f3q13 != " ") {
    if (f3q14 == " ") {
        append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 + f3q10 + f3q11 + f3q12 + f3q13 to firstf3q
    }
}
if (f3q14 != " ") {
    if (f3q15 == " ") {
    append f3q1 + f3q2 + f3q3 + f3q4 + f3q5 + f3q6 + f3q7 + f3q8 + f3q9 + f3q10 + f3q11 + f3q12 + f3q13 + f3q14 to firstf3q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq03"
                


                // 4th fqq03-4 capture
                capture line:12, column:32, length:1 assign to f4q1
                capture line:12, column:33, length:1 assign to f4q2
                capture line:12, column:34, length:1 assign to f4q3
                capture line:12, column:35, length:1 assign to f4q4
                capture line:12, column:36, length:1 assign to f4q5
                capture line:12, column:37, length:1 assign to f4q6
                capture line:12, column:38, length:1 assign to f4q7
                capture line:12, column:39, length:1 assign to f4q8
                capture line:12, column:40, length:1 assign to f4q9
                capture line:12, column:41, length:1 assign to f4q10
                capture line:12, column:42, length:1 assign to f4q11
                capture line:12, column:43, length:1 assign to f4q12
                capture line:12, column:44, length:1 assign to f4q13
                capture line:12, column:45, length:1 assign to f4q14
                capture line:12, column:45, length:1 assign to f4q15
                // 4th fqq03-4 capture complete
                    assign "" to firstf4q
                }
                    if (ok4 == "OK"){
    
                    if (f4q1 != " ") {
    if (f4q2 == " ") {
        append f4q1 to firstf4q
    }
}
if (f4q2 != " ") {
    if (f4q3 == " ") {
        append f4q1 + f4q2 to firstf4q
    }
}
if (f4q3 != " ") {
    if (f4q4 == " ") {
        append f4q1 + f4q2 + f4q3 to firstf4q
    }
}
if (f4q4 != " ") {
    if (f4q5 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 to firstf4q
    }
}
if (f4q5 != " ") {
    if (f4q6 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 to firstf4q
    }
}
if (f4q6 != " ") {
    if (f4q7 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 to firstf4q
    }
}
if (f4q7 != " ") {
    if (f4q8 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 to firstf4q
    }
}
if (f4q8 != " ") {
    if (f4q9 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 to firstf4q
    }
}
if (f4q9 != " ") {
    if (f4q10 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 to firstf4q
    }
}
if (f4q10 != " ") {
    if (f4q11 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 + f4q10 to firstf4q
    }
}
if (f4q11 != " ") {
    if (f4q12 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 + f4q10 + f4q11 to firstf4q
    }
}
if (f4q12 != " ") {
    if (f4q13 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 + f4q10 + f4q11 + f4q12 to firstf4q
    }
}
if (f4q13 != " ") {
    if (f4q14 == " ") {
        append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 + f4q10 + f4q11 + f4q12 + f4q13 to firstf4q
    }
}
if (f4q14 != " ") {
if (f4q15 == " ") {
    append f4q1 + f4q2 + f4q3 + f4q4 + f4q5 + f4q6 + f4q7 + f4q8 + f4q9 + f4q10 + f4q11 + f4q12 + f4q13 + f4q14 to firstf4q
}

                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq03"
                    
                




                // 5th fqq03-5 capture
                capture line:13, column:32, length:1 assign to f5q1
                capture line:13, column:33, length:1 assign to f5q2
                capture line:13, column:34, length:1 assign to f5q3
                capture line:13, column:35, length:1 assign to f5q4
                capture line:13, column:36, length:1 assign to f5q5
                capture line:13, column:37, length:1 assign to f5q6
                capture line:13, column:38, length:1 assign to f5q7
                capture line:13, column:39, length:1 assign to f5q8
                capture line:13, column:40, length:1 assign to f5q9
                capture line:13, column:41, length:1 assign to f5q10
                capture line:13, column:42, length:1 assign to f5q11
                capture line:13, column:43, length:1 assign to f5q12
                capture line:13, column:44, length:1 assign to f5q13
                capture line:13, column:45, length:1 assign to f5q14
                capture line:13, column:46, length:1 assign to f5q15
                // 5th fqq03-5 capture complete
                assign "" to firstf5q
                }
                if (ok5 == "OK"){
                     if (f5q1 != " ") {
    if (f5q2 == " ") {
        append f5q1 to firstf5q
    }
}
if (f5q2 != " ") {
    if (f5q3 == " ") {
        append f5q1 + f5q2 to firstf5q
    }
}
if (f5q3 != " ") {
    if (f5q4 == " ") {
        append f5q1 + f5q2 + f5q3 to firstf5q
    }
}
if (f5q4 != " ") {
    if (f5q5 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 to firstf5q
    }
}
if (f5q5 != " ") {
    if (f5q6 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 to firstf5q
    }
}
if (f5q6 != " ") {
    if (f5q7 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 to firstf5q
    }
}
if (f5q7 != " ") {
    if (f5q8 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 to firstf5q
    }
}
if (f5q8 != " ") {
    if (f5q9 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 to firstf5q
    }
}
if (f5q9 != " ") {
    if (f5q10 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 to firstf5q
    }
}
if (f5q10 != " ") {
    if (f5q11 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 + f5q10 to firstf5q
    }
}
if (f5q11 != " ") {
    if (f5q12 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 + f5q10 + f5q11 to firstf5q
    }
}
if (f5q12 != " ") {
    if (f5q13 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 + f5q10 + f5q11 + f5q12 to firstf5q
    }
}
if (f5q13 != " ") {
    if (f5q14 == " ") {
        append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 + f5q10 + f5q11 + f5q12 + f5q13 to firstf5q
    }
}
if (f5q14 != " ") {
    if (f5q15 == " ") {
    append f5q1 + f5q2 + f5q3 + f5q4 + f5q5 + f5q6 + f5q7 + f5q8 + f5q9 + f5q10 + f5q11 + f5q12 + f5q13 + f5q14 to firstf5q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq03"
                  
                

                // 6th fqq03-6 capture
                capture line:14, column:32, length:1 assign to f6q1
                capture line:14, column:33, length:1 assign to f6q2
                capture line:14, column:34, length:1 assign to f6q3
                capture line:14, column:35, length:1 assign to f6q4
                capture line:14, column:36, length:1 assign to f6q5
                capture line:14, column:37, length:1 assign to f6q6
                capture line:14, column:38, length:1 assign to f6q7
                capture line:14, column:39, length:1 assign to f6q8
                capture line:14, column:40, length:1 assign to f6q9
                capture line:14, column:41, length:1 assign to f6q10
                capture line:14, column:42, length:1 assign to f6q11
                capture line:14, column:43, length:1 assign to f6q12
                capture line:14, column:44, length:1 assign to f6q13
                capture line:14, column:45, length:1 assign to f6q14
                capture line:14, column:46, length:1 assign to f6q15
                // 6th fqq03-6 capture complete

                assign "" to firstf6q
                }
if (ok6 == "OK"){
if (f6q1 != " ") {
 if (f6q2 == " ") {
 append f6q1 to firstf6q
}
}
    if (f6q2 != " ") {
        if (f6q3 == " ") {
            append f6q1 + f6q2 to firstf6q
        }
    }
    if (f6q3 != " ") {
        if (f6q4 == " ") {
            append f6q1 + f6q2 + f6q3 to firstf6q
        }
    }
    if (f6q4 != " ") {
        if (f6q5 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 to firstf6q
        }
    }
    if (f6q5 != " ") {
        if (f6q6 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 to firstf6q
        }
    }
    if (f6q6 != " ") {
        if (f6q7 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 to firstf6q
        }
    }
    if (f6q7 != " ") {
        if (f6q8 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 to firstf6q
        }
    }
    if (f6q8 != " ") {
        if (f6q9 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 to firstf6q
        }
    }
    if (f6q9 != " ") {
        if (f6q10 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 to firstf6q
        }
    }
    if (f6q10 != " ") {
        if (f6q11 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 + f6q10 to firstf6q
        }
    }
    if (f6q11 != " ") {
        if (f6q12 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 + f6q10 + f6q11 to firstf6q
        }
    }
    if (f6q12 != " ") {
        if (f6q13 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 + f6q10 + f6q11 + f6q12 to firstf6q
        }
    }
    if (f6q13 != " ") {
        if (f6q14 == " ") {
            append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 + f6q10 + f6q11 + f6q12 + f6q13 to firstf6q
        }
    }
    if (f6q14 != " ") {
    if (f6q15 == " ") {
        append f6q1 + f6q2 + f6q3 + f6q4 + f6q5 + f6q6 + f6q7 + f6q8 + f6q9 + f6q10 + f6q11 + f6q12 + f6q13 + f6q14 to firstf6q
    }

                }
                }
                }
                }
                }
                }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04"
                
        // 6th fqq3-6 check complete
                //------------------------------------------------------------------------------------------------------------------
                // check fqq04
                 capture line:3, column:1, length:5 assign to check4
                }
     if (check4 != "check"){
        // 1st ffarecheck ffqq04
                capture line:9, column:32, length:1 assign to ff1q1
                capture line:9, column:33, length:1 assign to ff1q2
                capture line:9, column:34, length:1 assign to ff1q3
                capture line:9, column:35, length:1 assign to ff1q4
                capture line:9, column:36, length:1 assign to ff1q5
                capture line:9, column:37, length:1 assign to ff1q6
                capture line:9, column:38, length:1 assign to ff1q7
                capture line:9, column:39, length:1 assign to ff1q8
                capture line:9, column:40, length:1 assign to ff1q9
                capture line:9, column:41, length:1 assign to ff1q10
                capture line:9, column:42, length:1 assign to ff1q11
                capture line:9, column:43, length:1 assign to ff1q12
                capture line:9, column:44, length:1 assign to ff1q13
                capture line:9, column:45, length:1 assign to ff1q14
                capture line:9, column:46, length:1 assign to ff1q15

                // ffirst ffare base , fqq04-1 check complete 

        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
        send "fqq04"
     if (ff1q1 != " ") {
    if (ff1q2 == " ") {
        append ff1q1 to firstff1q
    }
}
if (ff1q2 != " ") {
    if (ff1q3 == " ") {
        append ff1q1 + ff1q2 to firstff1q
    }
}
if (ff1q3 != " ") {
    if (ff1q4 == " ") {
        append ff1q1 + ff1q2 + ff1q3 to firstff1q
    }
}
if (ff1q4 != " ") {
    if (ff1q5 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 to firstff1q
    }
}
if (ff1q5 != " ") {
    if (ff1q6 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 to firstff1q
    }
}
if (ff1q6 != " ") {
    if (ff1q7 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 to firstff1q
    }
}
if (ff1q7 != " ") {
    if (ff1q8 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 to firstff1q
    }
}
if (ff1q8 != " ") {
    if (ff1q9 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 to firstff1q
    }
}
if (ff1q9 != " ") {
    if (ff1q10 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 to firstff1q
    }
}
if (ff1q10 != " ") {
    if (ff1q11 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 + ff1q10 to firstff1q
    }
}
if (ff1q11 != " ") {
    if (ff1q12 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 + ff1q10 + ff1q11 to firstff1q
    }
}
if (ff1q12 != " ") {
    if (ff1q13 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 + ff1q10 + ff1q11 + ff1q12 to firstff1q
    }
}
if (ff1q13 != " ") {
    if (ff1q14 == " ") {
        append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 + ff1q10 + ff1q11 + ff1q12 + ff1q13 to firstff1q
    }
}
if (ff1q14 != " ") {
    if (ff1q14 == " ") {
    append ff1q1 + ff1q2 + ff1q3 + ff1q4 + ff1q5 + ff1q6 + ff1q7 + ff1q8 + ff1q9 + ff1q10 + ff1q11 + ff1q12 + ff1q13 + ff1q14 to firstff1q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04"
                
                    // 2nd fqq04-2 check
                capture line:10, column:32, length:1 assign to ff2q1
                capture line:10, column:33, length:1 assign to ff2q2
                capture line:10, column:34, length:1 assign to ff2q3
                capture line:10, column:35, length:1 assign to ff2q4
                capture line:10, column:36, length:1 assign to ff2q5
                capture line:10, column:37, length:1 assign to ff2q6
                capture line:10, column:38, length:1 assign to ff2q7
                capture line:10, column:39, length:1 assign to ff2q8
                capture line:10, column:40, length:1 assign to ff2q9
                capture line:10, column:41, length:1 assign to ff2q10
                capture line:10, column:42, length:1 assign to ff2q11
                capture line:10, column:43, length:1 assign to ff2q12
                capture line:10, column:44, length:1 assign to ff2q13
                capture line:10, column:45, length:1 assign to ff2q14
                capture line:10, column:46, length:1 assign to ff2q15

                // 2nd fqq04-2 check complete
                assign "" to firstff2q
                }
                if (ok2 == "OK"){
               if (ff2q1 != " ") {
    if (ff2q2 == " ") {
        append ff2q1 to firstff2q
    }
}
if (ff2q2 != " ") {
    if (ff2q3 == " ") {
        append ff2q1 + ff2q2 to firstff2q
    }
}
if (ff2q3 != " ") {
    if (ff2q4 == " ") {
        append ff2q1 + ff2q2 + ff2q3 to firstff2q
    }
}
if (ff2q4 != " ") {
    if (ff2q5 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 to firstff2q
    }
}
if (ff2q5 != " ") {
    if (ff2q6 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 to firstff2q
    }
}
if (ff2q6 != " ") {
    if (ff2q7 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 to firstff2q
    }
}
if (ff2q7 != " ") {
    if (ff2q8 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 to firstff2q
    }
}
if (ff2q8 != " ") {
    if (ff2q9 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 to firstff2q
    }
}
if (ff2q9 != " ") {
    if (ff2q10 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 to firstff2q
    }
}
if (ff2q10 != " ") {
    if (ff2q11 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 + ff2q10 to firstff2q
    }
}
if (ff2q11 != " ") {
    if (ff2q12 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 + ff2q10 + ff2q11 to firstff2q
    }
}
if (ff2q12 != " ") {
    if (ff2q13 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 + ff2q10 + ff2q11 + ff2q12 to firstff2q
    }
}
if (ff2q13 != " ") {
    if (ff2q14 == " ") {
        append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 + ff2q10 + ff2q11 + ff2q12 + ff2q13 to firstff2q
    }
}
if (ff2q14 != " ") {
 if (ff2q15 == " ") {
    append ff2q1 + ff2q2 + ff2q3 + ff2q4 + ff2q5 + ff2q6 + ff2q7 + ff2q8 + ff2q9 + ff2q10 + ff2q11 + ff2q12 + ff2q13 + ff2q14 to firstff2q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04" 
                


                // 3rd fqq04-3 check

                capture line:11, column:32, length:1 assign to ff3q1
                capture line:11, column:33, length:1 assign to ff3q2
                capture line:11, column:34, length:1 assign to ff3q3
                capture line:11, column:35, length:1 assign to ff3q4
                capture line:11, column:36, length:1 assign to ff3q5
                capture line:11, column:37, length:1 assign to ff3q6
                capture line:11, column:38, length:1 assign to ff3q7
                capture line:11, column:39, length:1 assign to ff3q8
                capture line:11, column:40, length:1 assign to ff3q9
                capture line:11, column:41, length:1 assign to ff3q10
                capture line:11, column:42, length:1 assign to ff3q11
                capture line:11, column:43, length:1 assign to ff3q12
                capture line:11, column:44, length:1 assign to ff3q13
                capture line:11, column:45, length:1 assign to ff3q14
                capture line:11, column:46, length:1 assign to ff3q15

                // 3th fqq04-3 check complete
                assign "" to firstff3q
                }
                if (ok3 == "OK"){
                if (ff3q1 != " ") {
    if (ff3q2 == " ") {
        append ff3q1 to firstff3q
    }
}
if (ff3q2 != " ") {
    if (ff3q3 == " ") {
        append ff3q1 + ff3q2 to firstff3q
    }
}
if (ff3q3 != " ") {
    if (ff3q4 == " ") {
        append ff3q1 + ff3q2 + ff3q3 to firstff3q
    }
}
if (ff3q4 != " ") {
    if (ff3q5 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 to firstff3q
    }
}
if (ff3q5 != " ") {
    if (ff3q6 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 to firstff3q
    }
}
if (ff3q6 != " ") {
    if (ff3q7 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 to firstff3q
    }
}
if (ff3q7 != " ") {
    if (ff3q8 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 to firstff3q
    }
}
if (ff3q8 != " ") {
    if (ff3q9 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 to firstff3q
    }
}
if (ff3q9 != " ") {
    if (ff3q10 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 to firstff3q
    }
}
if (ff3q10 != " ") {
    if (ff3q11 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 + ff3q10 to firstff3q
    }
}
if (ff3q11 != " ") {
    if (ff3q12 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 + ff3q10 + ff3q11 to firstff3q
    }
}
if (ff3q12 != " ") {
    if (ff3q13 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 + ff3q10 + ff3q11 + ff3q12 to firstff3q
    }
}
if (ff3q13 != " ") {
    if (ff3q14 == " ") {
        append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 + ff3q10 + ff3q11 + ff3q12 + ff3q13 to firstff3q
    }
}
if (ff3q14 != " ") {
if (ff3q15 == " ") {
    append ff3q1 + ff3q2 + ff3q3 + ff3q4 + ff3q5 + ff3q6 + ff3q7 + ff3q8 + ff3q9 + ff3q10 + ff3q11 + ff3q12 + ff3q13 + ff3q14 to firstff3q
}
                }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04"
                    
                






                // 4th fqq04-4 check
                capture line:12, column:32, length:1 assign to ff4q1
                capture line:12, column:33, length:1 assign to ff4q2
                capture line:12, column:34, length:1 assign to ff4q3
                capture line:12, column:35, length:1 assign to ff4q4
                capture line:12, column:36, length:1 assign to ff4q5
                capture line:12, column:37, length:1 assign to ff4q6
                capture line:12, column:38, length:1 assign to ff4q7
                capture line:12, column:39, length:1 assign to ff4q8
                capture line:12, column:40, length:1 assign to ff4q9
                capture line:12, column:41, length:1 assign to ff4q10
                capture line:12, column:42, length:1 assign to ff4q11
                capture line:12, column:43, length:1 assign to ff4q12
                capture line:12, column:44, length:1 assign to ff4q13
                capture line:12, column:45, length:1 assign to ff4q14
                capture line:12, column:46, length:1 assign to ff4q15
                

                // 4th fqq04-4 check complete


assign "" to firstff4q
                }
                if (ok4 == "OK"){
if (ff4q1 != " ") {
    if (ff4q2 == " ") {
        append ff4q1 to firstff4q
    }
}
if (ff4q2 != " ") {
    if (ff4q3 == " ") {
        append ff4q1 + ff4q2 to firstff4q
    }
}
if (ff4q3 != " ") {
    if (ff4q4 == " ") {
        append ff4q1 + ff4q2 + ff4q3 to firstff4q
    }
}
if (ff4q4 != " ") {
    if (ff4q5 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 to firstff4q
    }
}
if (ff4q5 != " ") {
    if (ff4q6 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 to firstff4q
    }
}
if (ff4q6 != " ") {
    if (ff4q7 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 to firstff4q
    }
}
if (ff4q7 != " ") {
    if (ff4q8 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 to firstff4q
    }
}
if (ff4q8 != " ") {
    if (ff4q9 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 to firstff4q
    }
}
if (ff4q9 != " ") {
    if (ff4q10 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 to firstff4q
    }
}
if (ff4q10 != " ") {
    if (ff4q11 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 + ff4q10 to firstff4q
    }
}
if (ff4q11 != " ") {
    if (ff4q12 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 + ff4q10 + ff4q11 to firstff4q
    }
}
if (ff4q12 != " ") {
    if (ff4q13 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 + ff4q10 + ff4q11 + ff4q12 to firstff4q
    }
}
if (ff4q13 != " ") {
    if (ff4q14 == " ") {
        append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 + ff4q10 + ff4q11 + ff4q12 + ff4q13 to firstff4q
    }
}
if (ff4q14 != " ") {
    if (ff4q15 == " ") {
    append ff4q1 + ff4q2 + ff4q3 + ff4q4 + ff4q5 + ff4q6 + ff4q7 + ff4q8 + ff4q9 + ff4q10 + ff4q11 + ff4q12 + ff4q13 + ff4q14 to firstff4q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04"
                    
                
                // 5th fqq04-5 check
                capture line:13, column:32, length:1 assign to ff5q1
                capture line:13, column:33, length:1 assign to ff5q2
                capture line:13, column:34, length:1 assign to ff5q3
                capture line:13, column:35, length:1 assign to ff5q4
                capture line:13, column:36, length:1 assign to ff5q5
                capture line:13, column:37, length:1 assign to ff5q6
                capture line:13, column:38, length:1 assign to ff5q7
                capture line:13, column:39, length:1 assign to ff5q8
                capture line:13, column:40, length:1 assign to ff5q9
                capture line:13, column:41, length:1 assign to ff5q10
                capture line:13, column:42, length:1 assign to ff5q11
                capture line:13, column:43, length:1 assign to ff5q12
                capture line:13, column:44, length:1 assign to ff5q13
                capture line:13, column:45, length:1 assign to ff5q14
                capture line:13, column:46, length:1 assign to ff5q15

                // 5th fqq04-5 check complete
assign "" to firstff5q
                }
                if (ok5 == "OK"){
if (ff5q1 != " ") {
    if (ff5q2 == " ") {
        append ff5q1 to firstff5q
    }
}
if (ff5q2 != " ") {
    if (ff5q3 == " ") {
        append ff5q1 + ff5q2 to firstff5q
    }
}
if (ff5q3 != " ") {
    if (ff5q4 == " ") {
        append ff5q1 + ff5q2 + ff5q3 to firstff5q
    }
}
if (ff5q4 != " ") {
    if (ff5q5 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 to firstff5q
    }
}
if (ff5q5 != " ") {
    if (ff5q6 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 to firstff5q
    }
}
if (ff5q6 != " ") {
    if (ff5q7 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 to firstff5q
    }
}
if (ff5q7 != " ") {
    if (ff5q8 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 to firstff5q
    }
}
if (ff5q8 != " ") {
    if (ff5q9 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 to firstff5q
    }
}
if (ff5q9 != " ") {
    if (ff5q10 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 to firstff5q
    }
}
if (ff5q10 != " ") {
    if (ff5q11 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 + ff5q10 to firstff5q
    }
}
if (ff5q11 != " ") {
    if (ff5q12 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 + ff5q10 + ff5q11 to firstff5q
    }
}
if (ff5q12 != " ") {
    if (ff5q13 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 + ff5q10 + ff5q11 + ff5q12 to firstff5q
    }
}
if (ff5q13 != " ") {
    if (ff5q14 == " ") {
        append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 + ff5q10 + ff5q11 + ff5q12 + ff5q13 to firstff5q
    }
}
if (ff5q14 != " ") {
    if (ff5q15 == " ") {
    append ff5q1 + ff5q2 + ff5q3 + ff5q4 + ff5q5 + ff5q6 + ff5q7 + ff5q8 + ff5q9 + ff5q10 + ff5q11 + ff5q12 + ff5q13 + ff5q14 to firstff5q
}
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq04"
                     
                




                // 6th fqq04-6 check
                capture line:14, column:32, length:1 assign to ff6q1
                capture line:14, column:33, length:1 assign to ff6q2
                capture line:14, column:34, length:1 assign to ff6q3
                capture line:14, column:35, length:1 assign to ff6q4
                capture line:14, column:36, length:1 assign to ff6q5
                capture line:14, column:37, length:1 assign to ff6q6
                capture line:14, column:38, length:1 assign to ff6q7
                capture line:14, column:39, length:1 assign to ff6q8
                capture line:14, column:40, length:1 assign to ff6q9
                capture line:14, column:41, length:1 assign to ff6q10
                capture line:14, column:42, length:1 assign to ff6q11
                capture line:14, column:43, length:1 assign to ff6q12
                capture line:14, column:44, length:1 assign to ff6q13
                capture line:14, column:45, length:1 assign to ff6q14
                capture line:14, column:46, length:1 assign to ff6q15
                
                // 6th fqq04-6 check complete
                assign "" to firstff6q
                }
                if (ok6 == "OK"){
                if (ff6q1 != " ") {
    if (ff6q2 == " ") {
        append ff6q1 to firstff6q
    }
}
if (ff6q2 != " ") {
    if (ff6q3 == " ") {
        append ff6q1 + ff6q2 to firstff6q
    }
}
if (ff6q3 != " ") {
    if (ff6q4 == " ") {
        append ff6q1 + ff6q2 + ff6q3 to firstff6q
    }
}
if (ff6q4 != " ") {
    if (ff6q5 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 to firstff6q
    }
}
if (ff6q5 != " ") {
    if (ff6q6 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 to firstff6q
    }
}
if (ff6q6 != " ") {
    if (ff6q7 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 to firstff6q
    }
}
if (ff6q7 != " ") {
    if (ff6q8 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 to firstff6q
    }
}
if (ff6q8 != " ") {
    if (ff6q9 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 to firstff6q
    }
}
if (ff6q9 != " ") {
    if (ff6q10 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 to firstff6q
    }
}
if (ff6q10 != " ") {
    if (ff6q11 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 + ff6q10 to firstff6q
    }
}
if (ff6q11 != " ") {
    if (ff6q12 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 + ff6q10 + ff6q11 to firstff6q
    }
}
if (ff6q12 != " ") {
    if (ff6q13 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 + ff6q10 + ff6q11 + ff6q12 to firstff6q
    }
}
if (ff6q13 != " ") {
    if (ff6q14 == " ") {
        append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 + ff6q10 + ff6q11 + ff6q12 + ff6q13 to firstff6q
    }
}
if (ff6q14 != " ") {
    if (ff6q15 == " ") {
    append ff6q1 + ff6q2 + ff6q3 + ff6q4 + ff6q5 + ff6q6 + ff6q7 + ff6q8 + ff6q9 + ff6q10 + ff6q11 + ff6q12 + ff6q13 + ff6q14 to firstff6q
}
                }
                }
                }
                }
                }
                }else {
                 send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                 send "fqq05" 
                 capture line:3, column:1, length:5 assign to check5
                }
                
     if (check5 != "check"){



                 // 1st farecheck fqq05
                capture line:9, column:32, length:1 assign to ff1qq1
                capture line:9, column:33, length:1 assign to ff1qq2
                capture line:9, column:34, length:1 assign to ff1qq3
                capture line:9, column:35, length:1 assign to ff1qq4
                capture line:9, column:36, length:1 assign to ff1qq5
                capture line:9, column:37, length:1 assign to ff1qq6
                capture line:9, column:38, length:1 assign to ff1qq7
                capture line:9, column:39, length:1 assign to ff1qq8
                capture line:9, column:40, length:1 assign to ff1qq9
                capture line:9, column:41, length:1 assign to ff1qq10
                capture line:9, column:42, length:1 assign to ff1qq11
                capture line:9, column:43, length:1 assign to ff1qq12
                capture line:9, column:44, length:1 assign to ff1qq13
                capture line:9, column:45, length:1 assign to ff1qq14
                capture line:9, column:46, length:1 assign to ff1qq15

                // first fare base , fqq05-1 check complete 



 assign "" to firstff1qq
 if (ff1qq1 != " ") {
    if (ff1qq2 == " ") {
        append ff1qq1 to firstff1qq
    }
}
if (ff1qq2 != " ") {
    if (ff1qq3 == " ") {
        append ff1qq1 + ff1qq2 to firstff1qq
    }
}
if (ff1qq3 != " ") {
    if (ff1qq4 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 to firstff1qq
    }
}
if (ff1qq4 != " ") {
    if (ff1qq5 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 to firstff1qq
    }
}
if (ff1qq5 != " ") {
    if (ff1qq6 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 to firstff1qq
    }
}
if (ff1qq6 != " ") {
    if (ff1qq7 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 to firstff1qq
    }
}
if (ff1qq7 != " ") {
    if (ff1qq8 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 to firstff1qq
    }
}
if (ff1qq8 != " ") {
    if (ff1qq9 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 to firstff1qq
    }
}
if (ff1qq9 != " ") {
    if (ff1qq10 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 to firstff1qq
    }
}
if (ff1qq10 != " ") {
    if (ff1qq11 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 + ff1qq10 to firstff1qq
    }
}
if (ff1qq11 != " ") {
    if (ff1qq12 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 + ff1qq10 + ff1qq11 to firstff1qq
    }
}
if (ff1qq12 != " ") {
    if (ff1qq13 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 + ff1qq10 + ff1qq11 + ff1qq12 to firstff1qq
    }
}
if (ff1qq13 != " ") {
    if (ff1qq14 == " ") {
        append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 + ff1qq10 + ff1qq11 + ff1qq12 + ff1qq13 to firstff1qq
    }
}
if (ff1qq14 != " ") {
 if (ff1qq15 == " ") {  
    append ff1qq1 + ff1qq2 + ff1qq3 + ff1qq4 + ff1qq5 + ff1qq6 + ff1qq7 + ff1qq8 + ff1qq9 + ff1qq10 + ff1qq11 + ff1qq12 + ff1qq13 + ff1qq14 to firstff1qq
 }
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq05"
                     
                



                        
                    // 2nd fqq05-2 check
                capture line:10, column:32, length:1 assign to ff2qq1
                capture line:10, column:33, length:1 assign to ff2qq2
                capture line:10, column:34, length:1 assign to ff2qq3
                capture line:10, column:35, length:1 assign to ff2qq4
                capture line:10, column:36, length:1 assign to ff2qq5
                capture line:10, column:37, length:1 assign to ff2qq6
                capture line:10, column:38, length:1 assign to ff2qq7
                capture line:10, column:39, length:1 assign to ff2qq8
                capture line:10, column:40, length:1 assign to ff2qq9
                capture line:10, column:41, length:1 assign to ff2qq10
                capture line:10, column:42, length:1 assign to ff2qq11
                capture line:10, column:43, length:1 assign to ff2qq12
                capture line:10, column:44, length:1 assign to ff2qq13
                capture line:10, column:45, length:1 assign to ff2qq14
                capture line:10, column:46, length:1 assign to ff2qq15

                // 2nd fqq05-2 check complete
                        assign "" to firstff2qq
                }
                if (OK2 == "OK"){
                if (ff2qq1 != " ") {
    if (ff2qq2 == " ") {
        append ff2qq1 to firstff2qq
    }
}
if (ff2qq2 != " ") {
    if (ff2qq3 == " ") {
        append ff2qq1 + ff2qq2 to firstff2qq
    }
}
if (ff2qq3 != " ") {
    if (ff2qq4 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 to firstff2qq
    }
}
if (ff2qq4 != " ") {
    if (ff2qq5 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 to firstff2qq
    }
}
if (ff2qq5 != " ") {
    if (ff2qq6 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 to firstff2qq
    }
}
if (ff2qq6 != " ") {
    if (ff2qq7 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 to firstff2qq
    }
}
if (ff2qq7 != " ") {
    if (ff2qq8 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 to firstff2qq
    }
}
if (ff2qq8 != " ") {
    if (ff2qq9 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 to firstff2qq
    }
}
if (ff2qq9 != " ") {
    if (ff2qq10 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 to firstff2qq
    }
}
if (ff2qq10 != " ") {
    if (ff2qq11 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 + ff2qq10 to firstff2qq
    }
}
if (ff2qq11 != " ") {
    if (ff2qq12 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 + ff2qq10 + ff2qq11 to firstff2qq
    }
}
if (ff2qq12 != " ") {
    if (ff2qq13 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 + ff2qq10 + ff2qq11 + ff2qq12 to firstff2qq
    }
}
if (ff2qq13 != " ") {
    if (ff2qq14 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 + ff2qq10 + ff2qq11 + ff2qq12 + ff2qq13 to firstff2qq
    }
}
if (ff2qq14 != " ") {
    if (ff2qq15 == " ") {
        append ff2qq1 + ff2qq2 + ff2qq3 + ff2qq4 + ff2qq5 + ff2qq6 + ff2qq7 + ff2qq8 + ff2qq9 + ff2qq10 + ff2qq11 + ff2qq12 + ff2qq13 + ff2qq14 to firstff2qq
                }
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq05"
                      
                


                // 3rd fqq05-3 check

                capture line:11, column:32, length:1 assign to ff3qq1
                capture line:11, column:33, length:1 assign to ff3qq2
                capture line:11, column:34, length:1 assign to ff3qq3
                capture line:11, column:35, length:1 assign to ff3qq4
                capture line:11, column:36, length:1 assign to ff3qq5
                capture line:11, column:37, length:1 assign to ff3qq6
                capture line:11, column:38, length:1 assign to ff3qq7
                capture line:11, column:39, length:1 assign to ff3qq8
                capture line:11, column:40, length:1 assign to ff3qq9
                capture line:11, column:41, length:1 assign to ff3qq10
                capture line:11, column:42, length:1 assign to ff3qq11
                capture line:11, column:43, length:1 assign to ff3qq12
                capture line:11, column:44, length:1 assign to ff3qq13
                capture line:11, column:45, length:1 assign to ff3qq14
                capture line:11, column:46, length:1 assign to ff3qq15

                // 3th fqq05-3 check complete
                    assign "" to firstff3qq
                }
                if (OK3 == "OK"){
       if (ff3qq1 != " ") {
    if (ff3qq2 == " ") {
        append ff3qq1 to firstff3qq
    }
}
if (ff3qq2 != " ") {
    if (ff3qq3 == " ") {
        append ff3qq1 + ff3qq2 to firstff3qq
    }
}
if (ff3qq3 != " ") {
    if (ff3qq4 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 to firstff3qq
    }
}
if (ff3qq4 != " ") {
    if (ff3qq5 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 to firstff3qq
    }
}
if (ff3qq5 != " ") {
    if (ff3qq6 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 to firstff3qq
    }
}
if (ff3qq6 != " ") {
    if (ff3qq7 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 to firstff3qq
    }
}
if (ff3qq7 != " ") {
    if (ff3qq8 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 to firstff3qq
    }
}
if (ff3qq8 != " ") {
    if (ff3qq9 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 to firstff3qq
    }
}
if (ff3qq9 != " ") {
    if (ff3qq10 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 to firstff3qq
    }
}
if (ff3qq10 != " ") {
    if (ff3qq11 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 + ff3qq10 to firstff3qq
    }
}
if (ff3qq11 != " ") {
    if (ff3qq12 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 + ff3qq10 + ff3qq11 to firstff3qq
    }
}
if (ff3qq12 != " ") {
    if (ff3qq13 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 + ff3qq10 + ff3qq11 + ff3qq12 to firstff3qq
    }
}
if (ff3qq13 != " ") {
    if (ff3qq14 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 + ff3qq10 + ff3qq11 + ff3qq12 + ff3qq13 to firstff3qq
    }
}
if (ff3qq14 != " ") {
    if (ff3qq15 == " ") {
        append ff3qq1 + ff3qq2 + ff3qq3 + ff3qq4 + ff3qq5 + ff3qq6 + ff3qq7 + ff3qq8 + ff3qq9 + ff3qq10 + ff3qq11 + ff3qq12 + ff3qq13 + ff3qq14 to firstff3qq
    }
}else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq05"
                   
                



                // 4th fqq05-4 check
                capture line:12, column:32, length:1 assign to ff4qq1
                capture line:12, column:33, length:1 assign to ff4qq2
                capture line:12, column:34, length:1 assign to ff4qq3
                capture line:12, column:35, length:1 assign to ff4qq4
                capture line:12, column:36, length:1 assign to ff4qq5
                capture line:12, column:37, length:1 assign to ff4qq6
                capture line:12, column:38, length:1 assign to ff4qq7
                capture line:12, column:39, length:1 assign to ff4qq8
                capture line:12, column:40, length:1 assign to ff4qq9
                capture line:12, column:41, length:1 assign to ff4qq10
                capture line:12, column:42, length:1 assign to ff4qq11
                capture line:12, column:43, length:1 assign to ff4qq12
                capture line:12, column:44, length:1 assign to ff4qq13
                capture line:12, column:45, length:1 assign to ff4qq14
                capture line:12, column:46, length:1 assign to ff4qq15
                
                // 4th fqq05-4 check complete
                assign "" to firstff4qq
}
                
if (OK4 == "OK"){
     if (ff4qq1 != " ") {
    if (ff4qq2 == " ") {
        append ff4qq1 to firstff4qq
    }
}
if (ff4qq2 != " ") {
    if (ff4qq3 == " ") {
        append ff4qq1 + ff4qq2 to firstff4qq
    }
}
if (ff4qq3 != " ") {
    if (ff4qq4 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 to firstff4qq
    }
}
if (ff4qq4 != " ") {
    if (ff4qq5 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 to firstff4qq
    }
}
if (ff4qq5 != " ") {
    if (ff4qq6 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 to firstff4qq
    }
}
if (ff4qq6 != " ") {
    if (ff4qq7 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 to firstff4qq
    }
}
if (ff4qq7 != " ") {
    if (ff4qq8 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 to firstff4qq
    }
}
if (ff4qq8 != " ") {
    if (ff4qq9 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 to firstff4qq
    }
}
if (ff4qq9 != " ") {
    if (ff4qq10 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 to firstff4qq
    }
}
if (ff4qq10 != " ") {
    if (ff4qq11 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 + ff4qq10 to firstff4qq
    }
}
if (ff4qq11 != " ") {
    if (ff4qq12 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 + ff4qq10 + ff4qq11 to firstff4qq
    }
}
if (ff4qq12 != " ") {
    if (ff4qq13 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 + ff4qq10 + ff4qq11 + ff4qq12 to firstff4qq
    }
}
if (ff4qq13 != " ") {
    if (ff4qq14 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 + ff4qq10 + ff4qq11 + ff4qq12 + ff4qq13 to firstff4qq
    }
}
if (ff4qq14 != " ") {
    if (ff4qq15 == " ") {
        append ff4qq1 + ff4qq2 + ff4qq3 + ff4qq4 + ff4qq5 + ff4qq6 + ff4qq7 + ff4qq8 + ff4qq9 + ff4qq10 + ff4qq11 + ff4qq12 + ff4qq13 + ff4qq14 to firstff4qq
                }
                }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq05"
                   
    
                // 5th fqq05-5 check
                capture line:13, column:32, length:1 assign to ff5qq1
                capture line:13, column:33, length:1 assign to ff5qq2
                capture line:13, column:34, length:1 assign to ff5qq3
                capture line:13, column:35, length:1 assign to ff5qq4
                capture line:13, column:36, length:1 assign to ff5qq5
                capture line:13, column:37, length:1 assign to ff5qq6
                capture line:13, column:38, length:1 assign to ff5qq7
                capture line:13, column:39, length:1 assign to ff5qq8
                capture line:13, column:40, length:1 assign to ff5qq9
                capture line:13, column:41, length:1 assign to ff5qq10
                capture line:13, column:42, length:1 assign to ff5qq11
                capture line:13, column:43, length:1 assign to ff5qq12
                capture line:13, column:44, length:1 assign to ff5qq13
                capture line:13, column:45, length:1 assign to ff5qq14
                capture line:13, column:46, length:1 assign to ff5qq15

                // 5th fqq05-5 check complete
                assign "" to firstff5qq
                }
                
                if (OK5 == "OK"){
                if (ff5qq1 != " ") {
    if (ff5qq2 == " ") {
        append ff5qq1 to firstff5qq
    }
}
if (ff5qq2 != " ") {
    if (ff5qq3 == " ") {
        append ff5qq1 + ff5qq2 to firstff5qq
    }
}
if (ff5qq3 != " ") {
    if (ff5qq4 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 to firstff5qq
    }
}
if (ff5qq4 != " ") {
    if (ff5qq5 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 to firstff5qq
    }
}
if (ff5qq5 != " ") {
    if (ff5qq6 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 to firstff5qq
    }
}
if (ff5qq6 != " ") {
    if (ff5qq7 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 to firstff5qq
    }
}
if (ff5qq7 != " ") {
    if (ff5qq8 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 to firstff5qq
    }
}
if (ff5qq8 != " ") {
    if (ff5qq9 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 to firstff5qq
    }
}
if (ff5qq9 != " ") {
    if (ff5qq10 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 to firstff5qq
    }
}
if (ff5qq10 != " ") {
    if (ff5qq11 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 + ff5qq10 to firstff5qq
    }
}
if (ff5qq11 != " ") {
    if (ff5qq12 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 + ff5qq10 + ff5qq11 to firstff5qq
    }
}
if (ff5qq12 != " ") {
    if (ff5qq13 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 + ff5qq10 + ff5qq11 + ff5qq12 to firstff5qq
    }
}
if (ff5qq13 != " ") {
    if (ff5qq14 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 + ff5qq10 + ff5qq11 + ff5qq12 + ff5qq13 to firstff5qq
    }
}
if (ff5qq14 != " ") {
    if (ff5qq15 == " ") {
        append ff5qq1 + ff5qq2 + ff5qq3 + ff5qq4 + ff5qq5 + ff5qq6 + ff5qq7 + ff5qq8 + ff5qq9 + ff5qq10 + ff5qq11 + ff5qq12 + ff5qq13 + ff5qq14 to firstff5qq
                }
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq05"
                     
                


                // 6th fqq05-6 check
                capture line:14, column:32, length:1 assign to ff6qq1
                capture line:14, column:33, length:1 assign to ff6qq2
                capture line:14, column:34, length:1 assign to ff6qq3
                capture line:14, column:35, length:1 assign to ff6qq4
                capture line:14, column:36, length:1 assign to ff6qq5
                capture line:14, column:37, length:1 assign to ff6qq6
                capture line:14, column:38, length:1 assign to ff6qq7
                capture line:14, column:39, length:1 assign to ff6qq8
                capture line:14, column:40, length:1 assign to ff6qq9
                capture line:14, column:41, length:1 assign to ff6qq10
                capture line:14, column:42, length:1 assign to ff6qq11
                capture line:14, column:43, length:1 assign to ff6qq12
                capture line:14, column:44, length:1 assign to ff6qq13
                capture line:14, column:45, length:1 assign to ff6qq14
                capture line:14, column:46, length:1 assign to ff6qq15
                
                // 6th fqq05-6 check complete
                assign "" to firstff6qq
                }
   if (OK6 == "OK"){
   if (ff6qq1 != " ") {
    if (ff6qq2 == " ") {
        append ff6qq1 to firstff6qq
    }
}
if (ff6qq2 != " ") {
    if (ff6qq3 == " ") {
        append ff6qq1 + ff6qq2 to firstff6qq
    }
}
if (ff6qq3 != " ") {
    if (ff6qq4 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 to firstff6qq
    }
}
if (ff6qq4 != " ") {
    if (ff6qq5 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 to firstff6qq
    }
}
if (ff6qq5 != " ") {
    if (ff6qq6 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 to firstff6qq
    }
}
if (ff6qq6 != " ") {
    if (ff6qq7 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 to firstff6qq
    }
}
if (ff6qq7 != " ") {
    if (ff6qq8 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 to firstff6qq
    }
}
if (ff6qq8 != " ") {
    if (ff6qq9 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 to firstff6qq
    }
}
if (ff6qq9 != " ") {
    if (ff6qq10 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 to firstff6qq
    }
}
if (ff6qq10 != " ") {
    if (ff6qq11 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 + ff6qq10 to firstff6qq
    }
}
if (ff6qq11 != " ") {
    if (ff6qq12 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 + ff6qq10 + ff6qq11 to firstff6qq
    }
}
if (ff6qq12 != " ") {
    if (ff6qq13 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 + ff6qq10 + ff6qq11 + ff6qq12 to firstff6qq
    }
}
if (ff6qq13 != " ") {
    if (ff6qq14 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 + ff6qq10 + ff6qq11 + ff6qq12 + ff6qq13 to firstff6qq
    }
}
if (ff6qq14 != " ") {
    if (ff6qq15 == " ") {
        append ff6qq1 + ff6qq2 + ff6qq3 + ff6qq4 + ff6qq5 + ff6qq6 + ff6qq7 + ff6qq8 + ff6qq9 + ff6qq10 + ff6qq11 + ff6qq12 + ff6qq13 + ff6qq14 to firstff6qq
                }
}
   }
                }
}
                }
                }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                capture line:3, column:1, length:5 assign to check6
                }
     if (check6 != "check"){

                //--------------------------------------------------------------------------------------


                        // checkfqq06

                  // 1st farecheckfqq06
                capture line:9, column:32, length:1 assign to fff1qq1
                capture line:9, column:33, length:1 assign to fff1qq2
                capture line:9, column:34, length:1 assign to fff1qq3
                capture line:9, column:35, length:1 assign to fff1qq4
                capture line:9, column:36, length:1 assign to fff1qq5
                capture line:9, column:37, length:1 assign to fff1qq6
                capture line:9, column:38, length:1 assign to fff1qq7
                capture line:9, column:39, length:1 assign to fff1qq8
                capture line:9, column:40, length:1 assign to fff1qq9
                capture line:9, column:41, length:1 assign to fff1qq10
                capture line:9, column:42, length:1 assign to fff1qq11
                capture line:9, column:43, length:1 assign to fff1qq12
                capture line:9, column:44, length:1 assign to fff1qq13
                capture line:9, column:45, length:1 assign to fff1qq14
                capture line:9, column:46, length:1 assign to fff1qq15

                // first fare base ,fqq06-1 check complete 
                assign "" to firstfff1qq
 if (fff1qq1 != " ") {
    if (fff1qq2 == " ") {
        append fff1qq1 to firstfff1qq
    }
}
if (fff1qq2 != " ") {
    if (fff1qq3 == " ") {
        append fff1qq1 + fff1qq2 to firstfff1qq
    }
}
if (fff1qq3 != " ") {
    if (fff1qq4 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 to firstfff1qq
    }
}
if (fff1qq4 != " ") {
    if (fff1qq5 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 to firstfff1qq
    }
}
if (fff1qq5 != " ") {
    if (fff1qq6 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 to firstfff1qq
    }
}
if (fff1qq6 != " ") {
    if (fff1qq7 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 to firstfff1qq
    }
}
if (fff1qq7 != " ") {
    if (fff1qq8 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 to firstfff1qq
    }
}
if (fff1qq8 != " ") {
    if (fff1qq9 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 to firstfff1qq
    }
}
if (fff1qq9 != " ") {
    if (fff1qq10 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 to firstfff1qq
    }
}
if (fff1qq10 != " ") {
    if (fff1qq11 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 + fff1qq10 to firstfff1qq
    }
}
if (fff1qq11 != " ") {
    if (fff1qq12 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 + fff1qq10 + fff1qq11 to firstfff1qq
    }
}
if (fff1qq12 != " ") {
    if (fff1qq13 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 + fff1qq10 + fff1qq11 + fff1qq12 to firstfff1qq
    }
}
if (fff1qq13 != " ") {
    if (fff1qq14 == " ") {
        append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 + fff1qq10 + fff1qq11 + fff1qq12 + fff1qq13 to firstfff1qq
    }
}
if (fff1qq14 != " ") {
if (fff1qq15 == " ") {
    append fff1qq1 + fff1qq2 + fff1qq3 + fff1qq4 + fff1qq5 + fff1qq6 + fff1qq7 + fff1qq8 + fff1qq9 + fff1qq10 + fff1qq11 + fff1qq12 + fff1qq13 + fff1qq14 to firstfff1qq
}

                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                

                // 2ndfqq06-2 check
                capture line:10, column:32, length:1 assign to fff2qq1
                capture line:10, column:33, length:1 assign to fff2qq2
                capture line:10, column:34, length:1 assign to fff2qq3
                capture line:10, column:35, length:1 assign to fff2qq4
                capture line:10, column:36, length:1 assign to fff2qq5
                capture line:10, column:37, length:1 assign to fff2qq6
                capture line:10, column:38, length:1 assign to fff2qq7
                capture line:10, column:39, length:1 assign to fff2qq8
                capture line:10, column:40, length:1 assign to fff2qq9
                capture line:10, column:41, length:1 assign to fff2qq10
                capture line:10, column:42, length:1 assign to fff2qq11
                capture line:10, column:43, length:1 assign to fff2qq12
                capture line:10, column:44, length:1 assign to fff2qq13
                capture line:10, column:45, length:1 assign to fff2qq14
                capture line:10, column:46, length:1 assign to fff2qq15

                // 2ndfqq06-2 check complete
                assign "" to firstfff2qq
                }
                if (OK2=="OK"){
                 if (fff2qq1 != " ") {
    if (fff2qq2 == " ") {
        append fff2qq1 to firstfff2qq
    }
}
if (fff2qq2 != " ") {
    if (fff2qq3 == " ") {
        append fff2qq1 + fff2qq2 to firstfff2qq
    }
}
if (fff2qq3 != " ") {
    if (fff2qq4 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 to firstfff2qq
    }
}
if (fff2qq4 != " ") {
    if (fff2qq5 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 to firstfff2qq
    }
}
if (fff2qq5 != " ") {
    if (fff2qq6 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 to firstfff2qq
    }
}
if (fff2qq6 != " ") {
    if (fff2qq7 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 to firstfff2qq
    }
}
if (fff2qq7 != " ") {
    if (fff2qq8 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 to firstfff2qq
    }
}
if (fff2qq8 != " ") {
    if (fff2qq9 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 to firstfff2qq
    }
}
if (fff2qq9 != " ") {
    if (fff2qq10 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 to firstfff2qq
    }
}
if (fff2qq10 != " ") {
    if (fff2qq11 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 + fff2qq10 to firstfff2qq
    }
}
if (fff2qq11 != " ") {
    if (fff2qq12 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 + fff2qq10 + fff2qq11 to firstfff2qq
    }
}
if (fff2qq12 != " ") {
    if (fff2qq13 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 + fff2qq10 + fff2qq11 + fff2qq12 to firstfff2qq
    }
}
if (fff2qq13 != " ") {
    if (fff2qq14 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 + fff2qq10 + fff2qq11 + fff2qq12 + fff2qq13 to firstfff2qq
    }
}
if (fff2qq14 != " ") {
    if (fff2qq15 == " ") {
        append fff2qq1 + fff2qq2 + fff2qq3 + fff2qq4 + fff2qq5 + fff2qq6 + fff2qq7 + fff2qq8 + fff2qq9 + fff2qq10 + fff2qq11 + fff2qq12 + fff2qq13 + fff2qq14 to firstfff2qq
    }
                } else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                




                // 3rdfqq06-3 check

                capture line:11, column:32, length:1 assign to fff3qq1
                capture line:11, column:33, length:1 assign to fff3qq2
                capture line:11, column:34, length:1 assign to fff3qq3
                capture line:11, column:35, length:1 assign to fff3qq4
                capture line:11, column:36, length:1 assign to fff3qq5
                capture line:11, column:37, length:1 assign to fff3qq6
                capture line:11, column:38, length:1 assign to fff3qq7
                capture line:11, column:39, length:1 assign to fff3qq8
                capture line:11, column:40, length:1 assign to fff3qq9
                capture line:11, column:41, length:1 assign to fff3qq10
                capture line:11, column:42, length:1 assign to fff3qq11
                capture line:11, column:43, length:1 assign to fff3qq12
                capture line:11, column:44, length:1 assign to fff3qq13
                capture line:11, column:45, length:1 assign to fff3qq14
                capture line:11, column:46, length:1 assign to fff3qq15

                // 3thfqq06-3 check complete
                 assign "" to firstfff3qq
                }
                if (OK3=="OK"){
                 if (fff3qq1 != " ") {
    if (fff3qq2 == " ") {
        append fff3qq1 to firstfff3qq
    }
}
if (fff3qq2 != " ") {
    if (fff3qq3 == " ") {
        append fff3qq1 + fff3qq2 to firstfff3qq
    }
}
if (fff3qq3 != " ") {
    if (fff3qq4 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 to firstfff3qq
    }
}
if (fff3qq4 != " ") {
    if (fff3qq5 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 to firstfff3qq
    }
}
if (fff3qq5 != " ") {
    if (fff3qq6 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 to firstfff3qq
    }
}
if (fff3qq6 != " ") {
    if (fff3qq7 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 to firstfff3qq
    }
}
if (fff3qq7 != " ") {
    if (fff3qq8 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 to firstfff3qq
    }
}
if (fff3qq8 != " ") {
    if (fff3qq9 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 to firstfff3qq
    }
}
if (fff3qq9 != " ") {
    if (fff3qq10 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 to firstfff3qq
    }
}
if (fff3qq10 != " ") {
    if (fff3qq11 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 + fff3qq10 to firstfff3qq
    }
}
if (fff3qq11 != " ") {
    if (fff3qq12 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 + fff3qq10 + fff3qq11 to firstfff3qq
    }
}
if (fff3qq12 != " ") {
    if (fff3qq13 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 + fff3qq10 + fff3qq11 + fff3qq12 to firstfff3qq
    }
}
if (fff3qq13 != " ") {
    if (fff3qq14 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 + fff3qq10 + fff3qq11 + fff3qq12 + fff3qq13 to firstfff3qq
    }
}
if (fff3qq14 != " ") {
    if (fff3qq15 == " ") {
        append fff3qq1 + fff3qq2 + fff3qq3 + fff3qq4 + fff3qq5 + fff3qq6 + fff3qq7 + fff3qq8 + fff3qq9 + fff3qq10 + fff3qq11 + fff3qq12 + fff3qq13 + fff3qq14 to firstfff3qq
    }
 }else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                   
                



                // 4thfqq06-4 check
                capture line:12, column:32, length:1 assign to fff4qq1
                capture line:12, column:33, length:1 assign to fff4qq2
                capture line:12, column:34, length:1 assign to fff4qq3
                capture line:12, column:35, length:1 assign to fff4qq4
                capture line:12, column:36, length:1 assign to fff4qq5
                capture line:12, column:37, length:1 assign to fff4qq6
                capture line:12, column:38, length:1 assign to fff4qq7
                capture line:12, column:39, length:1 assign to fff4qq8
                capture line:12, column:40, length:1 assign to fff4qq9
                capture line:12, column:41, length:1 assign to fff4qq10
                capture line:12, column:42, length:1 assign to fff4qq11
                capture line:12, column:43, length:1 assign to fff4qq12
                capture line:12, column:44, length:1 assign to fff4qq13
                capture line:12, column:45, length:1 assign to fff4qq14
                capture line:12, column:46, length:1 assign to fff4qq15
                

                // 4thfqq06-4 check complete
                assign "" to firstfff4qq
 }
                if (OK4=="OK"){
                 if (fff4qq1 != " ") {
    if (fff4qq2 == " ") {
        append fff4qq1 to firstfff4qq
    }
}
if (fff4qq2 != " ") {
    if (fff4qq3 == " ") {
        append fff4qq1 + fff4qq2 to firstfff4qq
    }
}
if (fff4qq3 != " ") {
    if (fff4qq4 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 to firstfff4qq
    }
}
if (fff4qq4 != " ") {
    if (fff4qq5 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 to firstfff4qq
    }
}
if (fff4qq5 != " ") {
    if (fff4qq6 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 to firstfff4qq
    }
}
if (fff4qq6 != " ") {
    if (fff4qq7 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 to firstfff4qq
    }
}
if (fff4qq7 != " ") {
    if (fff4qq8 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 to firstfff4qq
    }
}
if (fff4qq8 != " ") {
    if (fff4qq9 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 to firstfff4qq
    }
}
if (fff4qq9 != " ") {
    if (fff4qq10 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 to firstfff4qq
    }
}
if (fff4qq10 != " ") {
    if (fff4qq11 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 + fff4qq10 to firstfff4qq
    }
}
if (fff4qq11 != " ") {
    if (fff4qq12 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 + fff4qq10 + fff4qq11 to firstfff4qq
    }
}
if (fff4qq12 != " ") {
    if (fff4qq13 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 + fff4qq10 + fff4qq11 + fff4qq12 to firstfff4qq
    }
}
if (fff4qq13 != " ") {
    if (fff4qq14 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 + fff4qq10 + fff4qq11 + fff4qq12 + fff4qq13 to firstfff4qq
    }
}
if (fff4qq14 != " ") {
    if (fff4qq15 == " ") {
        append fff4qq1 + fff4qq2 + fff4qq3 + fff4qq4 + fff4qq5 + fff4qq6 + fff4qq7 + fff4qq8 + fff4qq9 + fff4qq10 + fff4qq11 + fff4qq12 + fff4qq13 + fff4qq14 to firstfff4qq
    }
} else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                     
                


                // 5thfqq06-5 check
                capture line:13, column:32, length:1 assign to fff5qq1
                capture line:13, column:33, length:1 assign to fff5qq2
                capture line:13, column:34, length:1 assign to fff5qq3
                capture line:13, column:35, length:1 assign to fff5qq4
                capture line:13, column:36, length:1 assign to fff5qq5
                capture line:13, column:37, length:1 assign to fff5qq6
                capture line:13, column:38, length:1 assign to fff5qq7
                capture line:13, column:39, length:1 assign to fff5qq8
                capture line:13, column:40, length:1 assign to fff5qq9
                capture line:13, column:41, length:1 assign to fff5qq10
                capture line:13, column:42, length:1 assign to fff5qq11
                capture line:13, column:43, length:1 assign to fff5qq12
                capture line:13, column:44, length:1 assign to fff5qq13
                capture line:13, column:45, length:1 assign to fff5qq14
                capture line:13, column:46, length:1 assign to fff5qq15

                // 5thfqq06-5 check complete
                assign "" to firstfff5qq
}
            
                if (OK5=="OK"){
                if (fff5qq1 != " ") {
    if (fff5qq2 == " ") {
        append fff5qq1 to firstfff5qq
    }
}
if (fff5qq2 != " ") {
    if (fff5qq3 == " ") {
        append fff5qq1 + fff5qq2 to firstfff5qq
    }
}
if (fff5qq3 != " ") {
    if (fff5qq4 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 to firstfff5qq
    }
}
if (fff5qq4 != " ") {
    if (fff5qq5 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 to firstfff5qq
    }
}
if (fff5qq5 != " ") {
    if (fff5qq6 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 to firstfff5qq
    }
}
if (fff5qq6 != " ") {
    if (fff5qq7 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 to firstfff5qq
    }
}
if (fff5qq7 != " ") {
    if (fff5qq8 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 to firstfff5qq
    }
}
if (fff5qq8 != " ") {
    if (fff5qq9 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 to firstfff5qq
    }
}
if (fff5qq9 != " ") {
    if (fff5qq10 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 to firstfff5qq
    }
}
if (fff5qq10 != " ") {
    if (fff5qq11 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 + fff5qq10 to firstfff5qq
    }
}
if (fff5qq11 != " ") {
    if (fff5qq12 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 + fff5qq10 + fff5qq11 to firstfff5qq
    }
}
if (fff5qq12 != " ") {
    if (fff5qq13 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 + fff5qq10 + fff5qq11 + fff5qq12 to firstfff5qq
    }
}
if (fff5qq13 != " ") {
    if (fff5qq14 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 + fff5qq10 + fff5qq11 + fff5qq12 + fff5qq13 to firstfff5qq
    }
}
if (fff5qq14 != " ") {
    if (fff5qq15 == " ") {
        append fff5qq1 + fff5qq2 + fff5qq3 + fff5qq4 + fff5qq5 + fff5qq6 + fff5qq7 + fff5qq8 + fff5qq9 + fff5qq10 + fff5qq11 + fff5qq12 + fff5qq13 + fff5qq14 to firstfff5qq
    }
} else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    send "fqq06"
                    
                


                // 6thfqq06-6 check
                capture line:14, column:32, length:1 assign to fff6qq1
                capture line:14, column:33, length:1 assign to fff6qq2
                capture line:14, column:34, length:1 assign to fff6qq3
                capture line:14, column:35, length:1 assign to fff6qq4
                capture line:14, column:36, length:1 assign to fff6qq5
                capture line:14, column:37, length:1 assign to fff6qq6
                capture line:14, column:38, length:1 assign to fff6qq7
                capture line:14, column:39, length:1 assign to fff6qq8
                capture line:14, column:40, length:1 assign to fff6qq9
                capture line:14, column:41, length:1 assign to fff6qq10
                capture line:14, column:42, length:1 assign to fff6qq11
                capture line:14, column:43, length:1 assign to fff6qq12
                capture line:14, column:44, length:1 assign to fff6qq13
                capture line:14, column:45, length:1 assign to fff6qq14
                capture line:14, column:46, length:1 assign to fff6qq15
                
                // 6thfqq06-6 check complete
                assign "" to firstfff6qq
}
                
                if (OK6=="OK"){
                if (fff6qq1 != " ") {
    if (fff6qq2 == " ") {
        append fff6qq1 to firstfff6qq
    }
}
if (fff6qq2 != " ") {
    if (fff6qq3 == " ") {
        append fff6qq1 + fff6qq2 to firstfff6qq
    }
}
if (fff6qq3 != " ") {
    if (fff6qq4 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 to firstfff6qq
    }
}
if (fff6qq4 != " ") {
    if (fff6qq5 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 to firstfff6qq
    }
}
if (fff6qq5 != " ") {
    if (fff6qq6 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 to firstfff6qq
    }
}
if (fff6qq6 != " ") {
    if (fff6qq7 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 to firstfff6qq
    }
}
if (fff6qq7 != " ") {
    if (fff6qq8 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 to firstfff6qq
    }
}
if (fff6qq8 != " ") {
    if (fff6qq9 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 to firstfff6qq
    }
}
if (fff6qq9 != " ") {
    if (fff6qq10 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 to firstfff6qq
    }
}
if (fff6qq10 != " ") {
    if (fff6qq11 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 + fff6qq10 to firstfff6qq
    }
}
if (fff6qq11 != " ") {
    if (fff6qq12 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 + fff6qq10 + fff6qq11 to firstfff6qq
    }
}

if (fff6qq12 != " ") {
    if (fff6qq13 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 + fff6qq10 + fff6qq11 + fff6qq12 to firstfff6qq
    }
}
if (fff6qq13 != " ") {
    if (fff6qq14 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 + fff6qq10 + fff6qq11 + fff6qq12 + fff6qq13 to firstfff6qq
    }
}
if (fff6qq14 != " ") {
    if (fff6qq15 == " ") {
        append fff6qq1 + fff6qq2 + fff6qq3 + fff6qq4 + fff6qq5 + fff6qq6 + fff6qq7 + fff6qq8 + fff6qq9 + fff6qq10 + fff6qq11 + fff6qq12 + fff6qq13 + fff6qq14 to firstfff6qq
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
}else {
                    send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                }
                //----------------------------------------------------------------------------------------------------------------------------------------------
                //All six fqq01- fqq06 checked captured accordingg to tkt fares  
                //--------------------------------------------------------------------------------------------------------------------------------

                // first case onefare
                if (OK2 != "OK"){
                if (fb1check == first) {
                    send "fqn1-1*pe"
                    capture line:1, column:1, length:3 assign to fqn1w1check
                    if (fqn1w1check == "FQN") {
                        send "m"
                        send "m"
                        send "m"
                    }
                    }else{
                        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    
                    if (fb1check == firstffq){
                        send "fqn2-1*pe"
                       capture line:1, column:1, length:3 assign to fqn1w2check 
                    if (fqn1w2check == "FQN") {
                        send "m"
                        send "m"
                        send "m"
                    }
                    }else{
                        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    
                    if (fb1check == firstf1q){
                        send "fqn3-1*pe"
                       capture line:1, column:1, length:3 assign to fqn1w3check 
                    if (fqn1w3check == "FQN") {
                        send "m"
                        send "m"
                        send "m"
                    }
                    }else{
                        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    
                    if (fb1check == firstff1q ){
                        send "fqn4-1*pe"
                       capture line:1, column:1, length:3 assign to fqn1w4check 
                    if (fqn1w4check == "FQN") {
                        send "m"
                        send "m"
                        send "m"
                    }
                    }else{
                        send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                    }
                    if (fb1check == firstff1qq){
                        send "fqn5-1*pe"
                        capture line:1, column:1, length:3 assign to fqn1w5check
                        if (fqn1w5check == "FQN") {
                            send "m"
                            send "m"
                            send "m"
                        }
                        }else{
                            send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                        
                        if (fb1check == firstfff1qq){
                            send "fqn6-1*pe"
                            capture line:1, column:1, length:3 assign to fqn1w6check
                            if (fqn1w6check == "FQN") {
                                send "m"
                                send "m"
                                send "m"
                            }
                            }
                            }
                            }
                            }
                            }
                            }else{
                                send "FQP" + FQPCommand + "/R," + DOI + tourcode1
                            }
                         // first fare opendone incase of onefare  
                                //----------------------------------------------------------------
                                //secondcase ifthere istwo fare same name 
                                //----------------------------------------------------------------
                                // second fare same name case onefare                        
                           