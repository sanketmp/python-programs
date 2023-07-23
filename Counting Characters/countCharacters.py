def countCharacters(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    print(count)


print(countCharacters("GithubSampleCodes"))