package main


type TreeNode struct {
	Val    int
	Left   *TreeNode
	Right  *TreeNode
}

type ListNode struct {
	Val    int
	Next   *ListNode
}


func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
