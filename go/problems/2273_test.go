package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRemoveAnagrams2273(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name  string
		words []string
		want  []string
	}{
		{
			name:  "test 1",
			words: []string{"abba", "baba", "bbaa", "cd", "cd"},
			want:  []string{"abba", "cd"},
		},
		{
			name:  "test 2",
			words: []string{"a", "b", "c", "d", "e"},
			want:  []string{"a", "b", "c", "d", "e"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := removeAnagrams2273(tt.words)
			assert.Equal(t, tt.want, got)
		})
	}
}
