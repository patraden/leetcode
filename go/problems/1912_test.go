package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMovieRentingSystemCase1(t *testing.T) {
	t.Parallel()

	n := 3
	entries := [][]int{
		{0, 1, 5},
		{0, 2, 6},
		{0, 3, 7},
		{1, 1, 4},
		{1, 2, 7},
		{2, 1, 5},
	}

	// fmt.Println("============")
	// for movie, q := range mrs.unrented {
	// 	fmt.Println(movie, q.Len())
	// }

	mrs := ConstructorMRS(n, entries)
	unrented := 0
	for _, q := range mrs.unrented {
		unrented += q.Len()
	}

	assert.Equal(t, 6, unrented)
	assert.Equal(t, 0, mrs.rented.Len())

	shops := mrs.Search(1)
	assert.Equal(t, []int{1, 0, 2}, shops)

	mrs.Rent(0, 1)
	mrs.Rent(1, 2)
	unrented = 0
	for _, q := range mrs.unrented {
		unrented += q.Len()
	}

	assert.Equal(t, 2, mrs.rented.Len())
	assert.Equal(t, 4, unrented)

	report := mrs.Report()
	assert.Equal(t, [][]int{{0, 1}, {1, 2}}, report)

	mrs.Drop(1, 2)
	unrented = 0
	for _, q := range mrs.unrented {
		unrented += q.Len()
	}

	assert.Equal(t, 1, mrs.rented.Len())
	assert.Equal(t, 5, unrented)

	shops = mrs.Search(2)
	assert.Equal(t, []int{0, 1}, shops)

}
