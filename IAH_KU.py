// IAH_KU

//retrirval
mandatory ask "Enter the PNR: " assign to pnr
send "IG"

send "JGD/USN"
capture line:8, column:43, length:1 assign to agtName
capture line:8, column:44, length:1 assign to agtNameChar2
capture line:8, column:45, length:1 assign to agtNameChar3
capture line:8, column:46, length:1 assign to agtNameChar4
capture line:8, column:47, length:1 assign to agtNameChar5
capture line:8, column:48, length:1 assign to agtNameChar6
capture line:8, column:49, length:1 assign to agtNameChar7
capture line:8, column:50, length:1 assign to agtNameChar8
capture line:8, column:51, length:1 assign to agtNameChar9
capture line:8, column:52, length:1 assign to agtNameChar10
capture line:8, column:53, length:1 assign to agtNameChar11
capture line:8, column:54, length:1 assign to agtNameChar12
capture line:8, column:55, length:1 assign to agtNameChar13
capture line:8, column:56, length:1 assign to agtNameChar14
capture line:8, column:57, length:1 assign to agtNameChar15
capture line:8, column:58, length:1 assign to agtNameChar16
capture line:8, column:59, length:1 assign to agtNameChar17
capture line:8, column:60, length:1 assign to agtNameChar18
capture line:8, column:61, length:1 assign to agtNameChar19
capture line:8, column:62, length:1 assign to agtNameChar20
capture line:8, column:63, length:1 assign to agtNameChar21
capture line:8, column:64, length:1 assign to agtNameChar22

if (agtNameChar2!=" "){
append agtNameChar2 to agtName
if (agtNameChar3!=" "){
append agtNameChar3 to agtName
if (agtNameChar4!=" "){
append agtNameChar4 to agtName
if (agtNameChar5!=" "){
append agtNameChar5 to agtName
if (agtNameChar6!=" "){
append agtNameChar6 to agtName
if (agtNameChar7!=" "){
append agtNameChar7 to agtName
if (agtNameChar8!=" "){
append agtNameChar8 to agtName
if (agtNameChar9!=" "){
append agtNameChar9 to agtName
if (agtNameChar10!=" "){
append agtNameChar10 to agtName
if (agtNameChar11!=" "){
append agtNameChar11 to agtName
if (agtNameChar12!=" "){
append agtNameChar12 to agtName
if (agtNameChar13!=" "){
append agtNameChar13 to agtName
if (agtNameChar14!=" "){
append agtNameChar14 to agtName
if (agtNameChar15!=" "){
append agtNameChar15 to agtName
if (agtNameChar16!=" "){
append agtNameChar16 to agtName
if (agtNameChar17!=" "){
append agtNameChar17 to agtName
if (agtNameChar18!=" "){
append agtNameChar18 to agtName
if (agtNameChar19!=" "){
append agtNameChar19 to agtName
if (agtNameChar20!=" "){
append agtNameChar20 to agtName
if (agtNameChar21!=" "){
append agtNameChar21 to agtName
if (agtNameChar22!=" "){
append agtNameChar22 to agtName
}}}}}}}}}}}}}}}}}}}}}//agtNameChar2

if (agtName == "GUEST"){
  assign "SF" to agtName
}


send "rt" +pnr
// Checking Airline(s) and Travel date and passenger count
send "RTA"

