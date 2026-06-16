#include <iostream>
using namespace std;

const long long MOD = 1e9 + 7;

// dp[j] = number of (combination) ways to make sum j; global to keep it off the stack
long long dp[1000001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    cin >> n >> x;

    int coins[100];
    for (int i = 0; i < n; i++) cin >> coins[i];

    dp[0] = 1;

    // coins outer, sum inner -> counts combinations (not permutations)
    for (int i = 0; i < n; i++) {
        int c = coins[i];
        for (int j = c; j <= x; j++) {
            dp[j] = (dp[j] + dp[j - c]) % MOD;
        }
    }

    cout << dp[x] << "\n";
    return 0;
}
