package main

import "fmt"

// 二叉搜索树：指一棵空树或者具有以下性质的二叉树：
// 1. 若任意节点的左子树不空，则左子树所有节点的值均小于它的根节点的值；
// 2. 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
// 3. 任意节点的左、右子树也分别为二叉搜索树；
// 4. 没有键值相等的节点。

type TreeNode struct {
	Val    int
	Left   *TreeNode
	Right  *TreeNode
}


func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}

	root := len(nums) / 2
	Root := &TreeNode{
		nums[root],
		sortedArrayToBST(nums[:root]),
		sortedArrayToBST(nums[root + 1:]),
	}

	return Root
}

func preOrderTraversal(root *TreeNode) (res []int) {
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


func main() {
	node := sortedArrayToBST([]int{-10, -3, 0, 5, 9})
	fmt.Println(preOrderTraversal(node))
}