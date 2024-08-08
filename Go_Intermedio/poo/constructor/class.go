package main

import "fmt"

type Employee struct {
	id       int
	name     string
	vacation bool
}

func NewEmployee(id int, name string, vacation bool) *Employee {
	return &Employee{
		id:       id,
		name:     name,
		vacation: vacation,
	}
}

func main() {
	//forma 1
	e := Employee{}
	fmt.Printf("%v \n", e)

	//forma 2
	e2 := Employee{
		id:       1,
		name:     "Nombre",
		vacation: true,
	}
	fmt.Printf("%v \n", e2)

	//forma 3
	e3 := new(Employee)
	fmt.Printf("%v \n", *e3)

	//forma 4
	e4 := NewEmployee(1, "Name 4", false)
	fmt.Printf("%v \n", *e4)

}
