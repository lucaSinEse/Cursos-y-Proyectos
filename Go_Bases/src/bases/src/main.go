package main

import (
	"fmt"
	pk "go_bases/src/bases/src/mypackage"
)

func main() {
	var myCar pk.CarPublic
	myCar.Brand = "Ferrari"
	myCar.Year = 2020
	fmt.Println(myCar)

	pk.PrintMessage("holaaaa")
}
