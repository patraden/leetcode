package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxNumber321(t *testing.T) {
	tests := []struct {
		name  string
		nums1 []int
		nums2 []int
		k     int
		want  []int
	}{
		{
			name:  "test 1",
			nums1: []int{3, 4, 6, 5},
			nums2: []int{9, 1, 2, 5, 8, 3},
			k:     5,
			want:  []int{9, 8, 6, 5, 3},
		},
		{
			name:  "test 2",
			nums1: []int{6, 7},
			nums2: []int{6, 0, 4},
			k:     5,
			want:  []int{6, 7, 6, 0, 4},
		},
		{
			name:  "test 3",
			nums1: []int{3, 9},
			nums2: []int{8, 9},
			k:     3,
			want:  []int{9, 8, 9},
		},
		{
			name:  "test 4",
			nums1: []int{8, 9},
			nums2: []int{3, 9},
			k:     3,
			want:  []int{9, 8, 9},
		},
		{
			name:  "test 5",
			nums1: []int{9},
			nums2: []int{8},
			k:     2,
			want:  []int{9, 8},
		},
		{
			name:  "test 6",
			nums1: []int{8},
			nums2: []int{8},
			k:     2,
			want:  []int{8, 8},
		},
		{
			name:  "test 7",
			nums1: []int{8, 9, 8},
			nums2: []int{8, 8},
			k:     2,
			want:  []int{9, 8},
		},
		{
			name:  "test 8",
			nums1: []int{8, 6, 9},
			nums2: []int{1, 7, 5},
			k:     3,
			want:  []int{9, 7, 5},
		},
		{
			name:  "test 9",
			nums1: []int{2, 1, 7, 8, 0, 1, 7, 3, 5, 8, 9, 0, 0, 7, 0, 2, 2, 7, 3, 5, 5},
			nums2: []int{2, 6, 2, 0, 1, 0, 5, 4, 5, 5, 3, 3, 3, 4},
			k:     35,
			want:  []int{2, 6, 2, 2, 1, 7, 8, 0, 1, 7, 3, 5, 8, 9, 0, 1, 0, 5, 4, 5, 5, 3, 3, 3, 4, 0, 0, 7, 0, 2, 2, 7, 3, 5, 5},
		},
		{
			name:  "test 10",
			nums1: []int{2, 5, 6, 4, 4, 0},
			nums2: []int{7, 3, 8, 0, 6, 5, 7, 6, 2},
			k:     15,
			want:  []int{7, 3, 8, 2, 5, 6, 4, 4, 0, 6, 5, 7, 6, 2, 0},
		},
		{
			name:  "test 11",
			nums1: []int{5, 0, 2, 1, 0, 1, 0, 3, 9, 1, 2, 8, 0, 9, 8, 1, 4, 7, 3},
			nums2: []int{7, 6, 7, 1, 0, 1, 0, 5, 6, 0, 5, 0},
			k:     31,
			want:  []int{7, 6, 7, 5, 1, 0, 2, 1, 0, 1, 0, 5, 6, 0, 5, 0, 1, 0, 3, 9, 1, 2, 8, 0, 9, 8, 1, 4, 7, 3, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxNumber321(tt.nums1, tt.nums2, tt.k)
			assert.Equal(t, tt.want, got)
		})
	}

}
