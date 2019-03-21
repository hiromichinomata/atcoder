n = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)
result = a.map do |i|
  count = 0
  while i % 2 == 0 do
    i = i /2
    count += 1
  end
  count
end
puts(result.min)
