package main

import (
	"fmt"
	"retriever/real"
	"time"
)

type Retriver interface {
	Get(url string) string
}

func download(r Retriver) string {
	return r.Get("https://www.baidu.com")
}

func main() {
	var r Retriver
	// r = &mock.Retriever{"this is a fack baidu"}
	r = &real.Retriver{
		UserAgent: "Mozilla/5.0",
		TimeOut:   time.Minute,
	}
	fmt.Println(download(r))
}
