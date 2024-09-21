package problems

import "testing"

func TestLexicalOrder386(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want []int
	}{
		{
			name: "test 1",
			n:    13,
			want: []int{1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9},
		},
		{
			name: "test 2",
			n:    2,
			want: []int{1, 2},
		},
		{
			name: "test 3",
			n:    1,
			want: []int{1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := lexicalOrder386(tt.n)
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
