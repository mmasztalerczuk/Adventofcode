package main

import (
       "fmt"
       "bufio"
       "os"
       "strings"
       "strconv"
)

func main(){
       var dir, x, y, ans_x, ans_y  int = 0, 0, 0, 0, 0
       var fin bool = false
       values := [800][800]int{}

       reader := bufio.NewReader(os.Stdin)
       text, _ := reader.ReadString('\n')

       r := strings.Split(strings.TrimSpace(text), ", ")
       for i := 0; i < len(r); i++ {




	      if fin {
                     break
              }

              tmp, err := strconv.Atoi(r[i][1:])
              if err != nil {
                     fmt.Println(err)
              }

              if dir == 0 {
                     if r[i][0] == 'R' {

                            for a := x; x+tmp != a; {
                                   a += 1
                                   if values[400+a][400+y] == 1 {
                                          ans_x = a
                                          ans_y = y
                                          fin = true
                                          break
                                   }
                                   values[400+a][400+y] = 1
                            }
                            x += tmp

                     } else {
                            for a := x; x-tmp != a; {
                                   a -= 1
                                   if values[400+a][400+y]  == 1 {
                                          ans_x = a
                                          ans_y = y
                                          fin = true
                                          break
                                   }
                                   values[400+a][400+y] = 1
                            }
                            x -= tmp
                     }
              } else if dir == 1 {
                     if r[i][0] == 'R' {
                            for a := y; y-tmp != a; {
                                   a -= 1
                                   if values[400+x][400+a]  == 1 {
                                          ans_x = x
                                          ans_y = a
                                          fin = true
                                          break
                                   }
                                   values[400+x][400+a] = 1
                            }
                            y -= tmp
                     } else {
                            for a := y; y+tmp != a; {
                                   a += 1
                                   if values[400+x][400+a]  == 1 {
                                          ans_x = x
                                          ans_y = a
                                          fin = true
                                          break
                                   }
                                   values[400+x][400+a] = 1
                            }
                            y += tmp
                     }
              } else if dir == 2 {
                     if r[i][0] == 'R' {
                            for a := x; x-tmp != a; {
                                   a -= 1
                                   if values[400+a][400+y]  == 1 {
                                          ans_x = a
                                          ans_y = y
                                          fin = true
                                          break
                                   }
                                   values[400+a][400+y] = 1
                            }
                            x -= tmp
                     } else {
                            for a := x; x+tmp != a; {
                                   a += 1
                                   if values[400+a][400+y]  == 1 {
                                          ans_x = a
                                          ans_y = y
                                          fin = true
                                          break
                                   }
                                   values[400+a][400+y] = 1
                            }
                            x += tmp
                     }
              } else  {
                     if r[i][0] == 'R' {
			     fmt.Print("ELO")
                            for a := y; y+tmp != a; {
                                   a += 1
                                   if values[400+x][400+a]  == 1 {
                                          ans_x = x
                                          ans_y = a
                                          fin = true
                                          break
                                   }
                                   values[400+x][400+a] = 1
                            }
                            y += tmp
                     } else {
                            for a := y; y-tmp != a; {
                                   a -= 1
                                   if values[400+x][400+a]  == 1 {
                                          ans_x = x
                                          ans_y = a
                                          fin = true
                                          break
                                   }
                                   values[400+x][400+a] = 1
                            }
                            y -= tmp
                     }
              }

              if r[i][0] == 'R' {
                     dir += 1
              } else {
                     dir -= 1
              }

              if dir < 0 {
                     dir = 3
              } else if dir > 3 {
                     dir = 0
              }


       }
       fmt.Printf("%d %d\n", ans_x, ans_y)
}