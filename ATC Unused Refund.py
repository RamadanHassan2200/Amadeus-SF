ask "Enter the Unused Tickets, (With/Without TWD/TKT)" assign to tickets_patch
send "IG"
send  "SRT" +tickets_patch

assign "0" to ticket1
assign "0" to ticket2
assign "0" to ticket3
assign "0" to ticket4
assign "0" to ticket5
assign "0" to ticket6
assign "0" to ticket7
assign "0" to ticket8
assign "0" to ticket9
assign "0" to ticket10
assign "0" to ticket11
assign "0" to ticket12
assign "0" to ticket13
assign "0" to ticket14
assign "0" to ticket15
assign "0" to ticket16
assign "0" to ticket17
assign "0" to ticket18
assign "0" to ticket19
assign "0" to ticket20
assign "0" to ticket21
assign "0" to ticket22
assign "0" to ticket23
assign "0" to ticket24
assign "0" to ticket25
assign "0" to ticket26
assign "0" to ticket27
assign "0" to ticket28
assign "0" to ticket29
assign "0" to ticket30
assign "0" to ticket31
assign "0" to ticket32
assign "0" to ticket33
assign "0" to ticket34
assign "0" to ticket35
assign "0" to ticket36
assign "0" to ticket37
assign "0" to ticket38
assign "0" to ticket39
assign "0" to ticket40
assign "0" to ticket41
assign "0" to ticket42
assign "0" to ticket43
assign "0" to ticket44
assign "0" to ticket45
assign "0" to ticket46
assign "0" to ticket47
assign "0" to ticket48
assign "0" to ticket49
assign "0" to ticket50
assign "0" to ticket51
assign "0" to ticket52
assign "0" to ticket53
assign "0" to ticket54
assign "0" to ticket55
assign "0" to ticket56
assign "0" to ticket57
assign "0" to ticket58
assign "0" to ticket59
assign "0" to ticket60
assign "0" to ticket61
assign "0" to ticket62
assign "0" to ticket63
assign "0" to ticket64
assign "0" to ticket65
assign "0" to ticket66
assign "0" to ticket67
assign "0" to ticket68
assign "0" to ticket69
assign "0" to ticket70
assign "0" to ticket71
assign "0" to ticket72
assign "0" to ticket73
assign "0" to ticket74
assign "0" to ticket75
assign "0" to ticket76
assign "0" to ticket77
assign "0" to ticket78
assign "0" to ticket79
assign "0" to ticket80
assign "0" to ticket81
assign "0" to ticket82
assign "0" to ticket83
assign "0" to ticket84
assign "0" to ticket85
assign "0" to ticket86
assign "0" to ticket87
assign "0" to ticket88
assign "0" to ticket89
assign "0" to ticket90
assign "0" to ticket91
assign "0" to ticket92
assign "0" to ticket93
assign "0" to ticket94
assign "0" to ticket95
assign "0" to ticket96
assign "0" to ticket97
assign "0" to ticket98
assign "0" to ticket99
assign "0" to ticket100
assign "0" to ticket101
assign "0" to ticket102
assign "0" to ticket103
assign "0" to ticket104
assign "0" to ticket105
assign "0" to ticket106
assign "0" to ticket107
assign "0" to ticket108
assign "0" to ticket109
assign "0" to ticket110
assign "0" to ticket111
assign "0" to ticket112
assign "0" to ticket113
assign "0" to ticket114
assign "0" to ticket115
assign "0" to ticket116
assign "0" to ticket117
assign "0" to ticket118
assign "0" to ticket119
assign "0" to ticket120
assign "0" to ticket121
assign "0" to ticket122
assign "0" to ticket123
assign "0" to ticket124
assign "0" to ticket125
assign "0" to ticket126
assign "0" to ticket127
assign "0" to ticket128
assign "0" to ticket129
assign "0" to ticket130
assign "0" to ticket131
assign "0" to ticket132
assign "0" to ticket133
assign "0" to ticket134
assign "0" to ticket135
assign "0" to ticket136
assign "0" to ticket137
assign "0" to ticket138
assign "0" to ticket139
assign "0" to ticket140
assign "0" to ticket141
assign "0" to ticket142
assign "0" to ticket143
assign "0" to ticket144
assign "0" to ticket145
assign "0" to ticket146
assign "0" to ticket147
assign "0" to ticket148
assign "0" to ticket149
assign "0" to ticket150
assign "0" to ticket151



