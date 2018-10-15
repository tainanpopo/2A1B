# author : Eric Lin
import random

# 規則如下 : https://zh.wikipedia.org/wiki/%E7%8C%9C%E6%95%B0%E5%AD%97
# 如果有出現重複的數字，則重複的數字每個也只能算一次，且以最優的結果為準，
# 如正確答案為5543，猜的人猜5255，則在這裡不能認為猜測的第一個5對正確答案第二個，
# 根據最優結果為準的原理和每個數字只能有一次的規則，兩個比較後應該為1A1B，第一個5位子正確，記為1A；
# 猜測數字中的第三個5或第四個5和答案的第二個5匹配，只能記為1B。
# 當然，如果有猜5267中的第一個5不能與答案中的第二個5匹配，因此只能記作1A0B。


def cut(tmp, i):  # 將已經確定是A的數字去掉
    left = tmp[:i]
    right = tmp[i+1:]
    tmp = left + right
    return tmp


def main(times, ans):
    while True:
        tmp_ans = ans
        while True:
            word = input('請輸入一個5位數數字:')
            tmp_word = word
            if len(word) == 5:
                break
            else:
                print('輸入5位數數字啦幹!')

        a = 0  # 數字對，位置也對
        b = 0  # 數字對，位置錯
        a_array = []  # 儲存已經有的 A
        repeat_number = []  # 儲存重複的字元

        for i in range(len(word)):
            if word[i] == ans[i]:  # 題目跟回答的數字位置都對，就是 A
                a += 1
                a_array.append(word[i])

        count = 0
        # print(a)
        while True:  # 開始去做切割字串，把 A 去除
            if count == a:
                break
            # print(tmp_ans)
            # print(tmp_word)
            for i in range(len(tmp_word)):
                # print('-------------')
                if tmp_word[i] == tmp_ans[i]:  # 找到一個 A 就開切。
                    count += 1
                    tmp_ans = cut(tmp_ans, i)
                    tmp_word = cut(tmp_word, i)
                    # print(tmp_ans)
                    # print(tmp_word)
                    break

        # print('出來囉')
        # print(a_array)

        b_array = []  # 儲存 B，根據最優結果為準的原理和每個數字只能有一次的規則，避免已經有的數字卻重複計算。
        for i in range(len(tmp_word)):
            if tmp_word[i] in tmp_ans and tmp_word[i] != tmp_ans[i] and tmp_word[i] not in b_array:
                b += 1
                b_array.append(tmp_word[i])

        if ans == word:
            if times == 0:
                print('Ans : {} 一次就答對囉!'.format(ans))
                break
            else:
                print('兄ㄉㄟˇ，猜了%s次才答對，真D菜!' % times)
                break
        else:
            print('{}A{}B'.format(a, b))
            times += 1


if __name__ == "__main__":
    print("*" * 5 + "猜數字遊戲" + "*" * 5)
    times = 0  # 記錄總共猜了幾次
    digit = ('0123456789')
    ans = ''.join(random.sample(digit, 5))  # 多個字元中選取特定數量的字元
    print(ans)
    main(times, ans)
