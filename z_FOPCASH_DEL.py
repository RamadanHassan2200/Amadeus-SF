// z_FOPCASH_DEL
send "rtf"
capture line:1, column:1, length:19 assign to checksuccess
if (checksuccess =="ENTRY NOT PROCESSED"){
    send "IR"
    send "rtf"
    call "z_FOPCASH_DEL"
}

// DELETE FP Line
capture line:1, column:5, length:2 assign to FOP
if(FOP=="FP"){
    capture line:1, column:2, length:2 assign to FOPL1  
    send "XE" + FOPL1
    call "z_FOPCASH_DEL"
}
capture line:2, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:2, column:2, length:2 assign to FOPL2
    send "XE" + FOPL2
    call "z_FOPCASH_DEL"
}

capture line:3, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:3, column:2, length:2 assign to FOPL3
    send "XE" + FOPL3
    call "z_FOPCASH_DEL"
}

capture line:4, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:4, column:2, length:2 assign to FOPL4
    send "XE" + FOPL4
    call "z_FOPCASH_DEL"
}

capture line:5, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:5, column:2, length:2 assign to FOPL5
    send "XE" + FOPL5
    call "z_FOPCASH_DEL"
}

capture line:6, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:6, column:2, length:2 assign to FOPL6
    send "XE" + FOPL6
    call "z_FOPCASH_DEL"
}

capture line:7, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:7, column:2, length:2 assign to FOPL7
    send "XE" + FOPL7
    call "z_FOPCASH_DEL"
}

capture line:8, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:8, column:2, length:2 assign to FOPL8
    send "XE" + FOPL8
    call "z_FOPCASH_DEL"
}

capture line:9, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:9, column:2, length:2 assign to FOPL9
    send "XE" + FOPL9
    call "z_FOPCASH_DEL"
}

capture line:10, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:10, column:2, length:2 assign to FOPL10
    send "XE" + FOPL10
    call "z_FOPCASH_DEL"
}

capture line:11, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:11, column:2, length:2 assign to FOPL11
    send "XE" + FOPL11
    call "z_FOPCASH_DEL"
}

capture line:12, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:12, column:2, length:2 assign to FOPL12
    send "XE" + FOPL12
    call "z_FOPCASH_DEL"
}

capture line:13, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:13, column:2, length:2 assign to FOPL13
    send "XE" + FOPL13
    call "z_FOPCASH_DEL"
}

capture line:14, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:14, column:2, length:2 assign to FOPL14
    send "XE" + FOPL14
    call "z_FOPCASH_DEL"
}

capture line:15, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:15, column:2, length:2 assign to FOPL15
    send "XE" + FOPL15
    call "z_FOPCASH_DEL"
}
capture line:16, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:16, column:2, length:2 assign to FOPL16
    send "XE" + FOPL16
    call "z_FOPCASH_DEL"
}

capture line:17, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:17, column:2, length:2 assign to FOPL17
    send "XE" + FOPL17
    call "z_FOPCASH_DEL"
}

capture line:18, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:18, column:2, length:2 assign to FOPL18
    send "XE" + FOPL18
    call "z_FOPCASH_DEL"
}

capture line:19, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:19, column:2, length:2 assign to FOPL19
    send "XE" + FOPL19
    call "z_FOPCASH_DEL"
}

capture line:20, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:20, column:2, length:2 assign to FOPL20
    send "XE" + FOPL20
    call "z_FOPCASH_DEL"
}

capture line:21, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:21, column:2, length:2 assign to FOPL21
    send "XE" + FOPL21
    call "z_FOPCASH_DEL"
}

capture line:22, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:22, column:2, length:2 assign to FOPL22
    send "XE" + FOPL22
    call "z_FOPCASH_DEL"
}

capture line:23, column:5, length:2 assign to FOP
if (FOP=="FP"){
    capture line:23, column:2, length:2 assign to FOPL23
    send "XE" + FOPL23
    call "z_FOPCASH_DEL"
}

capture line:24, column:1, length:2 assign to checkNext
if (checkNext == ")>"){
    send "MD"
    call "z_FOPCASH_DEL"                                                                 
}

