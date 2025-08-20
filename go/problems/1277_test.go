package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountSquares1277(t *testing.T) {
	t.Parallel()

	res := countSquares(
		[][]int{
			{0, 1, 1, 1},
			{1, 1, 1, 1},
			{0, 1, 1, 1},
		},
	)

	assert.Equal(t, 15, res)

	res = countSquares(
		[][]int{
			{1, 0, 1},
			{1, 1, 0},
			{1, 1, 0},
		},
	)

	assert.Equal(t, 7, res)

	res = countSquares(
		[][]int{
			{0},
		},
	)

	assert.Equal(t, 0, res)
}
