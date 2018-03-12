def expand(format, d, marker='"', safe=False):
  if safe:
    def lookup(w): return d.get(w, w.join(marker * 2))
  else:
    def lookup(w): return d[w]

  parts = format.split(marker)
  # This part of code expect the marker, in this case is double quote '"' is always
  # used in a pair. So in that case, it can use stride 2 in the below code, it starts
  # from the second element in the array, then travles the array using step 2.
  parts[1::2] = map(lookup, parts[1::2])
  return ''.join(parts)


if __name__ == '__main__':
  print expand('""just "a" test test test"a""a" "a" "a" ', {'a': 'one'}, safe=True)