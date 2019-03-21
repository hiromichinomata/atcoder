n = gets.chomp.to_i
t = []
x = []
y = []
(0...n).each do |i|
  t[i], x[i], y[i] = gets.chomp.split(" ").map(&:to_i)
end

dt = []
dx = []
dy = []
dt[0] = t[0]
dx[0] = x[0].abs
dy[0] = y[0].abs
(1...n).each do |i|
  dt[i] = t[i] - t[i-1]
  dx[i] = (x[i] - x[i-1]).abs
  dy[i] = (y[i] - y[i-1]).abs
end

exit_flag = false
(0...n).each do |i|
  distance = dx[i] + dy[i]
  if dt[i] < distance
    exit_flag = true
    break
  elsif (distance - dt[i]) % 2 == 0
    next
  else
    exit_flag = true
    break
  end
end

if exit_flag
  puts("No")
else
  puts("Yes")
end
