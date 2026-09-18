#include <string>
#include <vector>

using namespace std;

int solution(int num) {
    int answer = 0;
    long long N = (long long)num;
    
    while (N > 1 and answer < 500) {
        if (N % 2 == 0)
            N = N / 2;
        else
            N = N * 3 + 1;
        answer += 1;
    }
    
    if (N == 1)
        return answer;
    else
        return -1;
}