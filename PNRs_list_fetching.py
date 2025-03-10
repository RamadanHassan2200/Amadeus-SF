mandatory ask number "How many PNRS?" assign to PNRNumber

mandatory ask "Enter the PNRs and separate with (one space only)" assign to PNRS
send "SRT" + PNRS

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