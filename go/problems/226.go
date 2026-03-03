package problems

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	l := invertTree(root.Left)
	r := invertTree(root.Right)

	root.Right = l
	root.Left = r

	return root
}
