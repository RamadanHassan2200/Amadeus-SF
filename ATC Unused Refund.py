ask "Enter the Unused Tickets, (With/Without TWD/TKT)" assign to tickets_patch
send "IG"
send "SRT" +tickets_patch


capture line:1, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:32, length:14 assign to ticket01
}
capture line:1, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:33, length:14 assign to ticket02
}
capture line:1, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:34, length:14 assign to ticket03
}
capture line:1, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:35, length:14 assign to ticket04
}
capture line:1, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:36, length:14 assign to ticket05
}
capture line:1, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:37, length:14 assign to ticket06
}
capture line:1, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:38, length:14 assign to ticket07
}
capture line:1, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:39, length:14 assign to ticket08
}
capture line:1, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:40, length:14 assign to ticket09
}
capture line:1, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:41, length:14 assign to ticket10
}
capture line:1, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:42, length:14 assign to ticket11
}
capture line:1, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:43, length:14 assign to ticket12
}
capture line:1, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:44, length:14 assign to ticket13
}
capture line:1, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:45, length:14 assign to ticket14
}
capture line:1, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:46, length:14 assign to ticket15
}
capture line:1, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:47, length:14 assign to ticket16
}
capture line:1, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:48, length:14 assign to ticket17
}
capture line:1, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:49, length:14 assign to ticket18
}
capture line:1, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:50, length:14 assign to ticket19
}
capture line:1, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:51, length:13 assign to ticket20
    capture line:2, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket20
}
capture line:1, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:52, length:12 assign to ticket21
    capture line:2, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket21
}
capture line:1, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:53, length:11 assign to ticket22
    capture line:2, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket22
}
capture line:1, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:54, length:10 assign to ticket23
    capture line:2, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket23
}
capture line:1, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:55, length:9 assign to ticket24
    capture line:2, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket24
}
capture line:1, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:56, length:8 assign to ticket25
    capture line:2, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket25
}
capture line:1, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:57, length:7 assign to ticket26
    capture line:2, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket26
}
capture line:1, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:58, length:6 assign to ticket27
    capture line:2, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket27
}
capture line:1, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:59, length:5 assign to ticket28
    capture line:2, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket28
}
capture line:1, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:60, length:4 assign to ticket29
    capture line:2, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket29
}

capture line:2, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:61, length:3 assign to ticket30
    capture line:2, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket30
}
capture line:2, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:62, length:2 assign to ticket31
    capture line:2, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket31
}
capture line:2, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:1, column:63, length:1 assign to ticket32
    capture line:2, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket32
}
capture line:2, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:2, length:14 assign to ticket33
}
capture line:2, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:3, length:14 assign to ticket34
}
capture line:2, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:4, length:14 assign to ticket35
}
capture line:2, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:5, length:14 assign to ticket36
}
capture line:2, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:6, length:14 assign to ticket37
}
capture line:2, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:7, length:14 assign to ticket38
}
capture line:2, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:8, length:14 assign to ticket39
}
capture line:2, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:9, length:14 assign to ticket40
}
capture line:2, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:10, length:14 assign to ticket41
}
capture line:2, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:11, length:14 assign to ticket42
}
capture line:2, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:12, length:14 assign to ticket43
}
capture line:2, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:13, length:14 assign to ticket44
}
capture line:2, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:14, length:14 assign to ticket45
}
capture line:2, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:15, length:14 assign to ticket46
}
capture line:2, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:16, length:14 assign to ticket47
}
capture line:2, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:17, length:14 assign to ticket48
}
capture line:2, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:18, length:14 assign to ticket49
}
capture line:2, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:19, length:14 assign to ticket50
}
capture line:2, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:20, length:14 assign to ticket51
}
capture line:2, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:21, length:14 assign to ticket52
}
capture line:2, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:22, length:14 assign to ticket53
}
capture line:2, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:23, length:14 assign to ticket54
}
capture line:2, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:24, length:14 assign to ticket55
}
capture line:2, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:25, length:14 assign to ticket56
}
capture line:2, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:26, length:14 assign to ticket57
}
capture line:2, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:27, length:14 assign to ticket58
}
capture line:2, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:28, length:14 assign to ticket59
}
capture line:2, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:29, length:14 assign to ticket60
}
capture line:2, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:30, length:14 assign to ticket61
}
capture line:2, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:31, length:14 assign to ticket62
}
capture line:2, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:32, length:14 assign to ticket63
}
capture line:2, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:33, length:14 assign to ticket64
}
capture line:2, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:34, length:14 assign to ticket65
}
capture line:2, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:35, length:14 assign to ticket66
}
capture line:2, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:36, length:14 assign to ticket67
}
capture line:2, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:37, length:14 assign to ticket68
}
capture line:2, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:38, length:14 assign to ticket69
}
capture line:2, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:39, length:14 assign to ticket70
}
capture line:2, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:40, length:14 assign to ticket71
}
capture line:2, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:41, length:14 assign to ticket72
}
capture line:2, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:42, length:14 assign to ticket73
}
capture line:2, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:43, length:14 assign to ticket74
}
capture line:2, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:44, length:14 assign to ticket75
}
capture line:2, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:45, length:14 assign to ticket76
}
capture line:2, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:46, length:14 assign to ticket77
}
capture line:2, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:47, length:14 assign to ticket78
}
capture line:2, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:48, length:14 assign to ticket79
}
capture line:2, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:49, length:14 assign to ticket80
}
capture line:2, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:50, length:14 assign to ticket81
}
capture line:2, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:51, length:13 assign to ticket82
    capture line:3, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket82
}
capture line:2, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:52, length:12 assign to ticket83
    capture line:3, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket83
}
capture line:2, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:53, length:11 assign to ticket84
    capture line:3, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket84
}
capture line:2, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:54, length:10 assign to ticket85
    capture line:3, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket85
}
capture line:2, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:55, length:9 assign to ticket86
    capture line:3, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket86
}
capture line:2, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:56, length:8 assign to ticket87
    capture line:3, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket87
}
capture line:2, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:57, length:7 assign to ticket88
    capture line:3, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket88
}
capture line:2, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:58, length:6 assign to ticket89
    capture line:3, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket89
}
capture line:2, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:59, length:5 assign to ticket90
    capture line:3, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket90
}
capture line:2, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:60, length:4 assign to ticket91
    capture line:3, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket91
}

capture line:3, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:61, length:3 assign to ticket92
    capture line:3, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket30
}
capture line:3, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:62, length:2 assign to ticket93
    capture line:3, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket93
}
capture line:3, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:2, column:63, length:1 assign to ticket94
    capture line:3, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket94
}
capture line:3, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:2, length:14 assign to ticket95
}
capture line:3, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:3, length:14 assign to ticket96
}
capture line:3, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:4, length:14 assign to ticket97
}
capture line:3, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:5, length:14 assign to ticket98
}
capture line:3, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:6, length:14 assign to ticket99
}
capture line:3, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:7, length:14 assign to ticket100
}
capture line:3, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:8, length:14 assign to ticket101
}
capture line:3, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:9, length:14 assign to ticket102
}
capture line:3, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:10, length:14 assign to ticket103
}
capture line:3, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:11, length:14 assign to ticket104
}
capture line:3, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:12, length:14 assign to ticket105
}
capture line:3, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:13, length:14 assign to ticket106
}
capture line:3, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:14, length:14 assign to ticket107
}
capture line:3, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:15, length:14 assign to ticket108
}
capture line:3, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:16, length:14 assign to ticket109
}
capture line:3, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:17, length:14 assign to ticket110
}
capture line:3, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:18, length:14 assign to ticket111
}
capture line:3, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:19, length:14 assign to ticket112
}
capture line:3, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:20, length:14 assign to ticket113
}
capture line:3, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:21, length:14 assign to ticket114
}
capture line:3, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:22, length:14 assign to ticket115
}
capture line:3, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:23, length:14 assign to ticket116
}
capture line:3, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:24, length:14 assign to ticket117
}
capture line:3, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:25, length:14 assign to ticket118
}
capture line:3, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:26, length:14 assign to ticket119
}
capture line:3, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:27, length:14 assign to ticket120
}
capture line:3, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:28, length:14 assign to ticket121
}
capture line:3, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:29, length:14 assign to ticket122
}
capture line:3, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:30, length:14 assign to ticket123
}
capture line:3, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:31, length:14 assign to ticket124
}
capture line:3, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:32, length:14 assign to ticket125
}
capture line:3, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:33, length:14 assign to ticket126
}
capture line:3, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:34, length:14 assign to ticket127
}
capture line:3, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:35, length:14 assign to ticket128
}
capture line:3, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:36, length:14 assign to ticket129
}
capture line:3, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:37, length:14 assign to ticket130
}
capture line:3, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:38, length:14 assign to ticket131
}
capture line:3, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:39, length:14 assign to ticket132
}
capture line:3, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:40, length:14 assign to ticket133
}
capture line:3, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:41, length:14 assign to ticket134
}
capture line:3, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:42, length:14 assign to ticket135
}
capture line:3, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:43, length:14 assign to ticket136
}
capture line:3, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:44, length:14 assign to ticket137
}
capture line:3, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:45, length:14 assign to ticket138
}
capture line:3, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:46, length:14 assign to ticket139
}
capture line:3, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:47, length:14 assign to ticket140
}
capture line:3, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:48, length:14 assign to ticket141
}
capture line:3, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:49, length:14 assign to ticket142
}
capture line:3, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:50, length:14 assign to ticket143
}
capture line:3, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:51, length:13 assign to ticket144
    capture line:4, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket144
}
capture line:3, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:52, length:12 assign to ticket145
    capture line:4, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket145
}
capture line:3, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:53, length:11 assign to ticket146
    capture line:4, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket146
}
capture line:3, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:54, length:10 assign to ticket147
    capture line:4, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket147
}
capture line:3, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:55, length:9 assign to ticket148
    capture line:4, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket148
}
capture line:3, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:56, length:8 assign to ticket149
    capture line:4, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket149
}
capture line:3, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:57, length:7 assign to ticket150
    capture line:4, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket150
}
capture line:3, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:58, length:6 assign to ticket151
    capture line:4, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket151
}
capture line:3, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:59, length:5 assign to ticket152
    capture line:4, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket152
}
capture line:3, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:60, length:4 assign to ticket153
    capture line:4, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket153
}

capture line:4, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:61, length:3 assign to ticket154
    capture line:4, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket154
}
capture line:4, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:62, length:2 assign to ticket155
    capture line:4, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket155
}
capture line:4, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:3, column:63, length:1 assign to ticket156
    capture line:4, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket156
}
capture line:4, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:2, length:14 assign to ticket157
}
capture line:4, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:3, length:14 assign to ticket158
}
capture line:4, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:4, length:14 assign to ticket159
}
capture line:4, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:5, length:14 assign to ticket160
}
capture line:4, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:6, length:14 assign to ticket161
}
capture line:4, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:7, length:14 assign to ticket162
}
capture line:4, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:8, length:14 assign to ticket163
}
capture line:4, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:9, length:14 assign to ticket164
}
capture line:4, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:10, length:14 assign to ticket165
}
capture line:4, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:11, length:14 assign to ticket166
}
capture line:4, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:12, length:14 assign to ticket167
}
capture line:4, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:13, length:14 assign to ticket168
}
capture line:4, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:14, length:14 assign to ticket169
}
capture line:4, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:15, length:14 assign to ticket170
}
capture line:4, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:16, length:14 assign to ticket171
}
capture line:4, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:17, length:14 assign to ticket172
}
capture line:4, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:18, length:14 assign to ticket173
}
capture line:4, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:19, length:14 assign to ticket174
}
capture line:4, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:20, length:14 assign to ticket175
}
capture line:4, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:21, length:14 assign to ticket176
}
capture line:4, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:22, length:14 assign to ticket177
}
capture line:4, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:23, length:14 assign to ticket178
}
capture line:4, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:24, length:14 assign to ticket179
}
capture line:4, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:25, length:14 assign to ticket180
}
capture line:4, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:26, length:14 assign to ticket181
}
capture line:4, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:27, length:14 assign to ticket182
}
capture line:4, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:28, length:14 assign to ticket183
}
capture line:4, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:29, length:14 assign to ticket184
}
capture line:4, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:30, length:14 assign to ticket185
}
capture line:4, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:31, length:14 assign to ticket186
}
capture line:4, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:32, length:14 assign to ticket187
}
capture line:4, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:33, length:14 assign to ticket188
}
capture line:4, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:34, length:14 assign to ticket189
}
capture line:4, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:35, length:14 assign to ticket190
}
capture line:4, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:36, length:14 assign to ticket191
}
capture line:4, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:37, length:14 assign to ticket192
}
capture line:4, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:38, length:14 assign to ticket193
}
capture line:4, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:39, length:14 assign to ticket194
}
capture line:4, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:40, length:14 assign to ticket195
}
capture line:4, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:41, length:14 assign to ticket196
}
capture line:4, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:42, length:14 assign to ticket197
}
capture line:4, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:43, length:14 assign to ticket198
}
capture line:4, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:44, length:14 assign to ticket199
}
capture line:4, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:45, length:14 assign to ticket200
}
capture line:4, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:46, length:14 assign to ticket201
}
capture line:4, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:47, length:14 assign to ticket202
}
capture line:4, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:48, length:14 assign to ticket203
}
capture line:4, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:49, length:14 assign to ticket204
}
capture line:4, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:50, length:14 assign to ticket205
}
capture line:4, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:51, length:13 assign to ticket206
    capture line:5, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket206
}
capture line:4, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:52, length:12 assign to ticket207
    capture line:5, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket207
}
capture line:4, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:53, length:11 assign to ticket208
    capture line:5, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket208
}
capture line:4, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:54, length:10 assign to ticket209
    capture line:5, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket209
}
capture line:4, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:55, length:9 assign to ticket210
    capture line:5, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket210
}
capture line:4, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:56, length:8 assign to ticket211
    capture line:5, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket211
}
capture line:4, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:57, length:7 assign to ticket212
    capture line:5, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket212
}
capture line:4, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:58, length:6 assign to ticket213
    capture line:5, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket213
}
capture line:4, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:59, length:5 assign to ticket214
    capture line:5, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket214
}
capture line:4, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:60, length:4 assign to ticket215
    capture line:5, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket215
}

capture line:5, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:61, length:3 assign to ticket216
    capture line:5, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket216
}
capture line:5, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:62, length:2 assign to ticket217
    capture line:5, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket217
}
capture line:5, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:4, column:63, length:1 assign to ticket218
    capture line:5, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket218
}
capture line:5, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:2, length:14 assign to ticket219
}
capture line:5, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:3, length:14 assign to ticket220
}
capture line:5, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:4, length:14 assign to ticket221
}
capture line:5, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:5, length:14 assign to ticket222
}
capture line:5, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:6, length:14 assign to ticket223
}
capture line:5, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:7, length:14 assign to ticket224
}
capture line:5, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:8, length:14 assign to ticket225
}
capture line:5, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:9, length:14 assign to ticket226
}
capture line:5, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:10, length:14 assign to ticket227
}
capture line:5, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:11, length:14 assign to ticket228
}
capture line:5, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:12, length:14 assign to ticket229
}
capture line:5, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:13, length:14 assign to ticket230
}
capture line:5, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:14, length:14 assign to ticket231
}
capture line:5, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:15, length:14 assign to ticket232
}
capture line:5, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:16, length:14 assign to ticket233
}
capture line:5, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:17, length:14 assign to ticket234
}
capture line:5, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:18, length:14 assign to ticket235
}
capture line:5, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:19, length:14 assign to ticket236
}
capture line:5, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:20, length:14 assign to ticket237
}
capture line:5, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:21, length:14 assign to ticket238
}
capture line:5, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:22, length:14 assign to ticket239
}
capture line:5, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:23, length:14 assign to ticket240
}
capture line:5, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:24, length:14 assign to ticket241
}
capture line:5, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:25, length:14 assign to ticket242
}
capture line:5, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:26, length:14 assign to ticket243
}
capture line:5, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:27, length:14 assign to ticket244
}
capture line:5, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:28, length:14 assign to ticket245
}
capture line:5, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:29, length:14 assign to ticket246
}
capture line:5, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:30, length:14 assign to ticket247
}
capture line:5, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:31, length:14 assign to ticket248
}
capture line:5, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:32, length:14 assign to ticket249
}
capture line:5, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:33, length:14 assign to ticket250
}
capture line:5, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:34, length:14 assign to ticket251
}
capture line:5, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:35, length:14 assign to ticket252
}
capture line:5, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:36, length:14 assign to ticket253
}
capture line:5, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:37, length:14 assign to ticket254
}
capture line:5, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:38, length:14 assign to ticket255
}
capture line:5, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:39, length:14 assign to ticket256
}
capture line:5, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:40, length:14 assign to ticket257
}
capture line:5, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:41, length:14 assign to ticket258
}
capture line:5, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:42, length:14 assign to ticket259
}
capture line:5, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:43, length:14 assign to ticket260
}
capture line:5, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:44, length:14 assign to ticket261
}
capture line:5, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:45, length:14 assign to ticket262
}
capture line:5, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:46, length:14 assign to ticket263
}
capture line:5, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:47, length:14 assign to ticket264
}
capture line:5, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:48, length:14 assign to ticket265
}
capture line:5, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:49, length:14 assign to ticket266
}
capture line:5, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:50, length:14 assign to ticket267
}
capture line:5, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:51, length:13 assign to ticket268
    capture line:6, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket268
}
capture line:5, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:52, length:12 assign to ticket269
    capture line:6, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket269
}
capture line:5, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:53, length:11 assign to ticket270
    capture line:6, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket270
}
capture line:5, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:54, length:10 assign to ticket271
    capture line:6, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket271
}
capture line:5, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:55, length:9 assign to ticket272
    capture line:6, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket272
}
capture line:5, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:56, length:8 assign to ticket273
    capture line:6, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket273
}
capture line:5, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:57, length:7 assign to ticket274
    capture line:6, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket274
}
capture line:5, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:58, length:6 assign to ticket275
    capture line:6, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket275
}
capture line:5, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:59, length:5 assign to ticket276
    capture line:6, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket276
}
capture line:5, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:60, length:4 assign to ticket277
    capture line:6, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket277
}

capture line:6, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:61, length:3 assign to ticket278
    capture line:6, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket278
}
capture line:6, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:62, length:2 assign to ticket279
    capture line:6, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket279
}
capture line:6, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:5, column:63, length:1 assign to ticket280
    capture line:6, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket280
}
capture line:6, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:2, length:14 assign to ticket281
}
capture line:6, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:3, length:14 assign to ticket282
}
capture line:6, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:4, length:14 assign to ticket283
}
capture line:6, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:5, length:14 assign to ticket284
}
capture line:6, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:6, length:14 assign to ticket285
}
capture line:6, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:7, length:14 assign to ticket286
}
capture line:6, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:8, length:14 assign to ticket287
}
capture line:6, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:9, length:14 assign to ticket288
}
capture line:6, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:10, length:14 assign to ticket289
}
capture line:6, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:11, length:14 assign to ticket290
}
capture line:6, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:12, length:14 assign to ticket291
}
capture line:6, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:13, length:14 assign to ticket292
}
capture line:6, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:14, length:14 assign to ticket293
}
capture line:6, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:15, length:14 assign to ticket294
}
capture line:6, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:16, length:14 assign to ticket295
}
capture line:6, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:17, length:14 assign to ticket296
}
capture line:6, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:18, length:14 assign to ticket297
}
capture line:6, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:19, length:14 assign to ticket298
}
capture line:6, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:20, length:14 assign to ticket299
}
capture line:6, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:21, length:14 assign to ticket300
}
capture line:6, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:22, length:14 assign to ticket301
}
capture line:6, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:23, length:14 assign to ticket302
}
capture line:6, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:24, length:14 assign to ticket303
}
capture line:6, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:25, length:14 assign to ticket304
}
capture line:6, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:26, length:14 assign to ticket305
}
capture line:6, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:27, length:14 assign to ticket306
}
capture line:6, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:28, length:14 assign to ticket307
}
capture line:6, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:29, length:14 assign to ticket308
}
capture line:6, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:30, length:14 assign to ticket309
}
capture line:6, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:31, length:14 assign to ticket310
}
capture line:6, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:32, length:14 assign to ticket311
}
capture line:6, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:33, length:14 assign to ticket312
}
capture line:6, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:34, length:14 assign to ticket313
}
capture line:6, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:35, length:14 assign to ticket314
}
capture line:6, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:36, length:14 assign to ticket315
}
capture line:6, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:37, length:14 assign to ticket316
}
capture line:6, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:38, length:14 assign to ticket317
}
capture line:6, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:39, length:14 assign to ticket318
}
capture line:6, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:40, length:14 assign to ticket319
}
capture line:6, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:41, length:14 assign to ticket320
}
capture line:6, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:42, length:14 assign to ticket321
}
capture line:6, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:43, length:14 assign to ticket322
}
capture line:6, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:44, length:14 assign to ticket323
}
capture line:6, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:45, length:14 assign to ticket324
}
capture line:6, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:46, length:14 assign to ticket325
}
capture line:6, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:47, length:14 assign to ticket326
}
capture line:6, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:48, length:14 assign to ticket327
}
capture line:6, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:49, length:14 assign to ticket328
}
capture line:6, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:50, length:14 assign to ticket329
}
capture line:6, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:51, length:13 assign to ticket330
    capture line:7, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket330
}
capture line:6, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:52, length:12 assign to ticket331
    capture line:7, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket331
}
capture line:6, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:53, length:11 assign to ticket332
    capture line:7, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket332
}
capture line:6, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:54, length:10 assign to ticket333
    capture line:7, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket333
}
capture line:6, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:55, length:9 assign to ticket334
    capture line:7, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket334
}
capture line:6, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:56, length:8 assign to ticket335
    capture line:7, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket335
}
capture line:6, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:57, length:7 assign to ticket336
    capture line:7, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket336
}
capture line:6, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:58, length:6 assign to ticket337
    capture line:7, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket337
}
capture line:6, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:59, length:5 assign to ticket338
    capture line:7, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket338
}
capture line:6, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:60, length:4 assign to ticket339
    capture line:7, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket339
}

capture line:7, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:61, length:3 assign to ticket340
    capture line:7, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket340
}
capture line:7, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:62, length:2 assign to ticket341
    capture line:7, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket341
}
capture line:7, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:6, column:63, length:1 assign to ticket342
    capture line:7, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket342
}
capture line:7, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:2, length:14 assign to ticket343
}
capture line:7, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:3, length:14 assign to ticket344
}
capture line:7, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:4, length:14 assign to ticket345
}
capture line:7, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:5, length:14 assign to ticket346
}
capture line:7, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:6, length:14 assign to ticket347
}
capture line:7, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:7, length:14 assign to ticket348
}
capture line:7, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:8, length:14 assign to ticket349
}
capture line:7, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:9, length:14 assign to ticket350
}
capture line:7, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:10, length:14 assign to ticket351
}
capture line:7, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:11, length:14 assign to ticket352
}
capture line:7, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:12, length:14 assign to ticket353
}
capture line:7, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:13, length:14 assign to ticket354
}
capture line:7, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:14, length:14 assign to ticket355
}
capture line:7, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:15, length:14 assign to ticket356
}
capture line:7, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:16, length:14 assign to ticket357
}
capture line:7, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:17, length:14 assign to ticket358
}
capture line:7, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:18, length:14 assign to ticket359
}
capture line:7, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:19, length:14 assign to ticket360
}
capture line:7, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:20, length:14 assign to ticket361
}
capture line:7, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:21, length:14 assign to ticket362
}
capture line:7, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:22, length:14 assign to ticket363
}
capture line:7, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:23, length:14 assign to ticket364
}
capture line:7, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:24, length:14 assign to ticket365
}
capture line:7, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:25, length:14 assign to ticket366
}
capture line:7, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:26, length:14 assign to ticket367
}
capture line:7, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:27, length:14 assign to ticket368
}
capture line:7, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:28, length:14 assign to ticket369
}
capture line:7, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:29, length:14 assign to ticket370
}
capture line:7, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:30, length:14 assign to ticket371
}
capture line:7, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:31, length:14 assign to ticket372
}
capture line:7, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:32, length:14 assign to ticket373
}
capture line:7, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:33, length:14 assign to ticket374
}
capture line:7, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:34, length:14 assign to ticket375
}
capture line:7, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:35, length:14 assign to ticket376
}
capture line:7, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:36, length:14 assign to ticket377
}
capture line:7, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:37, length:14 assign to ticket378
}
capture line:7, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:38, length:14 assign to ticket379
}
capture line:7, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:39, length:14 assign to ticket380
}
capture line:7, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:40, length:14 assign to ticket381
}
capture line:7, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:41, length:14 assign to ticket382
}
capture line:7, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:42, length:14 assign to ticket383
}
capture line:7, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:43, length:14 assign to ticket384
}
capture line:7, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:44, length:14 assign to ticket385
}
capture line:7, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:45, length:14 assign to ticket386
}
capture line:7, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:46, length:14 assign to ticket387
}
capture line:7, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:47, length:14 assign to ticket388
}
capture line:7, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:48, length:14 assign to ticket389
}
capture line:7, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:49, length:14 assign to ticket390
}
capture line:7, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:50, length:14 assign to ticket391
}
capture line:7, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:51, length:13 assign to ticket392
    capture line:8, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket392
}
capture line:7, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:52, length:12 assign to ticket393
    capture line:8, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket393
}
capture line:7, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:53, length:11 assign to ticket394
    capture line:8, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket394
}
capture line:7, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:54, length:10 assign to ticket395
    capture line:8, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket395
}
capture line:7, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:55, length:9 assign to ticket396
    capture line:8, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket396
}
capture line:7, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:56, length:8 assign to ticket397
    capture line:8, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket397
}
capture line:7, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:57, length:7 assign to ticket398
    capture line:8, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket398
}
capture line:7, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:58, length:6 assign to ticket399
    capture line:8, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket399
}
capture line:7, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:59, length:5 assign to ticket400
    capture line:8, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket400
}
capture line:7, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:60, length:4 assign to ticket401
    capture line:8, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket401
}

capture line:8, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:61, length:3 assign to ticket402
    capture line:8, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket402
}
capture line:8, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:62, length:2 assign to ticket403
    capture line:8, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket403
}
capture line:8, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:7, column:63, length:1 assign to ticket404
    capture line:8, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket404
}
capture line:8, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:2, length:14 assign to ticket405
}
capture line:8, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:3, length:14 assign to ticket406
}
capture line:8, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:4, length:14 assign to ticket407
}
capture line:8, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:5, length:14 assign to ticket408
}
capture line:8, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:6, length:14 assign to ticket409
}
capture line:8, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:7, length:14 assign to ticket410
}
capture line:8, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:8, length:14 assign to ticket411
}
capture line:8, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:9, length:14 assign to ticket412
}
capture line:8, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:10, length:14 assign to ticket413
}
capture line:8, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:11, length:14 assign to ticket414
}
capture line:8, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:12, length:14 assign to ticket415
}
capture line:8, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:13, length:14 assign to ticket416
}
capture line:8, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:14, length:14 assign to ticket417
}
capture line:8, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:15, length:14 assign to ticket418
}
capture line:8, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:16, length:14 assign to ticket419
}
capture line:8, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:17, length:14 assign to ticket420
}
capture line:8, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:18, length:14 assign to ticket421
}
capture line:8, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:19, length:14 assign to ticket422
}
capture line:8, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:20, length:14 assign to ticket423
}
capture line:8, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:21, length:14 assign to ticket424
}
capture line:8, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:22, length:14 assign to ticket425
}
capture line:8, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:23, length:14 assign to ticket426
}
capture line:8, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:24, length:14 assign to ticket427
}
capture line:8, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:25, length:14 assign to ticket428
}
capture line:8, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:26, length:14 assign to ticket429
}
capture line:8, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:27, length:14 assign to ticket430
}
capture line:8, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:28, length:14 assign to ticket431
}
capture line:8, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:29, length:14 assign to ticket432
}
capture line:8, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:30, length:14 assign to ticket433
}
capture line:8, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:31, length:14 assign to ticket434
}
capture line:8, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:32, length:14 assign to ticket435
}
capture line:8, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:33, length:14 assign to ticket436
}
capture line:8, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:34, length:14 assign to ticket437
}
capture line:8, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:35, length:14 assign to ticket438
}
capture line:8, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:36, length:14 assign to ticket439
}
capture line:8, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:37, length:14 assign to ticket440
}
capture line:8, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:38, length:14 assign to ticket441
}
capture line:8, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:39, length:14 assign to ticket442
}
capture line:8, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:40, length:14 assign to ticket443
}
capture line:8, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:41, length:14 assign to ticket444
}
capture line:8, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:42, length:14 assign to ticket445
}
capture line:8, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:43, length:14 assign to ticket446
}
capture line:8, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:44, length:14 assign to ticket447
}
capture line:8, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:45, length:14 assign to ticket448
}
capture line:8, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:46, length:14 assign to ticket449
}
capture line:8, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:47, length:14 assign to ticket450
}
capture line:8, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:48, length:14 assign to ticket451
}
capture line:8, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:49, length:14 assign to ticket452
}
capture line:8, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:50, length:14 assign to ticket453
}
capture line:8, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:51, length:13 assign to ticket454
    capture line:9, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket454
}
capture line:8, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:52, length:12 assign to ticket455
    capture line:9, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket455
}
capture line:8, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:53, length:11 assign to ticket456
    capture line:9, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket456
}
capture line:8, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:54, length:10 assign to ticket457
    capture line:9, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket457
}
capture line:8, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:55, length:9 assign to ticket458
    capture line:9, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket458
}
capture line:8, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:56, length:8 assign to ticket459
    capture line:9, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket459
}
capture line:8, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:57, length:7 assign to ticket460
    capture line:9, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket460
}
capture line:8, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:58, length:6 assign to ticket461
    capture line:9, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket461
}
capture line:8, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:59, length:5 assign to ticket462
    capture line:9, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket462
}
capture line:8, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:60, length:4 assign to ticket463
    capture line:9, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket463
}

