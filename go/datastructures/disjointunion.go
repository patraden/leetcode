/*
A disjoint-set—also called union-find—data structure keeps track of
nonoverlapping partitions of a collection of data elements.
Initially, each data element belongs to its own, singleton, set.

References:
https://en.wikipedia.org/wiki/Disjoint-set_data_structure
https://cp-algorithms.com/data_structures/disjoint_set_union.html
*/

package disjointunion

type Element struct {
	parent *Element // Parent element
	size   int      // Size of the subtree with this element as root
	Data   any      // Arbitrary user-provided payload
}

func NewElement() *Element {
	s := &Element{}
	s.parent = s
	s.size = 1
	return s
}

func (e *Element) Find() *Element {
	// stack is an optimization for tree compression which
	// collects elements on the path to the root
	// in order to update their roots later
	stack := []*Element{}

	for e.parent != e {
		stack = append(stack, e)
		e = e.parent
	}
	for _, o := range stack {
		o.parent = e
	}
	return e
}

func (e *Element) Union(o *Element) {
	eRoot := e.Find()
	oRoot := o.Find()

	if eRoot == oRoot {
		return
	}

	// Create a union by attaching the smaller tree to larger tree.
	if oRoot.size > eRoot.size {
		eRoot, oRoot = oRoot, eRoot
	}
	oRoot.parent = eRoot
	eRoot.size += oRoot.size

}
