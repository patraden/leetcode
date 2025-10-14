package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestHasIncreasingSubarrays(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		nums []int
		k    int
		want bool
	}{
		{
			name: "test 1",
			nums: []int{2, 5, 7, 8, 9, 2, 3, 4, 3, 1},
			k:    3,
			want: true,
		},
		{
			name: "test 2",
			nums: []int{1, 2, 3, 4, 4, 4, 4, 5, 6, 7},
			k:    5,
			want: false,
		},
		{
			name: "test 3",
			nums: []int{1, 2, 3, 4, 5, 6},
			k:    3,
			want: true,
		},
		{
			name: "test 4",
			nums: []int{1, 2, 3, 0, 1, 2, 3},
			k:    3,
			want: true,
		},
		{
			name: "test 5",
			nums: []int{1, 2, 3, 4, 5, 6},
			k:    2,
			want: true,
		},
		{
			name: "test 6",
			nums: []int{1, 2, 3},
			k:    2,
			want: false,
		},
		{
			name: "test 7",
			nums: []int{19, 5},
			k:    1,
			want: true,
		},
		{
			name: "test 8",
			nums: []int{5, 8, -2, -1},
			k:    2,
			want: true,
		},
		{
			name: "test 9",
			nums: []int{13, 4, -7, -6},
			k:    2,
			want: false,
		},
		{
			name: "test 10",
			nums: []int{19, 4, 19, 6, 18},
			k:    2,
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := hasIncreasingSubarrays(tt.nums, tt.k)
			assert.Equal(t, tt.want, got)
		})
	}
}
