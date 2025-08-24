package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLongestSubarray1493(t *testing.T) {
	t.Parallel()

	val := longestSubarray1493([]int{1, 1, 0, 1})
	assert.Equal(t, 3, val)

	val = longestSubarray1493([]int{0, 1, 1, 1, 0, 1, 1, 0, 1})
	assert.Equal(t, 5, val)

	val = longestSubarray1493([]int{1, 1, 1})
	assert.Equal(t, 2, val)

}
