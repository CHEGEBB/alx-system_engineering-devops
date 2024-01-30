string = "The quick 12 brown fox jumped over the lazy dog"

puts string =~ /quick/

puts string =~ /z/ ? "Valid" : "Invalid"

puts string =~ /Z/i ? "Valid" : "Invalid"

p string.to_enum(:scan,/\d+/).map {Regexp.last_match}
