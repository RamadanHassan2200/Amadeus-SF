send "rttn"
capture line:3, column:5, length:2 assign to FA2
if (FA2=="FA"){
  capture line:3, column:2, length:2 assign to XFA2
  capture line:3, column:26, length:3 assign to XVA2
}
capture line:4, column:5, length:2 assign to FA3
if (FA3=="FA"){
  capture line:4, column:2, length:2 assign to XFA3
  capture line:4, column:26, length:3 assign to XVA3
}
capture line:5, column:5, length:2 assign to FA4
if (FA4=="FA"){
  capture line:5, column:2, length:2 assign to XFA4
  capture line:5, column:26, length:3 assign to XVA4
}
capture line:6, column:5, length:2 assign to FA5
if (FA5=="FA"){
  capture line:6, column:2, length:2 assign to XFA5
  capture line:6, column:26, length:3 assign to XVA5
}
capture line:7, column:5, length:2 assign to FA6
if (FA6=="FA"){
  capture line:7, column:2, length:2 assign to XFA6
  capture line:7, column:26, length:3 assign to XVA6
}
capture line:8, column:5, length:2 assign to FA7
if (FA7=="FA"){
  capture line:8, column:2, length:2 assign to XFA7
  capture line:8, column:26, length:3 assign to XVA7
}
capture line:9, column:5, length:2 assign to FA8
if (FA8=="FA"){
  capture line:9, column:2, length:2 assign to XFA8
  capture line:9, column:26, length:3 assign to XVA8
}
capture line:10, column:5, length:2 assign to FA9
if (FA9=="FA"){
  capture line:10, column:2, length:2 assign to XFA9
  capture line:10, column:26, length:3 assign to XVA9
}
capture line:11, column:5, length:2 assign to FA10
if (FA10=="FA"){
  capture line:11, column:2, length:2 assign to XFA10
  capture line:11, column:26, length:3 assign to XVA10
}
capture line:12, column:5, length:2 assign to FA11
if (FA11=="FA"){
  capture line:12, column:2, length:2 assign to XFA11
  capture line:12, column:26, length:3 assign to XVA11
}
capture line:13, column:5, length:2 assign to FA12
if (FA12=="FA"){
  capture line:13, column:2, length:2 assign to XFA12
  capture line:13, column:26, length:3 assign to XVA12
}
capture line:14, column:5, length:2 assign to FA13
if (FA13=="FA"){
  capture line:14, column:2, length:2 assign to XFA13
  capture line:14, column:26, length:3 assign to XVA13
}
capture line:15, column:5, length:2 assign to FA14
if (FA14=="FA"){
  capture line:15, column:2, length:2 assign to XFA14
  capture line:15, column:26, length:3 assign to XVA14
}
capture line:16, column:5, length:2 assign to FA15
if (FA15=="FA"){
  capture line:16, column:2, length:2 assign to XFA15
  capture line:16, column:26, length:3 assign to XVA15
}
capture line:17, column:5, length:2 assign to FA16
if (FA16=="FA"){
  capture line:17, column:2, length:2 assign to XFA16
  capture line:17, column:26, length:3 assign to XVA16
}
capture line:18, column:5, length:2 assign to FA17
if (FA17=="FA"){
  capture line:18, column:2, length:2 assign to XFA17
  capture line:18, column:26, length:3 assign to XVA17
}
capture line:19, column:5, length:2 assign to FA18
if (FA18=="FA"){
  capture line:19, column:2, length:2 assign to XFA18
  capture line:19, column:26, length:3 assign to XVA18
}
capture line:20, column:5, length:2 assign to FA19
if (FA19=="FA"){
  capture line:20, column:2, length:2 assign to XFA19
  capture line:20, column:26, length:3 assign to XVA19
}
capture line:21, column:5, length:2 assign to FA20
if (FA20=="FA"){
  capture line:21, column:2, length:2 assign to XFA20
  capture line:21, column:26, length:3 assign to XVA20
}
capture line:22, column:5, length:2 assign to FA21
if (FA21=="FA"){
  capture line:22, column:2, length:2 assign to XFA21
  capture line:22, column:26, length:3 assign to XVA21
}
capture line:23, column:5, length:2 assign to FA22
if (FA22=="FA"){
  capture line:23, column:2, length:2 assign to XFA22
  capture line:23, column:26, length:3 assign to XVA22
}
capture line:24, column:5, length:2 assign to FA23
if (FA23=="FA"){
  capture line:24, column:2, length:2 assign to XFA23
  capture line:24, column:26, length:3 assign to XVA23
}

