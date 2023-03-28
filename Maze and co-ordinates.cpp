#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
int maze[MAXN][MAXN];
bool visited[MAXN][MAXN];

bool dfs(int x, int y, int end_x, int end_y, int n, int m) {
    if (x == end_x && y == end_y) {
        return true;
    }
    visited[x][y] = true;
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if ((dx == 0 || dy == 0) && dx != dy) {
                int next_x = x + dx, next_y = y + dy;
                if (next_x >= 0 && next_x < n && next_y >= 0 && next_y < m &&
                    !visited[next_x][next_y] && maze[next_x][next_y] <= maze[x][y]) {
                    if (dfs(next_x, next_y, end_x, end_y, n, m)) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    int start_x, start_y, end_x, end_y;
    scanf("%d %d %d %d", &start_x, &start_y, &end_x, &end_y);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
            visited[i][j] = false;
        }
    }
    if (dfs(start_x-1, start_y-1, end_x-1, end_y-1, n, m)) {
        printf("Hie Barua\n");
    } else {
        printf("No Chance\n");
    }
    return 0;
}
