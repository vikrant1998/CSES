// CSES Flight Routes — k shortest path lengths from 1 to n.
// k-shortest-paths Dijkstra: pop node u until it has been finalized k times;
// each pop yields the next shortest distance to u. Stop once n hits k.
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<pair<int, long long>>> graph(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b; long long w;
        cin >> a >> b >> w;
        graph[a].push_back({b, w});
    }

    vector<int> cnt(n + 1, 0);
    vector<long long> res;
    res.reserve(k);

    // min-heap on (dist, node)
    priority_queue<pair<long long, int>,
                   vector<pair<long long, int>>,
                   greater<>> pq;
    pq.push({0, 1});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (cnt[u] >= k) continue;
        ++cnt[u];
        if (u == n) {
            res.push_back(d);
            if ((int)res.size() == k) break;
        }
        for (auto [v, w] : graph[u]) {
            if (cnt[v] < k) pq.push({d + w, v});
        }
    }

    for (size_t i = 0; i < res.size(); ++i) {
        cout << res[i] << ' ';
    }
    cout << '\n';
    return 0;
}
