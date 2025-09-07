package problems

func makeTheIntegerZero(num1 int, num2 int) int {
	k := 1
	for {
		x := int64(num1) - int64(num2)*int64(k)
		if x < int64(k) {
			return -1
		}
		if k >= bitCount(x) {
			return k
		}
		k++
	}
}

func bitCount(n int64) int {
	count := 0
	for n != 0 {
		count++
		n &= n - 1
	}
	return count
}
