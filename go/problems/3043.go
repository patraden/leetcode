package problems

import (
	"leetcode/datastructures/trie"
	"strconv"
)

func longestCommonPrefix(arr1 []int, arr2 []int) int {

	root := trie.NewTrieNode()
	for _, num := range arr1 {
		strNum := strconv.Itoa(num)
		root.Add(strNum)
	}

	res := 0
	for _, num := range arr2 {
		node := root
		for i, r := range strconv.Itoa(num) {
			if v, ok := node.Alphabet[r]; ok {
				node = v
				res = max(res, i+1)
			} else {
				break
			}
		}
	}

	return res
}
