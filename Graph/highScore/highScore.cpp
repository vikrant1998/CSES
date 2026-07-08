#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> from(m), to(m);
    vector<long long> w(m);
    for (int i = 0; i < m; i++) {
        cin >> from[i] >> to[i] >> w[i];
    }

    const long long NEG_INF = LLONG_MIN / 4;
    // We MAXIMIZE score, so relax with '>' and start dist[1] = 0.
    vector<long long> dist(n + 1, NEG_INF);
    dist[1] = 0;

    // Bellman-Ford: n passes to settle longest-path distances.
    // (n rather than n-1 so a self-loop when n == 1 still gets relaxed.)
    for (int pass = 0; pass < n; pass++) {
        bool changed = false;
        for (int e = 0; e < m; e++) {
            if (dist[from[e]] > NEG_INF &&
                dist[from[e]] + w[e] > dist[to[e]]) {
                dist[to[e]] = dist[from[e]] + w[e];
                changed = true;
            }
        }
        if (!changed) break;  // early exit once stable
    }

    // n more passes: any node still improving is on/after a positive cycle.
    // Mark it +INF (unbounded). The mark propagates forward each pass.
    for (int pass = 0; pass < n; pass++) {
        for (int e = 0; e < m; e++) {
            if (dist[from[e]] > NEG_INF &&
                dist[from[e]] + w[e] > dist[to[e]]) {
                dist[to[e]] = LLONG_MAX / 4;  // poisoned: unbounded score
            }
        }
    }

    if (dist[n] >= LLONG_MAX / 4)
        cout << -1 << "\n";
    else
        cout << dist[n] << "\n";

    return 0;
}
