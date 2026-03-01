package problems

import "leetcode/datastructures/binarytree"

func connectNodesRight(root *binarytree.NodeR) *binarytree.NodeR {
	// s - starting node in the layer
	// c - current node in the layer
	var c, s *binarytree.NodeR

	s = root
	for s != nil {
		c = s
		s = nil
		// on current level all Next nodes are resolved
		for c != nil {
			children := []*binarytree.NodeR{}
			if c.Left != nil {
				if s == nil {
					s = c.Left
				}

				if c.Right != nil {
					c.Left.Next = c.Right
				} else {
					children = append(children, c.Left)
				}

			}

			if c.Right != nil {
				if s == nil {
					s = c.Right
				}
				children = append(children, c.Right)
			}

			for _, child := range children {
				if child.Next != nil {
					continue
				}

				cn := c.Next
				for cn != nil {
					if cn.Left != nil {
						child.Next = cn.Left
						break
					}
					if cn.Right != nil {
						child.Next = cn.Right
						break
					}
					cn = cn.Next
				}
			}
			c = c.Next
		}
	}

	return nil

}
