package problems

import "slices"

func triangleNumber611(nums []int) int {
	slices.Sort(nums)
	res := 0
	n := len(nums)
	for i := n - 1; i >= 2; i-- {

		// optimization
		if nums[0]+nums[1] > nums[i] {
			res += (i + 1) * i * (i - 1) / 6
			break
		}

		// optimization
		if nums[i-2]+nums[i-1] <= nums[i] {
			continue
		}

		l, r := 0, i-1
		for l < r {
			s := nums[l] + nums[r]
			if s > nums[i] {
				res += r - l
				r--
			} else {
				l++
			}
		}
	}

	return res
}
