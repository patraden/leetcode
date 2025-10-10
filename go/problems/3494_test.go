package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinTime3494(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name  string
		skill []int
		mana  []int
		want  int64
	}{
		{
			name:  "test 1",
			skill: []int{1, 5, 2, 4},
			mana:  []int{5, 1, 4, 2},
			want:  110,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := minTime3494(tt.skill, tt.mana)
			assert.Equal(t, tt.want, got)
		})
	}
}
