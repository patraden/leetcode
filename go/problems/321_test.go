package problems

import "testing"

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
		// {
		// 	name:  "test 2",
		// 	nums1: []int{6, 7},
		// 	nums2: []int{6, 0, 4},
		// 	k:     5,
		// 	want:  []int{6, 7, 6, 0, 4},
		// },
		// {
		// 	name:  "test 3",
		// 	nums1: []int{3, 9},
		// 	nums2: []int{8, 9},
		// 	k:     3,
		// 	want:  []int{9, 8, 9},
		// },
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxNumber321(tt.nums1, tt.nums2, tt.k)
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
