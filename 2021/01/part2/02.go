package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	f, err := os.Open("01/part2/input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	var lastSum int = 0
	var windowSize int = 3
	var count int = 0

	scanner := bufio.NewScanner(f)
	var arr []int
	for scanner.Scan() {
		line, _ := strconv.ParseInt(scanner.Text(), 10, 64)
		arr = append(arr, int(line))
	}

	//first window
	var i int
	for i = 0; i < windowSize; i++ {
		lastSum += arr[i]
	}

	//window sum of indices 0,1,2 starting point
	//(sum of indices 0,1,2) + (indice 3 - indice[3 - 3]) = sum of indices 1,2,3
	//(sum of indices 1,2,3) + (indice 4 - indice[4 - 3]) = sum of indices 2,3,4
	//etc
	windowSum := lastSum
	for i = windowSize; i < int(len(arr)); i++ {
		windowSum += arr[i] - arr[i-windowSize]
		if windowSum > lastSum {
			count++
		}
		lastSum = windowSum
	}

	fmt.Println(count)
}
