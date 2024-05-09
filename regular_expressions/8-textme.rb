#!/usr/bin/env ruby

# Define a method to parse log lines and extract required information
def parse_log_line(line)
  # Match sender, receiver, and flags using regex
  sender_match = line.match(/\[from:(?<sender>[^\]]+)\]/)
  receiver_match = line.match(/\[to:(?<receiver>[^\]]+)\]/)
  flags_match = line.match(/\[flags:(?<flags>[^\]]+)\]/)

  # Extract sender, receiver, and flags if matches are found
  sender = sender_match[:sender] if sender_match
  receiver = receiver_match[:receiver] if receiver_match
  flags = flags_match[:flags] if flags_match

  # Output formatted result if all information is available
  if sender && receiver && flags
    puts "#{sender},#{receiver},#{flags}"
  end
end

# Read log file provided as command line argument
logfile = ARGV[0]

# Check if logfile argument is provided
if logfile.nil?
  puts "Usage: #{$PROGRAM_NAME} <logfile>"
  exit 1
end

# Read the logfile line by line and parse each line
File.foreach(logfile) do |line|
  # Parse log line
  parse_log_line(line)
end

