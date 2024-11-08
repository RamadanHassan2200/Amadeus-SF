RP/RUHAA28WH/RUHAA28WH            AA/SU   4SEP24/0138Z   U9PM8N
  3  SV1903 N 05SEP 4 RUHTIF HK2  0520 0655  05SEP  E  SV/U9PM8N
-------------------------------------------
capture line:2, column:30, length:2 assign to segHK1
capture line:3, column:30, length:2 assign to segHK2
capture line:4, column:30, length:2 assign to segHK3
capture line:5, column:30, length:2 assign to segHK4
capture line:6, column:30, length:2 assign to segHK5
capture line:7, column:30, length:2 assign to segHK6

if (segHK6=="HK"){
  append "6" to segCount
}
else{
  if (segHK5=="HK"){
    append "5" to segCount
  }
  else{
    if (segHK4=="HK"){
      append "4" to segCount
    }
    else{
      if (segHK3=="HK"){
        append "3" to segCount
      }
      else{
        if (segHK2=="HK"){
          append "2" to segCount
        }
        else{
          if (segHK1=="HK"){
            append "1" to segCount
          }
          else{
            send "There're No Segments Confirmed!"
            send "ig"
          }
        }
      }
    }
  }
}