capture line:2, column:30, length:2 assign to HK1Test
if (HK1Test=="HK"){
  assign "1" to segmentsCount
  capture line:2, column:6, length:2 assign to Airline1
  capture line:2, column:15, length:5 assign to TravelDate
  capture line:2, column:23, length:3 assign to OriginCity
  capture line:2, column:32, length:1 assign to PassengerCount
  capture line:3, column:30, length:2 assign to HKnextTest
  if (HKnextTest=="HK"){
    assign "2" to segmentsCount
    capture line:4, column:30, length:2 assign to HK3Test
    if (HK3Test=="HK"){
      assign "3" to segmentsCount
      capture line:5, column:30, length:2 assign to HK4Test
      if (HK4Test=="HK"){
          assign "4" to segmentsCount
          capture line:6, column:30, length:2 assign to HK5Test
          if (HK5Test=="HK"){
            assign "5" to segmentsCount
            capture line:7, column:30, length:2 assign to HK6Test
            if (HK6Test=="HK"){
                assign "6" to segmentsCount
                capture line:8, column:30, length:2 assign to HK7Test
                if (HK7Test=="HK"){
                    send "SmartFlow now working on more than 6 segments"
                    ask "ignore?" assign to qz5
                    send "ig"
                    call "test1"
                }
            }
          }
      }
    }
  }

}
else{
capture line:3, column:30, length:2 assign to HK2Test
if (HK2Test=="HK"){
  assign "1" to segmentsCount
  capture line:3, column:6, length:2 assign to Airline1
  capture line:3, column:15, length:5 assign to TravelDate
  capture line:3, column:23, length:3 assign to OriginCity
  capture line:3, column:32, length:1 assign to PassengerCount
  capture line:4, column:30, length:2 assign to HKnextTest
      if (HKnextTest=="HK"){
        assign "2" to segmentsCount
        capture line:5, column:30, length:2 assign to HK3Test
        if (HK3Test=="HK"){
          assign "3" to segmentsCount
          capture line:6, column:30, length:2 assign to HK4Test
          if (HK4Test=="HK"){
              assign "4" to segmentsCount
              capture line:7, column:30, length:2 assign to HK5Test
              if (HK5Test=="HK"){
                assign "5" to segmentsCount
                capture line:8, column:30, length:2 assign to HK6Test
                if (HK6Test=="HK"){
                    assign "6" to segmentsCount
                    capture line:9, column:30, length:2 assign to HK7Test
                    if (HK7Test=="HK"){
                        send "SmartFlow now working on more than 6 segments"
                        ask "ignore?" assign to qz5
                        send "ig"
                        call "test1"
                    }
                }
              }
          }
        }
      }
}
else{
  send "Not Confirmed Segments please, check again!"
  ask "Stop and Review" assign to qz5
  send "ig"
}
}


  send "tqt/t500"
  capture line:2, column:1, length:3 assign to TQTNumber1
  capture line:2, column:42, length:10 assign to TQTPrice1
  capture line:3, column:1, length:3 assign to TQTNumber2
  capture line:3, column:42, length:10 assign to TQTPrice2
  capture line:4, column:1, length:3 assign to TQTNumber3
  capture line:4, column:42, length:10 assign to TQTPrice3
  capture line:5, column:1, length:3 assign to TQTNumber4
  capture line:5, column:42, length:10 assign to TQTPrice4
  capture line:6, column:1, length:3 assign to TQTNumber5
  capture line:6, column:42, length:10 assign to TQTPrice5
  capture line:7, column:1, length:3 assign to TQTNumber6
  capture line:7, column:42, length:10 assign to TQTPrice6
  capture line:8, column:1, length:3 assign to TQTNumber7
  capture line:8, column:42, length:10 assign to TQTPrice7
  capture line:9, column:1, length:3 assign to TQTNumber8
  capture line:9, column:42, length:10 assign to TQTPrice8
  capture line:10, column:1, length:3 assign to TQTNumber9
  capture line:10, column:42, length:10 assign to TQTPrice9
  capture line:11, column:1, length:3 assign to TQTNumber10
  capture line:11, column:42, length:10 assign to TQTPrice10
  capture line:12, column:1, length:3 assign to TQTNumber11
  capture line:12, column:42, length:10 assign to TQTPrice11
  capture line:13, column:1, length:3 assign to TQTNumber12
  capture line:13, column:42, length:10 assign to TQTPrice12
  capture line:14, column:1, length:3 assign to TQTNumber13
  capture line:14, column:42, length:10 assign to TQTPrice13
  capture line:15, column:1, length:3 assign to TQTNumber14
  capture line:15, column:42, length:10 assign to TQTPrice14
  capture line:16, column:1, length:3 assign to TQTNumber15
  capture line:16, column:42, length:10 assign to TQTPrice15
  capture line:17, column:1, length:3 assign to TQTNumber16
  capture line:17, column:42, length:10 assign to TQTPrice16
  capture line:18, column:1, length:3 assign to TQTNumber17
  capture line:18, column:42, length:10 assign to TQTPrice17
  capture line:19, column:1, length:3 assign to TQTNumber18
  capture line:19, column:42, length:10 assign to TQTPrice18

  assign "0" to heighestTST
  if (TQTNumber1=="DEL"){
    assign "0" to TQTNumber1
  } 
  if (TQTNumber1==""){
    assign "0" to TQTNumber1
  }
  if (TQTNumber2=="DEL"){
    assign "0" to TQTNumber2
  } 
  if (TQTNumber2==""){
    assign "0" to TQTNumber2
  }
  if (TQTNumber3=="DEL"){
    assign "0" to TQTNumber3
  } 
  if (TQTNumber3==""){
    assign "0" to TQTNumber3
  }
  if (TQTNumber4=="DEL"){
    assign "0" to TQTNumber4
  } 
  if (TQTNumber4==""){
    assign "0" to TQTNumber4
  }
  if (TQTNumber5=="DEL"){
    assign "0" to TQTNumber5
  } 
  if (TQTNumber5==""){
    assign "0" to TQTNumber5
  }
  if (TQTNumber6=="DEL"){
    assign "0" to TQTNumber6
  } 
  if (TQTNumber6==""){
    assign "0" to TQTNumber6
  }
  if (TQTNumber7=="DEL"){
    assign "0" to TQTNumber7
  } 
  if (TQTNumber7==""){
    assign "0" to TQTNumber7
  }
  if (TQTNumber8=="DEL"){
    assign "0" to TQTNumber8
  } 
  if (TQTNumber8==""){
    assign "0" to TQTNumber8
  }
  if (TQTNumber9=="DEL"){
    assign "0" to TQTNumber9
  } 
  if (TQTNumber9==""){
    assign "0" to TQTNumber9
  }
  if (TQTNumber10=="DEL"){
    assign "0" to TQTNumber10
  } 
  if (TQTNumber10==""){
    assign "0" to TQTNumber10
  }
  if (TQTNumber11=="DEL"){
    assign "0" to TQTNumber11
  } 
  if (TQTNumber11==""){
    assign "0" to TQTNumber11
  }
  if (TQTNumber12=="DEL"){
    assign "0" to TQTNumber12
  } 
  if (TQTNumber12==""){
    assign "0" to TQTNumber12
  }
  if (TQTNumber13=="DEL"){
    assign "0" to TQTNumber13
  } 
  if (TQTNumber13==""){
    assign "0" to TQTNumber13
  }
  if (TQTNumber14=="DEL"){
    assign "0" to TQTNumber14
  } 
  if (TQTNumber14==""){
    assign "0" to TQTNumber14
  }
  if (TQTNumber15=="DEL"){
    assign "0" to TQTNumber15
  } 
  if (TQTNumber15==""){
    assign "0" to TQTNumber15
  }
  if (TQTNumber16=="DEL"){
    assign "0" to TQTNumber16
  } 
  if (TQTNumber16==""){
    assign "0" to TQTNumber16
  }
  if (TQTNumber17=="DEL"){
    assign "0" to TQTNumber17
  } 
  if (TQTNumber17==""){
    assign "0" to TQTNumber17
  }
  if (TQTNumber18=="DEL"){
    assign "0" to TQTNumber18
  } 
  if (TQTNumber18==""){
    assign "0" to TQTNumber18
  }

  if (TQTPrice1 =="E TTH     "){
      assign "0" to TQTPrice1
  }
  if (TQTPrice2 =="E TTH     "){
      assign "0" to TQTPrice2
  }
  if (TQTPrice3 =="E TTH     "){
      assign "0" to TQTPrice3
  }
  if (TQTPrice4 =="E TTH     "){
      assign "0" to TQTPrice4
  }
  if (TQTPrice5 =="E TTH     "){
      assign "0" to TQTPrice5
  }
  if (TQTPrice6 =="E TTH     "){
      assign "0" to TQTPrice6
  }
  if (TQTPrice7 =="E TTH     "){
      assign "0" to TQTPrice7
  }
  if (TQTPrice8 =="E TTH     "){
      assign "0" to TQTPrice8
  }
  if (TQTPrice9 =="E TTH     "){
      assign "0" to TQTPrice9
  }
  if (TQTPrice10 =="E TTH     "){
      assign "0" to TQTPrice10
  }
  if (TQTPrice11 =="E TTH     "){
      assign "0" to TQTPrice11
  }
  if (TQTPrice12 =="E TTH     "){
      assign "0" to TQTPrice12
  }
  if (TQTPrice13 =="E TTH     "){
      assign "0" to TQTPrice13
  }
  if (TQTPrice14 =="E TTH     "){
      assign "0" to TQTPrice14
  }
  if (TQTPrice15 =="E TTH     "){
      assign "0" to TQTPrice15
  }
  if (TQTPrice16 =="E TTH     "){
      assign "0" to TQTPrice16
  }
  if (TQTPrice17 =="E TTH     "){
      assign "0" to TQTPrice17
  }
  if (TQTPrice18 =="E TTH     "){
      assign "0" to TQTPrice18
  }

  assign "0" to heighestPrice
        
  if (TQTNumber1!="0"){
    if (TQTPrice1>heighestPrice){
      assign TQTNumber1 to heighestTST
      assign TQTPrice1 to heighestPrice
    }
  }
  if (TQTNumber2!="0"){
    if (TQTPrice2>heighestPrice){
      assign TQTNumber2 to heighestTST
      assign TQTPrice2 to heighestPrice
    }
  }
  if (TQTNumber3!="0"){
    if (TQTPrice3>heighestPrice){
      assign TQTNumber3 to heighestTST
      assign TQTPrice3 to heighestPrice
    }
  }
  if (TQTNumber4!="0"){
    if (TQTPrice4>heighestPrice){
      assign TQTNumber4 to heighestTST
      assign TQTPrice4 to heighestPrice
    }
  }
  if (TQTNumber5!="0"){
    if (TQTPrice5>heighestPrice){
      assign TQTNumber5 to heighestTST
      assign TQTPrice5 to heighestPrice
    }
  }
  if (TQTNumber6!="0"){
    if (TQTPrice6>heighestPrice){
      assign TQTNumber6 to heighestTST
      assign TQTPrice6 to heighestPrice
    }
  }
  if (TQTNumber7!="0"){
    if (TQTPrice7>heighestPrice){
      assign TQTNumber7 to heighestTST
      assign TQTPrice7 to heighestPrice
    }
  }
  if (TQTNumber8!="0"){
    if (TQTPrice8>heighestPrice){
      assign TQTNumber8 to heighestTST
      assign TQTPrice8 to heighestPrice
    }
  }
  if (TQTNumber9!="0"){
    if (TQTPrice9>heighestPrice){
      assign TQTNumber9 to heighestTST
      assign TQTPrice9 to heighestPrice
    }
  }
  if (TQTNumber10!="0"){
    if (TQTPrice10>heighestPrice){
      assign TQTNumber10 to heighestTST
      assign TQTPrice10 to heighestPrice
    }
  }
  if (TQTNumber11!="0"){
    if (TQTPrice11>heighestPrice){
      assign TQTNumber11 to heighestTST
      assign TQTPrice11 to heighestPrice
    }
  }
  if (TQTNumber12!="0"){
    if (TQTPrice12>heighestPrice){
      assign TQTNumber12 to heighestTST
      assign TQTPrice12 to heighestPrice
    }
  }
  if (TQTNumber13!="0"){
    if (TQTPrice13>heighestPrice){
      assign TQTNumber13 to heighestTST
      assign TQTPrice13 to heighestPrice
    }
  }
  if (TQTNumber14!="0"){
    if (TQTPrice14>heighestPrice){
      assign TQTNumber14 to heighestTST
      assign TQTPrice14 to heighestPrice
    }
  }
  if (TQTNumber15!="0"){
    if (TQTPrice15>heighestPrice){
      assign TQTNumber15 to heighestTST
      assign TQTPrice15 to heighestPrice
    }
  }
  if (TQTNumber16!="0"){
    if (TQTPrice16>heighestPrice){
      assign TQTNumber16 to heighestTST
      assign TQTPrice16 to heighestPrice
    }
  }
  if (TQTNumber17!="0"){
    if (TQTPrice17>heighestPrice){
      assign TQTNumber17 to heighestTST
      assign TQTPrice17 to heighestPrice
    }
  }
  if (TQTNumber18!="0"){
    if (TQTPrice18>heighestPrice){
      assign TQTNumber18 to heighestTST
      assign TQTPrice18 to heighestPrice
    }
  }

  send "TQT/T" +heighestTST

  capture line:5, column:32, length:2 assign to TQTOK1
  capture line:6, column:32, length:2 assign to TQTOK2
  capture line:7, column:32, length:2 assign to TQTOK3
  capture line:8, column:32, length:2 assign to TQTOK4
  capture line:9, column:32, length:2 assign to TQTOK5
  capture line:10, column:32, length:2 assign to TQTOK6
  capture line:11, column:32, length:2 assign to TQTOK7
  capture line:12, column:32, length:2 assign to TQTOK8
  capture line:13, column:32, length:2 assign to TQTOK9
  capture line:14, column:32, length:2 assign to TQTOK10
  capture line:15, column:32, length:2 assign to TQTOK11
  capture line:16, column:32, length:2 assign to TQTOK12
  capture line:17, column:32, length:2 assign to TQTOK13
  capture line:18, column:32, length:2 assign to TQTOK14
  capture line:19, column:32, length:2 assign to TQTOK15

  assign "0" to TQTSegmentNo
  if (TQTOK1=="OK"){
    capture line:5, column:62, length:2 assign to Bg1
    assign "1" to TQTSegmentNo
  }
  if (TQTOK2=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:6, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    else{
      capture line:6, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
  }
  if (TQTOK3=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:7, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:7, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:7, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
  }
  if (TQTOK4=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:8, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:8, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:8, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:8, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
  }
  if (TQTOK5=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:9, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:9, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:9, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:9, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:9, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
  }
  if (TQTOK6=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:10, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:10, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:10, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:10, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:10, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:10, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK7=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:11, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:11, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:11, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:11, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:11, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:11, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK8=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:12, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:12, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:12, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:12, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:12, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:12, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK9=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:13, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:13, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:13, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:13, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:13, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:13, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK10=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:14, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:14, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:14, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:14, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:14, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:14, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK11=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:15, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:15, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:15, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:15, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:15, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:15, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK12=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:16, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:16, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:16, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:16, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:16, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:16, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK13=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:17, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:17, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:17, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:17, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:17, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:17, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK14=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:18, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:18, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:18, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:18, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:18, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:18, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK15=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:19, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:19, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
      capture line:19, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:19, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
      capture line:19, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
      capture line:19, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }

if (Bg1 =="  "){
    assign "0p" to Bg1
}
if (Bg1 =="NO"){
    assign "0p" to Bg1
}

if (Bg2 =="  "){
    assign "0p" to Bg2
}
if (Bg2 =="NO"){
    assign "0p" to Bg2
}

if (Bg3 =="  "){
    assign "0p" to Bg3
}
if (Bg3 =="NO"){
    assign "0p" to Bg3
}

if (Bg4 =="  "){
    assign "0p" to Bg4
}
if (Bg4 =="NO"){
    assign "0p" to Bg4
}

if (Bg5 =="  "){
    assign "0p" to Bg5
}
if (Bg5 =="NO"){
    assign "0p" to Bg5
}

if (Bg6 =="  "){
    assign "0p" to Bg6
}
if (Bg6 =="NO"){
    assign "0p" to Bg6
}



send "tqt/t500"
  capture line:1, column:1, length:2 assign to testTST
    
  capture line:2, column:35, length:3 assign to firstCurr
  capture line:2, column:41, length:10 assign to firstTSTPrice
  capture line:3, column:35, length:3 assign to secondCurr
  capture line:3, column:41, length:10 assign to secondTSTPrice
  capture line:4, column:35, length:3 assign to thirdCurr
  capture line:4, column:41, length:10 assign to thirdTSTPrice
  capture line:5, column:35, length:3 assign to fourthCurr
  capture line:5, column:41, length:10 assign to fourthTSTPrice
  capture line:6, column:35, length:3 assign to fifthCurr
  capture line:6, column:41, length:10 assign to fifthTSTPrice
  capture line:7, column:35, length:3 assign to sixthCurr
  capture line:7, column:41, length:10 assign to sixthTSTPrice
  capture line:8, column:35, length:3 assign to seventhCurr
  capture line:8, column:41, length:10 assign to seventhTSTPrice
  capture line:9, column:35, length:3 assign to eighthCurr
  capture line:9, column:41, length:10 assign to eighthTSTPrice
  capture line:10, column:35, length:3 assign to ninthCurr
  capture line:10, column:41, length:10 assign to ninthTSTPrice
    
  if (testTST != "T "){
    send "There're no TST"
    mandatory ask "Continue?" assign to qz5
  }
  if (ninthCurr == firstCurr){
    send "df" +ninthTSTPrice +";" +eighthTSTPrice +";" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
  if (eighthCurr == firstCurr){
      send "df"  +eighthTSTPrice +";" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (seventhCurr == firstCurr){
       send "df" +seventhTSTPrice +";" +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (sixthCurr == firstCurr){
      send "df"   +sixthTSTPrice +";" +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (fifthCurr == firstCurr){
        send "df"   +fifthTSTPrice +";" +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (fourthCurr == firstCurr){
        send "df"   +fourthTSTPrice +";" +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (thirdCurr == firstCurr){
          send "df"   +thirdTSTPrice +";" +secondTSTPrice +";" +firstTSTPrice
}
else{
if (secondCurr == firstCurr){
          send "df"   +secondTSTPrice +";" +firstTSTPrice
}
else{
  send "df"   +firstTSTPrice
}//1
}//2
}//3
}//4
}//5
}//6
}//7
}//8
capture line:2, column:1, length:10 assign to totalOldTSTPrice

send "FXB/K/R,UP"
capture line:1, column:1, length:8 assign to checkAttn
if (checkAttn=="**ATTN**"){
    mandatory ask "There's unavailable class(es)!" assign to qz5
}

capture line:6, column:20, length:6 assign to totals6
capture line:7, column:20, length:6 assign to totals7
capture line:8, column:20, length:6 assign to totals8
capture line:9, column:20, length:6 assign to totals9
capture line:10, column:20, length:6 assign to totals10
capture line:11, column:20, length:6 assign to totals11
capture line:12, column:20, length:6 assign to totals12
capture line:13, column:20, length:6 assign to totals13
capture line:14, column:20, length:6 assign to totals14
capture line:15, column:20, length:6 assign to totals15
capture line:16, column:20, length:6 assign to totals16

if (totals6=="TOTALS"){
     capture line:6, column:51, length:10 assign to totalNewPrice
}
if (totals7=="TOTALS"){
     capture line:7, column:51, length:10 assign to totalNewPrice
}
if (totals8=="TOTALS"){
     capture line:8, column:51, length:10 assign to totalNewPrice
}
if (totals9=="TOTALS"){
     capture line:9, column:51, length:10 assign to totalNewPrice     
}
if (totals10=="TOTALS"){
     capture line:10, column:51, length:10 assign to totalNewPrice
}
if (totals11=="TOTALS"){
     capture line:11, column:51, length:10 assign to totalNewPrice
}
if (totals12=="TOTALS"){
     capture line:12, column:51, length:10 assign to totalNewPrice
}
if (totals13=="TOTALS"){
     capture line:13, column:51, length:10 assign to totalNewPrice
}
if (totals14=="TOTALS"){
     capture line:14, column:51, length:10 assign to totalNewPrice
}
if (totals15=="TOTALS"){
     capture line:15, column:51, length:10 assign to totalNewPrice
}
if (totals16=="TOTALS"){
     capture line:16, column:51, length:10 assign to totalNewPrice
}
     
     if (PassengerCount=="1"){
          capture line:6, column:1, length:3 assign to checknewCurr6
          capture line:7, column:1, length:3 assign to checknewCurr7
          capture line:8, column:1, length:3 assign to checknewCurr8
          capture line:9, column:1, length:3 assign to checknewCurr9
          capture line:10, column:1, length:3 assign to checknewCurr10
          capture line:11, column:1, length:3 assign to checknewCurr11
          capture line:12, column:1, length:3 assign to checknewCurr12
          capture line:13, column:1, length:3 assign to checknewCurr13
          capture line:14, column:1, length:3 assign to checknewCurr14
          capture line:15, column:1, length:3 assign to checknewCurr15
          capture line:16, column:1, length:3 assign to checknewCurr16
          capture line:17, column:1, length:3 assign to checknewCurr17
          capture line:18, column:1, length:3 assign to checknewCurr18
          capture line:19, column:1, length:3 assign to checknewCurr19
          capture line:20, column:1, length:3 assign to checknewCurr20
          capture line:21, column:1, length:3 assign to checknewCurr21
          capture line:22, column:1, length:3 assign to checknewCurr22
          capture line:23, column:1, length:3 assign to checknewCurr23

          if (checknewCurr6 == "USD"){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == "USD"){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == "USD"){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == "USD"){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == "USD"){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == "USD"){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == "USD"){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == "USD"){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == "USD"){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == "USD"){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == "USD"){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == "USD"){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == "USD"){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == "USD"){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == "USD"){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == "USD"){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == "USD"){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == "USD"){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }

            

send "fqq1"


      assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
        send "FXB/K/R,UP/SBF"
capture line:1, column:1, length:8 assign to checkAttn
if (checkAttn=="**ATTN**"){
    mandatory ask "There's unavailable class(es)!" assign to qz5
}

capture line:6, column:20, length:6 assign to totals6
capture line:7, column:20, length:6 assign to totals7
capture line:8, column:20, length:6 assign to totals8
capture line:9, column:20, length:6 assign to totals9
capture line:10, column:20, length:6 assign to totals10
capture line:11, column:20, length:6 assign to totals11
capture line:12, column:20, length:6 assign to totals12
capture line:13, column:20, length:6 assign to totals13
capture line:14, column:20, length:6 assign to totals14
capture line:15, column:20, length:6 assign to totals15
capture line:16, column:20, length:6 assign to totals16

if (totals6=="TOTALS"){
     capture line:6, column:51, length:10 assign to totalNewPrice
}
if (totals7=="TOTALS"){
     capture line:7, column:51, length:10 assign to totalNewPrice
}
if (totals8=="TOTALS"){
     capture line:8, column:51, length:10 assign to totalNewPrice
}
if (totals9=="TOTALS"){
     capture line:9, column:51, length:10 assign to totalNewPrice     
}
if (totals10=="TOTALS"){
     capture line:10, column:51, length:10 assign to totalNewPrice
}
if (totals11=="TOTALS"){
     capture line:11, column:51, length:10 assign to totalNewPrice
}
if (totals12=="TOTALS"){
     capture line:12, column:51, length:10 assign to totalNewPrice
}
if (totals13=="TOTALS"){
     capture line:13, column:51, length:10 assign to totalNewPrice
}
if (totals14=="TOTALS"){
     capture line:14, column:51, length:10 assign to totalNewPrice
}
if (totals15=="TOTALS"){
     capture line:15, column:51, length:10 assign to totalNewPrice
}
if (totals16=="TOTALS"){
     capture line:16, column:51, length:10 assign to totalNewPrice
}
     
     if (PassengerCount=="1"){
          capture line:6, column:1, length:3 assign to checknewCurr6
          capture line:7, column:1, length:3 assign to checknewCurr7
          capture line:8, column:1, length:3 assign to checknewCurr8
          capture line:9, column:1, length:3 assign to checknewCurr9
          capture line:10, column:1, length:3 assign to checknewCurr10
          capture line:11, column:1, length:3 assign to checknewCurr11
          capture line:12, column:1, length:3 assign to checknewCurr12
          capture line:13, column:1, length:3 assign to checknewCurr13
          capture line:14, column:1, length:3 assign to checknewCurr14
          capture line:15, column:1, length:3 assign to checknewCurr15
          capture line:16, column:1, length:3 assign to checknewCurr16
          capture line:17, column:1, length:3 assign to checknewCurr17
          capture line:18, column:1, length:3 assign to checknewCurr18
          capture line:19, column:1, length:3 assign to checknewCurr19
          capture line:20, column:1, length:3 assign to checknewCurr20
          capture line:21, column:1, length:3 assign to checknewCurr21
          capture line:22, column:1, length:3 assign to checknewCurr22
          capture line:23, column:1, length:3 assign to checknewCurr23

          if (checknewCurr6 == "USD"){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == "USD"){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == "USD"){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == "USD"){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == "USD"){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == "USD"){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == "USD"){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == "USD"){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == "USD"){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == "USD"){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == "USD"){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == "USD"){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == "USD"){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == "USD"){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == "USD"){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == "USD"){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == "USD"){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == "USD"){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }

            

send "fqq1"


      assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
      send "" +baggageCheckerStatment + " Segment(s)"
      ask "Continue with FXP?" assign to qz5
      send "FXP/R,UP"
      assign "1" to fxp_TST
      choose "Have got the requied TST?" until "Yes"{
          when ("No"){
            ask "Please Enter the TST NO:" assign to fxp_TST_NO
            send "FQQ" + fxp_TST_NO
          }
      }
      send "tte/all"
          send "fxr/k/R,UP"
        send "fxp/R,UP"
group{
       mandatory ask "ENTER the Adult TST line ( Please take 01 insstead of 1" assign to TST1
       ask "ENTER the Child TST line" assign to TST2
       ask "ENTER the Infant TST line" assign to TST3
}
// first line:
capture line:3, column:1, length:2 assign to TSTLine1
if (TSTLine1==TST1){
    capture line:3, column:28, length:8 assign to PaxCount1
}
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:8 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:8 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:8 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:8 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:8 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:8 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:8 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:8 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:8 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:8 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:8 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:8 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:8 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:8 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:8 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:8 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:8 assign to PaxCount3
      }
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}

    }
    }

