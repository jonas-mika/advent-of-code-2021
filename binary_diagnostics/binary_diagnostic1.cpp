#include <iostream>
#include <vector>

using namespace std;

int main() {
    string g, e, line;
    vector<string> bits;
    int s, n;
    
    n=0; 
    while (getline(cin, line)) {
        bits.push_back(line);
        n++;
    }

    for (int j=0; j<5; j++) {
        s = 0;
        for (int i=0; i<bits.size(); i++) {
            if (bits[i][j] == '1') {
                s++;
            }
        }
        if (s > n / 2) { 
            g+="1";
            e+="0";
        } else {
            g+="0";
            e+="1";
        }
    }
    cout << stol(g,0,2) * stol(e, 0, 2) << endl;

    return 0;
}
