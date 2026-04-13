package problems_test

import (
	"leetcode/problems"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsMatch44(t *testing.T) {
	t.Parallel()

	for _, tt := range []struct {
		name string
		s    string
		p    string
		res  bool
	}{
		{"TestCase1", "aa", "a", false},
		{"TestCase2", "aa", "*", true},
		{"TestCase3", "cb", "?a", false},
		{"TestCase4", "cba", "??a", true},
		{"TestCase5", "cbdajdhasa", "*jdhas*?", true},
		{"TestCase6", "", "", true},
	} {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			res := problems.IsMatch(tt.s, tt.p)
			require.Equal(t, tt.res, res)
		})
	}
}
