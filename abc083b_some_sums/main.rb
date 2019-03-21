n, a, b = gets.chomp.split(" ").map(&:to_i)
sum_total = 0
(1..n).each do |i|
  digits = i.to_s.split("").map(&:to_i)
  sum = digits.inject(:+)
  if a <= sum && sum <= b
    sum_total += i
  end
end
puts(sum_total)
