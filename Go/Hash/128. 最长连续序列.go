package main

import "fmt"

func longestConsecutive(num []int) int {
	hashDict := map[int]int{}
	maxLength := 0

	for _, val := range num {
		if _, ok := hashDict[val]; ok {
			continue
		} else {
			left := getVal(val-1, hashDict)
			right := getVal(val+1, hashDict)

			curLength := left + right + 1
			if curLength > maxLength {
				maxLength = curLength
			}

			hashDict[val] = curLength
			hashDict[val-left] = curLength
			hashDict[val+right] = curLength
		}
	}

	return maxLength
}

func getVal(val int, hashD map[int]int) int {
	if _, ok := hashD[val]; ok {
		return hashD[val]
	} else {
		return 0
	}
}

func main() {
	res := longestConsecutive([]int{1, 0, 2, 5, 6, 7, 8})
	fmt.Println(res)
}
