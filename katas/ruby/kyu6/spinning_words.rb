def spin_words(string)
  string.split.map { |word| word.size >= 5 ? word.reverse : word }.join(' ')
end
