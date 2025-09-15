package problems

import (
	"strings"
)

func canBeTypedWords(text string, brokenLetters string) int {
	res := 0

	h := make(map[rune]struct{})
	for _, r := range brokenLetters {
		h[r] = struct{}{}
	}

	for w := range strings.SplitSeq(text, " ") {
		ok := true
		for _, r := range w {
			if _, exists := h[r]; exists {
				ok = false
				break
			}
		}
		if ok {
			res++
		}
	}

	return res
}
