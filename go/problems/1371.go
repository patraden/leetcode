package problems

func FindTheLongestSubstring(s string) int {
	masks := map[rune]int{
		'a': 1,
		'e': 2,
		'i': 4,
		'o': 8,
		'u': 16,
	}

	h := map[int]int{0: -1}
	res, mask := 0, 0

	for i, c := range s {
		mask ^= masks[c]
		if j, ok := h[mask]; ok {
			if i-j > res {
				res = i - j
			}
		} else {
			h[mask] = i
		}
	}

	return res

}
