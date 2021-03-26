elements = []

(0..5).each do |i|
  puts "adding #{i} to the list."
  # pushes the i variable on the *end* of the list
  elements.push(i)
end

elements.each {|i| puts "Element was: #{i}" }
