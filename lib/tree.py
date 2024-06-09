class Tree:
  def __init__(self, root = None):
    self.root = root
  def get_element_by_id(self, id):
    self.stack = []
    self.stack.append(self.root)
    while self.stack:
      node = self.stack.pop()
      if node['id'] == id:
        return node
      else:
        for child in node['children']:
          self.stack.append(child)
    pass
