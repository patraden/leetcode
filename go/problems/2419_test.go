package problems

import "testing"

func TestLongestSubarray(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "test 1",
			nums: []int{1, 2, 3, 3, 2, 2},
			want: 2,
		},
		{
			name: "test 2",
			nums: []int{1, 2, 3, 4},
			want: 1,
		},
		{
			name: "test 3",
			nums: []int{3},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := LongestSubarray(tt.nums); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
