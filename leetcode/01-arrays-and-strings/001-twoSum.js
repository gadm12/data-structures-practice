"use strict";
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

console.log(twoSum([2, 7, 11, 15], 9));

const twoSum2 = function (nums, target) {
  const seen = {};
  for (let i = 0; i < nums.length; i++) {
    let num = nums[i];
    let diff = target - num;

    if (diff in seen) {
      return [seen[diff], i];
    }

    seen[num] = i;
  }

  return [];
};

console.log(twoSum2([2, 7, 11, 15], 9));
