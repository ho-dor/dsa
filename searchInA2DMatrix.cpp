bool searchMatrix(vector<vector<int> > &mat, int target)
{
    int n = mat.size();
    int m = mat[0].size();

    for (int i = 0; i < n; i++)
    {
        if (mat[i][0] == target)
            return true;
        if (mat[i][m - 1] == target)
            return true;
        if (mat[i][0] < target && mat[i][m - 1] < target)
        {
            continue;
        }
        if (mat[i][0] < target && mat[i][m - 1] > target)
        {
            for (int j = 1; j < m - 1; j++)
            {
                if (mat[i][j] == target)
                    return true;
            }
        }
    }

    return false;
}