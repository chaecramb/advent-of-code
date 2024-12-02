#!/usr/bin/env ruby
# frozen_string_literal: true

location_ids = ARGF.readlines.map { _1.split.map(&:to_i) }

lefts, rights = location_ids.transpose.map(&:sort)
total_distance = lefts.zip(rights).sum { (_1 - _2).abs }

puts "Part One: #{total_distance}"

tally = rights.tally
similarity = (lefts & tally.keys).sum { |num| num * tally[num] }

puts "Part Two: #{similarity}"
