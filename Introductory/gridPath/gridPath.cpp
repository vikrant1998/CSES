#include <iostream>
#include <string>
using namespace std;

string path;
int n;
bool visited[7][7];
long long ways = 0;

bool blocked(int i, int j) {
    return i < 0 || j < 0 || i >= 7 || j >= 7 || visited[i][j];
}

// corridor pruning: returns true if continuing from (i, j) would split the
// remaining free region into two parts that can't both be filled.
bool splits_grid(int i, int j) {
    bool up    = blocked(i - 1, j);
    bool down  = blocked(i + 1, j);
    bool left  = blocked(i, j - 1);
    bool right = blocked(i, j + 1);

    // straight pinch: blocked on two opposite sides, open on the other two
    if ((up && down && !left && !right) ||
        (left && right && !up && !down))
        return true;

    // diagonal pinch: a blocked diagonal whose two connecting sides are both
    // open splits the remaining free region into two halves
    if (blocked(i - 1, j - 1) && !up && !left)   return true;
    if (blocked(i - 1, j + 1) && !up && !right)  return true;
    if (blocked(i + 1, j - 1) && !down && !left) return true;
    if (blocked(i + 1, j + 1) && !down && !right) return true;

    return false;
}

const int DI[4] = {-1, 0, 1, 0};   // U, L, D, R
const int DJ[4] = {0, -1, 0, 1};

void recurse(int move, int i, int j) {
    // reached the lower-left corner
    if (i == 6 && j == 0) {
        if (move == n) ways++;   // valid only if all 49 squares visited
        return;
    }

    if (move >= n) return;
    if (blocked(i, j)) return;
    if (splits_grid(i, j)) return;

    visited[i][j] = true;

    char c = path[move];
    for (int d = 0; d < 4; d++) {
        // which directions does this character allow?
        bool allow = (c == '?')
                  || (c == 'U' && d == 0)
                  || (c == 'L' && d == 1)
                  || (c == 'D' && d == 2)
                  || (c == 'R' && d == 3);
        if (!allow) continue;

        int ni = i + DI[d], nj = j + DJ[d];
        if (!blocked(ni, nj))
            recurse(move + 1, ni, nj);
    }

    visited[i][j] = false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> path;
    n = (int)path.size();

    recurse(0, 0, 0);
    cout << ways << "\n";
    return 0;
}
