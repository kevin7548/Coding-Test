#include <string>
#include <vector>

using namespace std;

bool solution(string s) {

    for (char ch: s)
        if (!isdigit(ch))
            return false;

    if (s.size() == 4 || s.size() == 6)
        return true;
    else
        return false;
}