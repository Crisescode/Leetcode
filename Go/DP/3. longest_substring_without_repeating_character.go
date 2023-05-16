package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	left, n := -1, len(s)
	res := 0
	window := make(map[byte]int, 0)

	for right := 0; right < n; right++ {
		ch := s[right]

		window[ch]++
		for window[ch] > 1 {
			left++
			window[s[left]]--
		}
		res = max(res, right-left)
	}
	return res
}

//func max(a, b int) int {
//	if a > b {
//		return a
//	}
//	return b
//}

func main() {
	res := lengthOfLongestSubstring("pwwkew")
	fmt.Println(res)
}