capture line:1, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:32, length:14 assign to ticket1
}
capture line:1, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:39, length:14 assign to ticket2
}
capture line:1, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:47, length:14 assign to ticket3
}
capture line:2, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:61, length:3 assign to ticket4
    capture line:2, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket4
}
capture line:2, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:62, length:2 assign to ticket5
    capture line:2, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket5
}
capture line:2, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:15, length:14 assign to ticket6
}
capture line:2, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:21, length:14 assign to ticket7
}
capture line:2, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:43, length:14 assign to ticket8
}
capture line:3, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:3, length:14 assign to ticket9
}
capture line:3, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:13, length:14 assign to ticket10
}
capture line:3, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:25, length:14 assign to ticket11
}
capture line:3, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:28, length:14 assign to ticket12
}
capture line:3, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:43, length:14 assign to ticket13
}
capture line:3, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:47, length:14 assign to ticket14
}
capture line:3, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:58, length:6 assign to ticket15
    capture line:4, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket15
}
capture line:4, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:7, length:14 assign to ticket16
}
capture line:4, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:11, length:14 assign to ticket17
}
capture line:4, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:26, length:14 assign to ticket18
}
capture line:4, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:29, length:14 assign to ticket19
}
capture line:4, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:41, length:14 assign to ticket20
}
capture line:4, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:51, length:13 assign to ticket21
    capture line:5, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket21
}
capture line:4, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:56, length:8 assign to ticket22
    capture line:5, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket22
}
capture line:5, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:9, length:14 assign to ticket23
}
capture line:5, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:11, length:14 assign to ticket24
}
capture line:5, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:24, length:14 assign to ticket25
}
capture line:5, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:33, length:14 assign to ticket26
}
capture line:5, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:39, length:14 assign to ticket27
}
capture line:5, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:54, length:10 assign to ticket28
    capture line:6, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket28
}
capture line:5, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:55, length:9 assign to ticket29
    capture line:6, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket29
}
capture line:6, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:7, length:14 assign to ticket30
}
capture line:6, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:15, length:14 assign to ticket31
}
capture line:6, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:22, length:14 assign to ticket32
}
capture line:6, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:37, length:14 assign to ticket33
}
capture line:6, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:52, length:12 assign to ticket34
    capture line:7, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket34
}
capture line:6, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:59, length:5 assign to ticket35
    capture line:7, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket35
}
capture line:7, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:5, length:14 assign to ticket36
}
capture line:7, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:19, length:14 assign to ticket37
}
capture line:7, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:20, length:14 assign to ticket38
}
capture line:7, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:35, length:14 assign to ticket39
}
capture line:7, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:41, length:14 assign to ticket40
}
capture line:7, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:50, length:14 assign to ticket41
}
capture line:8, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:63, length:1 assign to ticket42
    capture line:8, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket42
}
capture line:8, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:3, length:14 assign to ticket43
}
capture line:8, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:18, length:14 assign to ticket44
}
capture line:8, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:23, length:14 assign to ticket45
}
capture line:8, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:33, length:14 assign to ticket46
}
capture line:8, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:45, length:14 assign to ticket47
}
capture line:8, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:48, length:14 assign to ticket48
}
capture line:9, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:63, length:1 assign to ticket49
    capture line:9, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket49
}
capture line:9, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:5, length:14 assign to ticket50
}
capture line:9, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:16, length:14 assign to ticket51
}
capture line:9, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:27, length:14 assign to ticket52
}
capture line:9, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:31, length:14 assign to ticket53
}
capture line:9, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:46, length:14 assign to ticket54
}
capture line:9, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:49, length:14 assign to ticket55
}
capture line:10, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:61, length:3 assign to ticket56
    capture line:10, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket56
}
capture line:10, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:9, length:14 assign to ticket57
}
capture line:10, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:14, length:14 assign to ticket58
}
capture line:10, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:29, length:14 assign to ticket59
}
capture line:10, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:31, length:14 assign to ticket60
}
capture line:10, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:44, length:14 assign to ticket61
}
capture line:10, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:53, length:11 assign to ticket62
    capture line:11, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket62
}
capture line:10, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:59, length:5 assign to ticket63
    capture line:11, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket63
}
capture line:11, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:12, length:14 assign to ticket64
}
capture line:11, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:13, length:14 assign to ticket65
}
capture line:11, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:27, length:14 assign to ticket66
}
capture line:11, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:35, length:14 assign to ticket67
}
capture line:11, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:42, length:14 assign to ticket68
}
capture line:11, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:57, length:7 assign to ticket69
    capture line:12, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket69
}
capture line:12, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:10, length:14 assign to ticket70
}
capture line:12, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:17, length:14 assign to ticket71
}
capture line:12, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:25, length:14 assign to ticket72
}
capture line:12, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:39, length:14 assign to ticket73
}
capture line:12, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:40, length:14 assign to ticket74
}
capture line:12, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:55, length:9 assign to ticket75
    capture line:13, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket76
}
capture line:13, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:61, length:3 assign to ticket77
    capture line:13, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket77
}
capture line:13, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:8, length:14 assign to ticket78
}
capture line:13, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:21, length:14 assign to ticket79
}
capture line:13, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:23, length:14 assign to ticket80
}
capture line:13, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:38, length:14 assign to ticket81
}
capture line:13, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:43, length:14 assign to ticket82
}
capture line:13, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:53, length:11 assign to ticket83
    capture line:14, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket83
}
capture line:14, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:3, length:14 assign to ticket84
}
capture line:14, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:6, length:14 assign to ticket85
}
capture line:14, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:21, length:14 assign to ticket86
}
capture line:14, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:25, length:14 assign to ticket87
}
capture line:14, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:36, length:14 assign to ticket89
}
capture line:14, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:47, length:14 assign to ticket90
}
capture line:14, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:51, length:13 assign to ticket91
    capture line:15, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket91
}
capture line:15, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:4, length:14 assign to ticket92
}
capture line:15, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:7, length:14 assign to ticket93
}
capture line:15, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:19, length:14 assign to ticket94
}
capture line:15, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:29, length:14 assign to ticket95
}
capture line:15, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:34, length:14 assign to ticket96
}
capture line:15, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:49, length:14 assign to ticket97
}
capture line:15, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:51, length:13 assign to ticket98
    capture line:16, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket98
}
capture line:16, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:2, length:14 assign to ticket99
}
capture line:16, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:11, length:14 assign to ticket100
}
capture line:16, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:17, length:14 assign to ticket101
}
capture line:16, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:32, length:14 assign to ticket102
}
capture line:16, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:33, length:14 assign to ticket103
}
capture line:16, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:47, length:14 assign to ticket104
}
capture line:16, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:55, length:9 assign to ticket105
    capture line:17, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket105
}
capture line:17, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:62, length:2 assign to ticket106
    capture line:17, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket106
}
capture line:17, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:15, length:14 assign to ticket107
}
capture line:17, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:30, length:14 assign to ticket108
}
capture line:17, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:37, length:14 assign to ticket109
}
capture line:17, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:45, length:14 assign to ticket110
}
capture line:17, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:59, length:5 assign to ticket111
    capture line:18, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket111
}
capture line:17, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:60, length:4 assign to ticket112
    capture line:18, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket112
}
capture line:18, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:13, length:14 assign to ticket113
}
capture line:18, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:19, length:14 assign to ticket114
}
capture line:18, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:28, length:14 assign to ticket115
}
capture line:18, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:41, length:14 assign to ticket116
}
capture line:18, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:43, length:14 assign to ticket117
}
capture line:18, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:58, length:6 assign to ticket118
    capture line:19, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket118
}
capture line:19, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:63, length:1 assign to ticket119
    capture line:19, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket119
}
capture line:19, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:11, length:14 assign to ticket120
}
capture line:19, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:23, length:14 assign to ticket121
}
capture line:19, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:26, length:14 assign to ticket122
}
capture line:19, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:41, length:14 assign to ticket123
}
capture line:19, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:45, length:14 assign to ticket124
}
capture line:19, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:56, length:8 assign to ticket125
    capture line:20, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket125
}
capture line:20, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:5, length:14 assign to ticket126
}
capture line:20, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:9, length:14 assign to ticket127
}
capture line:20, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:24, length:14 assign to ticket128
}
capture line:20, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:27, length:14 assign to ticket129
}
capture line:20, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:39, length:14 assign to ticket130
}
capture line:20, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:49, length:14 assign to ticket131
}
capture line:20, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:54, length:10 assign to ticket132
    capture line:21, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket132
}
capture line:21, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:7, length:14 assign to ticket133
}
capture line:21, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:9, length:14 assign to ticket134
}
capture line:21, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:22, length:14 assign to ticket135
}
capture line:21, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:31, length:14 assign to ticket136
}
capture line:21, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:37, length:14 assign to ticket137
}
capture line:21, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:52, length:12 assign to ticket138
    capture line:22, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket138
}
capture line:21, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:53, length:11 assign to ticket139
    capture line:22, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket139
}
capture line:22, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:5, length:14 assign to ticket140
}
capture line:22, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:13, length:14 assign to ticket141
}
capture line:22, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:20, length:14 assign to ticket142
}
capture line:22, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:35, length:14 assign to ticket143
}
capture line:22, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:50, length:14 assign to ticket144
}
capture line:22, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:57, length:7 assign to ticket145
    capture line:23, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket145
}
capture line:23, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:3, length:14 assign to ticket146
}
capture line:23, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:17, length:14 assign to ticket147
}
capture line:23, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:18, length:14 assign to ticket148
}
capture line:23, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:33, length:14 assign to ticket149
}
capture line:23, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:39, length:14 assign to ticket150
}
capture line:23, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:48, length:14 assign to ticket151
}

