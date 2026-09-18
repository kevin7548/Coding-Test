#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

long long solution(int a, int b) {
    long long answer = 0;
    answer = (long long)(a + b) * (abs(b - a) + 1) / 2;
    return answer;
}