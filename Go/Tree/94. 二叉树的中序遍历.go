package main

// 递归法
func inorderTraversal(root *TreeNode) []int {
	var (
		Traversal func(node *TreeNode)
		res       []int
	)

	Traversal = func(node *TreeNode) {
		if node == nil {
			return
		}
		Traversal(node.Left)
		res = append(res, node.Val)
		Traversal(node.Right)
	}
	Traversal(root)
	return res
}

// 迭代法
func inorderTraversal2(root *TreeNode) []int {

}
