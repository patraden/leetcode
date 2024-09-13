package problems_test

import (
	"leetcode/problems"
	"testing"
)

func TestCountConsistentStrings(t *testing.T) {
	tests := []struct {
		name    string
		allowed string
		words   []string
		want    int
	}{
		{
			name:    "test 1",
			allowed: "ab",
			words:   []string{"ad", "bd", "aaab", "baa", "badab"},
			want:    2,
		},
		{
			name:    "test 2",
			allowed: "abc",
			words:   []string{"a", "b", "c", "ab", "ac", "bc", "abc"},
			want:    7,
		},
		{
			name:    "test 3",
			allowed: "cad",
			words:   []string{"cc", "acd", "b", "ba", "bac", "bad", "ac", "d"},
			want:    4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := problems.CountConsistentStrings(tt.allowed, tt.words)
			t.Logf("Expected: %d, Got: %d\n", tt.want, got)
			if got != tt.want {
				t.Errorf("CountConsistentStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}
