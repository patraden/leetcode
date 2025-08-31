package problems

func precomputeCandidates() [512][]byte {
	var candidates [512][]byte

	for mask := range 512 {
		for i := range 9 {
			if (mask>>i)&1 == 0 {
				candidates[mask] = append(candidates[mask], byte(i))
			}
		}
	}

	return candidates
}

func backtrack(board [][]byte, rows, cols, boxes *[9]uint16, candidates *[512][]byte) bool {
	var mi, mj, mn, mbox int
	mn = 10

	for i := range 9 {
		for j := range 9 {
			c := board[i][j]
			if c != '.' {
				continue
			}

			box := 3*(i/3) + j/3
			mask := rows[i] | cols[j] | boxes[box]
			if len(candidates[mask]) == 0 {
				// bad case
				return false
			}

			if len(candidates[mask]) < mn {
				mi, mj, mbox = i, j, box
				mn = len(candidates[mask])
			}
		}
	}

	if mn == 10 {
		return true // no empty cells → solved
	}

	mask := rows[mi] | cols[mj] | boxes[mbox]
	for _, idx := range candidates[mask] {
		bit := uint16(1 << idx)

		// place digit
		board[mi][mj] = '1' + idx
		rows[mi] |= bit
		cols[mj] |= bit
		boxes[mbox] |= bit

		// recurse
		if backtrack(board, rows, cols, boxes, candidates) {
			return true
		}

		// undo
		board[mi][mj] = '.'
		rows[mi] &^= bit
		cols[mj] &^= bit
		boxes[mbox] &^= bit
	}

	return false
}

func solveSudoku(board [][]byte) {
	var rows, cols, boxes [9]uint16
	candidates := precomputeCandidates()

	// initialize masks
	for i := range 9 {
		for j := range 9 {
			c := board[i][j]
			if c == '.' {
				continue
			}
			bit := uint16(1 << (c - '1'))
			box := 3*(i/3) + j/3
			rows[i] |= bit
			cols[j] |= bit
			boxes[box] |= bit
		}
	}

	backtrack(board, &rows, &cols, &boxes, &candidates)

}
