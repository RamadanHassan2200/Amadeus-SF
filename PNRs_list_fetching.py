//PNRs_list_fetching

capture line: 1, column: 33, length: 1 assign to check1dash
capture line: 1, column: 34, length: 1 assign to check2dash
capture line: 1, column: 35, length: 1 assign to check3dash

if (check1dash=="-"){
    capture line: 1, column: 32, length: 1 assign to PNRNumber
    capture line: 1, column: 34, length: 30 assign to srtp1
}
if (check2dash=="-"){
    capture line: 1, column: 32, length: 2 assign to PNRNumber
    capture line: 1, column: 35, length: 29 assign to srtp1
}

if (check3dash=="-"){
    capture line: 1, column: 32, length: 3 assign to PNRNumber
    capture line: 1, column: 36, length: 28 assign to srtp1
}
capture line: 2, column: 2, length: 62 assign to srtp2
capture line: 3, column: 2, length: 62 assign to srtp3
capture line: 4, column: 2, length: 62 assign to srtp4
capture line: 5, column: 2, length: 62 assign to srtp5
capture line: 6, column: 2, length: 62 assign to srtp6
capture line: 7, column: 2, length: 62 assign to srtp7
capture line: 8, column: 2, length: 62 assign to srtp8
capture line: 9, column: 2, length: 62 assign to srtp9
capture line: 10, column: 2, length: 62 assign to srtp10
capture line: 11, column: 2, length: 62 assign to srtp11
capture line: 12, column: 2, length: 62 assign to srtp12
capture line: 13, column: 2, length: 62 assign to srtp13
capture line: 14, column: 2, length: 62 assign to srtp14
capture line: 15, column: 2, length: 62 assign to srtp15
capture line: 16, column: 2, length: 62 assign to srtp16
capture line: 17, column: 2, length: 62 assign to srtp17
capture line: 18, column: 2, length: 62 assign to srtp18
capture line: 19, column: 2, length: 62 assign to srtp19
capture line: 20, column: 2, length: 62 assign to srtp20
capture line: 21, column: 2, length: 62 assign to srtp21
capture line: 22, column: 2, length: 62 assign to srtp22
capture line: 23, column: 2, length: 62 assign to srtp23

send "SRT" + srtp1 + srtp2 + srtp3 + srtp4 + srtp5 + srtp6 + srtp7 + srtp8 + srtp9 + srtp10 
+ srtp11 + srtp12 + srtp13 + srtp14 + srtp15 + srtp16 + srtp17 + srtp18 + srtp19 + srtp20  
+ srtp21 + srtp22 + srtp23

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

if (PNRNumber > "50"){
    capture line:7, column:10, length: 6 assign to PNR51
}

if (PNRNumber > "51"){
    capture line:7, column:17, length: 6 assign to PNR52
}

if (PNRNumber > "52"){
    capture line:7, column:24, length: 6 assign to PNR53
}

if (PNRNumber > "53"){
    capture line:7, column:31, length: 6 assign to PNR54
}

if (PNRNumber > "54"){
    capture line:7, column:38, length: 6 assign to PNR55
}

if (PNRNumber > "55"){
    capture line:7, column:45, length: 6 assign to PNR56
}

if (PNRNumber > "56"){
    capture line:7, column:52, length: 6 assign to PNR57
}

if (PNRNumber > "57"){
    capture line:7, column:59, length: 5 assign to PNR58p1
    capture line:8, column:2, length:1 assign to PNR58p2
    append "" +PNR58p1 + "" + PNR58p2 to PNR58
}

if (PNRNumber > "58"){
    capture line:8, column:4, length: 6 assign to PNR59
}

if (PNRNumber > "59"){
    capture line:8, column:11, length: 6 assign to PNR60
}

if (PNRNumber > "60"){
    capture line:8, column:18, length: 6 assign to PNR61
}

if (PNRNumber > "61"){
    capture line:8, column:25, length: 6 assign to PNR62
}

if (PNRNumber > "62"){
    capture line:8, column:32, length: 6 assign to PNR63
}

if (PNRNumber > "63"){
    capture line:8, column:39, length: 6 assign to PNR64
}

if (PNRNumber > "64"){
    capture line:8, column:46, length: 6 assign to PNR65
}

if (PNRNumber > "65"){
    capture line:8, column:53, length: 6 assign to PNR66
}

if (PNRNumber > "66"){
    capture line:8, column:60, length: 4 assign to PNR67p1
    capture line:9, column:2, length:2 assign to PNR67p2
    append "" + PNR67p1 + "" + PNR67p2 to PNR67
}

if (PNRNumber > "67"){
    capture line:9, column:5, length: 6 assign to PNR68
}

if (PNRNumber > "68"){
    capture line:9, column:12, length: 6 assign to PNR69
}

if (PNRNumber > "69"){
    capture line:9, column:19, length: 6 assign to PNR70
}

if (PNRNumber > "70"){
    capture line:9, column:26, length: 6 assign to PNR71
}

if (PNRNumber > "71"){
    capture line:9, column:33, length: 6 assign to PNR72
}

if (PNRNumber > "72"){
    capture line:9, column:40, length: 6 assign to PNR73
}

if (PNRNumber > "73"){
    capture line:9, column:47, length: 6 assign to PNR74
}

if (PNRNumber > "74"){
    capture line:9, column:54, length: 6 assign to PNR75
}

