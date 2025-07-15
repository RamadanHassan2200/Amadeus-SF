choose "<h2><font size=\"4\"><h2><font color=\"BLUE\">What Quote do you want to check?<h2><font size=\"3\"><p><font color=\"RED\"><br> For reissue, please make sure to add the new segments before proceeding!.</font></p></font></h2></font></h2></font></h2>"{
    when ("Reissue") {
        assign "Reissue" to quoteType
    }
    when ("Refund") {
        assign "Refund" to quoteType
    }
}
send "tqt/t500"

capture line:1, column:1, length:13 assign to TQT_Checker
if (TQT_Checker !="NO ACTIVE TST"){


capture line:2, column:75, length: 5 assign to old_segments_No

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

}else{
  send "TTH"
  mandator ask "Please enter the Same (Non INF) TTH Number as issued ticket... " with format "^\d{1,3}$" assign to heighestTST
}

  send "TTH/T" +heighestTST

assign "1" to faresCount
    // First Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis1_short
        capture line:1, column:6, length:1 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis1_short
        capture line:1, column:6, length:2 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis1_short
        capture line:1, column:6, length:3 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:4 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:5 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:6 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:7 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:8 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:9 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:10 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:11 assign to fareBasis1
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis1_short
        capture line:1, column:6, length:12 assign to fareBasis1
        append "1" to faresCount
      }
    }

    // Second Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1 != "BOTT"){
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis2_short
        capture line:1, column:6, length:1 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis2_short
        capture line:1, column:6, length:2 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis2_short
        capture line:1, column:6, length:3 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:4 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:5 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:6 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:7 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:8 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:9 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:10 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:11 assign to fareBasis2
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis2_short
        capture line:1, column:6, length:12 assign to fareBasis2
        append "1" to faresCount
      }
    }
    
    // Third Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1 != "BOTT"){
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis3_short
        capture line:1, column:6, length:1 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis3_short
        capture line:1, column:6, length:2 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis3_short
        capture line:1, column:6, length:3 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:4 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:5 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:6 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:7 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:8 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:9 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:10 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:11 assign to fareBasis3
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis3_short
        capture line:1, column:6, length:12 assign to fareBasis3
        append "1" to faresCount
      }
    }
    
    // Fourth Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1 != "BOTT"){
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis4_short
        capture line:1, column:6, length:1 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis4_short
        capture line:1, column:6, length:2 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis4_short
        capture line:1, column:6, length:3 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:4 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:5 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:6 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:7 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:8 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:9 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:10 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:11 assign to fareBasis4
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis4_short
        capture line:1, column:6, length:12 assign to fareBasis4
        append "1" to faresCount
      }
    }
    
    // Fifth Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1 != "BOTT"){
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis5_short
        capture line:1, column:6, length:1 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis5_short
        capture line:1, column:6, length:2 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis5_short
        capture line:1, column:6, length:3 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:4 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:5 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:6 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:7 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:8 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:9 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:10 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:11 assign to fareBasis5
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis5_short
        capture line:1, column:6, length:12 assign to fareBasis5
        append "1" to faresCount
      }
    }
    
    // Sixth Capture fareBasis
    send "MD-AB  "
    capture line:1, column:1, length:4 assign to AB1
    if (AB1 != "BOTT"){
    if (AB1=="AB  "){
      capture line:1, column:33, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:1 assign to fareBasis6_short
        capture line:1, column:6, length:1 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:34, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:2 assign to fareBasis6_short
        capture line:1, column:6, length:2 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:35, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:3 assign to fareBasis6_short
        capture line:1, column:6, length:3 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:36, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:4 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:37, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:5 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:38, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:6 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:39, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:7 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:40, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:8 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:41, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:9 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:42, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:10 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:43, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:11 assign to fareBasis6
        append "1" to faresCount
      }
      capture line:1, column:44, length:2 assign to OK
      if (OK=="OK"){
        capture line:1, column:6, length:4 assign to fareBasis6_short
        capture line:1, column:6, length:12 assign to fareBasis6
        append "1" to faresCount
      }
    }
    
    }//BOTT6

    }//BOTT5

    }//BOTT4

    }//BOTT3

    }//BOTT2


    send "TTH/T" +heighestTST

    // Baggage Checker
    send "MD-AA  "
    capture line:1, column:1, length:4 assign to AA1
    if (AA1=="AA  "){
      capture line:1, column:6, length:2 assign to Bg1
      capture line:1, column:14, length:13 assign to flight1
      capture line:1, column:22, length:5 assign to flight1_date
    }
    if (faresCount=="11"){
      capture line:1, column:1, length:4 assign to AA1
      if (AA1=="AA  "){
        capture line:1, column:6, length:2 assign to Bg2
        capture line:1, column:14, length:13 assign to flight2
        capture line:1, column:22, length:5 assign to flight2_date
      }
    }
    if (faresCount=="111"){
      capture line:1, column:1, length:4 assign to AA1
      if (AA1=="AA  "){
        capture line:1, column:6, length:2 assign to Bg3
        capture line:1, column:14, length:13 assign to flight3
        capture line:1, column:22, length:5 assign to flight3_date
      }
    }
    if (faresCount=="1111"){
      capture line:1, column:1, length:4 assign to AA1
      if (AA1=="AA  "){
        capture line:1, column:6, length:2 assign to Bg4
        capture line:1, column:14, length:13 assign to flight4
        capture line:1, column:22, length:5 assign to flight4_date
      }
    }
    if (faresCount=="11111"){
      capture line:1, column:1, length:4 assign to AA1
      if (AA1=="AA  "){
        capture line:1, column:6, length:2 assign to Bg5
        capture line:1, column:14, length:13 assign to flight5
        capture line:1, column:22, length:5 assign to flight5_date
      }
    }
    if (faresCount=="111111"){
      capture line:1, column:1, length:4 assign to AA1
      if (AA1=="AA  "){
        capture line:1, column:6, length:2 assign to Bg6
        capture line:1, column:14, length:13 assign to flight6
        capture line:1, column:22, length:5 assign to flight6_date
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


  // getting the issuing city and date of issue
  send "TTH/T" +heighestTST
  send "MD-RF-"

  capture line:1, column:5, length:2 assign to RF1
  if (RF1 == "RF"){
    capture line:1, column:15, length:3 assign to issuing_City
    capture line:1, column:35, length:5 assign to DOI
  }
  else{
    send "MD-RF-"
    capture line:1, column:5, length:2 assign to RF1
    if (RF1 == "RF"){
      capture line:1, column:15, length:3 assign to issuing_City
      capture line:1, column:35, length:5 assign to DOI
    }
  }

  send "FXX/R," +DOI +"," +issuing_City




if (quoteType=="Reissue"){
  

    
    
}
if (quoteType=="Refund"){
  send "RT"

   group {
    ask "Please enter the Old Segments Number(s)... " with format "^\d+\s*(?:[,-]\s*\d+)*$" assign to old_segments_No
    ask "Please enter the Used Segments Number(s)... " with format "^\d+\s*(?:[,-]\s*\d+)*$" assign to used_segments_No
  }

  if ()
  send "TQT/T" +heighestTST

  capture line:1, column:14, length:3 assign to issuing_City
  capture line:1, column:27, length:5 assign to DOI

    assign "" to fareBasis1
    assign "" to fareBasis2
    assign "" to fareBasis3
    assign "" to fareBasis4
    assign "" to fareBasis5
    assign "" to fareBasis6

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
    capture line:5, column:35, length:12 assign to fareBasis1
    capture line:5, column:62, length:2 assign to Bg1
    assign "1" to TQTSegmentNo
  }
  if (TQTOK2=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:6, column:35, length:12 assign to fareBasis1
      capture line:6, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    else{
      capture line:6, column:35, length:12 assign to fareBasis2
      capture line:6, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
  }
  if (TQTOK3=="OK"){
    if (TQTSegmentNo == "0"){
      capture line:7, column:35, length:12 assign to fareBasis1
      capture line:7, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:7, column:35, length:12 assign to fareBasis2
      capture line:7, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:7, column:35, length:12 assign to fareBasis3
      capture line:7, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
  }
  if (TQTOK4=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:8, column:35, length:12 assign to fareBasis1
      capture line:8, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:8, column:35, length:12 assign to fareBasis2
      capture line:8, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:8, column:35, length:12 assign to fareBasis3
      capture line:8, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
      capture line:8, column:35, length:12 assign to fareBasis4
      capture line:8, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
  }
  if (TQTOK5=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:9, column:35, length:12 assign to fareBasis1
      capture line:9, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
      capture line:9, column:35, length:12 assign to fareBasis2
      capture line:9, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:9, column:35, length:12 assign to fareBasis3
      capture line:9, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:9, column:35, length:12 assign to fareBasis4
      capture line:9, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:9, column:35, length:12 assign to fareBasis5
      capture line:9, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
  }
  if (TQTOK6=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:10, column:35, length:12 assign to fareBasis1
      capture line:10, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:10, column:35, length:12 assign to fareBasis2
      capture line:10, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:10, column:35, length:12 assign to fareBasis3
      capture line:10, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:10, column:35, length:12 assign to fareBasis4
      capture line:10, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:10, column:35, length:12 assign to fareBasis5
      capture line:10, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:10, column:35, length:12 assign to fareBasis6
      capture line:10, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK7=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:11, column:35, length:12 assign to fareBasis1
      capture line:11, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:11, column:35, length:12 assign to fareBasis2
      capture line:11, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:11, column:35, length:12 assign to fareBasis3
      capture line:11, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:11, column:35, length:12 assign to fareBasis4
      capture line:11, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:11, column:35, length:12 assign to fareBasis5
      capture line:11, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:11, column:35, length:12 assign to fareBasis6
      capture line:11, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK8=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:12, column:35, length:12 assign to fareBasis1
      capture line:12, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:12, column:35, length:12 assign to fareBasis2
      capture line:12, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:12, column:35, length:12 assign to fareBasis3
      capture line:12, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:12, column:35, length:12 assign to fareBasis4
      capture line:12, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:12, column:35, length:12 assign to fareBasis5
      capture line:12, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:12, column:35, length:12 assign to fareBasis6
      capture line:12, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK9=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:13, column:35, length:12 assign to fareBasis1
      capture line:13, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:13, column:35, length:12 assign to fareBasis2
      capture line:13, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:13, column:35, length:12 assign to fareBasis3
      capture line:13, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:13, column:35, length:12 assign to fareBasis4
      capture line:13, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:13, column:35, length:12 assign to fareBasis5
      capture line:13, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:13, column:35, length:12 assign to fareBasis6
      capture line:13, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK10=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:14, column:35, length:12 assign to fareBasis1
      capture line:14, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:14, column:35, length:12 assign to fareBasis2
      capture line:14, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:14, column:35, length:12 assign to fareBasis3
      capture line:14, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:14, column:35, length:12 assign to fareBasis4
      capture line:14, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:14, column:35, length:12 assign to fareBasis5
      capture line:14, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:14, column:35, length:12 assign to fareBasis6
      capture line:14, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK11=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:15, column:35, length:12 assign to fareBasis1
      capture line:15, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:15, column:35, length:12 assign to fareBasis2
      capture line:15, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:15, column:35, length:12 assign to fareBasis3
      capture line:15, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:15, column:35, length:12 assign to fareBasis4
      capture line:15, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:15, column:35, length:12 assign to fareBasis5
      capture line:15, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:15, column:35, length:12 assign to fareBasis6
      capture line:15, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK12=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:16, column:35, length:12 assign to fareBasis1
      capture line:16, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:16, column:35, length:12 assign to fareBasis2
      capture line:16, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:16, column:35, length:12 assign to fareBasis3
      capture line:16, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:16, column:35, length:12 assign to fareBasis4
      capture line:16, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:16, column:35, length:12 assign to fareBasis5
      capture line:16, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:16, column:35, length:12 assign to fareBasis6
      capture line:16, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK13=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:17, column:35, length:12 assign to fareBasis1
      capture line:17, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:17, column:35, length:12 assign to fareBasis2
      capture line:17, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:17, column:35, length:12 assign to fareBasis3
      capture line:17, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:17, column:35, length:12 assign to fareBasis4
      capture line:17, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:17, column:35, length:12 assign to fareBasis5
      capture line:17, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:17, column:35, length:12 assign to fareBasis6
      capture line:17, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK14=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:18, column:35, length:12 assign to fareBasis1
      capture line:18, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:18, column:35, length:12 assign to fareBasis2
      capture line:18, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:18, column:35, length:12 assign to fareBasis3
      capture line:18, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:18, column:35, length:12 assign to fareBasis4
      capture line:18, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:18, column:35, length:12 assign to fareBasis5
      capture line:18, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:18, column:35, length:12 assign to fareBasis6
      capture line:18, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }
  if (TQTOK15=="OK"){
    if (TQTSegmentNo == "0"){
        capture line:19, column:35, length:12 assign to fareBasis1
      capture line:19, column:62, length:2 assign to Bg1
      assign "1" to TQTSegmentNo
    }
    if (TQTSegmentNo == "1"){
        capture line:19, column:35, length:12 assign to fareBasis2
      capture line:19, column:62, length:2 assign to Bg2
      assign "2" to TQTSegmentNo
    }
    if (TQTSegmentNo == "2"){
        capture line:19, column:35, length:12 assign to fareBasis3
      capture line:19, column:62, length:2 assign to Bg3
      assign "3" to TQTSegmentNo
    }
    if (TQTSegmentNo == "3"){
        capture line:19, column:35, length:12 assign to fareBasis4
      capture line:19, column:62, length:2 assign to Bg4
      assign "4" to TQTSegmentNo
    }
    if (TQTSegmentNo == "4"){
        capture line:19, column:35, length:12 assign to fareBasis5
      capture line:19, column:62, length:2 assign to Bg5
      assign "5" to TQTSegmentNo
    }
    if (TQTSegmentNo == "5"){
        capture line:19, column:35, length:12 assign to fareBasis6
      capture line:19, column:62, length:2 assign to Bg6
      assign "6" to TQTSegmentNo
    }
  }



}