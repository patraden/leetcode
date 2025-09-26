package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTriangleNumber611(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{"Test 1", []int{2, 2, 3, 4}, 3},
		{"Test 2", []int{4, 2, 3, 4}, 4},
		{"Test 3", []int{2, 2, 2, 2}, 4},
		{"Test 4", []int{4, 2, 2}, 0},
		{"Test 5", []int{4, 3, 2}, 1},
		{"Test 6", []int{48, 66, 61, 46, 94, 75}, 19},
		{"Test 7", []int{1, 2, 3, 4, 5, 6}, 7},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := triangleNumber611(tt.nums)
			assert.Equal(t, tt.want, got)
		})
	}
}
