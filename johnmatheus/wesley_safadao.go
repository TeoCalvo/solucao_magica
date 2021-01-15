package main

import (
	"flag"
	"fmt"
	"time"
)

func somatorio(x int) int {
	total := 0
	for ; x > 0; x-- {
		total += x
	}
	return total
}

func main() {

	data := flag.String("data", "00-00-0000", "Data de aniversário")
	flag.Parse()

	newdata, _ := time.Parse("02-01-2006", *data)

	safadeza := somatorio(int(newdata.Month())) + (newdata.Year()/1000)*(50-newdata.Day())
	anjo := 100 - safadeza
	fmt.Println("Safadeza: ", safadeza)
	fmt.Println("Anjo :", anjo)
}
