package disjointunion

import (
	"math/rand"
	"testing"
)

func TestEvenOdd(t *testing.T) {
	const N = 1000
	sets := make([]*Element, N)
	for i := 0; i < N; i++ {
		sets[i] = NewElement()
	}

	// even numbers merged
	for i := 2; i < N; i += 2 {
		sets[i].Union(sets[i-2])
	}

	// odd numbers merged
	for i := 3; i < N; i += 2 {
		sets[i].Union(sets[i-2])
	}

	// Ensure that even numbers are in the same union as other even numbers
	// and odd numbers are in the same union as other oddn numbers.
	for i := 0; i < N*3; i++ {
		s1 := rand.Intn(N)
		s2 := rand.Intn(N)
		sameMod := s1%2 == s2%2
		sameRep := sets[s1].Find() == sets[s2].Find()
		if sameMod != sameRep {
			t.Fatalf("Should %d and %d lie in the same set?  The package incorrectly says %v.", s1, s2, sameRep)
		}
	}

}
