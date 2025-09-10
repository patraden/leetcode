package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinimumTeachings(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name        string
		n           int
		languages   [][]int
		friendships [][]int
		want        int
	}{
		{"Test1", 2, [][]int{{1}, {2}, {1, 2}}, [][]int{{1, 2}, {1, 3}, {2, 3}}, 1},
		{"Test2", 3, [][]int{{2}, {1, 3}, {1, 2}, {3}}, [][]int{{1, 4}, {1, 2}, {3, 4}, {2, 3}}, 2},
		{
			name: "Test3",
			n:    11,
			languages: [][]int{
				{3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6},
				{5, 10, 6, 4, 8, 7},
				{6, 11, 7, 9},
				{11, 10, 4},
				{6, 2, 8, 4, 3},
				{9, 2, 8, 4, 6, 1, 5, 7, 3, 10},
				{7, 5, 11, 1, 3, 4},
				{3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9},
				{8, 6, 10, 2, 3, 1, 11, 5},
				{5, 11, 6, 4, 2},
			},
			friendships: [][]int{
				{7, 9}, {3, 7}, {3, 4}, {2, 9}, {1, 8}, {5, 9},
				{8, 9}, {6, 9}, {3, 5}, {4, 5}, {4, 9}, {3, 6}, {1, 7}, {1, 3},
				{2, 8}, {2, 6}, {5, 7}, {4, 6}, {5, 8}, {5, 6}, {2, 7}, {4, 8},
				{3, 8}, {6, 8}, {2, 5}, {1, 4}, {1, 9}, {1, 6}, {6, 7},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := minimumTeachings(tt.n, tt.languages, tt.friendships)
			assert.Equal(t, tt.want, got)
		})
	}
}
