package problems

func findSmallestInteger(nums []int, value int) int {
	counter := make([]int, value)
	for _, num := range nums {
		r := num % value
		if r < 0 {
			r += value
		}
		counter[r]++
	}

	res := 0
	i := 0
	for counter[i%value] > 0 {
		counter[i%value]--
		res++
		i++
	}

	return res
}
