class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int bottom = matrix.size()-1;
        int right = matrix[0].size()-1;
        int left = 0;
        int top = 0;
        vector<int> result;
        while(left <= right && top <= bottom)
        {
            for(int i = left ;i<=right;i++)
            result.push_back(matrix[top][i]);
                top += 1;
                if(top <= bottom)
            for(int i =top ;i <=bottom;i++)
            result.push_back(matrix[i][right]);
            right -=1;
            if(left <= right && top<= bottom)
            for(int i = right ; i >=left;i-- )
            result.push_back(matrix[bottom][i]);
            bottom--;
             if(left <= right && top<= bottom)
            for(int i = bottom ;i >= top ;i--)
            result.push_back(matrix[i][left]);
            left+=1;
        }return result;
    }
};
