def main(inp):
	inp = list(inp)
	stack = []
	index = 0
	while index<len(inp):
		if inp[index]!= "{":
			stack.append(inp[index])
			index+=1
		else:
			count = ""
			index+=1
			while inp[index]!= "}":
				count+=inp[index]
				index+=1
			index+=1    # to skip the closing } bracket
			count = int(count)
			stack.pop() # to pop the opening ( bracket
			tempStr = []
			while stack[-1]!="(":
				tempStr.append(stack.pop())
			stack.pop()  # to pop the opening ( bracket  
			tempStr.reverse()
			tempStr = "".join(tempStr)
			tempStr = tempStr*count
			tempStr = list(tempStr)
			for each in tempStr:
				stack.append(each)
	output = []
	for each in stack:
		if each.isalpha():
			output.append(each)
	print("".join(output))

# main("(ab){3}(cd){2}")
# main("(ab(d){3}){2}")
main("(ab(c){3}d){2}")