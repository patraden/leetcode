package problems

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func MaxArea(height []int) int {
	l, r := 0, len(height)-1
	res, cur := 0, 0

	for l < r {

		cur = min(height[l], height[r]) * (r - l)

		if height[l] < height[r] {
			l += 1
		} else {
			r -= 1
		}

		res = -min(-cur, -res)
	}

	return res
}
