package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLenOfVDiagonal(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		grid [][]int
		want int
	}{
		{
			"Example1",
			[][]int{
				{2, 2, 1, 2, 2},
				{2, 0, 2, 2, 0},
				{2, 0, 1, 1, 0},
				{1, 0, 2, 2, 2},
				{2, 0, 0, 2, 2},
			},
			5,
		},
		{
			"Example2",
			[][]int{
				{2, 2, 2, 2, 2},
				{2, 0, 2, 2, 0},
				{2, 0, 1, 1, 0},
				{1, 0, 2, 2, 2},
				{2, 0, 0, 2, 2},
			},
			4,
		},
		{
			"Example3",
			[][]int{
				{1, 2, 2, 2, 2},
				{2, 2, 2, 2, 0},
				{2, 0, 0, 0, 0},
				{0, 0, 2, 2, 2},
				{2, 0, 0, 2, 0},
			},
			5,
		},
		{
			"Example4",
			[][]int{
				{2, 2, 2, 2, 2},
				{1, 2, 0, 2, 2},
			},
			3,
		},
		{
			"Example5",
			[][]int{
				{0, 2, 0},
				{0, 2, 0},
			},
			0,
		},
		{
			"Example6",
			[][]int{
				{2, 2, 0, 2, 0, 2, 0},
				{1, 2, 2, 1, 0, 2, 0},
			},
			2,
		},
		{
			"Example7",
			[][]int{
				{1, 0, 1, 2, 2, 1, 2},
				{0, 1, 2, 1, 2, 0, 0},
				{1, 0, 1, 1, 0, 0, 2},
			},
			4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			res := lenOfVDiagonal(tt.grid)
			assert.Equal(t, tt.want, res)
		})
	}

}
