package problems

func zeroFilledSubarray2348(nums []int) int64 {
	var cnt, streak int64 = 0, 0
	for _, num := range nums {
		if num == 0 {
			streak++
			cnt += streak
		} else {
			streak = 0
		}
	}
	return cnt
}
