package problems

import (
	"fmt"
	"testing"
)

func TestNumSubmat1504(t *testing.T) {
	t.Parallel()

	val := numSubmat([][]int{
		{1, 0, 1},
		{1, 1, 0},
		{1, 1, 0},
	})

	fmt.Println(val)

	val = numSubmat([][]int{
		{0, 1, 1, 0},
		{0, 1, 1, 1},
		{1, 1, 1, 0},
	})

	fmt.Println(val)

}
