package problems

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMergeTwoLists(t *testing.T) {
	t.Parallel()

	s := &ListNode{
		Val: 4,
		Next: &ListNode{
			Val: 5,
			Next: &ListNode{
				Val: 5,
			},
		},
	}

	f := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val: 4,
			},
		},
	}

	res := mergeTwoLists(s, f)
	require.NotNil(t, res)

	for res != nil {
		fmt.Println(res)
		res = res.Next
	}
}
