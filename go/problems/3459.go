package problems

func walkDiag(i, j int, dir [2]int, grid, memo [][]int) int {
	prev := -1
	sfx, pfx, res := 0, 0, 0

	for i > -1 && j > -1 && i < len(grid) && j < len(grid[0]) {
		// prefix
		switch {
		case grid[i][j] == 1:
			pfx = 1
		case grid[i][j]+prev == 3, pfx > 0 && grid[i][j]+prev == 2:
			pfx++
		default:
			pfx = 0
		}

		if pfx > 0 {
			res = max(res, pfx+memo[i][j])
		}

		// suffix
		switch {
		case grid[i][j] != 1 && grid[i][j]+prev == 2:
			sfx++
		default:
			sfx = 0
		}

		memo[i][j] = sfx
		prev = grid[i][j]
		i += dir[0]
		j += dir[1]
	}

	return res
}

func lenOfVDiagonal(grid [][]int) int {
	n, m := len(grid), len(grid[0])

	dirs := [5][2]int{
		{-1, 1},  // ↗
		{1, 1},   // ↘
		{1, -1},  // ↙
		{-1, -1}, // ↖
		{-1, 1},  // ↗
	}

	memo := make([][]int, n)
	for i := range len(grid) {
		memo[i] = make([]int, m)
	}

	res := 0
	for d, dir := range dirs {
		switch d % 4 {
		case 0: // ↗
			for j := m - 1; j > 0; j-- { // bot(r->l)
				res = max(res, walkDiag(n-1, j, dir, grid, memo))
			}
			for i := n - 1; i > -1; i-- { // left(b->t)
				res = max(res, walkDiag(i, 0, dir, grid, memo))
			}
		case 1: // ↘
			for j := range m { // top(l->r)
				res = max(res, walkDiag(0, j, dir, grid, memo))
			}
			for i := 1; i < n; i++ { // left(t->b)
				res = max(res, walkDiag(i, 0, dir, grid, memo))
			}
		case 2: // ↙
			for j := m - 1; j >= 0; j-- { // top(r->l)
				res = max(res, walkDiag(0, j, dir, grid, memo))
			}
			for i := 1; i < n; i++ { // right(t->b)
				res = max(res, walkDiag(i, m-1, dir, grid, memo))
			}
		case 3: // ↖
			for j := 0; j < m-1; j++ { // bot(l->r)
				res = max(res, walkDiag(n-1, j, dir, grid, memo))
			}
			for i := n - 1; i > -1; i-- { // right(b->t)
				res = max(res, walkDiag(i, m-1, dir, grid, memo))
			}
		default:
		}
	}

	return res
}
