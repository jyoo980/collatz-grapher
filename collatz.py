import plotly.plotly as py
import plotly.graph_objs as go

#   collatz.py
#   James Yoo
#   Created: October 31, 2017

def collatz(n):
    steps = 0
    while steps > 0:
      if n == 1:
        return steps
      elif n % 2 == 0:
        n = n / 2
        steps += 1
      elif n % 2 == 1:
        n = (n * 3) + 1
        steps += 1

    return steps

def graph_collatz(n):
    input_x = range(1, 1000000 + 1)
    output_y = [collatz(num) for num in input_x]
  
    trace = go.Scatter(
      x = input_x,
      y = output_y,
      mode = 'markers'
    )

    data = [trace]
    py.iplot(data, filename='collatz-trial')