if (PNRNumber > "75"){
    capture line:9, column:61, length: 3 assign to PNR76p1
    capture line:10, column:2, length:3 assign to PNR76p2
    append "" + PNR76p1 + "" + PNR76p2 to PNR76
}

if (PNRNumber > "76"){
    capture line:10, column:6, length: 6 assign to PNR77
}

if (PNRNumber > "77"){
    capture line:10, column:13, length: 6 assign to PNR78
}

if (PNRNumber > "78"){
    capture line:10, column:20, length: 6 assign to PNR79
}

if (PNRNumber > "79"){
    capture line:10, column:27, length: 6 assign to PNR80
}

if (PNRNumber > "80"){
    capture line:10, column:34, length: 6 assign to PNR81
}

if (PNRNumber > "81"){
    capture line:10, column:41, length: 6 assign to PNR82
}

if (PNRNumber > "82"){
    capture line:10, column:48, length: 6 assign to PNR83
}

if (PNRNumber > "83"){
    capture line:10, column:55, length: 6 assign to PNR84
}

if (PNRNumber > "84"){
    capture line:10, column:62, length: 2 assign to PNR85p1
    capture line:11, column:2, length:4 assign to PNR85p2
    append "" + PNR85p1 + "" + PNR85p2 to PNR85
}

if (PNRNumber > "85"){
    capture line:11, column:7, length: 6 assign to PNR86
}

if (PNRNumber > "86"){
    capture line:11, column:14, length: 6 assign to PNR87
}

if (PNRNumber > "87"){
    capture line:11, column:21, length: 6 assign to PNR88
}

if (PNRNumber > "88"){
    capture line:11, column:28, length: 6 assign to PNR89
}

if (PNRNumber > "89"){
    capture line:11, column:35, length: 6 assign to PNR90
}

if (PNRNumber > "90"){
    capture line:11, column:42, length: 6 assign to PNR91
}

if (PNRNumber > "91"){
    capture line:11, column:49, length: 6 assign to PNR92
}

if (PNRNumber > "92"){
    capture line:11, column:56, length: 6 assign to PNR93
}

if (PNRNumber > "93"){
    capture line:11, column:63, length: 1 assign to PNR94p1
    capture line:12, column:2, length:5 assign to PNR94p2
    append "" + PNR94p1 + "" + PNR94p2 to PNR94
}

if (PNRNumber > "94"){
    capture line:12, column:8, length: 6 assign to PNR95
}

if (PNRNumber > "95"){
    capture line:12, column:15, length: 6 assign to PNR96
}

if (PNRNumber > "96"){
    capture line:12, column:22, length: 6 assign to PNR97
}

if (PNRNumber > "97"){
    capture line:12, column:29, length: 6 assign to PNR98
}

if (PNRNumber > "98"){
    capture line:12, column:36, length: 6 assign to PNR99
}

if (PNRNumber > "99"){
    capture line:12, column:43, length: 6 assign to PNR100
}

if (PNRNumber > "100"){
    capture line:12, column:50, length: 6 assign to PNR101
}

if (PNRNumber > "101"){
    capture line:12, column:57, length: 6 assign to PNR102
}

if (PNRNumber > "102"){
    capture line:13, column:2, length: 6 assign to PNR103
}

if (PNRNumber > "103"){
    capture line:13, column:9, length: 6 assign to PNR104
}

if (PNRNumber > "104"){
    capture line:13, column:16, length: 6 assign to PNR105
}

if (PNRNumber > "105"){
    capture line:13, column:23, length: 6 assign to PNR106
}

if (PNRNumber > "106"){
    capture line:13, column:30, length: 6 assign to PNR107
}

if (PNRNumber > "107"){
    capture line:13, column:37, length: 6 assign to PNR108
}

if (PNRNumber > "108"){
    capture line:13, column:44, length: 6 assign to PNR109
}

if (PNRNumber > "109"){
    capture line:13, column:51, length: 6 assign to PNR110
}

if (PNRNumber > "110"){
    capture line:13, column:58, length: 6 assign to PNR111
}

if (PNRNumber > "111"){
    capture line:14, column:3, length: 6 assign to PNR112
}

if (PNRNumber > "112"){
    capture line:14, column:10, length: 6 assign to PNR113
}

if (PNRNumber > "113"){
    capture line:14, column:17, length: 6 assign to PNR114
}

if (PNRNumber > "114"){
    capture line:14, column:24, length: 6 assign to PNR115
}

if (PNRNumber > "115"){
    capture line:14, column:31, length: 6 assign to PNR116
}

if (PNRNumber > "116"){
    capture line:14, column:38, length: 6 assign to PNR117
}

if (PNRNumber > "117"){
    capture line:14, column:45, length: 6 assign to PNR118
}

if (PNRNumber > "118"){
    capture line:14, column:52, length: 6 assign to PNR119
}

if (PNRNumber > "119"){
    capture line:14, column:59, length: 5 assign to PNR120p1
    capture line:15, column:2, length:1 assign to PNR120p2
    append "" + PNR120p1 + "" + PNR120p2 to PNR120
}

if (PNRNumber > "120"){
    capture line:15, column:4, length: 6 assign to PNR121
}

if (PNRNumber > "121"){
    capture line:15, column:11, length: 6 assign to PNR122
}

if (PNRNumber > "122"){
    capture line:15, column:18, length: 6 assign to PNR123
}

