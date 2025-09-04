package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinMovesToMakePalindrome(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name string
		s    string
		want int
	}{
		{
			"test 1",
			"aabb",
			2,
		},
		{
			"test 2",
			"letelt",
			2,
		},
		{
			"test 3",
			"aletelt",
			5,
		},
		{
			"test 4",
			"skwhhaaunskegmdtutlgtteunmuuludii",
			163,
		},
		{
			"test 5",
			"s",
			0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := minMovesToMakePalindrome(tt.s)
			assert.Equal(t, tt.want, got)
		})
	}
}
