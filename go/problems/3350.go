package problems

func maxIncreasingSubarrays(nums []int) int {
	ans := 0
	p, c := 0, 1

	for i := 1; i < len(nums); i++ {
		if nums[i] <= nums[i-1] {
			p = c
			c = 1
		} else {
			c++
		}

		ans = max(ans, min(c, p))
		ans = max(ans, c/2)
	}

	return ans
}
