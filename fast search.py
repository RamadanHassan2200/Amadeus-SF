  // fast_search
  send "TTH/ALL"
  capture line:2, column:35, length:3 assign to currency
  capture line:2, column:42, length:9 assign to first_Amount

  send "FXR/K"
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
    assign "True" to starFound
  }
  if (secondSeg == "*"){
    assign "True" to starFound
  }
  if (thirdSeg == "*"){
    assign "True" to starFound
  }
  if (fourthSeg == "*"){
    assign "True" to starFound
  }
  if (fifthSeg == "*"){
    assign "True" to starFound
  }
  if (sixthSeg == "*"){
    assign "True" to starFound
  }
  if (seventhSeg == "*"){
    assign "True" to starFound
  }
  if (eighthSeg == "*"){
    assign "True" to starFound
  }
  if (currency != "KWD"){
  if (starFound == "True"){
    capture line:23, column:1, length:3 assign to SAR_Key
    capture line:23, column:4, length:9 assign to SAR_Amount
    if (SAR_Key != "SAR"){
      capture line:22, column:1, length:3 assign to SAR_Key
      capture line:22, column:4, length:9 assign to SAR_Amount
      if (SAR_Key != "SAR"){
        capture line:21, column:1, length:3 assign to SAR_Key
        capture line:21, column:4, length:9 assign to SAR_Amount
        if (SAR_Key != "SAR"){
          capture line:20, column:1, length:3 assign to SAR_Key
          capture line:20, column:4, length:9 assign to SAR_Amount
          if (SAR_Key != "SAR"){
            capture line:19, column:1, length:3 assign to SAR_Key
            capture line:19, column:4, length:9 assign to SAR_Amount
            if (SAR_Key != "SAR"){
              capture line:18, column:1, length:3 assign to SAR_Key
              capture line:18, column:4, length:9 assign to SAR_Amount
              if (SAR_Key != "SAR"){
                capture line:17, column:1, length:3 assign to SAR_Key
                capture line:17, column:4, length:9 assign to SAR_Amount
                if (SAR_Key != "SAR"){
                  capture line:17, column:1, length:3 assign to SAR_Key
                  capture line:17, column:4, length:9 assign to SAR_Amount
                }
              }
            }
          }
        }
      }
    }

    if (SAR_Amount >= first_Amount){
      assign "False" to starFound
    }
  }

  }

   send "ig"
  if (starFound == "True"){
      send "SRTSuccess"
  }
 

  