  mandatory ask "Please enter the PNR:" assign to PNR
  send "RT"+PNR


  choose "Do you want to" {
      when ("Proceed") {
         // Checking Airline(s) and Travel date
  capture line: 3, column:4, length:2 assign to TS1
  if (TS1=="  "){
    capture line:3, column:6, length:2 assign to Airline1
    capture line:3, column:15, length:5 assign to TD1
    capture line:3, column:30, length:2 assign to ConST1
    // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
    if (Airline1=="A3") {
      send "A3 airline is non-voidable for (P,U,T,S) Classes"
      send "ig"
    }
    if (Airline1=="ER"){
      send "ER airline is non-voidable"
      send "ig"
    }
    if (Airline1=="H1"){
      send "H1 airline is non-voidable"
      send "ig"
    }
    if (Airline1=="NP"){
      send "NP airline is non-voidable"
      send "ig"
    }
    if (Airline1=="R5"){
      send "R5 airline is non-voidable"
      send "ig"
    }
    if (Airline1=="UK"){
      ask "Is it connected with AI (Air India)?" assign to qz1
    }
    if (Airline1=="NE"){
      ask "Is it tomorrow?" assign to qz2
      send " NE airline is non-voidable within 24HRs"
      ask "Is it tomorrow?" assign to qz3
      }
    //Today dates aren't considered
    if (TD1== today){
      send  "No void for today flights"
      send "ig"
    }
  }
      capture line: 4, column:4, length:2 assign to TS2
      if (TS2=="  "){
        capture line:4, column:6, length:2 assign to Airline2
        capture line:4, column:15, length:5 assign to TD2
        capture line:4, column:30, length:2 assign to ConST2
        // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
        if (Airline2=="A3") {
          send "A3 airline is non-voidable for (P,U,T,S) Classes"
          send "ig"
        }
        if (Airline2=="ER"){
          send "ER airline is non-voidable"
          send "ig"
        }
        if (Airline2=="H1"){
          send "H1 airline is non-voidable"
          send "ig"
        }
        if (Airline2=="NP"){
          send "NP airline is non-voidable"
          send "ig"
        }
        if (Airline2=="R5"){
          send "R5 airline is non-voidable"
          send "ig"
        }
        if (Airline2=="UK"){
          ask "Is it connected with AI (Air India)?" assign to qz4
        }
        if (Airline2=="NE"){
          ask "Is it tomorrow?" assign to qz5
          send " NE airline is non-voidable within 24HRs"
          ask "Is it tomorrow?" assign to qz6
        }

        //Today dates aren't considered
        if (TD2== today){
          send  "No void for today flights"
          send "ig"
        }
      }
          capture line: 5, column:4, length:2 assign to TS3
          if (TS3=="  "){
            capture line:5, column:6, length:2 assign to Airline3
            capture line:5, column:15, length:5 assign to TD3
            capture line:5, column:30, length:2 assign to ConST3
            // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
            if (Airline3=="A3") {
              send "A3 airline is non-voidable for (P,U,T,S) Classes"
              send "ig"
            }
            if (Airline3=="ER"){
              send "ER airline is non-voidable"
              send "ig"
            }
            if (Airline3=="H1"){
              send "H1 airline is non-voidable"
              send "ig"
            }
            if (Airline3=="NP"){
              send "NP airline is non-voidable"
              send "ig"
            }
            if (Airline3=="R5"){
              send "R5 airline is non-voidable"
              send "ig"
            }
            if (Airline3=="UK"){
              ask "Is it connected with AI (Air India)?" assign to qz7
            }
            if (Airline3=="NE"){
              ask "Is it tomorrow?" assign to qz8
              send " NE airline is non-voidable within 24HRs"
              ask "Is it tomorrow?" assign to qz9
            }

            //Today dates aren't considered
            if (TD3== today){
              send  "No void for today flights"
              send "ig"
            }
          }
            capture line: 6, column:4, length:2 assign to TS4
            if (TS4=="  "){
              capture line:6, column:6, length:2 assign to Airline4
              capture line:6, column:15, length:5 assign to TD4
              capture line:6, column:30, length:2 assign to ConST4
              // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
              if (Airline4=="A3") {
                send "A3 airline is non-voidable for (P,U,T,S) Classes"
                send "ig"
              }
              if (Airline4=="ER"){
                send "ER airline is non-voidable"
                send "ig"
              }
              if (Airline4=="H1"){
                send "H1 airline is non-voidable"
                send "ig"
              }
              if (Airline4=="NP"){
                send "NP airline is non-voidable"
                send "ig"
              }
              if (Airline4=="R5"){
                send "R5 airline is non-voidable"
                send "ig"
              }
              if (Airline4=="UK"){
                ask "Is it connected with AI (Air India)?" assign to qz10
              }
              if (Airline4=="NE"){
                ask "Is it tomorrow?" assign to qz11
                send " NE airline is non-voidable within 24HRs"
                ask "Is it tomorrow?" assign to qz12
              }

              //Today dates aren't considered
              if (TD4== today){
                send  "No void for today flights"
                send "ig"
              }
            }
              capture line: 7, column:4, length:2 assign to TS5
              if (TS5=="  "){
                capture line:7, column:6, length:2 assign to Airline5
                capture line:7, column:15, length:5 assign to TD5
                capture line:7, column:30, length:2 assign to ConST5
                // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                if (Airline5=="A3") {
                  send "A3 airline is non-voidable for (P,U,T,S) Classes"
                  send "ig"
                }
                if (Airline5=="ER"){
                  send "ER airline is non-voidable"
                  send "ig"
                }
                if (Airline5=="H1"){
                  send "H1 airline is non-voidable"
                  send "ig"
                }
                if (Airline5=="NP"){
                  send "NP airline is non-voidable"
                  send "ig"
                }
                if (Airline5=="R5"){
                  send "R5 airline is non-voidable"
                  send "ig"
                }
                if (Airline5=="UK"){
                  ask "Is it connected with AI (Air India)?" assign to qz13
                }
                if (Airline5=="NE"){
                  ask "Is it tomorrow?" assign to qz14
                  send " NE airline is non-voidable within 24HRs"
                  ask "Is it tomorrow?" assign to qz15
                }

                //Today dates aren't considered
                if (TD5== today){
                  send  "No void for today flights"
                  send "ig"
                }
              }
                capture line: 8, column:4, length:2 assign to TS6
                if (TS6=="  "){
                  capture line:8, column:6, length:2 assign to Airline6
                  capture line:8, column:15, length:5 assign to TD6
                  capture line:8, column:30, length:2 assign to ConST6
                  // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                  if (Airline6=="A3") {
                    send "A3 airline is non-voidable for (P,U,T,S) Classes"
                    send "ig"
                  }
                  if (Airline6=="ER"){
                    send "ER airline is non-voidable"
                    send "ig"
                  }
                  if (Airline6=="H1"){
                    send "H1 airline is non-voidable"
                    send "ig"
                  }
                  if (Airline6=="NP"){
                    send "NP airline is non-voidable"
                    send "ig"
                  }
                  if (Airline6=="R5"){
                    send "R5 airline is non-voidable"
                    send "ig"
                  }
                  if (Airline6=="UK"){
                    ask "Is it connected with AI (Air India)?" assign to qz16
                  }
                  if (Airline6=="NE"){
                    ask "Is it tomorrow?" assign to qz17
                    send " NE airline is non-voidable within 24HRs"
                    ask "Is it tomorrow?" assign to qz18
                  }

                  //Today dates aren't considered
                  if (TD6== today){
                    send  "No void for today flights"
                    send "ig"
                  }
                }
                  capture line: 9, column:4, length:2 assign to TS7
                  if (TS7=="  "){
                    capture line:9, column:6, length:2 assign to Airline7
                    capture line:9, column:15, length:5 assign to TD7
                    capture line:9, column:30, length:2 assign to ConST7
                    // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                    if (Airline7=="A3") {
                      send "A3 airline is non-voidable for (P,U,T,S) Classes"
                      send "ig"
                    }
                    if (Airline7=="ER"){
                      send "ER airline is non-voidable"
                      send "ig"
                    }
                    if (Airline7=="H1"){
                      send "H1 airline is non-voidable"
                      send "ig"
                    }
                    if (Airline7=="NP"){
                      send "NP airline is non-voidable"
                      send "ig"
                    }
                    if (Airline7=="R5"){
                      send "R5 airline is non-voidable"
                      send "ig"
                    }
                    if (Airline7=="UK"){
                      ask "Is it connected with AI (Air India)?" assign to qz19
                    }
                    if (Airline7=="NE"){
                      ask "Is it tomorrow?" assign to qz0
                      send " NE airline is non-voidable within 24HRs"
                      ask "Is it tomorrow?" assign to qz21
                    }

                    //Today dates aren't considered
                    if (TD7== today){
                      send  "No void for today flights"
                      send "ig"
                    }
                  }
                    capture line: 10, column:4, length:2 assign to TS8
                    if (TS8=="  "){
                      capture line:10, column:6, length:2 assign to Airline8
                      capture line:10, column:15, length:5 assign to TD8
                      capture line:10, column:30, length:2 assign to ConST8
                      // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                      if (Airline8=="A3") {
                        send "A3 airline is non-voidable for (P,U,T,S) Classes"
                        send "ig"
                      }
                      if (Airline8=="ER"){
                        send "ER airline is non-voidable"
                        send "ig"
                      }
                      if (Airline8=="H1"){
                        send "H1 airline is non-voidable"
                        send "ig"
                      }
                      if (Airline8=="NP"){
                        send "NP airline is non-voidable"
                        send "ig"
                      }
                      if (Airline8=="R5"){
                        send "R5 airline is non-voidable"
                        send "ig"
                      }
                      if (Airline8=="UK"){
                        ask "Is it connected with AI (Air India)?" assign to qz22
                      }
                      if (Airline8=="NE"){
                        ask "Is it tomorrow?" assign to qz23
                        send " NE airline is non-voidable within 24HRs"
                        ask "Is it tomorrow?" assign to qz24
                      }

                      //Today dates aren't considered
                      if (TD8== today){
                        send  "No void for today flights"
                        send "ig"
                      }
                    }
                            capture line: 11, column:4, length:2 assign to TS9
                            if (TS9=="  "){
                              capture line:11, column:6, length:2 assign to Airline9
                              capture line:11, column:15, length:5 assign to TD9
                              capture line:11, column:30, length:2 assign to ConST9
                              // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                              if (Airline9=="A3") {
                                send "A3 airline is non-voidable for (P,U,T,S) Classes"
                                send "ig"
                              }
                              if (Airline9=="ER"){
                                send "ER airline is non-voidable"
                                send "ig"
                              }
                              if (Airline9=="H1"){
                                send "H1 airline is non-voidable"
                                send "ig"
                              }
                              if (Airline9=="NP"){
                                send "NP airline is non-voidable"
                                send "ig"
                              }
                              if (Airline9=="R5"){
                                send "R5 airline is non-voidable"
                                send "ig"
                              }
                              if (Airline9=="UK"){
                                ask "Is it connected with AI (Air India)?" assign to qz25
                              }
                              if (Airline9=="NE"){
                                ask "Is it tomorrow?" assign to qz26
                                send " NE airline is non-voidable within 24HRs"
                                ask "Is it tomorrow?" assign to qz27
                              }

                              //Today dates aren't considered
                              if (TD9== today){
                                send  "No void for today flights"
                                send "ig"
                              }
                            }
                              capture line: 12, column:4, length:2 assign to TS10
                              if (TS10=="  "){
                                capture line:12, column:6, length:2 assign to Airline10
                                capture line:12, column:15, length:5 assign to TD10
                                capture line:12, column:30, length:2 assign to ConST10
                                // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                                if (Airline10=="A3") {
                                  send "A3 airline is non-voidable for (P,U,T,S) Classes"
                                  send "ig"
                                }
                                if (Airline10=="ER"){
                                  send "ER airline is non-voidable"
                                  send "ig"
                                }
                                if (Airline10=="H1"){
                                  send "H1 airline is non-voidable"
                                  send "ig"
                                }
                                if (Airline10=="NP"){
                                  send "NP airline is non-voidable"
                                  send "ig"
                                }
                                if (Airline10=="R5"){
                                  send "R5 airline is non-voidable"
                                  send "ig"
                                }
                                if (Airline10=="UK"){
                                  ask "Is it connected with AI (Air India)?" assign to qz28
                                }
                                if (Airline10=="NE"){
                                  ask "Is it tomorrow?" assign to qz29
                                  send " NE airline is non-voidable within 24HRs"
                                  ask "Is it tomorrow?" assign to qz30
                                }

                                //Today dates aren't considered
                                if (TD10== today){
                                  send  "No void for today flights"
                                  send "ig"
                                }
                              }
                                capture line: 13, column:4, length:2 assign to TS11
                                if (TS11=="  "){
                                  capture line:13, column:6, length:2 assign to Airline11
                                  capture line:13, column:15, length:5 assign to TD11
                                  capture line:13, column:30, length:2 assign to ConST11
                                  // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                                  if (Airline11=="A3") {
                                    send "A3 airline is non-voidable for (P,U,T,S) Classes"
                                    send "ig"
                                  }
                                  if (Airline11=="ER"){
                                    send "ER airline is non-voidable"
                                    send "ig"
                                  }
                                  if (Airline11=="H1"){
                                    send "H1 airline is non-voidable"
                                    send "ig"
                                  }
                                  if (Airline11=="NP"){
                                    send "NP airline is non-voidable"
                                    send "ig"
                                  }
                                  if (Airline11=="R5"){
                                    send "R5 airline is non-voidable"
                                    send "ig"
                                  }
                                  if (Airline11=="UK"){
                                    ask "Is it connected with AI (Air India)?" assign to qz31
                                  }
                                  if (Airline11=="NE"){
                                    ask "Is it tomorrow?" assign to qz32
                                    send " NE airline is non-voidable within 24HRs"
                                    ask "Is it tomorrow?" assign to qz33
                                  }

                                  //Today dates aren't considered
                                  if (TD11== today){
                                    send  "No void for today flights"
                                    send "ig"
                                  }
                                }
                                  capture line: 14, column:4, length:2 assign to TS12
                                  if (TS12=="  "){
                                    capture line:14, column:6, length:2 assign to Airline12
                                    capture line:14, column:15, length:5 assign to TD12
                                    capture line:14, column:30, length:2 assign to ConST12
                                    // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                                    if (Airline12=="A3") {
                                      send "A3 airline is non-voidable for (P,U,T,S) Classes"
                                      send "ig"
                                    }
                                    if (Airline12=="ER"){
                                      send "ER airline is non-voidable"
                                      send "ig"
                                    }
                                    if (Airline12=="H1"){
                                      send "H1 airline is non-voidable"
                                      send "ig"
                                    }
                                    if (Airline12=="NP"){
                                      send "NP airline is non-voidable"
                                      send "ig"
                                    }
                                    if (Airline12=="R5"){
                                      send "R5 airline is non-voidable"
                                      send "ig"
                                    }
                                    if (Airline12=="UK"){
                                      ask "Is it connected with AI (Air India)?" assign to qz34
                                    }
                                    if (Airline12=="NE"){
                                      ask "Is it tomorrow?" assign to qz35
                                      send " NE airline is non-voidable within 24HRs"
                                      ask "Is it tomorrow?" assign to qz36
                                    }

                                    //Today dates aren't considered
                                    if (TD12== today){
                                      send  "No void for today flights"
                                      send "ig"
                                    }
                                  }
                                    capture line: 15, column:4, length:2 assign to TS13
                                    if (TS13=="  "){
                                      capture line:15, column:6, length:2 assign to Airline13
                                      capture line:15, column:15, length:5 assign to TD13
                                      capture line:15, column:30, length:2 assign to ConST13
                                      // Non-voidable airlines: A3, ER, H1, NP, R5, UK with AI
                                      if (Airline13=="A3") {
                                        send "A3 airline is non-voidable for (P,U,T,S) Classes"
                                        send "ig"
                                      }
                                      if (Airline13=="ER"){
                                        send "ER airline is non-voidable"
                                        send "ig"
                                      }
                                      if (Airline13=="H1"){
                                        send "H1 airline is non-voidable"
                                        send "ig"
                                      }
                                      if (Airline13=="NP"){
                                        send "NP airline is non-voidable"
                                        send "ig"
                                      }
                                      if (Airline13=="R5"){
                                        send "R5 airline is non-voidable"
                                        send "ig"
                                      }
                                      if (Airline13=="UK"){
                                        ask "Is it connected with AI (Air India)?" assign to qz37
                                      }
                                      if (Airline13=="NE"){
                                        ask "Is it tomorrow?" assign to qz38
                                        send " NE airline is non-voidable within 24HRs"
                                        ask "Is it tomorrow?" assign to qz39
                                      }

                                      //Today dates aren't considered
                                      if (TD13== today){
                                        send  "No void for today flights"
                                        send "ig"
                                      }
                                    }

  //checking if there's an emd
  send "tqm"
          capture line:1, column:1, length:20 assign to emdTest
          if (emdTest != "NO TSM RECORD EXISTS"){
          send "EMD! Please stop and check."
          mandatory ask "Ignore!" assign to qz5
          send "ig"
          }

  //getting the office IATA code
  send "PV"
  capture line:8, column:30, length:8 assign to thisOffice

  //opening the ticket:
  send "RTTN"
  capture line:1, column:1, length:16 assign to rttnWarning
  if (rttnWarning=="NO ELEMENT FOUND"){
    send "ig"
  }
  capture line:2, column:5, length:2 assign to FAcheck
  if (FAcheck=="FA"){
      capture line:2, column:2, length:2 assign to FANo
      send "TWD/L" +FANo
  }
  else{
      capture line:3, column:5, length:2 assign to FAcheck
      if (FAcheck=="FA"){
          capture line:3, column:2, length:2 assign to FANo1
          send "TWD/L" +FANo1
      }
      else{
          mandatory ask "Enter a (Non-Infant) Ticket line number" assign to TL1
          send "TWD/L" +TL1
      }
  }


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

