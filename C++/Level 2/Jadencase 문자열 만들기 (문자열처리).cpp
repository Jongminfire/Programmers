#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
	string answer = "";

	if (s[0] >= 'a' && s[0] <= 'z')
	{
		answer += s[0] - 'a' + 'A';
	}
	else
	{
		answer += s[0] - 0;
	}

	for (int i = 1;i < s.size();i++)
	{
		if (s[i] == ' ')
		{
			answer += ' ';
		}
		else
		{
			if (s[i - 1] == ' ')
			{
				if (s[i] >= 'a' && s[i] <= 'z')
					answer += s[i] - 'a' + 'A';
				else
					answer += s[i];
			}
			else
			{
				if (s[i] >= 'A' && s[i] <= 'Z')
					answer += s[i] - 'A' + 'a';
				else
					answer += s[i];
			}
		}
	}

	return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/12951
// 문자열 검사를 통해 대소문자 변환
