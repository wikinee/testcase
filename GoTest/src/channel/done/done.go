package main

import (
	"fmt"
	"sync"
)

func doWorker(id int, c chan int, wg *sync.WaitGroup) {
	for n := range c {
		fmt.Printf("worker %d received %c\n", id, n)
		wg.Done()
	}
}

type woker struct {
	in chan int
	wg *sync.WaitGroup
}

func createWoker(id int, wg *sync.WaitGroup) woker {
	w := woker{
		in: make(chan int),
		wg: wg,
	}
	go doWorker(id, w.in, wg)
	return w
}

func chanDemo() {
	var wg sync.WaitGroup
	var works [10]woker
	for i := 0; i < 10; i++ {
		works[i] = createWoker(i, &wg)
	}

	wg.Add(20)
	for i, worker := range works {
		worker.in <- 'a' + i
	}

	for i, worker := range works {
		worker.in <- 'A' + i
	}

	wg.Wait()
}

func main() {
	chanDemo()
}
