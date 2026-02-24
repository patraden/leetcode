package problems

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func validateFlattenHelper(t *testing.T, root *TreeNode) {
	t.Helper()

	node := root
	for node != nil {
		fmt.Println(node.Val)
		require.Nil(t, node.Left)
		node = node.Right
	}
}

func testTreeNode(t *testing.T) *TreeNode {
	node := &TreeNode{Val: 1}
	node.Left = &TreeNode{Val: 2}
	node.Right = &TreeNode{Val: 5}
	node.Left.Left = &TreeNode{Val: 3}
	node.Left.Right = &TreeNode{Val: 4}
	node.Right.Right = &TreeNode{Val: 6}

	return node
}

func TestFlatten(t *testing.T) {
	t.Parallel()

	node := testTreeNode(t)
	flatten(node)
	validateFlattenHelper(t, node)
}
