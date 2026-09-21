#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    vector<string> nums = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    for (int i = 0; i < 10; i++) {
        string numStr = nums[i];
        size_t pos = 0;
        while (s.find(numStr) != string::npos) {
            pos = s.find(numStr);
            s.replace(pos, numStr.size(), to_string(i));
        }
    }
    
    return stoi(s);
}