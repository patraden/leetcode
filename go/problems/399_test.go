package problems

import "testing"

func TestCalcEquation(t *testing.T) {
	tests := []struct {
		name      string
		equations [][]string
		values    []float64
		queries   [][]string
		want      []float64
	}{
		{
			name:      "test 1",
			equations: [][]string{{"a", "b"}, {"b", "c"}},
			values:    []float64{2.0, 3.0},
			queries:   [][]string{{"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}},
			want:      []float64{6.0, 0.5, -1.0, 1.0, -1.0},
		},
		{
			name:      "test 2",
			equations: [][]string{{"a", "b"}, {"b", "c"}, {"bc", "cd"}},
			values:    []float64{1.5, 2.5, 5.0},
			queries:   [][]string{{"a", "c"}, {"c", "b"}, {"bc", "cd"}, {"cd", "bc"}},
			want:      []float64{3.75, 0.4, 5.0, 0.2},
		},
		{
			name:      "test 3",
			equations: [][]string{{"a", "b"}},
			values:    []float64{0.5},
			queries:   [][]string{{"a", "b"}, {"b", "a"}, {"a", "c"}, {"x", "y"}},
			want:      []float64{0.5, 2.0, -1.0, -1.0},
		},
		{
			name:      "test 4",
			equations: [][]string{{"a", "e"}, {"b", "e"}},
			values:    []float64{4.0, 3.0},
			queries:   [][]string{{"a", "b"}, {"e", "e"}, {"x", "x"}},
			want:      []float64{4.0 / 3.0, 1.0, -1.0},
		},
		{
			name:      "test 5",
			equations: [][]string{{"x1", "x2"}, {"x2", "x3"}, {"x3", "x4"}, {"x4", "x5"}},
			values:    []float64{3.0, 4.0, 5.0, 6.0},
			queries:   [][]string{{"x1", "x5"}, {"x5", "x2"}, {"x2", "x4"}, {"x2", "x2"}, {"x2", "x9"}, {"x9", "x9"}},
			want:      []float64{360.0, 0.008333333333333333, 20.0, 1.0, -1.0, -1.0},
		},
		{
			name:      "test 6",
			equations: [][]string{{"a", "b"}, {"e", "f"}, {"b", "e"}},
			values:    []float64{3.4, 1.4, 2.3},
			queries:   [][]string{{"b", "a"}, {"a", "f"}, {"f", "f"}, {"e", "e"}, {"c", "c"}, {"a", "c"}, {"f", "e"}},
			want:      []float64{0.29411764705882354, 10.947999999999999, 1.00000, 1.00000, -1.00000, -1.00000, 0.7142857142857143},
		},
		{
			name:      "test 7",
			equations: [][]string{{"a", "b"}, {"b", "c"}, {"d", "e"}, {"a", "d"}},
			values:    []float64{1.0, 2.0, 3.0, 4.0},
			queries:   [][]string{{"c", "e"}},
			want:      []float64{6.0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := CalcEquation(tt.equations, tt.values, tt.queries)
			if len(got) != len(tt.want) {
				t.Errorf("length diff got = %v, want %v", len(got), len(tt.want))
			}
			for i := range got {
				if got[i] != tt.want[i] {
					t.Errorf("diff at index %v got = %v, want %v", i, got[i], tt.want[i])
				}
			}
		})
	}

}
