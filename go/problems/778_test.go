package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSwimInWater(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		grid [][]int
		want int
	}{
		// {
		// 	name: "test 1",
		// 	grid: [][]int{
		// 		{0, 2},
		// 		{1, 3},
		// 	},
		// 	want: 3,
		// },
		// {
		// 	name: "test 2",
		// 	grid: [][]int{
		// 		{0, 1, 2, 3, 4},
		// 		{24, 23, 22, 21, 5},
		// 		{12, 13, 14, 15, 16},
		// 		{11, 17, 18, 19, 20},
		// 		{10, 9, 8, 7, 6},
		// 	},
		// 	want: 16,
		// },
		// {
		// 	name: "test 3",
		// 	grid: [][]int{
		// 		{1, 1},
		// 		{9, 2},
		// 	},
		// 	want: 2,
		// },
		{
			name: "test 4",
			grid: [][]int{
				{3, 2},
				{0, 1},
			},
			want: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := swimInWater(tt.grid)
			assert.Equal(t, tt.want, got)
		})
	}
}
