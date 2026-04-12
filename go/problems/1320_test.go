package problems_test

import (
	"leetcode/problems"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMinimumDistance1320(t *testing.T) {
	t.Parallel()

	for _, tt := range []struct {
		name string
		word string
		res  int
	}{
		{"Test1", "CAKE", 3},
		{"Test2", "HAPPY", 6},
	} {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			res := problems.MinimumDistance1320(tt.word)
			require.Equal(t, tt.res, res)
		})
	}
}