assign "0" to ticketsNO

if (ticket1 != "0"){
    send "TWD/TKT" +ticket1
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket2 != "0"){
    send "TWD/TKT" +ticket2
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket3 != "0"){
    send "TWD/TKT" +ticket3
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket4 != "0"){
    send "TWD/TKT" +ticket4
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket5 != "0"){
    send "TWD/TKT" +ticket5
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket6 != "0"){
    send "TWD/TKT" +ticket6
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket7 != "0"){
    send "TWD/TKT" +ticket7
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket8 != "0"){
    send "TWD/TKT" +ticket8
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket9 != "0"){
    send "TWD/TKT" +ticket9
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket10 != "0"){
    send "TWD/TKT" +ticket10
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket11 != "0"){
    send "TWD/TKT" +ticket11
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket12 != "0"){
    send "TWD/TKT" +ticket12
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket13 != "0"){
    send "TWD/TKT" +ticket13
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket14 != "0"){
    send "TWD/TKT" +ticket14
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket15 != "0"){
    send "TWD/TKT" +ticket15
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket16 != "0"){
    send "TWD/TKT" +ticket16
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket17 != "0"){
    send "TWD/TKT" +ticket17
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket18 != "0"){
    send "TWD/TKT" +ticket18
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket19 != "0"){
    send "TWD/TKT" +ticket19
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket20 != "0"){
    send "TWD/TKT" +ticket20
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket21 != "0"){
    send "TWD/TKT" +ticket21
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket22 != "0"){
    send "TWD/TKT" +ticket22
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket23 != "0"){
    send "TWD/TKT" +ticket23
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket24 != "0"){
    send "TWD/TKT" +ticket24
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket25 != "0"){
    send "TWD/TKT" +ticket25
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket26 != "0"){
    send "TWD/TKT" +ticket26
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket27 != "0"){
    send "TWD/TKT" +ticket27
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket28 != "0"){
    send "TWD/TKT" +ticket28
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket29 != "0"){
    send "TWD/TKT" +ticket29
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket30 != "0"){
    send "TWD/TKT" +ticket30
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket31 != "0"){
    send "TWD/TKT" +ticket31
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket32 != "0"){
    send "TWD/TKT" +ticket32
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket33 != "0"){
    send "TWD/TKT" +ticket33
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket34 != "0"){
    send "TWD/TKT" +ticket34
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket35 != "0"){
    send "TWD/TKT" +ticket35
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket36 != "0"){
    send "TWD/TKT" +ticket36
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket37 != "0"){
    send "TWD/TKT" +ticket37
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket38 != "0"){
    send "TWD/TKT" +ticket38
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket39 != "0"){
    send "TWD/TKT" +ticket39
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket40 != "0"){
    send "TWD/TKT" +ticket40
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket41 != "0"){
    send "TWD/TKT" +ticket41
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket42 != "0"){
    send "TWD/TKT" +ticket42
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket43 != "0"){
    send "TWD/TKT" +ticket43
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket44 != "0"){
    send "TWD/TKT" +ticket44
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket45 != "0"){
    send "TWD/TKT" +ticket45
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket46 != "0"){
    send "TWD/TKT" +ticket46
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket47 != "0"){
    send "TWD/TKT" +ticket47
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket48 != "0"){
    send "TWD/TKT" +ticket48
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket49 != "0"){
    send "TWD/TKT" +ticket49
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket50 != "0"){
    send "TWD/TKT" +ticket50
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket51 != "0"){
    send "TWD/TKT" +ticket51
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket52 != "0"){
    send "TWD/TKT" +ticket52
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket53 != "0"){
    send "TWD/TKT" +ticket53
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket54 != "0"){
    send "TWD/TKT" +ticket54
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket55 != "0"){
    send "TWD/TKT" +ticket55
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket56 != "0"){
    send "TWD/TKT" +ticket56
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket57 != "0"){
    send "TWD/TKT" +ticket57
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket58 != "0"){
    send "TWD/TKT" +ticket58
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket59 != "0"){
    send "TWD/TKT" +ticket59
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket60 != "0"){
    send "TWD/TKT" +ticket60
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket61 != "0"){
    send "TWD/TKT" +ticket61
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket62 != "0"){
    send "TWD/TKT" +ticket62
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket63 != "0"){
    send "TWD/TKT" +ticket63
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket64 != "0"){
    send "TWD/TKT" +ticket64
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket65 != "0"){
    send "TWD/TKT" +ticket65
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket66 != "0"){
    send "TWD/TKT" +ticket66
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket67 != "0"){
    send "TWD/TKT" +ticket67
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket68 != "0"){
    send "TWD/TKT" +ticket68
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket69 != "0"){
    send "TWD/TKT" +ticket69
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket70 != "0"){
    send "TWD/TKT" +ticket70
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket71 != "0"){
    send "TWD/TKT" +ticket71
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket72 != "0"){
    send "TWD/TKT" +ticket72
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket73 != "0"){
    send "TWD/TKT" +ticket73
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket74 != "0"){
    send "TWD/TKT" +ticket74
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket75 != "0"){
    send "TWD/TKT" +ticket75
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket76 != "0"){
    send "TWD/TKT" +ticket76
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket77 != "0"){
    send "TWD/TKT" +ticket77
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket78 != "0"){
    send "TWD/TKT" +ticket78
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket79 != "0"){
    send "TWD/TKT" +ticket79
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket80 != "0"){
    send "TWD/TKT" +ticket80
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket81 != "0"){
    send "TWD/TKT" +ticket81
    call "z_ATC_Refund"
    ask "Done?" assign to qz5    
}
if (ticket82 != "0"){
    send "TWD/TKT" +ticket82
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket83 != "0"){
    send "TWD/TKT" +ticket83
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket84 != "0"){
    send "TWD/TKT" +ticket84
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket85 != "0"){
    send "TWD/TKT" +ticket85
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket86 != "0"){
    send "TWD/TKT" +ticket86
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket87 != "0"){
    send "TWD/TKT" +ticket87
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket88 != "0"){
    send "TWD/TKT" +ticket88
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket89 != "0"){
    send "TWD/TKT" +ticket89
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket90 != "0"){
    send "TWD/TKT" +ticket90
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket91 != "0"){
    send "TWD/TKT" +ticket91
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket92 != "0"){
    send "TWD/TKT" +ticket92
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket93 != "0"){
    send "TWD/TKT" +ticket93
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket94 != "0"){
    send "TWD/TKT" +ticket94
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket95 != "0"){
    send "TWD/TKT" +ticket95
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket96 != "0"){
    send "TWD/TKT" +ticket96
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket97 != "0"){
    send "TWD/TKT" +ticket97
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket98 != "0"){
    send "TWD/TKT" +ticket98
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket99 != "0"){
    send "TWD/TKT" +ticket99
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket100 != "0"){
    send "TWD/TKT" +ticket100
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket101 != "0"){
    send "TWD/TKT" +ticket101
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket102 != "0"){
    send "TWD/TKT" +ticket102
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket103 != "0"){
    send "TWD/TKT" +ticket103
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket104 != "0"){
    send "TWD/TKT" +ticket104
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket105 != "0"){
    send "TWD/TKT" +ticket105
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket106 != "0"){
    send "TWD/TKT" +ticket106
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket107 != "0"){
    send "TWD/TKT" +ticket107
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket108 != "0"){
    send "TWD/TKT" +ticket108
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket109 != "0"){
    send "TWD/TKT" +ticket109
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket110 != "0"){
    send "TWD/TKT" +ticket110
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket111 != "0"){
    send "TWD/TKT" +ticket111
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket112 != "0"){
    send "TWD/TKT" +ticket112
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket113 != "0"){
    send "TWD/TKT" +ticket113
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket114 != "0"){
    send "TWD/TKT" +ticket114
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket115 != "0"){
    send "TWD/TKT" +ticket115
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket116 != "0"){
    send "TWD/TKT" +ticket116
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket117 != "0"){
    send "TWD/TKT" +ticket117
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket118 != "0"){
    send "TWD/TKT" +ticket118
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket119 != "0"){
    send "TWD/TKT" +ticket119
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket120 != "0"){
    send "TWD/TKT" +ticket120
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket121 != "0"){
    send "TWD/TKT" +ticket121
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket122 != "0"){
    send "TWD/TKT" +ticket122
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket123 != "0"){
    send "TWD/TKT" +ticket123
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket124 != "0"){
    send "TWD/TKT" +ticket124
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket125 != "0"){
    send "TWD/TKT" +ticket125
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket126 != "0"){
    send "TWD/TKT" +ticket126
    send "TWD/TKT" +ticket
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket127 != "0"){
    send "TWD/TKT" +ticket127
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket128 != "0"){
    send "TWD/TKT" +ticket128
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket129 != "0"){
    send "TWD/TKT" +ticket129
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket130 != "0"){
    send "TWD/TKT" +ticket130
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket131 != "0"){
    send "TWD/TKT" +ticket131
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket132 != "0"){
    send "TWD/TKT" +ticket132
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket133 != "0"){
    send "TWD/TKT" +ticket133
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket134 != "0"){
    send "TWD/TKT" +ticket134
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket135 != "0"){
    send "TWD/TKT" +ticket135
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket136 != "0"){
    send "TWD/TKT" +ticket136
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket137 != "0"){
    send "TWD/TKT" +ticket137
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket138 != "0"){
    send "TWD/TKT" +ticket138
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket139 != "0"){
    send "TWD/TKT" +ticket139
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket140 != "0"){
    send "TWD/TKT" +ticket140
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket141 != "0"){
    send "TWD/TKT" +ticket141
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket142 != "0"){
    send "TWD/TKT" +ticket142
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket143 != "0"){
    send "TWD/TKT" +ticket143
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket144 != "0"){
    send "TWD/TKT" +ticket144
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket145 != "0"){
    send "TWD/TKT" +ticket145
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket146 != "0"){
    send "TWD/TKT" +ticket146
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket147 != "0"){
    send "TWD/TKT" +ticket147
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket148 != "0"){
    send "TWD/TKT" +ticket148
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}
if (ticket149 != "0"){
    send "TWD/TKT" +ticket149
    call "z_ATC_Refund"
    ask "Done?" assign to qz5  
}
if (ticket150 != "0"){
    send "TWD/TKT" +ticket150
    call "z_ATC_Refund"
    ask "Done?" assign to qz5   
}
if (ticket151 != "0"){
    send "TWD/TKT" +ticket151
    call "z_ATC_Refund"
    ask "Done?" assign to qz5
}


