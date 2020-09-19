package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
)

func main() {
	resqust, err : = http.NewRequest(http.MethodGet, "https://www.baidu.com", nil)
	resqust

	resp, err := http.Get("https://www.baidu.com")
	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	s, err := httputil.DumpResponse(resp, true)

	if err != nil {
		panic(err)
	}

	fmt.Printf("%s\n", s)
}
