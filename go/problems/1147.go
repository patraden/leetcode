package problems

func longestDecomposition(text string) int {
	n := len(text)
	count := 0

	start := 0
	for end := 1; end <= n/2; end++ {
		if text[start:end] == text[n-end:n-start] {
			start = end
			count += 2
		}
	}

	if n%2 == 1 || start < n/2 {
		count += 1
	}

	return count
}
