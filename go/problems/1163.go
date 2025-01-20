package problems

func lastSubstring1163(s string) string {
	res, start := 0, 0
	prev := -1

	for i, r := range s {
		// any bigger symbol
		if r > rune(s[start]) {
			start = i
			res = i
		}

		if r == rune(s[start]) && prev > -1 && rune(s[prev]) != r {
			// check the length of the last interval - shorter wins
			if start != res && s[res+i-start] < s[i] {
				res = start
			}
			start = i
		}
		prev = i

		// current res is optimal
		if res == start {
			continue
		}

		d := i - start
		if res+d < start {
			if s[res+d] < s[i] {
				res = start
			} else if s[res+d] > s[i] {
				start = res
			}
		}
	}

	return s[res:]
}
