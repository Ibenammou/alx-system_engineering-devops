#!/usr/bin/env ruby
# Ruby script that matches the regular expression into input argument

regex = /School/
input = ARGV[0]

match = input.scan(regex)

if match
  puts match.join
end
