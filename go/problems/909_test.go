package problems

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestSnakesAndLadders(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name  string
		board [][]int
		want  int
	}{
		{
			name: "example 1",
			board: [][]int{
				{-1, -1, -1, -1, -1, -1},
				{-1, -1, -1, -1, -1, -1},
				{-1, -1, -1, -1, -1, -1},
				{-1, 35, -1, -1, 13, -1},
				{-1, -1, -1, -1, -1, -1},
				{-1, 15, -1, -1, -1, -1},
			},
			want: 4,
		},
		{
			name: "example 2",
			board: [][]int{
				{-1, -1},
				{-1, 3},
			},
			want: 1,
		},
		{
			name: "unreachable",
			board: [][]int{
				{-1, -1, -1, -1, -1, -1},
				{-1, -1, -1, -1, -1, -1},
				{-1, -1, -1, -1, -1, -1},
				{-1, 35, -1, -1, 13, -1},
				{-1, -1, -1, -1, -1, 1},
				{-1, 1, 1, 1, 1, 1},
			},
			want: -1,
		},
		{
			name: "3x3 with ladder",
			board: [][]int{
				{-1, -1, -1},
				{-1, 9, 8},
				{-1, 8, 9},
			},
			want: 1,
		},
		{
			name: "3x3 with snake and ladder",
			board: [][]int{
				{-1, 4, -1},
				{6, 2, 6},
				{-1, 3, -1},
			},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := snakesAndLadders(tt.board)
			require.Equal(t, tt.want, got)
		})
	}
}
