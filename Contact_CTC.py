               send "RTJ"
                capture line:2, column:5, length:3 assign to apcheck2
                capture line:3, column:5, length:3 assign to apcheck3
                capture line:4, column:5, length:3 assign to apcheck4
                capture line:5, column:5, length:3 assign to apcheck5
                capture line:6, column:5, length:3 assign to apcheck6
                capture line:7, column:5, length:3 assign to apcheck7
                capture line:8, column:5, length:3 assign to apcheck8

                assign "" to APEDetails
                if (apcheck2 =="APE"){
                    capture line:2, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                    
                    capture line:2, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                    
                    capture line:2, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }

                    capture line:2, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck3 =="APE"){
                    capture line:3, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:3, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:3, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:3, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck4 =="APE"){
                    capture line:4, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:4, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:4, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:4, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck5 =="APE"){
                    capture line:5, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:5, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:5, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:5, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck6 =="APE"){
                    capture line:6, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:6, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:6, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:6, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck7 =="APE"){
                    capture line:7, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:7, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:7, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:7, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }

                if (apcheck8 =="APE"){
                    capture line:8, column:9, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:8, column:10, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:11, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:12, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:13, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:14, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:15, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:16, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:17, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:18, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:19, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:20, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:21, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:22, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:23, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:24, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:25, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:26, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:27, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:28, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:29, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:30, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:31, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:32, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:33, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:34, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:35, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:36, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:37, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:38, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:39, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:40, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:41, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:42, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:43, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:44, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:45, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                   
                    capture line:8, column:46, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:47, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:48, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:49, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:50, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:51, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:52, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:53, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:54, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:55, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:56, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:57, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:58, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:59, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:60, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:61, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:62, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }


                    capture line:8, column:63, length:1 assign to apeChar
                    if (apeChar>="0"){
                        if (apeChar<="9"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar>="A"){
                        if (apeChar <="Z"){
                            append apeChar to APEDetails
                        }
                    }
                    if (apeChar=="-"){
                        append "./" to APEDetails
                    }
                    if (apeChar=="_"){
                        append ".." to APEDetails
                    }
                    if (apeChar=="@"){
                        append "//" to APEDetails
                    }
                    if (apeChar=="/"){
                        append "/" to APEDetails
                    }
					if (apeChar=="."){
                        append "." to APEDetails
                    }
                }
                
                assign "" to APMDetails
                assign "True" to VaildNo
                if (apcheck2 == "APM"){
                    capture line:2, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:2, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:2, column:10, length:12 assign to APMDetails
                }

                if (apcheck3 == "APM"){
                    capture line:3, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:3, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:3, column:10, length:12 assign to APMDetails
                }

                if (apcheck4 == "APM"){
                    capture line:4, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:4, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:4, column:10, length:12 assign to APMDetails
                }

                if (apcheck5 == "APM"){
                    capture line:5, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:5, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:5, column:10, length:12 assign to APMDetails
                }

                if (apcheck6 == "APM"){
                    capture line:6, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:6, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:6, column:10, length:12 assign to APMDetails
                }

                if (apcheck7 == "APM"){
                    capture line:7, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:7, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:7, column:10, length:12 assign to APMDetails
                }

                if (apcheck8 == "APM"){
                    capture line:8, column:9, length:1 assign to apmNo
                    if (apmNo!="+"){
                        assign "False" to VaildNo
                    }
                    capture line:8, column:22, length:1 assign to apmNo
                    if (apmNo>="0"){
                        if (apmNo<="9"){
                            assign "False" to VaildNo
                        }
                    }

                    capture line:8, column:10, length:12 assign to APMDetails
                }

                if (VaildNo== "False"){
                    ask "Please write the Mobile Number Correctly:" assign to APMDetails
                }

                send "SRCTCE-" +APEDetails
                send "SRCTCM-" +APMDetails