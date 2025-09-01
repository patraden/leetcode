package problems

import "container/heap"

type Heap struct {
	classes [][]int
}

func (h *Heap) Len() int {
	return len(h.classes)
}

func (h *Heap) Less(i, j int) bool {
	// Calculate the improvement when adding one student to each class
	// For class i: (a+1)/(b+1) - a/b = (b-a)/(b+1)b
	// We want to maximize this improvement, so we use a max heap
	a1, b1 := h.classes[i][0], h.classes[i][1]
	a2, b2 := h.classes[j][0], h.classes[j][1]

	improvement1 := float64(b1-a1) / float64((b1+1)*b1)
	improvement2 := float64(b2-a2) / float64((b2+1)*b2)

	return improvement1 > improvement2
}

func (h *Heap) Swap(i, j int) {
	h.classes[i], h.classes[j] = h.classes[j], h.classes[i]
}

func (h *Heap) Push(x any) {
	h.classes = append(h.classes, x.([]int))
}

func (h *Heap) Pop() any {
	old := h.classes
	n := len(old)
	x := old[n-1]
	h.classes = old[0 : n-1]
	return x
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	h := &Heap{make([][]int, len(classes))}
	copy(h.classes, classes)
	heap.Init(h)

	for range extraStudents {
		bestClass := heap.Pop(h).([]int)
		bestClass[0]++ // pass
		bestClass[1]++ // total
		heap.Push(h, bestClass)
	}

	totalRatio := 0.0
	for _, class := range h.classes {
		totalRatio += float64(class[0]) / float64(class[1])
	}

	result := totalRatio / float64(len(classes))
	return result
}
