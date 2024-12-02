#!/usr/bin/env ruby
# frozen_string_literal: true

def safe_report?(report)
  report.each_cons(2).all? { (_1 > _2) && (_1 - _2).abs.between?(1, 3) } ||
  report.each_cons(2).all? { (_1 < _2) && (_1 - _2).abs.between?(1, 3) }
end

reports = ARGF.readlines.map { _1.split.map(&:to_i) }
safe_reports = reports.count { safe_report?(_1) }

puts "Safe reports: #{safe_reports}"

