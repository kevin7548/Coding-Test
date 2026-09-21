#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    const vector<string> nums = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    for (int i = 0; i < 10; i++) {
        size_t pos;
        while ((pos = s.find(nums[i])) != string::npos) {
            s.replace(pos, nums[i].size(), to_string(i));
        }
    }
    
    return stoi(s);
}