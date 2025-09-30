package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTriangularSum2221(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		nums []int
		want int
	}{
		{"Test1", []int{1, 2, 3, 4, 5}, 8},
		{"Test2", []int{5}, 5},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := triangularSum2221(tt.nums)
			assert.Equal(t, tt.want, got)
		})
	}
}
