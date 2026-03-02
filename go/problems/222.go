package problems

func countNodes(root *TreeNode) int {

	fullTreeCount := func(root *TreeNode) (bool, int) {
		if root == nil {
			return true, 0
		}

		res := 2
		l, r := root.Left, root.Right
		for l != nil && r != nil {
			res *= 2
			r = r.Right
			l = l.Left
		}

		if r == nil && l == nil {
			return true, res - 1
		}

		return false, 0
	}

	if ok, cnt := fullTreeCount(root); ok {
		return cnt
	}

	if ok, cnt := fullTreeCount(root.Right); ok {
		return cnt + 1 + countNodes(root.Left)
	}

	if ok, cnt := fullTreeCount(root.Left); ok {
		return cnt + 1 + countNodes(root.Right)
	}

	// tree is not balanced
	return -1
}
