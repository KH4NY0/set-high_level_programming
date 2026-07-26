# Python - Everything is Object

Identity versus equality, mutable versus immutable types, how names are bound
to objects, and CPython's small integer cache and string interning.

## Files

| File | Topic |
| --- | --- |
| `0-answer.txt`, `1-answer.txt` | `type` and `id` |
| `2-answer.txt` - `5-answer.txt` | Integer identity and the small int cache |
| `6-answer.txt` - `9-answer.txt` | String `==` versus `is` |
| `10-answer.txt` - `13-answer.txt` | List `==` versus `is` |
| `14-answer.txt` - `18-answer.txt` | Mutation versus rebinding, including in functions |
| `19-copy_list.py` | `copy_list()` - returns a shallow copy of a list |
| `20-answer.txt` - `23-answer.txt` | What actually makes a tuple |
| `24-answer.txt` - `26-answer.txt` | Tuple identity, and the empty tuple singleton |
| `27-answer.txt`, `28-answer.txt` | `a = a + [x]` versus `a += [x]` |
| `100-magic_string.py` | `magic_string()` - the mutable default argument trick |
| `101-locked_class.py` | `LockedClass` - attribute locking with `__slots__` |
| `103-*.txt` | How many int objects `a = 1` creates |
| `104-*.txt` | The same question for `1024`, outside the cache |
| `105-line1.txt` | How many ints exist before the second `print` |
| `106-*.txt` | The same questions for interned strings |
