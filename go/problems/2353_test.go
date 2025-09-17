package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFoodRatingsTest1(t *testing.T) {
	t.Parallel()

	foods := []string{"kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"}
	cuisines := []string{"korean", "japanese", "japanese", "greek", "japanese", "korean"}
	ratings := []int{9, 12, 8, 15, 14, 7}

	fr := Constructor(foods, cuisines, ratings)

	assert.Equal(t, "kimchi", fr.HighestRated("korean"))
	assert.Equal(t, "ramen", fr.HighestRated("japanese"))
	fr.ChangeRating("sushi", 16)
	assert.Equal(t, "sushi", fr.HighestRated("japanese"))
	fr.ChangeRating("ramen", 16)
	assert.Equal(t, "ramen", fr.HighestRated("japanese"))

}
