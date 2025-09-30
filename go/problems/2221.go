package problems

func triangularSum2221(nums []int) int {
	for m := len(nums) - 1; m > 0; m-- {
		for j := range m {
			nums[len(nums)-1-j] += nums[len(nums)-j-2]
			nums[len(nums)-1-j] %= 10
		}
	}

	return nums[len(nums)-1]
}