if (FA23=="FA"){
  if (XVA23=="/EV"){
  send "XE" +XFA2 +"-" +XFA23
  }
}
else{
if (FA22=="FA"){
  if (XVA22=="/EV"){
  send "XE" +XFA2 +"-" +XFA22
  }
}
else{
if (FA21=="FA"){
  if (XVA21=="/EV"){
  send "XE" +XFA2 +"-" +XFA21
  }
}
else{
if (FA20=="FA"){
  if (XVA20=="/EV"){
  send "XE" +XFA2 +"-" +XFA20
  }
}
else{
if (FA19=="FA"){
  if (XVA19=="/EV"){
  send "XE" +XFA2 +"-" +XFA19
  }
}
else{
if (FA18=="FA"){
  if (XVA18=="/EV"){
  send "XE" +XFA2 +"-" +XFA18
  }
}
else{
if (FA17=="FA"){
  if (XVA17=="/EV"){
  send "XE" +XFA2 +"-" +XFA17
  }
}
else{
if (FA16=="FA"){
  if (XVA16=="/EV"){
  send "XE" +XFA2 +"-" +XFA16
  }
}
else{
if (FA15=="FA"){
  if (XVA15=="/EV"){
  send "XE" +XFA2 +"-" +XFA15
  }
}
else{
if (FA14=="FA"){
  if (XVA14=="/EV"){
  send "XE" +XFA2 +"-" +XFA14
  }
}
else{
if (FA13=="FA"){
  if (XVA13=="/EV"){
  send "XE" +XFA2 +"-" +XFA13
  }
}
else{
if (FA12=="FA"){
  if (XVA12=="/EV"){
  send "XE" +XFA2 +"-" +XFA12
  }
}
else{
if (FA11=="FA"){
  if (XVA11=="/EV"){
  send "XE" +XFA2 +"-" +XFA11
  }
}
else{
if (FA10=="FA"){
  if (XVA10=="/EV"){
  send "XE" +XFA2 +"-" +XFA10
  }
}
else{
if (FA9=="FA"){
  if (XVA9=="/EV"){
  send "XE" +XFA2 +"-" +XFA9
  }
}
else{
if (FA8=="FA"){
  if (XVA8=="/EV"){
  send "XE" +XFA2 +"-" +XFA8
  }
}
else{
if (FA7=="FA"){
  if (XVA7=="/EV"){
  send "XE" +XFA2 +"-" +XFA7
  }
}
else{
if (FA6=="FA"){
  if (XVA6=="/EV"){
  send "XE" +XFA2 +"-" +XFA6
  }
}
else{
if (FA5=="FA"){
  if (XVA5=="/EV"){
  send "XE" +XFA2 +"-" +XFA5
  }
}
else{
if (FA4=="FA"){
  if (XVA4=="/EV"){
  send "XE" +XFA2 +"-" +XFA4
  }
}
else{
if (FA3=="FA"){
  if (XVA3=="/EV"){
  send "XE" +XFA2 +"-" +XFA3
  }
}
else{
if (FA2=="FA"){
  if (XVA2=="/EV"){
  send "XE" +XFA2 +"-" +XFA2
  }
}
}//2
}//3
}//4
}//5
}//6
}//7
}//8
}//9
}//10
}//11
}//12
}//13
}//14
}//15
}//16
}//17
}//18
}//19
}//20
}//21
}//22
}//23
