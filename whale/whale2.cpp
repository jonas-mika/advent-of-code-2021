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

int mean(vector<int> v) {
    int s = 0;
    for (int i=0; i<v.size(); i++) {
        s+=v[i];
    }
    return s / v.size();
}  

int main() {
    vector<int> nums;
    string tmp;
    
    cin >> tmp;    
    nums = split_string(tmp, ',');

    int m = mean(nums);
    int max_dist = 0;
    for (int i=m-2; i<=m+2; i++) {
        int dist = 0;
        for (int j=0; j<nums.size(); j++) {
            int n = abs(i-nums[j]);
            dist += (n * (n+1)) / 2;
        }

        if (i == m-2) {
            max_dist = dist;
        } else {
            if (dist < max_dist) {
                max_dist = dist;
            }
        }
    }
    cout << max_dist << endl;

    return 0;
}
