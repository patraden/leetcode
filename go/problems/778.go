package problems

func swimInWater(grid [][]int) int {
	n, m := len(grid), len(grid[0])
	if n == 1 && m == 1 {
		return 0
	}

	visited := make([][]int, n)
	for i := range visited {
		visited[i] = make([]int, m)
	}

	generation := 0
	bfs := func(target int) bool {
		if grid[0][0] > target {
			return false
		}

		generation++

		q := NewQueue(n * m)
		q.Push([]int{0, 0})
		visited[0][0] = generation

		for !q.IsEmpty() {
			u := q.Pop()
			i, j := u[0], u[1]
			if i == n-1 && j == m-1 {
				return true
			}

			for _, d := range [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}} {
				ic, jc := i+d[0], j+d[1]
				if ic >= 0 && ic < n && jc >= 0 && jc < m && visited[ic][jc] < generation && grid[ic][jc] <= target {
					q.Push([]int{ic, jc})
					visited[ic][jc] = generation
				}
			}
		}

		return false
	}

	l, r := 0, 2500
	for l < r {
		m := (l + r) / 2
		if bfs(m) {
			r = m
		} else {
			l = m + 1
		}
	}

	return r
}
