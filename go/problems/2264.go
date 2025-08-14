package problems

func LargestGoodInteger(num string) string {
	r := byte(0)

	for i := 2; i < len(num); i++ {
		if num[i-2] == num[i-1] && num[i-1] == num[i] && num[i] > r {
			r = num[i]
		}
	}

	if r == 0 {
		return ""
	}

	return string([]byte{r, r, r})

}
