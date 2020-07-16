import sys
sys.stdin = open("4880.txt")

# 다시 풀어보기
























def dfs(player1, player2):
    # print(player1, player2)
    if player1 == player2:
        return player1
    else:
        beforeLeague = dfs(player1, (player1 + player2)//2)
        afterLeague = dfs((player1 + player2)//2 + 1, player2)
        if cards[beforeLeague] == 1 and cards[afterLeague] == 2:
            return afterLeague
        elif cards[beforeLeague] == 2 and cards[afterLeague] == 3:
            return afterLeague
        elif cards[beforeLeague] == 3 and cards[afterLeague] == 1:
            return afterLeague
        elif cards[afterLeague] == 1 and cards[beforeLeague] == 2:
            return beforeLeague
        elif cards[afterLeague] == 2 and cards[beforeLeague] == 3:
            return beforeLeague
        elif cards[afterLeague] == 3 and cards[beforeLeague] == 1:
            return beforeLeague
        elif cards[beforeLeague] == cards[afterLeague]:
            return beforeLeague

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))

    print("#{} {}".format(tc, dfs(0, N-1) + 1))


    # while cards.count(0) != N - 1:
    #     print(cards)
    #     for c in range(len(cards)):
    #         i = -1
    #         if c and i != c:
    #             i = c
    #             continue
    #         if i != -1 and c:
    #             if cards[i] == 1 and cards[c] == 2:
    #                 cards[i] = 0
    #             elif cards[i] == 2 and cards[c] == 3:
    #                 cards[i] = 0
    #             elif cards[i] == 3 and cards[c] == 1:
    #                 cards[i] = 0
    #             elif cards[c] == 1 and cards[i] == 2:
    #                 cards[c] = 0
    #             elif cards[c] == 2 and cards[i] == 3:
    #                 cards[c] = 0
    #             elif cards[c] == 3 and cards[i] == 1:
    #                 cards[c] = 0
    #             elif cards[i] == cards[c]:
    #                 cards[i] = 0
    #             break
    # print(cards)