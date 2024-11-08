send "rttn"
capture line:2, column:5, length:2 assign to FA1
if (FA1=="FA"){
  capture line:2, column:12, length:14 assign to TFA1
  capture line:2, column:26, length:3 assign to TTA1
}
capture line:3, column:5, length:2 assign to FA2
if (FA2=="FA"){
  capture line:3, column:12, length:14 assign to TFA2
  capture line:3, column:26, length:3 assign to TTA2
}
capture line:4, column:5, length:2 assign to FA3
if (FA3=="FA"){
  capture line:4, column:12, length:14 assign to TFA3
  capture line:4, column:26, length:3 assign to TTA3
}
capture line:5, column:5, length:2 assign to FA4
if (FA4=="FA"){
  capture line:5, column:12, length:14 assign to TFA4
  capture line:5, column:26, length:3 assign to TTA4
}
capture line:6, column:5, length:2 assign to FA5
if (FA5=="FA"){
  capture line:6, column:12, length:14 assign to TFA5
  capture line:6, column:26, length:3 assign to TTA5
}
capture line:7, column:5, length:2 assign to FA6
if (FA6=="FA"){
  capture line:7, column:12, length:14 assign to TFA6
  capture line:7, column:26, length:3 assign to TTA6
}
capture line:8, column:5, length:2 assign to FA7
if (FA7=="FA"){
  capture line:8, column:12, length:14 assign to TFA7
  capture line:8, column:26, length:3 assign to TTA7
}
capture line:9, column:5, length:2 assign to FA8
if (FA8=="FA"){
  capture line:9, column:12, length:14 assign to TFA8
  capture line:9, column:26, length:3 assign to TTA8
}
capture line:10, column:5, length:2 assign to FA9
if (FA9=="FA"){
  capture line:10, column:12, length:14 assign to TFA9
  capture line:10, column:26, length:3 assign to TTA9
}
capture line:11, column:5, length:2 assign to FA10
if (FA10=="FA"){
  capture line:11, column:12, length:14 assign to TFA10
  capture line:11, column:26, length:3 assign to TTA10
}
capture line:12, column:5, length:2 assign to FA11
if (FA11=="FA"){
  capture line:12, column:12, length:14 assign to TFA11
  capture line:12, column:26, length:3 assign to TTA11
}
capture line:13, column:5, length:2 assign to FA12
if (FA12=="FA"){
  capture line:13, column:12, length:14 assign to TFA12
  capture line:13, column:26, length:3 assign to TTA12
}
capture line:14, column:5, length:2 assign to FA13
if (FA13=="FA"){
  capture line:14, column:12, length:14 assign to TFA13
  capture line:14, column:26, length:3 assign to TTA13
}
capture line:15, column:5, length:2 assign to FA14
if (FA14=="FA"){
  capture line:15, column:12, length:14 assign to TFA14
  capture line:15, column:26, length:3 assign to TTA14
}
capture line:16, column:5, length:2 assign to FA15
if (FA15=="FA"){
  capture line:16, column:12, length:14 assign to TFA15
  capture line:16, column:26, length:3 assign to TTA15
}
capture line:17, column:5, length:2 assign to FA16
if (FA16=="FA"){
  capture line:17, column:12, length:14 assign to TFA16
  capture line:17, column:26, length:3 assign to TTA16
}
capture line:18, column:5, length:2 assign to FA17
if (FA17=="FA"){
  capture line:18, column:12, length:14 assign to TFA17
  capture line:18, column:26, length:3 assign to TTA17
}
capture line:19, column:5, length:2 assign to FA18
if (FA18=="FA"){
  capture line:19, column:12, length:14 assign to TFA18
  capture line:19, column:26, length:3 assign to TTA18
}

