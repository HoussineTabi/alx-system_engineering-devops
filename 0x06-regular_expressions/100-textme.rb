#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from\s.+[^\]]/).join