capture line:9, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:61, length:3 assign to ticket464
    capture line:9, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket464
}
capture line:9, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:62, length:2 assign to ticket465
    capture line:9, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket465
}
capture line:9, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:8, column:63, length:1 assign to ticket466
    capture line:9, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket466
}
capture line:9, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:2, length:14 assign to ticket467
}
capture line:9, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:3, length:14 assign to ticket468
}
capture line:9, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:4, length:14 assign to ticket469
}
capture line:9, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:5, length:14 assign to ticket470
}
capture line:9, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:6, length:14 assign to ticket471
}
capture line:9, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:7, length:14 assign to ticket472
}
capture line:9, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:8, length:14 assign to ticket473
}
capture line:9, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:9, length:14 assign to ticket474
}
capture line:9, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:10, length:14 assign to ticket475
}
capture line:9, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:11, length:14 assign to ticket476
}
capture line:9, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:12, length:14 assign to ticket477
}
capture line:9, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:13, length:14 assign to ticket478
}
capture line:9, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:14, length:14 assign to ticket479
}
capture line:9, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:15, length:14 assign to ticket480
}
capture line:9, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:16, length:14 assign to ticket481
}
capture line:9, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:17, length:14 assign to ticket482
}
capture line:9, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:18, length:14 assign to ticket483
}
capture line:9, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:19, length:14 assign to ticket484
}
capture line:9, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:20, length:14 assign to ticket485
}
capture line:9, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:21, length:14 assign to ticket486
}
capture line:9, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:22, length:14 assign to ticket487
}
capture line:9, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:23, length:14 assign to ticket488
}
capture line:9, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:24, length:14 assign to ticket489
}
capture line:9, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:25, length:14 assign to ticket490
}
capture line:9, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:26, length:14 assign to ticket491
}
capture line:9, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:27, length:14 assign to ticket492
}
capture line:9, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:28, length:14 assign to ticket493
}
capture line:9, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:29, length:14 assign to ticket494
}
capture line:9, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:30, length:14 assign to ticket495
}
capture line:9, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:31, length:14 assign to ticket496
}
capture line:9, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:32, length:14 assign to ticket497
}
capture line:9, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:33, length:14 assign to ticket498
}
capture line:9, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:34, length:14 assign to ticket499
}
capture line:9, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:35, length:14 assign to ticket500
}
capture line:9, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:36, length:14 assign to ticket501
}
capture line:9, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:37, length:14 assign to ticket502
}
capture line:9, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:38, length:14 assign to ticket503
}
capture line:9, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:39, length:14 assign to ticket504
}
capture line:9, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:40, length:14 assign to ticket505
}
capture line:9, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:41, length:14 assign to ticket506
}
capture line:9, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:42, length:14 assign to ticket507
}
capture line:9, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:43, length:14 assign to ticket508
}
capture line:9, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:44, length:14 assign to ticket509
}
capture line:9, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:45, length:14 assign to ticket510
}
capture line:9, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:46, length:14 assign to ticket511
}
capture line:9, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:47, length:14 assign to ticket512
}
capture line:9, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:48, length:14 assign to ticket513
}
capture line:9, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:49, length:14 assign to ticket514
}
capture line:9, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:50, length:14 assign to ticket515
}
capture line:9, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:51, length:13 assign to ticket516
    capture line:10, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket516
}
capture line:9, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:52, length:12 assign to ticket517
    capture line:10, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket517
}
capture line:9, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:53, length:11 assign to ticket518
    capture line:10, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket518
}
capture line:9, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:54, length:10 assign to ticket519
    capture line:10, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket519
}
capture line:9, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:55, length:9 assign to ticket520
    capture line:10, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket520
}
capture line:9, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:56, length:8 assign to ticket521
    capture line:10, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket521
}
capture line:9, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:57, length:7 assign to ticket522
    capture line:10, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket522
}
capture line:9, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:58, length:6 assign to ticket523
    capture line:10, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket523
}
capture line:9, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:59, length:5 assign to ticket524
    capture line:10, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket524
}
capture line:9, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:60, length:4 assign to ticket525
    capture line:10, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket525
}

capture line:10, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:61, length:3 assign to ticket526
    capture line:10, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket526
}
capture line:10, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:62, length:2 assign to ticket527
    capture line:10, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket527
}
capture line:10, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:9, column:63, length:1 assign to ticket528
    capture line:10, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket528
}
capture line:10, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:2, length:14 assign to ticket529
}
capture line:10, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:3, length:14 assign to ticket530
}
capture line:10, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:4, length:14 assign to ticket531
}
capture line:10, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:5, length:14 assign to ticket532
}
capture line:10, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:6, length:14 assign to ticket533
}
capture line:10, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:7, length:14 assign to ticket534
}
capture line:10, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:8, length:14 assign to ticket535
}
capture line:10, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:9, length:14 assign to ticket536
}
capture line:10, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:10, length:14 assign to ticket537
}
capture line:10, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:11, length:14 assign to ticket538
}
capture line:10, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:12, length:14 assign to ticket539
}
capture line:10, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:13, length:14 assign to ticket540
}
capture line:10, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:14, length:14 assign to ticket541
}
capture line:10, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:15, length:14 assign to ticket542
}
capture line:10, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:16, length:14 assign to ticket543
}
capture line:10, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:17, length:14 assign to ticket544
}
capture line:10, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:18, length:14 assign to ticket545
}
capture line:10, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:19, length:14 assign to ticket546
}
capture line:10, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:20, length:14 assign to ticket547
}
capture line:10, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:21, length:14 assign to ticket548
}
capture line:10, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:22, length:14 assign to ticket549
}
capture line:10, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:23, length:14 assign to ticket550
}
capture line:10, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:24, length:14 assign to ticket551
}
capture line:10, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:25, length:14 assign to ticket552
}
capture line:10, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:26, length:14 assign to ticket553
}
capture line:10, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:27, length:14 assign to ticket554
}
capture line:10, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:28, length:14 assign to ticket555
}
capture line:10, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:29, length:14 assign to ticket556
}
capture line:10, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:30, length:14 assign to ticket557
}
capture line:10, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:31, length:14 assign to ticket558
}
capture line:10, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:32, length:14 assign to ticket559
}
capture line:10, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:33, length:14 assign to ticket560
}
capture line:10, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:34, length:14 assign to ticket561
}
capture line:10, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:35, length:14 assign to ticket562
}
capture line:10, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:36, length:14 assign to ticket563
}
capture line:10, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:37, length:14 assign to ticket564
}
capture line:10, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:38, length:14 assign to ticket565
}
capture line:10, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:39, length:14 assign to ticket566
}
capture line:10, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:40, length:14 assign to ticket567
}
capture line:10, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:41, length:14 assign to ticket568
}
capture line:10, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:42, length:14 assign to ticket569
}
capture line:10, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:43, length:14 assign to ticket570
}
capture line:10, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:44, length:14 assign to ticket571
}
capture line:10, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:45, length:14 assign to ticket572
}
capture line:10, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:46, length:14 assign to ticket573
}
capture line:10, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:47, length:14 assign to ticket574
}
capture line:10, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:48, length:14 assign to ticket575
}
capture line:10, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:49, length:14 assign to ticket576
}
capture line:10, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:50, length:14 assign to ticket577
}
capture line:10, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:51, length:13 assign to ticket578
    capture line:11, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket578
}
capture line:10, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:52, length:12 assign to ticket579
    capture line:11, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket579
}
capture line:10, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:53, length:11 assign to ticket580
    capture line:11, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket580
}
capture line:10, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:54, length:10 assign to ticket581
    capture line:11, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket581
}
capture line:10, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:55, length:9 assign to ticket582
    capture line:11, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket582
}
capture line:10, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:56, length:8 assign to ticket583
    capture line:11, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket583
}
capture line:10, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:57, length:7 assign to ticket584
    capture line:11, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket584
}
capture line:10, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:58, length:6 assign to ticket585
    capture line:11, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket585
}
capture line:10, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:59, length:5 assign to ticket586
    capture line:11, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket586
}
capture line:10, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:60, length:4 assign to ticket587
    capture line:11, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket587
}

capture line:11, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:61, length:3 assign to ticket588
    capture line:11, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket588
}
capture line:11, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:62, length:2 assign to ticket589
    capture line:11, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket589
}
capture line:11, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:10, column:63, length:1 assign to ticket590
    capture line:11, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket590
}
capture line:11, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:2, length:14 assign to ticket591
}
capture line:11, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:3, length:14 assign to ticket592
}
capture line:11, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:4, length:14 assign to ticket593
}
capture line:11, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:5, length:14 assign to ticket594
}
capture line:11, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:6, length:14 assign to ticket595
}
capture line:11, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:7, length:14 assign to ticket596
}
capture line:11, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:8, length:14 assign to ticket597
}
capture line:11, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:9, length:14 assign to ticket598
}
capture line:11, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:10, length:14 assign to ticket599
}
capture line:11, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:11, length:14 assign to ticket600
}
capture line:11, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:12, length:14 assign to ticket601
}
capture line:11, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:13, length:14 assign to ticket602
}
capture line:11, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:14, length:14 assign to ticket603
}
capture line:11, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:15, length:14 assign to ticket604
}
capture line:11, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:16, length:14 assign to ticket605
}
capture line:11, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:17, length:14 assign to ticket606
}
capture line:11, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:18, length:14 assign to ticket607
}
capture line:11, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:19, length:14 assign to ticket608
}
capture line:11, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:20, length:14 assign to ticket609
}
capture line:11, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:21, length:14 assign to ticket610
}
capture line:11, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:22, length:14 assign to ticket611
}
capture line:11, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:23, length:14 assign to ticket612
}
capture line:11, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:24, length:14 assign to ticket613
}
capture line:11, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:25, length:14 assign to ticket614
}
capture line:11, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:26, length:14 assign to ticket615
}
capture line:11, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:27, length:14 assign to ticket616
}
capture line:11, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:28, length:14 assign to ticket617
}
capture line:11, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:29, length:14 assign to ticket618
}
capture line:11, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:30, length:14 assign to ticket619
}
capture line:11, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:31, length:14 assign to ticket620
}
capture line:11, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:32, length:14 assign to ticket621
}
capture line:11, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:33, length:14 assign to ticket622
}
capture line:11, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:34, length:14 assign to ticket623
}
capture line:11, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:35, length:14 assign to ticket624
}
capture line:11, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:36, length:14 assign to ticket625
}
capture line:11, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:37, length:14 assign to ticket626
}
capture line:11, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:38, length:14 assign to ticket627
}
capture line:11, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:39, length:14 assign to ticket628
}
capture line:11, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:40, length:14 assign to ticket629
}
capture line:11, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:41, length:14 assign to ticket630
}
capture line:11, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:42, length:14 assign to ticket631
}
capture line:11, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:43, length:14 assign to ticket632
}
capture line:11, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:44, length:14 assign to ticket633
}
capture line:11, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:45, length:14 assign to ticket634
}
capture line:11, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:46, length:14 assign to ticket635
}
capture line:11, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:47, length:14 assign to ticket636
}
capture line:11, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:48, length:14 assign to ticket637
}
capture line:11, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:49, length:14 assign to ticket638
}
capture line:11, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:50, length:14 assign to ticket639
}
capture line:11, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:51, length:13 assign to ticket640
    capture line:12, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket640
}
capture line:11, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:52, length:12 assign to ticket641
    capture line:12, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket641
}
capture line:11, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:53, length:11 assign to ticket642
    capture line:12, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket642
}
capture line:11, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:54, length:10 assign to ticket643
    capture line:12, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket643
}
capture line:11, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:55, length:9 assign to ticket644
    capture line:12, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket644
}
capture line:11, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:56, length:8 assign to ticket645
    capture line:12, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket645
}
capture line:11, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:57, length:7 assign to ticket646
    capture line:12, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket646
}
capture line:11, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:58, length:6 assign to ticket647
    capture line:12, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket647
}
capture line:11, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:59, length:5 assign to ticket648
    capture line:12, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket648
}
capture line:11, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:60, length:4 assign to ticket649
    capture line:12, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket649
}

capture line:12, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:61, length:3 assign to ticket650
    capture line:12, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket650
}
capture line:12, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:62, length:2 assign to ticket651
    capture line:12, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket651
}
capture line:12, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:11, column:63, length:1 assign to ticket652
    capture line:12, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket652
}
capture line:12, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:2, length:14 assign to ticket653
}
capture line:12, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:3, length:14 assign to ticket654
}
capture line:12, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:4, length:14 assign to ticket655
}
capture line:12, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:5, length:14 assign to ticket656
}
capture line:12, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:6, length:14 assign to ticket657
}
capture line:12, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:7, length:14 assign to ticket658
}
capture line:12, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:8, length:14 assign to ticket659
}
capture line:12, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:9, length:14 assign to ticket660
}
capture line:12, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:10, length:14 assign to ticket661
}
capture line:12, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:11, length:14 assign to ticket662
}
capture line:12, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:12, length:14 assign to ticket663
}
capture line:12, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:13, length:14 assign to ticket664
}
capture line:12, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:14, length:14 assign to ticket665
}
capture line:12, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:15, length:14 assign to ticket666
}
capture line:12, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:16, length:14 assign to ticket667
}
capture line:12, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:17, length:14 assign to ticket668
}
capture line:12, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:18, length:14 assign to ticket669
}
capture line:12, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:19, length:14 assign to ticket670
}
capture line:12, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:20, length:14 assign to ticket671
}
capture line:12, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:21, length:14 assign to ticket672
}
capture line:12, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:22, length:14 assign to ticket673
}
capture line:12, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:23, length:14 assign to ticket674
}
capture line:12, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:24, length:14 assign to ticket675
}
capture line:12, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:25, length:14 assign to ticket676
}
capture line:12, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:26, length:14 assign to ticket677
}
capture line:12, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:27, length:14 assign to ticket678
}
capture line:12, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:28, length:14 assign to ticket679
}
capture line:12, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:29, length:14 assign to ticket680
}
capture line:12, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:30, length:14 assign to ticket681
}
capture line:12, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:31, length:14 assign to ticket682
}
capture line:12, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:32, length:14 assign to ticket683
}
capture line:12, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:33, length:14 assign to ticket684
}
capture line:12, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:34, length:14 assign to ticket685
}
capture line:12, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:35, length:14 assign to ticket686
}
capture line:12, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:36, length:14 assign to ticket687
}
capture line:12, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:37, length:14 assign to ticket688
}
capture line:12, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:38, length:14 assign to ticket689
}
capture line:12, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:39, length:14 assign to ticket690
}
capture line:12, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:40, length:14 assign to ticket691
}
capture line:12, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:41, length:14 assign to ticket692
}
capture line:12, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:42, length:14 assign to ticket693
}
capture line:12, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:43, length:14 assign to ticket694
}
capture line:12, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:44, length:14 assign to ticket695
}
capture line:12, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:45, length:14 assign to ticket696
}
capture line:12, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:46, length:14 assign to ticket697
}
capture line:12, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:47, length:14 assign to ticket698
}
capture line:12, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:48, length:14 assign to ticket699
}
capture line:12, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:49, length:14 assign to ticket700
}
capture line:12, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:50, length:14 assign to ticket701
}
capture line:12, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:51, length:13 assign to ticket702
    capture line:13, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket702
}
capture line:12, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:52, length:12 assign to ticket703
    capture line:13, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket703
}
capture line:12, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:53, length:11 assign to ticket704
    capture line:13, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket704
}
capture line:12, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:54, length:10 assign to ticket705
    capture line:13, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket705
}
capture line:12, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:55, length:9 assign to ticket706
    capture line:13, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket706
}
capture line:12, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:56, length:8 assign to ticket707
    capture line:13, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket707
}
capture line:12, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:57, length:7 assign to ticket708
    capture line:13, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket708
}
capture line:12, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:58, length:6 assign to ticket709
    capture line:13, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket709
}
capture line:12, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:59, length:5 assign to ticket710
    capture line:13, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket710
}
capture line:12, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:60, length:4 assign to ticket711
    capture line:13, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket711
}

capture line:13, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:61, length:3 assign to ticket712
    capture line:13, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket712
}
capture line:13, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:62, length:2 assign to ticket713
    capture line:13, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket713
}
capture line:13, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:12, column:63, length:1 assign to ticket714
    capture line:13, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket714
}
capture line:13, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:2, length:14 assign to ticket715
}
capture line:13, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:3, length:14 assign to ticket716
}
capture line:13, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:4, length:14 assign to ticket717
}
capture line:13, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:5, length:14 assign to ticket718
}
capture line:13, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:6, length:14 assign to ticket719
}
capture line:13, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:7, length:14 assign to ticket720
}
capture line:13, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:8, length:14 assign to ticket721
}
capture line:13, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:9, length:14 assign to ticket722
}
capture line:13, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:10, length:14 assign to ticket723
}
capture line:13, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:11, length:14 assign to ticket724
}
capture line:13, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:12, length:14 assign to ticket725
}
capture line:13, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:13, length:14 assign to ticket726
}
capture line:13, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:14, length:14 assign to ticket727
}
capture line:13, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:15, length:14 assign to ticket728
}
capture line:13, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:16, length:14 assign to ticket729
}
capture line:13, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:17, length:14 assign to ticket730
}
capture line:13, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:18, length:14 assign to ticket731
}
capture line:13, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:19, length:14 assign to ticket732
}
capture line:13, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:20, length:14 assign to ticket733
}
capture line:13, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:21, length:14 assign to ticket734
}
capture line:13, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:22, length:14 assign to ticket735
}
capture line:13, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:23, length:14 assign to ticket736
}
capture line:13, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:24, length:14 assign to ticket737
}
capture line:13, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:25, length:14 assign to ticket738
}
capture line:13, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:26, length:14 assign to ticket739
}
capture line:13, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:27, length:14 assign to ticket740
}
capture line:13, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:28, length:14 assign to ticket741
}
capture line:13, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:29, length:14 assign to ticket742
}
capture line:13, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:30, length:14 assign to ticket743
}
capture line:13, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:31, length:14 assign to ticket744
}
capture line:13, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:32, length:14 assign to ticket745
}
capture line:13, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:33, length:14 assign to ticket746
}
capture line:13, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:34, length:14 assign to ticket747
}
capture line:13, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:35, length:14 assign to ticket748
}
capture line:13, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:36, length:14 assign to ticket749
}
capture line:13, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:37, length:14 assign to ticket750
}
capture line:13, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:38, length:14 assign to ticket751
}
capture line:13, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:39, length:14 assign to ticket752
}
capture line:13, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:40, length:14 assign to ticket753
}
capture line:13, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:41, length:14 assign to ticket754
}
capture line:13, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:42, length:14 assign to ticket755
}
capture line:13, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:43, length:14 assign to ticket756
}
capture line:13, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:44, length:14 assign to ticket757
}
capture line:13, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:45, length:14 assign to ticket758
}
capture line:13, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:46, length:14 assign to ticket759
}
capture line:13, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:47, length:14 assign to ticket760
}
capture line:13, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:48, length:14 assign to ticket761
}
capture line:13, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:49, length:14 assign to ticket762
}
capture line:13, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:50, length:14 assign to ticket763
}
capture line:13, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:51, length:13 assign to ticket764
    capture line:14, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket764
}
capture line:13, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:52, length:12 assign to ticket765
    capture line:14, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket765
}
capture line:13, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:53, length:11 assign to ticket766
    capture line:14, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket766
}
capture line:13, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:54, length:10 assign to ticket767
    capture line:14, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket767
}
capture line:13, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:55, length:9 assign to ticket768
    capture line:14, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket768
}
capture line:13, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:56, length:8 assign to ticket769
    capture line:14, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket769
}
capture line:13, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:57, length:7 assign to ticket770
    capture line:14, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket770
}
capture line:13, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:58, length:6 assign to ticket771
    capture line:14, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket771
}
capture line:13, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:59, length:5 assign to ticket772
    capture line:14, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket772
}
capture line:13, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:60, length:4 assign to ticket773
    capture line:14, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket773
}

capture line:14, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:61, length:3 assign to ticket774
    capture line:14, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket774
}
capture line:14, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:62, length:2 assign to ticket775
    capture line:14, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket775
}
capture line:14, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:13, column:63, length:1 assign to ticket776
    capture line:14, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket776
}
capture line:14, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:2, length:14 assign to ticket777
}
capture line:14, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:3, length:14 assign to ticket778
}
capture line:14, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:4, length:14 assign to ticket779
}
capture line:14, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:5, length:14 assign to ticket780
}
capture line:14, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:6, length:14 assign to ticket781
}
capture line:14, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:7, length:14 assign to ticket782
}
capture line:14, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:8, length:14 assign to ticket783
}
capture line:14, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:9, length:14 assign to ticket784
}
capture line:14, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:10, length:14 assign to ticket785
}
capture line:14, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:11, length:14 assign to ticket786
}
capture line:14, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:12, length:14 assign to ticket787
}
capture line:14, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:13, length:14 assign to ticket788
}
capture line:14, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:14, length:14 assign to ticket789
}
capture line:14, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:15, length:14 assign to ticket790
}
capture line:14, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:16, length:14 assign to ticket791
}
capture line:14, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:17, length:14 assign to ticket792
}
capture line:14, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:18, length:14 assign to ticket793
}
capture line:14, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:19, length:14 assign to ticket794
}
capture line:14, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:20, length:14 assign to ticket795
}
capture line:14, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:21, length:14 assign to ticket796
}
capture line:14, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:22, length:14 assign to ticket797
}
capture line:14, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:23, length:14 assign to ticket798
}
capture line:14, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:24, length:14 assign to ticket799
}
capture line:14, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:25, length:14 assign to ticket800
}
capture line:14, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:26, length:14 assign to ticket801
}
capture line:14, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:27, length:14 assign to ticket802
}
capture line:14, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:28, length:14 assign to ticket803
}
capture line:14, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:29, length:14 assign to ticket804
}
capture line:14, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:30, length:14 assign to ticket805
}
capture line:14, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:31, length:14 assign to ticket806
}
capture line:14, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:32, length:14 assign to ticket807
}
capture line:14, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:33, length:14 assign to ticket808
}
capture line:14, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:34, length:14 assign to ticket809
}
capture line:14, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:35, length:14 assign to ticket810
}
capture line:14, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:36, length:14 assign to ticket811
}
capture line:14, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:37, length:14 assign to ticket812
}
capture line:14, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:38, length:14 assign to ticket813
}
capture line:14, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:39, length:14 assign to ticket814
}
capture line:14, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:40, length:14 assign to ticket815
}
capture line:14, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:41, length:14 assign to ticket816
}
capture line:14, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:42, length:14 assign to ticket817
}
capture line:14, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:43, length:14 assign to ticket818
}
capture line:14, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:44, length:14 assign to ticket819
}
capture line:14, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:45, length:14 assign to ticket820
}
capture line:14, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:46, length:14 assign to ticket821
}
capture line:14, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:47, length:14 assign to ticket822
}
capture line:14, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:48, length:14 assign to ticket823
}
capture line:14, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:49, length:14 assign to ticket824
}
capture line:14, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:50, length:14 assign to ticket825
}
capture line:14, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:51, length:13 assign to ticket826
    capture line:15, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket826
}
capture line:14, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:52, length:12 assign to ticket827
    capture line:15, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket827
}
capture line:14, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:53, length:11 assign to ticket828
    capture line:15, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket828
}
capture line:14, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:54, length:10 assign to ticket829
    capture line:15, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket829
}
capture line:14, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:55, length:9 assign to ticket830
    capture line:15, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket830
}
capture line:14, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:56, length:8 assign to ticket831
    capture line:15, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket831
}
capture line:14, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:57, length:7 assign to ticket832
    capture line:15, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket832
}
capture line:14, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:58, length:6 assign to ticket833
    capture line:15, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket833
}
capture line:14, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:59, length:5 assign to ticket834
    capture line:15, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket834
}
capture line:14, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:60, length:4 assign to ticket835
    capture line:15, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket835
}

capture line:15, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:61, length:3 assign to ticket836
    capture line:15, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket836
}
capture line:15, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:62, length:2 assign to ticket837
    capture line:15, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket837
}
capture line:15, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:14, column:63, length:1 assign to ticket838
    capture line:15, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket838
}
capture line:15, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:2, length:14 assign to ticket839
}
capture line:15, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:3, length:14 assign to ticket840
}
capture line:15, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:4, length:14 assign to ticket841
}
capture line:15, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:5, length:14 assign to ticket842
}
capture line:15, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:6, length:14 assign to ticket843
}
capture line:15, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:7, length:14 assign to ticket844
}
capture line:15, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:8, length:14 assign to ticket845
}
capture line:15, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:9, length:14 assign to ticket846
}
capture line:15, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:10, length:14 assign to ticket847
}
capture line:15, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:11, length:14 assign to ticket848
}
capture line:15, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:12, length:14 assign to ticket849
}
capture line:15, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:13, length:14 assign to ticket850
}
capture line:15, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:14, length:14 assign to ticket851
}
capture line:15, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:15, length:14 assign to ticket852
}
capture line:15, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:16, length:14 assign to ticket853
}
capture line:15, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:17, length:14 assign to ticket854
}
capture line:15, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:18, length:14 assign to ticket855
}
capture line:15, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:19, length:14 assign to ticket856
}
capture line:15, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:20, length:14 assign to ticket857
}
capture line:15, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:21, length:14 assign to ticket858
}
capture line:15, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:22, length:14 assign to ticket859
}
capture line:15, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:23, length:14 assign to ticket860
}
capture line:15, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:24, length:14 assign to ticket861
}
capture line:15, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:25, length:14 assign to ticket862
}
capture line:15, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:26, length:14 assign to ticket863
}
capture line:15, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:27, length:14 assign to ticket864
}
capture line:15, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:28, length:14 assign to ticket865
}
capture line:15, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:29, length:14 assign to ticket866
}
capture line:15, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:30, length:14 assign to ticket867
}
capture line:15, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:31, length:14 assign to ticket868
}
capture line:15, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:32, length:14 assign to ticket869
}
capture line:15, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:33, length:14 assign to ticket870
}
capture line:15, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:34, length:14 assign to ticket871
}
capture line:15, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:35, length:14 assign to ticket872
}
capture line:15, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:36, length:14 assign to ticket873
}
capture line:15, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:37, length:14 assign to ticket874
}
capture line:15, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:38, length:14 assign to ticket875
}
capture line:15, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:39, length:14 assign to ticket876
}
capture line:15, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:40, length:14 assign to ticket877
}
capture line:15, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:41, length:14 assign to ticket878
}
capture line:15, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:42, length:14 assign to ticket879
}
capture line:15, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:43, length:14 assign to ticket880
}
capture line:15, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:44, length:14 assign to ticket881
}
capture line:15, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:45, length:14 assign to ticket882
}
capture line:15, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:46, length:14 assign to ticket883
}
capture line:15, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:47, length:14 assign to ticket884
}
capture line:15, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:48, length:14 assign to ticket885
}
capture line:15, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:49, length:14 assign to ticket886
}
capture line:15, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:50, length:14 assign to ticket887
}
capture line:15, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:51, length:13 assign to ticket888
    capture line:16, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket888
}
capture line:15, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:52, length:12 assign to ticket889
    capture line:16, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket889
}
capture line:15, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:53, length:11 assign to ticket890
    capture line:16, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket890
}
capture line:15, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:54, length:10 assign to ticket891
    capture line:16, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket891
}
capture line:15, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:55, length:9 assign to ticket892
    capture line:16, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket892
}
capture line:15, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:56, length:8 assign to ticket893
    capture line:16, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket893
}
capture line:15, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:57, length:7 assign to ticket894
    capture line:16, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket894
}
capture line:15, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:58, length:6 assign to ticket895
    capture line:16, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket895
}
capture line:15, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:59, length:5 assign to ticket896
    capture line:16, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket896
}
capture line:15, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:60, length:4 assign to ticket897
    capture line:16, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket897
}

capture line:16, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:61, length:3 assign to ticket898
    capture line:16, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket898
}
capture line:16, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:62, length:2 assign to ticket899
    capture line:16, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket899
}
capture line:16, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:15, column:63, length:1 assign to ticket900
    capture line:16, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket900
}
capture line:16, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:2, length:14 assign to ticket901
}
capture line:16, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:3, length:14 assign to ticket902
}
capture line:16, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:4, length:14 assign to ticket903
}
capture line:16, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:5, length:14 assign to ticket904
}
capture line:16, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:6, length:14 assign to ticket905
}
capture line:16, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:7, length:14 assign to ticket906
}
capture line:16, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:8, length:14 assign to ticket907
}
capture line:16, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:9, length:14 assign to ticket908
}
capture line:16, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:10, length:14 assign to ticket909
}
capture line:16, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:11, length:14 assign to ticket910
}
capture line:16, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:12, length:14 assign to ticket911
}
capture line:16, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:13, length:14 assign to ticket912
}
capture line:16, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:14, length:14 assign to ticket913
}
capture line:16, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:15, length:14 assign to ticket914
}
capture line:16, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:16, length:14 assign to ticket915
}
capture line:16, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:17, length:14 assign to ticket916
}
capture line:16, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:18, length:14 assign to ticket917
}
capture line:16, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:19, length:14 assign to ticket918
}
capture line:16, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:20, length:14 assign to ticket919
}
capture line:16, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:21, length:14 assign to ticket920
}
capture line:16, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:22, length:14 assign to ticket921
}
capture line:16, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:23, length:14 assign to ticket922
}
capture line:16, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:24, length:14 assign to ticket923
}
capture line:16, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:25, length:14 assign to ticket924
}
capture line:16, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:26, length:14 assign to ticket925
}
capture line:16, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:27, length:14 assign to ticket926
}
capture line:16, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:28, length:14 assign to ticket927
}
capture line:16, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:29, length:14 assign to ticket928
}
capture line:16, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:30, length:14 assign to ticket929
}
capture line:16, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:31, length:14 assign to ticket930
}
capture line:16, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:32, length:14 assign to ticket931
}
capture line:16, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:33, length:14 assign to ticket932
}
capture line:16, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:34, length:14 assign to ticket933
}
capture line:16, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:35, length:14 assign to ticket934
}
capture line:16, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:36, length:14 assign to ticket935
}
capture line:16, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:37, length:14 assign to ticket936
}
capture line:16, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:38, length:14 assign to ticket937
}
capture line:16, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:39, length:14 assign to ticket938
}
capture line:16, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:40, length:14 assign to ticket939
}
capture line:16, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:41, length:14 assign to ticket940
}
capture line:16, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:42, length:14 assign to ticket941
}
capture line:16, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:43, length:14 assign to ticket942
}
capture line:16, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:44, length:14 assign to ticket943
}
capture line:16, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:45, length:14 assign to ticket944
}
capture line:16, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:46, length:14 assign to ticket945
}
capture line:16, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:47, length:14 assign to ticket946
}
capture line:16, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:48, length:14 assign to ticket947
}
capture line:16, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:49, length:14 assign to ticket948
}
capture line:16, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:50, length:14 assign to ticket949
}
capture line:16, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:51, length:13 assign to ticket950
    capture line:17, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket950
}
capture line:16, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:52, length:12 assign to ticket951
    capture line:17, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket951
}
capture line:16, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:53, length:11 assign to ticket952
    capture line:17, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket952
}
capture line:16, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:54, length:10 assign to ticket953
    capture line:17, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket953
}
capture line:16, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:55, length:9 assign to ticket954
    capture line:17, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket954
}
capture line:16, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:56, length:8 assign to ticket955
    capture line:17, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket955
}
capture line:16, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:57, length:7 assign to ticket956
    capture line:17, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket956
}
capture line:16, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:58, length:6 assign to ticket957
    capture line:17, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket957
}
capture line:16, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:59, length:5 assign to ticket958
    capture line:17, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket958
}
capture line:16, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:60, length:4 assign to ticket959
    capture line:17, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket959
}

