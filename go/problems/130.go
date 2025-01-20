package problems

func solve130(board [][]byte) {

	stack := [][2]int{}
	n, m := len(board), len(board[0])

	if n < 3 || m < 3 {
		return
	}

	// left column
	for i := 0; i < n; i++ {
		if board[i][0] == 'O' {
			stack = append(stack, [2]int{i, 0})
		}
	}

	// right column
	for i := 0; i < n; i++ {
		if board[i][m-1] == 'O' {
			stack = append(stack, [2]int{i, m - 1})
		}
	}

	// top row
	for j := 1; j < m-1; j++ {
		if board[0][j] == 'O' {
			stack = append(stack, [2]int{0, j})
		}
	}

	// bottom row
	for j := 1; j < m-1; j++ {
		if board[n-1][j] == 'O' {
			stack = append(stack, [2]int{n - 1, j})
		}
	}

	// dfs
	for len(stack) > 0 {

		p := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if board[p[0]][p[1]] == 'O' {
			board[p[0]][p[1]] = 'V'
			for _, c := range [][2]int{
				{p[0] + 1, p[1]},
				{p[0] - 1, p[1]},
				{p[0], p[1] + 1},
				{p[0], p[1] - 1},
			} {
				if c[0] >= 0 &&
					c[0] < n &&
					c[1] >= 0 &&
					c[1] < m && board[c[0]][c[1]] == 'O' {
					stack = append(stack, c)
				}
			}
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if board[i][j] != 'V' {
				board[i][j] = 'X'
			} else {
				board[i][j] = 'O'
			}
		}
	}
}
