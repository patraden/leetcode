package problems

func maximumEnergy3147(energy []int, k int) int {
	pref := make([]int, len(energy))

	res := -1001
	for i := len(energy) - 1; i > -1; i-- {
		if i+k < len(energy) {
			pref[i] += pref[i+k]
		}

		pref[i] += energy[i]

		res = max(res, pref[i])
	}

	return res
}
