package problems

func minimumDistance(nums []int) int {
	res := -1
	m := map[int][2]int{}

	for i, num := range nums {
		if _, ok := m[num]; !ok {
			m[num] = [2]int{-1, i}
			continue
		}

		v := m[num]
		if v[0] == -1 {
			v[0], v[1] = v[1], i
			m[num] = v
			continue
		}

		d := (i - v[0]) * 2
		if res == -1 || d < res {
			res = d
		}
		v[0], v[1] = v[1], i
		m[num] = v
	}

	return res
}
