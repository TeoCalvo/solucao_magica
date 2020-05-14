package main

import (
	"fmt"
	"mypkg/tempconv"
)

func main() {

	c := tempconv.Celsius(32)

	fmt.Println(tempconv.CToF(c))

}
