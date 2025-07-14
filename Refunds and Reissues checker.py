mandatory ask "Enter the PNR: " assign to pnr
send "IG"
send "rt" +pnr

send "rhfa"
mandatory ask "What's the DOI?" assign to DOI

send "RTA"
choose "Do you want to add new or past segments?"{
    when ("Yes"){
        send "RHA"
        group{
            ask "What's the 1st segment (start with AL and add year)" assign to segment1
            ask "What's the 2nd segment (start with AL and add year)" assign to segment2
            ask "What's the 3rd segment (start with AL and add year)" assign to segment3
            ask "What's the 4th segment (start with AL and add year)" assign to segment4
            ask "What's the 5th segment (start with AL and add year)" assign to segment5
            ask "What's the 6th segment (start with AL and add year)" assign to segment6
        }

        if (segment1 != ""){
            send "SRT" +segment1
            capture line:1, column:32, length:2 assign to AL
            capture line:1, column:34, length:4 assign to flightNo
            capture line:1, column:38, length:3 assign to class
            capture line:1, column:41, length:5 assign to date
            capture line:1, column:46, length:1 assign to checkYear
            if (checkYear ==" "){
                capture line:1, column:49, length:6 assign to citypair
            }

        }

    }
    when ("No"){

    }
}

                               CX9201 N 03FEB 1*HKGDOH DK1 0025