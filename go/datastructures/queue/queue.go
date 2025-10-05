/*
fixed size queue based on slice
*/

package queue

import "fmt"

type Queue struct {
	queue []any
	head  int
	tail  int
	maxN  int
	size  int
}

func NewQueue(n int) *Queue {
	return &Queue{
		queue: make([]any, n),
		head:  0,
		tail:  0,
		maxN:  n,
		size:  0,
	}
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Push(x any) error {

	if q.size == q.maxN {
		return fmt.Errorf("queue is out of capacity %v", q.maxN)
	}

	q.queue[q.tail] = x
	q.tail = (q.tail + 1) % q.maxN
	q.size += 1
	return nil

}

func (q *Queue) Pop() any {
	if q.IsEmpty() {
		return nil
	}
	x := q.queue[q.head]
	q.queue[q.head] = nil
	q.head = (q.head + 1) % q.maxN
	q.size -= 1
	return x
}
