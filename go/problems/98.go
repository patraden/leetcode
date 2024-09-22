package problems

func helper(root *TreeNode, min int, max int) bool {
	if root == nil {
		return true
	}
	if root.Val >= max || root.Val <= min {
		return false
	}
	return helper(root.Left, min, root.Val) && helper(root.Right, root.Val, max)
}

func isValidBST(root *TreeNode) bool {
	return helper(root, -2147483649, 2147483648)
}
