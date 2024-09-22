package problems

import (
	"math"
)

func treeCounter(n int) func(int) int {
	maxDepth := int(math.Log10(float64(n))) + 1
	defaultTreeSize := map[int]int{}
	count := 1
	for i := 1; i <= maxDepth; i++ {
		defaultTreeSize[i] = count
		count *= 10
		count += 1
	}

	return func(prefix int) int {
		depth := int(math.Log10(float64(prefix))) + 1
		pow := int(math.Pow(float64(10), float64((maxDepth - depth))))
		lo := prefix * pow
		hi := (prefix+1)*pow - 1
		res := defaultTreeSize[maxDepth-depth+1]
		if n < lo {
			res -= hi - lo + 1
		} else if n < hi {
			res -= (hi - n)
		}
		return res
	}
}

func findKthNumber440(n int, k int) int {
	if n < 10 {
		return k
	}

	counter := treeCounter(n)
	prefix := 0

	for {
		d := 0
		if prefix == 0 {
			d = 1
		}
		for d <= 9 {
			if k-counter(prefix+d) > 0 {
				k -= counter(prefix + d)
			} else {
				k -= 1
				if k == 0 {
					return prefix + d
				}
				prefix += d
				prefix *= 10
				break
			}
			d += 1
		}
	}

}
