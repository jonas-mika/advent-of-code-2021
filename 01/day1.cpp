#include <iostream>
#include <vector>
 
using namespace std;

int main() {
    int num;
    vector<int> v;

    while(cin >> num) {
        v.push_back(num);
    }

    int c1 = 0;
    int c2 = 0;
    for (int i=1; i<v.size(); ++i ) {
        if (v[i] > v[i-1]) {
            c1++;
        }

        if (i >= 3) {
            if (v[i] > v[i-3]) {
                c2++;
            }
        }
    }


    cout << "Part 1: " << c1 << endl;
    cout << "Part 2: " << c2 << endl;

    return 0;
}
