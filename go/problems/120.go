package problems

import "math"

func minimumTotal120(triangle [][]int) int {
	for lvl, nums := range triangle {
		for i := range nums {
			if lvl == 0 {
				continue
			}

			switch {
			case i > 0 && i < len(triangle[lvl-1]):
				triangle[lvl][i] += min(triangle[lvl-1][i], triangle[lvl-1][i-1])
			case i == 0:
				triangle[lvl][i] += triangle[lvl-1][i]
			case i == len(nums)-1:
				triangle[lvl][i] += triangle[lvl-1][i-1]
			}

		}
	}

	res := math.MaxInt
	for _, num := range triangle[len(triangle)-1] {
		res = min(res, num)
	}

	return res
}
