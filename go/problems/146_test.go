package problems

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestLRUCache_HappyPath(t *testing.T) {
	t.Parallel()

	cacheCap := 2
	tests := []struct {
		op  string
		key int
		val int
	}{
		{"put", 1, 1},
		{"put", 2, 2},
		{"get", 1, 1},
		{"put", 3, 3},
		{"get", 2, -1},
		{"put", 4, 4},
		{"get", 1, -1},
		{"get", 3, 3},
		{"get", 4, 4},
	}

	cache := LRUCacheConstructor(cacheCap)
	for _, tcase := range tests {
		t.Run("happy path test", func(t *testing.T) {
			switch tcase.op {
			case "put":
				cache.Put(tcase.key, tcase.val)
			case "get":
				res := cache.Get(tcase.key)
				require.Equal(t, tcase.val, res)
			default:
			}
		})
	}
}

func TestLRUCache_CapacityOne(t *testing.T) {
	t.Parallel()

	cacheCap := 1
	tests := []struct {
		op  string
		key int
		val int
	}{
		{"put", 1, 1},
		{"put", 2, 2},
		{"get", 1, -1},
		{"put", 3, 3},
		{"get", 2, -1},
		{"get", 3, 3},
	}

	cache := LRUCacheConstructor(cacheCap)
	for _, tcase := range tests {
		t.Run("capacity one test", func(t *testing.T) {
			switch tcase.op {
			case "put":
				cache.Put(tcase.key, tcase.val)
			case "get":
				res := cache.Get(tcase.key)
				require.Equal(t, tcase.val, res)
			default:
			}
		})
	}

	require.Equal(t, 3, cache.lru.v)
	require.Equal(t, 3, cache.mru.v)
}
