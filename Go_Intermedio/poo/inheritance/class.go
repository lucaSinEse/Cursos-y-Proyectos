package main

import "fmt"

type Person struct {
	name string
	age  int
}

type Employee struct {
	id int
}

type FullTimeEmployee struct {
	Person
	Employee
	time string
}

func GetMessage(p Person) {
	fmt.Printf("%s with age %d\n", p.name, p.age)
}

func main() {
	ftEmployee := FullTimeEmployee{}
	ftEmployee.name = "Name"
	ftEmployee.age = 24
	ftEmployee.id = 5
	ftEmployee.time = "8 horas"
	fmt.Printf("%v\n", ftEmployee)
	GetMessage(ftEmployee.Person)
}
