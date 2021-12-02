############# Part 1
depth = 0
horizontal = 0

with open("input.txt") as file:
  data = file.readlines()
  for line in data:
    if "forward" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      horizontal = horizontal + number_list[0]
    elif "up" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      depth = depth - number_list[0]
    elif "down" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      depth = depth + number_list[0]

print(f"Depth: {depth}; Horizontal Position: {horizontal}")
print(f"Result: {depth * horizontal}")

############ Part 2
part2_depth = 0
part2_horizontal = 0
aim = 0

with open("input.txt") as file:
  data = file.readlines()
  for line in data:
    if "up" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      aim = aim - number_list[0]

    elif "down" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      aim = aim + number_list[0]

    elif "forward" in line:
      number_list = [int(i) for i in line.split() if i.isdigit()]
      part2_horizontal = part2_horizontal + number_list[0]
      part2_depth = part2_depth + (aim * number_list[0])

print(f"Depth: {part2_depth}; Horizontal Position: {part2_horizontal}")
print(f"Result: {part2_depth * horizontal}")



