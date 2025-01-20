package problems

import (
	"leetcode/datastructures/trie"
	"math"
)

func minExtraChar2707(s string, dictionary []string) int {

	root := trie.NewTrieNode()
	for _, word := range dictionary {
		root.Add(word)
	}

	dp := make([]int, len(s)+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = math.MaxInt
	}
	dp[0] = 0

	for i := 1; i < len(dp); i++ {
		node := root
		for j := i; j-1 < len(s); j++ {
			r := rune(s[j-1])
			v, ok := node.Alphabet[r]
			if !ok {
				break
			}
			node = v
			if node.IsTerminal {
				dp[j] = min(dp[i-1], dp[j])
			}
		}
		dp[i] = min(dp[i], dp[i-1]+1)
	}

	return dp[len(dp)-1]

}
