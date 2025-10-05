package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPacificAtlantic(t *testing.T) {
	tests := []struct {
		name    string
		heights [][]int
		want    [][]int
	}{
		{
			name: "test 1",
			heights: [][]int{
				{1, 2, 2, 3, 5},
				{3, 2, 3, 4, 4},
				{2, 4, 5, 3, 1},
				{6, 7, 1, 4, 5},
				{5, 1, 1, 2, 4},
			},
			want: [][]int{{0, 4}, {1, 3}, {1, 4}, {2, 2}, {3, 0}, {3, 1}, {4, 0}},
		},
		{
			name:    "test 2",
			heights: [][]int{{1}},
			want:    [][]int{{0, 0}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// pacificAtlantic(tt.heights)
			got := pacificAtlantic(tt.heights)
			assert.Equal(t, tt.want, got)
		})
	}
}
