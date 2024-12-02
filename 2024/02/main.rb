#!/usr/bin/env ruby
# frozen_string_literal: true

reports = ARGF.readlines.map { _1.split.map(&:to_i) }

def safe_report?(report)
  report.each_cons(2).all? { (_1 > _2) && (_1 - _2).abs.between?(1, 3) } ||
  report.each_cons(2).all? { (_1 < _2) && (_1 - _2).abs.between?(1, 3) }
end

safe_reports = reports.count { safe_report?(_1) }

puts "Part 1: Safe reports: #{safe_reports}"

safe_reports = reports.each_with_index.count do |report, i|
  next true if safe_report?(report)

  (0..report.size).any? do |i|
    safe_report?(report.reject.with_index { _2 == i })
  end
end

puts "Part 2: Safe reports: #{safe_reports}"


