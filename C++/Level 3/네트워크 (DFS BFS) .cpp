#include <string>
#include <vector>

using namespace std;

int visit[201] = { 0, };		// int형 배열 0으로 초기화

void dfs(vector<vector<int>> computers, int start, int n)
{
	visit[start] = 1;

	for (int i = 0;i < n;i++)
	{
		if (computers[start][i] && visit[i] != 1)
			dfs(computers, i, n);
	}
}

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;

	for (int i = 0;i < n;i++)
	{
		if (visit[i] != 1)
		{
			dfs(computers, i, n);
			answer++;
		}
	}

	return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/43162
// DFS와 BFS로 연결요소 찾는 문제
