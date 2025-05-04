// Step1- getting the PNR

Ask "Enter the PNR:" assign to PNR
send "RT" + PNR

assign "False" to dealchecker

//Step2 - checking the star
send "fxr/k"
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
    assign "True" to dealchecker
  }
  if (secondSeg == "*"){
    assign "True" to dealchecker
  }
  if (thirdSeg == "*"){
    assign "True" to dealchecker
  }
  if (fourthSeg == "*"){
    assign "True" to dealchecker
  }
  if (fifthSeg == "*"){
    assign "True" to dealchecker
  }
  if (sixthSeg == "*"){
    assign "True" to dealchecker
  }
  if (seventhSeg == "*"){
    assign "True" to dealchecker
  }
  if (eighthSeg == "*"){
    assign "True" to dealchecker
  }


//Step3- checking the deal if any

if (dealchecker == "True"){
    send "TQT/T500"
    capture line:1, column:72, length:8 assign to segments
    if (segments!="SEGMENTS"){
        assign "NO TST" to dealchecker
    }
    else{
        assign "1" to TSTcount
        capture line:2, column:1, length:3 assign to TSTNo1
        capture line:2, column:9, length:1 assign to Infcheck1
        capture line:2, column:38, length:13 assign to TSTPrice1
        capture line:2, column:75, length:5 assign to TSTSegments1

        assign TSTNo1 to HighestTST
        assign TSTPrice1 to HighestTSTPrice
        assign TSTSegments1 to FirstSegment
        assign "1" to Number_Of_Different_Segments

        capture line:4, column:1, length:1 assign to nextcheck
        if (nextcheck != "D"){
            assign "2" to TSTcount
            capture line:3, column:1, length:3 assign to TSTNo2
            capture line:3, column:9, length:1 assign to Infcheck2
            capture line:3, column:38, length:13 assign to TSTPrice2
            capture line:3, column:75, length:5 assign to TSTSegments2

            if (Infcheck2 != "I"){
                if (TSTPrice2 > HighestTSTPrice){
                    if (TSTSegments2==FirstSegment){
                        assign TSTNo2 to HighestTST
                        assign TSTPrice2 to HighestTSTPrice
                    }
                }
            }

            if (TSTSegments2!=FirstSegment){
                assign ""
            }
        }

        capture line:5, column:1, length:1 assign to nextcheck
        if (nextcheck != "D"){
            assign "3" to TSTcount
            capture line:4, column:1, length:3 assign to TSTNo3
            capture line:4, column:9, length:1 assign to Infcheck3
            capture line:4, column:38, length:13 assign to TSTPrice3
            capture line:4, column:75, length:5 assign to TSTSegments3

            if (Infcheck3 != "I"){
                if (TSTPrice3 > HighestTSTPrice){
                    if (TSTSegments2==TSTSegments1){
                        assign TSTNo3 to HighestTSTPrice
                        assign TSTNo2 to HighestTST
                    }
                }
            }

            if (TSTSegments2==TSTSegments1){
                assign "FirstSegment" to checkOriginal2
            }
            else{
                assign "SecondSegment" to checkOriginal2
            }
        }
    }
}
else{

}