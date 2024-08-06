def check_different_two_cnt(word):
    is_result_different = False
    cnt = 0

    for i in range(len(word)):
        for j in range(i + 1, len(word) - i - 1):
            if word[i] != word[j]:
                cnt += 1
            
        if cnt >= 2:
            is_result_different = True

    if is_result_different:
        print('Yes')
    else:
        print('No')

A = list(input())

check_different_two_cnt(A)