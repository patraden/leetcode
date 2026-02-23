package problems

import (
	"leetcode/datastructures/queue"
)

func snakesAndLadders(board [][]int) int {
	n := len(board)
	matrixIndex := func(idx int) (int, int) {
		i, j := n-1-(idx-1)/n, (idx-1)%n
		if i&1 == n&1 {
			j = n - 1 - j
		}
		return i, j
	}

	mx := n * n
	q := queue.NewQueue(n * n)
	distances := map[int]int{}

	var i, j, v, res int

	v = 1
	q.Push(v)
	distances[v] = 0

	for !q.IsEmpty() {
		v, _ = q.Pop().(int)

		if v == mx {
			res = min(distances[v], max(res, distances[v]))
		}

		for _, d := range []int{1, 2, 3, 4, 5, 6} {
			w := v + d
			if w > mx {
				continue
			}

			i, j = matrixIndex(w)
			if board[i][j] != -1 {
				w = board[i][j]
			}

			if _, ok := distances[w]; !ok || (ok && distances[w] > distances[v]+1) {
				q.Push(w)
				distances[w] = distances[v] + 1
			}
		}
	}

	if res == 0 {
		return -1
	}

	return res
}
