package problems

import (
	"fmt"
	"testing"
)

func TestJudgePoint24(t *testing.T) {
	t.Parallel()

	// ok := judgePoint24([]int{4, 1, 8, 7})
	// fmt.Println(ok)
	// ok = judgePoint24([]int{1, 2, 1, 2})
	// fmt.Println(ok)

	// 6/(1 - 3/4)
	ok := judgePoint24([]int{1, 3, 4, 6})
	fmt.Println(ok)
}
