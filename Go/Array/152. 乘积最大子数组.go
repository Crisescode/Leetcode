package main

import "fmt"

func maxProduct(nums []int) int {

	res := 0
	for i := 0; i < len(nums); i++ {
		for j := i; i < len(nums); i++ {
			s := 1
			for p := i; p < j; p++ {
				s *= nums[p]
			}

			if s > res {
				res = s
			}
		}
	}

	return res
}

func main() {
	fmt.Print(maxProduct([]int{2, 3, -2, 4}))
}
