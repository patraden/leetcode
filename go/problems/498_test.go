package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindDiagonalOrder(t *testing.T) {
	t.Parallel()

	testCases := []struct {
		name     string
		input    [][]int
		expected []int
	}{
		{
			name: "3x3 square matrix",
			input: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expected: []int{1, 2, 4, 7, 5, 3, 6, 8, 9},
		},
		{
			name: "2x2 square matrix",
			input: [][]int{
				{1, 2},
				{3, 4},
			},
			expected: []int{1, 2, 3, 4},
		},
		{
			name: "3x4 rectangular matrix",
			input: [][]int{
				{1, 2, 3, 5},
				{4, 5, 6, 7},
				{7, 8, 9, 10},
			},
			expected: []int{1, 2, 4, 7, 5, 3, 5, 6, 8, 9, 7, 10},
		},
		{
			name: "single row matrix",
			input: [][]int{
				{1, 2, 3, 5},
			},
			expected: []int{1, 2, 3, 5},
		},
		{
			name: "single column matrix",
			input: [][]int{
				{1},
				{20},
				{3},
			},
			expected: []int{1, 20, 3},
		},
	}

	for _, tc := range testCases {
		tc := tc // capture range variable for parallel execution
		t.Run(tc.name, func(t *testing.T) {
			t.Parallel()
			result := findDiagonalOrder(tc.input)
			assert.Equal(t, tc.expected, result)
		})
	}
}
