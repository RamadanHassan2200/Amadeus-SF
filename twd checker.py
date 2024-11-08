// capture the origin and the destination
capture line:2, column:5, length:6 assign to OD

//checking office & DOI
  capture line:2, column:53, length:3 assign to IOITEST
  if (IOITEST=="IOI"){
    capture line:2, column:44, length:5 assign to DOITEST
    capture line:2, column:57, length:8 assign to ticketingOffice
    capture line:3, column:32, length:3 assign to paxST
  }
  capture line:3, column:53, length:3 assign to IOITEST
  if (IOITEST=="IOI"){
    capture line:3, column:44, length:5 assign to DOITEST
    capture line:3, column:57, length:8 assign to ticketingOffice
    capture line:4, column:32, length:3 assign to paxST
  }
  
  if (DOITEST!=today){
    send "N0 Void as DOI-" +DOITEST
    ask "Please check again!" assign to qz5
    send "ig"
  }


//checking the baggege and status
  
capture line:4, column:30, length:2 assign to OK1
if (OK1=="OK"){
   capture line:4, column:47, length:1 assign to FST1
   capture line:4, column:62, length:2 assign to Bg1
   assign "1" to segCT
}
capture line:5, column:30, length:2 assign to OK2
if (OK2=="OK"){
    if (segCT=="1"){
      capture line:5, column:47, length:1 assign to FST2
      capture line:5, column:62, length:2 assign to Bg2
      assign "2" to segCT
    }
    else{
      capture line:5, column:47, length:1 assign to FST1
      capture line:5, column:62, length:2 assign to Bg1
      assign "1" to segCT
    }
}
capture line:6, column:30, length:2 assign to OK3
if (OK3=="OK"){
  if (segCT=="2"){
      capture line:6, column:47, length:1 assign to FST3
      capture line:6, column:62, length:2 assign to Bg3
      assign "3" to segCT
  }
  else{
      capture line:6, column:47, length:1 assign to FST2
      capture line:6, column:62, length:2 assign to Bg2
      assign "2" to segCT
  }
}
capture line:7, column:30, length:2 assign to OK4
if (OK4=="OK"){
  if (segCT=="3"){
      capture line:7, column:47, length:1 assign to FST4
      capture line:7, column:62, length:2 assign to Bg4
      assign "4" to segCT
  }
  else{
      capture line:7, column:47, length:1 assign to FST3
      capture line:7, column:62, length:2 assign to Bg3
      assign "3" to segCT
  }
}
capture line:8, column:30, length:2 assign to OK5
if (OK5=="OK"){
  if (segCT=="4"){
      send "Please Recheck!" 
      ask "Check the segment number" assign to qz5
  }
  else{
      capture line:8, column:47, length:1 assign to FST4
      capture line:8, column:62, length:2 assign to Bg4
      assign "4" to segCT
  }
}


