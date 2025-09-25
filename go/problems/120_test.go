package problems

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMinimumTotal120(t *testing.T) {
	tests := []struct {
		name     string
		triangle [][]int
		want     int
	}{
		{
			"Test 1",
			[][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}},
			11,
		},
		{
			"Test 2",
			[][]int{{-10}},
			-10,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := minimumTotal120(tt.triangle)
			require.Equal(t, tt.want, got)
		})
	}
}
