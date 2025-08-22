package problems

import (
	"fmt"
	"testing"
)

func TestMinimumArea3195(t *testing.T) {
	t.Parallel()

	val := minimumArea([][]int{
		{0, 1, 0},
		{1, 0, 1},
	})

	fmt.Println(val)

	val = minimumArea([][]int{
		{1, 0},
		{0, 0},
	})

	fmt.Println(val)

}
