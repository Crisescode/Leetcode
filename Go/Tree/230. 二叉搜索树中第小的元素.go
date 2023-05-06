package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
	var (
		sorted    []int
		traversal func(node *TreeNode)
	)

	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		traversal(node.Left)
		sorted = append(sorted, node.Val)
		traversal(node.Right)
	}
	traversal(root)
	return sorted[k-1]
}

func main() {
	root := new(TreeNode)
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 2}
	root.Left.Left = &TreeNode{Val: 3}
	root.Left.Right = &TreeNode{Val: 4}
	root.Right.Left = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 6}
	res := kthSmallest(root, 3)
	fmt.Println(res)
}
