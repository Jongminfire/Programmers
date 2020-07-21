#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string a, string b)
{
	if (a[n - 1] < b[n - 1])
		return true;
	else
		return false;
}

vector<string> solution(vector<string> strings, int n) {
	vector<string> answer = strings;
	sort(answer.begin(), answer.end(), cmp);

	return answer;
}
