package problems

func minimumDistance(nums []int) int {
	res := -1
	m := map[int][]int{}

	for i, num := range nums {
		m[num] = append(m[num], i)
		if len(m[num]) < 3 {
			continue
		}

		n := len(m[num])
		if res == -1 {
			res = (m[num][n-1] - m[num][n-3]) * 2
			continue

		}
		res = min(res, (m[num][n-1]-m[num][n-3])*2)
	}

	return res
}
