#include <string>
#include <vector>
#include <cctype>

using namespace std;

string solution(string s) {
    int cnt = 0;
    
    for (char &ch : s) {
        // 1. 빈 칸이면 cnt 초기화
        if (isspace(ch))
            cnt = 0;
        // 2. 문자 있고, 짝수 인덱스면 대문자로
        else {
            if (cnt % 2 == 0)
                ch = toupper(ch);
        // 3. 문자 있고, 홀수 인덱스면 소문자로
            else
                ch = tolower(ch);
            
            cnt++;
        }
    }
        
    return s;
}