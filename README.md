# soccer-py
### A python application to handle soccer data.
- Visualization tool for X & Y coordinates

[![Downloads](https://static.pepy.tech/personalized-badge/todofcpy?period=month&units=international_system&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/todofcpy)

## Documentation
Check out the [Documentation](https://soccer-py.readthedocs.io/en/latest/)

## Examples
```python
from todofcpy.graph import Sprintmap
df = df[['x_pos','y_pos']]
dat = df.to_numpy()
tsm = Sprintmap(data=dat)
plt = tsm.create_sprintmap_plot()
plt.show()
```

```python
from todofcpy.graph import Heatmap
df = df[['x_pos','y_pos']]
dat = df.to_numpy()
thm = Heatmap(data=dat)
thm.set_colors(color='plasma')
plt = thm.create_heatmap_plot()
plt.show()
...
(_or_)
...
from todofcpy.graph import Heatmap
df = df[['x_pos','y_pos']]
dat = df.to_numpy()
thm = Heatmap(data=dat, color='magma')
plt = thm.create_heatmap_plot()
plt.show()
```

## Extra Data Work
This is a passion project started at [Todo Football Club](https://todofootballclub.com/)

## Releases
#### 0.0.0 == Currently graphs a heatmap.
#### 0.1.0 == Sprintmaps.
#### 0.1.1 == 2d array bug fix.
#### 0.2.0 == Heatmap can choose color scheme from ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
####          Restructuring of codebase.
#### 0.3.0 == Animation of single player.
#### 0.3.1 == Create pyplot field with color choices.

## License
todofcpy is a [MIT License](https://github.com/Robinhoets/soccer-py/blob/main/LICENSE)
