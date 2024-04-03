class AlgumaCoisa: 
  def __enter__(self):
    print('Inicio!')

  def __exit__(self, exc_type, exc_value, exc_trace):
    print('Final!')

with AlgumaCoisa() as ola:
  print('Estou no meio')
