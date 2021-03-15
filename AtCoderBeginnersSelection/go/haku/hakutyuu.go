package main

import (
	"fmt"
	"os"
	"regexp"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)
	t := [...]string{"dream", "dreamer", "erase", "eraser"}

	for _, i := range t {
		b := check_regexp(i, s)
		if b == true {
			fmt.Println("YES")
			os.Exit(1)
		}
	}
	fmt.Println("NO")

}
func check_regexp(reg, str string) bool {
	b := regexp.MustCompile(reg).Match([]byte(str))
	return b
}
