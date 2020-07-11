#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {

	int answer = 0;
	int value = 0;
	int size = priorities.size();

	vector<int> v = priorities;
	deque<int> s;

	sort(v.begin(), v.end());

	for (int i = 0;i < priorities.size();i++)
	{
		if (i != location)
			s.push_back(priorities[i]);
		else
		{
			s.push_back(-1);
			value = priorities[i];
		}
	}

	for (int i = 0;i < size;i++)
	{
		while (1)
		{
			int pop = s.front();
			
			if(pop==-1)
			{
				if (value == v.back())
				{
					answer = i+1;
					return answer;
				}
			}

			if (s.front() == v.back())
			{
				break;
			}

			s.push_back(pop);
			s.pop_front();

		}

		s.pop_front();
		v.pop_back();
	}

	return answer;
}

int main()
{
	vector<int> vec = { 2, 1, 3, 2 };
	
	cout << solution(vec, 2) << "\n";
	getchar();
	return 0;
}

// https://programmers.co.kr/learn/courses/30/lessons/42587
