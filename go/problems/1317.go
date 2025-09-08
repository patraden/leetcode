package problems

func getNoZeroIntegers(n int) []int {
	var digit, bit, n1, n2 int

	if n < 10 {
		return []int{n - 1, 1}
	}

	p := 1
	for n > 0 {
		digit = n % 10
		digit -= bit

		if n < 10 {
			// last digit
			if digit != 0 {
				n1 += digit * p
			}
			break
		}

		if digit >= 2 {
			// enough to split between 2
			n1 += (digit - 1) * p
			n2 += 1 * p
			bit = 0
		} else {
			n1 += 8 * p
			n2 += (2 + digit) * p
			bit = 1
		}

		n /= 10
		p *= 10
	}

	return []int{n1, n2}
}
