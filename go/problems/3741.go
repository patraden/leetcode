package problems

func minimumDistance(nums []int) int {
	res := -1
	m := map[int][]int{}

	for i, num := range nums {
		m[num] = append(m[num], i)
	}

	for k := range m {
		if len(m[k]) < 3 {
			continue
		}

		i := 0
		for i+2 < len(m[k]) {
			if res == -1 {
				res = (m[k][i+2] - m[k][i]) * 2
				continue

			}
			res = min(res, (m[k][i+2]-m[k][i])*2)
			i++
		}
	}

	return res
}
