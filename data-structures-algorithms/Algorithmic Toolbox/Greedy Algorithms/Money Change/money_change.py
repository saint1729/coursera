# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    ans = money // 10
    money %= 10
    ans += (money // 5)
    money %= 5

    return ans + money


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
