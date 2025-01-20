package problems

import "testing"

func TestLongestCommonPrefix(t *testing.T) {
	tests := []struct {
		name string
		arr1 []int
		arr2 []int
		want int
	}{
		// {
		// 	name: "test 1",
		// 	arr1: []int{1, 10, 100},
		// 	arr2: []int{1000},
		// 	want: 3,
		// },
		// {
		// 	name: "test 2",
		// 	arr1: []int{1, 2, 3},
		// 	arr2: []int{4, 4, 4},
		// 	want: 0,
		// },
		{
			name: "test 3",
			arr1: []int{10},
			arr2: []int{17, 11},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonPrefix(tt.arr1, tt.arr2); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
