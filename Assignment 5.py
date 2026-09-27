# Longest Common Subsequence using Dynamic Programming

def lcs(str1, str2):

    m = len(str1)
    n = len(str2)

    # Create table
    table = [[0 for j in range(n + 1)]
             for i in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1

            else:
                table[i][j] = max(
                    table[i - 1][j],
                    table[i][j - 1]
                )

    length = table[m][n]

    # Find the LCS
    i = m
    j = n
    answer = []

    while i > 0 and j > 0:

        if str1[i - 1] == str2[j - 1]:
            answer.append(str1[i - 1])
            i -= 1
            j -= 1

        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1

        else:
            j -= 1

    answer.reverse()

    return length, ''.join(answer)


# Main Program

str1 = input("Enter first sequence: ")
str2 = input("Enter second sequence: ")

length, answer = lcs(str1, str2)

print("\nLongest Common Subsequence:", answer)
print("Length of LCS:", length)