if (PNRNumber > "123"){
    capture line:15, column:25, length: 6 assign to PNR124
}

if (PNRNumber > "124"){
    capture line:15, column:32, length: 6 assign to PNR125
}

if (PNRNumber > "125"){
    capture line:15, column:39, length: 6 assign to PNR126
}

if (PNRNumber > "126"){
    capture line:15, column:46, length: 6 assign to PNR127
}

if (PNRNumber > "127"){
    capture line:15, column:53, length: 6 assign to PNR128
}

if (PNRNumber > "128"){
    capture line:15, column:60, length: 4 assign to PNR129p1
    capture line:16, column:2, length:2 assign to PNR129p2
    append "" + PNR129p1 + "" + PNR129p2 to PNR129
}

if (PNRNumber > "129"){
    capture line:16, column:5, length: 6 assign to PNR130
}

if (PNRNumber > "130"){
    capture line:16, column:12, length: 6 assign to PNR131
}

if (PNRNumber > "131"){
    capture line:16, column:19, length: 6 assign to PNR132
}

if (PNRNumber > "132"){
    capture line:16, column:26, length: 6 assign to PNR133
}

if (PNRNumber > "133"){
    capture line:16, column:33, length: 6 assign to PNR134
}

if (PNRNumber > "134"){
    capture line:16, column:40, length: 6 assign to PNR135
}

if (PNRNumber > "135"){
    capture line:16, column:47, length: 6 assign to PNR136
}

if (PNRNumber > "136"){
    capture line:16, column:54, length: 6 assign to PNR137
}

if (PNRNumber > "137"){
    capture line:16, column:61, length: 3 assign to PNR138p1
    capture line:17, column:2, length:3 assign to PNR138p2
    append "" + PNR138p1 + "" + PNR138p2 to PNR138
}

if (PNRNumber > "138"){
    capture line:17, column:6, length: 6 assign to PNR139
}

if (PNRNumber > "139"){
    capture line:17, column:13, length: 6 assign to PNR140
}

if (PNRNumber > "140"){
    capture line:17, column:20, length: 6 assign to PNR141
}

if (PNRNumber > "141"){
    capture line:17, column:27, length: 6 assign to PNR142
}

if (PNRNumber > "142"){
    capture line:17, column:34, length: 6 assign to PNR143
}

if (PNRNumber > "143"){
    capture line:17, column:41, length: 6 assign to PNR144
}

if (PNRNumber > "144"){
    capture line:17, column:48, length: 6 assign to PNR145
}

if (PNRNumber > "145"){
    capture line:17, column:55, length: 6 assign to PNR146
}

if (PNRNumber > "146"){
    capture line:17, column:62, length: 2 assign to PNR147p1
    capture line:18, column:2, length:4 assign to PNR147p2
    append "" + PNR147p1 + "" + PNR147p2 to PNR147
}

if (PNRNumber > "147"){
    capture line:18, column:7, length: 6 assign to PNR148
}

if (PNRNumber > "148"){
    capture line:18, column:14, length: 6 assign to PNR149
}

if (PNRNumber > "149"){
    capture line:18, column:21, length: 6 assign to PNR150
}

if (PNRNumber > "150"){
    capture line:18, column:28, length: 6 assign to PNR151
}

if (PNRNumber > "151"){
    capture line:18, column:35, length: 6 assign to PNR152
}

if (PNRNumber > "152"){
    capture line:18, column:42, length: 6 assign to PNR153
}

if (PNRNumber > "153"){
    capture line:18, column:49, length: 6 assign to PNR154
}

if (PNRNumber > "154"){
    capture line:18, column:56, length: 6 assign to PNR155
}

if (PNRNumber > "155"){
    capture line:18, column:63, length: 1 assign to PNR156p1
    capture line:19, column:2, length:5 assign to PNR156p2
    append "" + PNR156p1 + "" + PNR156p2 to PNR156
}

if (PNRNumber > "156"){
    capture line:19, column:8, length: 6 assign to PNR157
}

if (PNRNumber > "157"){
    capture line:19, column:15, length: 6 assign to PNR158
}

if (PNRNumber > "158"){
    capture line:19, column:22, length: 6 assign to PNR159
}

if (PNRNumber > "159"){
    capture line:19, column:29, length: 6 assign to PNR160
}

if (PNRNumber > "160"){
    capture line:19, column:36, length: 6 assign to PNR161
}

if (PNRNumber > "161"){
    capture line:19, column:43, length: 6 assign to PNR162
}

if (PNRNumber > "162"){
    capture line:19, column:50, length: 6 assign to PNR163
}

if (PNRNumber > "163"){
    capture line:19, column:57, length: 6 assign to PNR164
}

if (PNRNumber > "164"){
    capture line:20, column:2, length: 6 assign to PNR165
}

if (PNRNumber > "165"){
    capture line:20, column:9, length: 6 assign to PNR166
}

if (PNRNumber > "166"){
    capture line:20, column:16, length: 6 assign to PNR167
}

if (PNRNumber > "167"){
    capture line:20, column:23, length: 6 assign to PNR168
}

if (PNRNumber > "168"){
    capture line:20, column:30, length: 6 assign to PNR169
}

if (PNRNumber > "169"){
    capture line:20, column:37, length: 6 assign to PNR170
}

if (PNRNumber > "170"){
    capture line:20, column:44, length: 6 assign to PNR171
}

