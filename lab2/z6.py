s = {"a": 12, "b":7, "c": 17}
if 'a' in s and s['a']<10:
        del s["a"]
if 'b' in s and s['b']<10:
        del s["b"]
if 'c' in s and s['c'] < 10:
        del s["c"]
print(s)