#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<int> next_day(vector<int> states, int d, int stop_at) {
    if (d >= stop_at) {
        return states;
    }

    int tmp = 0;
    for (int i=0; i<states.size(); i++) {
        if (i==0) {
            tmp = states[i];
        } else {
            states[i-1] = states[i];
        }
    }
    states[6] += tmp;
    states[8] = tmp;

    /*
    for (int i=0; i<states.size(); i++) {
        cout << states[i] << " ";
    }
    cout << endl;
    */

    return next_day(states, d+1, stop_at);
}

int main() {
    int x;
    string tmp;
    vector<int> states(9);

    cin >> tmp;
    stringstream ss(tmp);

    while ( getline(ss, tmp, ',') ) {
        stringstream cnv(tmp);
        cnv >> x;
        states[x]++;
    }

    states = next_day(states, 0, 80);


    int s = 0;
    for (int i=0; i<states.size(); i++) {
        s += states[i];
    }

    cout <<  s << endl;

    return 0;
}
