package main

import (
	"fmt"
	"leetcode/problems"
)

func main() {
	// allowed := "ab"
	// words := []string{"ad", "bd", "aaab", "baa", "badab"}
	// allowed := "abc"
	// words := []string{"a", "b", "c", "ab", "ac", "bc", "abc"}
	allowed := "cad"
	words := []string{"cc", "acd", "b", "ba", "bac", "bad", "ac", "d"}
	res := problems.CountConsistentStrings(allowed, words)
	fmt.Println(res)
}
