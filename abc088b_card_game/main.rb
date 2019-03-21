n = gets.chomp.to_i
a = gets.chomp.split(" ").map(&:to_i)
a = a.sort.reverse
alice = 0
bob = 0
(0...n).each do |i|
  if i % 2 == 0
    alice += a[i]
  else
    bob += a[i]
  end
end
puts(alice-bob)
