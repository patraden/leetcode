package problems

import "testing"

func TestFindKthNumber440(t *testing.T) {
	tests := []struct {
		name string
		n    int
		k    int
		want int
	}{
		{
			name: "test 1",
			n:    13,
			k:    2,
			want: 10,
		},
		{
			name: "test 2",
			n:    957747794,
			k:    424238336,
			want: 481814499,
		},
		{
			name: "test 4",
			n:    999,
			k:    22,
			want: 118,
		},
		{
			name: "test 5",
			n:    10,
			k:    3,
			want: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findKthNumber440(tt.n, tt.k); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}
}