////
if (TTA1=="/ET"){
  send "TWD/TKT" +TFA1
  capture line:4, column:47, length:1 assign to status1
  if (status1 =="O"){
    assign "TRUE" to Name1ST
  }
  if (status1=="A"){
     assign "TRUE" to Name1ST
  }
  if (Name1ST=="TRUE"){
    capture line:3, column:12, length:
  }
}
if (TTA2=="/ET"){
    send "TWD/TKT" +TFA2
  capture line:4, column:47, length:1 assign to status2
  if (status2 =="O"){
    capture line:3, column:6, length:20 assign to Name2
  }
  if (status2=="A"){
     capture line:3, column:6, length:20 assign to Name2
  }
}
if (TTA3=="/ET"){
    send "TWD/TKT" +TFA3
  capture line:4, column:47, length:1 assign to status3
  if (status3 =="O"){
    capture line:3, column:6, length:20 assign to Name3
  }
  if (status3=="A"){
     capture line:3, column:6, length:20 assign to Name3
  }
}
if (TTA4=="/ET"){
    send "TWD/TKT" +TFA4
  capture line:4, column:47, length:1 assign to status4
  if (status4 =="O"){
    capture line:3, column:6, length:20 assign to Name4
  }
  if (status4=="A"){
     capture line:3, column:6, length:20 assign to Name4
  }
}
if (TTA5=="/ET"){
    send "TWD/TKT" +TFA5
  capture line:4, column:47, length:1 assign to status5
  if (status5 =="O"){
    capture line:3, column:6, length:20 assign to Name5
  }
  if (status5=="A"){
     capture line:3, column:6, length:20 assign to Name5
  }
}
if (TTA6=="/ET"){
    send "TWD/TKT" +TFA6
  capture line:4, column:47, length:1 assign to status6
  if (status6 =="O"){
    capture line:3, column:6, length:20 assign to Name6
  }
  if (status6=="A"){
     capture line:3, column:6, length:20 assign to Name6
  }
}
if (TTA7=="/ET"){
    send "TWD/TKT" +TFA7
  capture line:4, column:47, length:1 assign to status7
  if (status7 =="O"){
    capture line:3, column:6, length:20 assign to Name7
  }
  if (status7=="A"){
     capture line:3, column:6, length:20 assign to Name7
  }
}
if (TTA8=="/ET"){
    send "TWD/TKT" +TFA8
  capture line:4, column:47, length:1 assign to status8
  if (status8 =="O"){
    capture line:3, column:6, length:20 assign to Name8
  }
  if (status8=="A"){
     capture line:3, column:6, length:20 assign to Name8
  }
}
if (TTA9=="/ET"){
    send "TWD/TKT" +TFA9
  capture line:4, column:47, length:1 assign to status9
  if (status9 =="O"){
    capture line:3, column:6, length:20 assign to Name9
  }
  if (status9=="A"){
     capture line:3, column:6, length:20 assign to Name9
  }
}
if (TTA10=="/ET"){
    send "TWD/TKT" +TFA10
  capture line:4, column:47, length:1 assign to status10
  if (status10 =="O"){
    capture line:3, column:6, length:20 assign to Name10
  }
  if (status10=="A"){
     capture line:3, column:6, length:20 assign to Name10
  }
}
if (TTA11=="/ET"){
    send "TWD/TKT" +TFA11
  capture line:4, column:47, length:1 assign to status11
  if (status11 =="O"){
    capture line:3, column:6, length:20 assign to Name11
  }
  if (status11=="A"){
     capture line:3, column:6, length:20 assign to Name11
  }
}
if (TTA12=="/ET"){
    send "TWD/TKT" +TFA12
  capture line:4, column:47, length:1 assign to status12
  if (status12 =="O"){
    capture line:3, column:6, length:20 assign to Name12
  }
  if (status12=="A"){
     capture line:3, column:6, length:20 assign to Name12
  }
}

if (Name12!=""){
      send "" +Name1 +"      " +TFA1 +"
      " +Name2 +"      " +TFA2 +"
      " +Name3 +"      " +TFA3 +"
      " +Name4 +"      " +TFA4 +"
      " +Name5 +"      " +TFA5 +"
      " +Name6 +"      " +TFA6 +"
      " +Name7 +"      " +TFA7 +"
      " +Name8 +"      " +TFA8 +"
      " +Name9 +"      " +TFA9 +"
      " +Name10 +"      " +TFA10 +"
      " +Name11 +"      " +TFA11 +"
      " +Name12 +"      " +TFA12 
}
else{
if (Name11!=""){
      send "" +Name1 +"      " +TFA1 +"
      " +Name2 +"      " +TFA2 +"
      " +Name3 +"      " +TFA3 +"
      " +Name4 +"      " +TFA4 +"
      " +Name5 +"      " +TFA5 +"
      " +Name6 +"      " +TFA6 +"
      " +Name7 +"      " +TFA7 +"
      " +Name8 +"      " +TFA8 +"
      " +Name9 +"      " +TFA9 +"
      " +Name10 +"      " +TFA10 +"
      " +Name11 +"      " +TFA11
}
else{
if (Name10!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5 +"
    " +Name6 +"      " +TFA6 +"
    " +Name7 +"      " +TFA7 +"
    " +Name8 +"      " +TFA8 +"
    " +Name9 +"      " +TFA9 +"
    " +Name10 +"      " +TFA10
}
else{
if (Name9!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5 +"
    " +Name6 +"      " +TFA6 +"
    " +Name7 +"      " +TFA7 +"
    " +Name8 +"      " +TFA8 +"
    " +Name9 +"      " +TFA9
}
else{
if (Name8!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5 +"
    " +Name6 +"      " +TFA6 +"
    " +Name7 +"      " +TFA7 +"
    " +Name8 +"      " +TFA8
}
else{
if (Name7!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5 +"
    " +Name6 +"      " +TFA6 +"
    " +Name7 +"      " +TFA7
}
else{
if (Name6!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5 +"
    " +Name6 +"      " +TFA6
}
else{
if (Name5!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4 +"
    " +Name5 +"      " +TFA5
}
else{
if (Name4!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3 +"
    " +Name4 +"      " +TFA4
}
else{
if (Name3!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2 +"
    " +Name3 +"      " +TFA3
}
else{
if (Name2!=""){
    send "" +Name1 +"      " +TFA1 +"
    " +Name2 +"      " +TFA2
}
else{
if (Name1!=""){
    send "" +Name1 +"      " +TFA1
}

}//1
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

