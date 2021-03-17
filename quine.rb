# https://florian.github.io/quines/
s = <<-STR
puts("s = <<-STR", s, "STR" s)
STR
puts("s = <<-STR", s, "STR", s)
