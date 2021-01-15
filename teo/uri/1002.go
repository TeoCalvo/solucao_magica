package main

import (
	"fmt"
	"math"
)

func main() {
	pi := 3.14159
	var raio float64
	fmt.Scanf("%f", &raio)
	fmt.Println(fmt.Sprintf("A=%.4f", pi*math.Pow(raio, 2)))
}