capture line:17, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:61, length:3 assign to ticket960
    capture line:17, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket960
}
capture line:17, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:62, length:2 assign to ticket961
    capture line:17, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket961
}
capture line:17, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:16, column:63, length:1 assign to ticket962
    capture line:17, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket962
}
capture line:17, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:2, length:14 assign to ticket963
}
capture line:17, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:3, length:14 assign to ticket964
}
capture line:17, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:4, length:14 assign to ticket965
}
capture line:17, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:5, length:14 assign to ticket966
}
capture line:17, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:6, length:14 assign to ticket967
}
capture line:17, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:7, length:14 assign to ticket968
}
capture line:17, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:8, length:14 assign to ticket969
}
capture line:17, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:9, length:14 assign to ticket970
}
capture line:17, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:10, length:14 assign to ticket971
}
capture line:17, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:11, length:14 assign to ticket972
}
capture line:17, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:12, length:14 assign to ticket973
}
capture line:17, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:13, length:14 assign to ticket974
}
capture line:17, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:14, length:14 assign to ticket975
}
capture line:17, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:15, length:14 assign to ticket976
}
capture line:17, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:16, length:14 assign to ticket977
}
capture line:17, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:17, length:14 assign to ticket978
}
capture line:17, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:18, length:14 assign to ticket979
}
capture line:17, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:19, length:14 assign to ticket980
}
capture line:17, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:20, length:14 assign to ticket981
}
capture line:17, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:21, length:14 assign to ticket982
}
capture line:17, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:22, length:14 assign to ticket983
}
capture line:17, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:23, length:14 assign to ticket984
}
capture line:17, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:24, length:14 assign to ticket985
}
capture line:17, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:25, length:14 assign to ticket986
}
capture line:17, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:26, length:14 assign to ticket987
}
capture line:17, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:27, length:14 assign to ticket988
}
capture line:17, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:28, length:14 assign to ticket989
}
capture line:17, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:29, length:14 assign to ticket990
}
capture line:17, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:30, length:14 assign to ticket991
}
capture line:17, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:31, length:14 assign to ticket992
}
capture line:17, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:32, length:14 assign to ticket993
}
capture line:17, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:33, length:14 assign to ticket994
}
capture line:17, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:34, length:14 assign to ticket995
}
capture line:17, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:35, length:14 assign to ticket996
}
capture line:17, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:36, length:14 assign to ticket997
}
capture line:17, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:37, length:14 assign to ticket998
}
capture line:17, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:38, length:14 assign to ticket999
}
capture line:17, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:39, length:14 assign to ticket1000
}
capture line:17, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:40, length:14 assign to ticket1001
}
capture line:17, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:41, length:14 assign to ticket1002
}
capture line:17, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:42, length:14 assign to ticket1003
}
capture line:17, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:43, length:14 assign to ticket1004
}
capture line:17, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:44, length:14 assign to ticket1005
}
capture line:17, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:45, length:14 assign to ticket1006
}
capture line:17, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:46, length:14 assign to ticket1007
}
capture line:17, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:47, length:14 assign to ticket1008
}
capture line:17, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:48, length:14 assign to ticket1009
}
capture line:17, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:49, length:14 assign to ticket1010
}
capture line:17, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:50, length:14 assign to ticket1011
}
capture line:17, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:51, length:13 assign to ticket1012
    capture line:18, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1012
}
capture line:17, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:52, length:12 assign to ticket1013
    capture line:18, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1013
}
capture line:17, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:53, length:11 assign to ticket1014
    capture line:18, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1014
}
capture line:17, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:54, length:10 assign to ticket1015
    capture line:18, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1015
}
capture line:17, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:55, length:9 assign to ticket1016
    capture line:18, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1016
}
capture line:17, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:56, length:8 assign to ticket1017
    capture line:18, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1017
}
capture line:17, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:57, length:7 assign to ticket1018
    capture line:18, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1018
}
capture line:17, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:58, length:6 assign to ticket1019
    capture line:18, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1019
}
capture line:17, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:59, length:5 assign to ticket1020
    capture line:18, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1020
}
capture line:17, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:60, length:4 assign to ticket1021
    capture line:18, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1021
}

capture line:18, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:61, length:3 assign to ticket1022
    capture line:18, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1022
}
capture line:18, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:62, length:2 assign to ticket1023
    capture line:18, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1023
}
capture line:18, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:17, column:63, length:1 assign to ticket1024
    capture line:18, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1024
}
capture line:18, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:2, length:14 assign to ticket1025
}
capture line:18, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:3, length:14 assign to ticket1026
}
capture line:18, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:4, length:14 assign to ticket1027
}
capture line:18, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:5, length:14 assign to ticket1028
}
capture line:18, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:6, length:14 assign to ticket1029
}
capture line:18, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:7, length:14 assign to ticket1030
}
capture line:18, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:8, length:14 assign to ticket1031
}
capture line:18, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:9, length:14 assign to ticket1032
}
capture line:18, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:10, length:14 assign to ticket1033
}
capture line:18, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:11, length:14 assign to ticket1034
}
capture line:18, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:12, length:14 assign to ticket1035
}
capture line:18, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:13, length:14 assign to ticket1036
}
capture line:18, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:14, length:14 assign to ticket1037
}
capture line:18, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:15, length:14 assign to ticket1038
}
capture line:18, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:16, length:14 assign to ticket1039
}
capture line:18, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:17, length:14 assign to ticket1040
}
capture line:18, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:18, length:14 assign to ticket1041
}
capture line:18, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:19, length:14 assign to ticket1042
}
capture line:18, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:20, length:14 assign to ticket1043
}
capture line:18, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:21, length:14 assign to ticket1044
}
capture line:18, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:22, length:14 assign to ticket1045
}
capture line:18, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:23, length:14 assign to ticket1046
}
capture line:18, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:24, length:14 assign to ticket1047
}
capture line:18, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:25, length:14 assign to ticket1048
}
capture line:18, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:26, length:14 assign to ticket1049
}
capture line:18, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:27, length:14 assign to ticket1050
}
capture line:18, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:28, length:14 assign to ticket1051
}
capture line:18, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:29, length:14 assign to ticket1052
}
capture line:18, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:30, length:14 assign to ticket1053
}
capture line:18, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:31, length:14 assign to ticket1054
}
capture line:18, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:32, length:14 assign to ticket1055
}
capture line:18, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:33, length:14 assign to ticket1056
}
capture line:18, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:34, length:14 assign to ticket1057
}
capture line:18, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:35, length:14 assign to ticket1058
}
capture line:18, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:36, length:14 assign to ticket1059
}
capture line:18, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:37, length:14 assign to ticket1060
}
capture line:18, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:38, length:14 assign to ticket1061
}
capture line:18, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:39, length:14 assign to ticket1062
}
capture line:18, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:40, length:14 assign to ticket1063
}
capture line:18, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:41, length:14 assign to ticket1064
}
capture line:18, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:42, length:14 assign to ticket1065
}
capture line:18, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:43, length:14 assign to ticket1066
}
capture line:18, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:44, length:14 assign to ticket1067
}
capture line:18, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:45, length:14 assign to ticket1068
}
capture line:18, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:46, length:14 assign to ticket1069
}
capture line:18, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:47, length:14 assign to ticket1070
}
capture line:18, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:48, length:14 assign to ticket1071
}
capture line:18, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:49, length:14 assign to ticket1072
}
capture line:18, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:50, length:14 assign to ticket1073
}
capture line:18, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:51, length:13 assign to ticket1074
    capture line:19, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1074
}
capture line:18, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:52, length:12 assign to ticket1075
    capture line:19, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1075
}
capture line:18, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:53, length:11 assign to ticket1076
    capture line:19, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1076
}
capture line:18, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:54, length:10 assign to ticket1077
    capture line:19, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1077
}
capture line:18, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:55, length:9 assign to ticket1078
    capture line:19, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1078
}
capture line:18, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:56, length:8 assign to ticket1079
    capture line:19, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1079
}
capture line:18, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:57, length:7 assign to ticket1080
    capture line:19, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1080
}
capture line:18, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:58, length:6 assign to ticket1081
    capture line:19, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1081
}
capture line:18, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:59, length:5 assign to ticket1082
    capture line:19, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1082
}
capture line:18, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:60, length:4 assign to ticket1083
    capture line:19, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1083
}

capture line:19, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:61, length:3 assign to ticket1084
    capture line:19, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1084
}
capture line:19, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:62, length:2 assign to ticket1085
    capture line:19, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1085
}
capture line:19, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:18, column:63, length:1 assign to ticket1086
    capture line:19, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1086
}
capture line:19, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:2, length:14 assign to ticket1087
}
capture line:19, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:3, length:14 assign to ticket1088
}
capture line:19, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:4, length:14 assign to ticket1089
}
capture line:19, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:5, length:14 assign to ticket1090
}
capture line:19, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:6, length:14 assign to ticket1091
}
capture line:19, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:7, length:14 assign to ticket1092
}
capture line:19, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:8, length:14 assign to ticket1093
}
capture line:19, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:9, length:14 assign to ticket1094
}
capture line:19, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:10, length:14 assign to ticket1095
}
capture line:19, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:11, length:14 assign to ticket1096
}
capture line:19, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:12, length:14 assign to ticket1097
}
capture line:19, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:13, length:14 assign to ticket1098
}
capture line:19, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:14, length:14 assign to ticket1099
}
capture line:19, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:15, length:14 assign to ticket1100
}
capture line:19, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:16, length:14 assign to ticket1101
}
capture line:19, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:17, length:14 assign to ticket1102
}
capture line:19, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:18, length:14 assign to ticket1103
}
capture line:19, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:19, length:14 assign to ticket1104
}
capture line:19, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:20, length:14 assign to ticket1105
}
capture line:19, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:21, length:14 assign to ticket1106
}
capture line:19, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:22, length:14 assign to ticket1107
}
capture line:19, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:23, length:14 assign to ticket1108
}
capture line:19, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:24, length:14 assign to ticket1109
}
capture line:19, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:25, length:14 assign to ticket1110
}
capture line:19, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:26, length:14 assign to ticket1111
}
capture line:19, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:27, length:14 assign to ticket1112
}
capture line:19, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:28, length:14 assign to ticket1113
}
capture line:19, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:29, length:14 assign to ticket1114
}
capture line:19, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:30, length:14 assign to ticket1115
}
capture line:19, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:31, length:14 assign to ticket1116
}
capture line:19, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:32, length:14 assign to ticket1117
}
capture line:19, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:33, length:14 assign to ticket1118
}
capture line:19, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:34, length:14 assign to ticket1119
}
capture line:19, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:35, length:14 assign to ticket1120
}
capture line:19, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:36, length:14 assign to ticket1121
}
capture line:19, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:37, length:14 assign to ticket1122
}
capture line:19, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:38, length:14 assign to ticket1123
}
capture line:19, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:39, length:14 assign to ticket1124
}
capture line:19, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:40, length:14 assign to ticket1125
}
capture line:19, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:41, length:14 assign to ticket1126
}
capture line:19, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:42, length:14 assign to ticket1127
}
capture line:19, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:43, length:14 assign to ticket1128
}
capture line:19, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:44, length:14 assign to ticket1129
}
capture line:19, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:45, length:14 assign to ticket1130
}
capture line:19, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:46, length:14 assign to ticket1131
}
capture line:19, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:47, length:14 assign to ticket1132
}
capture line:19, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:48, length:14 assign to ticket1133
}
capture line:19, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:49, length:14 assign to ticket1134
}
capture line:19, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:50, length:14 assign to ticket1135
}
capture line:19, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:51, length:13 assign to ticket1136
    capture line:20, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1136
}
capture line:19, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:52, length:12 assign to ticket1137
    capture line:20, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1137
}
capture line:19, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:53, length:11 assign to ticket1138
    capture line:20, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1138
}
capture line:19, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:54, length:10 assign to ticket1139
    capture line:20, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1139
}
capture line:19, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:55, length:9 assign to ticket1140
    capture line:20, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1140
}
capture line:19, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:56, length:8 assign to ticket1141
    capture line:20, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1141
}
capture line:19, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:57, length:7 assign to ticket1142
    capture line:20, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1142
}
capture line:19, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:58, length:6 assign to ticket1143
    capture line:20, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1143
}
capture line:19, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:59, length:5 assign to ticket1144
    capture line:20, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1144
}
capture line:19, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:60, length:4 assign to ticket1145
    capture line:20, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1145
}

capture line:20, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:61, length:3 assign to ticket1146
    capture line:20, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1146
}
capture line:20, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:62, length:2 assign to ticket1147
    capture line:20, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1147
}
capture line:20, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:19, column:63, length:1 assign to ticket1148
    capture line:20, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1148
}
capture line:20, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:2, length:14 assign to ticket1149
}
capture line:20, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:3, length:14 assign to ticket1150
}
capture line:20, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:4, length:14 assign to ticket1151
}
capture line:20, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:5, length:14 assign to ticket1152
}
capture line:20, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:6, length:14 assign to ticket1153
}
capture line:20, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:7, length:14 assign to ticket1154
}
capture line:20, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:8, length:14 assign to ticket1155
}
capture line:20, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:9, length:14 assign to ticket1156
}
capture line:20, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:10, length:14 assign to ticket1157
}
capture line:20, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:11, length:14 assign to ticket1158
}
capture line:20, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:12, length:14 assign to ticket1159
}
capture line:20, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:13, length:14 assign to ticket1160
}
capture line:20, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:14, length:14 assign to ticket1161
}
capture line:20, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:15, length:14 assign to ticket1162
}
capture line:20, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:16, length:14 assign to ticket1163
}
capture line:20, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:17, length:14 assign to ticket1164
}
capture line:20, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:18, length:14 assign to ticket1165
}
capture line:20, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:19, length:14 assign to ticket1166
}
capture line:20, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:20, length:14 assign to ticket1167
}
capture line:20, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:21, length:14 assign to ticket1168
}
capture line:20, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:22, length:14 assign to ticket1169
}
capture line:20, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:23, length:14 assign to ticket1170
}
capture line:20, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:24, length:14 assign to ticket1171
}
capture line:20, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:25, length:14 assign to ticket1172
}
capture line:20, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:26, length:14 assign to ticket1173
}
capture line:20, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:27, length:14 assign to ticket1174
}
capture line:20, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:28, length:14 assign to ticket1175
}
capture line:20, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:29, length:14 assign to ticket1176
}
capture line:20, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:30, length:14 assign to ticket1177
}
capture line:20, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:31, length:14 assign to ticket1178
}
capture line:20, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:32, length:14 assign to ticket1179
}
capture line:20, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:33, length:14 assign to ticket1180
}
capture line:20, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:34, length:14 assign to ticket1181
}
capture line:20, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:35, length:14 assign to ticket1182
}
capture line:20, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:36, length:14 assign to ticket1183
}
capture line:20, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:37, length:14 assign to ticket1184
}
capture line:20, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:38, length:14 assign to ticket1185
}
capture line:20, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:39, length:14 assign to ticket1186
}
capture line:20, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:40, length:14 assign to ticket1187
}
capture line:20, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:41, length:14 assign to ticket1188
}
capture line:20, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:42, length:14 assign to ticket1189
}
capture line:20, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:43, length:14 assign to ticket1190
}
capture line:20, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:44, length:14 assign to ticket1191
}
capture line:20, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:45, length:14 assign to ticket1192
}
capture line:20, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:46, length:14 assign to ticket1193
}
capture line:20, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:47, length:14 assign to ticket1194
}
capture line:20, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:48, length:14 assign to ticket1195
}
capture line:20, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:49, length:14 assign to ticket1196
}
capture line:20, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:50, length:14 assign to ticket1197
}
capture line:20, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:51, length:13 assign to ticket1198
    capture line:21, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1198
}
capture line:20, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:52, length:12 assign to ticket1199
    capture line:21, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1199
}
capture line:20, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:53, length:11 assign to ticket1200
    capture line:21, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1200
}
capture line:20, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:54, length:10 assign to ticket1201
    capture line:21, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1201
}
capture line:20, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:55, length:9 assign to ticket1202
    capture line:21, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1202
}
capture line:20, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:56, length:8 assign to ticket1203
    capture line:21, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1203
}
capture line:20, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:57, length:7 assign to ticket1204
    capture line:21, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1204
}
capture line:20, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:58, length:6 assign to ticket1205
    capture line:21, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1205
}
capture line:20, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:59, length:5 assign to ticket1206
    capture line:21, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1206
}
capture line:20, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:60, length:4 assign to ticket1207
    capture line:21, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1207
}

capture line:21, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:61, length:3 assign to ticket1208
    capture line:21, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1208
}
capture line:21, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:62, length:2 assign to ticket1209
    capture line:21, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1209
}
capture line:21, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:20, column:63, length:1 assign to ticket1210
    capture line:21, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1210
}
capture line:21, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:2, length:14 assign to ticket1211
}
capture line:21, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:3, length:14 assign to ticket1212
}
capture line:21, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:4, length:14 assign to ticket1213
}
capture line:21, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:5, length:14 assign to ticket1214
}
capture line:21, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:6, length:14 assign to ticket1215
}
capture line:21, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:7, length:14 assign to ticket1216
}
capture line:21, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:8, length:14 assign to ticket1217
}
capture line:21, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:9, length:14 assign to ticket1218
}
capture line:21, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:10, length:14 assign to ticket1219
}
capture line:21, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:11, length:14 assign to ticket1220
}
capture line:21, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:12, length:14 assign to ticket1221
}
capture line:21, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:13, length:14 assign to ticket1222
}
capture line:21, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:14, length:14 assign to ticket1223
}
capture line:21, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:15, length:14 assign to ticket1224
}
capture line:21, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:16, length:14 assign to ticket1225
}
capture line:21, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:17, length:14 assign to ticket1226
}
capture line:21, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:18, length:14 assign to ticket1227
}
capture line:21, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:19, length:14 assign to ticket1228
}
capture line:21, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:20, length:14 assign to ticket1229
}
capture line:21, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:21, length:14 assign to ticket1230
}
capture line:21, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:22, length:14 assign to ticket1231
}
capture line:21, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:23, length:14 assign to ticket1232
}
capture line:21, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:24, length:14 assign to ticket1233
}
capture line:21, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:25, length:14 assign to ticket1234
}
capture line:21, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:26, length:14 assign to ticket1235
}
capture line:21, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:27, length:14 assign to ticket1236
}
capture line:21, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:28, length:14 assign to ticket1237
}
capture line:21, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:29, length:14 assign to ticket1238
}
capture line:21, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:30, length:14 assign to ticket1239
}
capture line:21, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:31, length:14 assign to ticket1240
}
capture line:21, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:32, length:14 assign to ticket1241
}
capture line:21, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:33, length:14 assign to ticket1242
}
capture line:21, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:34, length:14 assign to ticket1243
}
capture line:21, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:35, length:14 assign to ticket1244
}
capture line:21, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:36, length:14 assign to ticket1245
}
capture line:21, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:37, length:14 assign to ticket1246
}
capture line:21, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:38, length:14 assign to ticket1247
}
capture line:21, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:39, length:14 assign to ticket1248
}
capture line:21, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:40, length:14 assign to ticket1249
}
capture line:21, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:41, length:14 assign to ticket1250
}
capture line:21, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:42, length:14 assign to ticket1251
}
capture line:21, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:43, length:14 assign to ticket1252
}
capture line:21, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:44, length:14 assign to ticket1253
}
capture line:21, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:45, length:14 assign to ticket1254
}
capture line:21, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:46, length:14 assign to ticket1255
}
capture line:21, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:47, length:14 assign to ticket1256
}
capture line:21, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:48, length:14 assign to ticket1257
}
capture line:21, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:49, length:14 assign to ticket1258
}
capture line:21, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:50, length:14 assign to ticket1259
}
capture line:21, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:51, length:13 assign to ticket1260
    capture line:22, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1260
}
capture line:21, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:52, length:12 assign to ticket1261
    capture line:22, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1261
}
capture line:21, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:53, length:11 assign to ticket1262
    capture line:22, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1262
}
capture line:21, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:54, length:10 assign to ticket1263
    capture line:22, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1263
}
capture line:21, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:55, length:9 assign to ticket1264
    capture line:22, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1264
}
capture line:21, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:56, length:8 assign to ticket1265
    capture line:22, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1265
}
capture line:21, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:57, length:7 assign to ticket1266
    capture line:22, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1266
}
capture line:21, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:58, length:6 assign to ticket1267
    capture line:22, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1267
}
capture line:21, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:59, length:5 assign to ticket1268
    capture line:22, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1268
}
capture line:21, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:60, length:4 assign to ticket1269
    capture line:22, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1269
}

capture line:22, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:61, length:3 assign to ticket1270
    capture line:22, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1270
}
capture line:22, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:62, length:2 assign to ticket1271
    capture line:22, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1271
}
capture line:22, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:21, column:63, length:1 assign to ticket1272
    capture line:22, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1272
}
capture line:22, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:2, length:14 assign to ticket1273
}
capture line:22, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:3, length:14 assign to ticket1274
}
capture line:22, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:4, length:14 assign to ticket1275
}
capture line:22, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:5, length:14 assign to ticket1276
}
capture line:22, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:6, length:14 assign to ticket1277
}
capture line:22, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:7, length:14 assign to ticket1278
}
capture line:22, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:8, length:14 assign to ticket1279
}
capture line:22, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:9, length:14 assign to ticket1280
}
capture line:22, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:10, length:14 assign to ticket1281
}
capture line:22, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:11, length:14 assign to ticket1282
}
capture line:22, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:12, length:14 assign to ticket1283
}
capture line:22, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:13, length:14 assign to ticket1284
}
capture line:22, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:14, length:14 assign to ticket1285
}
capture line:22, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:15, length:14 assign to ticket1286
}
capture line:22, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:16, length:14 assign to ticket1287
}
capture line:22, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:17, length:14 assign to ticket1288
}
capture line:22, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:18, length:14 assign to ticket1289
}
capture line:22, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:19, length:14 assign to ticket1290
}
capture line:22, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:20, length:14 assign to ticket1291
}
capture line:22, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:21, length:14 assign to ticket1292
}
capture line:22, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:22, length:14 assign to ticket1293
}
capture line:22, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:23, length:14 assign to ticket1294
}
capture line:22, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:24, length:14 assign to ticket1295
}
capture line:22, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:25, length:14 assign to ticket1296
}
capture line:22, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:26, length:14 assign to ticket1297
}
capture line:22, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:27, length:14 assign to ticket1298
}
capture line:22, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:28, length:14 assign to ticket1299
}
capture line:22, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:29, length:14 assign to ticket1300
}
capture line:22, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:30, length:14 assign to ticket1301
}
capture line:22, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:31, length:14 assign to ticket1302
}
capture line:22, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:32, length:14 assign to ticket1303
}
capture line:22, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:33, length:14 assign to ticket1304
}
capture line:22, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:34, length:14 assign to ticket1305
}
capture line:22, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:35, length:14 assign to ticket1306
}
capture line:22, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:36, length:14 assign to ticket1307
}
capture line:22, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:37, length:14 assign to ticket1308
}
capture line:22, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:38, length:14 assign to ticket1309
}
capture line:22, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:39, length:14 assign to ticket1310
}
capture line:22, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:40, length:14 assign to ticket1311
}
capture line:22, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:41, length:14 assign to ticket1312
}
capture line:22, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:42, length:14 assign to ticket1313
}
capture line:22, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:43, length:14 assign to ticket1314
}
capture line:22, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:44, length:14 assign to ticket1315
}
capture line:22, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:45, length:14 assign to ticket1316
}
capture line:22, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:46, length:14 assign to ticket1317
}
capture line:22, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:47, length:14 assign to ticket1318
}
capture line:22, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:48, length:14 assign to ticket1319
}
capture line:22, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:49, length:14 assign to ticket1320
}
capture line:22, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:50, length:14 assign to ticket1321
}
capture line:22, column:54, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:51, length:13 assign to ticket1322
    capture line:23, column:2, length:1 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1322
}
capture line:22, column:55, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:52, length:12 assign to ticket1323
    capture line:23, column:2, length:2 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1323
}
capture line:22, column:56, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:53, length:11 assign to ticket1324
    capture line:23, column:2, length:3 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1324
}
capture line:22, column:57, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:54, length:10 assign to ticket1325
    capture line:23, column:2, length:4 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1325
}
capture line:22, column:58, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:55, length:9 assign to ticket1326
    capture line:23, column:2, length:5 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1326
}
capture line:22, column:59, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:56, length:8 assign to ticket1327
    capture line:23, column:2, length:6 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1327
}
capture line:22, column:60, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:57, length:7 assign to ticket1328
    capture line:23, column:2, length:7 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1328
}
capture line:22, column:61, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:58, length:6 assign to ticket1329
    capture line:23, column:2, length:8 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1329
}
capture line:22, column:62, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:59, length:5 assign to ticket1330
    capture line:23, column:2, length:9 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1330
}
capture line:22, column:63, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:60, length:4 assign to ticket1331
    capture line:23, column:2, length:10 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1331
}

capture line:23, column:2, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:61, length:3 assign to ticket1332
    capture line:23, column:2, length:11 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1332
}
capture line:23, column:3, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:62, length:2 assign to ticket1333
    capture line:23, column:2, length:12 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1333
}
capture line:23, column:4, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:22, column:63, length:1 assign to ticket1334
    capture line:23, column:2, length:13 assign to remaining_Ticket_Part
    append remaining_Ticket_Part to ticket1334
}
capture line:23, column:5, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:2, length:14 assign to ticket1335
}
capture line:23, column:6, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:3, length:14 assign to ticket1336
}
capture line:23, column:7, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:4, length:14 assign to ticket1337
}
capture line:23, column:8, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:5, length:14 assign to ticket1338
}
capture line:23, column:9, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:6, length:14 assign to ticket1339
}
capture line:23, column:10, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:7, length:14 assign to ticket1340
}
capture line:23, column:11, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:8, length:14 assign to ticket1341
}
capture line:23, column:12, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:9, length:14 assign to ticket1342
}
capture line:23, column:13, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:10, length:14 assign to ticket1343
}
capture line:23, column:14, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:11, length:14 assign to ticket1344
}
capture line:23, column:15, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:12, length:14 assign to ticket1345
}
capture line:23, column:16, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:13, length:14 assign to ticket1346
}
capture line:23, column:17, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:14, length:14 assign to ticket1347
}
capture line:23, column:18, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:15, length:14 assign to ticket1348
}
capture line:23, column:19, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:16, length:14 assign to ticket1349
}
capture line:23, column:20, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:17, length:14 assign to ticket1350
}
capture line:23, column:21, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:18, length:14 assign to ticket1351
}
capture line:23, column:22, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:19, length:14 assign to ticket1352
}
capture line:23, column:23, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:20, length:14 assign to ticket1353
}
capture line:23, column:24, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:21, length:14 assign to ticket1354
}
capture line:23, column:25, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:22, length:14 assign to ticket1355
}
capture line:23, column:26, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:23, length:14 assign to ticket1356
}
capture line:23, column:27, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:24, length:14 assign to ticket1357
}
capture line:23, column:28, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:25, length:14 assign to ticket1358
}
capture line:23, column:29, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:26, length:14 assign to ticket1359
}
capture line:23, column:30, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:27, length:14 assign to ticket1360
}
capture line:23, column:31, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:28, length:14 assign to ticket1361
}
capture line:23, column:32, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:29, length:14 assign to ticket1362
}
capture line:23, column:33, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:30, length:14 assign to ticket1363
}
capture line:23, column:34, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:31, length:14 assign to ticket1364
}
capture line:23, column:35, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:32, length:14 assign to ticket1365
}
capture line:23, column:36, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:33, length:14 assign to ticket1366
}
capture line:23, column:37, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:34, length:14 assign to ticket1367
}
capture line:23, column:38, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:35, length:14 assign to ticket1368
}
capture line:23, column:39, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:36, length:14 assign to ticket1369
}
capture line:23, column:40, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:37, length:14 assign to ticket1370
}
capture line:23, column:41, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:38, length:14 assign to ticket1371
}
capture line:23, column:42, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:39, length:14 assign to ticket1372
}
capture line:23, column:43, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:40, length:14 assign to ticket1373
}
capture line:23, column:44, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:41, length:14 assign to ticket1374
}
capture line:23, column:45, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:42, length:14 assign to ticket1375
}
capture line:23, column:46, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:43, length:14 assign to ticket1376
}
capture line:23, column:47, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:44, length:14 assign to ticket1377
}
capture line:23, column:48, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:45, length:14 assign to ticket1378
}
capture line:23, column:49, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:46, length:14 assign to ticket1379
}
capture line:23, column:50, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:47, length:14 assign to ticket1380
}
capture line:23, column:51, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:48, length:14 assign to ticket1381
}
capture line:23, column:52, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:49, length:14 assign to ticket1382
}
capture line:23, column:53, length:1 assign to check_Ticket
if (check_Ticket == "-"){
    capture line:23, column:50, length:14 assign to ticket1383
}


