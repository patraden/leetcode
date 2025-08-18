package problems

func new21Game(n int, k int, maxPts int) float64 {
	dp := make([]float64, n+1)
	dp[0] = 1.0

	s := 0.0
	if k > 0 {
		s = 1.0
	}

	res := 0.0
	if k == 0 {
		res = 1.0
	}

	for i := 1; i <= n; i++ {
		dp[i] = s / float64(maxPts)

		if i < k {
			s += dp[i]
		}

		if i >= maxPts && i-maxPts < k {
			s -= dp[i-maxPts]
		}

		if i >= k {
			res += dp[i]
		}
	}

	return res
}
