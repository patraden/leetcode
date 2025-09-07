package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinOperations3495(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name    string
		queries [][]int
		want    int64
	}{
		{
			name:    "test 1",
			queries: [][]int{{1, 2}, {2, 4}},
			want:    3,
		},
		{
			name:    "test 2",
			queries: [][]int{{2, 6}},
			want:    4,
		},
		{
			name:    "test 3",
			queries: [][]int{{1, 21}},
			want:    23,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := minOperations3495(tt.queries)
			assert.Equal(t, tt.want, got)
		})
	}
}
