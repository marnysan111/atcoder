package main

import "fmt"

func main() {
	var (
		a int
		b int
		c int
		s string
	)
	fmt.Scanf("%d", &a)
	fmt.Scanf("%d %d", &b, &c)
	fmt.Scanf("%s", &s)
	fmt.Println(a + b + c)
	fmt.Println(s)
}
