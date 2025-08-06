package problems_test

import (
	"leetcode/problems"
	"testing"
)

func TestThreeSumClosest16(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   int
	}{
		{
			name:   "test 1",
			nums:   []int{-1, 2, 1, -4},
			target: 1,
			want:   2,
		},
		{
			name:   "test 2",
			nums:   []int{0, 0, 0},
			target: 1,
			want:   0,
		},
		{
			name:   "test 3",
			nums:   []int{-10, 10, 11, -15, 28, 16, 29},
			target: 38,
			want:   37,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := problems.ThreeSumClosest(tt.nums, tt.target)
			if res != tt.want {
				t.Errorf("ThreeSumClosest() = %v, want %v", res, tt.want)
			}
		})
	}

}

func TestTwoSumClosesTwoPointers16(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		start  int
		target int
		want   int
	}{
		{
			name:   "test 1",
			nums:   []int{1, 2, 5, 9},
			start:  0,
			target: 11,
			want:   11,
		},
		{
			name:   "test 2",
			nums:   []int{1, 2, 3},
			start:  0,
			target: 6,
			want:   5,
		},
		{
			name:   "test 3",
			nums:   []int{-5, 1, 10, 11},
			start:  0,
			target: -1,
			want:   -4,
		},
		{
			name:   "test 4",
			nums:   []int{-5, 1, 10, 11, 12, 17},
			start:  3,
			target: 30,
			want:   29,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			res := problems.TwoSumClosesTwoPointers(tt.nums, tt.start, tt.target)
			if res != tt.want {
				t.Errorf("TwoSumClosest() = %v, want %v", res, tt.want)
			}
		})
	}

}
