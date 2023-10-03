#!/usr/bin/env ruby
# search for a word with repetition of a letter
puts ARGV[0].scan(/hbt{1,5}n/).join
