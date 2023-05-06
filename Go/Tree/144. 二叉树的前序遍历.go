package main

import (
	"container/list"
	"fmt"
)

//type TreeNode struct {
//	Val   int
//	Left  *TreeNode
//	Right *TreeNode
//}

func NewTreeNode(val int) *TreeNode {
	return &TreeNode{Val: val}
}

// 递归法
func preOrderTraversalWithRecv(root *TreeNode) (res []int) {
	var traversal func(node *TreeNode)
	traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		res = append(res, node.Val)
		traversal(node.Left)
		traversal(node.Right)
	}
	traversal(root)
	return res
}

// 迭代法
func preOrderTraversalWithIter(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	var (
		stack = list.New()
		node  *TreeNode
		res   []int
	)

	stack.PushBack(root)
	for stack.Len() > 0 {
		e := stack.Back()
		stack.Remove(e)
		if e.Value == nil {
			e = stack.Back()
			stack.Remove(e)
			node = e.Value.(*TreeNode)
			res = append(res, node.Val)
			continue
		}
		node = e.Value.(*TreeNode)
		if node.Right != nil {
			stack.PushBack(node.Right)
		}
		if node.Left != nil {
			stack.PushBack(node.Left)
		}
		stack.PushBack(node)
		stack.PushBack(nil)
	}
	return res
}

func main() {
	root := new(TreeNode)
	root.Left = &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 2}
	root.Left.Left = &TreeNode{Val: 3}
	root.Left.Right = &TreeNode{Val: 4}
	root.Right.Left = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 6}
	res := preOrderTraversalWithRecv(root)
	fmt.Println(res)
	res2 := preOrderTraversalWithRecv(root)
	fmt.Println(res2)
}
