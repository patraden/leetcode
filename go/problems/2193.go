package problems

func minMovesToMakePalindrome(s string) int {
	as := []byte(s)

	res := 0
	p1, p2 := 0, len(as)-1

	for p1 < p2 {
		if as[p1] == as[p2] {
			p1++
			p2--
			continue
		}

		p2c := p2 - 1
		for p2c > p1 && as[p2c] != as[p1] {
			p2c--
		}

		if p2c == p1 {
			as[p1], as[p1+1] = as[p1+1], as[p1]
			res++
			continue
		}

		for i := p2c; i < p2; i++ {
			as[i], as[i+1] = as[i+1], as[i]
			res++
		}
		p1++
		p2--
	}

	return res
}
