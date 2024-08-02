package main

import (
	"fmt"
	"strconv"
	"time"
)

func main() {
	//Explicita
	var x int
	x = 8
	//Implicita
	y := 7

	fmt.Println(x)
	fmt.Println(y)

	myValue, err := strconv.ParseInt("a", 0, 64)
	if err != nil {
		fmt.Printf("%v \n", err)
	}
	fmt.Println(myValue)

	//map
	m := make(map[string]int)
	m["Key"] = 6
	fmt.Println(m["Key"])

	// Slice
	s := []int{1, 2, 3}

	for index, value := range s {
		fmt.Println(index)
		fmt.Println(value)

	}
	s = append(s, 16)
	for index, value := range s {
		fmt.Println(index)
		fmt.Println(value)
	}

	c := make(chan int)
	go doSomething(c)
	<-c

	g := 25
	fmt.Println(g)
	h := &g
	fmt.Println(h)
	fmt.Println(*h)
}

func doSomething(c chan int) {
	time.Sleep(3 * time.Second)
	fmt.Println("Done")
	c <- 1
}
