#!/usr/bin/env ruby
# frozen_string_literal: true

input_data = File.open('input')


location_ids = input_data.map do |line|
  line.split.map(&:to_i)
end

sorted_group_1_locations, sorted_group_2_locations = location_ids.transpose.map(&:sort)

distances = sorted_group_1_locations.each_with_index.map do |l, i|
  (l - sorted_group_2_locations[i]).abs
end

puts "Part one: #{distances.sum}"
