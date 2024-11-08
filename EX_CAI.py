capture line:1, column:1, length:22 assign to checkticketopenness
if (checkticketopenness=="SECURED ETKT RECORD(S)"){
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
    if (TQTSegmentNo == "1"){
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
}

//TEST
