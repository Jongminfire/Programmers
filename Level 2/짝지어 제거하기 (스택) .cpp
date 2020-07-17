#include <iostream>
#include <string>
#include <queue>

using namespace std;

int solution(string s)
{
	int answer = 0;
	deque<char> dq;

	for (int i = 0;i < s.size();i++)
	{
		if (dq.empty() || dq.back() != s[i])
			dq.push_back(s[i]);
		else
			dq.pop_back();
	}

	if (dq.empty())
		answer = 1;
	else
		answer = 0;

	return answer;
}

int main()
{
	string s = "baabaa";
	cout << solution(s) << "\n";

	getchar();

	return 0;
}

// https://programmers.co.kr/learn/courses/30/lessons/12973