ticketingOffice  }
  if (DOITEST!=today){
    send "N0 Void as DOI-" +DOITEST
    send "ig"
  }
  if (thisOffice!= ticketingOffice){
    send "PV/" +ticketingOffice
    send "ig"
  }

  //checking if this is an Infant ticket
  if (paxST=="INF"){
    ask "This's an Infant ticket, please enter a different ticket line no." assign to TL2
      send "TWD/l" +TL2
  }

  //checking the baggege and status
  capture line:3, column:47, length:2 assign to status1
  if (status1=="ST"){
    capture line:4, column:47, length:1 assign to FST1
    capture line:4, column:62, length:3 assign to BG1

    capture line:5, column:47, length:1 assign to FST2
    capture line:5, column:62, length:3 assign to BG2

    capture line:6, column:47, length:1 assign to FST3
    capture line:6, column:62, length:3 assign to BG3

    capture line:7, column:47, length:1 assign to FST4
    capture line:7, column:62, length:3 assign to BG4
  }
    capture line:4, column:47, length:2 assign to status2
    if (status2=="ST"){
      capture line:5, column:47, length:1 assign to FST1
      capture line:5, column:62, length:3 assign to BG1

      capture line:6, column:47, length:1 assign to FST2
      capture line:6, column:62, length:3 assign to BG2

      capture line:7, column:47, length:1 assign to FST3
      capture line:7, column:62, length:3 assign to BG3

      capture line:8, column:47, length:1 assign to FST4
      capture line:8, column:62, length:3 assign to BG4
    }

  if (FST1=="A"){
    }
    else{
        if(FST1=="O"){
        }
        else{
            if (FST1==""){
            }
            else{
            send "check status"
            send "ig"
            }
        }
    }
    if (FST2=="A"){
    }
    else{
        if(FST2=="O"){
        }
        else{
            if (FST2==""){
            }
            else{
            send "check status"
            send "ig"
            }
        }
    }
    if (FST3=="A"){
    }
    else{
        if(FST3=="O"){
        }
        else{
            if (FST3==""){
            }
            else{
            send "check status"
            send "ig"
            }
        }
    }
    if (FST4=="A"){
    }
    else{
        if(FST4=="O"){
        }
        else{
            if (FST4==""){
            }
            else{
            send "check status"
            send "ig"
            }
        }
    }


  send "tqt"
          capture line:1, column:1, length:3 assign to tqtSpace
          if (tqtSpace == "T  "){
              capture  line:2, column:1, length:2 assign to tqtNumber
              send "tqt/t" +tqtNumber
          }
          // WAIT
          ask "Ok?" assign to aa1
          //FXR/k/r,up
          send "FXR/K/R,UP"
          send "FQQ1"
          //FXR SELECTION
          choose "Next Action..?" {
            when ("Proceed"){
              choose "Continue?"{
                  when ("Yes"){
                      send "trdc/all"
                      capture line:1, column:1, length:26 assign to Voidmsg
                      if (Voidmsg!="OK - DOCUMENT(S) CANCELLED"){
                      ask "Is it voided?" assign to trdcr
                      }
                      send "tte/all"
                      send "fxb/k/r,up"
                      send "rfRAMADAN;er"
                      capture line:1, column:1, length:7 assign to Warning
                      if (Warning =="WARNING"){
                          send "er"
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
                                  send "rfr;er"
                                  send "er"
                                  send "tth"
                          }
                      }
                      send "tth"
                      send "fpcash"
                      send "fm0"
                      call "z_RTTN_DEL"          
                      send "rfRAMADAN;er"
                      capture line:1, column:1, length:7 assign to Warning
                      if (Warning =="WARNING"){send "er"}
                       choose "Manual issuing or Queued?" {
                          when ("Queued"){
                              ask "is this office is RUHAA2218 or RUHAA2196 ?" assign to officeID
                              send "qe/" +officeID +"/21c0"
                          }
                          when ("manual"){
                              send "rm fresh issue"
                              send "rm first issue"
                              send "rm skip hf"
                              send "rm amex"
                              send "rfr;er"
                              send "ttp/rt"
                              send "rttn"
                              capture line:2, column:2, length:2 assign to LineNumber
                              send "TWD/l"+LineNumber
                          }
                        }    
                      }
                      when ("NO"){
                          send "ig"
                      }
                   }

              }
              when ("Search with FXX"){    
                  call "FXX_TEST"
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



