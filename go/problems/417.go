package problems

import (
	"fmt"
	"sort"
)

type Queue struct {
	queue [][]int
	head  int
	tail  int
	maxN  int
	size  int
}

func NewQueue(n int) *Queue {
	return &Queue{
		queue: make([][]int, n),
		head:  0,
		tail:  0,
		maxN:  n,
		size:  0,
	}
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Push(x []int) error {

	if q.size == q.maxN {
		return fmt.Errorf("queue is out of capacity %v", q.maxN)
	}

	q.queue[q.tail] = x
	q.tail = (q.tail + 1) % q.maxN
	q.size += 1
	return nil

}

func (q *Queue) Pop() []int {
	if q.IsEmpty() {
		return nil
	}
	x := q.queue[q.head]
	q.queue[q.head] = nil
	q.head = (q.head + 1) % q.maxN
	q.size -= 1
	return x
}

func pacificAtlantic(heights [][]int) [][]int {
	res := [][]int{}
	n := len(heights)
	m := len(heights[0])

	visited := make([][]int, n)
	for i := range visited {
		visited[i] = make([]int, m)
	}

	q := NewQueue(n * m)

	// pacific ocean
	for j := range m {
		q.Push([]int{0, j})
		visited[0][j] += 1
	}

	for i := 1; i < n; i++ {
		q.Push([]int{i, 0})
		visited[i][0] += 1
	}

	for !q.IsEmpty() {
		u := q.Pop()
		i, j := u[0], u[1]

		for _, d := range [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}} {
			ic, jc := i+d[0], j+d[1]
			if ic >= 0 && ic < n && jc >= 0 && jc < m &&
				visited[ic][jc] < 1 && heights[ic][jc] >= heights[i][j] {
				visited[ic][jc] += 1
				q.Push([]int{ic, jc})
			}
		}
	}

	// atlantic ocean
	for j := range m {
		q.Push([]int{n - 1, j})
		visited[n-1][j] += 2
	}

	for i := 0; i < n-1; i++ {
		q.Push([]int{i, m - 1})
		visited[i][m-1] += 2
	}

	for !q.IsEmpty() {
		u := q.Pop()
		i, j := u[0], u[1]
		if visited[i][j] == 3 {
			res = append(res, []int{i, j})
		}

		for _, d := range [][]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}} {
			ic, jc := i+d[0], j+d[1]
			if ic >= 0 && ic < n && jc >= 0 && jc < m &&
				visited[ic][jc] < 2 && heights[ic][jc] >= heights[i][j] {
				visited[ic][jc] += 2
				q.Push([]int{ic, jc})
			}
		}
	}

	sort.Slice(res, func(i, j int) bool {
		if res[i][0] == res[j][0] {
			return res[i][1] < res[j][1]
		}
		return res[i][0] < res[j][0]
	})

	return res
}
