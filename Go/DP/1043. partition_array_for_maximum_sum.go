package main

import "fmt"

func maxSumAfterPartitioning(arr []int, k int) int {
	n := len(arr)
	f := make([]int, k)
	for i := range arr {
		res := 0
		for j, mx := i, 0;j > i - k && j >= 0; j-- {
			mx = max(mx, arr[j])
			res = max(res, f[j % k] + (i - j + 1)* mx)
		}
		f[(i + 1) % k] = res
	}
	return f[n % k]
}

//func max(a, b int) int {
//	if a < b {
//		return b
//	}
//	return a
//}

func main() {
	arr := []int{1, 15, 7, 9, 2, 5, 10}
	res := maxSumAfterPartitioning(arr, 3)
	fmt.Println(res)
}