package problems

import (
	"slices"
)

func sortMatrix3446(grid [][]int) [][]int {
	n := len(grid)
	if n < 2 {
		return grid
	}

	for k := range n {
		i, j := k, 0
		d := make([]int, 0, n-k)
		for i < n && j < n {
			d = append(d, grid[i][j])
			i++
			j++
		}

		slices.SortFunc(d, func(a, b int) int { return b - a })

		i, j = k, 0
		m := 0
		for i < n && j < n {
			grid[i][j] = d[m]
			i++
			j++
			m++
		}
	}

	for k := n - 1; k > 0; k-- {
		i := 0
		j := k
		d := make([]int, 0, n-k)
		for i < n && j < n {
			d = append(d, grid[i][j])
			i++
			j++
		}

		slices.Sort(d)

		i, j = 0, k
		m := 0
		for i < n && j < n {
			grid[i][j] = d[m]
			i++
			j++
			m++
		}
	}

	return grid
}
