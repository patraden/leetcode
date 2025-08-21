package problems

func numSubmat(mat [][]int) int {
	n, m := len(mat), len(mat[0])

	// transform to row based histogram
	for i := range n {
		for j := range m {
			if mat[i][j] == 1 && i > 0 {
				mat[i][j] = mat[i-1][j] + 1
			}
		}
	}

	res := 0
	zdp := make([]int, m)

	for _, row := range mat {
		dp := zdp
		stack := []int{}
		for i, num := range row {
			// get prev <= num
			for len(stack) > 0 && row[stack[len(stack)-1]] > num {
				stack = stack[:len(stack)-1]
			}

			val := 0
			prev, j := 0, -1
			if len(stack) > 0 {
				j = stack[len(stack)-1]
				prev = dp[j]
			}

			val += prev
			val += (i - j) * num
			dp[i] = val

			res += val

			stack = append(stack, i)
		}
	}

	return res
}
