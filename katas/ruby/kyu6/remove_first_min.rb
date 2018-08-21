def remove_smallest(numbers)
  min = numbers.min
  numbers.reject { |n| min = n - 1 if n == min }
end
