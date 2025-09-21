package problems

import "container/heap"

type Movie struct {
	id    int
	shop  int
	price int
	index int
}

type PriorityQueueMRS []*Movie

func (pq PriorityQueueMRS) Len() int { return len(pq) }

func (pq PriorityQueueMRS) Less(i, j int) bool {
	if pq[i].price == pq[j].price && pq[i].shop == pq[j].shop {
		return pq[i].id < pq[j].id
	}

	if pq[i].price == pq[j].price {
		return pq[i].shop < pq[j].shop
	}

	return pq[i].price < pq[j].price
}

func (pq PriorityQueueMRS) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueueMRS) Push(x any) {
	if item, ok := x.(*Movie); ok {
		item.index = len(*pq)
		*pq = append(*pq, item)
	}
}

func (pq *PriorityQueueMRS) Pop() any {
	old := *pq
	n := len(old)
	if n == 0 {
		return nil
	}

	item := old[n-1]
	old[n-1] = nil  // don't stop the GC from reclaiming the item eventually
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

type MovieRentingSystem struct {
	n        int
	movies   map[int]map[int]*Movie
	unrented map[int]*PriorityQueueMRS
	rented   *PriorityQueueMRS
}

func ConstructorMRS(n int, entries [][]int) MovieRentingSystem {
	unrented := make(map[int]*PriorityQueueMRS)
	movies := make(map[int]map[int]*Movie)
	rented := &PriorityQueueMRS{}
	heap.Init(rented)

	for _, e := range entries {
		m := &Movie{
			shop:  e[0],
			id:    e[1],
			price: e[2],
			index: -1,
		}

		if _, ok := movies[m.shop]; !ok {
			movies[m.shop] = make(map[int]*Movie)
		}
		movies[m.shop][m.id] = m

		if _, ok := unrented[m.id]; !ok {
			pq := &PriorityQueueMRS{}
			heap.Init(pq)
			unrented[m.id] = pq
		}
		heap.Push(unrented[m.id], m)
	}

	return MovieRentingSystem{
		n:        n,
		movies:   movies,
		unrented: unrented,
		rented:   rented,
	}
}

func (mrs *MovieRentingSystem) Search(movie int) []int {
	res, movies := []int{}, make([]*Movie, 0, 5)
	if q, ok := mrs.unrented[movie]; ok {
		i := 0
		for i < 5 && q.Len() > 0 {
			item := heap.Pop(q)
			if m, ok := item.(*Movie); ok {
				res = append(res, m.shop)
				movies = append(movies, m)
			}
			i++
		}

		for _, m := range movies {
			heap.Push(q, m)
		}
	}

	return res
}

func (mrs *MovieRentingSystem) Rent(shop int, movie int) {
	m, ok := mrs.movies[shop][movie]
	if !ok {
		return
	}

	if q, ok := mrs.unrented[movie]; ok {
		heap.Remove(q, m.index)
		heap.Push(mrs.rented, m)
	}
}

func (mrs *MovieRentingSystem) Drop(shop int, movie int) {
	m, ok := mrs.movies[shop][movie]
	if !ok {
		return
	}

	heap.Remove(mrs.rented, m.index)
	heap.Push(mrs.unrented[m.id], m)
}

func (mrs *MovieRentingSystem) Report() [][]int {
	res, movies := [][]int{}, make([]*Movie, 0, 5)

	i := 0
	for i < 5 && mrs.rented.Len() > 0 {
		item := heap.Pop(mrs.rented)
		if m, ok := item.(*Movie); ok {
			res = append(res, []int{m.shop, m.id})
			movies = append(movies, m)
		}
		i++
	}

	for _, m := range movies {
		heap.Push(mrs.rented, m)
	}

	return res
}
