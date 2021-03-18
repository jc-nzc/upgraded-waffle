s = IO.readlines("quine_producer.rb")[1]
puts('s= <<-STR', s, 'STR', s)
