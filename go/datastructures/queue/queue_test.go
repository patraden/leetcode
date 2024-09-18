package queue

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQueue(t *testing.T) {

	q := NewQueue(3)

	if q.maxN != 3 {
		t.Errorf("max size is not set")
	}

	if !q.IsEmpty() {
		t.Errorf("queue expected to be empty")
	}

	q.Push(1)
	q.Push(2)
	assert.Equal(t, q.Push(3), nil, "unexpected error")
	assert.Error(t, q.Push(4), "expected error")
	assert.Equal(t, q.Pop(), 1)
	assert.Equal(t, q.Pop(), 2)

	q.Push(4)
	q.Push(5)
	assert.Equal(t, q.Pop(), 3)
	assert.Equal(t, q.Pop(), 4)
	assert.Equal(t, q.Pop(), 5)

	if !q.IsEmpty() {
		t.Errorf("queue expected to be empty")
	}

}
