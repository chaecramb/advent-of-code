#!/usr/bin/env ruby
# frozen_string_literal: true

input_data = File.open('input')

location_ids = input_data.readlines.map { _1.split.map(&:to_i) }
sorted_locations = location_ids.transpose.map(&:sort)
total_distance = sorted_locations.transpose.sum { (_1 - _2).abs }

puts "Part One: #{total_distance}"

left_list, right_list = sorted_locations
similarity = left_list.reduce(0) { |sum, l| sum + (l * right_list.count(l)) }

puts "Part Two: #{similarity}"
