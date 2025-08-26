package problems

func areaOfMaxDiagonal(dimensions [][]int) int {
	var l, w int

	prev := []int{0, 0, 0}
	for _, row := range dimensions {
		l, w = row[0], row[1]
		switch {
		case l*l+w*w > prev[2]:
			prev[0] = l
			prev[1] = w
			prev[2] = l*l + w*w
		case l*l+w*w == prev[2] && l*w > prev[0]*prev[1]:
			prev[0] = l
			prev[1] = w
		default:
		}

	}

	return prev[0] * prev[1]
}
