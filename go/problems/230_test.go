package problems

import "testing"

func TestKthSmallest(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		k    int
		want int
	}{
		{
			name: "test 1",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val:  1,
					Left: nil,
					Right: &TreeNode{
						Val:   2,
						Left:  nil,
						Right: nil,
					},
				},
				Right: &TreeNode{
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
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 2,
						Left: &TreeNode{
							Val:   1,
							Left:  nil,
							Right: nil,
						},
						Right: nil,
					},
					Right: &TreeNode{
						Val:   4,
						Left:  nil,
						Right: nil,
					},
				},
				Right: &TreeNode{
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
