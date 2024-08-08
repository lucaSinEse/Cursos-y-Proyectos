package main

import "fmt"

func main() {
	x := 5
	y := func() int {
		return x * 2
	}()
	fmt.Println(y)
}
