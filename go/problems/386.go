package problems

func lexicalOrder386(n int) []int {
	res := []int{}
	stack := []int{9, 8, 7, 6, 5, 4, 3, 2, 1}

	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if v <= n {
			res = append(res, v)
			for i := 9; i >= 0; i-- {
				w := v*10 + i
				if w <= n {
					stack = append(stack, w)
				}
			}
		}
	}

	return res

}
