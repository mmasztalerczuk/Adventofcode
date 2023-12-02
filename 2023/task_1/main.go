package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var ans int = 0
	for scanner.Scan() {
		txt := scanner.Text()
		var a byte = 0
		var b byte = 0
		for i := 0; i < len(txt); i++ {
    			if (a == 0 && txt[i] >= '0' && txt[i] <= '9') {
				a = txt[i]
			}
			if (txt[i] >= '0' && txt[i] <= '9') {
				b = txt[i]
			}
 		}
		//fmt.Printf("%d %d\n", a-'0', b-'0')
		ans += int((a-'0')*10) + int(b-'0')
	}
	fmt.Printf("%d", ans)
}
