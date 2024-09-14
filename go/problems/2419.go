package problems

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func LongestSubarray(nums []int) int {
	res := 0
	mx := 0
	for _, num := range nums {
		mx = max(mx, num)
	}

	count := 0
	for _, num := range nums {
		if num == mx {
			count += 1
		} else {
			count = 0
		}

		res = max(res, count)
	}
	return res
}
