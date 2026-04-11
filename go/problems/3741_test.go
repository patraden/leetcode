package problems

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMinimumDistance(t *testing.T) {
	t.Parallel()

	for _, tt := range []struct {
		name  string
		input []int
		res   int
	}{
		{
			name:  "Test1",
			input: []int{1, 2, 1, 1, 3},
			res:   6,
		},
		{
			name:  "Test2",
			input: []int{1, 1, 2, 3, 2, 1, 2},
			res:   8,
		},
		{
			name:  "Test3",
			input: []int{1},
			res:   -1,
		},
	} {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			res := minimumDistance(tt.input)
			require.Equal(t, tt.res, res)

		})
	}
}
