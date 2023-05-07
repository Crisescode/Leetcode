package main

import "fmt"

// 暴力法
func subarraySum(num []int, k int) int {
	count := 0
	for i := 0; i < len(num); i++ {
		for j := i; j < len(num); j++ {
			sum := 0
			for q := i; q <= j; q++ {
				sum += num[q]
			}

			if sum == k {
				count++
			}
		}
	}
	return count
}

//

func subarraySum2(num []int, k int) int {
	count := 0
	hash := map[int]int{0: 1}
	preSum := 0

	for i := 0; i < len(num); i++ {
		preSum += num[i]
		if hash[preSum-k] > 0 {
			count += hash[preSum-k]
		}
		hash[preSum]++
	}

	return count
}

func main() {
	//fmt.Println(subarraySum([]int{1, 2, 3, 4, 2, 5, 1, 6}, 6))
	fmt.Println(subarraySum2([]int{0, 1, 2, 3}, 0))
}
