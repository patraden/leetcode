package problems

func minimumDistance(nums []int) int {
	res := -1
	m := map[int][3]int{}

	for i, num := range nums {
		if _, ok := m[num]; !ok {
			m[num] = [3]int{-1, -1, i}
			continue
		}

		v := m[num]
		v[0], v[1], v[2] = v[1], v[2], i
		m[num] = v

		if v[0] == -1 {
			continue
		}

		if res == -1 {
			res = (v[2] - v[0]) * 2
			continue

		}
		res = min(res, (v[2]-v[0])*2)
	}

	return res
}
