package problems

import (
	"sort"
)

func maximumTotalDamage(power []int) int64 {
	counter := make(map[int]int)
	for _, p := range power {
		counter[p]++
	}

	upower := make([]int, 0, len(counter))
	upower = append(upower, -2)
	for k := range counter {
		upower = append(upower, k)
	}

	sort.Ints(upower)

	dp := make([]int64, len(upower))
	for i := 1; i < len(upower); i++ {
		p := upower[i]
		cast := int64(upower[i] * counter[p])
		switch {
		case p-upower[i-1] == 2:
			dp[i] = max(dp[i-2]+cast, dp[i-1])
		case p-upower[i-1] == 1 && p-upower[i-2] == 2:
			dp[i] = max(dp[i-3]+cast, dp[i-1], dp[i-2])
		case p-upower[i-1] == 1:
			dp[i] = max(dp[i-2]+cast, dp[i-1])
		default:
			dp[i] = dp[i-1] + cast
		}
	}

	return dp[len(dp)-1]
}
