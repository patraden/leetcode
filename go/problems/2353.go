package problems

import "container/heap"

type Item struct {
	name     string
	priority int
	index    int
}

func NewItem(name string, priority int) *Item {
	return &Item{
		name:     name,
		priority: priority,
		index:    -1,
	}
}

func (i *Item) Set(priority int) {
	i.priority = priority
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the highest, not lowest, priority so we use greater than here.
	if pq[i].priority == pq[j].priority {
		return pq[i].name < pq[j].name
	}

	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x any) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
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

func (pq *PriorityQueue) Top() *Item {
	if pq.Len() == 0 {
		return nil
	}

	return (*pq)[0]
}

type FoodRatings struct {
	foods          map[string]*Item
	foodCousine    map[string]string         // cousine for food
	cuisinesQueues map[string]*PriorityQueue // all foods of cousine
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	foodsMap := make(map[string]*Item)
	foodCousine := make(map[string]string)
	cuisinesQueues := make(map[string]*PriorityQueue)

	for i, food := range foods {
		cuisine, rating := cuisines[i], ratings[i]
		if _, ok := cuisinesQueues[cuisine]; !ok {
			pq := &PriorityQueue{}
			cuisinesQueues[cuisine] = pq
			heap.Init(pq)
		}

		foodCousine[food] = cuisine
		item := NewItem(food, rating)
		heap.Push(cuisinesQueues[cuisine], item)
		foodsMap[food] = item
	}

	return FoodRatings{
		foodCousine:    foodCousine,
		cuisinesQueues: cuisinesQueues,
		foods:          foodsMap,
	}
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	if item, exists := this.foods[food]; exists {
		item.Set(newRating)
		cuisine := this.foodCousine[food]
		heap.Fix(this.cuisinesQueues[cuisine], item.index)
	}
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	pq := this.cuisinesQueues[cuisine]
	top := pq.Top()
	if top == nil {
		return ""
	}

	return top.name
}
