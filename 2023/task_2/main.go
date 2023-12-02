  package main

import (
	"bufio"
	"strconv"
	"strings"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var i int = 1
	var ans int = 0
	for scanner.Scan() {
		txt := scanner.Text()
		// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
		values := strings.TrimSpace(strings.Split(txt, ":")[1])
		turns := strings.Split(values, ";")
		var possible bool = true
		for _, ch := range turns {
			trim_ch := strings.TrimSpace(ch)
			rounds := strings.Split(trim_ch, ",")
			for _, r := range rounds {
				trim_r := strings.TrimSpace(r)
				number_and_color := strings.Split(trim_r, " ")
				val, _ := strconv.ParseInt(number_and_color[0], 10, 0)
				color := number_and_color[1]
				if (color == "red") {
					if (val > 12) {
						possible = false
					}
				}
				if (color == "green") {
					if (val > 13) {
						possible = false
					}
				}
				if (color == "blue") {
					if (val > 14) {
						possible = false
					}
				}								
			}
		}
		if (possible) {
			ans += i
		}
		i += 1
	}
	fmt.Println(ans)
}
