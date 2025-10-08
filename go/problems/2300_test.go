package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSuccessfulPairs(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name    string
		spells  []int
		potions []int
		success int64
		want    []int
	}{
		{
			name:    "test 1",
			spells:  []int{5, 1, 3},
			potions: []int{1, 2, 3, 4, 5},
			success: 7,
			want:    []int{4, 0, 3},
		},
		{
			name:    "test 2",
			spells:  []int{3, 1, 2},
			potions: []int{8, 5, 8},
			success: 16,
			want:    []int{2, 0, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := successfulPairs(tt.spells, tt.potions, tt.success)
			assert.Equal(t, tt.want, got)
		})
	}
}
