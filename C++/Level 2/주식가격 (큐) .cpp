#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer;

	for (int i = 0;i < prices.size() - 1;i++)
	{
		int num = 1;
		int top = prices[i];

		for (int j = i + 1;j < prices.size() - 1;j++)
		{
			if (top <= prices[j])
			{
				num++;
			}
			else
			{
				break;
			}
		}

		answer.push_back(num);
	}

	answer.push_back(0);

	return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/42584
// 2중 포문과 벡터를 활용해서 가격이 떨어지지 않는 케이스를 구하는 문제
