ask "What is the route?" asisgn to route1
send "SRT" + route1
capture line:1, column:32, length:3 assign to city1
capture line:1, column:38, length:3 assign to city2
capture line:1, column:42, length:2 assign to airline

capture line:1, column:48, length:1 assign to Dcheck1
capture line:1, column:49, length:1 assign to Dcheck2
capture line:1, column:50, length:1 assign to Dcheck3

if (Dcheck1 =="D"){
    capture line:1, column:45, length:2 assign to flightNo
    capture line:1, column:58, length:2 assign to day
    capture line:1, column:61, length:2 assign to month
    capture line:2, column:4, length:2 assign to year

}
if (Dcheck2 =="D"){
    capture line:1, column:45, length:3 assign to flightNo
    capture line:1, column:59, length:2 assign to day
    capture line:1, column:62, length:2 assign to month
    capture line:2, column:5, length:2 assign to year

}
if (Dcheck3 =="D"){
    capture line:1, column:45, length:4 assign to flightNo
    capture line:1, column:60, length:2 assign to day
    capture line:1, column:63, length:1 assign to month1
    capture line:2, column:2, length:1 assign to month2
    append month1 + month2 to month
    capture line:2, column:6, length:2 assign to year

}

ask "what's the class of the route?" assign to class

if (month=="01"){
    assign "JAN" to month
}

if (month=="02"){
    assign "FEB" to month
}

if (month=="03"){
    assign "MAR" to month
}

if (month=="04"){
    assign "APR" to month
}

if (month=="05"){
    assign "MAY" to month
}

if (month=="06"){
    assign "JUN" to month
}

if (month=="07"){
    assign "JUL" to month
}

if (month=="08"){
    assign "AUG" to month
}

if (month=="09"){
    assign "SEP" to month
}

if (month=="10"){
    assign "OCT" to month
}

if (month=="11"){
    assign "NOV" to month
}

if (month=="12"){
    assign "DEC" to month
}

send "SS" + airline + flightNo +" " + class + " " + day + month + year +" " + city1 + city2 + "GK1/relcoc"