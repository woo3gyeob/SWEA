dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pos = [[0] for _ in range(N * N + 1)]
    cnt = [1] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            pos[arr[i][j]] = [i, j]
    for i in range(1, N * N + 1):
        r, c = pos[i]
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if nr > -1 and nr < N and nc > -1 and nc < N and i + 1 == arr[nr][nc]:
                cnt[i + 1] = cnt[i] + 1

    val = max(cnt)
    num = cnt.index(val)
    print('#%d %d %d' % (tc, num - val + 1, val))