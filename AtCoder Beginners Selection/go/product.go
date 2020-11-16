package main

import "fmt"

func main() {
	var (
		a int
		b int
	)

	fmt.Scanf("%d", &a)
	fmt.Scanf("%d", &b)
	c := a * b
	if c%2 == 0 {
		fmt.Println("Even")
	} else {
		fmt.Println("Odd")
	}
}