if (PNRNumber > "171"){
    capture line:20, column:51, length: 6 assign to PNR172
}

if (PNRNumber > "172"){
    capture line:20, column:58, length: 6 assign to PNR173
}

if (PNRNumber > "173"){
    capture line:21, column:3, length: 6 assign to PNR174
}

if (PNRNumber > "174"){
    capture line:21, column:10, length: 6 assign to PNR175
}

if (PNRNumber > "175"){
    capture line:21, column:17, length: 6 assign to PNR176
}

if (PNRNumber > "176"){
    capture line:21, column:24, length: 6 assign to PNR177
}

if (PNRNumber > "177"){
    capture line:21, column:31, length: 6 assign to PNR178
}

if (PNRNumber > "178"){
    capture line:21, column:38, length: 6 assign to PNR179
}

if (PNRNumber > "179"){
    capture line:21, column:45, length: 6 assign to PNR180
}

if (PNRNumber > "180"){
    capture line:21, column:52, length: 6 assign to PNR181
}

if (PNRNumber > "181"){
    capture line:21, column:59, length: 5 assign to PNR182p1
    capture line:22, column:2, length:1 assign to PNR182p2
    append "" + PNR182p1 + "" + PNR182p2 to PNR182
}

if (PNRNumber > "182"){
    capture line:22, column:4, length: 6 assign to PNR183
}

if (PNRNumber > "183"){
    capture line:22, column:11, length: 6 assign to PNR184
}

if (PNRNumber > "184"){
    capture line:22, column:18, length: 6 assign to PNR185
}

if (PNRNumber > "185"){
    capture line:22, column:25, length: 6 assign to PNR186
}

if (PNRNumber > "186"){
    capture line:22, column:32, length: 6 assign to PNR187
}

if (PNRNumber > "187"){
    capture line:22, column:39, length: 6 assign to PNR188
}

if (PNRNumber > "188"){
    capture line:22, column:46, length: 6 assign to PNR189
}

if (PNRNumber > "189"){
    capture line:22, column:53, length: 6 assign to PNR190
}

if (PNRNumber > "190"){
    capture line:22, column:60, length: 4 assign to PNR191p1
    capture line:23, column:2, length:2 assign to PNR191p2
    append "" + PNR191p1 + "" + PNR191p2 to PNR191
}

if (PNRNumber > "191"){
    capture line:23, column:5, length: 6 assign to PNR192
}

if (PNRNumber > "192"){
    capture line:23, column:12, length: 6 assign to PNR193
}

if (PNRNumber > "193"){
    capture line:23, column:19, length: 6 assign to PNR194
}

if (PNRNumber > "194"){
    capture line:23, column:26, length: 6 assign to PNR195
}

if (PNRNumber > "195"){
    capture line:23, column:33, length: 6 assign to PNR196
}

if (PNRNumber > "196"){
    capture line:23, column:40, length: 6 assign to PNR197
}

if (PNRNumber > "197"){
    capture line:23, column:47, length: 6 assign to PNR198
}

if (PNRNumber > "198"){
    capture line:23, column:54, length: 6 assign to PNR199
}

/////////////////////////////////////////////////////////////////

assign "" to PNRs_List
if (PNRNumber > "0"){
    send "RT" + PNR1
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR1 + ", " to PNRs_List
    }
}

if (PNRNumber > "1"){
    send "RT" + PNR2
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR2 + ", " to PNRs_List
    }
}

if (PNRNumber > "2"){
    send "RT" + PNR3
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR3 + ", " to PNRs_List
    }
}

if (PNRNumber > "3"){
    send "RT" + PNR4
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR4 + ", " to PNRs_List
    }
}

if (PNRNumber > "4"){
    send "RT" + PNR5
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR5 + ", " to PNRs_List
    }
}
if (PNRNumber > "5"){
    send "RT" + PNR6
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR6 + ", " to PNRs_List
    }
}

if (PNRNumber > "6"){
    send "RT" + PNR7
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR7 + ", " to PNRs_List
    }
}

if (PNRNumber > "7"){
    send "RT" + PNR8
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR8 + ", " to PNRs_List
    }
}

if (PNRNumber > "8"){
    send "RT" + PNR9
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR9 + ", " to PNRs_List
    }
}

if (PNRNumber > "9"){
    send "RT" + PNR10
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR10 + ", " to PNRs_List
    }
}

if (PNRNumber > "10"){
    send "RT" + PNR11
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR11 + ", " to PNRs_List
    }
}

if (PNRNumber > "11"){
    send "RT" + PNR12
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR12 + ", " to PNRs_List
    }
}

if (PNRNumber > "12"){
    send "RT" + PNR13
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR13 + ", " to PNRs_List
    }
}
if (PNRNumber > "13"){
    send "RT" + PNR14
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR14 + ", " to PNRs_List
    }
}

if (PNRNumber > "14"){
    send "RT" + PNR15
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR15 + ", " to PNRs_List
    }
}

if (PNRNumber > "15"){
    send "RT" + PNR16
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR16 + ", " to PNRs_List
    }
}

if (PNRNumber > "16"){
    send "RT" + PNR17
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR17 + ", " to PNRs_List
    }
}

if (PNRNumber > "17"){
    send "RT" + PNR18
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR18 + ", " to PNRs_List
    }
}

if (PNRNumber > "18"){
    send "RT" + PNR19
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR19 + ", " to PNRs_List
    }
}

