package problems

import (
	"leetcode/datastructures/binarytree"
	"testing"
)

func TestValidBST(t *testing.T) {
	tests := []struct {
		name string
		root *binarytree.TreeNode
		want bool
	}{
		{
			name: "test 0",
			root: &binarytree.TreeNode{
				Val:   2,
				Left:  nil,
				Right: nil,
			},
			want: true,
		},
		{
			name: "test 1",
			root: &binarytree.TreeNode{
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
			want: true,
		},
		{
			name: "test 2",
			root: &binarytree.TreeNode{
				Val: 5,
				Left: &binarytree.TreeNode{
					Val:   1,
					Left:  nil,
					Right: nil,
				},
				Right: &binarytree.TreeNode{
					Val: 4,
					Left: &binarytree.TreeNode{
						Val:   3,
						Left:  nil,
						Right: nil,
					},
					Right: &binarytree.TreeNode{
						Val:   6,
						Left:  nil,
						Right: nil,
					},
				},
			},
			want: false,
		},
		{
			name: "test 3",
			root: &binarytree.TreeNode{
				Val: 5,
				Left: &binarytree.TreeNode{
					Val:   4,
					Left:  nil,
					Right: nil,
				},
				Right: &binarytree.TreeNode{
					Val: 6,
					Left: &binarytree.TreeNode{
						Val:   3,
						Left:  nil,
						Right: nil,
					},
					Right: &binarytree.TreeNode{
						Val:   7,
						Left:  nil,
						Right: nil,
					},
				},
			},
			want: false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isValidBST(tt.root); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
