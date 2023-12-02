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
	var ans int64 = 0
	for scanner.Scan() {
		txt := scanner.Text()
		// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
		values := strings.TrimSpace(strings.Split(txt, ":")[1])
		turns := strings.Split(values, ";")
		
			var red int64 = 0
			var green int64 = 0
			var blue int64 = 0
		for _, ch := range turns {
			trim_ch := strings.TrimSpace(ch)
			rounds := strings.Split(trim_ch, ",")
			for _, r := range rounds {
				trim_r := strings.TrimSpace(r)
				number_and_color := strings.Split(trim_r, " ")
				val, _ := strconv.ParseInt(number_and_color[0], 10, 0)
				color := number_and_color[1]
				if (color == "red") {
					if (val > red) {
						red = val
					}
				}
				if (color == "green") {
					if (val > green) {
						green = val
					}
				}
				if (color == "blue") {
					if (val > blue) {
						blue = val
					}
				}								
			}
		}
		ans += red*green*blue
	}
	fmt.Println(ans)
}
