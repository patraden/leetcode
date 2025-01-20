package problems

type Node struct {
	Alphabet map[rune]*Node
	Count    int
}

func NewNode() *Node {
	return &Node{
		Alphabet: map[rune]*Node{},
		Count:    0,
	}
}

func sumPrefixScores(words []string) []int {
	res := make([]int, len(words))
	root := NewNode()

	for _, word := range words {
		node := root
		for _, r := range word {
			if v, ok := node.Alphabet[r]; ok {
				node = v
			} else {
				node.Alphabet[r] = NewNode()
				node = node.Alphabet[r]
			}
			node.Count += 1
		}
	}

	for i, word := range words {
		c := 0
		node := root
		for _, r := range word {
			node = node.Alphabet[r]
			c += node.Count
		}
		res[i] = c
	}

	return res
}
