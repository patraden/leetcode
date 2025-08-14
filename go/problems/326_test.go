package problems_test

import (
	"leetcode/problems"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPowerOfThree(t *testing.T) {
	assert.True(t, problems.IsPowerOfThree(3))
	assert.False(t, problems.IsPowerOfThree(-1))
	assert.True(t, problems.IsPowerOfThree(177147))
	assert.False(t, problems.IsPowerOfThree(177148))

}
