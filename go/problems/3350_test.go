package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxIncreasingSubarrays(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "test 1",
			nums: []int{2, 5, 7, 8, 9, 2, 3, 4, 3, 1},
			want: 3,
		},
		// {
		// 	name: "test 2",
		// 	nums: []int{1, 2, 3, 4, 4, 4, 4, 5, 6, 7},
		// 	want: 2,
		// },
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxIncreasingSubarrays(tt.nums)
			assert.Equal(t, tt.want, got)
		})
	}

}
