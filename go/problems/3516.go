package problems

func findClosest(x int, y int, z int) int {
	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	switch {
	case abs(x-z) < abs(y-z):
		return 1
	case abs(y-z) < abs(x-z):
		return 2
	default:
		return 0
	}
}
