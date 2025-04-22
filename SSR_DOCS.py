send "RTA"

capture line:2, column:30, length:2 assign to HK1Test
if (HK1Test=="HK"){
  capture line:2, column:6, length:2 assign to Airline
}
else{
capture line:3, column:30, length:2 assign to HK2Test
if (HK2Test=="HK"){
  capture line:3, column:6, length:2 assign to Airline
}
else{
  send "Not Confirmed Segemnts please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
}
}

send "RT"
group{
mandatory ask "ENTER THE PAX No:" assign to paxNO
mandatory ask "ENTER THE PAX Name:" assign to paxNAME
select "ENTER THE PAX INFO Type:" from "P,I" assign to passType
ask "ENTER THE PAX Passport NO:" assign to paxPassbort
ask "ENTER THE PAX Passport Expiry Date:" assign to paxPassExpiry
select "ENTER THE PAX Gender:" from "M,F" assign to gender
ask "ENTER THE PAX Passport Nasionalty:" assign to paxPassNasjonalty
ask "ENTER THE PAX DOB:" assign to paxDOB
}

send "SRT" +paxPassExpiry
capture line:1, column:32, length:2 assign to paxPassExpiryDay
capture line:1, column:35, length:2 assign to paxPassExpiryMonth
capture line:1, column:40, length:2 assign to paxPassExpiryYear

if (paxPassExpiryMonth=="01"){
    assign "JAN" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="02"){
    assign "FEB" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="03"){
    assign "MAR" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="04"){
    assign "APR" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="05"){
    assign "MAY" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="06"){
    assign "JUN" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="07"){
    assign "JUL" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="08"){
    assign "AUG" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="09"){
    assign "SEP" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="10"){
    assign "OCT" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="11"){
    assign "NOV" to paxPassExpiryMonth
}
if (paxPassExpiryMonth=="12"){
    assign "DEC" to paxPassExpiryMonth
}

send "SRT" +paxDOB
capture line:1, column:32, length:2 assign to paxDOBDay
capture line:1, column:35, length:2 assign to paxDOBMonth
capture line:1, column:40, length:2 assign to paxDOBYear
if (paxDOBMonth=="01"){
    assign "JAN" to paxDOBMonth
}
if (paxDOBMonth=="02"){
    assign "FEB" to paxDOBMonth
}
if (paxDOBMonth=="03"){
    assign "MAR" to paxDOBMonth
}
if (paxDOBMonth=="04"){
    assign "APR" to paxDOBMonth
}
if (paxDOBMonth=="05"){
    assign "MAY" to paxDOBMonth
}
if (paxDOBMonth=="06"){
    assign "JUN" to paxDOBMonth
}
if (paxDOBMonth=="07"){
    assign "JUL" to paxDOBMonth
}
if (paxDOBMonth=="08"){
    assign "AUG" to paxDOBMonth
}
if (paxDOBMonth=="09"){
    assign "SEP" to paxDOBMonth
}
if (paxDOBMonth=="10"){
    assign "OCT" to paxDOBMonth
}
if (paxDOBMonth=="11"){
    assign "NOV" to paxDOBMonth
}
if (paxDOBMonth=="12"){
    assign "DEC" to paxDOBMonth
}

send "SRDOCS " +Airline + "HK1 -"  passType+ +"/" +paxPassNasjonalty +"/" +paxPassbort
  +"/" +paxPassNasjonalty +"/" +paxDOBDay +paxDOBMonth +paxDOBYear +"/" +gender
  +"/" +paxPassExpiryDay +paxPassExpiryMonth +paxPassExpiryYear +"/" +paxNAME +"/P" +paxNO



