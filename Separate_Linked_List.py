def sortAbsoluteValues(root):
	if not root: return root
	newH = prev = Node(None)
	newH.next = root
	newL = None
	def rec(prev, curr):
		if not curr:
			return
		if curr.val < 0:
			_next = curr
			prev.next = prev.next.next
			_next.next = newL
			newL = _next
			return rec(prev, prev.next)
		else:
			return rec(curr, curr.next)
	rec(newH, root)
	temp = newL
	while temp and temp.next!= None:
		temp = temp.next
	if temp:
		temp.next = newH.next
		return newL
	return newH.next