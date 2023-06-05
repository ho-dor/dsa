#include <bits/stdc++.h>

vector<vector<long long int> > printPascal(int n)
{
    // Write your code here.
    vector<vector<long long int> > result(n);
    result[0].push_back(1);

    for (int i = 1; i < n; i++)
    {
        result[i].push_back(1);
        if (i >= 2)
        {
            int j = 1;
            while (j < i)
            {
                result[i].push_back(result[i - 1][j - 1] + result[i - 1][j]);
                j++;
            }
        }
        result[i].push_back(1);
    }
    return result;
}
