package problems

func countWord(m map[rune]int, word string) int {
	for _, r := range word {
		if _, ok := m[r]; !ok {
			return 0
		}
	}
	return 1
}

func CountConsistentStrings(allowed string, words []string) int {
	var res int
	m := make(map[rune]int)
	runes := []rune(allowed)

	for i, r := range runes {
		m[r] = i
	}

	for _, word := range words {
		res += countWord(m, word)
	}

	return res
}
