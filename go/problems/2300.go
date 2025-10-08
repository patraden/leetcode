package problems

import (
	"sort"
)

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Ints(potions)

	bs := func(spell int) int {
		var m int
		l, r := 0, len(potions)
		for l < r {
			m = (l + r) / 2
			if int64(spell)*int64(potions[m]) < success {
				l = m + 1
			} else {
				r = m
			}
		}

		return l
	}

	res := make([]int, len(spells))
	for i, spell := range spells {
		m := bs(spell)
		res[i] = len(potions) - m
	}

	return res

}
