n, y = gets.chomp.split(" ").map(&:to_i)
result = ""
exit_flag = false
(0..n).each do |i|
  (0..n-i).each do |j|
    k = n-i-j
    sum = 10000 * i + 5000 * j + 1000 * k
    if sum == y
      result = [i, j, k].join(" ")
      puts(result)
      exit_flag = true
      break
    end
  end
  if exit_flag
    break
  end
end
if result.size == 0
  puts("-1 -1 -1")
end