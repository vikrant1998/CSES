#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    cin >> h >> w;

    vector<string> maze(h);
    for (int i = 0; i < h; i++) cin >> maze[i];

    const int INF = INT_MAX;
    vector<vector<int>> monsterTime(h, vector<int>(w, INF));

    // 4 directions with their move letters (U, R, D, L).
    const int di[4] = {-1, 0, 1, 0};
    const int dj[4] = {0, 1, 0, -1};
    const char moveCh[4] = {'U', 'R', 'D', 'L'};

    // Multi-source BFS from every monster.
    deque<pair<int,int>> mq;
    int si = -1, sj = -1;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (maze[i][j] == 'M') {
                monsterTime[i][j] = 0;
                mq.push_back({i, j});
            } else if (maze[i][j] == 'A') {
                si = i; sj = j;
            }
        }
    }
    while (!mq.empty()) {
        auto [ci, cj] = mq.front(); mq.pop_front();
        for (int k = 0; k < 4; k++) {
            int ni = ci + di[k], nj = cj + dj[k];
            if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
            if (maze[ni][nj] == '#') continue;
            if (monsterTime[ni][nj] != INF) continue;
            monsterTime[ni][nj] = monsterTime[ci][cj] + 1;
            mq.push_back({ni, nj});
        }
    }

    // Player BFS from A, gated by arriving strictly before any monster.
    // parent[i][j] stores the direction index used to step INTO (i,j),
    // and visited marks cells so the queue drains and paths form a tree.
    vector<vector<int>> parentDir(h, vector<int>(w, -1));
    vector<vector<char>> visited(h, vector<char>(w, 0));
    vector<vector<int>> dist(h, vector<int>(w, 0));

    deque<pair<int,int>> aq;
    visited[si][sj] = 1;
    aq.push_back({si, sj});

    bool won = false;
    int wi = -1, wj = -1;

    while (!aq.empty()) {
        auto [ci, cj] = aq.front(); aq.pop_front();

        if (ci == 0 || ci == h - 1 || cj == 0 || cj == w - 1) {
            won = true; wi = ci; wj = cj;
            break;
        }

        for (int k = 0; k < 4; k++) {
            int ni = ci + di[k], nj = cj + dj[k];
            if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
            if (maze[ni][nj] == '#' || visited[ni][nj]) continue;
            if (dist[ci][cj] + 1 >= monsterTime[ni][nj]) continue;  // monster gets there first
            visited[ni][nj] = 1;
            dist[ni][nj] = dist[ci][cj] + 1;
            parentDir[ni][nj] = k;
            aq.push_back({ni, nj});
        }
    }

    if (!won) {
        cout << "NO\n";
        return 0;
    }

    // Reconstruct: walk backward from the boundary cell to A using parentDir.
    string path;
    int ci = wi, cj = wj;
    while (!(ci == si && cj == sj)) {
        int k = parentDir[ci][cj];
        path.push_back(moveCh[k]);
        ci -= di[k];  // step back to the parent cell
        cj -= dj[k];
    }
    reverse(path.begin(), path.end());

    cout << "YES\n";
    cout << path.size() << "\n";
    cout << path << "\n";

    return 0;
}
