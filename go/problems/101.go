package problems

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}

	var mirrored func(l, r *TreeNode) bool
	mirrored = func(l, r *TreeNode) bool {
		if (l != nil && r == nil) || (l == nil && r != nil) {
			return false
		}

		if l == nil && r == nil {
			return true
		}

		if l.Val != r.Val {
			return false
		}

		return mirrored(l.Right, r.Left) && mirrored(l.Left, r.Right)
	}

	return mirrored(root.Left, root.Right)
}
