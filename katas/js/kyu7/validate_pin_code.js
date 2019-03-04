/*
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.
eg:

validatePIN('1234') === true
validatePIN('12345') === false
validatePIN('a234') === false

Link to kata: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
*/

const isDigit = input => '0123456789'.includes(parseInt(input));
export const validatePin = digits => {
  const allDigits = [...digits].every(isDigit);
  return allDigits && (digits.length === 4 || digits.length === 6);
};
