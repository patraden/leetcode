package problems

func longestSubarray1493(nums []int) int {
	res := 0
	p := 0
	w := 0
	exists := false

	for i, num := range nums {
		if num == 0 {
			for p < i && nums[p] != 0 && exists {
				w--
				p++
			}

			if exists {
				p++
			}

			exists = true
		} else {
			w++
		}

		res = max(res, w)

	}

	if !exists {
		return len(nums) - 1
	}

	return res

}
