package problems

import (
	"math"
	"testing"
)

func TestMaxAverageRatio(t *testing.T) {
	tests := []struct {
		name          string
		classes       [][]int
		extraStudents int
		want          float64
	}{
		{
			name:          "test 1",
			classes:       [][]int{{1, 2}, {3, 5}, {2, 2}},
			extraStudents: 2,
			want:          0.78333,
		},
		{
			name:          "test 2",
			classes:       [][]int{{2, 4}, {3, 9}, {4, 5}, {2, 10}},
			extraStudents: 4,
			want:          0.53485,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := maxAverageRatio(tt.classes, tt.extraStudents)
			delta := 1e-5
			if math.Abs(got-tt.want) > delta {
				t.Errorf("got = %v, want %v, delta = %v", got, tt.want, delta)
			}
		})
	}
}