if (PNRNumber > "19"){
    send "RT" + PNR20
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR20 + ", " to PNRs_List
    }
}

if (PNRNumber > "20"){
    send "RT" + PNR21
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR21 + ", " to PNRs_List
    }
}

if (PNRNumber > "21"){
    send "RT" + PNR22
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR22 + ", " to PNRs_List
    }
}

if (PNRNumber > "22"){
    send "RT" + PNR23
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR23 + ", " to PNRs_List
    }
}

if (PNRNumber > "23"){
    send "RT" + PNR24
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR24 + ", " to PNRs_List
    }
}

if (PNRNumber > "24"){
    send "RT" + PNR25
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR25 + ", " to PNRs_List
    }
}

if (PNRNumber > "25"){
    send "RT" + PNR26
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR26 + ", " to PNRs_List
    }
}

if (PNRNumber > "26"){
    send "RT" + PNR27
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR27 + ", " to PNRs_List
    }
}

if (PNRNumber > "27"){
    send "RT" + PNR28
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR28 + ", " to PNRs_List
    }
}

if (PNRNumber > "28"){
    send "RT" + PNR29
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR29 + ", " to PNRs_List
    }
}

if (PNRNumber > "29"){
    send "RT" + PNR30
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR30 + ", " to PNRs_List
    }
}

if (PNRNumber > "30"){
    send "RT" + PNR31
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR31 + ", " to PNRs_List
    }

}

if (PNRNumber > "31"){
    send "RT" + PNR32
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR32 + ", " to PNRs_List
    }
}

if (PNRNumber > "32"){
    send "RT" + PNR33
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR33 + ", " to PNRs_List
    }
}

if (PNRNumber > "33"){
    send "RT" + PNR34
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR34 + ", " to PNRs_List
    }
}

if (PNRNumber > "34"){
    send "RT" + PNR35
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR35 + ", " to PNRs_List
    }
}

if (PNRNumber > "35"){
    send "RT" + PNR36
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR36 + ", " to PNRs_List
    }
}

if (PNRNumber > "36"){
    send "RT" + PNR37
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR37 + ", " to PNRs_List
    }
}

if (PNRNumber > "37"){
    send "RT" + PNR38
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR38 + ", " to PNRs_List
    }
}

if (PNRNumber > "38"){
    send "RT" + PNR39
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR39 + ", " to PNRs_List
    }
}

if (PNRNumber > "39"){
    send "RT" + PNR40
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR40 + ", " to PNRs_List
    }
}

if (PNRNumber > "40"){
    send "RT" + PNR41
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR41 + ", " to PNRs_List
    }
}

if (PNRNumber > "41"){
    send "RT" + PNR42
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR42 + ", " to PNRs_List
    }
}

if (PNRNumber > "42"){
    send "RT" + PNR43
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR43 + ", " to PNRs_List
    }
}

if (PNRNumber > "43"){
    send "RT" + PNR44
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR44 + ", " to PNRs_List
    }
}

if (PNRNumber > "44"){
    send "RT" + PNR45
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR45 + ", " to PNRs_List
    }
}

if (PNRNumber > "45"){
    send "RT" + PNR46
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR46 + ", " to PNRs_List
    }
}

if (PNRNumber > "46"){
    send "RT" + PNR47
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR47 + ", " to PNRs_List
    }
}

if (PNRNumber > "47"){
    send "RT" + PNR48
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR48 + ", " to PNRs_List
    }
}

if (PNRNumber > "48"){
    send "RT" + PNR49
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR49 + ", " to PNRs_List
    }
}

if (PNRNumber > "49"){
    send "RT" + PNR50
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR50 + ", " to PNRs_List
    }
}

if (PNRNumber > "50"){
    send "RT" + PNR51
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR51 + ", " to PNRs_List
    }
}

if (PNRNumber > "51"){
    send "RT" + PNR52
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR52 + ", " to PNRs_List
    }
}

if (PNRNumber > "52"){
    send "RT" + PNR53
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR53 + ", " to PNRs_List
    }
}

if (PNRNumber > "53"){
    send "RT" + PNR54
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR54 + ", " to PNRs_List
    }
}

if (PNRNumber > "54"){
    send "RT" + PNR55
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR55 + ", " to PNRs_List
    }
}

if (PNRNumber > "55"){
    send "RT" + PNR56
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR56 + ", " to PNRs_List
    }
}

if (PNRNumber > "56"){
    send "RT" + PNR57
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR57 + ", " to PNRs_List
    }
}

if (PNRNumber > "57"){
    send "RT" + PNR58
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR58 + ", " to PNRs_List
    }
}

if (PNRNumber > "58"){
    send "RT" + PNR59
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR59 + ", " to PNRs_List
    }
}

if (PNRNumber > "59"){
    send "RT" + PNR60
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR60 + ", " to PNRs_List
    }
}

if (PNRNumber > "60"){
    send "RT" + PNR61
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR61 + ", " to PNRs_List
    }
}

if (PNRNumber > "61"){
    send "RT" + PNR62
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR62 + ", " to PNRs_List
    }
}

if (PNRNumber > "62"){
    send "RT" + PNR63
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR63 + ", " to PNRs_List
    }
}

if (PNRNumber > "63"){
    send "RT" + PNR64
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR64 + ", " to PNRs_List
    }
}

