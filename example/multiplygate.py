class MultiplyGate(object):
  def forward(x, y):
    z = x * y
    return z
  
  def backward(dz):
    # dx = ... # todo
    # dy = ... # todo
    
    return [dx, dy]
