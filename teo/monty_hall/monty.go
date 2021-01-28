package main

import (
	"math/rand"
	"time"
)

func monty() (bool, bool) {

	// cria as portas
	portas := map[int32]bool{
		1: false,
		2: false,
		3: false,
	}

	// aleatoriza onde o premio estará
	premio := rand.Int31n(3) + 1
	portas[premio] = true

	escolha := rand.Int31n(3) + 1

	choices := []int32{}
	for k := range portas {
		if k != escolha && k != premio {
			choices = append(choices, k)
		}
	}

	rand.Shuffle(len(choices), func(i, j int) { choices[j], choices[i] = choices[i], choices[j] })
	abertura := choices[0]

	choices = []int32{}
	for k := range portas {
		if k != abertura {
			choices = append(choices, k)
		}
	}
	rand.Shuffle(len(choices), func(i, j int) { choices[j], choices[i] = choices[i], choices[j] })

	novaEscolha := choices[0]

	var troca, vencedor bool
	if novaEscolha == escolha {
		troca = true
	}

	if novaEscolha == premio {
		vencedor = true
	}

	return troca, vencedor

}

func main() {

	rand.Seed(time.Now().UnixNano())
	trocas := []bool{}
	vitorias := []bool{}

	for i := 1; i <= 1000000; i++ {
		troca, vitoria := monty()
		trocas = append(trocas, troca)
		vitorias = append(vitorias, vitoria)
	}
}
