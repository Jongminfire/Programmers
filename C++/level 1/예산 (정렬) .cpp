#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
	int answer = 0;

	sort(d.begin(), d.end());

	for (int i = 0;i < d.size();i++)
	{
		if (budget >= d[i])
		{
			budget -= d[i];
			answer++;
		}
	}

	return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/12982
// 정렬을 사용해 최대 개수 구하기
