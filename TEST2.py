mandatory ask "Please enter the PNR:" assign to PNR
send "RT"+PNR

// capturing airline:
  capture line

choose "Do you want to" {
    when ("Proceed") {
    //RTTN
        send "RTTN"
    choose "Is there's any DT?"{
        when ("Yes") {}
        when ("No") {}
    }
    //TWD
        capture line:2, column:2, length:2 assign to LineNumber
        send "TWD/l"+LineNumber
        send "tqt"
        capture line:1, column:1, length:3 assign to tqtSpace
        if (tqtSpace == "T  "){
            capture  line:2, column:1, length:2 assign to tqtNumber
            send "tqt/t" +tqtNumber
        }
    //FXR/k/r,up
        send "FXR/K/R,UP"
  send "FQQ1"
    //FXR SELECTION
        choose "Next Action..?" {
          when ("Proceed"){
      choose "Continue?"{
        when ("Yes"){
          send "trdc/all"
          send "tte/all"
          send "fxb/k/r,up"
          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"
            }
          capture line:1, column: 1, length: 12 assign to CheckSM
            if (CheckSM == "SIMULTANEOUS"){
            send "ir"
            send "tte/all"
            send "fxb/k/r,up"
            send "rfRAMADAN;er" 
            send "er"
          }


          send "tth"
          choose "have you taken the deal?" until "yes"{
            when ("No"){
                send "ir"
                send "tte/all"
          send "fxb/k/r,up"
          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"
            }
          capture line:1, column: 1, length: 12 assign to CheckSM
            if (CheckSM == "SIMULTANEOUS"){
            send "ir"
            send "tte/all"
            send "fxb/k/r,up"
            send "rfRAMADAN;er" 
            send "er"
            send "tth"
          }
            send "tth"
            }
          }
          send "tth"
          send "fpcash"
          send "fm0"
          send "rttn"
          ask "Enter (number1-number2) to delete FA Elements" assign to XEDelete
          send "XE" +XEDelete
          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"}
          ask "is this office is RUHAA2218 or RUHAA2196 ?" assign to officeID
          send "qe/" +officeID +"/21c0"    
        }
        when ("NO"){
          send "ig"
        }
      }

    }
    when ("Search with FXX"){
      send "fxx/r,up"
      ask "Enter number of ticket pricing to display" assign to FQQ1
      send "fqq" +FQQ1
      choose "is it ok?"{
    when ("Yes, Proceed!"){
    ask "Are You sure to take line number? " assign to T
    send "trdc/all"
          send "tte/all"
          send "fxr/k/r,up"
    send "fxp/r,up"
    ask "ENTER the Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount
    send "FXT" +FQQ1 +"/" +PaxCount
    choose "There're Children or Infants?"{
          when ("Yes, Children only"){
      group{
      ask "What's the Child price line? (Type it)" assign to CHDLine
      ask "ENTER the CHD Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +CHDLine +"/" +PaxCount1
    }
    when ("Yes, Children and Infants"){
      group{
      ask "What's the Child price line? (Type it)" assign to CHDLine
      ask "ENTER the CHD Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      ask "What's the Infant price line? (Type it)" assign to INFLine
      ask "ENTER the INF Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount2
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +CHDLine +"/" +PaxCount1

      send "fxr"
      send "fxp/r,up"
        send "FXT" +INFLine +"/" +PaxCount2

    }
    when ("Yes, Infants only"){
      group{
      ask "What's the Infant price line? (Type it)" assign to INFLine
      ask "ENTER the INF Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +INFLine +"/" +PaxCount1

    }
    when ("No, All are Adults"){

    }
    }

          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"
            }
          capture line:1, column: 1, length: 12 assign to CheckSM
            if (CheckSM == "SIMULTANEOUS"){
            // repeat
    send "tte/all"
        call "FXX_TEST"           

}
        send "rfRAMADAN;er"
        send "er"

          send "tth"
          choose "have you taken the deal?"{
            when ("Yes"){}
            when ("No"){
                send "fxx/r,up"
      ask "Enter number of ticket pricing to display" assign to FQQ1
      send "fqq" +FQQ1
      choose "is it ok?"{
    when ("Yes, Proceed!"){
    ask "Are You sure to take line number? " assign to T
    send "trdc/all"
          send "tte/all"
          send "fxr/k/r,up"
    send "fxp/r,up"
    ask "ENTER the Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount
    send "FXT" +FQQ1 +"/" +PaxCount
    choose "There're Children or Infants?"{
          when ("Yes, Children only"){
      group{
      ask "What's the Child price line? (Type it)" assign to CHDLine
      ask "ENTER the CHD Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +CHDLine +"/" +PaxCount1
    }
    when ("Yes, Children and Infants"){
      group{
      ask "What's the Child price line? (Type it)" assign to CHDLine
      ask "ENTER the CHD Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      ask "What's the Infant price line? (Type it)" assign to INFLine
      ask "ENTER the INF Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount2
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +CHDLine +"/" +PaxCount1

      send "fxr"
      send "fxp/r,up"
        send "FXT" +INFLine +"/" +PaxCount2

    }
    when ("Yes, Infants only"){
      group{
      ask "What's the Infant price line? (Type it)" assign to INFLine
      ask "ENTER the INF Passengers counting that's appeared as P1 or P1-Px" assign to PaxCount1
      }
      send "fxr"
      send "fxp/r,up"
        send "FXT" +INFLine +"/" +PaxCount1

    }
    when ("No, All are Adults"){

    }
    }

          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"
            }
          capture line:1, column: 1, length: 12 assign to CheckSM
            if (CheckSM == "SIMULTANEOUS"){
            // repeat
    send "tte/all"
        call "FXX_TEST"           

}
        send "rfRAMADAN;er"
        send "er"

          send "tth"
            }
          }
}
}
          send "fpcash"
          send "fm0"
          send "rttn"
          ask "Enter (number1-number2) to delete FA Elements" assign to XEDelete
          send "XE" +XEDelete
          send "rfRAMADAN;er"
          capture line:1, column:1, length:7 assign to Warning
          if (Warning =="WARNING"){send "er"}
          ask "is this office is RUHAA2218 or RUHAA2196 ?" assign to officeID
          send "qe/" +officeID +"/21c0"

        }
        when ("NO, retry"){
          call "FXX_TEST"
  }
        when ("No, Ignore"){
          send "IG"  
        }
      }    

    }

    when ("Ignore"){

      send "ig"
    }


  }
}


//ig
    when ("Ignore") {
        send "ig"
    }
}



