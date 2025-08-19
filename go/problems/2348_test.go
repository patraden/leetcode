package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestZeroFilledSubarray2348(t *testing.T) {
	t.Parallel()

	v := zeroFilledSubarray2348([]int{1, 3, 0, 0, 2, 0, 0, 4})
	assert.Equal(t, int64(6), v)

	v = zeroFilledSubarray2348([]int{0, 0, 0, 2, 0, 0})
	assert.Equal(t, int64(9), v)

	v = zeroFilledSubarray2348([]int{2, 10, 2019})
	assert.Equal(t, int64(0), v)
}
