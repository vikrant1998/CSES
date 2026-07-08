#include <iostream>
#include <vector>
#include <array>
#include <queue>
#include <tuple>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    // adjacency: for each node, list of (neighbor, weight)
    vector<vector<pair<int, int>>> graph(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].emplace_back(b, w);
    }

    const long long INF = LLONG_MAX;
    // d[node][used], used = 0 (no coupon yet) / 1 (coupon spent)
    vector<array<long long, 2>> d(n + 1, {INF, INF});
    d[1][0] = 0;

    // min-heap of (distance, node, used)
    priority_queue<tuple<long long, int, int>,
                   vector<tuple<long long, int, int>>,
                   greater<>> pq;
    pq.emplace(0LL, 1, 0);

    while (!pq.empty()) {
        auto [dc, u, used] = pq.top();
        pq.pop();
        if (dc > d[u][used]) continue;

        for (auto [v, w] : graph[u]) {
            // take edge at full price
            if (dc + w < d[v][used]) {
                d[v][used] = dc + w;
                pq.emplace(d[v][used], v, used);
            }
            // use the coupon on this edge (only if not used yet)
            if (used == 0) {
                long long nd = dc + w / 2;
                if (nd < d[v][1]) {
                    d[v][1] = nd;
                    pq.emplace(nd, v, 1);
                }
            }
        }
    }

    cout << min(d[n][0], d[n][1]) << "\n";
    return 0;
}
