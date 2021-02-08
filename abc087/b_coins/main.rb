c500 = gets.chomp.to_i
c100 = gets.chomp.to_i
c50 = gets.chomp.to_i
x = gets.chomp.to_i
count = 0
(0..c500).each do |i|
  (0..c100).each do |j|
    (0..c50).each do |k|
      if i*500 + j*100+ k*50 == x
        count += 1
      end      
    end
  end
end
puts(count)
