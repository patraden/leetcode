package problems

const (
	mod = 1_000_000_007
)

func NumberOfWays(n int, x int) int {
	dp := [301]int{}
	dp[0] = 1
	dp[1] = 1

	i, p := 2, pow(2, x)
	ps := p + 1
	for p <= n {
		start := n
		if ps < n {
			start = ps
		}

		for v := start; v >= i; v-- {
			if v-p >= 0 {
				dp[v] += dp[v-p]
				dp[v] %= mod
			}
		}
		i++
		p = pow(i, x)
		ps += p
	}

	return dp[n]
}

func pow(b, p int) int {
	if p == 0 {
		return 1
	}

	res := pow(b*b, p/2)
	if p&1 == 1 {
		res *= b
	}

	return res
}
