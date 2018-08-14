=begin
http://www.codewars.com/kata/reverse-a-number?utm_source=newsletter
Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Examples
 123 ->  321
-456 -> -654
1000 ->    1
=end

def reverse_number(number)
   number > 0 ? number.to_s.reverse.to_i : number.to_s.reverse.to_i * -1
end
