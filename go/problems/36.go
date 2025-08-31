package problems

func isValidSudoku(board [][]byte) bool {
	var rows, cols, boxes [9]uint16

	if len(board) != 9 || len(board[0]) != 9 {
		return false
	}

	for i := range 9 {
		for j := range 9 {
			c := board[i][j]
			if c == '.' {
				continue
			}

			bit := uint16(1 << (c - '1'))
			box := 3*(i/3) + j/3

			if rows[i]&bit != 0 || cols[j]&bit != 0 || boxes[box]&bit != 0 {
				return false
			}

			rows[i] |= bit
			cols[j] |= bit
			boxes[box] |= bit
		}
	}
	return true
}
