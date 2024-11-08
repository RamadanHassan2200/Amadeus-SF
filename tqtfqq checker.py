capture line:1, column:1, length:3 assign to firstcheck

if (firstcheck=="TST"){

capture line:1, column:57, length:6 assign to ODTST

capture line:10, column:1, length:11 assign to grandcheck1
if (grandcheck1=="GRAND TOTAL"){
    capture line:10, column:17, length:10 assign to TSTPrice
}
capture line:11, column:1, length:11 assign to grandcheck2
if (grandcheck2=="GRAND TOTAL"){
    capture line:11, column:17, length:10 assign to TSTPrice
}
capture line:12, column:1, length:11 assign to grandcheck3
if (grandcheck3=="GRAND TOTAL"){
    capture line:12, column:17, length:10 assign to TSTPrice
}
capture line:13, column:1, length:11 assign to grandcheck4
if (grandcheck4=="GRAND TOTAL"){
    capture line:13, column:17, length:10 assign to TSTPrice
}
capture line:14, column:1, length:11 assign to grandcheck5
if (grandcheck5=="GRAND TOTAL"){
    capture line:14, column:17, length:10 assign to TSTPrice
}
capture line:15, column:1, length:11 assign to grandcheck6
if (grandcheck6=="GRAND TOTAL"){
    capture line:15, column:17, length:10 assign to TSTPrice
}
capture line:16, column:1, length:11 assign to grandcheck7
if (grandcheck7=="GRAND TOTAL"){
    capture line:16, column:17, length:10 assign to TSTPrice
}
capture line:17, column:1, length:11 assign to grandcheck8
if (grandcheck8=="GRAND TOTAL"){
    capture line:17, column:17, length:10 assign to TSTPrice
}
capture line:18, column:1, length:11 assign to grandcheck9
if (grandcheck9=="GRAND TOTAL"){
    capture line:18, column:17, length:10 assign to TSTPrice
}
capture line:19, column:1, length:11 assign to grandcheck10
if (grandcheck10=="GRAND TOTAL"){
    capture line:19, column:17, length:10 assign to TSTPrice
}
capture line:20, column:1, length:11 assign to grandcheck11
if (grandcheck11=="GRAND TOTAL"){
    capture line:20, column:17, length:10 assign to TSTPrice
}
capture line:21, column:1, length:11 assign to grandcheck12
if (grandcheck12=="GRAND TOTAL"){
    capture line:21, column:17, length:10 assign to TSTPrice
}
capture line:22, column:1, length:11 assign to grandcheck13
if (grandcheck13=="GRAND TOTAL"){
    capture line:22, column:17, length:10 assign to TSTPrice
}
capture line:23, column:1, length:11 assign to grandcheck14
if (grandcheck14=="GRAND TOTAL"){
    capture line:23, column:17, length:10 assign to TSTPrice
}
capture line:24, column:1, length:11 assign to grandcheck15
if (grandcheck15=="GRAND TOTAL"){
    capture line:24, column:17, length:10 assign to TSTPrice
}
capture line:25, column:1, length:11 assign to grandcheck16
if (grandcheck16=="GRAND TOTAL"){
    capture line:25, column:17, length:10 assign to TSTPrice
}

send "SRT" +ODTST +TSTPrice
}
if (firstcheck=="FQQ"){

    capture line:6, column:59, length:2 assign to baggage1
    if (baggage=="BG"){
        assign "1" to BgCount
        capture line:8, column:59, length:2 assign to Bg1
        capture line:9, column:59, length:2 assign to Bg2check
        if (Bg2check!="  "){
            assign "2" to BgCount
            capture line:9, column:59, length:2 assign to Bg2
            capture line:10, column:59, length:2 assign to Bg3check
            if (Bg3check!="  "){
                assign "3" to BgCount
                capture line:10, column:59, length:2 assign to Bg3
                capture line:11, column:59, length:2 assign to Bg4check
                if (Bg4check!="  "){
                    assign "4" to BgCount
                    capture line:11, column:59, length:2 assign to Bg4
                }
            }
        }
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        assign "1" to BgCount
        capture line:9, column:59, length:2 assign to Bg1
        capture line:10, column:59, length:2 assign to Bg2check
        if (Bg2check!="  "){
            assign "2" to BgCount
            capture line:10, column:59, length:2 assign to Bg2
            capture line:11, column:59, length:2 assign to Bg3check
            if (Bg3check!="  "){
                assign "3" to BgCount
                capture line:11, column:59, length:2 assign to Bg3
                capture line:12, column:59, length:2 assign to Bg4check
                if (Bg4check!="  "){
                    assign "4" to BgCount
                    capture line:12, column:59, length:2 assign to Bg4
                }
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
        assign "1" to BgCount
        capture line:10, column:59, length:2 assign to Bg1
        capture line:11, column:59, length:2 assign to Bg2check
        if (Bg2check!="  "){
            assign "2" to BgCount
            capture line:11, column:59, length:2 assign to Bg2
            capture line:12, column:59, length:2 assign to Bg3check
            if (Bg3check!="  "){
                assign "3" to BgCount
                capture line:12, column:59, length:2 assign to Bg3
                capture line:13, column:59, length:2 assign to Bg4check
                if (Bg4check!="  "){
                    assign "4" to BgCount
                    capture line:13, column:59, length:2 assign to Bg4
                }
            }
        }
    }
    capture line:9, column:59, length:2 assign to baggage4
    if (baggage4=="BG"){
        assign "1" to BgCount
        capture line:11, column:59, length:2 assign to Bg1
        capture line:12, column:59, length:2 assign to Bg2check
        if (Bg2check!="  "){
            assign "2" to BgCount
            capture line:12, column:59, length:2 assign to Bg2
            capture line:13, column:59, length:2 assign to Bg3check
            if (Bg3check!="  "){
                assign "3" to BgCount
                capture line:13, column:59, length:2 assign to Bg3
                capture line:14, column:59, length:2 assign to Bg4check
                if (Bg4check!="  "){
                    assign "4" to BgCount
                    capture line:14, column:59, length:2 assign to Bg4
                }
            }
        }
    }
    capture line:10, column:59, length:2 assign to baggage5
    if (baggage5=="BG"){
        assign "1" to BgCount
        capture line:12, column:59, length:2 assign to Bg1
        capture line:13, column:59, length:2 assign to Bg2check
        if (Bg2check!="  "){
            assign "2" to BgCount
            capture line:13, column:59, length:2 assign to Bg2
            capture line:14, column:59, length:2 assign to Bg3check
            if (Bg3check!="  "){
                assign "3" to BgCount
                capture line:14, column:59, length:2 assign to Bg3
                capture line:15, column:59, length:2 assign to Bg4check
                if (Bg4check!="  "){
                    assign "4" to BgCount
                    capture line:15, column:59, length:2 assign to Bg4
                }
            }
        }
    }

    capture line:12, column:1, length:3 assign to curr1
    capture line:12, column:13, length:3 assign to curr1XT
    capture line:13, column:1, length:3 assign to curr2
    capture line:13, column:13, length:3 assign to curr2XT
    capture line:14, column:1, length:3 assign to curr3
    capture line:14, column:13, length:3 assign to curr3XT
    capture line:15, column:1, length:3 assign to curr4
    capture line:15, column:13, length:3 assign to curr4XT
    capture line:16, column:1, length:3 assign to curr5
    capture line:16, column:13, length:3 assign to curr5XT
    capture line:17, column:1, length:3 assign to curr6
    capture line:17, column:13, length:3 assign to curr6XT
    capture line:18, column:1, length:3 assign to curr7
    capture line:18, column:13, length:3 assign to curr7XT
    capture line:19, column:1, length:3 assign to curr8
    capture line:19, column:13, length:3 assign to curr8XT
    capture line:20, column:1, length:3 assign to curr9
    capture line:20, column:13, length:3 assign to curr9XT
    capture line:21, column:1, length:3 assign to curr10    
    if (curr1XT=="-XT"){
            if (curr1==curr2){
                capture line:13, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr2XT =="-XT"){
            if (curr2==curr3){
                capture line:14, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr3XT=="-XT"){
            if (curr3==curr4){
                capture line:15, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr4XT=="-XT"){
            if (curr4==curr5){
                capture line:16, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr5XT=="-XT"){
            if (curr5==curr6){
                capture line:17, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr6XT=="-XT"){
            if (curr6==curr7){
                capture line:18, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr7XT=="-XT"){
            if (curr7==curr8){
                capture line:19, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr8XT=="-XT"){
            if (curr8==curr9){
                capture line:20, column:4, length:10 assign to FQQPrice
            }
    }
    if (curr9XT=="-XT"){
            if (curr9==curr10){
                capture line:21, column:4, length:10 assign to FQQPrice
            }
    }
                
    if (curr1XT!="-XT"){
        if (curr2XT!="-XT"){
            if (curr3XT!="-XT"){
                if (curr4XT!="-XT"){
                    if (curr5XT!="-XT"){
                        if (curr6XT!="-XT"){
                            if (curr7XT!="-XT"){
                                if (curr8XT!="-XT"){
                                    if (curr9XT!="-XT"){
                                            mandatory ask "Can you Enter the FQQ Price here:" assign to FQQPrice
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    
    if (BgCount=="1"){
        send "SRT" +FQQPrice +Bg1
    }
    if (BgCount=="2"){
        send "SRT" +FQQPrice +Bg1 +Bg2
    }
    if (BgCount=="3"){
        send "SRT" +FQQPrice +Bg1 +Bg2 +Bg3
    }
    if (BgCount=="4"){
        send "SRT" +FQQPrice +Bg1 +Bg2 +Bg3 +Bg4
    }
}
else{
  send " ERROR!"
  mandatory ask "Try again Please" assign to FQQPrice
}