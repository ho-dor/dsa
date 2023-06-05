#include <bits/stdc++.h>

void setZeros(vector<vector<int>> &matrix)
{
	// Write your code here.
	vector<pair<int,int>> flags;
	int n = matrix.size();
	int m = matrix[0].size();
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(matrix[i][j] == 0){
				flags.push_back(make_pair(i,j));
			}
		}
	}

	for(int k=0; k<flags.size(); k++){
		for(int i=0; i<n; i++){
			matrix[i][flags[k].second] = 0;
		}

		for(int i=0; i<m; i++){
			matrix[flags[k].first][i] = 0;
		}
	}
}
