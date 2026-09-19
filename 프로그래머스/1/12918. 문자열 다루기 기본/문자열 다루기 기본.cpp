#include <string>
#include <vector>

using namespace std;

bool solution(string s) {
    if (s.size() != 4 && s.size() != 6)
        return false;
    
    for (char ch : s)
        if (!isdigit(ch))
            return false;

    return true;
}