package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestAreaOfMaxDiagonal(t *testing.T) {
	t.Parallel()

	v := areaOfMaxDiagonal([][]int{
		{9, 3},
		{8, 6},
	})

	assert.Equal(t, 48, v)

	v = areaOfMaxDiagonal([][]int{
		{3, 4},
		{4, 3},
	})

	assert.Equal(t, 12, v)
}
