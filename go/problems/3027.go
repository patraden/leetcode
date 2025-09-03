package problems

import "sort"

const minY = -1_000_0000_000

func numberOfPairs3027(points [][]int) int {
	res := 0

	sort.Slice(points, func(i, j int) bool {
		if points[i][0] != points[j][0] {
			return points[i][0] < points[j][0]
		}
		return points[i][1] > points[j][1]
	})

	for i := range points {
		mxy := minY
		for j := i + 1; j < len(points); j++ {
			if points[j][1] <= points[i][1] && (mxy == minY || points[j][1] > mxy) {
				mxy = points[j][1]
				res++
			}
		}
	}

	return res
}
