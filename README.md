This repository is experimental, based on the following discussion on Reddit: https://www.reddit.com/r/golang/comments/11spdom/go_is_23_times_slower_than_js_in_a_similar_code/. It is a simple attempt to test Python and mypyc on a basic function that finds prime numbers within a given range.

Run and test:

```bash
make dev-install
make run
```

Output

```
...
21:48:21,307 INFO: Last prime 199999 | Took 905 ms
```