send "FM5"


    assign "0" to first_TST
    assign "0" to second_TST
    assign "0" to third_TST
    assign "0" to fourth_TST
    assign "0" to fifth_TST
    assign "0" to sixth_TST
    assign "0" to seventh_TST
    assign "0" to eighth_TST
    assign "0" to ninth_TST

send "TQT/T500"

capture line:2, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:2, column:1, length:2 assign to first_TST
}
capture line:3, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:3, column:1, length:2 assign to second_TST
}
capture line:4, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:4, column:1, length:2 assign to third_TST
}
capture line:5, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:5, column:1, length:2 assign to fourth_TST
}
capture line:6, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:6, column:1, length:2 assign to fifth_TST
}
capture line:7, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:7, column:1, length:2 assign to sixth_TST
}
capture line:8, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:8, column:1, length:2 assign to seventh_TST
}
capture line:9, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:9, column:1, length:2 assign to eighth_TST
}
capture line:10, column:35, length:3 assign to USD_Currency
if (USD_Currency=="USD"){
    capture line:10, column:1, length:2 assign to ninth_TST
}

    assign "0" to fisrt_TQT_FM
    assign "0" to second_TQT_FM
    assign "0" to third_TQT_FM
    assign "0" to fourth_TQT_FM
    assign "0" to fifth_TQT_FM
    assign "0" to sixth_TQT_FM
    assign "0" to seventh_TQT_FM
    assign "0" to eighth_TQT_FM
    assign "0" to ninth_TQT_FM

