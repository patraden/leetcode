package problems

import (
	"leetcode/datastructures/binarytree"
	"testing"
)

func TestGetMinimumDifference530(t *testing.T) {
	tests := []struct {
		name string
		root *binarytree.TreeNode
		want int
	}{
		{
			name: "test 1",
			root: &binarytree.TreeNode{
				Val: 4,
				Left: &binarytree.TreeNode{
					Val: 2,
					Left: &binarytree.TreeNode{
						Val:   1,
						Left:  nil,
						Right: nil,
					},
					Right: &binarytree.TreeNode{
						Val:   3,
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
			want: 1,
		},
		{
			name: "test 2",
			root: &binarytree.TreeNode{
				Val: 1,
				Left: &binarytree.TreeNode{
					Val:   0,
					Left:  nil,
					Right: nil,
				},
				Right: &binarytree.TreeNode{
					Val: 48,
					Left: &binarytree.TreeNode{
						Val:   12,
						Left:  nil,
						Right: nil,
					},
					Right: &binarytree.TreeNode{
						Val:   49,
						Left:  nil,
						Right: nil,
					},
				},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getMinimumDifference530(tt.root); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
