package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTaskManagerTest0(t *testing.T) {
	t.Parallel()

	tasks := [][]int{}

	tm := ConstructorTM(tasks)

	tm.Add(4, 104, 5)
	uid := tm.ExecTop()
	assert.Equal(t, 4, uid)
	uid = tm.ExecTop()
	assert.Equal(t, -1, uid)

}

func TestTaskManagerTest1(t *testing.T) {
	t.Parallel()

	tasks := [][]int{
		{1, 101, 10},
		{2, 102, 20},
		{3, 103, 15},
	}

	tm := ConstructorTM(tasks)

	tm.Add(4, 104, 5)
	tm.Edit(102, 8)
	uid := tm.ExecTop()
	assert.Equal(t, 3, uid)

	tm.Rmv(101)
	tm.Add(5, 105, 15)

	uid = tm.ExecTop()
	assert.Equal(t, 5, uid)

}

func TestTaskManagerTest2(t *testing.T) {
	t.Parallel()

	tasks := [][]int{
		{10, 10, 50},
		{9, 29, 17},
		{1, 21, 3},
		{7, 17, 6},
	}

	tm := ConstructorTM(tasks)
	assert.Equal(t, 4, tm.pq.Len())
	assert.Equal(t, 4, len(tm.tasks))

	uid := tm.ExecTop()
	assert.Equal(t, 10, uid)

	tm.Rmv(29)
	assert.Equal(t, 2, tm.pq.Len())
	assert.Equal(t, 2, len(tm.tasks))

	tm.Add(4, 10, 7)
	assert.Equal(t, 3, tm.pq.Len())
	assert.Equal(t, 3, len(tm.tasks))

	uid = tm.ExecTop()
	assert.Equal(t, 4, uid)

	// tm.Add(5, 105, 15)

	// uid = tm.ExecTop()
	// assert.Equal(t, 5, uid)

}
