package problems

type DisjointSet struct {
	parents map[string]string
	weights map[string]float64
}

func (ds *DisjointSet) MakeSet(name string) {
	if _, ok := ds.parents[name]; !ok {
		ds.parents[name] = name
		ds.weights[name] = 1.0
	}
}

func (ds *DisjointSet) Find(name string) (string, bool) {

	if _, ok := ds.parents[name]; !ok {
		return name, false
	}

	e, parent := name, ds.parents[name]

	stack := []string{}

	for e != parent {
		stack = append(stack, e)
		e = parent
		parent = ds.parents[e]
	}

	w := 1.0
	for i := len(stack) - 1; i >= 0; i-- {
		e = stack[i]
		w *= ds.weights[e]
		ds.parents[e] = parent
		ds.weights[e] = w
	}

	return parent, true

}

func (ds *DisjointSet) Union(name1 string, name2 string, w float64) {
	name1Parent, _ := ds.Find(name1)
	name2Parent, _ := ds.Find(name2)

	if name1Parent != name2Parent {
		ds.parents[name1Parent] = name2Parent
		ds.weights[name1Parent] = w * ds.weights[name2] / ds.weights[name1]
	}

}

func CalcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	ds := DisjointSet{
		parents: map[string]string{},
		weights: map[string]float64{},
	}

	for i, eq := range equations {
		ds.MakeSet(eq[0])
		ds.MakeSet(eq[1])
		ds.Union(eq[0], eq[1], values[i])

	}

	res := []float64{}
	for _, eq := range queries {
		s, t := eq[0], eq[1]

		tp, tok := ds.Find(t)
		sp, sok := ds.Find(s)

		if !tok || !sok || tp != sp {
			res = append(res, -1.0)
		} else {
			res = append(res, float64(ds.weights[s]/ds.weights[t]))
		}
	}

	return res
}
