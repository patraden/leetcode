package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindSmallestInteger(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name   string
		nums   []int
		value  int
		expect int
	}{
		{
			name:   "test 1",
			nums:   []int{1, -10, 7, 13, 6, 8},
			value:  5,
			expect: 4,
		},
		// {
		// 	name:   "test 2",
		// 	nums:   []int{1, -10, 7, 13, 6, 8},
		// 	value:  7,
		// 	expect: 2,
		// },
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			t.Parallel()

			got := findSmallestInteger(test.nums, test.value)
			assert.Equal(t, test.expect, got)
		})
	}
}
