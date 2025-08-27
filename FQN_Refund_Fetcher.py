//FQN_Refund_Fetcher
send "MT"
send "MD-/TPM"
capture line:1, column:8, length:2 assign to check_Display
if (check_Display=="**"){
    capture line:1, column:18, length:2 assign to FQN_Airline
    capture line:3, column:4, length:10 assign to FQN_FareBasis
    capture line:3, column:35, length:3 assign to FQN_Refundable
}
else{

capture line:3, column:1, length:14 assign to check_Fare_Component
if (check_Fare_Component == "FARE COMPONENT"){
    capture line:3, column:33, length:2 assign to FQN_Airline
    capture line:3, column:37, length:10 assign to FQN_FareBasis
}

capture line:4, column:1, length:14 assign to check_Fare_Component
if (check_Fare_Component == "FARE COMPONENT"){
    capture line:4, column:33, length:2 assign to FQN_Airline
    capture line:4, column:37, length:10 assign to FQN_FareBasis
}

capture line:5, column:1, length:14 assign to check_Fare_Component
if (check_Fare_Component == "FARE COMPONENT"){
    capture line:5, column:33, length:2 assign to FQN_Airline
    capture line:5, column:37, length:10 assign to FQN_FareBasis
}
}
if (FQN_Refundable == "NRF"){
if (FQN_Airline !="AI"){
send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: Non-Refundable" +"
No-Show Penalty: Non-Refundable"
}//AI
}
else{
    send "MD-CANCELLATIONS"
    assign "" to normal_Penalty
    assign "" to noshow_Penalty
    assign "" to FQN_Currency

if (FQN_Airline == "SM"){
    send "MD-CANCEL/REFUND"
    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                                capture line:1, column:22, length:1 assign to check_Dot1
                                                if (check_Dot1 != "."){
                                                    assign "ERROR!" to normal_Penalty
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    
    send "MD-NO-SHOW"

    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }

    send "DF" +normal_Penalty +";" +noshow_Penalty
    capture line:2, column:1, length:12 assign to noshow_Penalty

    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: " +FQN_Currency + " " + normal_Penalty + "
No-Show Penalty: " +FQN_Currency + " " + noshow_Penalty

}//SM

if (FQN_Airline == "MS"){
    send "MD-CANCEL/REFUND"
    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                                capture line:1, column:22, length:1 assign to check_Dot1
                                                if (check_Dot1 != "."){
                                                    assign "ERROR!" to normal_Penalty
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }   

    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    
    
    send "MD-NO-SHOW"

    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }


    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: " +FQN_Currency + " " + normal_Penalty + "
No-Show Penalty: " +FQN_Currency + " " + noshow_Penalty

}//MS

if (FQN_Airline == "GF"){
    if (FQN_Refundable == " - "){
        send "MD-NO-SHOW"
        capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }

    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: USD "  + normal_Penalty + "
No-Show Penalty: USD "  + noshow_Penalty
    }
    else{
        send "MD-CANCEL/REFUND"
    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                                capture line:1, column:22, length:1 assign to check_Dot1
                                                if (check_Dot1 != "."){
                                                    assign "ERROR!" to normal_Penalty
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }   

    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    
    
    send "MD-NO-SHOW"

    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }

    send "DF" +normal_Penalty +";" +noshow_Penalty
    capture line:2, column:1, length:12 assign to noshow_Penalty

    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: " +FQN_Currency + " " + normal_Penalty + "
No-Show Penalty: " +FQN_Currency + " " + noshow_Penalty

    }
}//GF

if (FQN_Airline == "PR"){
    send "MD-REFUND."
    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                                capture line:1, column:22, length:1 assign to check_Dot1
                                                if (check_Dot1 != "."){
                                                    assign "ERROR!" to normal_Penalty
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    
    
    send "MD-NO-SHOW"

    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }

    send "DF" +normal_Penalty +";" +noshow_Penalty
    capture line:2, column:1, length:12 assign to noshow_Penalty
    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: " +FQN_Currency + " " + normal_Penalty + "
No-Show Penalty: " +FQN_Currency + " " + noshow_Penalty

}//PR

