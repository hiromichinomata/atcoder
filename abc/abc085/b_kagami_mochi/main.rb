n = gets.chomp.to_i
d = []
(0...n).each do |i|
  tmp = gets.chomp.to_i
  d[i] = tmp
end
count = d.uniq.sort.size
puts(count)
