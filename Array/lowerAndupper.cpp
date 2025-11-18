/* we can use the linear search but it takes O(n) so we use binary search method its more optimal */
class Solution {
  public:
    int upperBound(vector<int>& nums, int target) {
      int low = 0;
      int high = nums.size()-1;
      int result = nums.size();
      int mid = 0;
      while(low <= high)
      {
          mid = (low+high)/2;
          if(nums[mid] > target)
          {
              result = mid;
              high = mid - 1;
          }
          else low = mid+1;
      }return result;
    }
};


class Solution {
  public:
    int lowerBound(vector<int>& nums, int target) {
        // code here
      int low = 0;
      int high = nums.size()-1;
      int result = nums.size();
      int mid = 0;
      while(low <= high)
      {
          mid = (low+high)/2;
          if(nums[mid] >= target)
          {
              result = mid;
              high = mid - 1;
          }
          else low = mid+1;
      }return result;
      
    }
};