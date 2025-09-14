package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSpellchecker966(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name     string
		wordlist []string
		queries  []string
		want     []string
	}{
		// {
		// 	name:     "test 1",
		// 	wordlist: []string{"KiTe", "kite", "hare", "Hare"},
		// 	queries:  []string{"kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"},
		// 	want:     []string{"kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"},
		// },
		// {
		// 	name:     "test 2",
		// 	wordlist: []string{"yellow"},
		// 	queries:  []string{"YellOw"},
		// 	want:     []string{"yellow"},
		// },
		{
			name:     "test 3",
			wordlist: []string{"ae", "aa"},
			queries:  []string{"UU"},
			want:     []string{"ae"},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := spellchecker966(tt.wordlist, tt.queries)
			assert.Equal(t, tt.want, got)
		})
	}

}
