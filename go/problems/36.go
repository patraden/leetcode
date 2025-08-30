package problems

func isValidSudoku(board [][]byte) bool {
	points := [9][2]int{
		{2, 2},
		{2, 5},
		{2, 8},
		{5, 2},
		{5, 5},
		{5, 8},
		{8, 2},
		{8, 5},
		{8, 8},
	}

	var idx byte
	for i := range len(board) {
		check := [9]int{}
		for j := range len(board[0]) {
			if board[i][j] == byte('.') {
				continue
			}
			idx = board[i][j] - byte('1')
			if check[idx] > 0 {
				return false
			}
			check[idx]++
		}
	}

	for j := range len(board[0]) {
		check := [9]int{}
		for i := range len(board) {
			if board[i][j] == byte('.') {
				continue
			}
			idx = board[i][j] - byte('1')
			if check[idx] > 0 {
				return false
			}
			check[idx]++
		}
	}

	for _, point := range points {
		check := [9]int{}
		for k := point[0] - 2; k <= point[0]; k++ {
			for m := point[1] - 2; m <= point[1]; m++ {
				if board[k][m] == byte('.') {
					continue
				}
				idx = board[k][m] - byte('1')
				if check[idx] > 0 {
					return false
				}
				check[idx]++
			}
		}
	}

	return true
}
