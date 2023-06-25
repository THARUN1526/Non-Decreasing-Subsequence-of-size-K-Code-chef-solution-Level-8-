#include <iostream>
#include <vector>
using namespace std;
vector<int> a;
vector<int> freq;
vector<int> ans;
int n;
int getMaxFreq() {
    int max_freq = 0;
    for (int i = 1; i <= n; i++)
        max_freq = max(max_freq, freq[i]);
    return max_freq;
}
int getSmallestElement() {
    for (int i = 1; i <= n; i++) if(freq[i])
            return i;
    return -1;
}

void update_and_push(int k) {
    if (!k)
        return;
    for (int i = n; i > 0; i--) {
        if (freq[i] == k) {
            ans.push_back(i);
            freq[i]--;
        }
    }
}
void getB(int _k) {
    if (ans.size() == n)
        return;
    int smallest_element = getSmallestElement();
    bool need_to_push_element = smallest_element == - 1 || freq[smallest_element] == _k ? false : true;
    update_and_push(_k);
    if (need_to_push_element) {
        ans.push_back(smallest_element);
        freq[smallest_element]--;
    }
    getB(_k - 1);
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> n >> k;
        a.clear();
        freq.clear();
        ans.clear();
        a.resize(n);
        freq.resize(n + 1);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            freq[a[i]]++;
        }
        if (getMaxFreq() > k) {
            cout << -1 << endl;
            continue;
        }
        getB(k);
        for (int i = 0; i < n; i++)
            cout << ans[i] << " ";
        cout << endl;
    }
}