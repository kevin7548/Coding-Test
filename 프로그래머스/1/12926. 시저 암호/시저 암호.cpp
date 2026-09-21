#include <string>
#include <vector>

using namespace std;

string solution(string s, int n) {
    for (char &ch : s) {
        // 공백이면 continue
        if (ch == ' ')
            continue;
        
        // 알파벳 소문자 (97~122)
        else if ('a' <= ch && ch <= 'z') {
            ch = 'a' + (ch - 'a' + n) % 26;
        }
        // 알파벳 대문자 (65~90)
        else if ('A' <= ch && ch <= 'Z') {
            ch = 'A' + (ch - 'A' + n) % 26;
        }
    }
    return s;
}