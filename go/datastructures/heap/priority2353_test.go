package heap

import (
	"container/heap"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestPriorityQueuePushPop(t *testing.T) {
	t.Parallel()

	pq := &PriorityQueue{}
	heap.Init(pq)

	pItem, ok := pq.Pop().(*Item)
	require.False(t, ok)
	require.Nil(t, pItem)

	item := NewItem("miso", 10)
	heap.Push(pq, item)

	pItem, ok = heap.Pop(pq).(*Item)
	require.True(t, ok)

	assert.Equal(t, item.priority, pItem.priority)
	assert.Equal(t, -1, pItem.index)
	assert.Equal(t, "miso", pItem.name)

}

func TestPriorityQueuePushMultiplePopFirst(t *testing.T) {
	t.Parallel()

	pq := &PriorityQueue{}
	heap.Init(pq)

	item1 := NewItem("miso", 5)
	item2 := NewItem("ramen", 20)
	item3 := NewItem("sushi", 20)

	heap.Push(pq, item1)
	heap.Push(pq, item2)
	heap.Push(pq, item3)

	pItem, ok := heap.Pop(pq).(*Item)
	require.True(t, ok)

	assert.Equal(t, item2.priority, pItem.priority)
	assert.Equal(t, item2.name, pItem.name)
	assert.Equal(t, -1, pItem.index)

}

func TestPriorityQueueUpdateFix(t *testing.T) {
	t.Parallel()

	pq := &PriorityQueue{}
	heap.Init(pq)

	item1 := NewItem("miso", 5)
	item2 := NewItem("ramen", 20)
	item3 := NewItem("sushi", 20)

	heap.Push(pq, item1)
	heap.Push(pq, item2)
	heap.Push(pq, item3)

	item3.Set(30)
	heap.Fix(pq, item3.index)

	pItem, ok := heap.Pop(pq).(*Item)
	require.True(t, ok)

	assert.Equal(t, item3.priority, pItem.priority)
	assert.Equal(t, item3.name, pItem.name)
	assert.Equal(t, -1, pItem.index)
}
