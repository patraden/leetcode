package problems

import (
	"leetcode/datastructures/binarytree"
	"math"
)

func inorder(node *binarytree.TreeNode, prev *int, res *int) {
	if node == nil {
		return
	}
	inorder(node.Left, prev, res)
	if *prev != math.MaxInt {
		*res = min(*res, abs(node.Val-*prev))
	}
	*prev = node.Val
	inorder(node.Right, prev, res)

}

func getMinimumDifference530(root *binarytree.TreeNode) int {
	res, prev := math.MaxInt, math.MaxInt
	inorder(root, &prev, &res)
	return res
}
