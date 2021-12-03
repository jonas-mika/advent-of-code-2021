#include <iostream>
#include <vector>
 
using namespace std;

int main() {
    int num;
    vector<int> v;

    while(cin >> num) {
        v.push_back(num);
    }
    int c = 0;
    for (int i=3; i<v.size(); i++) {
        if (v[i] + v[i-1] + v[i-2] > v[i-1] + v[i-2] + v[i-3]) {
            c++;
        }
    }

    cout << c << endl;

    return 0;
}
