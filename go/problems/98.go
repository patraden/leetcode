package problems

import (
	"leetcode/datastructures/binarytree"
	"math"
)

func helper(root *binarytree.TreeNode, min int, max int) bool {
	if root == nil {
		return true
	}
	if root.Val >= max || root.Val <= min {
		return false
	}
	return helper(root.Left, min, root.Val) && helper(root.Right, root.Val, max)
}

func isValidBST(root *binarytree.TreeNode) bool {
	return helper(root, math.MinInt, math.MaxInt)
}
