package problems

func findDiagonalOrder(mat [][]int) []int {
	var i, j, idx int
	var odd bool

	n, m := len(mat), len(mat[0])
	res := make([]int, n*m)

	for i < n && j < m && idx < n*m {
		res[idx] = mat[i][j]

		odd = (i+j)%2 == 1

		switch {
		case i == n-1 && odd:
			j++
		case j == m-1 && !odd:
			i++
		case i == 0 && !odd:
			j++
		case j == 0 && odd:
			i++
		case !odd:
			i--
			j++
		case odd:
			i++
			j--
		default:
		}

		idx++
	}

	return res
}
