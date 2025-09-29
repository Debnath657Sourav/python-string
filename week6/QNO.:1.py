def process_queries(n, queries):
    q = Queue(n)
    results = []

    for query in queries:
        if query[0] == 1:
            q.enqueue(query[1])
        elif query[0] == 2:
            q.dequeue()
        elif query[0] == 3:
            results.append(q.getFront())
        elif query[0] == 4:
            results.append(q.getRear())
        elif query[0] == 5:
            results.append(q.isEmpty())
        elif query[0] == 6:
            results.append(q.isFull())

    return results
