#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n)
{
	int ans = 0;
	int init = n;

	while (init != 0)
	{
		if (init % 2 == 0)
			init = init / 2;
		else
		{
			init--;
			ans++;
		}
	}

	return ans;
}

// https://programmers.co.kr/learn/courses/30/lessons/12980
/* for문을 이용해서 2로 나누어지지 않는 경우 구하는 문제
처음에는 vector를 이용한 dp로 풀었으나 메모리초과와 시간초과로 다른 방법을 생각함
*/
