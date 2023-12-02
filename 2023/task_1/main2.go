package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var ans int = 0
	for scanner.Scan() {
		txt := scanner.Text()
		
		var index_a int = len(txt) + 1
		var val_a int = 0
		var index_b int = -1
		var val_b int = 0
		numbers := [9]string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
		for i := 0; i < len(numbers); i++ { 
                	tmp_a := strings.Index(txt, numbers[i])
			if (tmp_a != -1) {
				if (tmp_a < index_a) {
					index_a = tmp_a
					val_a = i + 1
				}
			}
			tmp_b := strings.LastIndex(txt, numbers[i])
			if (tmp_b != -1) {
				if (tmp_b > index_b) {
					index_b = tmp_b
					val_b = i + 1
				}
			}
    		}
                
		for i := 0; i < len(txt); i++ {
                        if (txt[i] >= '0' && txt[i] <= '9' && index_a > i) {
                                val_a = int(txt[i]-'0')
				index_a = i
                        }
                        if (txt[i] >= '0' && txt[i] <= '9' && index_b < i ) {
                                val_b = int(txt[i]-'0')
				index_b = i
                        }
                }

		ans += val_a * 10 + val_b

	}
	fmt.Printf("%d", ans)
}
