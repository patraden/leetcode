package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMaxBottlesDrunk3100(t *testing.T) {
	tests := []struct {
		name        string
		numBottles  int
		numExchange int
		want        int
	}{
		{
			name:        "test 1",
			numBottles:  13,
			numExchange: 6,
			want:        15,
		},
		{
			name:        "test 2",
			numBottles:  10,
			numExchange: 3,
			want:        13,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxBottlesDrunk3100(tt.numBottles, tt.numExchange)
			assert.Equal(t, tt.want, got)
		})
	}
}
