//Tax_Refund_Update

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
send "TRFU/RM Applied Tax refund"
send  "TRFT"
send "TRFU/TX"
