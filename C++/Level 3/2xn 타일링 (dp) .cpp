#include <string>
#include <vector>

using namespace std;

int solution(int n) {
	int answer = 0;

	vector<int> dp(n + 3);

	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;

	if (n > 3)
	{
		for (int i = 3;i <= n;i++)
		{
			dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007;
		}
	}

	answer = dp[n];

	return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/12900
