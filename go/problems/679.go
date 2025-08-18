package problems

type Ratio = [2]int

func NewRatio(n, d int) Ratio {
	return Ratio{n, d}
}

func Mul(a, b Ratio) Ratio {
	return Ratio{a[0] * b[0], a[1] * b[1]}
}

func Div(a, b Ratio) Ratio {
	return Ratio{a[0] * b[1], a[1] * b[0]}
}

func Add(a, b Ratio) Ratio {
	return Ratio{a[0]*b[1] + b[0]*a[1], a[1] * b[1]}
}

func Sub(a, b Ratio) Ratio {
	return Ratio{a[0]*b[1] - b[0]*a[1], a[1] * b[1]}
}

func heapPermute(a []int, n int, res *[][]int) {
	if n == 1 {
		tmp := append([]int(nil), a...)
		*res = append(*res, tmp)
		return
	}
	for i := range n {
		heapPermute(a, n-1, res)
		if n%2 == 1 {
			a[0], a[n-1] = a[n-1], a[0]
		} else {
			a[i], a[n-1] = a[n-1], a[i]
		}
	}
}

func judgePoint24CalcStack(a, b, c, d Ratio, op1, op2, op3 int) bool {
	// (((a,b),c),d)
	var r1, r2, r3 Ratio

	r1 = judgePoint24CalcRatio(a, b, op1)
	r2 = judgePoint24CalcRatio(r1, c, op2)
	r3 = judgePoint24CalcRatio(r2, d, op3)

	if r1[1] != 0 && r2[1] != 0 && r3[1] != 0 && r3[0]%r3[1] == 0 && r3[0]/r3[1] == 24 {
		// fmt.Println("(((a,b),c),d)", a, b, c, d, op1, op2, op3)
		return true
	}

	// ((a,(b,c)),d)
	r1 = judgePoint24CalcRatio(b, c, op1)
	r2 = judgePoint24CalcRatio(a, r1, op2)
	r3 = judgePoint24CalcRatio(r2, d, op3)

	if r1[1] != 0 && r2[1] != 0 && r3[1] != 0 && r3[0]%r3[1] == 0 && r3[0]/r3[1] == 24 {
		// fmt.Println("((a,(b,c)),d)", a, b, c, d, op1, op2, op3)
		return true
	}

	// (a,((b,c),d))
	r1 = judgePoint24CalcRatio(b, c, op1)
	r2 = judgePoint24CalcRatio(r1, d, op2)
	r3 = judgePoint24CalcRatio(a, r2, op3)

	if r1[1] != 0 && r2[1] != 0 && r3[1] != 0 && r3[0]%r3[1] == 0 && r3[0]/r3[1] == 24 {
		// fmt.Println("(a,((b,c),d))", a, b, c, d, op1, op2, op3)
		return true
	}

	// (a,(b,(c,d)))
	r1 = judgePoint24CalcRatio(c, d, op1)
	r2 = judgePoint24CalcRatio(b, r1, op2)
	r3 = judgePoint24CalcRatio(a, r2, op3)

	if r1[1] != 0 && r2[1] != 0 && r3[1] != 0 && r3[0]%r3[1] == 0 && r3[0]/r3[1] == 24 {
		// fmt.Println("(a,(b,(c,d)))", a, b, c, d, op1, op2, op3)
		return true
	}

	// ((a, b),(c, d))
	r1 = judgePoint24CalcRatio(a, b, op1)
	r2 = judgePoint24CalcRatio(c, d, op2)
	r3 = judgePoint24CalcRatio(r1, r2, op3)

	if r1[1] != 0 && r2[1] != 0 && r3[1] != 0 && r3[0]%r3[1] == 0 && r3[0]/r3[1] == 24 {
		// fmt.Println("((a, b),(c, d))", a, b, c, d, op1, op2, op3, r1, r2, r3)
		return true
	}

	return false

}

func judgePoint24CalcRatio(a Ratio, b Ratio, op int) Ratio {
	switch op {
	case 10:
		return Add(a, b)
	case 11:
		return Sub(a, b)
	case 12:
		return Mul(a, b)
	case 13:
		return Div(a, b)
	default:
		return Ratio{}
	}

}

func judgePoint24Calc(perm []int) bool {
	ops := [4]int{10, 11, 12, 13}

	for _, op1 := range ops {
		for _, op2 := range ops {
			for _, op3 := range ops {
				a := NewRatio(perm[0], 1)
				b := NewRatio(perm[1], 1)
				c := NewRatio(perm[2], 1)
				d := NewRatio(perm[3], 1)
				if judgePoint24CalcStack(a, b, c, d, op1, op2, op3) {
					return true
				}
			}
		}
	}

	return false

}

func judgePoint24(cards []int) bool {

	perms := make([][]int, 0, 24)
	heapPermute(cards, 4, &perms)

	for _, p := range perms {

		if judgePoint24Calc(p) {
			return true
		}
	}

	return false
}