if (first_TST != "0"){
    send "TQT/T" +first_TST +"/FM"
    capture line:7, column:28, length:6 assign to fisrt_TQT_FM
}
if (second_TST != "0"){
    send "TQT/T" +second_TST +"/FM"
    capture line:7, column:28, length:6 assign to second_TQT_FM
}
if (third_TST != "0"){
    send "TQT/T" +third_TST +"/FM"
    capture line:7, column:28, length:6 assign to third_TQT_FM
}
if (fourth_TST != "0"){
    send "TQT/T" +fourth_TST +"/FM"
    capture line:7, column:28, length:6 assign to fourth_TQT_FM
}
if (fifth_TST != "0"){
    send "TQT/T" +fifth_TST +"/FM"
    capture line:7, column:28, length:6 assign to fifth_TQT_FM
}
if (sixth_TST != "0"){
    send "TQT/T" +sixth_TST +"/FM"
    capture line:7, column:28, length:6 assign to sixth_TQT_FM
}   
if (seventh_TST != "0"){
    send "TQT/T" +seventh_TST +"/FM"
    capture line:7, column:28, length:6 assign to seventh_TQT_FM
}
if (eighth_TST != "0"){
    send "TQT/T" +eighth_TST +"/FM"
    capture line:7, column:28, length:6 assign to eighth_TQT_FM
}
if (ninth_TST != "0"){
    send "TQT/T" +ninth_TST +"/FM"
    capture line:7, column:28, length:6 assign to ninth_TQT_FM
}

