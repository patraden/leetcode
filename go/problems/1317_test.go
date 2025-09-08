package problems

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetNoZeroIntegers(t *testing.T) {
	t.Parallel()

	n := 214
	val := getNoZeroIntegers(n)
	assert.Equal(t, n, val[0]+val[1])

	fmt.Println(val)

	n = 101
	val = getNoZeroIntegers(n)
	assert.Equal(t, n, val[0]+val[1])

	fmt.Println(val)

	n = 69
	val = getNoZeroIntegers(n)
	assert.Equal(t, n, val[0]+val[1])

	n = 1013728173106
	val = getNoZeroIntegers(n)
	assert.Equal(t, n, val[0]+val[1])

	fmt.Println(val)
}