if (PNRNumber > "64"){
    send "RT" + PNR65
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR65 + ", " to PNRs_List
    }
}

if (PNRNumber > "65"){
    send "RT" + PNR66
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR66 + ", " to PNRs_List
    }
}

if (PNRNumber > "66"){
    send "RT" + PNR67
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR67 + ", " to PNRs_List
    }
}

if (PNRNumber > "67"){
    send "RT" + PNR68
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR68 + ", " to PNRs_List
    }
}

if (PNRNumber > "68"){
    send "RT" + PNR69
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR69 + ", " to PNRs_List
    }
}

if (PNRNumber > "69"){
    send "RT" + PNR70
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR70 + ", " to PNRs_List
    }
}

if (PNRNumber > "70"){
    send "RT" + PNR71
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR71 + ", " to PNRs_List
    }
}

if (PNRNumber > "71"){
    send "RT" + PNR72
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR72 + ", " to PNRs_List
    }
}

if (PNRNumber > "72"){
    send "RT" + PNR73
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR73 + ", " to PNRs_List
    }
}

if (PNRNumber > "73"){
    send "RT" + PNR74
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR74 + ", " to PNRs_List
    }
}

if (PNRNumber > "74"){
    send "RT" + PNR75
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR75 + ", " to PNRs_List
    }
}

if (PNRNumber > "75"){
    send "RT" + PNR76
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR76 + ", " to PNRs_List
    }
}

if (PNRNumber > "76"){
    send "RT" + PNR77
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR77 + ", " to PNRs_List
    }
}

if (PNRNumber > "77"){
    send "RT" + PNR78
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR78 + ", " to PNRs_List
    }
}

if (PNRNumber > "78"){
    send "RT" + PNR79
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR79 + ", " to PNRs_List
    }
}

if (PNRNumber > "79"){
    send "RT" + PNR80
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR80 + ", " to PNRs_List
    }
}

if (PNRNumber > "80"){
    send "RT" + PNR81
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR81 + ", " to PNRs_List
    }
}

if (PNRNumber > "81"){
    send "RT" + PNR82
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR82 + ", " to PNRs_List
    }
}

if (PNRNumber > "82"){
    send "RT" + PNR83
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR83 + ", " to PNRs_List
    }
}

if (PNRNumber > "83"){
    send "RT" + PNR84
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR84 + ", " to PNRs_List
    }
}

if (PNRNumber > "84"){
    send "RT" + PNR85
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR85 + ", " to PNRs_List
    }
}

if (PNRNumber > "85"){
    send "RT" + PNR86
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR86 + ", " to PNRs_List
    }
}

if (PNRNumber > "86"){
    send "RT" + PNR87
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR87 + ", " to PNRs_List
    }
}

if (PNRNumber > "87"){
    send "RT" + PNR88
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR88 + ", " to PNRs_List
    }
}

if (PNRNumber > "88"){
    send "RT" + PNR89
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR89 + ", " to PNRs_List
    }
}

if (PNRNumber > "89"){
    send "RT" + PNR90
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR90 + ", " to PNRs_List
    }
}

if (PNRNumber > "90"){
    send "RT" + PNR91
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR91 + ", " to PNRs_List
    }
}

if (PNRNumber > "91"){
    send "RT" + PNR92
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR92 + ", " to PNRs_List
    }
}

if (PNRNumber > "92"){
    send "RT" + PNR93
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR93 + ", " to PNRs_List
    }
}

if (PNRNumber > "93"){
    send "RT" + PNR94
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR94 + ", " to PNRs_List
    }
}

if (PNRNumber > "94"){
    send "RT" + PNR95
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR95 + ", " to PNRs_List
    }
}

if (PNRNumber > "95"){
    send "RT" + PNR96
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR96 + ", " to PNRs_List
    }
}

if (PNRNumber > "96"){
    send "RT" + PNR97
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR97 + ", " to PNRs_List
    }
}

if (PNRNumber > "97"){
    send "RT" + PNR98
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR98 + ", " to PNRs_List
    }
}

if (PNRNumber > "98"){
    send "RT" + PNR99
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR99 + ", " to PNRs_List
    }
}

if (PNRNumber > "99"){
    send "RT" + PNR100
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR100 + ", " to PNRs_List
    }
}

if (PNRNumber > "100"){
    send "RT" + PNR101
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR101 + ", " to PNRs_List
    }
}

if (PNRNumber > "101"){
    send "RT" + PNR102
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR102 + ", " to PNRs_List
    }
}

if (PNRNumber > "102"){
    send "RT" + PNR103
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR103 + ", " to PNRs_List
    }
}

if (PNRNumber > "103"){
    send "RT" + PNR104
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR104 + ", " to PNRs_List
    }
}

if (PNRNumber > "104"){
    send "RT" + PNR105
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR105 + ", " to PNRs_List
    }
}
if (PNRNumber > "105"){
    send "RT" + PNR106
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR106 + ", " to PNRs_List
    }
}

if (PNRNumber > "106"){
    send "RT" + PNR107
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR107 + ", " to PNRs_List
    }
}

if (PNRNumber > "107"){
    send "RT" + PNR108
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR108 + ", " to PNRs_List
    }
}

if (PNRNumber > "108"){
    send "RT" + PNR109
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR109 + ", " to PNRs_List
    }
}

if (PNRNumber > "109"){
    send "RT" + PNR110
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR110 + ", " to PNRs_List
    }
}

