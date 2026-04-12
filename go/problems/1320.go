package problems

func MinimumDistance1320(word string) int {
	dist := func(n, m int) int {
		xn, yn := n/6, n%6
		xm, ym := m/6, m%6
		return abs(xn-xm) + abs(yn-ym)
	}

	dp := make([][26][26]int, len(word))
	for i := range len(word) {
		a := [26][26]int{}
		for k := range 26 {
			for m := range 26 {
				a[k][m] = 1 << 30
			}
		}
		dp[i] = a
	}

	firstChar := int(word[0] - 'A')
	for k := range 26 {
		dp[0][k][firstChar] = 0
		dp[0][firstChar][k] = 0
	}

	for i := 1; i < len(word); i++ {
		cur := int(word[i] - 'A')
		prv := int(word[i-1] - 'A')
		d := dist(cur, prv)
		for j := range 26 {
			dp[i][cur][j] = min(dp[i][cur][j], dp[i-1][prv][j]+d)
			dp[i][j][cur] = min(dp[i][j][cur], dp[i-1][j][prv]+d)
			if j == prv {
				for k := range 26 {
					d0 := dist(cur, k)
					dp[i][cur][j] = min(dp[i][cur][j], dp[i-1][k][j]+d0)
					dp[i][j][cur] = min(dp[i][j][cur], dp[i-1][j][k]+d0)
				}
			}
		}

	}

	res := 1 << 30
	for i := range 26 {
		for j := range 26 {
			res = min(res, dp[len(word)-1][i][j])
		}
	}

	return res
}
