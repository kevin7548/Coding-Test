#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s, int n) {
    for (char &ch : s) {
        // 공백이면 continue
        if (isspace(ch))
            continue;
        
        int idx = ch + n;
        // 알파벳 소문자 (97~122)
        if ('a' <= ch && ch <= 'z') {
            if (idx > 122)
                idx -= 26;
        }
        // 알파벳 대문자 (65~90)
        else if ('A' <= ch && ch <= 'Z') {
            if (idx > 90)
                idx -= 26;
        }
        ch = (char)idx;
    }
    return s;
}