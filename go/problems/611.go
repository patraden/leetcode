package problems

import (
	"sort"
)

func triangleNumber611(nums []int) int {
	if len(nums) < 3 {
		return 0
	}

	// find index of the left most num
	// which is greater than or equal to target
	leftMost := func(nums []int, start, target int) int {
		l := start
		r := len(nums)
		for l < r {
			m := (l + r) / 2
			if nums[m] < target {
				l = m + 1
			} else {
				r = m
			}
		}

		return l
	}

	sort.Ints(nums)

	res := 0
	for p1 := 0; p1 < len(nums)-2; p1++ {
		for p2 := p1 + 1; p2 < len(nums)-1; p2++ {
			idx := leftMost(nums, p2+1, nums[p1]+nums[p2])
			res += idx - p2 - 1
		}
	}

	return res
}