send "DF" +fisrt_TQT_FM +";" +second_TQT_FM +";" +third_TQT_FM +";" +fourth_TQT_FM 
+";" +fifth_TQT_FM +";" +sixth_TQT_FM +";" +seventh_TQT_FM +";" +eighth_TQT_FM +";" +ninth_TQT_FM

capture line:2, column:1, length:10 assign to totalNewPrice
capture line:6, column:1, length:1 assign to dfnextcheck
if (dfnextcheck == ">"){
    capture line:4, column:1, length:10 assign to totalNewPrice
}
capture line:5, column:1, length:1 assign to dfnextcheck
if (dfnextcheck == ">"){
    capture line:3, column:1, length:10 assign to totalNewPrice
}
capture line:4, column:1, length:1 assign to dfnextcheck
if (dfnextcheck == ">"){
    capture line:2, column:1, length:10 assign to totalNewPrice
}



    send "FQC" +totalNewPrice +"USD/AED"
    capture line:5, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:2 assign to totalNewPrice
    }
    capture line:5, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:3 assign to totalNewPrice
    }
    capture line:5, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:4 assign to totalNewPrice
    }
    capture line:5, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:5 assign to totalNewPrice
    }
    capture line:5, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:6 assign to totalNewPrice
    }
    capture line:5, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:7 assign to totalNewPrice
    }
    capture line:5, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:8 assign to totalNewPrice
    }
    capture line:5, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:9 assign to totalNewPrice
    }
    capture line:5, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:10 assign to totalNewPrice
    }
    capture line:5, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:11 assign to totalNewPrice
    }
    capture line:5, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:12 assign to totalNewPrice
    }
    
    send "FQC" +totalNewPrice +"AED/" +firstCurr
    capture line:5, column:7, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:2 assign to totalNewPrice
    }
    capture line:5, column:8, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:3 assign to totalNewPrice
    }
    capture line:5, column:9, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:4 assign to totalNewPrice
    }
    capture line:5, column:10, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:5 assign to totalNewPrice
    }
    capture line:5, column:11, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:6 assign to totalNewPrice
    }
    capture line:5, column:12, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:7 assign to totalNewPrice
    }
    capture line:5, column:13, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:8 assign to totalNewPrice
    }
    capture line:5, column:14, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:9 assign to totalNewPrice
    }
    capture line:5, column:15, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:10 assign to totalNewPrice
    }
    capture line:5, column:16, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:11 assign to totalNewPrice
    }
    capture line:5, column:17, length:1 assign to check_AED_Final
    if (check_AED_Final == "-"){
        capture line:5, column:5, length:12 assign to totalNewPrice
    }


    send "df" +totalOldTSTPrice +"-" +totalNewPrice

    choose "Do you want to continue?" until "Yes"{
        when ("No"){
        }
    }

    send "IR"
    send "IR"
    send "TTE/All"
    send "FXB/K/R,UP"
