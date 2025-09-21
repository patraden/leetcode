package problems

import (
	"sort"
)

type Packet struct {
	source, destination, timestamp int
}

type ring struct {
	data []Packet
	head int // index of front
	size int // number of items
}

func newRing(capacity int) *ring {
	return &ring{data: make([]Packet, capacity)}
}

func (r *ring) empty() bool { return r.size == 0 }

// pushBack adds x to the tail.
// If full, it evicts and returns the evicted front; otherwise returns nil.
func (r *ring) pushBack(x Packet) *Packet {
	if len(r.data) == 0 {
		return nil
	}
	if r.size < len(r.data) {
		idx := (r.head + r.size) % len(r.data)
		r.data[idx] = x
		r.size++
		return nil
	}
	// full: overwrite front and advance head
	old := r.data[r.head]
	r.data[r.head] = x
	r.head = (r.head + 1) % len(r.data)
	return &old
}

// popFront removes and returns the front element.
func (r *ring) popFront() (Packet, bool) {
	if r.size == 0 {
		return Packet{}, false
	}
	v := r.data[r.head]
	r.head = (r.head + 1) % len(r.data)
	r.size--
	return v, true
}

type Router struct {
	q       *ring
	seen    map[Packet]struct{}
	byDest  map[int][]int // dest -> timestamps (non-decreasing)
	headIdx map[int]int   // dest -> live prefix offset
}

func ConstructorRouter(memoryLimit int) Router {
	return Router{
		q:       newRing(memoryLimit),
		seen:    make(map[Packet]struct{}),
		byDest:  make(map[int][]int),
		headIdx: make(map[int]int),
	}
}

func (rt *Router) AddPacket(source int, destination int, timestamp int) bool {
	p := Packet{source, destination, timestamp}
	if _, dup := rt.seen[p]; dup {
		return false
	}
	// Push; if evicted, clean indices for evicted packet
	if ev := rt.q.pushBack(p); ev != nil {
		delete(rt.seen, *ev)
		rt.headIdx[ev.destination]++
	}
	rt.seen[p] = struct{}{}
	rt.byDest[destination] = append(rt.byDest[destination], timestamp)
	return true
}

func (rt *Router) ForwardPacket() []int {
	p, ok := rt.q.popFront()
	if !ok {
		return []int{}
	}
	delete(rt.seen, p)
	rt.headIdx[p.destination]++
	return []int{p.source, p.destination, p.timestamp}
}

func (rt *Router) GetCount(destination int, startTime int, endTime int) int {
	arr := rt.byDest[destination]
	start := rt.headIdx[destination]
	if start > len(arr) {
		start = len(arr)
	}
	arr = arr[start:] // live suffix
	if len(arr) == 0 {
		return 0
	}
	left := sort.Search(len(arr), func(i int) bool { return arr[i] >= startTime })
	right := sort.Search(len(arr), func(i int) bool { return arr[i] > endTime })
	return right - left
}
