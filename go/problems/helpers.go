package problems

import (
	"leetcode/datastructures/binarytree"
	"leetcode/datastructures/trie"
)

type TreeNode = binarytree.TreeNode
type TrieNode = trie.TrieNode

func abs(a int, b int) int {
	if a < b {
		return b - a
	}
	return a - b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