capture line:1, column:1, length:8 assign to checkAttn
if (checkAttn=="**ATTN**"){
    mandatory ask "There's unavailable class(es)!" assign to qz5
}

capture line:6, column:20, length:6 assign to totals6
capture line:7, column:20, length:6 assign to totals7
capture line:8, column:20, length:6 assign to totals8
capture line:9, column:20, length:6 assign to totals9
capture line:10, column:20, length:6 assign to totals10
capture line:11, column:20, length:6 assign to totals11
capture line:12, column:20, length:6 assign to totals12
capture line:13, column:20, length:6 assign to totals13
capture line:14, column:20, length:6 assign to totals14
capture line:15, column:20, length:6 assign to totals15
capture line:16, column:20, length:6 assign to totals16

if (totals6=="TOTALS"){
     capture line:6, column:51, length:10 assign to totalNewPrice
}
if (totals7=="TOTALS"){
     capture line:7, column:51, length:10 assign to totalNewPrice
}
if (totals8=="TOTALS"){
     capture line:8, column:51, length:10 assign to totalNewPrice
}
if (totals9=="TOTALS"){
     capture line:9, column:51, length:10 assign to totalNewPrice     
}
if (totals10=="TOTALS"){
     capture line:10, column:51, length:10 assign to totalNewPrice
}
if (totals11=="TOTALS"){
     capture line:11, column:51, length:10 assign to totalNewPrice
}
if (totals12=="TOTALS"){
     capture line:12, column:51, length:10 assign to totalNewPrice
}
if (totals13=="TOTALS"){
     capture line:13, column:51, length:10 assign to totalNewPrice
}
if (totals14=="TOTALS"){
     capture line:14, column:51, length:10 assign to totalNewPrice
}
if (totals15=="TOTALS"){
     capture line:15, column:51, length:10 assign to totalNewPrice
}
if (totals16=="TOTALS"){
     capture line:16, column:51, length:10 assign to totalNewPrice
}
     
     if (PassengerCount=="1"){
          capture line:6, column:1, length:3 assign to checknewCurr6
          capture line:7, column:1, length:3 assign to checknewCurr7
          capture line:8, column:1, length:3 assign to checknewCurr8
          capture line:9, column:1, length:3 assign to checknewCurr9
          capture line:10, column:1, length:3 assign to checknewCurr10
          capture line:11, column:1, length:3 assign to checknewCurr11
          capture line:12, column:1, length:3 assign to checknewCurr12
          capture line:13, column:1, length:3 assign to checknewCurr13
          capture line:14, column:1, length:3 assign to checknewCurr14
          capture line:15, column:1, length:3 assign to checknewCurr15
          capture line:16, column:1, length:3 assign to checknewCurr16
          capture line:17, column:1, length:3 assign to checknewCurr17
          capture line:18, column:1, length:3 assign to checknewCurr18
          capture line:19, column:1, length:3 assign to checknewCurr19
          capture line:20, column:1, length:3 assign to checknewCurr20
          capture line:21, column:1, length:3 assign to checknewCurr21
          capture line:22, column:1, length:3 assign to checknewCurr22
          capture line:23, column:1, length:3 assign to checknewCurr23

          if (checknewCurr6 == "USD"){
               capture line:6, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr7 == "USD"){
               capture line:7, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr8 == "USD"){
               capture line:8, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr9 == "USD"){
               capture line:9, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr10 == "USD"){
               capture line:10, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr11 == "USD"){
               capture line:11, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr12 == "USD"){
               capture line:12, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr13 == "USD"){
               capture line:13, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr14 == "USD"){
               capture line:14, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr15 == "USD"){
               capture line:15, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr16 == "USD"){
               capture line:16, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr17 == "USD"){
               capture line:17, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr18 == "USD"){
               capture line:18, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr19 == "USD"){
               capture line:19, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr20 == "USD"){
               capture line:20, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr21 == "USD"){
               capture line:21, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr22 == "USD"){
               capture line:22, column:4, length:10 assign to totalNewPrice
          }
          if (checknewCurr23 == "USD"){
               capture line:23, column:4, length:10 assign to totalNewPrice
          }
     }

            

