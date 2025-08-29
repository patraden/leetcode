package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFlowerGame(t *testing.T) {
	t.Parallel()

	var v int64

	v = flowerGame(3, 2)
	assert.Equal(t, int64(3), v)

	v = flowerGame(1, 1)
	assert.Equal(t, int64(0), v)

	v = flowerGame(4, 3)
	assert.Equal(t, int64(6), v)
}
