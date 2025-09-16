package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReplaceNonCoprimes(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		nums []int
		want []int
	}{
		{
			name: "Test1",
			nums: []int{6, 4, 3, 2, 7, 6, 2},
			want: []int{12, 7, 6},
		},
		{
			name: "Test2",
			nums: []int{2, 2, 1, 1, 3, 3, 3},
			want: []int{2, 1, 1, 3},
		},
		{
			name: "Test3",
			nums: []int{3},
			want: []int{3},
		},
		{
			name: "Test4",
			nums: []int{287, 41, 49, 287, 899, 23, 23, 20677, 5, 825},
			want: []int{2009, 20677, 825},
		},
		{
			name: "Test5",
			nums: []int{
				8303, 361, 8303, 361, 437, 361, 8303,
				8303, 8303, 6859, 19, 19, 361, 70121,
				70121, 70121, 70121, 70121, 70121,
				70121, 70121, 70121, 70121, 70121,
				70121, 70121, 70121, 70121, 70121,
				1271, 31, 961, 31, 7, 2009, 7, 2009, 2009,
				49, 7, 7, 8897, 1519, 31, 1519, 217,
			},
			want: []int{157757, 70121, 1930649},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := replaceNonCoprimes(tt.nums)
			assert.Equal(t, tt.want, got)
			// fmt.Println(got)
		})
	}

}
