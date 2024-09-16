package problems

import "testing"

func TestFindMinDifference(t *testing.T) {
	tests := []struct {
		name       string
		timePoints []string
		want       int
	}{
		{
			name:       "test 1",
			timePoints: []string{"23:59", "00:00"},
			want:       1,
		},
		{
			name:       "test 2",
			timePoints: []string{"00:00", "23:59", "00:00"},
			want:       0,
		},
		{
			name:       "test 3",
			timePoints: []string{"23:59", "22:51", "22:54"},
			want:       3,
		},
		{
			name:       "test 4",
			timePoints: []string{"05:31", "22:08", "00:35"},
			want:       147,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindMinDifference(tt.timePoints); got != tt.want {
				t.Errorf("got = %v, want %v", got, tt.want)
			}
		})
	}

}
