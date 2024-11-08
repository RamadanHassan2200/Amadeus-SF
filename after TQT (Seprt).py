send "TQT"

capture line:1, column:1, length:3 assign to checkTSTNo

//NO TST
if (checkTSTNo=="NO "){
  mandatory ask "There's no TST!" assign to qz5
  send "ig"
}

// More than One TST
if (checkTSTNo !="TST"){
  capture line:1, column:35, length:5 assign to checkTSTTOTAL
  if (checkTSTTOTAL=="TOTAL"){
    mandatory ask "There's more than one TST?" assign to qz5
  }
  capture line:2, column:1, length:3 assign to TST1no
  capture line:2, column:75, length:5 assign to TST1segments
    
  capture line:3, column:1, length:3 assign to TST2no
  capture line:3, column:75, length:5 assign to TST2segments
    
  capture line:4, column:1, length:3 assign to TST3no
  capture line:4, column:75, length:5 assign to TST3segments
    
  capture line:5, column:1, length:3 assign to TST4no
  capture line:5, column:75, length:5 assign to TST4segments
    
  capture line:6, column:1, length:3 assign to TST5no
  capture line:6, column:75, length:5 assign to TST5segments
    
  capture line:7, column:1, length:3 assign to TST6no
  capture line:7, column:75, length:5 assign to TST6segments
    
  capture line:8, column:1, length:3 assign to TST7no
  capture line:8, column:75, length:5 assign to TST7segments
    
  capture line:9, column:1, length:3 assign to TST8no
  capture line:9, column:75, length:5 assign to TST8segments
    
  capture line:10, column:1, length:3 assign to TST9no
  capture line:10, column:75, length:5 assign to TST9segments
    
  capture line:11, column:1, length:3 assign to TST10no
  capture line:11, column:75, length:5 assign to TST10segments
    
  capture line:12, column:1, length:3 assign to TST11no
  capture line:12, column:75, length:5 assign to TST11segments
    
  capture line:13, column:1, length:3 assign to TST12no
  capture line:13, column:75, length:5 assign to TST12segments
    
  capture line:14, column:1, length:3 assign to TST13no
  capture line:14, column:75, length:5 assign to TST13segments
    
  capture line:15, column:1, length:3 assign to TST14no
  capture line:15, column:75, length:5 assign to TST14segments
    
  capture line:16, column:1, length:3 assign to TST15no
  capture line:16, column:75, length:5 assign to TST15segments
    
  capture line:17, column:1, length:3 assign to TST16no
  capture line:17, column:75, length:5 assign to TST16segments
    
  capture line:18, column:1, length:3 assign to TST17no
  capture line:18, column:75, length:5 assign to TST17segments
    
  capture line:19, column:1, length:3 assign to TST18no
  capture line:19, column:75, length:5 assign to TST18segments
    
  capture line:20, column:35, length:3 assign to TST19currency
  if (TST19currency == TST1currency){
    send "More than 18 TST!"
    mandatory ask "Plesae continue manually!" assign to qz5
    send "ig"
  }
  assign "1" to separateSegmentsCount
  assign TST1segments to firstSegment
  append TST1no to firstGroup 
  if ()
  

  
  
  
}
