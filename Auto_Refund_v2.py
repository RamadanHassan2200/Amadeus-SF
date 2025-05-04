send "SRT" +DOI
  capture line:1, column:37, length:2 assign to travelYear
  send "DD" +DOI +"/" +travelDate1 +travelYear
  capture line:2, column:1, length:1 assign to checkyear
  if (checkyear =="-"){
  send "DF" +travelYear +";1"
  capture line:2, column:1, length:2 assign to travelYear
  }

  send "DD"
  capture line:2, column:33, length:7 assign to todaysdate
  send "DD" +todaysdate +"/" +travelDate1 +travelYear

  if ()

