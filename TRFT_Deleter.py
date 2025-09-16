//TRFT_Deleter
assign "" to tax1
assign "" to tax2
assign "" to tax3
assign "" to tax4
assign "" to tax5
assign "" to tax6
assign "" to tax7
assign "" to tax8
assign "" to tax9
assign "" to tax10
assign "" to tax11
assign "" to tax12
assign "" to tax13
assign "" to tax14
assign "" to tax15

// accepted: 2YQYRE3S4...etc
capture line:1, column:32, length:2 assign to tax_Count
if (tax_Count > "0 "){
    capture line:1, column:34, length:2 assign to tax1
}
if (tax_Count > "1 "){
    capture line:1, column:36, length:2 assign to tax2
}
if (tax_Count > "2 "){
    capture line:1, column:38, length:2 assign to tax3
}
if (tax_Count > "3 "){
    capture line:1, column:40, length:2 assign to tax4
}
if (tax_Count > "4 "){
    capture line:1, column:42, length:2 assign to tax5
}
if (tax_Count > "5 "){
    capture line:1, column:44, length:2 assign to tax6
}
if (tax_Count > "6 "){
    capture line:1, column:46, length:2 assign to tax7
}
if (tax_Count > "7 "){
    capture line:1, column:48, length:2 assign to tax8
}
if (tax_Count > "8 "){
    capture line:1, column:50, length:2 assign to tax9
}
if (tax_Count > "9 "){
    capture line:1, column:52, length:2 assign to tax10
}
if (tax_Count > "10"){
    capture line:1, column:54, length:2 assign to tax11
}
if (tax_Count > "11"){
    capture line:1, column:56, length:2 assign to tax12
}
if (tax_Count > "12"){
    capture line:1, column:58, length:2 assign to tax13
}
if (tax_Count > "13"){
    capture line:1, column:60, length:2 assign to tax14
}
if (tax_Count > "14"){
    capture line:1, column:62, length:2 assign to tax15
}




send "TRFT"

capture line:5, column:5, length:3 assign to tx_No
capture line:5, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:6, column:5, length:3 assign to tx_No
capture line:6, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:7, column:5, length:3 assign to tx_No
capture line:7, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:8, column:5, length:3 assign to tx_No
capture line:8, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:9, column:5, length:3 assign to tx_No
capture line:9, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:10, column:5, length:3 assign to tx_No
capture line:10, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:11, column:5, length:3 assign to tx_No
capture line:11, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:12, column:5, length:3 assign to tx_No
capture line:12, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:13, column:5, length:3 assign to tx_No
capture line:13, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:14, column:5, length:3 assign to tx_No
capture line:14, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
 capture line:15, column:4, length:3 assign to tx_No
capture line:15, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:16, column:4, length:3 assign to tx_No
capture line:16, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:17, column:4, length:3 assign to tx_No
capture line:17, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:18, column:4, length:3 assign to tx_No
capture line:18, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:19, column:4, length:3 assign to tx_No
capture line:19, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:20, column:4, length:3 assign to tx_No
capture line:20, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:21, column:4, length:3 assign to tx_No
capture line:21, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:22, column:4, length:3 assign to tx_No
capture line:22, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:23, column:4, length:3 assign to tx_No
capture line:23, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}

capture line:5, column:5, length:3 assign to tx_No
capture line:5, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:6, column:5, length:3 assign to tx_No
capture line:6, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:7, column:5, length:3 assign to tx_No
capture line:7, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:8, column:5, length:3 assign to tx_No
capture line:8, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:9, column:5, length:3 assign to tx_No
capture line:9, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:10, column:5, length:3 assign to tx_No
capture line:10, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:11, column:5, length:3 assign to tx_No
capture line:11, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:12, column:5, length:3 assign to tx_No
capture line:12, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:13, column:5, length:3 assign to tx_No
capture line:13, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:14, column:5, length:3 assign to tx_No
capture line:14, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:15, column:4, length:3 assign to tx_No
capture line:15, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:16, column:4, length:3 assign to tx_No
capture line:16, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:17, column:4, length:3 assign to tx_No
capture line:17, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:18, column:4, length:3 assign to tx_No
capture line:18, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:19, column:4, length:3 assign to tx_No
capture line:19, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:20, column:4, length:3 assign to tx_No
capture line:20, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:21, column:4, length:3 assign to tx_No
capture line:21, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:22, column:4, length:3 assign to tx_No
capture line:22, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:23, column:4, length:3 assign to tx_No
capture line:23, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}

capture line:5, column:5, length:3 assign to tx_No
capture line:5, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:6, column:5, length:3 assign to tx_No
capture line:6, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:7, column:5, length:3 assign to tx_No
capture line:7, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:8, column:5, length:3 assign to tx_No
capture line:8, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:9, column:5, length:3 assign to tx_No
capture line:9, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:10, column:5, length:3 assign to tx_No
capture line:10, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:11, column:5, length:3 assign to tx_No
capture line:11, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:12, column:5, length:3 assign to tx_No
capture line:12, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:13, column:5, length:3 assign to tx_No
capture line:13, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:14, column:5, length:3 assign to tx_No
capture line:14, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:15, column:4, length:3 assign to tx_No
capture line:15, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:16, column:4, length:3 assign to tx_No
capture line:16, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:17, column:4, length:3 assign to tx_No
capture line:17, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:18, column:4, length:3 assign to tx_No
capture line:18, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:19, column:4, length:3 assign to tx_No
capture line:19, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:20, column:4, length:3 assign to tx_No
capture line:20, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:21, column:4, length:3 assign to tx_No
capture line:21, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:22, column:4, length:3 assign to tx_No
capture line:22, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:23, column:4, length:3 assign to tx_No
capture line:23, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}

capture line:5, column:5, length:3 assign to tx_No
capture line:5, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:6, column:5, length:3 assign to tx_No
capture line:6, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:7, column:5, length:3 assign to tx_No
capture line:7, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:8, column:5, length:3 assign to tx_No
capture line:8, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:9, column:5, length:3 assign to tx_No
capture line:9, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:10, column:5, length:3 assign to tx_No
capture line:10, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:11, column:5, length:3 assign to tx_No
capture line:11, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:12, column:5, length:3 assign to tx_No
capture line:12, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:13, column:5, length:3 assign to tx_No
capture line:13, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:14, column:5, length:3 assign to tx_No
capture line:14, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:15, column:4, length:3 assign to tx_No
capture line:15, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:16, column:4, length:3 assign to tx_No
capture line:16, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:17, column:4, length:3 assign to tx_No
capture line:17, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:18, column:4, length:3 assign to tx_No
capture line:18, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:19, column:4, length:3 assign to tx_No
capture line:19, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:20, column:4, length:3 assign to tx_No
capture line:20, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:21, column:4, length:3 assign to tx_No
capture line:21, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:22, column:4, length:3 assign to tx_No
capture line:22, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}
capture line:23, column:4, length:3 assign to tx_No

capture line:23, column:20, length:2 assign to tx_name
if (tx_name != ""){
if (tx_name == tax1){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax2){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax3){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax4){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax5){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax6){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax7){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax8){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax9){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax10){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax11){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax12){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax13){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax14){
    send "TRFu/TX" +tx_No
}
if (tx_name == tax15){
    send "TRFu/TX" +tx_No
}
}