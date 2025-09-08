package problems

func getNoZeroIntegers(n int) []int {
	var digit, bit, n1, n2 int

	if n < 10 {
		return []int{n - 1, 1}
	}

	d := 1
	for n > 0 {
		digit = n % 10

		if n < 10 {
			// last digit
			digit -= bit
			if digit != 0 {
				n1 += digit * d
			}
			break
		}

		digit -= bit
		if digit >= 2 {
			// enough to split between 2
			n1 += (digit - 1) * d
			n2 += 1 * d
			bit = 0
		} else {
			n1 += 8 * d
			n2 += (2 + digit) * d
			bit = 1
		}

		n /= 10
		d *= 10
	}

	return []int{n1, n2}
}
