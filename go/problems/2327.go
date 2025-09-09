package problems

func peopleAwareOfSecret(n int, delay int, forget int) int {
	const m = 1_000_000_007

	// dp[i] = number of people who discover the secret on day i
	dp := make([]int, n+1)

	// Day 1: one person discovers the secret
	dp[1] = 1

	// share = number of people who can share the secret
	share := 0

	for i := 2; i <= n; i++ {
		// Remove people who forget the secret today (discovered forget days ago)
		// This must be done BEFORE calculating new discoveries
		if i-forget >= 1 {
			share = (share - dp[i-forget] + m) % m
		}

		// Add people who can start sharing today (discovered delay days ago)
		if i-delay >= 1 {
			share = (share + dp[i-delay]) % m
		}

		// New people who discover the secret today = people who can share
		dp[i] = share % m

	}

	// Total people who know the secret = sum of people who discovered it
	// and haven't forgotten yet
	total := 0
	for i := 1; i <= n; i++ {
		// People who discovered on day i and haven't forgotten by day n
		if i+forget > n {
			total = (total + dp[i]) % m
		}
	}

	return total
}
