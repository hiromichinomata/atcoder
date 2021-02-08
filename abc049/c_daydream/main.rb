s = gets.chomp
len = s.size
s.reverse!
patterns = ["dream", "dreamer", "erase", "eraser"].map(&:reverse)
pattern_length = patterns.map(&:size)

i = 0
exit_flag = false
while i < len do
  match_flag = false
  (0..3).each do |j|
    if s[i, pattern_length[j]] == patterns[j]
      i += pattern_length[j]
      match_flag = true
      break
    end
  end
  if not match_flag
    exit_flag = true
    break
  end
end

if exit_flag
  puts("NO")
else
  puts("YES")
end
