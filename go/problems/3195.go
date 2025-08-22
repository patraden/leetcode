package problems

func minimumArea(grid [][]int) int {

	mni, mxi, mnj, mxj := -1, -1, -1, -1

	for i := range len(grid) {
		for j := range grid[0] {
			if grid[i][j] == 0 {
				continue
			}

			if mni == -1 {
				mni = i
				mxi = i
				mnj = j
				mxj = j
			} else if j > mxj {
				mxj = j
			} else if j < mnj {
				mnj = j
			}

			mxi = i
		}
	}

	return (mxi - mni + 1) * (mxj - mnj + 1)

}
