package problems

import "slices"

func largestPerimeter976(nums []int) int {
	slices.Sort(nums)

	for i := len(nums) - 1; i > 1; i-- {
		if nums[i-1]+nums[i-2] > nums[i] {
			return nums[i-1] + nums[i-2] + nums[i]
		}
	}

	return 0
}
