package main

import "fmt"

type Employee struct {
	id   int
	name string
}

func (e *Employee) SetId(id int) {
	e.id = id
}

func (e *Employee) SetName(name string) {
	e.name = name
}

func (e *Employee) GetId() int {
	return e.id
}

func (e *Employee) GetName() string {
	return e.name
}

func main() {
	e := Employee{}
	fmt.Printf("%v \n", e)

	e.SetId(10)
	e.SetName("Luca")
	fmt.Printf("%v \n", e)

	fmt.Printf("%v \n", e.GetId())
	fmt.Printf("%v \n", e.GetName())

}
