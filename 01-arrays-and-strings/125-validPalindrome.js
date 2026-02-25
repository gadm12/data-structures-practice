"use strict";

/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function (s) {
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  const reversed = cleaned.split("").reverse().join("");

  return cleaned === reversed;
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));

console.log(isPalindrome("race a car"));
