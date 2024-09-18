package problems

import "testing"

func TestLargestNumber(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want string
	}{
		{
			name: "test 1",
			nums: []int{10, 2},
			want: "210",
		},
		{
			name: "test 2",
			nums: []int{9, 5, 34, 30, 3},
			want: "9534330",
		},
		{
			name: "test 3",
			nums: []int{0, 0},
			want: "0",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestNumber(tt.nums); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