if (ticket01 != "undefined"){
    send "TWD/TKT" +ticket01
    call "z_ATC_Refund"
}
if (ticket02 != "undefined"){
    send "TWD/TKT" +ticket02
    call "z_ATC_Refund"
}
if (ticket03 != "undefined"){
    send "TWD/TKT" +ticket03
    call "z_ATC_Refund"
}
if (ticket04 != "undefined"){
    send "TWD/TKT" +ticket04
    call "z_ATC_Refund"
}
if (ticket05 != "undefined"){
    send "TWD/TKT" +ticket05
    call "z_ATC_Refund"
}
if (ticket06 != "undefined"){
    send "TWD/TKT" +ticket06
    call "z_ATC_Refund"
}
if (ticket07 != "undefined"){
    send "TWD/TKT" +ticket07
    call "z_ATC_Refund"
}
if (ticket08 != "undefined"){
    send "TWD/TKT" +ticket08
    call "z_ATC_Refund"
}
if (ticket09 != "undefined"){
    send "TWD/TKT" +ticket09
    call "z_ATC_Refund"
}
if (ticket10 != "undefined"){
    send "TWD/TKT" +ticket10
    call "z_ATC_Refund"
}
if (ticket11 != "undefined"){
    send "TWD/TKT" +ticket11
    call "z_ATC_Refund"
}
if (ticket12 != "undefined"){
    send "TWD/TKT" +ticket12
    call "z_ATC_Refund"
}
if (ticket13 != "undefined"){
    send "TWD/TKT" +ticket13
    call "z_ATC_Refund"
}
if (ticket14 != "undefined"){
    send "TWD/TKT" +ticket14
    call "z_ATC_Refund"
}
if (ticket15 != "undefined"){
    send "TWD/TKT" +ticket15
    call "z_ATC_Refund"
}
if (ticket16 != "undefined"){
    send "TWD/TKT" +ticket16
    call "z_ATC_Refund"
}
if (ticket17 != "undefined"){
    send "TWD/TKT" +ticket17
    call "z_ATC_Refund"
}
if (ticket18 != "undefined"){
    send "TWD/TKT" +ticket18
    call "z_ATC_Refund"
}
if (ticket19 != "undefined"){
    send "TWD/TKT" +ticket19
    call "z_ATC_Refund"
}
if (ticket20 != "undefined"){
    send "TWD/TKT" +ticket20
    call "z_ATC_Refund"
}
if (ticket21 != "undefined"){
    send "TWD/TKT" +ticket21
    call "z_ATC_Refund"
}
if (ticket22 != "undefined"){
    send "TWD/TKT" +ticket22
    call "z_ATC_Refund"
}
if (ticket23 != "undefined"){
    send "TWD/TKT" +ticket23
    call "z_ATC_Refund"
}
if (ticket24 != "undefined"){
    send "TWD/TKT" +ticket24
    call "z_ATC_Refund"
}
if (ticket25 != "undefined"){
    send "TWD/TKT" +ticket25
    call "z_ATC_Refund"
}
if (ticket26 != "undefined"){
    send "TWD/TKT" +ticket26
    call "z_ATC_Refund"
}
if (ticket27 != "undefined"){
    send "TWD/TKT" +ticket27
    call "z_ATC_Refund"
}
if (ticket28 != "undefined"){
    send "TWD/TKT" +ticket28
    call "z_ATC_Refund"
}
if (ticket29 != "undefined"){
    send "TWD/TKT" +ticket29
    call "z_ATC_Refund"
}
if (ticket30 != "undefined"){
    send "TWD/TKT" +ticket30
    call "z_ATC_Refund"
}
if (ticket31 != "undefined"){
    send "TWD/TKT" +ticket31
    call "z_ATC_Refund"
}
if (ticket32 != "undefined"){
    send "TWD/TKT" +ticket32
    call "z_ATC_Refund"
}
if (ticket33 != "undefined"){
    send "TWD/TKT" +ticket33
    call "z_ATC_Refund"
}
if (ticket34 != "undefined"){
    send "TWD/TKT" +ticket34
    call "z_ATC_Refund"
}
if (ticket35 != "undefined"){
    send "TWD/TKT" +ticket35
    call "z_ATC_Refund"
}
if (ticket36 != "undefined"){
    send "TWD/TKT" +ticket36
    call "z_ATC_Refund"
}
if (ticket37 != "undefined"){
    send "TWD/TKT" +ticket37
    call "z_ATC_Refund"
}
if (ticket38 != "undefined"){
    send "TWD/TKT" +ticket38
    call "z_ATC_Refund"
}
if (ticket39 != "undefined"){
    send "TWD/TKT" +ticket39
    call "z_ATC_Refund"
}
if (ticket40 != "undefined"){
    send "TWD/TKT" +ticket40
    call "z_ATC_Refund"
}
if (ticket41 != "undefined"){
    send "TWD/TKT" +ticket41
    call "z_ATC_Refund"
}
if (ticket42 != "undefined"){
    send "TWD/TKT" +ticket42
    call "z_ATC_Refund"
}
if (ticket43 != "undefined"){
    send "TWD/TKT" +ticket43
    call "z_ATC_Refund"
}
if (ticket44 != "undefined"){
    send "TWD/TKT" +ticket44
    call "z_ATC_Refund"
}
if (ticket45 != "undefined"){
    send "TWD/TKT" +ticket45
    call "z_ATC_Refund"
}
if (ticket46 != "undefined"){
    send "TWD/TKT" +ticket46
    call "z_ATC_Refund"
}
if (ticket47 != "undefined"){
    send "TWD/TKT" +ticket47
    call "z_ATC_Refund"
}
if (ticket48 != "undefined"){
    send "TWD/TKT" +ticket48
    call "z_ATC_Refund"
}
if (ticket49 != "undefined"){
    send "TWD/TKT" +ticket49
    call "z_ATC_Refund"
}
if (ticket50 != "undefined"){
    send "TWD/TKT" +ticket50
    call "z_ATC_Refund"
}
if (ticket51 != "undefined"){
    send "TWD/TKT" +ticket51
    call "z_ATC_Refund"
}
if (ticket52 != "undefined"){
    send "TWD/TKT" +ticket52
    call "z_ATC_Refund"
}
if (ticket53 != "undefined"){
    send "TWD/TKT" +ticket53
    call "z_ATC_Refund"
}
if (ticket54 != "undefined"){
    send "TWD/TKT" +ticket54
    call "z_ATC_Refund"
}
if (ticket55 != "undefined"){
    send "TWD/TKT" +ticket55
    call "z_ATC_Refund"
}
if (ticket56 != "undefined"){
    send "TWD/TKT" +ticket56
    call "z_ATC_Refund"
}
if (ticket57 != "undefined"){
    send "TWD/TKT" +ticket57
    call "z_ATC_Refund"
}
if (ticket58 != "undefined"){
    send "TWD/TKT" +ticket58
    call "z_ATC_Refund"
}
if (ticket59 != "undefined"){
    send "TWD/TKT" +ticket59
    call "z_ATC_Refund"
}
if (ticket60 != "undefined"){
    send "TWD/TKT" +ticket60
    call "z_ATC_Refund"
}
if (ticket61 != "undefined"){
    send "TWD/TKT" +ticket61
    call "z_ATC_Refund"
}
if (ticket62 != "undefined"){
    send "TWD/TKT" +ticket62
    call "z_ATC_Refund"
}
if (ticket63 != "undefined"){
    send "TWD/TKT" +ticket63
    call "z_ATC_Refund"
}
if (ticket64 != "undefined"){
    send "TWD/TKT" +ticket64
    call "z_ATC_Refund"
}
if (ticket65 != "undefined"){
    send "TWD/TKT" +ticket65
    call "z_ATC_Refund"
}
if (ticket66 != "undefined"){
    send "TWD/TKT" +ticket66
    call "z_ATC_Refund"
}
if (ticket67 != "undefined"){
    send "TWD/TKT" +ticket67
    call "z_ATC_Refund"
}
if (ticket68 != "undefined"){
    send "TWD/TKT" +ticket68
    call "z_ATC_Refund"
}
if (ticket69 != "undefined"){
    send "TWD/TKT" +ticket69
    call "z_ATC_Refund"
}
if (ticket70 != "undefined"){
    send "TWD/TKT" +ticket70
    call "z_ATC_Refund"
}
if (ticket71 != "undefined"){
    send "TWD/TKT" +ticket71
    call "z_ATC_Refund"
}
if (ticket72 != "undefined"){
    send "TWD/TKT" +ticket72
    call "z_ATC_Refund"
}
if (ticket73 != "undefined"){
    send "TWD/TKT" +ticket73
    call "z_ATC_Refund"
}
if (ticket74 != "undefined"){
    send "TWD/TKT" +ticket74
    call "z_ATC_Refund"
}
if (ticket75 != "undefined"){
    send "TWD/TKT" +ticket75
    call "z_ATC_Refund"
}
if (ticket76 != "undefined"){
    send "TWD/TKT" +ticket76
    call "z_ATC_Refund"
}
if (ticket77 != "undefined"){
    send "TWD/TKT" +ticket77
    call "z_ATC_Refund"
}
if (ticket78 != "undefined"){
    send "TWD/TKT" +ticket78
    call "z_ATC_Refund"
}
if (ticket79 != "undefined"){
    send "TWD/TKT" +ticket79
    call "z_ATC_Refund"
}
if (ticket80 != "undefined"){
    send "TWD/TKT" +ticket80
    call "z_ATC_Refund"
}
if (ticket81 != "undefined"){
    send "TWD/TKT" +ticket81
    call "z_ATC_Refund"
}
if (ticket82 != "undefined"){
    send "TWD/TKT" +ticket82
    call "z_ATC_Refund"
}
if (ticket83 != "undefined"){
    send "TWD/TKT" +ticket83
    call "z_ATC_Refund"
}
if (ticket84 != "undefined"){
    send "TWD/TKT" +ticket84
    call "z_ATC_Refund"
}
if (ticket85 != "undefined"){
    send "TWD/TKT" +ticket85
    call "z_ATC_Refund"
}
if (ticket86 != "undefined"){
    send "TWD/TKT" +ticket86
    call "z_ATC_Refund"
}
if (ticket87 != "undefined"){
    send "TWD/TKT" +ticket87
    call "z_ATC_Refund"
}
if (ticket88 != "undefined"){
    send "TWD/TKT" +ticket88
    call "z_ATC_Refund"
}
if (ticket89 != "undefined"){
    send "TWD/TKT" +ticket89
    call "z_ATC_Refund"
}
if (ticket90 != "undefined"){
    send "TWD/TKT" +ticket90
    call "z_ATC_Refund"
}
if (ticket91 != "undefined"){
    send "TWD/TKT" +ticket91
    call "z_ATC_Refund"
}
if (ticket92 != "undefined"){
    send "TWD/TKT" +ticket92
    call "z_ATC_Refund"
}
if (ticket93 != "undefined"){
    send "TWD/TKT" +ticket93
    call "z_ATC_Refund"
}
if (ticket94 != "undefined"){
    send "TWD/TKT" +ticket94
    call "z_ATC_Refund"
}
if (ticket95 != "undefined"){
    send "TWD/TKT" +ticket95
    call "z_ATC_Refund"
}
if (ticket96 != "undefined"){
    send "TWD/TKT" +ticket96
    call "z_ATC_Refund"
}
if (ticket97 != "undefined"){
    send "TWD/TKT" +ticket97
    call "z_ATC_Refund"
}
if (ticket98 != "undefined"){
    send "TWD/TKT" +ticket98
    call "z_ATC_Refund"
}
if (ticket99 != "undefined"){
    send "TWD/TKT" +ticket99
    call "z_ATC_Refund"
}
if (ticket100 != "undefined"){
    send "TWD/TKT" +ticket100
    call "z_ATC_Refund"
}
if (ticket101 != "undefined"){
    send "TWD/TKT" +ticket101
    call "z_ATC_Refund"
}
if (ticket102 != "undefined"){
    send "TWD/TKT" +ticket102
    call "z_ATC_Refund"
}
if (ticket103 != "undefined"){
    send "TWD/TKT" +ticket103
    call "z_ATC_Refund"
}
if (ticket104 != "undefined"){
    send "TWD/TKT" +ticket104
    call "z_ATC_Refund"
}
if (ticket105 != "undefined"){
    send "TWD/TKT" +ticket105
    call "z_ATC_Refund"
}
if (ticket106 != "undefined"){
    send "TWD/TKT" +ticket106
    call "z_ATC_Refund"
}
if (ticket107 != "undefined"){
    send "TWD/TKT" +ticket107
    call "z_ATC_Refund"
}
if (ticket108 != "undefined"){
    send "TWD/TKT" +ticket108
    call "z_ATC_Refund"
}
if (ticket109 != "undefined"){
    send "TWD/TKT" +ticket109
    call "z_ATC_Refund"
}
if (ticket110 != "undefined"){
    send "TWD/TKT" +ticket110
    call "z_ATC_Refund"
}
if (ticket111 != "undefined"){
    send "TWD/TKT" +ticket111
    call "z_ATC_Refund"
}
if (ticket112 != "undefined"){
    send "TWD/TKT" +ticket112
    call "z_ATC_Refund"
}
if (ticket113 != "undefined"){
    send "TWD/TKT" +ticket113
    call "z_ATC_Refund"
}
if (ticket114 != "undefined"){
    send "TWD/TKT" +ticket114
    call "z_ATC_Refund"
}
if (ticket115 != "undefined"){
    send "TWD/TKT" +ticket115
    call "z_ATC_Refund"
}
if (ticket116 != "undefined"){
    send "TWD/TKT" +ticket116
    call "z_ATC_Refund"
}
if (ticket117 != "undefined"){
    send "TWD/TKT" +ticket117
    call "z_ATC_Refund"
}
if (ticket118 != "undefined"){
    send "TWD/TKT" +ticket118
    call "z_ATC_Refund"
}
if (ticket119 != "undefined"){
    send "TWD/TKT" +ticket119
    call "z_ATC_Refund"
}
if (ticket120 != "undefined"){
    send "TWD/TKT" +ticket120
    call "z_ATC_Refund"
}
if (ticket121 != "undefined"){
    send "TWD/TKT" +ticket121
    call "z_ATC_Refund"
}
if (ticket122 != "undefined"){
    send "TWD/TKT" +ticket122
    call "z_ATC_Refund"
}
if (ticket123 != "undefined"){
    send "TWD/TKT" +ticket123
    call "z_ATC_Refund"
}
if (ticket124 != "undefined"){
    send "TWD/TKT" +ticket124
    call "z_ATC_Refund"
}
if (ticket125 != "undefined"){
    send "TWD/TKT" +ticket125
    call "z_ATC_Refund"
}
if (ticket126 != "undefined"){
    send "TWD/TKT" +ticket126
    call "z_ATC_Refund"
}
if (ticket127 != "undefined"){
    send "TWD/TKT" +ticket127
    call "z_ATC_Refund"
}
if (ticket128 != "undefined"){
    send "TWD/TKT" +ticket128
    call "z_ATC_Refund"
}
if (ticket129 != "undefined"){
    send "TWD/TKT" +ticket129
    call "z_ATC_Refund"
}
if (ticket130 != "undefined"){
    send "TWD/TKT" +ticket130
    call "z_ATC_Refund"
}
if (ticket131 != "undefined"){
    send "TWD/TKT" +ticket131
    call "z_ATC_Refund"
}
if (ticket132 != "undefined"){
    send "TWD/TKT" +ticket132
    call "z_ATC_Refund"
}
if (ticket133 != "undefined"){
    send "TWD/TKT" +ticket133
    call "z_ATC_Refund"
}
if (ticket134 != "undefined"){
    send "TWD/TKT" +ticket134
    call "z_ATC_Refund"
}
if (ticket135 != "undefined"){
    send "TWD/TKT" +ticket135
    call "z_ATC_Refund"
}
if (ticket136 != "undefined"){
    send "TWD/TKT" +ticket136
    call "z_ATC_Refund"
}
if (ticket137 != "undefined"){
    send "TWD/TKT" +ticket137
    call "z_ATC_Refund"
}
if (ticket138 != "undefined"){
    send "TWD/TKT" +ticket138
    call "z_ATC_Refund"
}
if (ticket139 != "undefined"){
    send "TWD/TKT" +ticket139
    call "z_ATC_Refund"
}
if (ticket140 != "undefined"){
    send "TWD/TKT" +ticket140
    call "z_ATC_Refund"
}
if (ticket141 != "undefined"){
    send "TWD/TKT" +ticket141
    call "z_ATC_Refund"
}
if (ticket142 != "undefined"){
    send "TWD/TKT" +ticket142
    call "z_ATC_Refund"
}
if (ticket143 != "undefined"){
    send "TWD/TKT" +ticket143
    call "z_ATC_Refund"
}
if (ticket144 != "undefined"){
    send "TWD/TKT" +ticket144
    call "z_ATC_Refund"
}
if (ticket145 != "undefined"){
    send "TWD/TKT" +ticket145
    call "z_ATC_Refund"
}
if (ticket146 != "undefined"){
    send "TWD/TKT" +ticket146
    call "z_ATC_Refund"
}
if (ticket147 != "undefined"){
    send "TWD/TKT" +ticket147
    call "z_ATC_Refund"
}
if (ticket148 != "undefined"){
    send "TWD/TKT" +ticket148
    call "z_ATC_Refund"
}
if (ticket149 != "undefined"){
    send "TWD/TKT" +ticket149
    call "z_ATC_Refund"
}
if (ticket150 != "undefined"){
    send "TWD/TKT" +ticket150
    call "z_ATC_Refund"
}
if (ticket151 != "undefined"){
    send "TWD/TKT" +ticket151
    call "z_ATC_Refund"
}
if (ticket152 != "undefined"){
    send "TWD/TKT" +ticket152
    call "z_ATC_Refund"
}
if (ticket153 != "undefined"){
    send "TWD/TKT" +ticket153
    call "z_ATC_Refund"
}
if (ticket154 != "undefined"){
    send "TWD/TKT" +ticket154
    call "z_ATC_Refund"
}
if (ticket155 != "undefined"){
    send "TWD/TKT" +ticket155
    call "z_ATC_Refund"
}
if (ticket156 != "undefined"){
    send "TWD/TKT" +ticket156
    call "z_ATC_Refund"
}
if (ticket157 != "undefined"){
    send "TWD/TKT" +ticket157
    call "z_ATC_Refund"
}
if (ticket158 != "undefined"){
    send "TWD/TKT" +ticket158
    call "z_ATC_Refund"
}
if (ticket159 != "undefined"){
    send "TWD/TKT" +ticket159
    call "z_ATC_Refund"
}
if (ticket160 != "undefined"){
    send "TWD/TKT" +ticket160
    call "z_ATC_Refund"
}
if (ticket161 != "undefined"){
    send "TWD/TKT" +ticket161
    call "z_ATC_Refund"
}
if (ticket162 != "undefined"){
    send "TWD/TKT" +ticket162
    call "z_ATC_Refund"
}
if (ticket163 != "undefined"){
    send "TWD/TKT" +ticket163
    call "z_ATC_Refund"
}
if (ticket164 != "undefined"){
    send "TWD/TKT" +ticket164
    call "z_ATC_Refund"
}
if (ticket165 != "undefined"){
    send "TWD/TKT" +ticket165
    call "z_ATC_Refund"
}
if (ticket166 != "undefined"){
    send "TWD/TKT" +ticket166
    call "z_ATC_Refund"
}
if (ticket167 != "undefined"){
    send "TWD/TKT" +ticket167
    call "z_ATC_Refund"
}
if (ticket168 != "undefined"){
    send "TWD/TKT" +ticket168
    call "z_ATC_Refund"
}
if (ticket169 != "undefined"){
    send "TWD/TKT" +ticket169
    call "z_ATC_Refund"
}
if (ticket170 != "undefined"){
    send "TWD/TKT" +ticket170
    call "z_ATC_Refund"
}
if (ticket171 != "undefined"){
    send "TWD/TKT" +ticket171
    call "z_ATC_Refund"
}
if (ticket172 != "undefined"){
    send "TWD/TKT" +ticket172
    call "z_ATC_Refund"
}
if (ticket173 != "undefined"){
    send "TWD/TKT" +ticket173
    call "z_ATC_Refund"
}
if (ticket174 != "undefined"){
    send "TWD/TKT" +ticket174
    call "z_ATC_Refund"
}
if (ticket175 != "undefined"){
    send "TWD/TKT" +ticket175
    call "z_ATC_Refund"
}
if (ticket176 != "undefined"){
    send "TWD/TKT" +ticket176
    call "z_ATC_Refund"
}
if (ticket177 != "undefined"){
    send "TWD/TKT" +ticket177
    call "z_ATC_Refund"
}
if (ticket178 != "undefined"){
    send "TWD/TKT" +ticket178
    call "z_ATC_Refund"
}
if (ticket179 != "undefined"){
    send "TWD/TKT" +ticket179
    call "z_ATC_Refund"
}
if (ticket180 != "undefined"){
    send "TWD/TKT" +ticket180
    call "z_ATC_Refund"
}
if (ticket181 != "undefined"){
    send "TWD/TKT" +ticket181
    call "z_ATC_Refund"
}
if (ticket182 != "undefined"){
    send "TWD/TKT" +ticket182
    call "z_ATC_Refund"
}
if (ticket183 != "undefined"){
    send "TWD/TKT" +ticket183
    call "z_ATC_Refund"
}
if (ticket184 != "undefined"){
    send "TWD/TKT" +ticket184
    call "z_ATC_Refund"
}
if (ticket185 != "undefined"){
    send "TWD/TKT" +ticket185
    call "z_ATC_Refund"
}
if (ticket186 != "undefined"){
    send "TWD/TKT" +ticket186
    call "z_ATC_Refund"
}
if (ticket187 != "undefined"){
    send "TWD/TKT" +ticket187
    call "z_ATC_Refund"
}
if (ticket188 != "undefined"){
    send "TWD/TKT" +ticket188
    call "z_ATC_Refund"
}
if (ticket189 != "undefined"){
    send "TWD/TKT" +ticket189
    call "z_ATC_Refund"
}
if (ticket190 != "undefined"){
    send "TWD/TKT" +ticket190
    call "z_ATC_Refund"
}
if (ticket191 != "undefined"){
    send "TWD/TKT" +ticket191
    call "z_ATC_Refund"
}
if (ticket192 != "undefined"){
    send "TWD/TKT" +ticket192
    call "z_ATC_Refund"
}
if (ticket193 != "undefined"){
    send "TWD/TKT" +ticket193
    call "z_ATC_Refund"
}
if (ticket194 != "undefined"){
    send "TWD/TKT" +ticket194
    call "z_ATC_Refund"
}
if (ticket195 != "undefined"){
    send "TWD/TKT" +ticket195
    call "z_ATC_Refund"
}
if (ticket196 != "undefined"){
    send "TWD/TKT" +ticket196
    call "z_ATC_Refund"
}
if (ticket197 != "undefined"){
    send "TWD/TKT" +ticket197
    call "z_ATC_Refund"
}
if (ticket198 != "undefined"){
    send "TWD/TKT" +ticket198
    call "z_ATC_Refund"
}
if (ticket199 != "undefined"){
    send "TWD/TKT" +ticket199
    call "z_ATC_Refund"
}
if (ticket200 != "undefined"){
    send "TWD/TKT" +ticket200
    call "z_ATC_Refund"
}
if (ticket201 != "undefined"){
    send "TWD/TKT" +ticket201
    call "z_ATC_Refund"
}
if (ticket202 != "undefined"){
    send "TWD/TKT" +ticket202
    call "z_ATC_Refund"
}
if (ticket203 != "undefined"){
    send "TWD/TKT" +ticket203
    call "z_ATC_Refund"
}
if (ticket204 != "undefined"){
    send "TWD/TKT" +ticket204
    call "z_ATC_Refund"
}
if (ticket205 != "undefined"){
    send "TWD/TKT" +ticket205
    call "z_ATC_Refund"
}
if (ticket206 != "undefined"){
    send "TWD/TKT" +ticket206
    call "z_ATC_Refund"
}
if (ticket207 != "undefined"){
    send "TWD/TKT" +ticket207
    call "z_ATC_Refund"
}
if (ticket208 != "undefined"){
    send "TWD/TKT" +ticket208
    call "z_ATC_Refund"
}
if (ticket209 != "undefined"){
    send "TWD/TKT" +ticket209
    call "z_ATC_Refund"
}
if (ticket210 != "undefined"){
    send "TWD/TKT" +ticket210
    call "z_ATC_Refund"
}
if (ticket211 != "undefined"){
    send "TWD/TKT" +ticket211
    call "z_ATC_Refund"
}
if (ticket212 != "undefined"){
    send "TWD/TKT" +ticket212
    call "z_ATC_Refund"
}
if (ticket213 != "undefined"){
    send "TWD/TKT" +ticket213
    call "z_ATC_Refund"
}
if (ticket214 != "undefined"){
    send "TWD/TKT" +ticket214
    call "z_ATC_Refund"
}
if (ticket215 != "undefined"){
    send "TWD/TKT" +ticket215
    call "z_ATC_Refund"
}
if (ticket216 != "undefined"){
    send "TWD/TKT" +ticket216
    call "z_ATC_Refund"
}
if (ticket217 != "undefined"){
    send "TWD/TKT" +ticket217
    call "z_ATC_Refund"
}
if (ticket218 != "undefined"){
    send "TWD/TKT" +ticket218
    call "z_ATC_Refund"
}
if (ticket219 != "undefined"){
    send "TWD/TKT" +ticket219
    call "z_ATC_Refund"
}
if (ticket220 != "undefined"){
    send "TWD/TKT" +ticket220
    call "z_ATC_Refund"
}
if (ticket221 != "undefined"){
    send "TWD/TKT" +ticket221
    call "z_ATC_Refund"
}
if (ticket222 != "undefined"){
    send "TWD/TKT" +ticket222
    call "z_ATC_Refund"
}
if (ticket223 != "undefined"){
    send "TWD/TKT" +ticket223
    call "z_ATC_Refund"
}
if (ticket224 != "undefined"){
    send "TWD/TKT" +ticket224
    call "z_ATC_Refund"
}
if (ticket225 != "undefined"){
    send "TWD/TKT" +ticket225
    call "z_ATC_Refund"
}
if (ticket226 != "undefined"){
    send "TWD/TKT" +ticket226
    call "z_ATC_Refund"
}
if (ticket227 != "undefined"){
    send "TWD/TKT" +ticket227
    call "z_ATC_Refund"
}
if (ticket228 != "undefined"){
    send "TWD/TKT" +ticket228
    call "z_ATC_Refund"
}
if (ticket229 != "undefined"){
    send "TWD/TKT" +ticket229
    call "z_ATC_Refund"
}
if (ticket230 != "undefined"){
    send "TWD/TKT" +ticket230
    call "z_ATC_Refund"
}
if (ticket231 != "undefined"){
    send "TWD/TKT" +ticket231
    call "z_ATC_Refund"
}
if (ticket232 != "undefined"){
    send "TWD/TKT" +ticket232
    call "z_ATC_Refund"
}
if (ticket233 != "undefined"){
    send "TWD/TKT" +ticket233
    call "z_ATC_Refund"
}
if (ticket234 != "undefined"){
    send "TWD/TKT" +ticket234
    call "z_ATC_Refund"
}
if (ticket235 != "undefined"){
    send "TWD/TKT" +ticket235
    call "z_ATC_Refund"
}
if (ticket236 != "undefined"){
    send "TWD/TKT" +ticket236
    call "z_ATC_Refund"
}
if (ticket237 != "undefined"){
    send "TWD/TKT" +ticket237
    call "z_ATC_Refund"
}
if (ticket238 != "undefined"){
    send "TWD/TKT" +ticket238
    call "z_ATC_Refund"
}
if (ticket239 != "undefined"){
    send "TWD/TKT" +ticket239
    call "z_ATC_Refund"
}
if (ticket240 != "undefined"){
    send "TWD/TKT" +ticket240
    call "z_ATC_Refund"
}
if (ticket241 != "undefined"){
    send "TWD/TKT" +ticket241
    call "z_ATC_Refund"
}
if (ticket242 != "undefined"){
    send "TWD/TKT" +ticket242
    call "z_ATC_Refund"
}
if (ticket243 != "undefined"){
    send "TWD/TKT" +ticket243
    call "z_ATC_Refund"
}
if (ticket244 != "undefined"){
    send "TWD/TKT" +ticket244
    call "z_ATC_Refund"
}
if (ticket245 != "undefined"){
    send "TWD/TKT" +ticket245
    call "z_ATC_Refund"
}
if (ticket246 != "undefined"){
    send "TWD/TKT" +ticket246
    call "z_ATC_Refund"
}
if (ticket247 != "undefined"){
    send "TWD/TKT" +ticket247
    call "z_ATC_Refund"
}
if (ticket248 != "undefined"){
    send "TWD/TKT" +ticket248
    call "z_ATC_Refund"
}
if (ticket249 != "undefined"){
    send "TWD/TKT" +ticket249
    call "z_ATC_Refund"
}
if (ticket250 != "undefined"){
    send "TWD/TKT" +ticket250
    call "z_ATC_Refund"
}
if (ticket251 != "undefined"){
    send "TWD/TKT" +ticket251
    call "z_ATC_Refund"
}
if (ticket252 != "undefined"){
    send "TWD/TKT" +ticket252
    call "z_ATC_Refund"
}
if (ticket253 != "undefined"){
    send "TWD/TKT" +ticket253
    call "z_ATC_Refund"
}
if (ticket254 != "undefined"){
    send "TWD/TKT" +ticket254
    call "z_ATC_Refund"
}
if (ticket255 != "undefined"){
    send "TWD/TKT" +ticket255
    call "z_ATC_Refund"
}
if (ticket256 != "undefined"){
    send "TWD/TKT" +ticket256
    call "z_ATC_Refund"
}
if (ticket257 != "undefined"){
    send "TWD/TKT" +ticket257
    call "z_ATC_Refund"
}
if (ticket258 != "undefined"){
    send "TWD/TKT" +ticket258
    call "z_ATC_Refund"
}
if (ticket259 != "undefined"){
    send "TWD/TKT" +ticket259
    call "z_ATC_Refund"
}
if (ticket260 != "undefined"){
    send "TWD/TKT" +ticket260
    call "z_ATC_Refund"
}
if (ticket261 != "undefined"){
    send "TWD/TKT" +ticket261
    call "z_ATC_Refund"
}
if (ticket262 != "undefined"){
    send "TWD/TKT" +ticket262
    call "z_ATC_Refund"
}
if (ticket263 != "undefined"){
    send "TWD/TKT" +ticket263
    call "z_ATC_Refund"
}
if (ticket264 != "undefined"){
    send "TWD/TKT" +ticket264
    call "z_ATC_Refund"
}
if (ticket265 != "undefined"){
    send "TWD/TKT" +ticket265
    call "z_ATC_Refund"
}
if (ticket266 != "undefined"){
    send "TWD/TKT" +ticket266
    call "z_ATC_Refund"
}
if (ticket267 != "undefined"){
    send "TWD/TKT" +ticket267
    call "z_ATC_Refund"
}
if (ticket268 != "undefined"){
    send "TWD/TKT" +ticket268
    call "z_ATC_Refund"
}
if (ticket269 != "undefined"){
    send "TWD/TKT" +ticket269
    call "z_ATC_Refund"
}
if (ticket270 != "undefined"){
    send "TWD/TKT" +ticket270
    call "z_ATC_Refund"
}
if (ticket271 != "undefined"){
    send "TWD/TKT" +ticket271
    call "z_ATC_Refund"
}
if (ticket272 != "undefined"){
    send "TWD/TKT" +ticket272
    call "z_ATC_Refund"
}
if (ticket273 != "undefined"){
    send "TWD/TKT" +ticket273
    call "z_ATC_Refund"
}
if (ticket274 != "undefined"){
    send "TWD/TKT" +ticket274
    call "z_ATC_Refund"
}
if (ticket275 != "undefined"){
    send "TWD/TKT" +ticket275
    call "z_ATC_Refund"
}
if (ticket276 != "undefined"){
    send "TWD/TKT" +ticket276
    call "z_ATC_Refund"
}
if (ticket277 != "undefined"){
    send "TWD/TKT" +ticket277
    call "z_ATC_Refund"
}
if (ticket278 != "undefined"){
    send "TWD/TKT" +ticket278
    call "z_ATC_Refund"
}
if (ticket279 != "undefined"){
    send "TWD/TKT" +ticket279
    call "z_ATC_Refund"
}
if (ticket280 != "undefined"){
    send "TWD/TKT" +ticket280
    call "z_ATC_Refund"
}
if (ticket281 != "undefined"){
    send "TWD/TKT" +ticket281
    call "z_ATC_Refund"
}
if (ticket282 != "undefined"){
    send "TWD/TKT" +ticket282
    call "z_ATC_Refund"
}
if (ticket283 != "undefined"){
    send "TWD/TKT" +ticket283
    call "z_ATC_Refund"
}
if (ticket284 != "undefined"){
    send "TWD/TKT" +ticket284
    call "z_ATC_Refund"
}
if (ticket285 != "undefined"){
    send "TWD/TKT" +ticket285
    call "z_ATC_Refund"
}
if (ticket286 != "undefined"){
    send "TWD/TKT" +ticket286
    call "z_ATC_Refund"
}
if (ticket287 != "undefined"){
    send "TWD/TKT" +ticket287
    call "z_ATC_Refund"
}
if (ticket288 != "undefined"){
    send "TWD/TKT" +ticket288
    call "z_ATC_Refund"
}
if (ticket289 != "undefined"){
    send "TWD/TKT" +ticket289
    call "z_ATC_Refund"
}
if (ticket290 != "undefined"){
    send "TWD/TKT" +ticket290
    call "z_ATC_Refund"
}
if (ticket291 != "undefined"){
    send "TWD/TKT" +ticket291
    call "z_ATC_Refund"
}
if (ticket292 != "undefined"){
    send "TWD/TKT" +ticket292
    call "z_ATC_Refund"
}
if (ticket293 != "undefined"){
    send "TWD/TKT" +ticket293
    call "z_ATC_Refund"
}
if (ticket294 != "undefined"){
    send "TWD/TKT" +ticket294
    call "z_ATC_Refund"
}
if (ticket295 != "undefined"){
    send "TWD/TKT" +ticket295
    call "z_ATC_Refund"
}
if (ticket296 != "undefined"){
    send "TWD/TKT" +ticket296
    call "z_ATC_Refund"
}
if (ticket297 != "undefined"){
    send "TWD/TKT" +ticket297
    call "z_ATC_Refund"
}
if (ticket298 != "undefined"){
    send "TWD/TKT" +ticket298
    call "z_ATC_Refund"
}
if (ticket299 != "undefined"){
    send "TWD/TKT" +ticket299
    call "z_ATC_Refund"
}
if (ticket300 != "undefined"){
    send "TWD/TKT" +ticket300
    call "z_ATC_Refund"
}
if (ticket301 != "undefined"){
    send "TWD/TKT" +ticket301
    call "z_ATC_Refund"
}
if (ticket302 != "undefined"){
    send "TWD/TKT" +ticket302
    call "z_ATC_Refund"
}
if (ticket303 != "undefined"){
    send "TWD/TKT" +ticket303
    call "z_ATC_Refund"
}
if (ticket304 != "undefined"){
    send "TWD/TKT" +ticket304
    call "z_ATC_Refund"
}
if (ticket305 != "undefined"){
    send "TWD/TKT" +ticket305
    call "z_ATC_Refund"
}
if (ticket306 != "undefined"){
    send "TWD/TKT" +ticket306
    call "z_ATC_Refund"
}
if (ticket307 != "undefined"){
    send "TWD/TKT" +ticket307
    call "z_ATC_Refund"
}
if (ticket308 != "undefined"){
    send "TWD/TKT" +ticket308
    call "z_ATC_Refund"
}
if (ticket309 != "undefined"){
    send "TWD/TKT" +ticket309
    call "z_ATC_Refund"
}
if (ticket310 != "undefined"){
    send "TWD/TKT" +ticket310
    call "z_ATC_Refund"
}
if (ticket311 != "undefined"){
    send "TWD/TKT" +ticket311
    call "z_ATC_Refund"
}
if (ticket312 != "undefined"){
    send "TWD/TKT" +ticket312
    call "z_ATC_Refund"
}
if (ticket313 != "undefined"){
    send "TWD/TKT" +ticket313
    call "z_ATC_Refund"
}
if (ticket314 != "undefined"){
    send "TWD/TKT" +ticket314
    call "z_ATC_Refund"
}
if (ticket315 != "undefined"){
    send "TWD/TKT" +ticket315
    call "z_ATC_Refund"
}
if (ticket316 != "undefined"){
    send "TWD/TKT" +ticket316
    call "z_ATC_Refund"
}
if (ticket317 != "undefined"){
    send "TWD/TKT" +ticket317
    call "z_ATC_Refund"
}
if (ticket318 != "undefined"){
    send "TWD/TKT" +ticket318
    call "z_ATC_Refund"
}
if (ticket319 != "undefined"){
    send "TWD/TKT" +ticket319
    call "z_ATC_Refund"
}
if (ticket320 != "undefined"){
    send "TWD/TKT" +ticket320
    call "z_ATC_Refund"
}
if (ticket321 != "undefined"){
    send "TWD/TKT" +ticket321
    call "z_ATC_Refund"
}
if (ticket322 != "undefined"){
    send "TWD/TKT" +ticket322
    call "z_ATC_Refund"
}
if (ticket323 != "undefined"){
    send "TWD/TKT" +ticket323
    call "z_ATC_Refund"
}
if (ticket324 != "undefined"){
    send "TWD/TKT" +ticket324
    call "z_ATC_Refund"
}
if (ticket325 != "undefined"){
    send "TWD/TKT" +ticket325
    call "z_ATC_Refund"
}
if (ticket326 != "undefined"){
    send "TWD/TKT" +ticket326
    call "z_ATC_Refund"
}
if (ticket327 != "undefined"){
    send "TWD/TKT" +ticket327
    call "z_ATC_Refund"
}
if (ticket328 != "undefined"){
    send "TWD/TKT" +ticket328
    call "z_ATC_Refund"
}
if (ticket329 != "undefined"){
    send "TWD/TKT" +ticket329
    call "z_ATC_Refund"
}
if (ticket330 != "undefined"){
    send "TWD/TKT" +ticket330
    call "z_ATC_Refund"
}
if (ticket331 != "undefined"){
    send "TWD/TKT" +ticket331
    call "z_ATC_Refund"
}
if (ticket332 != "undefined"){
    send "TWD/TKT" +ticket332
    call "z_ATC_Refund"
}
if (ticket333 != "undefined"){
    send "TWD/TKT" +ticket333
    call "z_ATC_Refund"
}
if (ticket334 != "undefined"){
    send "TWD/TKT" +ticket334
    call "z_ATC_Refund"
}
if (ticket335 != "undefined"){
    send "TWD/TKT" +ticket335
    call "z_ATC_Refund"
}
if (ticket336 != "undefined"){
    send "TWD/TKT" +ticket336
    call "z_ATC_Refund"
}
if (ticket337 != "undefined"){
    send "TWD/TKT" +ticket337
    call "z_ATC_Refund"
}
if (ticket338 != "undefined"){
    send "TWD/TKT" +ticket338
    call "z_ATC_Refund"
}
if (ticket339 != "undefined"){
    send "TWD/TKT" +ticket339
    call "z_ATC_Refund"
}
if (ticket340 != "undefined"){
    send "TWD/TKT" +ticket340
    call "z_ATC_Refund"
}
if (ticket341 != "undefined"){
    send "TWD/TKT" +ticket341
    call "z_ATC_Refund"
}
if (ticket342 != "undefined"){
    send "TWD/TKT" +ticket342
    call "z_ATC_Refund"
}
if (ticket343 != "undefined"){
    send "TWD/TKT" +ticket343
    call "z_ATC_Refund"
}
if (ticket344 != "undefined"){
    send "TWD/TKT" +ticket344
    call "z_ATC_Refund"
}
if (ticket345 != "undefined"){
    send "TWD/TKT" +ticket345
    call "z_ATC_Refund"
}
if (ticket346 != "undefined"){
    send "TWD/TKT" +ticket346
    call "z_ATC_Refund"
}
if (ticket347 != "undefined"){
    send "TWD/TKT" +ticket347
    call "z_ATC_Refund"
}
if (ticket348 != "undefined"){
    send "TWD/TKT" +ticket348
    call "z_ATC_Refund"
}
if (ticket349 != "undefined"){
    send "TWD/TKT" +ticket349
    call "z_ATC_Refund"
}
if (ticket350 != "undefined"){
    send "TWD/TKT" +ticket350
    call "z_ATC_Refund"
}
if (ticket351 != "undefined"){
    send "TWD/TKT" +ticket351
    call "z_ATC_Refund"
}
if (ticket352 != "undefined"){
    send "TWD/TKT" +ticket352
    call "z_ATC_Refund"
}
if (ticket353 != "undefined"){
    send "TWD/TKT" +ticket353
    call "z_ATC_Refund"
}
if (ticket354 != "undefined"){
    send "TWD/TKT" +ticket354
    call "z_ATC_Refund"
}
if (ticket355 != "undefined"){
    send "TWD/TKT" +ticket355
    call "z_ATC_Refund"
}
if (ticket356 != "undefined"){
    send "TWD/TKT" +ticket356
    call "z_ATC_Refund"
}
if (ticket357 != "undefined"){
    send "TWD/TKT" +ticket357
    call "z_ATC_Refund"
}
if (ticket358 != "undefined"){
    send "TWD/TKT" +ticket358
    call "z_ATC_Refund"
}
if (ticket359 != "undefined"){
    send "TWD/TKT" +ticket359
    call "z_ATC_Refund"
}
if (ticket360 != "undefined"){
    send "TWD/TKT" +ticket360
    call "z_ATC_Refund"
}
if (ticket361 != "undefined"){
    send "TWD/TKT" +ticket361
    call "z_ATC_Refund"
}
if (ticket362 != "undefined"){
    send "TWD/TKT" +ticket362
    call "z_ATC_Refund"
}
if (ticket363 != "undefined"){
    send "TWD/TKT" +ticket363
    call "z_ATC_Refund"
}
if (ticket364 != "undefined"){
    send "TWD/TKT" +ticket364
    call "z_ATC_Refund"
}
if (ticket365 != "undefined"){
    send "TWD/TKT" +ticket365
    call "z_ATC_Refund"
}
if (ticket366 != "undefined"){
    send "TWD/TKT" +ticket366
    call "z_ATC_Refund"
}
if (ticket367 != "undefined"){
    send "TWD/TKT" +ticket367
    call "z_ATC_Refund"
}
if (ticket368 != "undefined"){
    send "TWD/TKT" +ticket368
    call "z_ATC_Refund"
}
if (ticket369 != "undefined"){
    send "TWD/TKT" +ticket369
    call "z_ATC_Refund"
}
if (ticket370 != "undefined"){
    send "TWD/TKT" +ticket370
    call "z_ATC_Refund"
}
if (ticket371 != "undefined"){
    send "TWD/TKT" +ticket371
    call "z_ATC_Refund"
}
if (ticket372 != "undefined"){
    send "TWD/TKT" +ticket372
    call "z_ATC_Refund"
}
if (ticket373 != "undefined"){
    send "TWD/TKT" +ticket373
    call "z_ATC_Refund"
}
if (ticket374 != "undefined"){
    send "TWD/TKT" +ticket374
    call "z_ATC_Refund"
}
if (ticket375 != "undefined"){
    send "TWD/TKT" +ticket375
    call "z_ATC_Refund"
}
if (ticket376 != "undefined"){
    send "TWD/TKT" +ticket376
    call "z_ATC_Refund"
}
if (ticket377 != "undefined"){
    send "TWD/TKT" +ticket377
    call "z_ATC_Refund"
}
if (ticket378 != "undefined"){
    send "TWD/TKT" +ticket378
    call "z_ATC_Refund"
}
if (ticket379 != "undefined"){
    send "TWD/TKT" +ticket379
    call "z_ATC_Refund"
}
if (ticket380 != "undefined"){
    send "TWD/TKT" +ticket380
    call "z_ATC_Refund"
}
if (ticket381 != "undefined"){
    send "TWD/TKT" +ticket381
    call "z_ATC_Refund"
}
if (ticket382 != "undefined"){
    send "TWD/TKT" +ticket382
    call "z_ATC_Refund"
}
if (ticket383 != "undefined"){
    send "TWD/TKT" +ticket383
    call "z_ATC_Refund"
}
if (ticket384 != "undefined"){
    send "TWD/TKT" +ticket384
    call "z_ATC_Refund"
}
if (ticket385 != "undefined"){
    send "TWD/TKT" +ticket385
    call "z_ATC_Refund"
}
if (ticket386 != "undefined"){
    send "TWD/TKT" +ticket386
    call "z_ATC_Refund"
}
if (ticket387 != "undefined"){
    send "TWD/TKT" +ticket387
    call "z_ATC_Refund"
}
if (ticket388 != "undefined"){
    send "TWD/TKT" +ticket388
    call "z_ATC_Refund"
}
if (ticket389 != "undefined"){
    send "TWD/TKT" +ticket389
    call "z_ATC_Refund"
}
if (ticket390 != "undefined"){
    send "TWD/TKT" +ticket390
    call "z_ATC_Refund"
}
if (ticket391 != "undefined"){
    send "TWD/TKT" +ticket391
    call "z_ATC_Refund"
}
if (ticket392 != "undefined"){
    send "TWD/TKT" +ticket392
    call "z_ATC_Refund"
}
if (ticket393 != "undefined"){
    send "TWD/TKT" +ticket393
    call "z_ATC_Refund"
}
if (ticket394 != "undefined"){
    send "TWD/TKT" +ticket394
    call "z_ATC_Refund"
}
if (ticket395 != "undefined"){
    send "TWD/TKT" +ticket395
    call "z_ATC_Refund"
}
if (ticket396 != "undefined"){
    send "TWD/TKT" +ticket396
    call "z_ATC_Refund"
}
if (ticket397 != "undefined"){
    send "TWD/TKT" +ticket397
    call "z_ATC_Refund"
}
if (ticket398 != "undefined"){
    send "TWD/TKT" +ticket398
    call "z_ATC_Refund"
}
if (ticket399 != "undefined"){
    send "TWD/TKT" +ticket399
    call "z_ATC_Refund"
}
if (ticket400 != "undefined"){
    send "TWD/TKT" +ticket400
    call "z_ATC_Refund"
}
if (ticket401 != "undefined"){
    send "TWD/TKT" +ticket401
    call "z_ATC_Refund"
}
if (ticket402 != "undefined"){
    send "TWD/TKT" +ticket402
    call "z_ATC_Refund"
}
if (ticket403 != "undefined"){
    send "TWD/TKT" +ticket403
    call "z_ATC_Refund"
}
if (ticket404 != "undefined"){
    send "TWD/TKT" +ticket404
    call "z_ATC_Refund"
}
if (ticket405 != "undefined"){
    send "TWD/TKT" +ticket405
    call "z_ATC_Refund"
}
if (ticket406 != "undefined"){
    send "TWD/TKT" +ticket406
    call "z_ATC_Refund"
}
if (ticket407 != "undefined"){
    send "TWD/TKT" +ticket407
    call "z_ATC_Refund"
}
if (ticket408 != "undefined"){
    send "TWD/TKT" +ticket408
    call "z_ATC_Refund"
}
if (ticket409 != "undefined"){
    send "TWD/TKT" +ticket409
    call "z_ATC_Refund"
}
if (ticket410 != "undefined"){
    send "TWD/TKT" +ticket410
    call "z_ATC_Refund"
}
if (ticket411 != "undefined"){
    send "TWD/TKT" +ticket411
    call "z_ATC_Refund"
}
if (ticket412 != "undefined"){
    send "TWD/TKT" +ticket412
    call "z_ATC_Refund"
}
if (ticket413 != "undefined"){
    send "TWD/TKT" +ticket413
    call "z_ATC_Refund"
}
if (ticket414 != "undefined"){
    send "TWD/TKT" +ticket414
    call "z_ATC_Refund"
}
if (ticket415 != "undefined"){
    send "TWD/TKT" +ticket415
    call "z_ATC_Refund"
}
if (ticket416 != "undefined"){
    send "TWD/TKT" +ticket416
    call "z_ATC_Refund"
}
if (ticket417 != "undefined"){
    send "TWD/TKT" +ticket417
    call "z_ATC_Refund"
}
if (ticket418 != "undefined"){
    send "TWD/TKT" +ticket418
    call "z_ATC_Refund"
}
if (ticket419 != "undefined"){
    send "TWD/TKT" +ticket419
    call "z_ATC_Refund"
}
if (ticket420 != "undefined"){
    send "TWD/TKT" +ticket420
    call "z_ATC_Refund"
}
if (ticket421 != "undefined"){
    send "TWD/TKT" +ticket421
    call "z_ATC_Refund"
}
if (ticket422 != "undefined"){
    send "TWD/TKT" +ticket422
    call "z_ATC_Refund"
}
if (ticket423 != "undefined"){
    send "TWD/TKT" +ticket423
    call "z_ATC_Refund"
}
if (ticket424 != "undefined"){
    send "TWD/TKT" +ticket424
    call "z_ATC_Refund"
}
if (ticket425 != "undefined"){
    send "TWD/TKT" +ticket425
    call "z_ATC_Refund"
}
if (ticket426 != "undefined"){
    send "TWD/TKT" +ticket426
    call "z_ATC_Refund"
}
if (ticket427 != "undefined"){
    send "TWD/TKT" +ticket427
    call "z_ATC_Refund"
}
if (ticket428 != "undefined"){
    send "TWD/TKT" +ticket428
    call "z_ATC_Refund"
}
if (ticket429 != "undefined"){
    send "TWD/TKT" +ticket429
    call "z_ATC_Refund"
}
if (ticket430 != "undefined"){
    send "TWD/TKT" +ticket430
    call "z_ATC_Refund"
}
if (ticket431 != "undefined"){
    send "TWD/TKT" +ticket431
    call "z_ATC_Refund"
}
if (ticket432 != "undefined"){
    send "TWD/TKT" +ticket432
    call "z_ATC_Refund"
}
if (ticket433 != "undefined"){
    send "TWD/TKT" +ticket433
    call "z_ATC_Refund"
}
if (ticket434 != "undefined"){
    send "TWD/TKT" +ticket434
    call "z_ATC_Refund"
}
if (ticket435 != "undefined"){
    send "TWD/TKT" +ticket435
    call "z_ATC_Refund"
}
if (ticket436 != "undefined"){
    send "TWD/TKT" +ticket436
    call "z_ATC_Refund"
}
if (ticket437 != "undefined"){
    send "TWD/TKT" +ticket437
    call "z_ATC_Refund"
}
if (ticket438 != "undefined"){
    send "TWD/TKT" +ticket438
    call "z_ATC_Refund"
}
if (ticket439 != "undefined"){
    send "TWD/TKT" +ticket439
    call "z_ATC_Refund"
}
if (ticket440 != "undefined"){
    send "TWD/TKT" +ticket440
    call "z_ATC_Refund"
}
if (ticket441 != "undefined"){
    send "TWD/TKT" +ticket441
    call "z_ATC_Refund"
}
if (ticket442 != "undefined"){
    send "TWD/TKT" +ticket442
    call "z_ATC_Refund"
}
if (ticket443 != "undefined"){
    send "TWD/TKT" +ticket443
    call "z_ATC_Refund"
}
if (ticket444 != "undefined"){
    send "TWD/TKT" +ticket444
    call "z_ATC_Refund"
}
if (ticket445 != "undefined"){
    send "TWD/TKT" +ticket445
    call "z_ATC_Refund"
}
if (ticket446 != "undefined"){
    send "TWD/TKT" +ticket446
    call "z_ATC_Refund"
}
if (ticket447 != "undefined"){
    send "TWD/TKT" +ticket447
    call "z_ATC_Refund"
}
if (ticket448 != "undefined"){
    send "TWD/TKT" +ticket448
    call "z_ATC_Refund"
}
if (ticket449 != "undefined"){
    send "TWD/TKT" +ticket449
    call "z_ATC_Refund"
}
if (ticket450 != "undefined"){
    send "TWD/TKT" +ticket450
    call "z_ATC_Refund"
}
if (ticket451 != "undefined"){
    send "TWD/TKT" +ticket451
    call "z_ATC_Refund"
}
if (ticket452 != "undefined"){
    send "TWD/TKT" +ticket452
    call "z_ATC_Refund"
}
if (ticket453 != "undefined"){
    send "TWD/TKT" +ticket453
    call "z_ATC_Refund"
}
if (ticket454 != "undefined"){
    send "TWD/TKT" +ticket454
    call "z_ATC_Refund"
}
if (ticket455 != "undefined"){
    send "TWD/TKT" +ticket455
    call "z_ATC_Refund"
}
if (ticket456 != "undefined"){
    send "TWD/TKT" +ticket456
    call "z_ATC_Refund"
}
if (ticket457 != "undefined"){
    send "TWD/TKT" +ticket457
    call "z_ATC_Refund"
}
if (ticket458 != "undefined"){
    send "TWD/TKT" +ticket458
    call "z_ATC_Refund"
}
if (ticket459 != "undefined"){
    send "TWD/TKT" +ticket459
    call "z_ATC_Refund"
}
if (ticket460 != "undefined"){
    send "TWD/TKT" +ticket460
    call "z_ATC_Refund"
}
if (ticket461 != "undefined"){
    send "TWD/TKT" +ticket461
    call "z_ATC_Refund"
}
if (ticket462 != "undefined"){
    send "TWD/TKT" +ticket462
    call "z_ATC_Refund"
}
if (ticket463 != "undefined"){
    send "TWD/TKT" +ticket463
    call "z_ATC_Refund"
}
if (ticket464 != "undefined"){
    send "TWD/TKT" +ticket464
    call "z_ATC_Refund"
}
if (ticket465 != "undefined"){
    send "TWD/TKT" +ticket465
    call "z_ATC_Refund"
}
if (ticket466 != "undefined"){
    send "TWD/TKT" +ticket466
    call "z_ATC_Refund"
}
if (ticket467 != "undefined"){
    send "TWD/TKT" +ticket467
    call "z_ATC_Refund"
}
if (ticket468 != "undefined"){
    send "TWD/TKT" +ticket468
    call "z_ATC_Refund"
}
if (ticket469 != "undefined"){
    send "TWD/TKT" +ticket469
    call "z_ATC_Refund"
}
if (ticket470 != "undefined"){
    send "TWD/TKT" +ticket470
    call "z_ATC_Refund"
}
if (ticket471 != "undefined"){
    send "TWD/TKT" +ticket471
    call "z_ATC_Refund"
}
if (ticket472 != "undefined"){
    send "TWD/TKT" +ticket472
    call "z_ATC_Refund"
}
if (ticket473 != "undefined"){
    send "TWD/TKT" +ticket473
    call "z_ATC_Refund"
}
if (ticket474 != "undefined"){
    send "TWD/TKT" +ticket474
    call "z_ATC_Refund"
}
if (ticket475 != "undefined"){
    send "TWD/TKT" +ticket475
    call "z_ATC_Refund"
}
if (ticket476 != "undefined"){
    send "TWD/TKT" +ticket476
    call "z_ATC_Refund"
}
if (ticket477 != "undefined"){
    send "TWD/TKT" +ticket477
    call "z_ATC_Refund"
}
if (ticket478 != "undefined"){
    send "TWD/TKT" +ticket478
    call "z_ATC_Refund"
}
if (ticket479 != "undefined"){
    send "TWD/TKT" +ticket479
    call "z_ATC_Refund"
}
if (ticket480 != "undefined"){
    send "TWD/TKT" +ticket480
    call "z_ATC_Refund"
}
if (ticket481 != "undefined"){
    send "TWD/TKT" +ticket481
    call "z_ATC_Refund"
}
if (ticket482 != "undefined"){
    send "TWD/TKT" +ticket482
    call "z_ATC_Refund"
}
if (ticket483 != "undefined"){
    send "TWD/TKT" +ticket483
    call "z_ATC_Refund"
}
if (ticket484 != "undefined"){
    send "TWD/TKT" +ticket484
    call "z_ATC_Refund"
}
if (ticket485 != "undefined"){
    send "TWD/TKT" +ticket485
    call "z_ATC_Refund"
}
if (ticket486 != "undefined"){
    send "TWD/TKT" +ticket486
    call "z_ATC_Refund"
}
if (ticket487 != "undefined"){
    send "TWD/TKT" +ticket487
    call "z_ATC_Refund"
}
if (ticket488 != "undefined"){
    send "TWD/TKT" +ticket488
    call "z_ATC_Refund"
}
if (ticket489 != "undefined"){
    send "TWD/TKT" +ticket489
    call "z_ATC_Refund"
}
if (ticket490 != "undefined"){
    send "TWD/TKT" +ticket490
    call "z_ATC_Refund"
}
if (ticket491 != "undefined"){
    send "TWD/TKT" +ticket491
    call "z_ATC_Refund"
}
if (ticket492 != "undefined"){
    send "TWD/TKT" +ticket492
    call "z_ATC_Refund"
}
if (ticket493 != "undefined"){
    send "TWD/TKT" +ticket493
    call "z_ATC_Refund"
}
if (ticket494 != "undefined"){
    send "TWD/TKT" +ticket494
    call "z_ATC_Refund"
}
if (ticket495 != "undefined"){
    send "TWD/TKT" +ticket495
    call "z_ATC_Refund"
}
if (ticket496 != "undefined"){
    send "TWD/TKT" +ticket496
    call "z_ATC_Refund"
}
if (ticket497 != "undefined"){
    send "TWD/TKT" +ticket497
    call "z_ATC_Refund"
}
if (ticket498 != "undefined"){
    send "TWD/TKT" +ticket498
    call "z_ATC_Refund"
}
if (ticket499 != "undefined"){
    send "TWD/TKT" +ticket499
    call "z_ATC_Refund"
}
if (ticket500 != "undefined"){
    send "TWD/TKT" +ticket500
    call "z_ATC_Refund"
}
if (ticket501 != "undefined"){
    send "TWD/TKT" +ticket501
    call "z_ATC_Refund"
}
if (ticket502 != "undefined"){
    send "TWD/TKT" +ticket502
    call "z_ATC_Refund"
}
if (ticket503 != "undefined"){
    send "TWD/TKT" +ticket503
    call "z_ATC_Refund"
}
if (ticket504 != "undefined"){
    send "TWD/TKT" +ticket504
    call "z_ATC_Refund"
}
if (ticket505 != "undefined"){
    send "TWD/TKT" +ticket505
    call "z_ATC_Refund"
}
if (ticket506 != "undefined"){
    send "TWD/TKT" +ticket506
    call "z_ATC_Refund"
}
if (ticket507 != "undefined"){
    send "TWD/TKT" +ticket507
    call "z_ATC_Refund"
}
if (ticket508 != "undefined"){
    send "TWD/TKT" +ticket508
    call "z_ATC_Refund"
}
if (ticket509 != "undefined"){
    send "TWD/TKT" +ticket509
    call "z_ATC_Refund"
}
if (ticket510 != "undefined"){
    send "TWD/TKT" +ticket510
    call "z_ATC_Refund"
}
if (ticket511 != "undefined"){
    send "TWD/TKT" +ticket511
    call "z_ATC_Refund"
}
if (ticket512 != "undefined"){
    send "TWD/TKT" +ticket512
    call "z_ATC_Refund"
}
if (ticket513 != "undefined"){
    send "TWD/TKT" +ticket513
    call "z_ATC_Refund"
}
if (ticket514 != "undefined"){
    send "TWD/TKT" +ticket514
    call "z_ATC_Refund"
}
if (ticket515 != "undefined"){
    send "TWD/TKT" +ticket515
    call "z_ATC_Refund"
}
if (ticket516 != "undefined"){
    send "TWD/TKT" +ticket516
    call "z_ATC_Refund"
}
if (ticket517 != "undefined"){
    send "TWD/TKT" +ticket517
    call "z_ATC_Refund"
}
if (ticket518 != "undefined"){
    send "TWD/TKT" +ticket518
    call "z_ATC_Refund"
}
if (ticket519 != "undefined"){
    send "TWD/TKT" +ticket519
    call "z_ATC_Refund"
}
if (ticket520 != "undefined"){
    send "TWD/TKT" +ticket520
    call "z_ATC_Refund"
}
if (ticket521 != "undefined"){
    send "TWD/TKT" +ticket521
    call "z_ATC_Refund"
}
if (ticket522 != "undefined"){
    send "TWD/TKT" +ticket522
    call "z_ATC_Refund"
}
if (ticket523 != "undefined"){
    send "TWD/TKT" +ticket523
    call "z_ATC_Refund"
}
if (ticket524 != "undefined"){
    send "TWD/TKT" +ticket524
    call "z_ATC_Refund"
}
if (ticket525 != "undefined"){
    send "TWD/TKT" +ticket525
    call "z_ATC_Refund"
}
if (ticket526 != "undefined"){
    send "TWD/TKT" +ticket526
    call "z_ATC_Refund"
}
if (ticket527 != "undefined"){
    send "TWD/TKT" +ticket527
    call "z_ATC_Refund"
}
if (ticket528 != "undefined"){
    send "TWD/TKT" +ticket528
    call "z_ATC_Refund"
}
if (ticket529 != "undefined"){
    send "TWD/TKT" +ticket529
    call "z_ATC_Refund"
}
if (ticket530 != "undefined"){
    send "TWD/TKT" +ticket530
    call "z_ATC_Refund"
}
if (ticket531 != "undefined"){
    send "TWD/TKT" +ticket531
    call "z_ATC_Refund"
}
if (ticket532 != "undefined"){
    send "TWD/TKT" +ticket532
    call "z_ATC_Refund"
}
if (ticket533 != "undefined"){
    send "TWD/TKT" +ticket533
    call "z_ATC_Refund"
}
if (ticket534 != "undefined"){
    send "TWD/TKT" +ticket534
    call "z_ATC_Refund"
}
if (ticket535 != "undefined"){
    send "TWD/TKT" +ticket535
    call "z_ATC_Refund"
}
if (ticket536 != "undefined"){
    send "TWD/TKT" +ticket536
    call "z_ATC_Refund"
}
if (ticket537 != "undefined"){
    send "TWD/TKT" +ticket537
    call "z_ATC_Refund"
}
if (ticket538 != "undefined"){
    send "TWD/TKT" +ticket538
    call "z_ATC_Refund"
}
if (ticket539 != "undefined"){
    send "TWD/TKT" +ticket539
    call "z_ATC_Refund"
}
if (ticket540 != "undefined"){
    send "TWD/TKT" +ticket540
    call "z_ATC_Refund"
}
if (ticket541 != "undefined"){
    send "TWD/TKT" +ticket541
    call "z_ATC_Refund"
}
if (ticket542 != "undefined"){
    send "TWD/TKT" +ticket542
    call "z_ATC_Refund"
}
if (ticket543 != "undefined"){
    send "TWD/TKT" +ticket543
    call "z_ATC_Refund"
}
if (ticket544 != "undefined"){
    send "TWD/TKT" +ticket544
    call "z_ATC_Refund"
}
if (ticket545 != "undefined"){
    send "TWD/TKT" +ticket545
    call "z_ATC_Refund"
}
if (ticket546 != "undefined"){
    send "TWD/TKT" +ticket546
    call "z_ATC_Refund"
}
if (ticket547 != "undefined"){
    send "TWD/TKT" +ticket547
    call "z_ATC_Refund"
}
if (ticket548 != "undefined"){
    send "TWD/TKT" +ticket548
    call "z_ATC_Refund"
}
if (ticket549 != "undefined"){
    send "TWD/TKT" +ticket549
    call "z_ATC_Refund"
}
if (ticket550 != "undefined"){
    send "TWD/TKT" +ticket550
    call "z_ATC_Refund"
}
if (ticket551 != "undefined"){
    send "TWD/TKT" +ticket551
    call "z_ATC_Refund"
}
if (ticket552 != "undefined"){
    send "TWD/TKT" +ticket552
    call "z_ATC_Refund"
}
if (ticket553 != "undefined"){
    send "TWD/TKT" +ticket553
    call "z_ATC_Refund"
}
if (ticket554 != "undefined"){
    send "TWD/TKT" +ticket554
    call "z_ATC_Refund"
}
if (ticket555 != "undefined"){
    send "TWD/TKT" +ticket555
    call "z_ATC_Refund"
}
if (ticket556 != "undefined"){
    send "TWD/TKT" +ticket556
    call "z_ATC_Refund"
}
if (ticket557 != "undefined"){
    send "TWD/TKT" +ticket557
    call "z_ATC_Refund"
}
if (ticket558 != "undefined"){
    send "TWD/TKT" +ticket558
    call "z_ATC_Refund"
}
if (ticket559 != "undefined"){
    send "TWD/TKT" +ticket559
    call "z_ATC_Refund"
}
if (ticket560 != "undefined"){
    send "TWD/TKT" +ticket560
    call "z_ATC_Refund"
}
if (ticket561 != "undefined"){
    send "TWD/TKT" +ticket561
    call "z_ATC_Refund"
}
if (ticket562 != "undefined"){
    send "TWD/TKT" +ticket562
    call "z_ATC_Refund"
}
if (ticket563 != "undefined"){
    send "TWD/TKT" +ticket563
    call "z_ATC_Refund"
}
if (ticket564 != "undefined"){
    send "TWD/TKT" +ticket564
    call "z_ATC_Refund"
}
if (ticket565 != "undefined"){
    send "TWD/TKT" +ticket565
    call "z_ATC_Refund"
}
if (ticket566 != "undefined"){
    send "TWD/TKT" +ticket566
    call "z_ATC_Refund"
}
if (ticket567 != "undefined"){
    send "TWD/TKT" +ticket567
    call "z_ATC_Refund"
}
if (ticket568 != "undefined"){
    send "TWD/TKT" +ticket568
    call "z_ATC_Refund"
}
if (ticket569 != "undefined"){
    send "TWD/TKT" +ticket569
    call "z_ATC_Refund"
}
if (ticket570 != "undefined"){
    send "TWD/TKT" +ticket570
    call "z_ATC_Refund"
}
if (ticket571 != "undefined"){
    send "TWD/TKT" +ticket571
    call "z_ATC_Refund"
}
if (ticket572 != "undefined"){
    send "TWD/TKT" +ticket572
    call "z_ATC_Refund"
}
if (ticket573 != "undefined"){
    send "TWD/TKT" +ticket573
    call "z_ATC_Refund"
}
if (ticket574 != "undefined"){
    send "TWD/TKT" +ticket574
    call "z_ATC_Refund"
}
if (ticket575 != "undefined"){
    send "TWD/TKT" +ticket575
    call "z_ATC_Refund"
}
if (ticket576 != "undefined"){
    send "TWD/TKT" +ticket576
    call "z_ATC_Refund"
}
if (ticket577 != "undefined"){
    send "TWD/TKT" +ticket577
    call "z_ATC_Refund"
}
if (ticket578 != "undefined"){
    send "TWD/TKT" +ticket578
    call "z_ATC_Refund"
}
if (ticket579 != "undefined"){
    send "TWD/TKT" +ticket579
    call "z_ATC_Refund"
}
if (ticket580 != "undefined"){
    send "TWD/TKT" +ticket580
    call "z_ATC_Refund"
}
if (ticket581 != "undefined"){
    send "TWD/TKT" +ticket581
    call "z_ATC_Refund"
}
if (ticket582 != "undefined"){
    send "TWD/TKT" +ticket582
    call "z_ATC_Refund"
}
if (ticket583 != "undefined"){
    send "TWD/TKT" +ticket583
    call "z_ATC_Refund"
}
if (ticket584 != "undefined"){
    send "TWD/TKT" +ticket584
    call "z_ATC_Refund"
}
if (ticket585 != "undefined"){
    send "TWD/TKT" +ticket585
    call "z_ATC_Refund"
}
if (ticket586 != "undefined"){
    send "TWD/TKT" +ticket586
    call "z_ATC_Refund"
}
if (ticket587 != "undefined"){
    send "TWD/TKT" +ticket587
    call "z_ATC_Refund"
}
if (ticket588 != "undefined"){
    send "TWD/TKT" +ticket588
    call "z_ATC_Refund"
}
if (ticket589 != "undefined"){
    send "TWD/TKT" +ticket589
    call "z_ATC_Refund"
}
if (ticket590 != "undefined"){
    send "TWD/TKT" +ticket590
    call "z_ATC_Refund"
}
if (ticket591 != "undefined"){
    send "TWD/TKT" +ticket591
    call "z_ATC_Refund"
}
if (ticket592 != "undefined"){
    send "TWD/TKT" +ticket592
    call "z_ATC_Refund"
}
if (ticket593 != "undefined"){
    send "TWD/TKT" +ticket593
    call "z_ATC_Refund"
}
if (ticket594 != "undefined"){
    send "TWD/TKT" +ticket594
    call "z_ATC_Refund"
}
if (ticket595 != "undefined"){
    send "TWD/TKT" +ticket595
    call "z_ATC_Refund"
}
if (ticket596 != "undefined"){
    send "TWD/TKT" +ticket596
    call "z_ATC_Refund"
}
if (ticket597 != "undefined"){
    send "TWD/TKT" +ticket597
    call "z_ATC_Refund"
}
if (ticket598 != "undefined"){
    send "TWD/TKT" +ticket598
    call "z_ATC_Refund"
}
if (ticket599 != "undefined"){
    send "TWD/TKT" +ticket599
    call "z_ATC_Refund"
}
if (ticket600 != "undefined"){
    send "TWD/TKT" +ticket600
    call "z_ATC_Refund"
}
if (ticket601 != "undefined"){
    send "TWD/TKT" +ticket601
    call "z_ATC_Refund"
}
if (ticket602 != "undefined"){
    send "TWD/TKT" +ticket602
    call "z_ATC_Refund"
}
if (ticket603 != "undefined"){
    send "TWD/TKT" +ticket603
    call "z_ATC_Refund"
}
if (ticket604 != "undefined"){
    send "TWD/TKT" +ticket604
    call "z_ATC_Refund"
}
if (ticket605 != "undefined"){
    send "TWD/TKT" +ticket605
    call "z_ATC_Refund"
}
if (ticket606 != "undefined"){
    send "TWD/TKT" +ticket606
    call "z_ATC_Refund"
}
if (ticket607 != "undefined"){
    send "TWD/TKT" +ticket607
    call "z_ATC_Refund"
}
if (ticket608 != "undefined"){
    send "TWD/TKT" +ticket608
    call "z_ATC_Refund"
}
if (ticket609 != "undefined"){
    send "TWD/TKT" +ticket609
    call "z_ATC_Refund"
}
if (ticket610 != "undefined"){
    send "TWD/TKT" +ticket610
    call "z_ATC_Refund"
}
if (ticket611 != "undefined"){
    send "TWD/TKT" +ticket611
    call "z_ATC_Refund"
}
if (ticket612 != "undefined"){
    send "TWD/TKT" +ticket612
    call "z_ATC_Refund"
}
if (ticket613 != "undefined"){
    send "TWD/TKT" +ticket613
    call "z_ATC_Refund"
}
if (ticket614 != "undefined"){
    send "TWD/TKT" +ticket614
    call "z_ATC_Refund"
}
if (ticket615 != "undefined"){
    send "TWD/TKT" +ticket615
    call "z_ATC_Refund"
}
if (ticket616 != "undefined"){
    send "TWD/TKT" +ticket616
    call "z_ATC_Refund"
}
if (ticket617 != "undefined"){
    send "TWD/TKT" +ticket617
    call "z_ATC_Refund"
}
if (ticket618 != "undefined"){
    send "TWD/TKT" +ticket618
    call "z_ATC_Refund"
}
if (ticket619 != "undefined"){
    send "TWD/TKT" +ticket619
    call "z_ATC_Refund"
}
if (ticket620 != "undefined"){
    send "TWD/TKT" +ticket620
    call "z_ATC_Refund"
}
if (ticket621 != "undefined"){
    send "TWD/TKT" +ticket621
    call "z_ATC_Refund"
}
if (ticket622 != "undefined"){
    send "TWD/TKT" +ticket622
    call "z_ATC_Refund"
}
if (ticket623 != "undefined"){
    send "TWD/TKT" +ticket623
    call "z_ATC_Refund"
}
if (ticket624 != "undefined"){
    send "TWD/TKT" +ticket624
    call "z_ATC_Refund"
}
if (ticket625 != "undefined"){
    send "TWD/TKT" +ticket625
    call "z_ATC_Refund"
}
if (ticket626 != "undefined"){
    send "TWD/TKT" +ticket626
    call "z_ATC_Refund"
}
if (ticket627 != "undefined"){
    send "TWD/TKT" +ticket627
    call "z_ATC_Refund"
}
if (ticket628 != "undefined"){
    send "TWD/TKT" +ticket628
    call "z_ATC_Refund"
}
if (ticket629 != "undefined"){
    send "TWD/TKT" +ticket629
    call "z_ATC_Refund"
}
if (ticket630 != "undefined"){
    send "TWD/TKT" +ticket630
    call "z_ATC_Refund"
}
if (ticket631 != "undefined"){
    send "TWD/TKT" +ticket631
    call "z_ATC_Refund"
}
if (ticket632 != "undefined"){
    send "TWD/TKT" +ticket632
    call "z_ATC_Refund"
}
if (ticket633 != "undefined"){
    send "TWD/TKT" +ticket633
    call "z_ATC_Refund"
}
if (ticket634 != "undefined"){
    send "TWD/TKT" +ticket634
    call "z_ATC_Refund"
}
if (ticket635 != "undefined"){
    send "TWD/TKT" +ticket635
    call "z_ATC_Refund"
}
if (ticket636 != "undefined"){
    send "TWD/TKT" +ticket636
    call "z_ATC_Refund"
}
if (ticket637 != "undefined"){
    send "TWD/TKT" +ticket637
    call "z_ATC_Refund"
}
if (ticket638 != "undefined"){
    send "TWD/TKT" +ticket638
    call "z_ATC_Refund"
}
if (ticket639 != "undefined"){
    send "TWD/TKT" +ticket639
    call "z_ATC_Refund"
}
if (ticket640 != "undefined"){
    send "TWD/TKT" +ticket640
    call "z_ATC_Refund"
}
if (ticket641 != "undefined"){
    send "TWD/TKT" +ticket641
    call "z_ATC_Refund"
}
if (ticket642 != "undefined"){
    send "TWD/TKT" +ticket642
    call "z_ATC_Refund"
}
if (ticket643 != "undefined"){
    send "TWD/TKT" +ticket643
    call "z_ATC_Refund"
}
if (ticket644 != "undefined"){
    send "TWD/TKT" +ticket644
    call "z_ATC_Refund"
}
if (ticket645 != "undefined"){
    send "TWD/TKT" +ticket645
    call "z_ATC_Refund"
}
if (ticket646 != "undefined"){
    send "TWD/TKT" +ticket646
    call "z_ATC_Refund"
}
if (ticket647 != "undefined"){
    send "TWD/TKT" +ticket647
    call "z_ATC_Refund"
}
if (ticket648 != "undefined"){
    send "TWD/TKT" +ticket648
    call "z_ATC_Refund"
}
if (ticket649 != "undefined"){
    send "TWD/TKT" +ticket649
    call "z_ATC_Refund"
}
if (ticket650 != "undefined"){
    send "TWD/TKT" +ticket650
    call "z_ATC_Refund"
}
if (ticket651 != "undefined"){
    send "TWD/TKT" +ticket651
    call "z_ATC_Refund"
}
if (ticket652 != "undefined"){
    send "TWD/TKT" +ticket652
    call "z_ATC_Refund"
}
if (ticket653 != "undefined"){
    send "TWD/TKT" +ticket653
    call "z_ATC_Refund"
}
if (ticket654 != "undefined"){
    send "TWD/TKT" +ticket654
    call "z_ATC_Refund"
}
if (ticket655 != "undefined"){
    send "TWD/TKT" +ticket655
    call "z_ATC_Refund"
}
if (ticket656 != "undefined"){
    send "TWD/TKT" +ticket656
    call "z_ATC_Refund"
}
if (ticket657 != "undefined"){
    send "TWD/TKT" +ticket657
    call "z_ATC_Refund"
}
if (ticket658 != "undefined"){
    send "TWD/TKT" +ticket658
    call "z_ATC_Refund"
}
if (ticket659 != "undefined"){
    send "TWD/TKT" +ticket659
    call "z_ATC_Refund"
}
if (ticket660 != "undefined"){
    send "TWD/TKT" +ticket660
    call "z_ATC_Refund"
}
if (ticket661 != "undefined"){
    send "TWD/TKT" +ticket661
    call "z_ATC_Refund"
}
if (ticket662 != "undefined"){
    send "TWD/TKT" +ticket662
    call "z_ATC_Refund"
}
if (ticket663 != "undefined"){
    send "TWD/TKT" +ticket663
    call "z_ATC_Refund"
}
if (ticket664 != "undefined"){
    send "TWD/TKT" +ticket664
    call "z_ATC_Refund"
}
if (ticket665 != "undefined"){
    send "TWD/TKT" +ticket665
    call "z_ATC_Refund"
}
if (ticket666 != "undefined"){
    send "TWD/TKT" +ticket666
    call "z_ATC_Refund"
}
if (ticket667 != "undefined"){
    send "TWD/TKT" +ticket667
    call "z_ATC_Refund"
}
if (ticket668 != "undefined"){
    send "TWD/TKT" +ticket668
    call "z_ATC_Refund"
}
if (ticket669 != "undefined"){
    send "TWD/TKT" +ticket669
    call "z_ATC_Refund"
}
if (ticket670 != "undefined"){
    send "TWD/TKT" +ticket670
    call "z_ATC_Refund"
}
if (ticket671 != "undefined"){
    send "TWD/TKT" +ticket671
    call "z_ATC_Refund"
}
if (ticket672 != "undefined"){
    send "TWD/TKT" +ticket672
    call "z_ATC_Refund"
}
if (ticket673 != "undefined"){
    send "TWD/TKT" +ticket673
    call "z_ATC_Refund"
}
if (ticket674 != "undefined"){
    send "TWD/TKT" +ticket674
    call "z_ATC_Refund"
}
if (ticket675 != "undefined"){
    send "TWD/TKT" +ticket675
    call "z_ATC_Refund"
}
if (ticket676 != "undefined"){
    send "TWD/TKT" +ticket676
    call "z_ATC_Refund"
}
if (ticket677 != "undefined"){
    send "TWD/TKT" +ticket677
    call "z_ATC_Refund"
}
if (ticket678 != "undefined"){
    send "TWD/TKT" +ticket678
    call "z_ATC_Refund"
}
if (ticket679 != "undefined"){
    send "TWD/TKT" +ticket679
    call "z_ATC_Refund"
}
if (ticket680 != "undefined"){
    send "TWD/TKT" +ticket680
    call "z_ATC_Refund"
}
if (ticket681 != "undefined"){
    send "TWD/TKT" +ticket681
    call "z_ATC_Refund"
}
if (ticket682 != "undefined"){
    send "TWD/TKT" +ticket682
    call "z_ATC_Refund"
}
if (ticket683 != "undefined"){
    send "TWD/TKT" +ticket683
    call "z_ATC_Refund"
}
if (ticket684 != "undefined"){
    send "TWD/TKT" +ticket684
    call "z_ATC_Refund"
}
if (ticket685 != "undefined"){
    send "TWD/TKT" +ticket685
    call "z_ATC_Refund"
}
if (ticket686 != "undefined"){
    send "TWD/TKT" +ticket686
    call "z_ATC_Refund"
}
if (ticket687 != "undefined"){
    send "TWD/TKT" +ticket687
    call "z_ATC_Refund"
}
if (ticket688 != "undefined"){
    send "TWD/TKT" +ticket688
    call "z_ATC_Refund"
}
if (ticket689 != "undefined"){
    send "TWD/TKT" +ticket689
    call "z_ATC_Refund"
}
if (ticket690 != "undefined"){
    send "TWD/TKT" +ticket690
    call "z_ATC_Refund"
}
if (ticket691 != "undefined"){
    send "TWD/TKT" +ticket691
    call "z_ATC_Refund"
}
if (ticket692 != "undefined"){
    send "TWD/TKT" +ticket692
    call "z_ATC_Refund"
}
if (ticket693 != "undefined"){
    send "TWD/TKT" +ticket693
    call "z_ATC_Refund"
}
if (ticket694 != "undefined"){
    send "TWD/TKT" +ticket694
    call "z_ATC_Refund"
}
if (ticket695 != "undefined"){
    send "TWD/TKT" +ticket695
    call "z_ATC_Refund"
}
if (ticket696 != "undefined"){
    send "TWD/TKT" +ticket696
    call "z_ATC_Refund"
}
if (ticket697 != "undefined"){
    send "TWD/TKT" +ticket697
    call "z_ATC_Refund"
}
if (ticket698 != "undefined"){
    send "TWD/TKT" +ticket698
    call "z_ATC_Refund"
}
if (ticket699 != "undefined"){
    send "TWD/TKT" +ticket699
    call "z_ATC_Refund"
}
if (ticket700 != "undefined"){
    send "TWD/TKT" +ticket700
    call "z_ATC_Refund"
}
if (ticket701 != "undefined"){
    send "TWD/TKT" +ticket701
    call "z_ATC_Refund"
}
if (ticket702 != "undefined"){
    send "TWD/TKT" +ticket702
    call "z_ATC_Refund"
}
if (ticket703 != "undefined"){
    send "TWD/TKT" +ticket703
    call "z_ATC_Refund"
}
if (ticket704 != "undefined"){
    send "TWD/TKT" +ticket704
    call "z_ATC_Refund"
}
if (ticket705 != "undefined"){
    send "TWD/TKT" +ticket705
    call "z_ATC_Refund"
}
if (ticket706 != "undefined"){
    send "TWD/TKT" +ticket706
    call "z_ATC_Refund"
}
if (ticket707 != "undefined"){
    send "TWD/TKT" +ticket707
    call "z_ATC_Refund"
}
if (ticket708 != "undefined"){
    send "TWD/TKT" +ticket708
    call "z_ATC_Refund"
}
if (ticket709 != "undefined"){
    send "TWD/TKT" +ticket709
    call "z_ATC_Refund"
}
if (ticket710 != "undefined"){
    send "TWD/TKT" +ticket710
    call "z_ATC_Refund"
}
if (ticket711 != "undefined"){
    send "TWD/TKT" +ticket711
    call "z_ATC_Refund"
}
if (ticket712 != "undefined"){
    send "TWD/TKT" +ticket712
    call "z_ATC_Refund"
}
if (ticket713 != "undefined"){
    send "TWD/TKT" +ticket713
    call "z_ATC_Refund"
}
if (ticket714 != "undefined"){
    send "TWD/TKT" +ticket714
    call "z_ATC_Refund"
}
if (ticket715 != "undefined"){
    send "TWD/TKT" +ticket715
    call "z_ATC_Refund"
}
if (ticket716 != "undefined"){
    send "TWD/TKT" +ticket716
    call "z_ATC_Refund"
}
if (ticket717 != "undefined"){
    send "TWD/TKT" +ticket717
    call "z_ATC_Refund"
}
if (ticket718 != "undefined"){
    send "TWD/TKT" +ticket718
    call "z_ATC_Refund"
}
if (ticket719 != "undefined"){
    send "TWD/TKT" +ticket719
    call "z_ATC_Refund"
}
if (ticket720 != "undefined"){
    send "TWD/TKT" +ticket720
    call "z_ATC_Refund"
}
if (ticket721 != "undefined"){
    send "TWD/TKT" +ticket721
    call "z_ATC_Refund"
}
if (ticket722 != "undefined"){
    send "TWD/TKT" +ticket722
    call "z_ATC_Refund"
}
if (ticket723 != "undefined"){
    send "TWD/TKT" +ticket723
    call "z_ATC_Refund"
}
if (ticket724 != "undefined"){
    send "TWD/TKT" +ticket724
    call "z_ATC_Refund"
}
if (ticket725 != "undefined"){
    send "TWD/TKT" +ticket725
    call "z_ATC_Refund"
}
if (ticket726 != "undefined"){
    send "TWD/TKT" +ticket726
    call "z_ATC_Refund"
}
if (ticket727 != "undefined"){
    send "TWD/TKT" +ticket727
    call "z_ATC_Refund"
}
if (ticket728 != "undefined"){
    send "TWD/TKT" +ticket728
    call "z_ATC_Refund"
}
if (ticket729 != "undefined"){
    send "TWD/TKT" +ticket729
    call "z_ATC_Refund"
}
if (ticket730 != "undefined"){
    send "TWD/TKT" +ticket730
    call "z_ATC_Refund"
}
if (ticket731 != "undefined"){
    send "TWD/TKT" +ticket731
    call "z_ATC_Refund"
}
if (ticket732 != "undefined"){
    send "TWD/TKT" +ticket732
    call "z_ATC_Refund"
}
if (ticket733 != "undefined"){
    send "TWD/TKT" +ticket733
    call "z_ATC_Refund"
}
if (ticket734 != "undefined"){
    send "TWD/TKT" +ticket734
    call "z_ATC_Refund"
}
if (ticket735 != "undefined"){
    send "TWD/TKT" +ticket735
    call "z_ATC_Refund"
}
if (ticket736 != "undefined"){
    send "TWD/TKT" +ticket736
    call "z_ATC_Refund"
}
if (ticket737 != "undefined"){
    send "TWD/TKT" +ticket737
    call "z_ATC_Refund"
}
if (ticket738 != "undefined"){
    send "TWD/TKT" +ticket738
    call "z_ATC_Refund"
}
if (ticket739 != "undefined"){
    send "TWD/TKT" +ticket739
    call "z_ATC_Refund"
}
if (ticket740 != "undefined"){
    send "TWD/TKT" +ticket740
    call "z_ATC_Refund"
}
if (ticket741 != "undefined"){
    send "TWD/TKT" +ticket741
    call "z_ATC_Refund"
}
if (ticket742 != "undefined"){
    send "TWD/TKT" +ticket742
    call "z_ATC_Refund"
}
if (ticket743 != "undefined"){
    send "TWD/TKT" +ticket743
    call "z_ATC_Refund"
}
if (ticket744 != "undefined"){
    send "TWD/TKT" +ticket744
    call "z_ATC_Refund"
}
if (ticket745 != "undefined"){
    send "TWD/TKT" +ticket745
    call "z_ATC_Refund"
}
if (ticket746 != "undefined"){
    send "TWD/TKT" +ticket746
    call "z_ATC_Refund"
}
if (ticket747 != "undefined"){
    send "TWD/TKT" +ticket747
    call "z_ATC_Refund"
}
if (ticket748 != "undefined"){
    send "TWD/TKT" +ticket748
    call "z_ATC_Refund"
}
if (ticket749 != "undefined"){
    send "TWD/TKT" +ticket749
    call "z_ATC_Refund"
}
if (ticket750 != "undefined"){
    send "TWD/TKT" +ticket750
    call "z_ATC_Refund"
}
if (ticket751 != "undefined"){
    send "TWD/TKT" +ticket751
    call "z_ATC_Refund"
}
if (ticket752 != "undefined"){
    send "TWD/TKT" +ticket752
    call "z_ATC_Refund"
}
if (ticket753 != "undefined"){
    send "TWD/TKT" +ticket753
    call "z_ATC_Refund"
}
if (ticket754 != "undefined"){
    send "TWD/TKT" +ticket754
    call "z_ATC_Refund"
}
if (ticket755 != "undefined"){
    send "TWD/TKT" +ticket755
    call "z_ATC_Refund"
}
if (ticket756 != "undefined"){
    send "TWD/TKT" +ticket756
    call "z_ATC_Refund"
}
if (ticket757 != "undefined"){
    send "TWD/TKT" +ticket757
    call "z_ATC_Refund"
}
if (ticket758 != "undefined"){
    send "TWD/TKT" +ticket758
    call "z_ATC_Refund"
}
if (ticket759 != "undefined"){
    send "TWD/TKT" +ticket759
    call "z_ATC_Refund"
}
if (ticket760 != "undefined"){
    send "TWD/TKT" +ticket760
    call "z_ATC_Refund"
}
if (ticket761 != "undefined"){
    send "TWD/TKT" +ticket761
    call "z_ATC_Refund"
}
if (ticket762 != "undefined"){
    send "TWD/TKT" +ticket762
    call "z_ATC_Refund"
}
if (ticket763 != "undefined"){
    send "TWD/TKT" +ticket763
    call "z_ATC_Refund"
}
if (ticket764 != "undefined"){
    send "TWD/TKT" +ticket764
    call "z_ATC_Refund"
}
if (ticket765 != "undefined"){
    send "TWD/TKT" +ticket765
    call "z_ATC_Refund"
}
if (ticket766 != "undefined"){
    send "TWD/TKT" +ticket766
    call "z_ATC_Refund"
}
if (ticket767 != "undefined"){
    send "TWD/TKT" +ticket767
    call "z_ATC_Refund"
}
if (ticket768 != "undefined"){
    send "TWD/TKT" +ticket768
    call "z_ATC_Refund"
}
if (ticket769 != "undefined"){
    send "TWD/TKT" +ticket769
    call "z_ATC_Refund"
}
if (ticket770 != "undefined"){
    send "TWD/TKT" +ticket770
    call "z_ATC_Refund"
}
if (ticket771 != "undefined"){
    send "TWD/TKT" +ticket771
    call "z_ATC_Refund"
}
if (ticket772 != "undefined"){
    send "TWD/TKT" +ticket772
    call "z_ATC_Refund"
}
if (ticket773 != "undefined"){
    send "TWD/TKT" +ticket773
    call "z_ATC_Refund"
}
if (ticket774 != "undefined"){
    send "TWD/TKT" +ticket774
    call "z_ATC_Refund"
}
if (ticket775 != "undefined"){
    send "TWD/TKT" +ticket775
    call "z_ATC_Refund"
}
if (ticket776 != "undefined"){
    send "TWD/TKT" +ticket776
    call "z_ATC_Refund"
}
if (ticket777 != "undefined"){
    send "TWD/TKT" +ticket777
    call "z_ATC_Refund"
}
if (ticket778 != "undefined"){
    send "TWD/TKT" +ticket778
    call "z_ATC_Refund"
}
if (ticket779 != "undefined"){
    send "TWD/TKT" +ticket779
    call "z_ATC_Refund"
}
if (ticket780 != "undefined"){
    send "TWD/TKT" +ticket780
    call "z_ATC_Refund"
}
if (ticket781 != "undefined"){
    send "TWD/TKT" +ticket781
    call "z_ATC_Refund"
}
if (ticket782 != "undefined"){
    send "TWD/TKT" +ticket782
    call "z_ATC_Refund"
}
if (ticket783 != "undefined"){
    send "TWD/TKT" +ticket783
    call "z_ATC_Refund"
}
if (ticket784 != "undefined"){
    send "TWD/TKT" +ticket784
    call "z_ATC_Refund"
}
if (ticket785 != "undefined"){
    send "TWD/TKT" +ticket785
    call "z_ATC_Refund"
}
if (ticket786 != "undefined"){
    send "TWD/TKT" +ticket786
    call "z_ATC_Refund"
}
if (ticket787 != "undefined"){
    send "TWD/TKT" +ticket787
    call "z_ATC_Refund"
}
if (ticket788 != "undefined"){
    send "TWD/TKT" +ticket788
    call "z_ATC_Refund"
}
if (ticket789 != "undefined"){
    send "TWD/TKT" +ticket789
    call "z_ATC_Refund"
}
if (ticket790 != "undefined"){
    send "TWD/TKT" +ticket790
    call "z_ATC_Refund"
}
if (ticket791 != "undefined"){
    send "TWD/TKT" +ticket791
    call "z_ATC_Refund"
}
if (ticket792 != "undefined"){
    send "TWD/TKT" +ticket792
    call "z_ATC_Refund"
}
if (ticket793 != "undefined"){
    send "TWD/TKT" +ticket793
    call "z_ATC_Refund"
}
if (ticket794 != "undefined"){
    send "TWD/TKT" +ticket794
    call "z_ATC_Refund"
}
if (ticket795 != "undefined"){
    send "TWD/TKT" +ticket795
    call "z_ATC_Refund"
}
if (ticket796 != "undefined"){
    send "TWD/TKT" +ticket796
    call "z_ATC_Refund"
}
if (ticket797 != "undefined"){
    send "TWD/TKT" +ticket797
    call "z_ATC_Refund"
}
if (ticket798 != "undefined"){
    send "TWD/TKT" +ticket798
    call "z_ATC_Refund"
}
if (ticket799 != "undefined"){
    send "TWD/TKT" +ticket799
    call "z_ATC_Refund"
}
if (ticket800 != "undefined"){
    send "TWD/TKT" +ticket800
    call "z_ATC_Refund"
}
if (ticket801 != "undefined"){
    send "TWD/TKT" +ticket801
    call "z_ATC_Refund"
}
if (ticket802 != "undefined"){
    send "TWD/TKT" +ticket802
    call "z_ATC_Refund"
}
if (ticket803 != "undefined"){
    send "TWD/TKT" +ticket803
    call "z_ATC_Refund"
}
if (ticket804 != "undefined"){
    send "TWD/TKT" +ticket804
    call "z_ATC_Refund"
}
if (ticket805 != "undefined"){
    send "TWD/TKT" +ticket805
    call "z_ATC_Refund"
}
if (ticket806 != "undefined"){
    send "TWD/TKT" +ticket806
    call "z_ATC_Refund"
}
if (ticket807 != "undefined"){
    send "TWD/TKT" +ticket807
    call "z_ATC_Refund"
}
if (ticket808 != "undefined"){
    send "TWD/TKT" +ticket808
    call "z_ATC_Refund"
}
if (ticket809 != "undefined"){
    send "TWD/TKT" +ticket809
    call "z_ATC_Refund"
}
if (ticket810 != "undefined"){
    send "TWD/TKT" +ticket810
    call "z_ATC_Refund"
}
if (ticket811 != "undefined"){
    send "TWD/TKT" +ticket811
    call "z_ATC_Refund"
}
if (ticket812 != "undefined"){
    send "TWD/TKT" +ticket812
    call "z_ATC_Refund"
}
if (ticket813 != "undefined"){
    send "TWD/TKT" +ticket813
    call "z_ATC_Refund"
}
if (ticket814 != "undefined"){
    send "TWD/TKT" +ticket814
    call "z_ATC_Refund"
}
if (ticket815 != "undefined"){
    send "TWD/TKT" +ticket815
    call "z_ATC_Refund"
}
if (ticket816 != "undefined"){
    send "TWD/TKT" +ticket816
    call "z_ATC_Refund"
}
if (ticket817 != "undefined"){
    send "TWD/TKT" +ticket817
    call "z_ATC_Refund"
}
if (ticket818 != "undefined"){
    send "TWD/TKT" +ticket818
    call "z_ATC_Refund"
}
if (ticket819 != "undefined"){
    send "TWD/TKT" +ticket819
    call "z_ATC_Refund"
}
if (ticket820 != "undefined"){
    send "TWD/TKT" +ticket820
    call "z_ATC_Refund"
}
if (ticket821 != "undefined"){
    send "TWD/TKT" +ticket821
    call "z_ATC_Refund"
}
if (ticket822 != "undefined"){
    send "TWD/TKT" +ticket822
    call "z_ATC_Refund"
}
if (ticket823 != "undefined"){
    send "TWD/TKT" +ticket823
    call "z_ATC_Refund"
}
if (ticket824 != "undefined"){
    send "TWD/TKT" +ticket824
    call "z_ATC_Refund"
}
if (ticket825 != "undefined"){
    send "TWD/TKT" +ticket825
    call "z_ATC_Refund"
}
if (ticket826 != "undefined"){
    send "TWD/TKT" +ticket826
    call "z_ATC_Refund"
}
if (ticket827 != "undefined"){
    send "TWD/TKT" +ticket827
    call "z_ATC_Refund"
}
if (ticket828 != "undefined"){
    send "TWD/TKT" +ticket828
    call "z_ATC_Refund"
}
if (ticket829 != "undefined"){
    send "TWD/TKT" +ticket829
    call "z_ATC_Refund"
}
if (ticket830 != "undefined"){
    send "TWD/TKT" +ticket830
    call "z_ATC_Refund"
}
if (ticket831 != "undefined"){
    send "TWD/TKT" +ticket831
    call "z_ATC_Refund"
}
if (ticket832 != "undefined"){
    send "TWD/TKT" +ticket832
    call "z_ATC_Refund"
}
if (ticket833 != "undefined"){
    send "TWD/TKT" +ticket833
    call "z_ATC_Refund"
}
if (ticket834 != "undefined"){
    send "TWD/TKT" +ticket834
    call "z_ATC_Refund"
}
if (ticket835 != "undefined"){
    send "TWD/TKT" +ticket835
    call "z_ATC_Refund"
}
if (ticket836 != "undefined"){
    send "TWD/TKT" +ticket836
    call "z_ATC_Refund"
}
if (ticket837 != "undefined"){
    send "TWD/TKT" +ticket837
    call "z_ATC_Refund"
}
if (ticket838 != "undefined"){
    send "TWD/TKT" +ticket838
    call "z_ATC_Refund"
}
if (ticket839 != "undefined"){
    send "TWD/TKT" +ticket839
    call "z_ATC_Refund"
}
if (ticket840 != "undefined"){
    send "TWD/TKT" +ticket840
    call "z_ATC_Refund"
}
if (ticket841 != "undefined"){
    send "TWD/TKT" +ticket841
    call "z_ATC_Refund"
}
if (ticket842 != "undefined"){
    send "TWD/TKT" +ticket842
    call "z_ATC_Refund"
}
if (ticket843 != "undefined"){
    send "TWD/TKT" +ticket843
    call "z_ATC_Refund"
}
if (ticket844 != "undefined"){
    send "TWD/TKT" +ticket844
    call "z_ATC_Refund"
}
if (ticket845 != "undefined"){
    send "TWD/TKT" +ticket845
    call "z_ATC_Refund"
}
if (ticket846 != "undefined"){
    send "TWD/TKT" +ticket846
    call "z_ATC_Refund"
}
if (ticket847 != "undefined"){
    send "TWD/TKT" +ticket847
    call "z_ATC_Refund"
}
if (ticket848 != "undefined"){
    send "TWD/TKT" +ticket848
    call "z_ATC_Refund"
}
if (ticket849 != "undefined"){
    send "TWD/TKT" +ticket849
    call "z_ATC_Refund"
}
if (ticket850 != "undefined"){
    send "TWD/TKT" +ticket850
    call "z_ATC_Refund"
}
if (ticket851 != "undefined"){
    send "TWD/TKT" +ticket851
    call "z_ATC_Refund"
}
if (ticket852 != "undefined"){
    send "TWD/TKT" +ticket852
    call "z_ATC_Refund"
}
if (ticket853 != "undefined"){
    send "TWD/TKT" +ticket853
    call "z_ATC_Refund"
}
if (ticket854 != "undefined"){
    send "TWD/TKT" +ticket854
    call "z_ATC_Refund"
}
if (ticket855 != "undefined"){
    send "TWD/TKT" +ticket855
    call "z_ATC_Refund"
}
if (ticket856 != "undefined"){
    send "TWD/TKT" +ticket856
    call "z_ATC_Refund"
}
if (ticket857 != "undefined"){
    send "TWD/TKT" +ticket857
    call "z_ATC_Refund"
}
if (ticket858 != "undefined"){
    send "TWD/TKT" +ticket858
    call "z_ATC_Refund"
}
if (ticket859 != "undefined"){
    send "TWD/TKT" +ticket859
    call "z_ATC_Refund"
}
if (ticket860 != "undefined"){
    send "TWD/TKT" +ticket860
    call "z_ATC_Refund"
}
if (ticket861 != "undefined"){
    send "TWD/TKT" +ticket861
    call "z_ATC_Refund"
}
if (ticket862 != "undefined"){
    send "TWD/TKT" +ticket862
    call "z_ATC_Refund"
}
if (ticket863 != "undefined"){
    send "TWD/TKT" +ticket863
    call "z_ATC_Refund"
}
if (ticket864 != "undefined"){
    send "TWD/TKT" +ticket864
    call "z_ATC_Refund"
}
if (ticket865 != "undefined"){
    send "TWD/TKT" +ticket865
    call "z_ATC_Refund"
}
if (ticket866 != "undefined"){
    send "TWD/TKT" +ticket866
    call "z_ATC_Refund"
}
if (ticket867 != "undefined"){
    send "TWD/TKT" +ticket867
    call "z_ATC_Refund"
}
if (ticket868 != "undefined"){
    send "TWD/TKT" +ticket868
    call "z_ATC_Refund"
}
if (ticket869 != "undefined"){
    send "TWD/TKT" +ticket869
    call "z_ATC_Refund"
}
if (ticket870 != "undefined"){
    send "TWD/TKT" +ticket870
    call "z_ATC_Refund"
}
if (ticket871 != "undefined"){
    send "TWD/TKT" +ticket871
    call "z_ATC_Refund"
}
if (ticket872 != "undefined"){
    send "TWD/TKT" +ticket872
    call "z_ATC_Refund"
}
if (ticket873 != "undefined"){
    send "TWD/TKT" +ticket873
    call "z_ATC_Refund"
}
if (ticket874 != "undefined"){
    send "TWD/TKT" +ticket874
    call "z_ATC_Refund"
}
if (ticket875 != "undefined"){
    send "TWD/TKT" +ticket875
    call "z_ATC_Refund"
}
if (ticket876 != "undefined"){
    send "TWD/TKT" +ticket876
    call "z_ATC_Refund"
}
if (ticket877 != "undefined"){
    send "TWD/TKT" +ticket877
    call "z_ATC_Refund"
}
if (ticket878 != "undefined"){
    send "TWD/TKT" +ticket878
    call "z_ATC_Refund"
}
if (ticket879 != "undefined"){
    send "TWD/TKT" +ticket879
    call "z_ATC_Refund"
}
if (ticket880 != "undefined"){
    send "TWD/TKT" +ticket880
    call "z_ATC_Refund"
}
if (ticket881 != "undefined"){
    send "TWD/TKT" +ticket881
    call "z_ATC_Refund"
}
if (ticket882 != "undefined"){
    send "TWD/TKT" +ticket882
    call "z_ATC_Refund"
}
if (ticket883 != "undefined"){
    send "TWD/TKT" +ticket883
    call "z_ATC_Refund"
}
if (ticket884 != "undefined"){
    send "TWD/TKT" +ticket884
    call "z_ATC_Refund"
}
if (ticket885 != "undefined"){
    send "TWD/TKT" +ticket885
    call "z_ATC_Refund"
}
if (ticket886 != "undefined"){
    send "TWD/TKT" +ticket886
    call "z_ATC_Refund"
}
if (ticket887 != "undefined"){
    send "TWD/TKT" +ticket887
    call "z_ATC_Refund"
}
if (ticket888 != "undefined"){
    send "TWD/TKT" +ticket888
    call "z_ATC_Refund"
}
if (ticket889 != "undefined"){
    send "TWD/TKT" +ticket889
    call "z_ATC_Refund"
}
if (ticket890 != "undefined"){
    send "TWD/TKT" +ticket890
    call "z_ATC_Refund"
}
if (ticket891 != "undefined"){
    send "TWD/TKT" +ticket891
    call "z_ATC_Refund"
}
if (ticket892 != "undefined"){
    send "TWD/TKT" +ticket892
    call "z_ATC_Refund"
}
if (ticket893 != "undefined"){
    send "TWD/TKT" +ticket893
    call "z_ATC_Refund"
}
if (ticket894 != "undefined"){
    send "TWD/TKT" +ticket894
    call "z_ATC_Refund"
}
if (ticket895 != "undefined"){
    send "TWD/TKT" +ticket895
    call "z_ATC_Refund"
}
if (ticket896 != "undefined"){
    send "TWD/TKT" +ticket896
    call "z_ATC_Refund"
}
if (ticket897 != "undefined"){
    send "TWD/TKT" +ticket897
    call "z_ATC_Refund"
}
if (ticket898 != "undefined"){
    send "TWD/TKT" +ticket898
    call "z_ATC_Refund"
}
if (ticket899 != "undefined"){
    send "TWD/TKT" +ticket899
    call "z_ATC_Refund"
}
if (ticket900 != "undefined"){
    send "TWD/TKT" +ticket900
    call "z_ATC_Refund"
}
if (ticket901 != "undefined"){
    send "TWD/TKT" +ticket901
    call "z_ATC_Refund"
}
if (ticket902 != "undefined"){
    send "TWD/TKT" +ticket902
    call "z_ATC_Refund"
}
if (ticket903 != "undefined"){
    send "TWD/TKT" +ticket903
    call "z_ATC_Refund"
}
if (ticket904 != "undefined"){
    send "TWD/TKT" +ticket904
    call "z_ATC_Refund"
}
if (ticket905 != "undefined"){
    send "TWD/TKT" +ticket905
    call "z_ATC_Refund"
}
if (ticket906 != "undefined"){
    send "TWD/TKT" +ticket906
    call "z_ATC_Refund"
}
if (ticket907 != "undefined"){
    send "TWD/TKT" +ticket907
    call "z_ATC_Refund"
}
if (ticket908 != "undefined"){
    send "TWD/TKT" +ticket908
    call "z_ATC_Refund"
}
if (ticket909 != "undefined"){
    send "TWD/TKT" +ticket909
    call "z_ATC_Refund"
}
if (ticket910 != "undefined"){
    send "TWD/TKT" +ticket910
    call "z_ATC_Refund"
}
if (ticket911 != "undefined"){
    send "TWD/TKT" +ticket911
    call "z_ATC_Refund"
}
if (ticket912 != "undefined"){
    send "TWD/TKT" +ticket912
    call "z_ATC_Refund"
}
if (ticket913 != "undefined"){
    send "TWD/TKT" +ticket913
    call "z_ATC_Refund"
}
if (ticket914 != "undefined"){
    send "TWD/TKT" +ticket914
    call "z_ATC_Refund"
}
if (ticket915 != "undefined"){
    send "TWD/TKT" +ticket915
    call "z_ATC_Refund"
}
if (ticket916 != "undefined"){
    send "TWD/TKT" +ticket916
    call "z_ATC_Refund"
}
if (ticket917 != "undefined"){
    send "TWD/TKT" +ticket917
    call "z_ATC_Refund"
}
if (ticket918 != "undefined"){
    send "TWD/TKT" +ticket918
    call "z_ATC_Refund"
}
if (ticket919 != "undefined"){
    send "TWD/TKT" +ticket919
    call "z_ATC_Refund"
}
if (ticket920 != "undefined"){
    send "TWD/TKT" +ticket920
    call "z_ATC_Refund"
}
if (ticket921 != "undefined"){
    send "TWD/TKT" +ticket921
    call "z_ATC_Refund"
}
if (ticket922 != "undefined"){
    send "TWD/TKT" +ticket922
    call "z_ATC_Refund"
}
if (ticket923 != "undefined"){
    send "TWD/TKT" +ticket923
    call "z_ATC_Refund"
}
if (ticket924 != "undefined"){
    send "TWD/TKT" +ticket924
    call "z_ATC_Refund"
}
if (ticket925 != "undefined"){
    send "TWD/TKT" +ticket925
    call "z_ATC_Refund"
}
if (ticket926 != "undefined"){
    send "TWD/TKT" +ticket926
    call "z_ATC_Refund"
}
if (ticket927 != "undefined"){
    send "TWD/TKT" +ticket927
    call "z_ATC_Refund"
}
if (ticket928 != "undefined"){
    send "TWD/TKT" +ticket928
    call "z_ATC_Refund"
}
if (ticket929 != "undefined"){
    send "TWD/TKT" +ticket929
    call "z_ATC_Refund"
}
if (ticket930 != "undefined"){
    send "TWD/TKT" +ticket930
    call "z_ATC_Refund"
}
if (ticket931 != "undefined"){
    send "TWD/TKT" +ticket931
    call "z_ATC_Refund"
}
if (ticket932 != "undefined"){
    send "TWD/TKT" +ticket932
    call "z_ATC_Refund"
}
if (ticket933 != "undefined"){
    send "TWD/TKT" +ticket933
    call "z_ATC_Refund"
}
if (ticket934 != "undefined"){
    send "TWD/TKT" +ticket934
    call "z_ATC_Refund"
}
if (ticket935 != "undefined"){
    send "TWD/TKT" +ticket935
    call "z_ATC_Refund"
}
if (ticket936 != "undefined"){
    send "TWD/TKT" +ticket936
    call "z_ATC_Refund"
}
if (ticket937 != "undefined"){
    send "TWD/TKT" +ticket937
    call "z_ATC_Refund"
}
if (ticket938 != "undefined"){
    send "TWD/TKT" +ticket938
    call "z_ATC_Refund"
}
if (ticket939 != "undefined"){
    send "TWD/TKT" +ticket939
    call "z_ATC_Refund"
}
if (ticket940 != "undefined"){
    send "TWD/TKT" +ticket940
    call "z_ATC_Refund"
}
if (ticket941 != "undefined"){
    send "TWD/TKT" +ticket941
    call "z_ATC_Refund"
}
if (ticket942 != "undefined"){
    send "TWD/TKT" +ticket942
    call "z_ATC_Refund"
}
if (ticket943 != "undefined"){
    send "TWD/TKT" +ticket943
    call "z_ATC_Refund"
}
if (ticket944 != "undefined"){
    send "TWD/TKT" +ticket944
    call "z_ATC_Refund"
}
if (ticket945 != "undefined"){
    send "TWD/TKT" +ticket945
    call "z_ATC_Refund"
}
if (ticket946 != "undefined"){
    send "TWD/TKT" +ticket946
    call "z_ATC_Refund"
}
if (ticket947 != "undefined"){
    send "TWD/TKT" +ticket947
    call "z_ATC_Refund"
}
if (ticket948 != "undefined"){
    send "TWD/TKT" +ticket948
    call "z_ATC_Refund"
}
if (ticket949 != "undefined"){
    send "TWD/TKT" +ticket949
    call "z_ATC_Refund"
}
if (ticket950 != "undefined"){
    send "TWD/TKT" +ticket950
    call "z_ATC_Refund"
}
if (ticket951 != "undefined"){
    send "TWD/TKT" +ticket951
    call "z_ATC_Refund"
}
if (ticket952 != "undefined"){
    send "TWD/TKT" +ticket952
    call "z_ATC_Refund"
}
if (ticket953 != "undefined"){
    send "TWD/TKT" +ticket953
    call "z_ATC_Refund"
}
if (ticket954 != "undefined"){
    send "TWD/TKT" +ticket954
    call "z_ATC_Refund"
}
if (ticket955 != "undefined"){
    send "TWD/TKT" +ticket955
    call "z_ATC_Refund"
}
if (ticket956 != "undefined"){
    send "TWD/TKT" +ticket956
    call "z_ATC_Refund"
}
if (ticket957 != "undefined"){
    send "TWD/TKT" +ticket957
    call "z_ATC_Refund"
}
if (ticket958 != "undefined"){
    send "TWD/TKT" +ticket958
    call "z_ATC_Refund"
}
if (ticket959 != "undefined"){
    send "TWD/TKT" +ticket959
    call "z_ATC_Refund"
}
if (ticket960 != "undefined"){
    send "TWD/TKT" +ticket960
    call "z_ATC_Refund"
}
if (ticket961 != "undefined"){
    send "TWD/TKT" +ticket961
    call "z_ATC_Refund"
}
if (ticket962 != "undefined"){
    send "TWD/TKT" +ticket962
    call "z_ATC_Refund"
}
if (ticket963 != "undefined"){
    send "TWD/TKT" +ticket963
    call "z_ATC_Refund"
}
if (ticket964 != "undefined"){
    send "TWD/TKT" +ticket964
    call "z_ATC_Refund"
}
if (ticket965 != "undefined"){
    send "TWD/TKT" +ticket965
    call "z_ATC_Refund"
}
if (ticket966 != "undefined"){
    send "TWD/TKT" +ticket966
    call "z_ATC_Refund"
}
if (ticket967 != "undefined"){
    send "TWD/TKT" +ticket967
    call "z_ATC_Refund"
}
if (ticket968 != "undefined"){
    send "TWD/TKT" +ticket968
    call "z_ATC_Refund"
}
if (ticket969 != "undefined"){
    send "TWD/TKT" +ticket969
    call "z_ATC_Refund"
}
if (ticket970 != "undefined"){
    send "TWD/TKT" +ticket970
    call "z_ATC_Refund"
}
if (ticket971 != "undefined"){
    send "TWD/TKT" +ticket971
    call "z_ATC_Refund"
}
if (ticket972 != "undefined"){
    send "TWD/TKT" +ticket972
    call "z_ATC_Refund"
}
if (ticket973 != "undefined"){
    send "TWD/TKT" +ticket973
    call "z_ATC_Refund"
}
if (ticket974 != "undefined"){
    send "TWD/TKT" +ticket974
    call "z_ATC_Refund"
}
if (ticket975 != "undefined"){
    send "TWD/TKT" +ticket975
    call "z_ATC_Refund"
}
if (ticket976 != "undefined"){
    send "TWD/TKT" +ticket976
    call "z_ATC_Refund"
}
if (ticket977 != "undefined"){
    send "TWD/TKT" +ticket977
    call "z_ATC_Refund"
}
if (ticket978 != "undefined"){
    send "TWD/TKT" +ticket978
    call "z_ATC_Refund"
}
if (ticket979 != "undefined"){
    send "TWD/TKT" +ticket979
    call "z_ATC_Refund"
}
if (ticket980 != "undefined"){
    send "TWD/TKT" +ticket980
    call "z_ATC_Refund"
}
if (ticket981 != "undefined"){
    send "TWD/TKT" +ticket981
    call "z_ATC_Refund"
}
if (ticket982 != "undefined"){
    send "TWD/TKT" +ticket982
    call "z_ATC_Refund"
}
if (ticket983 != "undefined"){
    send "TWD/TKT" +ticket983
    call "z_ATC_Refund"
}
if (ticket984 != "undefined"){
    send "TWD/TKT" +ticket984
    call "z_ATC_Refund"
}
if (ticket985 != "undefined"){
    send "TWD/TKT" +ticket985
    call "z_ATC_Refund"
}
if (ticket986 != "undefined"){
    send "TWD/TKT" +ticket986
    call "z_ATC_Refund"
}
if (ticket987 != "undefined"){
    send "TWD/TKT" +ticket987
    call "z_ATC_Refund"
}
if (ticket988 != "undefined"){
    send "TWD/TKT" +ticket988
    call "z_ATC_Refund"
}
if (ticket989 != "undefined"){
    send "TWD/TKT" +ticket989
    call "z_ATC_Refund"
}
if (ticket990 != "undefined"){
    send "TWD/TKT" +ticket990
    call "z_ATC_Refund"
}
if (ticket991 != "undefined"){
    send "TWD/TKT" +ticket991
    call "z_ATC_Refund"
}
if (ticket992 != "undefined"){
    send "TWD/TKT" +ticket992
    call "z_ATC_Refund"
}
if (ticket993 != "undefined"){
    send "TWD/TKT" +ticket993
    call "z_ATC_Refund"
}
if (ticket994 != "undefined"){
    send "TWD/TKT" +ticket994
    call "z_ATC_Refund"
}
if (ticket995 != "undefined"){
    send "TWD/TKT" +ticket995
    call "z_ATC_Refund"
}
if (ticket996 != "undefined"){
    send "TWD/TKT" +ticket996
    call "z_ATC_Refund"
}
if (ticket997 != "undefined"){
    send "TWD/TKT" +ticket997
    call "z_ATC_Refund"
}
if (ticket998 != "undefined"){
    send "TWD/TKT" +ticket998
    call "z_ATC_Refund"
}
if (ticket999 != "undefined"){
    send "TWD/TKT" +ticket999
    call "z_ATC_Refund"
}
if (ticket1000 != "undefined"){
    send "TWD/TKT" +ticket1000
    call "z_ATC_Refund"
}
if (ticket1001 != "undefined"){
    send "TWD/TKT" +ticket1001
    call "z_ATC_Refund"
}
if (ticket1002 != "undefined"){
    send "TWD/TKT" +ticket1002
    call "z_ATC_Refund"
}
if (ticket1003 != "undefined"){
    send "TWD/TKT" +ticket1003
    call "z_ATC_Refund"
}
if (ticket1004 != "undefined"){
    send "TWD/TKT" +ticket1004
    call "z_ATC_Refund"
}
if (ticket1005 != "undefined"){
    send "TWD/TKT" +ticket1005
    call "z_ATC_Refund"
}
if (ticket1006 != "undefined"){
    send "TWD/TKT" +ticket1006
    call "z_ATC_Refund"
}
if (ticket1007 != "undefined"){
    send "TWD/TKT" +ticket1007
    call "z_ATC_Refund"
}
if (ticket1008 != "undefined"){
    send "TWD/TKT" +ticket1008
    call "z_ATC_Refund"
}
if (ticket1009 != "undefined"){
    send "TWD/TKT" +ticket1009
    call "z_ATC_Refund"
}
if (ticket1010 != "undefined"){
    send "TWD/TKT" +ticket1010
    call "z_ATC_Refund"
}
if (ticket1011 != "undefined"){
    send "TWD/TKT" +ticket1011
    call "z_ATC_Refund"
}
if (ticket1012 != "undefined"){
    send "TWD/TKT" +ticket1012
    call "z_ATC_Refund"
}
if (ticket1013 != "undefined"){
    send "TWD/TKT" +ticket1013
    call "z_ATC_Refund"
}
if (ticket1014 != "undefined"){
    send "TWD/TKT" +ticket1014
    call "z_ATC_Refund"
}
if (ticket1015 != "undefined"){
    send "TWD/TKT" +ticket1015
    call "z_ATC_Refund"
}
if (ticket1016 != "undefined"){
    send "TWD/TKT" +ticket1016
    call "z_ATC_Refund"
}
if (ticket1017 != "undefined"){
    send "TWD/TKT" +ticket1017
    call "z_ATC_Refund"
}
if (ticket1018 != "undefined"){
    send "TWD/TKT" +ticket1018
    call "z_ATC_Refund"
}
if (ticket1019 != "undefined"){
    send "TWD/TKT" +ticket1019
    call "z_ATC_Refund"
}
if (ticket1020 != "undefined"){
    send "TWD/TKT" +ticket1020
    call "z_ATC_Refund"
}
if (ticket1021 != "undefined"){
    send "TWD/TKT" +ticket1021
    call "z_ATC_Refund"
}
if (ticket1022 != "undefined"){
    send "TWD/TKT" +ticket1022
    call "z_ATC_Refund"
}
if (ticket1023 != "undefined"){
    send "TWD/TKT" +ticket1023
    call "z_ATC_Refund"
}
if (ticket1024 != "undefined"){
    send "TWD/TKT" +ticket1024
    call "z_ATC_Refund"
}
if (ticket1025 != "undefined"){
    send "TWD/TKT" +ticket1025
    call "z_ATC_Refund"
}
if (ticket1026 != "undefined"){
    send "TWD/TKT" +ticket1026
    call "z_ATC_Refund"
}
if (ticket1027 != "undefined"){
    send "TWD/TKT" +ticket1027
    call "z_ATC_Refund"
}
if (ticket1028 != "undefined"){
    send "TWD/TKT" +ticket1028
    call "z_ATC_Refund"
}
if (ticket1029 != "undefined"){
    send "TWD/TKT" +ticket1029
    call "z_ATC_Refund"
}
if (ticket1030 != "undefined"){
    send "TWD/TKT" +ticket1030
    call "z_ATC_Refund"
}
if (ticket1031 != "undefined"){
    send "TWD/TKT" +ticket1031
    call "z_ATC_Refund"
}
if (ticket1032 != "undefined"){
    send "TWD/TKT" +ticket1032
    call "z_ATC_Refund"
}
if (ticket1033 != "undefined"){
    send "TWD/TKT" +ticket1033
    call "z_ATC_Refund"
}
if (ticket1034 != "undefined"){
    send "TWD/TKT" +ticket1034
    call "z_ATC_Refund"
}
if (ticket1035 != "undefined"){
    send "TWD/TKT" +ticket1035
    call "z_ATC_Refund"
}
if (ticket1036 != "undefined"){
    send "TWD/TKT" +ticket1036
    call "z_ATC_Refund"
}
if (ticket1037 != "undefined"){
    send "TWD/TKT" +ticket1037
    call "z_ATC_Refund"
}
if (ticket1038 != "undefined"){
    send "TWD/TKT" +ticket1038
    call "z_ATC_Refund"
}
if (ticket1039 != "undefined"){
    send "TWD/TKT" +ticket1039
    call "z_ATC_Refund"
}
if (ticket1040 != "undefined"){
    send "TWD/TKT" +ticket1040
    call "z_ATC_Refund"
}
if (ticket1041 != "undefined"){
    send "TWD/TKT" +ticket1041
    call "z_ATC_Refund"
}
if (ticket1042 != "undefined"){
    send "TWD/TKT" +ticket1042
    call "z_ATC_Refund"
}
if (ticket1043 != "undefined"){
    send "TWD/TKT" +ticket1043
    call "z_ATC_Refund"
}
if (ticket1044 != "undefined"){
    send "TWD/TKT" +ticket1044
    call "z_ATC_Refund"
}
if (ticket1045 != "undefined"){
    send "TWD/TKT" +ticket1045
    call "z_ATC_Refund"
}
if (ticket1046 != "undefined"){
    send "TWD/TKT" +ticket1046
    call "z_ATC_Refund"
}
if (ticket1047 != "undefined"){
    send "TWD/TKT" +ticket1047
    call "z_ATC_Refund"
}
if (ticket1048 != "undefined"){
    send "TWD/TKT" +ticket1048
    call "z_ATC_Refund"
}
if (ticket1049 != "undefined"){
    send "TWD/TKT" +ticket1049
    call "z_ATC_Refund"
}
if (ticket1050 != "undefined"){
    send "TWD/TKT" +ticket1050
    call "z_ATC_Refund"
}
if (ticket1051 != "undefined"){
    send "TWD/TKT" +ticket1051
    call "z_ATC_Refund"
}
if (ticket1052 != "undefined"){
    send "TWD/TKT" +ticket1052
    call "z_ATC_Refund"
}
if (ticket1053 != "undefined"){
    send "TWD/TKT" +ticket1053
    call "z_ATC_Refund"
}
if (ticket1054 != "undefined"){
    send "TWD/TKT" +ticket1054
    call "z_ATC_Refund"
}
if (ticket1055 != "undefined"){
    send "TWD/TKT" +ticket1055
    call "z_ATC_Refund"
}
if (ticket1056 != "undefined"){
    send "TWD/TKT" +ticket1056
    call "z_ATC_Refund"
}
if (ticket1057 != "undefined"){
    send "TWD/TKT" +ticket1057
    call "z_ATC_Refund"
}
if (ticket1058 != "undefined"){
    send "TWD/TKT" +ticket1058
    call "z_ATC_Refund"
}
if (ticket1059 != "undefined"){
    send "TWD/TKT" +ticket1059
    call "z_ATC_Refund"
}
if (ticket1060 != "undefined"){
    send "TWD/TKT" +ticket1060
    call "z_ATC_Refund"
}
if (ticket1061 != "undefined"){
    send "TWD/TKT" +ticket1061
    call "z_ATC_Refund"
}
if (ticket1062 != "undefined"){
    send "TWD/TKT" +ticket1062
    call "z_ATC_Refund"
}
if (ticket1063 != "undefined"){
    send "TWD/TKT" +ticket1063
    call "z_ATC_Refund"
}
if (ticket1064 != "undefined"){
    send "TWD/TKT" +ticket1064
    call "z_ATC_Refund"
}
if (ticket1065 != "undefined"){
    send "TWD/TKT" +ticket1065
    call "z_ATC_Refund"
}
if (ticket1066 != "undefined"){
    send "TWD/TKT" +ticket1066
    call "z_ATC_Refund"
}
if (ticket1067 != "undefined"){
    send "TWD/TKT" +ticket1067
    call "z_ATC_Refund"
}
if (ticket1068 != "undefined"){
    send "TWD/TKT" +ticket1068
    call "z_ATC_Refund"
}
if (ticket1069 != "undefined"){
    send "TWD/TKT" +ticket1069
    call "z_ATC_Refund"
}
if (ticket1070 != "undefined"){
    send "TWD/TKT" +ticket1070
    call "z_ATC_Refund"
}
if (ticket1071 != "undefined"){
    send "TWD/TKT" +ticket1071
    call "z_ATC_Refund"
}
if (ticket1072 != "undefined"){
    send "TWD/TKT" +ticket1072
    call "z_ATC_Refund"
}
if (ticket1073 != "undefined"){
    send "TWD/TKT" +ticket1073
    call "z_ATC_Refund"
}
if (ticket1074 != "undefined"){
    send "TWD/TKT" +ticket1074
    call "z_ATC_Refund"
}
if (ticket1075 != "undefined"){
    send "TWD/TKT" +ticket1075
    call "z_ATC_Refund"
}
if (ticket1076 != "undefined"){
    send "TWD/TKT" +ticket1076
    call "z_ATC_Refund"
}
if (ticket1077 != "undefined"){
    send "TWD/TKT" +ticket1077
    call "z_ATC_Refund"
}
if (ticket1078 != "undefined"){
    send "TWD/TKT" +ticket1078
    call "z_ATC_Refund"
}
if (ticket1079 != "undefined"){
    send "TWD/TKT" +ticket1079
    call "z_ATC_Refund"
}
if (ticket1080 != "undefined"){
    send "TWD/TKT" +ticket1080
    call "z_ATC_Refund"
}
if (ticket1081 != "undefined"){
    send "TWD/TKT" +ticket1081
    call "z_ATC_Refund"
}
if (ticket1082 != "undefined"){
    send "TWD/TKT" +ticket1082
    call "z_ATC_Refund"
}
if (ticket1083 != "undefined"){
    send "TWD/TKT" +ticket1083
    call "z_ATC_Refund"
}
if (ticket1084 != "undefined"){
    send "TWD/TKT" +ticket1084
    call "z_ATC_Refund"
}
if (ticket1085 != "undefined"){
    send "TWD/TKT" +ticket1085
    call "z_ATC_Refund"
}
if (ticket1086 != "undefined"){
    send "TWD/TKT" +ticket1086
    call "z_ATC_Refund"
}
if (ticket1087 != "undefined"){
    send "TWD/TKT" +ticket1087
    call "z_ATC_Refund"
}
if (ticket1088 != "undefined"){
    send "TWD/TKT" +ticket1088
    call "z_ATC_Refund"
}
if (ticket1089 != "undefined"){
    send "TWD/TKT" +ticket1089
    call "z_ATC_Refund"
}
if (ticket1090 != "undefined"){
    send "TWD/TKT" +ticket1090
    call "z_ATC_Refund"
}
if (ticket1091 != "undefined"){
    send "TWD/TKT" +ticket1091
    call "z_ATC_Refund"
}
if (ticket1092 != "undefined"){
    send "TWD/TKT" +ticket1092
    call "z_ATC_Refund"
}
if (ticket1093 != "undefined"){
    send "TWD/TKT" +ticket1093
    call "z_ATC_Refund"
}
if (ticket1094 != "undefined"){
    send "TWD/TKT" +ticket1094
    call "z_ATC_Refund"
}
if (ticket1095 != "undefined"){
    send "TWD/TKT" +ticket1095
    call "z_ATC_Refund"
}
if (ticket1096 != "undefined"){
    send "TWD/TKT" +ticket1096
    call "z_ATC_Refund"
}
if (ticket1097 != "undefined"){
    send "TWD/TKT" +ticket1097
    call "z_ATC_Refund"
}
if (ticket1098 != "undefined"){
    send "TWD/TKT" +ticket1098
    call "z_ATC_Refund"
}
if (ticket1099 != "undefined"){
    send "TWD/TKT" +ticket1099
    call "z_ATC_Refund"
}
if (ticket1100 != "undefined"){
    send "TWD/TKT" +ticket1100
    call "z_ATC_Refund"
}
if (ticket1101 != "undefined"){
    send "TWD/TKT" +ticket1101
    call "z_ATC_Refund"
}
if (ticket1102 != "undefined"){
    send "TWD/TKT" +ticket1102
    call "z_ATC_Refund"
}
if (ticket1103 != "undefined"){
    send "TWD/TKT" +ticket1103
    call "z_ATC_Refund"
}
if (ticket1104 != "undefined"){
    send "TWD/TKT" +ticket1104
    call "z_ATC_Refund"
}
if (ticket1105 != "undefined"){
    send "TWD/TKT" +ticket1105
    call "z_ATC_Refund"
}
if (ticket1106 != "undefined"){
    send "TWD/TKT" +ticket1106
    call "z_ATC_Refund"
}
if (ticket1107 != "undefined"){
    send "TWD/TKT" +ticket1107
    call "z_ATC_Refund"
}
if (ticket1108 != "undefined"){
    send "TWD/TKT" +ticket1108
    call "z_ATC_Refund"
}
if (ticket1109 != "undefined"){
    send "TWD/TKT" +ticket1109
    call "z_ATC_Refund"
}
if (ticket1110 != "undefined"){
    send "TWD/TKT" +ticket1110
    call "z_ATC_Refund"
}
if (ticket1111 != "undefined"){
    send "TWD/TKT" +ticket1111
    call "z_ATC_Refund"
}
if (ticket1112 != "undefined"){
    send "TWD/TKT" +ticket1112
    call "z_ATC_Refund"
}
if (ticket1113 != "undefined"){
    send "TWD/TKT" +ticket1113
    call "z_ATC_Refund"
}
if (ticket1114 != "undefined"){
    send "TWD/TKT" +ticket1114
    call "z_ATC_Refund"
}
if (ticket1115 != "undefined"){
    send "TWD/TKT" +ticket1115
    call "z_ATC_Refund"
}
if (ticket1116 != "undefined"){
    send "TWD/TKT" +ticket1116
    call "z_ATC_Refund"
}
if (ticket1117 != "undefined"){
    send "TWD/TKT" +ticket1117
    call "z_ATC_Refund"
}
if (ticket1118 != "undefined"){
    send "TWD/TKT" +ticket1118
    call "z_ATC_Refund"
}
if (ticket1119 != "undefined"){
    send "TWD/TKT" +ticket1119
    call "z_ATC_Refund"
}
if (ticket1120 != "undefined"){
    send "TWD/TKT" +ticket1120
    call "z_ATC_Refund"
}
if (ticket1121 != "undefined"){
    send "TWD/TKT" +ticket1121
    call "z_ATC_Refund"
}
if (ticket1122 != "undefined"){
    send "TWD/TKT" +ticket1122
    call "z_ATC_Refund"
}
if (ticket1123 != "undefined"){
    send "TWD/TKT" +ticket1123
    call "z_ATC_Refund"
}
if (ticket1124 != "undefined"){
    send "TWD/TKT" +ticket1124
    call "z_ATC_Refund"
}
if (ticket1125 != "undefined"){
    send "TWD/TKT" +ticket1125
    call "z_ATC_Refund"
}
if (ticket1126 != "undefined"){
    send "TWD/TKT" +ticket1126
    call "z_ATC_Refund"
}
if (ticket1127 != "undefined"){
    send "TWD/TKT" +ticket1127
    call "z_ATC_Refund"
}
if (ticket1128 != "undefined"){
    send "TWD/TKT" +ticket1128
    call "z_ATC_Refund"
}
if (ticket1129 != "undefined"){
    send "TWD/TKT" +ticket1129
    call "z_ATC_Refund"
}
if (ticket1130 != "undefined"){
    send "TWD/TKT" +ticket1130
    call "z_ATC_Refund"
}
if (ticket1131 != "undefined"){
    send "TWD/TKT" +ticket1131
    call "z_ATC_Refund"
}
if (ticket1132 != "undefined"){
    send "TWD/TKT" +ticket1132
    call "z_ATC_Refund"
}
if (ticket1133 != "undefined"){
    send "TWD/TKT" +ticket1133
    call "z_ATC_Refund"
}
if (ticket1134 != "undefined"){
    send "TWD/TKT" +ticket1134
    call "z_ATC_Refund"
}
if (ticket1135 != "undefined"){
    send "TWD/TKT" +ticket1135
    call "z_ATC_Refund"
}
if (ticket1136 != "undefined"){
    send "TWD/TKT" +ticket1136
    call "z_ATC_Refund"
}
if (ticket1137 != "undefined"){
    send "TWD/TKT" +ticket1137
    call "z_ATC_Refund"
}
if (ticket1138 != "undefined"){
    send "TWD/TKT" +ticket1138
    call "z_ATC_Refund"
}
if (ticket1139 != "undefined"){
    send "TWD/TKT" +ticket1139
    call "z_ATC_Refund"
}
if (ticket1140 != "undefined"){
    send "TWD/TKT" +ticket1140
    call "z_ATC_Refund"
}
if (ticket1141 != "undefined"){
    send "TWD/TKT" +ticket1141
    call "z_ATC_Refund"
}
if (ticket1142 != "undefined"){
    send "TWD/TKT" +ticket1142
    call "z_ATC_Refund"
}
if (ticket1143 != "undefined"){
    send "TWD/TKT" +ticket1143
    call "z_ATC_Refund"
}
if (ticket1144 != "undefined"){
    send "TWD/TKT" +ticket1144
    call "z_ATC_Refund"
}
if (ticket1145 != "undefined"){
    send "TWD/TKT" +ticket1145
    call "z_ATC_Refund"
}
if (ticket1146 != "undefined"){
    send "TWD/TKT" +ticket1146
    call "z_ATC_Refund"
}
if (ticket1147 != "undefined"){
    send "TWD/TKT" +ticket1147
    call "z_ATC_Refund"
}
if (ticket1148 != "undefined"){
    send "TWD/TKT" +ticket1148
    call "z_ATC_Refund"
}
if (ticket1149 != "undefined"){
    send "TWD/TKT" +ticket1149
    call "z_ATC_Refund"
}
if (ticket1150 != "undefined"){
    send "TWD/TKT" +ticket1150
    call "z_ATC_Refund"
}
if (ticket1151 != "undefined"){
    send "TWD/TKT" +ticket1151
    call "z_ATC_Refund"
}
if (ticket1152 != "undefined"){
    send "TWD/TKT" +ticket1152
    call "z_ATC_Refund"
}
if (ticket1153 != "undefined"){
    send "TWD/TKT" +ticket1153
    call "z_ATC_Refund"
}
if (ticket1154 != "undefined"){
    send "TWD/TKT" +ticket1154
    call "z_ATC_Refund"
}
if (ticket1155 != "undefined"){
    send "TWD/TKT" +ticket1155
    call "z_ATC_Refund"
}
if (ticket1156 != "undefined"){
    send "TWD/TKT" +ticket1156
    call "z_ATC_Refund"
}
if (ticket1157 != "undefined"){
    send "TWD/TKT" +ticket1157
    call "z_ATC_Refund"
}
if (ticket1158 != "undefined"){
    send "TWD/TKT" +ticket1158
    call "z_ATC_Refund"
}
if (ticket1159 != "undefined"){
    send "TWD/TKT" +ticket1159
    call "z_ATC_Refund"
}
if (ticket1160 != "undefined"){
    send "TWD/TKT" +ticket1160
    call "z_ATC_Refund"
}
if (ticket1161 != "undefined"){
    send "TWD/TKT" +ticket1161
    call "z_ATC_Refund"
}
if (ticket1162 != "undefined"){
    send "TWD/TKT" +ticket1162
    call "z_ATC_Refund"
}
if (ticket1163 != "undefined"){
    send "TWD/TKT" +ticket1163
    call "z_ATC_Refund"
}
if (ticket1164 != "undefined"){
    send "TWD/TKT" +ticket1164
    call "z_ATC_Refund"
}
if (ticket1165 != "undefined"){
    send "TWD/TKT" +ticket1165
    call "z_ATC_Refund"
}
if (ticket1166 != "undefined"){
    send "TWD/TKT" +ticket1166
    call "z_ATC_Refund"
}
if (ticket1167 != "undefined"){
    send "TWD/TKT" +ticket1167
    call "z_ATC_Refund"
}
if (ticket1168 != "undefined"){
    send "TWD/TKT" +ticket1168
    call "z_ATC_Refund"
}
if (ticket1169 != "undefined"){
    send "TWD/TKT" +ticket1169
    call "z_ATC_Refund"
}
if (ticket1170 != "undefined"){
    send "TWD/TKT" +ticket1170
    call "z_ATC_Refund"
}
if (ticket1171 != "undefined"){
    send "TWD/TKT" +ticket1171
    call "z_ATC_Refund"
}
if (ticket1172 != "undefined"){
    send "TWD/TKT" +ticket1172
    call "z_ATC_Refund"
}
if (ticket1173 != "undefined"){
    send "TWD/TKT" +ticket1173
    call "z_ATC_Refund"
}
if (ticket1174 != "undefined"){
    send "TWD/TKT" +ticket1174
    call "z_ATC_Refund"
}
if (ticket1175 != "undefined"){
    send "TWD/TKT" +ticket1175
    call "z_ATC_Refund"
}
if (ticket1176 != "undefined"){
    send "TWD/TKT" +ticket1176
    call "z_ATC_Refund"
}
if (ticket1177 != "undefined"){
    send "TWD/TKT" +ticket1177
    call "z_ATC_Refund"
}
if (ticket1178 != "undefined"){
    send "TWD/TKT" +ticket1178
    call "z_ATC_Refund"
}
if (ticket1179 != "undefined"){
    send "TWD/TKT" +ticket1179
    call "z_ATC_Refund"
}
if (ticket1180 != "undefined"){
    send "TWD/TKT" +ticket1180
    call "z_ATC_Refund"
}
if (ticket1181 != "undefined"){
    send "TWD/TKT" +ticket1181
    call "z_ATC_Refund"
}
if (ticket1182 != "undefined"){
    send "TWD/TKT" +ticket1182
    call "z_ATC_Refund"
}
if (ticket1183 != "undefined"){
    send "TWD/TKT" +ticket1183
    call "z_ATC_Refund"
}
if (ticket1184 != "undefined"){
    send "TWD/TKT" +ticket1184
    call "z_ATC_Refund"
}
if (ticket1185 != "undefined"){
    send "TWD/TKT" +ticket1185
    call "z_ATC_Refund"
}
if (ticket1186 != "undefined"){
    send "TWD/TKT" +ticket1186
    call "z_ATC_Refund"
}
if (ticket1187 != "undefined"){
    send "TWD/TKT" +ticket1187
    call "z_ATC_Refund"
}
if (ticket1188 != "undefined"){
    send "TWD/TKT" +ticket1188
    call "z_ATC_Refund"
}
if (ticket1189 != "undefined"){
    send "TWD/TKT" +ticket1189
    call "z_ATC_Refund"
}
if (ticket1190 != "undefined"){
    send "TWD/TKT" +ticket1190
    call "z_ATC_Refund"
}
if (ticket1191 != "undefined"){
    send "TWD/TKT" +ticket1191
    call "z_ATC_Refund"
}
if (ticket1192 != "undefined"){
    send "TWD/TKT" +ticket1192
    call "z_ATC_Refund"
}
if (ticket1193 != "undefined"){
    send "TWD/TKT" +ticket1193
    call "z_ATC_Refund"
}
if (ticket1194 != "undefined"){
    send "TWD/TKT" +ticket1194
    call "z_ATC_Refund"
}
if (ticket1195 != "undefined"){
    send "TWD/TKT" +ticket1195
    call "z_ATC_Refund"
}
if (ticket1196 != "undefined"){
    send "TWD/TKT" +ticket1196
    call "z_ATC_Refund"
}
if (ticket1197 != "undefined"){
    send "TWD/TKT" +ticket1197
    call "z_ATC_Refund"
}
if (ticket1198 != "undefined"){
    send "TWD/TKT" +ticket1198
    call "z_ATC_Refund"
}
if (ticket1199 != "undefined"){
    send "TWD/TKT" +ticket1199
    call "z_ATC_Refund"
}
if (ticket1200 != "undefined"){
    send "TWD/TKT" +ticket1200
    call "z_ATC_Refund"
}
if (ticket1201 != "undefined"){
    send "TWD/TKT" +ticket1201
    call "z_ATC_Refund"
}
if (ticket1202 != "undefined"){
    send "TWD/TKT" +ticket1202
    call "z_ATC_Refund"
}
if (ticket1203 != "undefined"){
    send "TWD/TKT" +ticket1203
    call "z_ATC_Refund"
}
if (ticket1204 != "undefined"){
    send "TWD/TKT" +ticket1204
    call "z_ATC_Refund"
}
if (ticket1205 != "undefined"){
    send "TWD/TKT" +ticket1205
    call "z_ATC_Refund"
}
if (ticket1206 != "undefined"){
    send "TWD/TKT" +ticket1206
    call "z_ATC_Refund"
}
if (ticket1207 != "undefined"){
    send "TWD/TKT" +ticket1207
    call "z_ATC_Refund"
}
if (ticket1208 != "undefined"){
    send "TWD/TKT" +ticket1208
    call "z_ATC_Refund"
}
if (ticket1209 != "undefined"){
    send "TWD/TKT" +ticket1209
    call "z_ATC_Refund"
}
if (ticket1210 != "undefined"){
    send "TWD/TKT" +ticket1210
    call "z_ATC_Refund"
}
if (ticket1211 != "undefined"){
    send "TWD/TKT" +ticket1211
    call "z_ATC_Refund"
}
if (ticket1212 != "undefined"){
    send "TWD/TKT" +ticket1212
    call "z_ATC_Refund"
}
if (ticket1213 != "undefined"){
    send "TWD/TKT" +ticket1213
    call "z_ATC_Refund"
}
if (ticket1214 != "undefined"){
    send "TWD/TKT" +ticket1214
    call "z_ATC_Refund"
}
if (ticket1215 != "undefined"){
    send "TWD/TKT" +ticket1215
    call "z_ATC_Refund"
}
if (ticket1216 != "undefined"){
    send "TWD/TKT" +ticket1216
    call "z_ATC_Refund"
}
if (ticket1217 != "undefined"){
    send "TWD/TKT" +ticket1217
    call "z_ATC_Refund"
}
if (ticket1218 != "undefined"){
    send "TWD/TKT" +ticket1218
    call "z_ATC_Refund"
}
if (ticket1219 != "undefined"){
    send "TWD/TKT" +ticket1219
    call "z_ATC_Refund"
}
if (ticket1220 != "undefined"){
    send "TWD/TKT" +ticket1220
    call "z_ATC_Refund"
}
if (ticket1221 != "undefined"){
    send "TWD/TKT" +ticket1221
    call "z_ATC_Refund"
}
if (ticket1222 != "undefined"){
    send "TWD/TKT" +ticket1222
    call "z_ATC_Refund"
}
if (ticket1223 != "undefined"){
    send "TWD/TKT" +ticket1223
    call "z_ATC_Refund"
}
if (ticket1224 != "undefined"){
    send "TWD/TKT" +ticket1224
    call "z_ATC_Refund"
}
if (ticket1225 != "undefined"){
    send "TWD/TKT" +ticket1225
    call "z_ATC_Refund"
}
if (ticket1226 != "undefined"){
    send "TWD/TKT" +ticket1226
    call "z_ATC_Refund"
}
if (ticket1227 != "undefined"){
    send "TWD/TKT" +ticket1227
    call "z_ATC_Refund"
}
if (ticket1228 != "undefined"){
    send "TWD/TKT" +ticket1228
    call "z_ATC_Refund"
}
if (ticket1229 != "undefined"){
    send "TWD/TKT" +ticket1229
    call "z_ATC_Refund"
}
if (ticket1230 != "undefined"){
    send "TWD/TKT" +ticket1230
    call "z_ATC_Refund"
}
if (ticket1231 != "undefined"){
    send "TWD/TKT" +ticket1231
    call "z_ATC_Refund"
}
if (ticket1232 != "undefined"){
    send "TWD/TKT" +ticket1232
    call "z_ATC_Refund"
}
if (ticket1233 != "undefined"){
    send "TWD/TKT" +ticket1233
    call "z_ATC_Refund"
}
if (ticket1234 != "undefined"){
    send "TWD/TKT" +ticket1234
    call "z_ATC_Refund"
}
if (ticket1235 != "undefined"){
    send "TWD/TKT" +ticket1235
    call "z_ATC_Refund"
}
if (ticket1236 != "undefined"){
    send "TWD/TKT" +ticket1236
    call "z_ATC_Refund"
}
if (ticket1237 != "undefined"){
    send "TWD/TKT" +ticket1237
    call "z_ATC_Refund"
}
if (ticket1238 != "undefined"){
    send "TWD/TKT" +ticket1238
    call "z_ATC_Refund"
}
if (ticket1239 != "undefined"){
    send "TWD/TKT" +ticket1239
    call "z_ATC_Refund"
}
if (ticket1240 != "undefined"){
    send "TWD/TKT" +ticket1240
    call "z_ATC_Refund"
}
if (ticket1241 != "undefined"){
    send "TWD/TKT" +ticket1241
    call "z_ATC_Refund"
}
if (ticket1242 != "undefined"){
    send "TWD/TKT" +ticket1242
    call "z_ATC_Refund"
}
if (ticket1243 != "undefined"){
    send "TWD/TKT" +ticket1243
    call "z_ATC_Refund"
}
if (ticket1244 != "undefined"){
    send "TWD/TKT" +ticket1244
    call "z_ATC_Refund"
}
if (ticket1245 != "undefined"){
    send "TWD/TKT" +ticket1245
    call "z_ATC_Refund"
}
if (ticket1246 != "undefined"){
    send "TWD/TKT" +ticket1246
    call "z_ATC_Refund"
}
if (ticket1247 != "undefined"){
    send "TWD/TKT" +ticket1247
    call "z_ATC_Refund"
}
if (ticket1248 != "undefined"){
    send "TWD/TKT" +ticket1248
    call "z_ATC_Refund"
}
if (ticket1249 != "undefined"){
    send "TWD/TKT" +ticket1249
    call "z_ATC_Refund"
}
if (ticket1250 != "undefined"){
    send "TWD/TKT" +ticket1250
    call "z_ATC_Refund"
}
if (ticket1251 != "undefined"){
    send "TWD/TKT" +ticket1251
    call "z_ATC_Refund"
}
if (ticket1252 != "undefined"){
    send "TWD/TKT" +ticket1252
    call "z_ATC_Refund"
}
if (ticket1253 != "undefined"){
    send "TWD/TKT" +ticket1253
    call "z_ATC_Refund"
}
if (ticket1254 != "undefined"){
    send "TWD/TKT" +ticket1254
    call "z_ATC_Refund"
}
if (ticket1255 != "undefined"){
    send "TWD/TKT" +ticket1255
    call "z_ATC_Refund"
}
if (ticket1256 != "undefined"){
    send "TWD/TKT" +ticket1256
    call "z_ATC_Refund"
}
if (ticket1257 != "undefined"){
    send "TWD/TKT" +ticket1257
    call "z_ATC_Refund"
}
if (ticket1258 != "undefined"){
    send "TWD/TKT" +ticket1258
    call "z_ATC_Refund"
}
if (ticket1259 != "undefined"){
    send "TWD/TKT" +ticket1259
    call "z_ATC_Refund"
}
if (ticket1260 != "undefined"){
    send "TWD/TKT" +ticket1260
    call "z_ATC_Refund"
}
if (ticket1261 != "undefined"){
    send "TWD/TKT" +ticket1261
    call "z_ATC_Refund"
}
if (ticket1262 != "undefined"){
    send "TWD/TKT" +ticket1262
    call "z_ATC_Refund"
}
if (ticket1263 != "undefined"){
    send "TWD/TKT" +ticket1263
    call "z_ATC_Refund"
}
if (ticket1264 != "undefined"){
    send "TWD/TKT" +ticket1264
    call "z_ATC_Refund"
}
if (ticket1265 != "undefined"){
    send "TWD/TKT" +ticket1265
    call "z_ATC_Refund"
}
if (ticket1266 != "undefined"){
    send "TWD/TKT" +ticket1266
    call "z_ATC_Refund"
}
if (ticket1267 != "undefined"){
    send "TWD/TKT" +ticket1267
    call "z_ATC_Refund"
}
if (ticket1268 != "undefined"){
    send "TWD/TKT" +ticket1268
    call "z_ATC_Refund"
}
if (ticket1269 != "undefined"){
    send "TWD/TKT" +ticket1269
    call "z_ATC_Refund"
}
if (ticket1270 != "undefined"){
    send "TWD/TKT" +ticket1270
    call "z_ATC_Refund"
}
if (ticket1271 != "undefined"){
    send "TWD/TKT" +ticket1271
    call "z_ATC_Refund"
}
if (ticket1272 != "undefined"){
    send "TWD/TKT" +ticket1272
    call "z_ATC_Refund"
}
if (ticket1273 != "undefined"){
    send "TWD/TKT" +ticket1273
    call "z_ATC_Refund"
}
if (ticket1274 != "undefined"){
    send "TWD/TKT" +ticket1274
    call "z_ATC_Refund"
}
if (ticket1275 != "undefined"){
    send "TWD/TKT" +ticket1275
    call "z_ATC_Refund"
}
if (ticket1276 != "undefined"){
    send "TWD/TKT" +ticket1276
    call "z_ATC_Refund"
}
if (ticket1277 != "undefined"){
    send "TWD/TKT" +ticket1277
    call "z_ATC_Refund"
}
if (ticket1278 != "undefined"){
    send "TWD/TKT" +ticket1278
    call "z_ATC_Refund"
}
if (ticket1279 != "undefined"){
    send "TWD/TKT" +ticket1279
    call "z_ATC_Refund"
}
if (ticket1280 != "undefined"){
    send "TWD/TKT" +ticket1280
    call "z_ATC_Refund"
}
if (ticket1281 != "undefined"){
    send "TWD/TKT" +ticket1281
    call "z_ATC_Refund"
}
if (ticket1282 != "undefined"){
    send "TWD/TKT" +ticket1282
    call "z_ATC_Refund"
}
if (ticket1283 != "undefined"){
    send "TWD/TKT" +ticket1283
    call "z_ATC_Refund"
}
if (ticket1284 != "undefined"){
    send "TWD/TKT" +ticket1284
    call "z_ATC_Refund"
}
if (ticket1285 != "undefined"){
    send "TWD/TKT" +ticket1285
    call "z_ATC_Refund"
}
if (ticket1286 != "undefined"){
    send "TWD/TKT" +ticket1286
    call "z_ATC_Refund"
}
if (ticket1287 != "undefined"){
    send "TWD/TKT" +ticket1287
    call "z_ATC_Refund"
}
if (ticket1288 != "undefined"){
    send "TWD/TKT" +ticket1288
    call "z_ATC_Refund"
}
if (ticket1289 != "undefined"){
    send "TWD/TKT" +ticket1289
    call "z_ATC_Refund"
}
if (ticket1290 != "undefined"){
    send "TWD/TKT" +ticket1290
    call "z_ATC_Refund"
}
if (ticket1291 != "undefined"){
    send "TWD/TKT" +ticket1291
    call "z_ATC_Refund"
}
if (ticket1292 != "undefined"){
    send "TWD/TKT" +ticket1292
    call "z_ATC_Refund"
}
if (ticket1293 != "undefined"){
    send "TWD/TKT" +ticket1293
    call "z_ATC_Refund"
}
if (ticket1294 != "undefined"){
    send "TWD/TKT" +ticket1294
    call "z_ATC_Refund"
}
if (ticket1295 != "undefined"){
    send "TWD/TKT" +ticket1295
    call "z_ATC_Refund"
}
if (ticket1296 != "undefined"){
    send "TWD/TKT" +ticket1296
    call "z_ATC_Refund"
}
if (ticket1297 != "undefined"){
    send "TWD/TKT" +ticket1297
    call "z_ATC_Refund"
}
if (ticket1298 != "undefined"){
    send "TWD/TKT" +ticket1298
    call "z_ATC_Refund"
}
if (ticket1299 != "undefined"){
    send "TWD/TKT" +ticket1299
    call "z_ATC_Refund"
}
if (ticket1300 != "undefined"){
    send "TWD/TKT" +ticket1300
    call "z_ATC_Refund"
}
if (ticket1301 != "undefined"){
    send "TWD/TKT" +ticket1301
    call "z_ATC_Refund"
}
if (ticket1302 != "undefined"){
    send "TWD/TKT" +ticket1302
    call "z_ATC_Refund"
}
if (ticket1303 != "undefined"){
    send "TWD/TKT" +ticket1303
    call "z_ATC_Refund"
}
if (ticket1304 != "undefined"){
    send "TWD/TKT" +ticket1304
    call "z_ATC_Refund"
}
if (ticket1305 != "undefined"){
    send "TWD/TKT" +ticket1305
    call "z_ATC_Refund"
}
if (ticket1306 != "undefined"){
    send "TWD/TKT" +ticket1306
    call "z_ATC_Refund"
}
if (ticket1307 != "undefined"){
    send "TWD/TKT" +ticket1307
    call "z_ATC_Refund"
}
if (ticket1308 != "undefined"){
    send "TWD/TKT" +ticket1308
    call "z_ATC_Refund"
}
if (ticket1309 != "undefined"){
    send "TWD/TKT" +ticket1309
    call "z_ATC_Refund"
}
if (ticket1310 != "undefined"){
    send "TWD/TKT" +ticket1310
    call "z_ATC_Refund"
}
if (ticket1311 != "undefined"){
    send "TWD/TKT" +ticket1311
    call "z_ATC_Refund"
}
if (ticket1312 != "undefined"){
    send "TWD/TKT" +ticket1312
    call "z_ATC_Refund"
}
if (ticket1313 != "undefined"){
    send "TWD/TKT" +ticket1313
    call "z_ATC_Refund"
}
if (ticket1314 != "undefined"){
    send "TWD/TKT" +ticket1314
    call "z_ATC_Refund"
}
if (ticket1315 != "undefined"){
    send "TWD/TKT" +ticket1315
    call "z_ATC_Refund"
}
if (ticket1316 != "undefined"){
    send "TWD/TKT" +ticket1316
    call "z_ATC_Refund"
}
if (ticket1317 != "undefined"){
    send "TWD/TKT" +ticket1317
    call "z_ATC_Refund"
}
if (ticket1318 != "undefined"){
    send "TWD/TKT" +ticket1318
    call "z_ATC_Refund"
}
if (ticket1319 != "undefined"){
    send "TWD/TKT" +ticket1319
    call "z_ATC_Refund"
}
if (ticket1320 != "undefined"){
    send "TWD/TKT" +ticket1320
    call "z_ATC_Refund"
}
if (ticket1321 != "undefined"){
    send "TWD/TKT" +ticket1321
    call "z_ATC_Refund"
}
if (ticket1322 != "undefined"){
    send "TWD/TKT" +ticket1322
    call "z_ATC_Refund"
}
if (ticket1323 != "undefined"){
    send "TWD/TKT" +ticket1323
    call "z_ATC_Refund"
}
if (ticket1324 != "undefined"){
    send "TWD/TKT" +ticket1324
    call "z_ATC_Refund"
}
if (ticket1325 != "undefined"){
    send "TWD/TKT" +ticket1325
    call "z_ATC_Refund"
}
if (ticket1326 != "undefined"){
    send "TWD/TKT" +ticket1326
    call "z_ATC_Refund"
}
if (ticket1327 != "undefined"){
    send "TWD/TKT" +ticket1327
    call "z_ATC_Refund"
}
if (ticket1328 != "undefined"){
    send "TWD/TKT" +ticket1328
    call "z_ATC_Refund"
}
if (ticket1329 != "undefined"){
    send "TWD/TKT" +ticket1329
    call "z_ATC_Refund"
}
if (ticket1330 != "undefined"){
    send "TWD/TKT" +ticket1330
    call "z_ATC_Refund"
}
if (ticket1331 != "undefined"){
    send "TWD/TKT" +ticket1331
    call "z_ATC_Refund"
}
if (ticket1332 != "undefined"){
    send "TWD/TKT" +ticket1332
    call "z_ATC_Refund"
}
if (ticket1333 != "undefined"){
    send "TWD/TKT" +ticket1333
    call "z_ATC_Refund"
}
if (ticket1334 != "undefined"){
    send "TWD/TKT" +ticket1334
    call "z_ATC_Refund"
}
if (ticket1335 != "undefined"){
    send "TWD/TKT" +ticket1335
    call "z_ATC_Refund"
}
if (ticket1336 != "undefined"){
    send "TWD/TKT" +ticket1336
    call "z_ATC_Refund"
}
if (ticket1337 != "undefined"){
    send "TWD/TKT" +ticket1337
    call "z_ATC_Refund"
}
if (ticket1338 != "undefined"){
    send "TWD/TKT" +ticket1338
    call "z_ATC_Refund"
}
if (ticket1339 != "undefined"){
    send "TWD/TKT" +ticket1339
    call "z_ATC_Refund"
}
if (ticket1340 != "undefined"){
    send "TWD/TKT" +ticket1340
    call "z_ATC_Refund"
}
if (ticket1341 != "undefined"){
    send "TWD/TKT" +ticket1341
    call "z_ATC_Refund"
}
if (ticket1342 != "undefined"){
    send "TWD/TKT" +ticket1342
    call "z_ATC_Refund"
}
if (ticket1343 != "undefined"){
    send "TWD/TKT" +ticket1343
    call "z_ATC_Refund"
}
if (ticket1344 != "undefined"){
    send "TWD/TKT" +ticket1344
    call "z_ATC_Refund"
}
if (ticket1345 != "undefined"){
    send "TWD/TKT" +ticket1345
    call "z_ATC_Refund"
}
if (ticket1346 != "undefined"){
    send "TWD/TKT" +ticket1346
    call "z_ATC_Refund"
}
if (ticket1347 != "undefined"){
    send "TWD/TKT" +ticket1347
    call "z_ATC_Refund"
}
if (ticket1348 != "undefined"){
    send "TWD/TKT" +ticket1348
    call "z_ATC_Refund"
}
if (ticket1349 != "undefined"){
    send "TWD/TKT" +ticket1349
    call "z_ATC_Refund"
}
if (ticket1350 != "undefined"){
    send "TWD/TKT" +ticket1350
    call "z_ATC_Refund"
}
if (ticket1351 != "undefined"){
    send "TWD/TKT" +ticket1351
    call "z_ATC_Refund"
}
if (ticket1352 != "undefined"){
    send "TWD/TKT" +ticket1352
    call "z_ATC_Refund"
}
if (ticket1353 != "undefined"){
    send "TWD/TKT" +ticket1353
    call "z_ATC_Refund"
}
if (ticket1354 != "undefined"){
    send "TWD/TKT" +ticket1354
    call "z_ATC_Refund"
}
if (ticket1355 != "undefined"){
    send "TWD/TKT" +ticket1355
    call "z_ATC_Refund"
}
if (ticket1356 != "undefined"){
    send "TWD/TKT" +ticket1356
    call "z_ATC_Refund"
}
if (ticket1357 != "undefined"){
    send "TWD/TKT" +ticket1357
    call "z_ATC_Refund"
}
if (ticket1358 != "undefined"){
    send "TWD/TKT" +ticket1358
    call "z_ATC_Refund"
}
if (ticket1359 != "undefined"){
    send "TWD/TKT" +ticket1359
    call "z_ATC_Refund"
}
if (ticket1360 != "undefined"){
    send "TWD/TKT" +ticket1360
    call "z_ATC_Refund"
}
if (ticket1361 != "undefined"){
    send "TWD/TKT" +ticket1361
    call "z_ATC_Refund"
}
if (ticket1362 != "undefined"){
    send "TWD/TKT" +ticket1362
    call "z_ATC_Refund"
}
if (ticket1363 != "undefined"){
    send "TWD/TKT" +ticket1363
    call "z_ATC_Refund"
}
if (ticket1364 != "undefined"){
    send "TWD/TKT" +ticket1364
    call "z_ATC_Refund"
}
if (ticket1365 != "undefined"){
    send "TWD/TKT" +ticket1365
    call "z_ATC_Refund"
}
if (ticket1366 != "undefined"){
    send "TWD/TKT" +ticket1366
    call "z_ATC_Refund"
}
if (ticket1367 != "undefined"){
    send "TWD/TKT" +ticket1367
    call "z_ATC_Refund"
}
if (ticket1368 != "undefined"){
    send "TWD/TKT" +ticket1368
    call "z_ATC_Refund"
}
if (ticket1369 != "undefined"){
    send "TWD/TKT" +ticket1369
    call "z_ATC_Refund"
}
if (ticket1370 != "undefined"){
    send "TWD/TKT" +ticket1370
    call "z_ATC_Refund"
}
if (ticket1371 != "undefined"){
    send "TWD/TKT" +ticket1371
    call "z_ATC_Refund"
}
if (ticket1372 != "undefined"){
    send "TWD/TKT" +ticket1372
    call "z_ATC_Refund"
}
if (ticket1373 != "undefined"){
    send "TWD/TKT" +ticket1373
    call "z_ATC_Refund"
}
if (ticket1374 != "undefined"){
    send "TWD/TKT" +ticket1374
    call "z_ATC_Refund"
}
if (ticket1375 != "undefined"){
    send "TWD/TKT" +ticket1375
    call "z_ATC_Refund"
}
if (ticket1376 != "undefined"){
    send "TWD/TKT" +ticket1376
    call "z_ATC_Refund"
}
if (ticket1377 != "undefined"){
    send "TWD/TKT" +ticket1377
    call "z_ATC_Refund"
}
if (ticket1378 != "undefined"){
    send "TWD/TKT" +ticket1378
    call "z_ATC_Refund"
}
if (ticket1379 != "undefined"){
    send "TWD/TKT" +ticket1379
    call "z_ATC_Refund"
}
if (ticket1380 != "undefined"){
    send "TWD/TKT" +ticket1380
    call "z_ATC_Refund"
}
if (ticket1381 != "undefined"){
    send "TWD/TKT" +ticket1381
    call "z_ATC_Refund"
}
if (ticket1382 != "undefined"){
    send "TWD/TKT" +ticket1382
    call "z_ATC_Refund"
}
if (ticket1383 != "undefined"){
    send "TWD/TKT" +ticket1383
    call "z_ATC_Refund"
}

send "Finished!"

