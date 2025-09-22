package problems

func maxFrequencyElements(nums []int) int {
	f := make([]int, 101)
	mx, cnt := 0, 0

	for _, num := range nums {
		f[num]++
		if f[num] > mx {
			cnt = 1
			mx = f[num]
			continue
		}

		if f[num] == mx {
			cnt++
		}
	}

	return mx * cnt
}
