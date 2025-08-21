package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNumSubmat1504(t *testing.T) {
	t.Parallel()

	val := numSubmat([][]int{
		{1, 0, 1},
		{1, 1, 0},
		{1, 1, 0},
	})

	assert.Equal(t, 13, val)

	val = numSubmat([][]int{
		{0, 1, 1, 0},
		{0, 1, 1, 1},
		{1, 1, 1, 0},
	})

	assert.Equal(t, 24, val)

}
