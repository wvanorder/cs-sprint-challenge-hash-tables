# Your code here
import re


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result =[]
    for fyle in files:
        fylearray = re.split("/", fyle)
        lastItem = fylearray[len(fylearray) - 1]
        s = "/"
        otherText = s.join(fylearray)
        if lastItem not in cache:
            cache[lastItem] = [otherText]
        else:
            cache[lastItem].append(otherText)

    for q in queries:
        if q in cache:
            for i in cache[q]:
                result.append(i)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
