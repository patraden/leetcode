package problems

import "container/heap"

type Task3408 struct {
	id       int
	userID   int
	priority int
	index    int
}

func NewTask3408(id, userID, priority int) *Task3408 {
	return &Task3408{
		id:       id,
		userID:   userID,
		priority: priority,
		index:    -1,
	}
}

func (t *Task3408) Set(priority int) {
	t.priority = priority
}

type PriorityQueue3408 []*Task3408

func (pq PriorityQueue3408) Len() int { return len(pq) }

func (pq PriorityQueue3408) Less(i, j int) bool {
	if pq[i].priority == pq[j].priority {
		return pq[i].id > pq[j].id
	}

	return pq[i].priority > pq[j].priority
}

func (pq PriorityQueue3408) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue3408) Push(x any) {
	n := len(*pq)
	item := x.(*Task3408)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue3408) Pop() any {
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

type TaskManager struct {
	pq    *PriorityQueue3408
	tasks map[int]*Task3408
}

func ConstructorTM(tasks [][]int) TaskManager {
	tasksMap := make(map[int]*Task3408)
	pq := &PriorityQueue3408{}
	heap.Init(pq)

	for _, task := range tasks {
		id, userID, p := task[1], task[0], task[2]
		t := NewTask3408(id, userID, p)
		tasksMap[id] = t
		heap.Push(pq, t)
	}

	return TaskManager{
		pq:    pq,
		tasks: tasksMap,
	}

}

func (tm *TaskManager) Add(userId int, taskId int, priority int) {
	if _, ok := tm.tasks[taskId]; !ok {
		t := NewTask3408(taskId, userId, priority)
		tm.tasks[taskId] = t
		heap.Push(tm.pq, t)
	}
}

func (tm *TaskManager) Edit(taskId int, newPriority int) {
	if _, ok := tm.tasks[taskId]; ok {
		item := tm.tasks[taskId]
		item.Set(newPriority)
		heap.Fix(tm.pq, item.index)
	}
}

func (tm *TaskManager) Rmv(taskId int) {
	if _, ok := tm.tasks[taskId]; ok {
		item := tm.tasks[taskId]
		delete(tm.tasks, taskId)
		heap.Remove(tm.pq, item.index)
	}

}

func (tm *TaskManager) ExecTop() int {
	if tm.pq.Len() > 0 {
		item := heap.Pop(tm.pq)
		if task, ok := item.(*Task3408); ok {
			delete(tm.tasks, task.id)
			return task.userID
		}

	}

	return -1
}
