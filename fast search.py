ask "what are the PNRS?" assign to pnrs
send "SRT" +pnrs

capture line:1, column:32, length:7 assign to PNR1
capture line:1, column:39, length:7 assign to PNR2
capture line:1, column:46, length:7 assign to PNR3
capture line:1, column:53, length:7 assign to PNR4
capture line:1, column:60, length:4 assign to PNR5p1
capture line:2, column:1, length:1 assign to secondline
if (secondline == "-"){
  capture line:1, column:2, length:3 assign to PNR5p2
  append PNR5p1 +"" +PNR5p2 to PNR5
}
  
//

send "RT" +PNR1
send "tqt"
            capture line:1, column:1, length:3 assign to tqtSpace
            if (tqtSpace == "T  "){
                capture  line:2, column:1, length:2 assign to tqtNumber
                send "tqt/t" +tqtNumber
            }

  send "FXR/k/r,up" 
  send "Fqq1"
  capture line:9, column:17, length:1 assign to firstSeg
  capture line:10, column:17, length:1 assign to secondSeg
  capture line:11, column:17, length:1 assign to thirdSeg
  capture line:12, column:17, length:1 assign to fourthSeg
  capture line:13, column:17, length:1 assign to fifthSeg
  capture line:14, column:17, length:1 assign to sixthSeg
  capture line:15, column:17, length:1 assign to seventhSeg
  capture line:16, column:17, length:1 assign to eighthSeg

  if (firstSeg == "*"){
    send "Star!"
  }
  if (secondSeg == "*"){
    send "Star!"
  }
  if (thirdSeg == "*"){
    send "Star!"
  }
  if (fourthSeg == "*"){
    send "Star!"
  }
  if (fifthSeg == "*"){
    send "Star!"
  }
  if (sixthSeg == "*"){
    send "Star!"
  }
  if (seventhSeg == "*"){
    send "Star!"
  }
  if (eighthSeg == "*"){
    send "Star!"
  }
  capture line:1, column:1, length:12 assign to starsign
  if (starsign=="CHECK FORMAT"){
  ask "Next action?" assign to tt
  }
  send "ig"
//
send "RT" +PNR1
send "tqt"
                capture line:1, column:1, length:3 assign to tqtSpace
                if (tqtSpace == "T  "){
                    capture  line:2, column:1, length:2 assign to tqtNumber
                    send "tqt/t" +tqtNumber
                }

      send "FXR/k/r,up" 
      send "Fqq1"
      capture line:9, column:17, length:1 assign to firstSeg
      capture line:10, column:17, length:1 assign to secondSeg
      capture line:11, column:17, length:1 assign to thirdSeg
      capture line:12, column:17, length:1 assign to fourthSeg
      capture line:13, column:17, length:1 assign to fifthSeg
      capture line:14, column:17, length:1 assign to sixthSeg
      capture line:15, column:17, length:1 assign to seventhSeg
      capture line:16, column:17, length:1 assign to eighthSeg

      if (firstSeg == "*"){
        send "Star!"
      }
      if (secondSeg == "*"){
        send "Star!"
      }
      if (thirdSeg == "*"){
        send "Star!"
      }
      if (fourthSeg == "*"){
        send "Star!"
      }
      if (fifthSeg == "*"){
        send "Star!"
      }
      if (sixthSeg == "*"){
        send "Star!"
      }
      if (seventhSeg == "*"){
        send "Star!"
      }
      if (eighthSeg == "*"){
        send "Star!"
      }
      capture line:1, column:1, length:12 assign to starsign
      if (starsign=="CHECK FORMAT"){
      ask "Next action?" assign to tt
      }
