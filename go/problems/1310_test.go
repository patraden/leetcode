package problems_test

import (
	"leetcode/problems"
	"testing"
)

func TestXorQueries(t *testing.T) {
	tests := []struct {
		name    string
		arr     []int
		queries [][]int
		want    []int
	}{
		{
			name:    "test 1",
			arr:     []int{1, 3, 4, 8},
			queries: [][]int{{0, 1}, {1, 2}, {0, 3}, {3, 3}},
			want:    []int{2, 7, 14, 8},
		},
		{
			name:    "test 2",
			arr:     []int{4, 8, 2, 10},
			queries: [][]int{{2, 3}, {1, 3}, {0, 0}, {0, 3}},
			want:    []int{8, 0, 4, 4},
		},
		{
			name:    "test 3",
			arr:     []int{11},
			queries: [][]int{{0, 0}, {0, 0}},
			want:    []int{11, 11},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := problems.XorQueries(tt.arr, tt.queries)
			if len(got) != len(tt.want) {
				t.Errorf("length diff got = %v, want %v", len(got), len(tt.want))
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("diff at index %v got = %v, want %v", i, got[i], tt.want[i])
				}
			}
		})
	}
}
