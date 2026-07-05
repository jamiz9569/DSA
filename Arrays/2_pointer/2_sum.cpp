#include <iostream>
using namespace std;

int nums[] = {2, 7, 11, 15};
int target = 9;

void two_sum() {
    int left = 0;
    int right = sizeof(nums) / sizeof(nums[0]) - 1;

    while (left < right) {
        int sum = nums[left] + nums[right];

        if (sum == target) {
            cout << "Indices: " << left << " " << right << endl;
            return;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    cout << "No solution found." << endl;
}

int main() {
    two_sum();
    return 0;
}