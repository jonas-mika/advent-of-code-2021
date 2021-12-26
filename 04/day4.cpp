#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> split_string(string s, string delimiter) {
    vector<int> ans;
    string tmp;
    int found;

    stringstream ss(s);

    // reading in nums as vec of ints
    while(ss.good())  {
        getline(ss,tmp,',');
        stringstream cnv(tmp);
        cnv >> found;
        ans.push_back(found);
    }
    return ans;
}

vector<int> split_whitespaces(string s) {
    string tmp;
    int found;
    vector<int> ans;

    stringstream ss(s);
    while (!ss.eof()) {
        ss >> tmp;

        if (stringstream(tmp) >> found) {
            ans.push_back(found);
        }
        tmp = "";
    }
    return ans;
}

int main() {
    vector<int> nums;
    vector<vector<vector<int> > > boards;
    int z;
    string tmp;

    // read nums as strings
    cin >> tmp;
    stringstream ss(tmp);

    nums = split_string(tmp, ",");

    int i = 0;
    int started = false;
    while (getline(cin, tmp)) {
        if (started==false && tmp == "") {
            continue;
        } else if (tmp == "") {
            vector<vector<int> > board;
            boards.push_back(board);
            i++;
            continue;
        }
        started = true;

        vector<int> row;
        row = split_whitespaces(tmp);
        // boards[i].push_back(row);
    }
    cout << boards.size() << endl;
    
    /*
    cout << nums.size() << endl;
    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
    */

    return 0;
}
