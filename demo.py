from numbersize import abbr,normal,decimal
import os

# Normal
print('Normal')

print(abbr(1000,normal)) 			# >> 1K
print(abbr(12100,normal))			# >> 12K
print(abbr(143000,normal))			# >> 143K
print(abbr(1000000,normal))			# >> 1M
print(abbr(15000000,normal))		# >> 15M
print(abbr(100000000,normal))		# >> 100M
print(abbr(1000000000,normal))		# >> 1G

print('----------')

# Decimal

print('Decimal')

print(abbr(1024,decimal)) 			# >> 1KB
print(abbr(1048576,decimal))		# >> 1MB
print(abbr(1073741824,decimal))		# >> 1GB
print(abbr(1099511627776,decimal))	# >> 1TB

os.system("pause")
