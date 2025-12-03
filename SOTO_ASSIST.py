//SOTO_ASSIST

// Features:
// 1. Check for deal "On Original PNR"
// 2. Bulk Share "ES" OR "RP" 
// 3. Bulk Void

send "IG"
choose "What is needed?" {
    when ("Check for deal On Original PNR") {
        call "SOTO_DEAL_CHECKER"
    }        
    when ("Bulk Share ES OR RP (Max 50 PNRs)") {
        group{
            mandatory ask "How Many PNRs?" with format "^\d{1,3}$" assign to PNRNumber
            mandatory ask "Enter PNRs:" assign to PNRs
            ask "Share Command (ES or RP):
 ex. ESRUHAA2***-B, RP/RUHAA2218/ALL" with format "^(ES|es|RP|rp).*" assign to shareCommand
        }
        send "SRT" + PNRs


if (PNRNumber > "0"){
    capture line: 1, column: 32, length: 6 assign to PNR1
}
if (PNRNumber > "1"){
    capture line: 1, column: 39, length: 6 assign to PNR2
}

if (PNRNumber > "2"){
    capture line: 1, column: 46, length: 6 assign to PNR3
}

if (PNRNumber > "3"){
    capture line: 1, column: 53, length: 6 assign to PNR4
}

if (PNRNumber > "4"){
    capture line: 1, column: 60, length: 4 assign to PNR5p1
    capture line: 2, column:2, length:2 assign to PNR5p2
    append "" +PNR5p1 + "" + PNR5p2 to PNR5
}

if (PNRNumber > "5"){
    capture line:2, column:5, length: 6 assign to PNR6
}

if (PNRNumber > "6"){
    capture line:2, column:12, length: 6 assign to PNR7
}

if (PNRNumber > "7"){
    capture line:2, column:19, length: 6 assign to PNR8
}

if (PNRNumber > "8"){
    capture line:2, column:26, length: 6 assign to PNR9
}

if (PNRNumber > "9"){
    capture line:2, column:33, length: 6 assign to PNR10
}

if (PNRNumber > "10"){
    capture line:2, column:40, length: 6 assign to PNR11
}

if (PNRNumber > "11"){
    capture line:2, column:47, length: 6 assign to PNR12
}

if (PNRNumber > "12"){
    capture line:2, column:54, length: 6 assign to PNR13
}

if (PNRNumber > "13"){
    capture line:2, column:61, length: 3 assign to PNR14p1
    capture line:3, column:2, length:3 assign to PNR14p2
    append "" +PNR14p1 + "" + PNR14p2 to PNR14
}

if (PNRNumber > "14"){
    capture line:3, column:6, length: 6 assign to PNR15
}

if (PNRNumber > "15"){
    capture line:3, column:13, length: 6 assign to PNR16
}

if (PNRNumber > "16"){
    capture line:3, column:20, length: 6 assign to PNR17
}

if (PNRNumber > "17"){
    capture line:3, column:27, length: 6 assign to PNR18
}

if (PNRNumber > "18"){
    capture line:3, column:34, length: 6 assign to PNR19
}

if (PNRNumber > "19"){
    capture line:3, column:41, length: 6 assign to PNR20
}

if (PNRNumber > "20"){
    capture line:3, column:48, length: 6 assign to PNR21
}

if (PNRNumber > "21"){
    capture line:3, column:55, length: 6 assign to PNR22
}

if (PNRNumber > "22"){
    capture line:3, column:62, length: 2 assign to PNR23p1
    capture line:4, column:2, length:4 assign to PNR23p2
    append "" +PNR23p1 + "" + PNR23p2 to PNR23
}

if (PNRNumber > "23"){
    capture line:4, column:7, length: 6 assign to PNR24
}

if (PNRNumber > "24"){
    capture line:4, column:14, length: 6 assign to PNR25
}

if (PNRNumber > "25"){
    capture line:4, column:21, length: 6 assign to PNR26
}

if (PNRNumber > "26"){
    capture line:4, column:28, length: 6 assign to PNR27
}

if (PNRNumber > "27"){
    capture line:4, column:35, length: 6 assign to PNR28
}

if (PNRNumber > "28"){
    capture line:4, column:42, length: 6 assign to PNR29
}

if (PNRNumber > "29"){
    capture line:4, column:49, length: 6 assign to PNR30
}

if (PNRNumber > "30"){
    capture line:4, column:56, length: 6 assign to PNR31
}

if (PNRNumber > "31"){
    capture line:4, column:63, length: 1 assign to PNR32p1
    capture line:5, column:2, length:5 assign to PNR32p2
    append "" +PNR32p1 + "" + PNR32p2 to PNR32
}

if (PNRNumber > "32"){
    capture line:5, column:8, length: 6 assign to PNR33
}

if (PNRNumber > "33"){
    capture line:5, column:15, length: 6 assign to PNR34
}

if (PNRNumber > "34"){
    capture line:5, column:22, length: 6 assign to PNR35
}

if (PNRNumber > "35"){
    capture line:5, column:29, length: 6 assign to PNR36
}

if (PNRNumber > "36"){
    capture line:5, column:36, length: 6 assign to PNR37
}

if (PNRNumber > "37"){
    capture line:5, column:43, length: 6 assign to PNR38
}

if (PNRNumber > "38"){
    capture line:5, column:50, length: 6 assign to PNR39
}

if (PNRNumber > "39"){
    capture line:5, column:57, length: 6 assign to PNR40
}

if (PNRNumber > "40"){
    capture line:6, column:2, length: 6 assign to PNR41
}

if (PNRNumber > "41"){
    capture line:6, column:9, length: 6 assign to PNR42
}

if (PNRNumber > "42"){
    capture line:6, column:16, length: 6 assign to PNR43
}

if (PNRNumber > "43"){
    capture line:6, column:23, length: 6 assign to PNR44
}

if (PNRNumber > "44"){
    capture line:6, column:30, length: 6 assign to PNR45
}

if (PNRNumber > "45"){
    capture line:6, column:37, length: 6 assign to PNR46
}

if (PNRNumber > "46"){
    capture line:6, column:44, length: 6 assign to PNR47
}

if (PNRNumber > "47"){
    capture line:6, column:51, length: 6 assign to PNR48
}

if (PNRNumber > "48"){
    capture line:6, column:58, length: 6 assign to PNR49
}

if (PNRNumber > "49"){
    capture line:7, column:3, length: 6 assign to PNR50
}

/////////////////////////////////////////////////////////////////

if (PNRNumber > "0"){
    send "RT" + PNR1
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "1"){
    send "RT" + PNR2
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "2"){
    send "RT" + PNR3
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "3"){
    send "RT" + PNR4
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "4"){
    send "RT" + PNR5
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}
if (PNRNumber > "5"){
    send "RT" + PNR6
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "6"){
    send "RT" + PNR7
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "7"){
    send "RT" + PNR8
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "8"){
    send "RT" + PNR9
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "9"){
    send "RT" + PNR10
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "10"){
    send "RT" + PNR11
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "11"){
    send "RT" + PNR12
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "12"){
    send "RT" + PNR13
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}
if (PNRNumber > "13"){
    send "RT" + PNR14
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "14"){
    send "RT" + PNR15
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "15"){
    send "RT" + PNR16
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "16"){
    send "RT" + PNR17
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "17"){
    send "RT" + PNR18
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "18"){
    send "RT" + PNR19
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "19"){
    send "RT" + PNR20
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "20"){
    send "RT" + PNR21
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "21"){
    send "RT" + PNR22
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "22"){
    send "RT" + PNR23
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "23"){
    send "RT" + PNR24
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "24"){
    send "RT" + PNR25
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "25"){
    send "RT" + PNR26
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "26"){
    send "RT" + PNR27
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "27"){
    send "RT" + PNR28
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "28"){
    send "RT" + PNR29
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "29"){
    send "RT" + PNR30
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "30"){
    send "RT" + PNR31
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "31"){
    send "RT" + PNR32
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "32"){
    send "RT" + PNR33
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "33"){
    send "RT" + PNR34
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "34"){
    send "RT" + PNR35
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "35"){
    send "RT" + PNR36
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "36"){
    send "RT" + PNR37
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "37"){
    send "RT" + PNR38
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "38"){
    send "RT" + PNR39
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "39"){
    send "RT" + PNR40
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "40"){
    send "RT" + PNR41
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "41"){
    send "RT" + PNR42
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "42"){
    send "RT" + PNR43
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "43"){
    send "RT" + PNR44
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "44"){
    send "RT" + PNR45
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "45"){
    send "RT" + PNR46
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "46"){
    send "RT" + PNR47
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "47"){
    send "RT" + PNR48
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "48"){
    send "RT" + PNR49
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}

if (PNRNumber > "49"){
    send "RT" + PNR50
    send "IR"
    send shareCommand
    send "RFSF;ER"
    capture line:1, column:1, length:7 assign to check_Share_Success
    if (check_Share_Success != "INVALID"){
        send "ER"
        capture line:1, column:1, length:7 assign to check_Share_Success
        if (check_Share_Success != "SECURED"){
            ask "Done?" assign to qz5
        }
    }
    send "IG"
}


    }
    when ("Bulk Void (Max 50 PNRs)") {
           group{
            mandatory ask "How Many PNRs?" with format "^\d{1,3}$" assign to PNRNumber
            mandatory ask "Enter PNRs:" assign to PNRs
        }
        send "SRT" + PNRs


if (PNRNumber > "0"){
    capture line: 1, column: 32, length: 6 assign to PNR1
}
if (PNRNumber > "1"){
    capture line: 1, column: 39, length: 6 assign to PNR2
}

if (PNRNumber > "2"){
    capture line: 1, column: 46, length: 6 assign to PNR3
}

if (PNRNumber > "3"){
    capture line: 1, column: 53, length: 6 assign to PNR4
}

if (PNRNumber > "4"){
    capture line: 1, column: 60, length: 4 assign to PNR5p1
    capture line: 2, column:2, length:2 assign to PNR5p2
    append "" +PNR5p1 + "" + PNR5p2 to PNR5
}

if (PNRNumber > "5"){
    capture line:2, column:5, length: 6 assign to PNR6
}

if (PNRNumber > "6"){
    capture line:2, column:12, length: 6 assign to PNR7
}

if (PNRNumber > "7"){
    capture line:2, column:19, length: 6 assign to PNR8
}

if (PNRNumber > "8"){
    capture line:2, column:26, length: 6 assign to PNR9
}

if (PNRNumber > "9"){
    capture line:2, column:33, length: 6 assign to PNR10
}

if (PNRNumber > "10"){
    capture line:2, column:40, length: 6 assign to PNR11
}

if (PNRNumber > "11"){
    capture line:2, column:47, length: 6 assign to PNR12
}

if (PNRNumber > "12"){
    capture line:2, column:54, length: 6 assign to PNR13
}

if (PNRNumber > "13"){
    capture line:2, column:61, length: 3 assign to PNR14p1
    capture line:3, column:2, length:3 assign to PNR14p2
    append "" +PNR14p1 + "" + PNR14p2 to PNR14
}

if (PNRNumber > "14"){
    capture line:3, column:6, length: 6 assign to PNR15
}

if (PNRNumber > "15"){
    capture line:3, column:13, length: 6 assign to PNR16
}

if (PNRNumber > "16"){
    capture line:3, column:20, length: 6 assign to PNR17
}

if (PNRNumber > "17"){
    capture line:3, column:27, length: 6 assign to PNR18
}

if (PNRNumber > "18"){
    capture line:3, column:34, length: 6 assign to PNR19
}

if (PNRNumber > "19"){
    capture line:3, column:41, length: 6 assign to PNR20
}

if (PNRNumber > "20"){
    capture line:3, column:48, length: 6 assign to PNR21
}

if (PNRNumber > "21"){
    capture line:3, column:55, length: 6 assign to PNR22
}

if (PNRNumber > "22"){
    capture line:3, column:62, length: 2 assign to PNR23p1
    capture line:4, column:2, length:4 assign to PNR23p2
    append "" +PNR23p1 + "" + PNR23p2 to PNR23
}

if (PNRNumber > "23"){
    capture line:4, column:7, length: 6 assign to PNR24
}

if (PNRNumber > "24"){
    capture line:4, column:14, length: 6 assign to PNR25
}

if (PNRNumber > "25"){
    capture line:4, column:21, length: 6 assign to PNR26
}

if (PNRNumber > "26"){
    capture line:4, column:28, length: 6 assign to PNR27
}

if (PNRNumber > "27"){
    capture line:4, column:35, length: 6 assign to PNR28
}

if (PNRNumber > "28"){
    capture line:4, column:42, length: 6 assign to PNR29
}

if (PNRNumber > "29"){
    capture line:4, column:49, length: 6 assign to PNR30
}

if (PNRNumber > "30"){
    capture line:4, column:56, length: 6 assign to PNR31
}

if (PNRNumber > "31"){
    capture line:4, column:63, length: 1 assign to PNR32p1
    capture line:5, column:2, length:5 assign to PNR32p2
    append "" +PNR32p1 + "" + PNR32p2 to PNR32
}

if (PNRNumber > "32"){
    capture line:5, column:8, length: 6 assign to PNR33
}

if (PNRNumber > "33"){
    capture line:5, column:15, length: 6 assign to PNR34
}

if (PNRNumber > "34"){
    capture line:5, column:22, length: 6 assign to PNR35
}

if (PNRNumber > "35"){
    capture line:5, column:29, length: 6 assign to PNR36
}

if (PNRNumber > "36"){
    capture line:5, column:36, length: 6 assign to PNR37
}

if (PNRNumber > "37"){
    capture line:5, column:43, length: 6 assign to PNR38
}

if (PNRNumber > "38"){
    capture line:5, column:50, length: 6 assign to PNR39
}

if (PNRNumber > "39"){
    capture line:5, column:57, length: 6 assign to PNR40
}

if (PNRNumber > "40"){
    capture line:6, column:2, length: 6 assign to PNR41
}

if (PNRNumber > "41"){
    capture line:6, column:9, length: 6 assign to PNR42
}

if (PNRNumber > "42"){
    capture line:6, column:16, length: 6 assign to PNR43
}

if (PNRNumber > "43"){
    capture line:6, column:23, length: 6 assign to PNR44
}

if (PNRNumber > "44"){
    capture line:6, column:30, length: 6 assign to PNR45
}

if (PNRNumber > "45"){
    capture line:6, column:37, length: 6 assign to PNR46
}

if (PNRNumber > "46"){
    capture line:6, column:44, length: 6 assign to PNR47
}

if (PNRNumber > "47"){
    capture line:6, column:51, length: 6 assign to PNR48
}

if (PNRNumber > "48"){
    capture line:6, column:58, length: 6 assign to PNR49
}

if (PNRNumber > "49"){
    capture line:7, column:3, length: 6 assign to PNR50
}

/////////////////////////////////////////////////////////////////

if (PNRNumber > "0"){
    send "RT" + PNR1
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "1"){
    send "RT" + PNR2
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "2"){
    send "RT" + PNR3
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "3"){
    send "RT" + PNR4
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "4"){
    send "RT" + PNR5
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}
if (PNRNumber > "5"){
    send "RT" + PNR6
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "6"){
    send "RT" + PNR7
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "7"){
    send "RT" + PNR8
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "8"){
    send "RT" + PNR9
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "9"){
    send "RT" + PNR10
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "10"){
    send "RT" + PNR11
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "11"){
    send "RT" + PNR12
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "12"){
    send "RT" + PNR13
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}
if (PNRNumber > "13"){
    send "RT" + PNR14
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "14"){
    send "RT" + PNR15
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "15"){
    send "RT" + PNR16
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "16"){
    send "RT" + PNR17
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "17"){
    send "RT" + PNR18
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "18"){
    send "RT" + PNR19
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "19"){
    send "RT" + PNR20
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "20"){
    send "RT" + PNR21
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "21"){
    send "RT" + PNR22
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "22"){
    send "RT" + PNR23
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "23"){
    send "RT" + PNR24
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "24"){
    send "RT" + PNR25
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "25"){
    send "RT" + PNR26
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "26"){
    send "RT" + PNR27
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "27"){
    send "RT" + PNR28
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "28"){
    send "RT" + PNR29
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "29"){
    send "RT" + PNR30
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "30"){
    send "RT" + PNR31
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "31"){
    send "RT" + PNR32
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "32"){
    send "RT" + PNR33
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "33"){
    send "RT" + PNR34
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "34"){
    send "RT" + PNR35
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "35"){
    send "RT" + PNR36
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "36"){
    send "RT" + PNR37
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "37"){
    send "RT" + PNR38
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "38"){
    send "RT" + PNR39
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "39"){
    send "RT" + PNR40
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "40"){
    send "RT" + PNR41
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "41"){
    send "RT" + PNR42
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "42"){
    send "RT" + PNR43
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "43"){
    send "RT" + PNR44
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "44"){
    send "RT" + PNR45
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "45"){
    send "RT" + PNR46
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "46"){
    send "RT" + PNR47
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "47"){
    send "RT" + PNR48
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "48"){
    send "RT" + PNR49
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}

if (PNRNumber > "49"){
    send "RT" + PNR50
    send "RTTN"
    choose "Void?"{
        when ("Yes"){
            send "TRDC/ALL"
            ask "Done?" assign to done
        }
        when ("No"){
        }
    }
    send "IG"
}
    }
}


