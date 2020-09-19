package mock

import "fmt"

type Retriever struct {
	Contenxt string
}

func (r *Retriever) Get(url string) string {
	return r.Contenxt
}

func (r *Retriever) Stringer() string {
	return fmt.Sprintf("Retriver: {Contents=%s}", r.Contenxt)
}
