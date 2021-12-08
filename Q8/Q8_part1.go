package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	f, err := os.Open("Q8_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()

	count := 0

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		// do something with a line
		v := strings.Split(scanner.Text(), "|")
		v = strings.Split(v[1], " ")
		for i := 1; i < len(v); i++ {
			for _, x := range []int{2, 4, 3, 7} {
				if x == len(v[i]) {
					count++
				}
			}
		}
	}

	fmt.Println(count)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
