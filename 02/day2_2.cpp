#include <iostream>

using namespace std;

int main() {
    // solution to dive
    int h = 0, d = 0, aim=0;
    string dir;
    int x;

    while (cin >> dir >> x) {
        if (dir == "forward") {
            h += x;
            d += x * aim;
        } else if (dir == "down") {
            aim += x;
        } else if (dir == "up") {
            aim -= x;
        }
    }

    cout << h * d << endl;
    
    return 0;
};
