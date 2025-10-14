package problems

func hasIncreasingSubarrays(nums []int, k int) bool {
	// [l;s)[s;r]

	var l, s int
	if k == 1 {
		return true
	}

	s = 1
	for s < len(nums) && nums[s] > nums[s-1] {
		s++
	}

	if s >= 2*k {
		return true
	}

	for r := s + 1; r < len(nums); r++ {
		if nums[r] <= nums[r-1] {
			l, s = s, r
		}
		if r-s+1 == 2*k {
			return true
		}

		if s-l >= k && r-s+1 >= k {
			return true
		}
	}

	return false
}
