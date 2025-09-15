package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCanBeTypedWords(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name          string
		text          string
		brokenLetters string
		want          int
	}{
		{"Test1", "hello world", "ad", 1},
		{"Test2", "leet code", "lt", 1},
		{"Test2", "leet code", "e", 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := canBeTypedWords(tt.text, tt.brokenLetters)
			assert.Equal(t, tt.want, got)
		})
	}

}
