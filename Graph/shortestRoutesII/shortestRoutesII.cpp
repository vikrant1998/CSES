// Shortest Routes II (CSES) — all-pairs shortest path via Floyd-Warshall.
//
// Sample:
// 4 3 5
// 1 2 5
// 1 3 9
// 2 3 3
// 1 2 -> 5
// 2 1 -> 5
// 1 3 -> 8
// 1 4 -> -1
// 3 2 -> 3
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;

    const long long INF = (long long)4e18;
    // Flat 1D matrix indexed as dist[i*(n+1)+j] for cache-friendly access.
    vector<long long> dist((long long)(n + 1) * (n + 1), INF);
    for (int i = 0; i <= n; ++i) dist[(long long)i * (n + 1) + i] = 0;

    for (int e = 0; e < m; ++e) {
        int a, b; long long w;
        cin >> a >> b >> w;
        long long idx = (long long)a * (n + 1) + b;
        long long jdx = (long long)b * (n + 1) + a;
        if (w < dist[idx]) { dist[idx] = w; dist[jdx] = w; }
    }

    for (int k = 1; k <= n; ++k) {
        const long long* dk = &dist[(long long)k * (n + 1)];
        for (int i = 1; i <= n; ++i) {
            long long* di = &dist[(long long)i * (n + 1)];
            long long dik = di[k];
            if (dik >= INF) continue;
            for (int j = 1; j <= n; ++j) {
                long long nd = dik + dk[j];
                if (nd < di[j]) di[j] = nd;
            }
        }
    }

    string out;
    out.reserve(q * 7);
    char buf[24];
    for (int e = 0; e < q; ++e) {
        int a, b;
        cin >> a >> b;
        long long d = dist[(long long)a * (n + 1) + b];
        if (d >= INF) out += "-1";
        else {
            int len = snprintf(buf, sizeof(buf), "%lld", d);
            out.append(buf, len);
        }
        out += '\n';
    }
    fputs(out.c_str(), stdout);
    return 0;
}
