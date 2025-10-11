package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaximumTotalDamage(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name  string
		power []int
		want  int64
	}{
		{
			name:  "Test1",
			power: []int{1, 1, 3, 4},
			want:  6,
		},
		{
			name:  "Test2",
			power: []int{7, 1, 6, 6},
			want:  13,
		},
		{
			name:  "Test3",
			power: []int{1, 2, 3, 4, 5, 6},
			want:  9,
		},
		{
			name:  "Test4",
			power: []int{3, 2, 4, 2, 3, 3, 1, 3, 2},
			want:  12,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := maximumTotalDamage(tt.power)
			assert.Equal(t, tt.want, got)
		})
	}

}
