package problems

type LRUCacheNode struct {
	k    int
	v    int
	Prev *LRUCacheNode
	Next *LRUCacheNode
}

type LRUCache struct {
	capacity int
	elems    map[int]*LRUCacheNode
	mru      *LRUCacheNode
	lru      *LRUCacheNode
}

func LRUCacheConstructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		elems:    make(map[int]*LRUCacheNode, capacity),
	}
}

func (c *LRUCache) asMRU(e *LRUCacheNode, exists bool) {
	if c.mru == nil {
		c.mru = e
		c.lru = e
		return
	}

	if !exists {
		c.mru.Prev = e
		e.Next = c.mru
		c.mru = e

		return
	}

	if e == c.mru {
		return
	}

	if e == c.lru {
		e.Prev.Next = nil
		c.lru = e.Prev
	} else {
		e.Prev.Next = e.Next
		e.Next.Prev = e.Prev
	}

	// e is mru now
	e.Prev = nil
	e.Next = c.mru
	c.mru.Prev = e
	c.mru = e
}

func (c *LRUCache) complyCapacity() {
	if len(c.elems) < c.capacity {
		return
	}

	delete(c.elems, c.lru.k)

	if c.capacity == 1 {
		c.mru = nil
		c.lru = nil
		return
	}

	c.lru.Prev.Next = nil
	c.lru = c.lru.Prev
}

func (c *LRUCache) Get(key int) int {
	e, ok := c.elems[key]
	if !ok || e == nil {
		return -1
	}

	c.asMRU(e, true)
	return e.v
}

func (c *LRUCache) Put(key int, value int) {
	n := &LRUCacheNode{k: key, v: value}

	if e, exists := c.elems[key]; exists {
		e.v = n.v
		c.asMRU(e, exists)
		return
	}

	c.complyCapacity()
	c.elems[n.k] = n
	c.asMRU(n, false)
}
