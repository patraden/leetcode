package problems

import (
	"math"
)

func inorder(node *TreeNode, prev *int, res *int) {
	if node == nil {
		return
	}
	inorder(node.Left, prev, res)
	if *prev != math.MaxInt {
		*res = min(*res, abs(node.Val, *prev))
	}
	*prev = node.Val
	inorder(node.Right, prev, res)

}

func getMinimumDifference530(root *TreeNode) int {
	res, prev := math.MaxInt, math.MaxInt
	inorder(root, &prev, &res)
	return res
}
