package problems

import (
	"leetcode/datastructures/binarytree"
	"testing"
)

func TestKthSmallest(t *testing.T) {
	tests := []struct {
		name string
		root *binarytree.TreeNode
		k    int
		want int
	}{
		{
			name: "test 1",
			root: &binarytree.TreeNode{
				Val: 3,
				Left: &binarytree.TreeNode{
					Val:  1,
					Left: nil,
					Right: &binarytree.TreeNode{
						Val:   2,
						Left:  nil,
						Right: nil,
					},
				},
				Right: &binarytree.TreeNode{
					Val:   4,
					Left:  nil,
					Right: nil,
				},
			},
			k:    1,
			want: 1,
		},
		{
			name: "test 2",
			root: &binarytree.TreeNode{
				Val: 5,
				Left: &binarytree.TreeNode{
					Val: 3,
					Left: &binarytree.TreeNode{
						Val: 2,
						Left: &binarytree.TreeNode{
							Val:   1,
							Left:  nil,
							Right: nil,
						},
						Right: nil,
					},
					Right: &binarytree.TreeNode{
						Val:   4,
						Left:  nil,
						Right: nil,
					},
				},
				Right: &binarytree.TreeNode{
					Val:   6,
					Left:  nil,
					Right: nil,
				},
			},
			k:    3,
			want: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := kthSmallest(tt.root, tt.k); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
