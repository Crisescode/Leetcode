package main

import (
	"fmt"
	"math"
)

func maxProduct(nums []int) int {

	res := math.MinInt
	for i := 0; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			s := 1
			for p := i; p <= j; p++ {
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
	fmt.Print(maxProduct([]int{-2, 3, 1, 6, 0, -4, -8}))
}
