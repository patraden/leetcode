package problems

import (
	"fmt"
	"leetcode/datastructures/binarytree"
	"testing"
)

func validateconnectNodesRightHelper(t *testing.T, root *binarytree.NodeR) {
	t.Helper()

	binarytree.InOrderTraversal(root, func(node *binarytree.NodeR) {
		fmt.Println("val:", node.Val)
		if node.Next != nil {
			fmt.Println("next:", node.Next.Val)
		} else {
			fmt.Println("next:nil")
		}
	})
}

func TestConnectNodesRight(t *testing.T) {
	t.Parallel()

	node := &binarytree.NodeR{Val: 1}
	node.Left = &binarytree.NodeR{Val: 2}
	node.Right = &binarytree.NodeR{Val: 3}
	node.Left.Left = &binarytree.NodeR{Val: 4}
	node.Left.Right = &binarytree.NodeR{Val: 5}
	node.Right.Right = &binarytree.NodeR{Val: 7}

	connectNodesRight(node)
	validateconnectNodesRightHelper(t, node)
}
