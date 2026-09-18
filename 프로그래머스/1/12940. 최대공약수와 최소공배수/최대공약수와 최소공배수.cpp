#include <string>
#include <vector>

using namespace std;

int lcd(int n, int m) {
    if (n > m)
        if (n % m == 0)
            return m;
        else
            return lcd(m, n % m);
    else
        if (m % n == 0)
            return n;
        else
            return lcd(n, m % n);
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    answer.push_back(lcd(n, m));
    answer.push_back(n * m / lcd(n, m));
    return answer;
}