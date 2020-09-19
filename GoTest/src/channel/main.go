package main

import (
	"fmt"
	"time"
)

func worker(id int, c chan int) {
	for n := range c {
		fmt.Printf("worker %d received %c\n", id, n)
	}
}

func createWoker(id int) chan int {
	c := make(chan int)
	go worker(id, c)
	return c
}

func chanDemo() {
	var channels [10]chan int
	for i := 0; i < 10; i++ {
		channels[i] = createWoker(i)
	}

	for i := 0; i < 10; i++ {
		channels[i] <- 'a' + i
	}

	for i := 0; i < 10; i++ {
		channels[i] <- 'A' + i
	}

	time.Sleep(1000 * time.Microsecond)
}

func bufferedChannel() {
	c := make(chan int, 3)
	go worker(0, c)
	c <- 'a'
	c <- 'b'
	c <- 'c'
	c <- 'd'
	time.Sleep(1000 * time.Microsecond)
}

func channelClose() {
	c := make(chan int, 3)
	go worker(0, c)
	c <- 'a'
	c <- 'b'
	c <- 'c'
	c <- 'd'
	time.Sleep(1000 * time.Microsecond)
}

func main() {
	// chanDemo()
	// bufferedChannel()
	channelClose()
}
