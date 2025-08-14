package problems_test

import (
	"leetcode/datastructures/linkedlist"
	"leetcode/problems"
	"testing"

	"github.com/stretchr/testify/assert"
)

type ListNode = linkedlist.ListNode

func TestRemoveNthFromEnd19(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		root *ListNode
		n    int
		want []int
	}{
		{
			name: "test 1",
			root: linkedlist.ArrayToList([]int{1, 2, 3, 4, 5}),
			n:    2,
			want: []int{1, 2, 3, 5},
		},
		{
			name: "test 2",
			root: linkedlist.ArrayToList([]int{1}),
			n:    1,
			want: []int{},
		},
		{
			name: "test 3",
			root: linkedlist.ArrayToList([]int{1, 2, 3, 4, 5}),
			n:    5,
			want: []int{2, 3, 4, 5},
		},
		{
			name: "test 4",
			root: linkedlist.ArrayToList([]int{1, 2, 3, 4, 5}),
			n:    3,
			want: []int{1, 2, 4, 5},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			node := problems.RemoveNthFromEnd(tt.root, tt.n)
			a := linkedlist.ListToArray(node)
			assert.Equal(t, tt.want, a)
		})
	}

}
