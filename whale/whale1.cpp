#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<int> split_string(string s, char delimiter) {
    vector<int> ans;
    string token; int in;

    stringstream ss(s);
    while (getline(ss, token, delimiter)) {
        stringstream cnv(token);
        cnv >> in;
        ans.push_back(in);
    }
    return ans;
}

int main() {
    vector<int> nums;
    string tmp;
    
    cin >> tmp;    
    nums = split_string(tmp, ',');

    sort(nums.begin(), nums.end());
    int m = nums[nums.size() / 2];


    int dist = 0;
    for (int i=0; i<nums.size(); i++) {
        dist += abs(m - nums[i]);
    }
    cout << dist << endl;

    return 0;
}
