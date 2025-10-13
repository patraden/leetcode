package problems

func removeAnagrams2273(words []string) []string {
	res := make([]string, 0, len(words))
	for i := range len(words) {
		if i > 0 && isAnagram(words[i], words[i-1]) {
			continue
		}
		res = append(res, words[i])
	}
	return res
}

func isAnagram(s1, s2 string) bool {
	h := make(map[rune]int)
	for _, c := range s1 {
		h[c] = h[c] + 1
	}

	for _, c := range s2 {
		h[c] = h[c] - 1
	}

	for _, v := range h {
		if v != 0 {
			return false
		}
	}

	return true
}
