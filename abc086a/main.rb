a, b = gets.chomp.split(" ").map(&:to_i)
product = a*b
if product % 2 == 0
  puts("Even")
else
  puts("Odd")
end
