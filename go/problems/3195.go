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
			} else {
				mxi = i
				if j > mxj {
					mxj = j
				}
				if j < mnj {
					mnj = j
				}
			}
		}
	}

	return (mxi - mni + 1) * (mxj - mnj + 1)

}
