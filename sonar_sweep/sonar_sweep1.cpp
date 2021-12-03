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
    for (int i=1; i<v.size(); ++i ) {
        if (v[i] > v[i-1]) {
            c++;
        }
    }

    cout << c << endl;

    return 0;
}
