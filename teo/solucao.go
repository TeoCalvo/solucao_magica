package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func importQuery(path string) string {
	content, err := ioutil.ReadFile(path)
	if err != nil {
		panic(err)
	}
	return string(content)
}

func formatQuery(query string, params map[string]string) string {
	for k, v := range params {
		query = strings.ReplaceAll(query, k, v)
	}
	return query
}

func main() {
	path := "/home/teo/Documentos/pessoais/projetos/ensino/projetos_twitch/solucao_magica/teo/select.sql"
	query := importQuery(path)

	fmt.Println("Query antiga:")
	fmt.Printf(query)

	fmt.Println("\n\nQuery novinha:")
	params := map[string]string{"{dt_ref}": "2020-05-01", "{table}": "tb_abt_nbo"}
	querynova := formatQuery(query, params)
	fmt.Printf(querynova)
}