if (segCT=="1"){
  if (BG1== "  "){
    assign "0 " to BG1
  }
  if (FST1== "O"){
    assign "OPENED" to FST
  }
  if (FST1== "A"){
    assign "OPENED" to FST
  }
  if (FST1== "V"){
    assign "VOIDED" to FST
  }
  if (FST1!="A"){
    if (FST1!="O"){
      if (FST1!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }
  
}

if (segCT=="2"){
  if (BG1== "  "){
    assign "0 " to BG1
  }
  if (BG2== "  "){
    assign "0 " to BG2
  }
  
  if (FST1== "O"){
    assign "OPENED" to FST
  }
  if (FST1== "A"){
    assign "OPENED" to FST
  }
  if (FST1== "V"){
    assign "VOIDED" to FST
  }
  if (FST1!="A"){
    if (FST1!="O"){
      if (FST1!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }

  if (FST2== "O"){
    assign "OPENED" to FST
  }
  if (FST2== "A"){
    assign "OPENED" to FST
  }
  if (FST2== "V"){
    assign "VOIDED" to FST
  }
  if (FST2!="A"){
    if (FST2!="O"){
      if (FST2!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }
}

if (segCT=="3"){
  if (BG1== "  "){
    assign "0 " to BG1
  }
  if (BG2== "  "){
    assign "0 " to BG2
  }
  if (BG3== "  "){
    assign "0 " to BG3
  }

  if (FST1== "O"){
    assign "OPENED" to FST
  }
  if (FST1== "A"){
    assign "OPENED" to FST
  }
  if (FST1== "V"){
    assign "VOIDED" to FST
  }
  if (FST1!="A"){
    if (FST1!="O"){
      if (FST1!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }

  if (FST2== "O"){
    assign "OPENED" to FST
  }
  if (FST2== "A"){
    assign "OPENED" to FST
  }
  if (FST2== "V"){
    assign "VOIDED" to FST
  }
  if (FST2!="A"){
    if (FST2!="O"){
      if (FST2!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }

  if (FST3== "O"){
    assign "OPENED" to FST
  }
  if (FST3== "A"){
    assign "OPENED" to FST
  }
  if (FST3== "V"){
    assign "VOIDED" to FST
  }
  if (FST3!="A"){
    if (FST3!="O"){
      if (FST3!="V"){
        send "Please Recheck!"
        ask "Check the segment status" assign to qz5
        send "ig"
      }
    }
  }

}

if (segCT=="4"){
if (BG1== "  "){
  assign "0 " to BG1
}
if (BG2== "  "){
  assign "0 " to BG2
}
if (BG3== "  "){
  assign "0 " to BG3
}
if (BG4== "  "){
  assign "0 " to BG4
}

if (FST1== "O"){
  assign "OPENED" to FST
}
if (FST1== "A"){
  assign "OPENED" to FST
}
if (FST1== "V"){
  assign "VOIDED" to FST
}
if (FST1!="A"){
  if (FST1!="O"){
    if (FST1!="V"){
      send "Please Recheck!"
      ask "Check the segment status" assign to qz5
      send "ig"
    }
  }
}

if (FST2== "O"){
  assign "OPENED" to FST
}
if (FST2== "A"){
  assign "OPENED" to FST
}
if (FST2== "V"){
  assign "VOIDED" to FST
}
if (FST2!="A"){
  if (FST2!="O"){
    if (FST2!="V"){
      send "Please Recheck!"
      ask "Check the segment status" assign to qz5
      send "ig"
    }
  }
}

if (FST3== "O"){
  assign "OPENED" to FST
}
if (FST3== "A"){
  assign "OPENED" to FST
}
if (FST3== "V"){
  assign "VOIDED" to FST
}
if (FST3!="A"){
  if (FST3!="O"){
    if (FST3!="V"){
      send "Please Recheck!"
      ask "Check the segment status" assign to qz5
      send "ig"
    }
  }
}

if (FST4== "O"){
  assign "OPENED" to FST
}
if (FST4== "A"){
  assign "OPENED" to FST
}
if (FST4== "V"){
  assign "VOIDED" to FST
}
if (FST4!="A"){
  if (FST4!="O"){
    if (FST4!="V"){
      send "Please Recheck!"
      ask "Check the segment status" assign to qz5
      send "ig"
    }
  }
}

}

if (segCT=="1"){
  send "SRT" +"1" +paxST +OD +ticketingOffice +FST +Bg1
}
else{
  if (segCT=="2"){
    send "SRT" +"2" +paxST +OD +ticketingOffice +FST +Bg1 +BG2
  }
  else{
    if (segCT=="3"){
      send "SRT" +"3" +paxST +OD +ticketingOffice +FST +Bg1 +BG2 +Bg3
    }
    else{
      if (segCT=="4"){
      send "SRT" +"4" +paxST +OD +ticketingOffice +FST +Bg1 +BG2 +Bg3 +Bg4
      }
      else{
        send "IR"
        send "RTTN"
        mandatory ask "Please Enter a FA or FH line number:" assign to TWDFA
        send "TWD/L" +TWDFA
        call "FA_FH Checker"
      }
    }
  }
}