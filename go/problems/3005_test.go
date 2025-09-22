package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxFrequencyElements(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		nums []int
		want int
	}{
		{"test 1", []int{1, 2, 2, 3, 1, 4}, 4},
		{"test 2", []int{1, 2, 3, 4, 5}, 5},
		{"test 3", []int{}, 0},
		{"test 4", []int{4, 4, 4, 3, 7, 1, 8, 3, 1, 6, 6, 6}, 6},
		{"test 5", []int{4, 4, 4, 4}, 4},
		{"test 5", []int{100}, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := maxFrequencyElements(tt.nums)
			assert.Equal(t, tt.want, got)
		})
	}
}