send "fqq1"


      assign "True" to BaggageChecker1
    assign "True" to BaggageChecker2
    assign "True" to BaggageChecker3
    assign "True" to BaggageChecker4
    assign "True" to BaggageChecker5
    assign "True" to BaggageChecker6

capture line:6, column:59, length:2 assign to baggage1
    if (baggage1=="BG"){
            capture line:8, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){
              assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:9, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:9, column:59, length:2 assign to fBg2
            capture line:10, column:59, length:2 assign to fBg3
            capture line:11, column:59, length:2 assign to fBg4
            capture line:12, column:59, length:2 assign to fBg5
            capture line:13, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
       
    }

    capture line:7, column:59, length:2 assign to baggage2
    if (baggage2=="BG"){
        capture line:9, column:59, length:2 assign to fBg1
            if (fBg1 != Bg1){ 
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:10, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:10, column:59, length:2 assign to fBg2
            capture line:11, column:59, length:2 assign to fBg3
            capture line:12, column:59, length:2 assign to fBg4
            capture line:13, column:59, length:2 assign to fBg5
            capture line:14, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

    capture line:8, column:59, length:2 assign to baggage3
    if (baggage3=="BG"){
            capture line:10, column:59, length:2 assign to fBg1
            if (fBg1 !=Bg1){
                assign "False" to BaggageChecker1
            }
        if (segmentsCount=="2"){
            capture line:11, column:59, length:2 assign to fBg2
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
        }
        if (segmentsCount=="3"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
        }
        if (segmentsCount=="4"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
        }
        if (segmentsCount=="5"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
        }
        if (segmentsCount=="6"){
            capture line:11, column:59, length:2 assign to fBg2
            capture line:12, column:59, length:2 assign to fBg3
            capture line:13, column:59, length:2 assign to fBg4
            capture line:14, column:59, length:2 assign to fBg5
            capture line:15, column:59, length:2 assign to fBg6
            if (fBg2 !=Bg2){
                assign "False" to BaggageChecker2
            }
            if (fBg3 !=Bg3){
                assign "False" to BaggageChecker3
            }
            if (fBg4 !=Bg4){
                assign "False" to BaggageChecker4
            }
            if (fBg5 !=Bg5){
                assign "False" to BaggageChecker5
            }
            if (fBg6!=Bg6){
                assign "False" to BaggageChecker6
            }
        }
    }

assign "Please check the baggage in: " to baggageCheckerStatment
      if (BaggageChecker1 == "False"){
      append "-1st-" to baggageCheckerStatment
    }
    if (BaggageChecker2 == "False"){
      append "-2nd-" to baggageCheckerStatment
    }
    if (BaggageChecker3 == "False"){
      append "-3rd-" to baggageCheckerStatment
    }
    if (BaggageChecker4 == "False"){
      append "-4th-" to baggageCheckerStatment
    }
    if (BaggageChecker5 == "False"){
      append "-5th-" to baggageCheckerStatment
    }
    if (BaggageChecker6 == "False"){
      append "-6th-" to baggageCheckerStatment
    }
    
    if (baggageCheckerStatment != "Please check the baggage in: "){
      send "" +baggageCheckerStatment + " Segment(s)"
      ask "Continue with FXP?" assign to qz5
      send "FXP/R,UP"
      assign "1" to fxp_TST
      choose "Have got the requied TST?" until "Yes"{
          when ("No"){
            ask "Please Enter the TST NO:" assign to fxp_TST_NO
            send "FQQ" + fxp_TST_NO
          }
      }
      send "tte/all"
          send "fxr/k/R,UP"
        send "fxp/R,UP"
group{
       mandatory ask "ENTER the Adult TST line ( Please take 01 insstead of 1" assign to TST1
       ask "ENTER the Child TST line" assign to TST2
       ask "ENTER the Infant TST line" assign to TST3
}
// first line:
capture line:3, column:1, length:2 assign to TSTLine1
if (TSTLine1==TST1){
    capture line:3, column:28, length:8 assign to PaxCount1
}
  capture line:4, column:1, length:2 assign to TSTLine2
  if (TSTLine2==TST1){
      capture line:4, column:28, length:8 assign to PaxCount1
  }
  capture line:5, column:1, length:2 assign to TSTLine3
  if (TSTLine3==TST1){
      capture line:5, column:28, length:8 assign to PaxCount1
  }
  capture line:6, column:1, length:2 assign to TSTLine4
  if (TSTLine4==TST1){
      capture line:6, column:28, length:8 assign to PaxCount1
  }
  capture line:7, column:1, length:2 assign to TSTLine5
  if (TSTLine5==TST1){
      capture line:7, column:28, length:8 assign to PaxCount1
  }
  capture line:8, column:1, length:2 assign to TSTLine6
  if (TSTLine6==TST1){
      capture line:8, column:28, length:8 assign to PaxCount1
  }
  capture line:9, column:1, length:2 assign to TSTLine7
  if (TSTLine7==TST1){
      capture line:9, column:28, length:8 assign to PaxCount1
  }
  capture line:10, column:1, length:2 assign to TSTLine8
  if (TSTLine8==TST1){
      capture line:10, column:28, length:8 assign to PaxCount1
  }
  capture line:11, column:1, length:2 assign to TSTLine9
  if (TSTLine9==TST1){
      capture line:11, column:28, length:8 assign to PaxCount1
  }
  capture line:12, column:1, length:2 assign to TSTLine10
  if (TSTLine10==TST1){
      capture line:12, column:28, length:8 assign to PaxCount1
  }
  capture line:13, column:1, length:2 assign to TSTLine11
  if (TSTLine11==TST1){
      capture line:13, column:28, length:8 assign to PaxCount1
  }
  capture line:14, column:1, length:2 assign to TSTLine12
  if (TSTLine12==TST1){
      capture line:14, column:28, length:8 assign to PaxCount1
  }
  capture line:15, column:1, length:2 assign to TSTLine13
  if (TSTLine13==TST1){
      capture line:15, column:28, length:8 assign to PaxCount1
  }
  capture line:16, column:1, length:2 assign to TSTLine14
  if (TSTLine14==TST1){
      capture line:16, column:28, length:8 assign to PaxCount1
  }
  capture line:17, column:1, length:2 assign to TSTLine15
  if (TSTLine15==TST1){
      capture line:17, column:28, length:8 assign to PaxCount1
  }
  capture line:18, column:1, length:2 assign to TSTLine16
  if (TSTLine16==TST1){
      capture line:18, column:28, length:8 assign to PaxCount1
  }

  // second line:
    if (TSTLine1==TST2){
        capture line:3, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine2==TST2){
        capture line:4, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine3==TST2){
        capture line:5, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine4==TST2){
        capture line:6, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine5==TST2){
        capture line:7, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine6==TST2){
        capture line:8, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine7==TST2){
        capture line:9, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine8==TST2){
        capture line:10, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine9==TST2){
        capture line:11, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine10==TST2){
        capture line:12, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine11==TST2){
        capture line:13, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine12==TST2){
        capture line:14, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine13==TST2){
        capture line:15, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine14==TST2){
        capture line:16, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine15==TST2){
        capture line:17, column:28, length:8 assign to PaxCount2
    }
    if (TSTLine16==TST2){
        capture line:18, column:28, length:8 assign to PaxCount2
    }
      // third line:
      if (TSTLine1==TST3){
        capture line:3, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine2==TST3){
        capture line:4, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine3==TST3){
        capture line:5, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine4==TST3){
        capture line:6, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine5==TST3){
        capture line:7, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine6==TST3){
        capture line:8, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine7==TST3){
        capture line:9, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine8==TST3){
        capture line:10, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine9==TST3){
        capture line:11, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine10==TST3){
        capture line:12, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine11==TST3){
        capture line:13, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine12==TST3){
        capture line:14, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine13==TST3){
        capture line:15, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine14==TST3){
        capture line:16, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine15==TST3){
        capture line:17, column:28, length:8 assign to PaxCount3
      }
      if (TSTLine16==TST3){
        capture line:18, column:28, length:8 assign to PaxCount3
      }
    
// No Infant
if (TST3 ==""){
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST2 +"/" +PaxCount2
  }
}
else {
  // No Child
  if (TST2 ==""){
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  else{
      send "FXT" +TST1 +"/" +PaxCount1
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST2 +"/" +PaxCount2
      send "fxr/k/R,UP"
      send "FXP/R,UP"
      send "FXT" +TST3 +"/" +PaxCount3
  }
  
}

    }

call "z_FM_DEL"

send "FM5"
call "z_FOPCASH_DEL" 
send "PDY"
send "PT*1"        
call "z_RTTN_DEL"
    
    send "RF" +agtName +";ER"
    send "er"
                    
send "ttp/rt"

capture line:1, column:1, length:36 assign to checkAfterTTP
if (checkAfterTTP== "GTW/ETS: UNABLE TO PROCESS - TIMEOUT"){
  send "TTP/RT"
}


call "z_Name Sorter"
ask "ok?" assign to qz5

call "IAH_KU"
