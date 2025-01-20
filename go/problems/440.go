package problems

import "math"

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
		lo, hi := prefix*pow, (prefix+1)*pow-1
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
		sd := 0
		if prefix == 0 {
			sd = 1
		}
		for d := sd; d <= 9; d++ {
			if k-counter(prefix+d) <= 0 {
				k -= 1
				if k == 0 {
					return prefix + d
				}
				prefix += d
				prefix *= 10
				break
			}
			k -= counter(prefix + d)
		}
	}

}
