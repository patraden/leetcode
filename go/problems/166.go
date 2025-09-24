package problems

import (
	"fmt"
	"strconv"
	"strings"
)

func fractionToDecimal(numerator int, denominator int) string {
	res := ""

	abs := func(a int) int {
		if a < 0 {
			return -a
		}
		return a
	}

	if numerator*denominator < 0 {
		res += "-"
	}
	numerator = abs(numerator)
	denominator = abs(denominator)

	res += strconv.Itoa(numerator / denominator)
	rem := numerator % denominator
	if rem == 0 {
		return res
	}

	rems := make(map[int]int)
	seq := []int{}
	idx := -1

	for rem > 0 {
		if _, ok := rems[rem]; ok {
			var prx, tail strings.Builder
			for _, v := range seq[:rems[rem]+1] {
				prx.WriteString(strconv.Itoa(v))
			}

			for _, v := range seq[rems[rem]+1:] {
				tail.WriteString(strconv.Itoa(v))
			}

			return fmt.Sprintf("%s.%s(%s)", res, prx.String(), tail.String())
		}

		rems[rem] = idx
		for rem < denominator {
			rem *= 10
			seq = append(seq, 0)
			idx++
		}

		seq[idx] = rem / denominator
		rem = rem % denominator
	}

	var t strings.Builder
	for _, v := range seq {
		t.WriteString(strconv.Itoa(v))
	}

	return fmt.Sprintf("%s.%s", res, t.String())
}