if (FQN_Airline == "EY"){
    if (FQN_Refundable == " - "){
        send "MD-CANCEL/REFUND"
        capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
        assign "0" to noshow_Penalty
    }

    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: USD "  + normal_Penalty + "
No-Show Penalty: USD "  + noshow_Penalty
    }
    else{
        send "MD-CANCEL/REFUND"
    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                                capture line:1, column:22, length:1 assign to check_Dot1
                                                if (check_Dot1 != "."){
                                                    assign "ERROR!" to normal_Penalty
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to normal_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to normal_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to normal_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to normal_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to normal_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to normal_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to normal_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to normal_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to normal_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to normal_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }   

    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to normal_Penalty
    }
    
    send "MD-CANCELLATIONS"
    send "MD-NO-SHOW"

    capture line:1, column:1, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:8, length:3 assign to FQN_Currency
        capture line:1, column:12, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:13, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:14, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:15, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:16, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:17, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:18, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:19, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:20, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:21, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:2, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:9, length:3 assign to FQN_Currency
        capture line:1, column:13, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:14, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:15, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:16, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:17, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:18, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:19, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:20, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:21, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:22, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:3, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:10, length:3 assign to FQN_Currency
        capture line:1, column:14, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:15, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:16, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:17, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:18, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:19, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:20, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:21, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:22, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:23, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    capture line:1, column:4, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:11, length:3 assign to FQN_Currency
        capture line:1, column:15, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:16, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:17, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:18, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:19, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:20, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:21, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:22, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:23, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:24, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:5, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:12, length:3 assign to FQN_Currency
        capture line:1, column:16, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:17, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:18, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:19, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:20, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:21, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:22, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:23, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:24, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:25, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:6, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:13, length:3 assign to FQN_Currency
        capture line:1, column:17, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:18, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:19, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:20, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:21, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:22, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:23, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:24, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:25, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:26, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:7, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:14, length:3 assign to FQN_Currency
        capture line:1, column:18, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:19, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:20, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:21, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:22, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:23, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:24, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:25, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:26, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:27, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:8, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:15, length:3 assign to FQN_Currency
        capture line:1, column:19, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:20, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:21, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:22, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:23, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:24, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:25, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:26, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:27, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:28, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:9, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:16, length:3 assign to FQN_Currency
        capture line:1, column:20, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:21, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:22, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:23, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:24, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:25, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:26, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:27, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:28, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:29, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    capture line:1, column:10, length:6 assign to check_CNX_Charge
    if (check_CNX_Charge == "CHARGE"){
        capture line:1, column:17, length:3 assign to FQN_Currency
        capture line:1, column:21, length:1 assign to check_Dot1
        if (check_Dot1 != "."){
            append check_Dot1 to noshow_Penalty
            capture line:1, column:22, length:1 assign to check_Dot1
            if (check_Dot1 != "."){
                append check_Dot1 to noshow_Penalty
                capture line:1, column:23, length:1 assign to check_Dot1
                if (check_Dot1 != "."){
                    append check_Dot1 to noshow_Penalty
                    capture line:1, column:24, length:1 assign to check_Dot1
                    if (check_Dot1 != "."){
                        append check_Dot1 to noshow_Penalty
                        capture line:1, column:25, length:1 assign to check_Dot1
                        if (check_Dot1 != "."){
                            append check_Dot1 to noshow_Penalty
                            capture line:1, column:26, length:1 assign to check_Dot1
                            if (check_Dot1 != "."){
                                append check_Dot1 to noshow_Penalty
                                capture line:1, column:27, length:1 assign to check_Dot1
                                if (check_Dot1 != "."){
                                    append check_Dot1 to noshow_Penalty
                                    capture line:1, column:28, length:1 assign to check_Dot1
                                    if (check_Dot1 != "."){
                                        append check_Dot1 to noshow_Penalty
                                        capture line:1, column:29, length:1 assign to check_Dot1
                                        if (check_Dot1 != "."){
                                            append check_Dot1 to noshow_Penalty
                                            capture line:1, column:30, length:1 assign to check_Dot1
                                            if (check_Dot1 != "."){
                                                append check_Dot1 to noshow_Penalty
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


    capture line:1, column:7, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:8, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:9, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:10, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:11, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:12, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:13, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:14, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:15, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:16, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:17, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:18, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:19, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:20, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:21, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:22, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }
    capture line:1, column:23, length:9 assign to check_CNX_permission
    if (check_CNX_permission == "PERMITTED"){
        assign "0" to noshow_Penalty
    }


    send "Fare Rule: " + FQN_FareBasis + "
Normal  Penalty: " +FQN_Currency + " " + normal_Penalty + "
No-Show Penalty: " +FQN_Currency + " " + noshow_Penalty

    }
}//EY



}// non NRF