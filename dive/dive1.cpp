#include <iostream>

using namespace std;

int main() {
    // solution to dive
    int h = 0, d = 0;
    string dir;
    int x;

    while (cin >> dir >> x) {
        if (dir == "forward") {
            h += x;
        } else if (dir == "down") {
            d += x;
        } else if (dir == "up") {
            d -= x;
        }
    }

    cout << h * d << endl;
    
    return 0;
};
