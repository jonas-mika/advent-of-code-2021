#include <iostream>
#include <vector>
#include <string>

using namespace std;

string compute_rate(vector<string> nums, string search="majority") {
    int j = 0;
    int s;

    while (nums.size() > 1) {
        double n = nums.size();

        s = 0;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i][j] == '1') {
                s++;
            }
        }

        if (search == "majority") {
            vector<string> new_nums;
            if (s >= n/2) {
                for (int i=0; i<nums.size(); i++) {
                    if (nums[i][j] == '1') {
                        new_nums.push_back(nums[i]);
                    }
                }
            } else {
                for (int i=0; i<nums.size(); i++) {
                    if (nums[i][j] == '0') {
                        new_nums.push_back(nums[i]);
                    }
                }
            } 
            nums = new_nums;
            j++;

        } else if (search == "minority") {
            vector<string> new_nums;
            if (s >= n/2) {
                for (int i=0; i<nums.size(); i++) {
                    if (nums[i][j] == '0') {
                        new_nums.push_back(nums[i]);
                    }
                }
            } else {
                for (int i=0; i<nums.size(); i++) {
                    if (nums[i][j] == '1') {
                        new_nums.push_back(nums[i]);
                    }
                }
            } 
            nums = new_nums;
            j++;
        }
    }
    return nums[0];
}

int main() {
    string o, e, line;
    vector<string> nums;
    int s, n;
    
    n=0; 
    while (getline(cin, line)) {
        nums.push_back(line);
        n++;
    }

    o = compute_rate(nums, "majority");
    e = compute_rate(nums, "minority");

    cout << stol(o,0,2) * stol(e, 0, 2) << endl;

    return 0;
}