if (PNRNumber > "110"){
    send "RT" + PNR111
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR111 + ", " to PNRs_List
    }
}

if (PNRNumber > "111"){
    send "RT" + PNR112
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR112 + ", " to PNRs_List
    }
}

if (PNRNumber > "112"){
    send "RT" + PNR113
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR113 + ", " to PNRs_List
    }
}
if (PNRNumber > "113"){
    send "RT" + PNR114
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR114 + ", " to PNRs_List
    }
}

if (PNRNumber > "114"){
    send "RT" + PNR115
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR115 + ", " to PNRs_List
    }
}

if (PNRNumber > "115"){
    send "RT" + PNR116
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR116 + ", " to PNRs_List
    }
}

if (PNRNumber > "116"){
    send "RT" + PNR117
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR117 + ", " to PNRs_List
    }
}

if (PNRNumber > "117"){
    send "RT" + PNR118
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR118 + ", " to PNRs_List
    }
}

if (PNRNumber > "118"){
    send "RT" + PNR119
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR119 + ", " to PNRs_List
    }
}

if (PNRNumber > "119"){
    send "RT" + PNR120
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR120 + ", " to PNRs_List
    }
}

if (PNRNumber > "120"){
    send "RT" + PNR121
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR121 + ", " to PNRs_List
    }
}

if (PNRNumber > "121"){
    send "RT" + PNR122
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR122 + ", " to PNRs_List
    }
}

if (PNRNumber > "122"){
    send "RT" + PNR123
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR123 + ", " to PNRs_List
    }
}

if (PNRNumber > "123"){
    send "RT" + PNR124
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR124 + ", " to PNRs_List
    }
}

if (PNRNumber > "124"){
    send "RT" + PNR125
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR125 + ", " to PNRs_List
    }
}

if (PNRNumber > "125"){
    send "RT" + PNR126
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR126 + ", " to PNRs_List
    }
}

if (PNRNumber > "126"){
    send "RT" + PNR127
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR127 + ", " to PNRs_List
    }
}

if (PNRNumber > "127"){
    send "RT" + PNR128
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR128 + ", " to PNRs_List
    }
}

if (PNRNumber > "128"){
    send "RT" + PNR129
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR129 + ", " to PNRs_List
    }
}

if (PNRNumber > "129"){
    send "RT" + PNR130
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR130 + ", " to PNRs_List
    }
}

if (PNRNumber > "130"){
    send "RT" + PNR131
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR131 + ", " to PNRs_List
    }
}

if (PNRNumber > "131"){
    send "RT" + PNR132
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR132 + ", " to PNRs_List
    }
}

if (PNRNumber > "132"){
    send "RT" + PNR133
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR133 + ", " to PNRs_List
    }
}

if (PNRNumber > "133"){
    send "RT" + PNR134
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR134 + ", " to PNRs_List
    }
}

if (PNRNumber > "134"){
    send "RT" + PNR135
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR135 + ", " to PNRs_List
    }
}

if (PNRNumber > "135"){
    send "RT" + PNR136
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR136 + ", " to PNRs_List
    }
}

if (PNRNumber > "136"){
    send "RT" + PNR137
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR137 + ", " to PNRs_List
    }
}

if (PNRNumber > "137"){
    send "RT" + PNR138
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR138 + ", " to PNRs_List
    }
}

if (PNRNumber > "138"){
    send "RT" + PNR139
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR139 + ", " to PNRs_List
    }
}

if (PNRNumber > "139"){
    send "RT" + PNR140
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR140 + ", " to PNRs_List
    }
}

if (PNRNumber > "140"){
    send "RT" + PNR141
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR141 + ", " to PNRs_List
    }
}

if (PNRNumber > "141"){
    send "RT" + PNR142
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR142 + ", " to PNRs_List
    }
}

if (PNRNumber > "142"){
    send "RT" + PNR143
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR143 + ", " to PNRs_List
    }
}

if (PNRNumber > "143"){
    send "RT" + PNR144
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR144 + ", " to PNRs_List
    }
}

if (PNRNumber > "144"){
    send "RT" + PNR145
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR145 + ", " to PNRs_List
    }
}

if (PNRNumber > "145"){
    send "RT" + PNR146
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR146 + ", " to PNRs_List
    }
}

if (PNRNumber > "146"){
    send "RT" + PNR147
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR147 + ", " to PNRs_List
    }
}

if (PNRNumber > "147"){
    send "RT" + PNR148
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR148 + ", " to PNRs_List
    }
}

if (PNRNumber > "148"){
    send "RT" + PNR149
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR149 + ", " to PNRs_List
    }
}

if (PNRNumber > "149"){
    send "RT" + PNR150
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR150 + ", " to PNRs_List
    }
}

if (PNRNumber > "150"){
    send "RT" + PNR151
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR151 + ", " to PNRs_List
    }
}

if (PNRNumber > "151"){
    send "RT" + PNR152
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR152 + ", " to PNRs_List
    }
}

if (PNRNumber > "152"){
    send "RT" + PNR153
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR153 + ", " to PNRs_List
    }
}

if (PNRNumber > "153"){
    send "RT" + PNR154
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR154 + ", " to PNRs_List
    }
}

if (PNRNumber > "154"){
    send "RT" + PNR155
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR155 + ", " to PNRs_List
    }
}

