package problems

import "testing"

func TestNumberOfPairs(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name   string
		points [][]int
		want   int
	}{
		{
			name:   "test 1",
			points: [][]int{{1, 1}, {2, 2}, {3, 3}},
			want:   0,
		},
		{
			name:   "test 2",
			points: [][]int{{6, 2}, {4, 4}, {2, 6}},
			want:   2,
		},
		{
			name:   "test 3",
			points: [][]int{{3, 1}, {1, 3}, {1, 1}},
			want:   2,
		},
		{
			name:   "test 4",
			points: [][]int{{1, 5}, {2, 0}, {5, 5}},
			want:   2,
		},
		{
			name:   "test 5",
			points: [][]int{{0, 0}, {0, 3}},
			want:   1,
		},
		{
			name:   "test 5",
			points: [][]int{{0, 0}, {0, 2}, {0, 3}},
			want:   2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberOfPairs(tt.points); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
