package problems

import "testing"

func TestSumPrefixScores(t *testing.T) {
	tests := []struct {
		name  string
		words []string
		want  []int
	}{
		{
			name:  "test 1",
			words: []string{"abc", "ab", "bc", "b"},
			want:  []int{5, 4, 3, 2},
		},
		{
			name:  "test 2",
			words: []string{"abcd"},
			want:  []int{4},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := sumPrefixScores(tt.words)
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
