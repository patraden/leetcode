package problems

import (
	"fmt"
	"testing"
)

func TestSortMatrix3446(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		grid [][]int
		want int
	}{
		{
			name: "test 1",
			grid: [][]int{{1, 7, 3}, {9, 8, 2}, {4, 5, 6}},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			sortMatrix3446(tt.grid)

			for _, row := range tt.grid {
				fmt.Println(row)
			}

		})
	}
}
