package problems

func XorQueries(arr []int, queries [][]int) []int {

	res := make([]int, len(queries))
	pr := make([]int, len(arr))
	p := 0

	for i, num := range arr {
		p ^= num
		pr[i] = p
	}

	cur := 0

	for i, t := range queries {
		l, r := t[0], t[1]

		cur = pr[r]

		if l > 0 {
			cur ^= pr[l-1]
		}

		res[i] = cur
	}

	return res

}
