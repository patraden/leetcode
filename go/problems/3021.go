package problems

func flowerGame(n int, m int) int64 {

	nodd := n/2 + n%2
	modd := m/2 + m%2
	neven := n / 2
	meven := m / 2

	return int64(nodd*meven + modd*neven)
}
