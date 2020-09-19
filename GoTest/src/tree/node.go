package main

import "fmt"

type treeNode struct {
	value       int
	left, right *treeNode
}

func createTreeNode(value int) *treeNode {
	return &treeNode{value: value}
}

func (node *treeNode) setValue(v int) {
	node.value = v
}

func (node treeNode) Print() {
	fmt.Println(node.value)
}

func main() {
	var root treeNode
	fmt.Println(root)
	root = treeNode{value: 4}
	root.left = &treeNode{}
	root.right = &treeNode{5, nil, nil}
	root.right.left = new(treeNode)
	root.left.right = createTreeNode(2)
	root.setValue(5)
	root.Print()
}
