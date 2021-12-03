package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	f, err := os.Open("01/input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	count := 0
	var prev int = 0
	i := 0

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		v, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err == nil && i > 0 && prev < v && v > 0 {
			count++
		}
		prev = v
		i++
	}

	fmt.Println(count)
}
