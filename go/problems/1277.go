package problems

func countSquares(matrix [][]int) int {
	res, mn := 0, 0
	for j := range len(matrix) {
		for i := range len(matrix[0]) {
			if matrix[j][i] == 0 {
				continue
			}

			if j >= 1 && i >= 1 {
				mn = min(matrix[j-1][i-1], min(matrix[j-1][i], matrix[j][i-1]))
				matrix[j][i] = mn + 1
			}

			res += matrix[j][i]
		}
	}

	return res
}
