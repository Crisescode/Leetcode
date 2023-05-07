package main

import (
	"fmt"
	"math"
)

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func isValidBST(root *TreeNode) bool {
	pre := math.MinInt
	var traversal func(node *TreeNode) bool

	traversal = func(node *TreeNode) bool {
		if node == nil {
			return true
		}

		if traversal(node.Left) || node.Val < pre {
			return false
		}
		pre = node.Val
		return traversal(node.Right)
	}
	return traversal(root)
}

func main() {
	root := new(TreeNode)
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 2}
	root.Left.Left = &TreeNode{Val: 3}
	root.Left.Right = &TreeNode{Val: 4}
	root.Right.Left = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 6}
	fmt.Println(isValidBST(root))
}
