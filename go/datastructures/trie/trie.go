package trie

type TrieNode struct {
	Alphabet   map[rune]*TrieNode
	IsTerminal bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{
		Alphabet:   map[rune]*TrieNode{},
		IsTerminal: false,
	}
}

func (t *TrieNode) Add(word string) {
	node := t
	for _, r := range word {
		if v, ok := node.Alphabet[r]; ok {
			node = v
		} else {
			node.Alphabet[r] = NewTrieNode()
			node = node.Alphabet[r]
		}
	}
	node.IsTerminal = true
}
