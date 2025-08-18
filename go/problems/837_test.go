package problems

import (
	"fmt"
	"testing"
)

func TestNew21Game837(t *testing.T) {
	t.Parallel()

	v := new21Game(21, 17, 10)
	// v := new21Game(6, 1, 10)
	fmt.Println(v)
}