if (PNRNumber > "155"){
    send "RT" + PNR156
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR156 + ", " to PNRs_List
    }
}

if (PNRNumber > "156"){
    send "RT" + PNR157
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR157 + ", " to PNRs_List
    }
}

if (PNRNumber > "157"){
    send "RT" + PNR158
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR158 + ", " to PNRs_List
    }
}

if (PNRNumber > "158"){
    send "RT" + PNR159
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR159 + ", " to PNRs_List
    }
}

if (PNRNumber > "159"){
    send "RT" + PNR160
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR160 + ", " to PNRs_List
    }
}

if (PNRNumber > "160"){
    send "RT" + PNR161
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR161 + ", " to PNRs_List
    }
}

if (PNRNumber > "161"){
    send "RT" + PNR162
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR162 + ", " to PNRs_List
    }
}

if (PNRNumber > "162"){
    send "RT" + PNR163
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR163 + ", " to PNRs_List
    }
}

if (PNRNumber > "163"){
    send "RT" + PNR164
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR164 + ", " to PNRs_List
    }
}

if (PNRNumber > "164"){
    send "RT" + PNR165
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR165 + ", " to PNRs_List
    }
}

if (PNRNumber > "165"){
    send "RT" + PNR166
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR166 + ", " to PNRs_List
    }
}

if (PNRNumber > "166"){
    send "RT" + PNR167
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR167 + ", " to PNRs_List
    }
}

if (PNRNumber > "167"){
    send "RT" + PNR168
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR168 + ", " to PNRs_List
    }
}

if (PNRNumber > "168"){
    send "RT" + PNR169
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR169 + ", " to PNRs_List
    }
}

if (PNRNumber > "169"){
    send "RT" + PNR170
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR170 + ", " to PNRs_List
    }
}

if (PNRNumber > "170"){
    send "RT" + PNR171
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR171 + ", " to PNRs_List
    }
}

if (PNRNumber > "171"){
    send "RT" + PNR172
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR172 + ", " to PNRs_List
    }
}

if (PNRNumber > "172"){
    send "RT" + PNR173
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR173 + ", " to PNRs_List
    }
}

if (PNRNumber > "173"){
    send "RT" + PNR174
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR174 + ", " to PNRs_List
    }
}

if (PNRNumber > "174"){
    send "RT" + PNR175
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR175 + ", " to PNRs_List
    }
}

if (PNRNumber > "175"){
    send "RT" + PNR176
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR176 + ", " to PNRs_List
    }
}

if (PNRNumber > "176"){
    send "RT" + PNR177
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR177 + ", " to PNRs_List
    }
}

if (PNRNumber > "177"){
    send "RT" + PNR178
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR178 + ", " to PNRs_List
    }
}

if (PNRNumber > "178"){
    send "RT" + PNR179
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR179 + ", " to PNRs_List
    }
}

if (PNRNumber > "179"){
    send "RT" + PNR180
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR180 + ", " to PNRs_List
    }
}

if (PNRNumber > "180"){
    send "RT" + PNR181
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR181 + ", " to PNRs_List
    }
}

if (PNRNumber > "181"){
    send "RT" + PNR182
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR182 + ", " to PNRs_List
    }
}

if (PNRNumber > "182"){
    send "RT" + PNR183
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR183 + ", " to PNRs_List
    }
}

if (PNRNumber > "183"){
    send "RT" + PNR184
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR184 + ", " to PNRs_List
    }
}

if (PNRNumber > "184"){
    send "RT" + PNR185
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR185 + ", " to PNRs_List
    }
}

if (PNRNumber > "185"){
    send "RT" + PNR186
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR186 + ", " to PNRs_List
    }
}

if (PNRNumber > "186"){
    send "RT" + PNR187
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR187 + ", " to PNRs_List
    }
}

if (PNRNumber > "187"){
    send "RT" + PNR188
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR188 + ", " to PNRs_List
    }
}

if (PNRNumber > "188"){
    send "RT" + PNR189
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR189 + ", " to PNRs_List
    }
}

if (PNRNumber > "189"){
    send "RT" + PNR190
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR190 + ", " to PNRs_List
    }
}

if (PNRNumber > "190"){
    send "RT" + PNR191
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR191 + ", " to PNRs_List
    }
}

if (PNRNumber > "191"){
    send "RT" + PNR192
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR192 + ", " to PNRs_List
    }
}

if (PNRNumber > "192"){
    send "RT" + PNR193
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR193 + ", " to PNRs_List
    }
}

if (PNRNumber > "193"){
    send "RT" + PNR194
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR194 + ", " to PNRs_List
    }
}

if (PNRNumber > "194"){
    send "RT" + PNR195
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR195 + ", " to PNRs_List
    }
}

if (PNRNumber > "195"){
    send "RT" + PNR196
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR196 + ", " to PNRs_List
    }
}

if (PNRNumber > "196"){
    send "RT" + PNR197
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR197 + ", " to PNRs_List
    }
}

if (PNRNumber > "197"){
    send "RT" + PNR198
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR198 + ", " to PNRs_List
    }
}

if (PNRNumber > "198"){
    send "RT" + PNR199
    call "fast_search"
    capture line:1, column:32, length:7 assign to success_indicator
    if (success_indicator == "Success"){
        append PNR199 + ", " to PNRs_List
    }
}

send "SRT" + PNRs_List
ask "Continue?" assign to continue_response

