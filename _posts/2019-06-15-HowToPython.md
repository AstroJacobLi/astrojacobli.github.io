---
layout: post
title:  "How to use Python as an astronomer"
date:   2019-06-25 21:40:00
author: Jiaxuan Li
categories: Coding
---

# Data Visualization

### [Book: Fundamentals of Data Visualization](https://serialmentor.com/dataviz/visualizing-amounts.html)

Really really nice book on principles of plotting and visualizing data. Like it! I will post some content below later.

### Other packages for plot

- [mpld3](http://mpld3.github.io/notebooks/interactive_legend.html): renderer interactive figures (using d3) for Matplotlib code. Quite nice, though incomplete. Worth trying!
- [Altair](https://github.com/altair-viz/altair) is a relatively new declarative visualization library for Python. It's easy to use and makes great looking plots, however the ability to customize those plots is not nearly as powerful as in Matplotlib.
- [plot.ly](https://plot.ly/) can generate nice plots - this used to be a paid service only but was recently open sourced. Looks fancy!

### [Incredible cheat sheet for Matplotlib!](https://github.com/rougier/matplotlib-cheatsheet)
{% include image.html url="/images/matplotlib-cheatsheet.png" caption="`Matplotlib` cheatsheet" width=950 align="center" %}

And here are some commands in common use.

```python
%matplotlib inline
%load_ext autoreload
%autoreload 2
from IPython.display import clear_output

plt.rcParams['figure.dpi'] = 200.0
plt.rcParams['figure.facecolor'] = 'w'
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 25.0
plt.rcParams['text.usetex'] = True

fig, ax = plt.subplots(1, 2, figsize=(10, 10)) # Two columns
ax.tick_params(direction='in')         # Set tick direction to 'in'
ax2.get_shared_y_axes().join(ax1, ax2) # Share axis
ax.axis('off') # No frame when showing images
plt.savefig('xxx.png', dpi=200, bbox_inches='tight') # Save without empty margin
# If you find your figure too large, pass `rasterized=True` to `plt.savefig()`.
```

[How to create a zoom-in inset in a figure?](http://akuederle.com/matplotlib-zoomed-up-inset)

# Useful Python packages in astrophysics:

Here I only list several nice packages in astrophysics research. For more please check my GitHub [stars](https://github.com/AstroJacobLi?tab=stars) and GitHub [astrophysics](https://github.com/topics/astrophysics) and [astronomy](https://github.com/topics/astronomy) topics. 

- [`taotie`](https://github.com/dr-guangtou/taotie): A curated collection of resources for astrophysical research, best tutorial for anyone in this field!

- [`unagi`](https://github.com/dr-guangtou/unagi): Search and download data from Hyper Suprime-Cam (HSC) Subaru Strategic Survey (SSP). Useful for people working with HSC data.
- [`photutils`](https://github.com/astropy/photutils): Astropy package for source detection and photometry, basically substitutes of many IRAF functions.
- [`galsim`](https://github.com/GalSim-developers/GalSim): Galaxy image simulation tool, broadly used in weak lensing and mock tests in galaxy research.
- [`prospector`](https://github.com/bd-j/prospector): Python code for Stellar Population Inference from Spectra and SEDs.
- [`sedpy`](https://github.com/bd-j/sedpy): Utilities for astronomical spectral energy distributions.

- [`healpy`](https://healpy.readthedocs.io/en/latest/install.html): It is a package dealing with data on a sphere. It can map every direction to a pixel position, and vice versa. It can also calculate power spectrum of things like CMB. Although it's super useful, its python documentation is really unfriendly for beginners.
- [`starry`](https://rodluger.github.io/starry/tutorials/hd189.html): very cool package that can calculate light curves of transits and secondary eclipses of exoplanets, light curves of eclipsing binaries, rotational phase curves of exoplanets, light curves of planet-planet and planet-moon occultations, and more. A very cool tutorial: [A map of the hot jupiter HD 189733b](https://rodluger.github.io/starry/tutorials/hd189.html).
- [`cosmology`](https://github.com/esheldon/cosmology): cosmology package based on C, written by esheldon. Fast calculate distances. It can also be replaced by [`astropy.cosmology`](http://docs.astropy.org/en/stable/cosmology/index.html#module-astropy.cosmology).
- [`corner`](https://corner.readthedocs.io/en/latest/): A package of drawing corner diagrams of MCMC and 2d histogram. It's very easy to use and has many options. Good tool! You can find some examples in the `SN cosmology.ipynb`. [Song Huang](http://dr-guangtou.github.io) also uses `corner` to "explore" data: plot everything with everything. It can check the dependence between variables directly. Example by Song Huang: 

  ```python
  import corner 
  sdss_labels = [
        r'$u-g$', r'$g-i$',
        r'$\log \mathrm{EW}_{\mathrm{H}\alpha}$',
        r'$\log \mathrm{EW}_{\mathrm{H}\beta}$',
        r'$\log \mathrm{EW}_{[\mathrm{OIII}]}$'
    ]

  sdss_corner = corner.corner(
        sdss_obs, bins=15, color=plt.get_cmap('coolwarm')(0.9),
        smooth=0.5, labels=sdss_labels,
        label_kwargs={'fontsize': 22},
        quantiles=[0.16, 0.5, 0.84],
        plot_contours=True, fill_contours=True,
        show_titles=True, title_kwargs={"fontsize": 18},
        hist_kwargs={"histtype": 'stepfilled', "alpha": 0.8, "edgecolor": "none"},
        use_math_text=True)

  sdss_corner.set_size_inches(14, 14)
  ```

- [`multiprocess.Pool`](https://docs.python.org/3.7/library/multiprocessing.html): simple tool to run your loop tasks on multiple cores. This is embedded in `python` itself, and goes like below. For more complicated usage (multiple arguments as input), please refer to the documentation.

  ```python
  from multiprocessing import Pool
  def run_SBP(obj):
  slug.run_SBP(obj)

  print('Number of processor to use:')
  n_jobs = int(input())

  pool = Pool(n_jobs)
  pool.map(run_SBP, obj_cat)
  ```

- [`joblib`](https://joblib.readthedocs.io/en/latest/parallel.html): an awesome tool of building pipelines in python. Just like a superior `pickle`, it can dump and load functions and data (especially large data arrays) efficiently. It can also distribute loop tasks to multiple processors. See the usages below:

  ```python
  # Parallel computing
  from joblib import Parallel, delayed
  def run_SBP(obj):
  slug.run_SBP(obj)

  n_jobs = 4
  with Parallel(n_jobs=n_jobs, backend='loky') as parallel:
  parallel(delayed(run_SBP)(obj) for obj in obj_cat)
  ```

    There are various backends for this `Parallel` function, such as `loky`, `threading` and also `multiprocessing` as stated above. 

  ```python
  # Dump and load
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier()
  knn.fit(X_train, y_train)
  print(metrics.classification_report(y_test, knn.predict(X_test)))

  # After training a classifier using scikit-learn, 
  # you want to dump it and use it next time.
  import joblib
  joblib.dump(knn, './clf_cache/knn.joblib')
  # If you want to dump the file after compressing, use this.
  joblib.dump(knn, './clf_cache/knn.joblib.compress', compress=True)  
  ```
  
- [`ipyparallel`](https://ipyparallel.readthedocs.io/en/latest/index.html): Using IPython for parallel computing



# Tricks
### Build your package
- [How to write `requirements.txt` for a package](https://pip.readthedocs.io/en/1.1/requirements.html#requirements-file-format)
- [How to write documentation using `sphinx`](https://pythonhosted.org/an_example_pypi_project/sphinx.html) and [publish using `Readthedocs`](https://docs.readthedocs.io/page/intro/getting-started-with-sphinx.html).
- [Python Packaging User Guier (PyPI)](https://packaging.python.org): note that when pushing your local files in `dist` to PyPI, you only need to do `python3 -m twine upload dist/*`. Don't forget to add non-Python files in `MANIFEST.in` and `setup.py`.

### Jupyter Notebook

No matter under macOs or Linux, or even under Windows, you'll find that a quick check of Jupiter Notebook is hard and cumbersome. You need to open `jupyter notebook` in this folder to check, then terminate this thread. However, using a new tool [ipynb-quicklook](https://github.com/tuxu/ipynb-quicklook/) and a new app [Jupyter Notebook Viewer](https://github.com/tuxu/nbviewer-app), things get much more easier (under macOS and linux). Simply press `space` and check your notebooks!

The following are some other tricks involved when using `jupyter notebook`.

- `Command + click`: multiple cursors in a cell.
- `%load_ext autoreload`: import the IPython extension called `autoreload`. Then `%autoreload 2` will reload every module again automatically before executing.
- `%%time`: Magic command to time your cell for a single run. Useful!
- `%%timeit`: this command can be used to test your code's performance. It runs your cell for many times and calculate the mean time consumed. 
- `%matplotlib inline`: show Matplotlib figures inline. Useful!
- `%matplotlib qt`: show Matplotlib figures outside in a `Qt` interface, in which you can check positions and corresponding value of points.
- `%run ./two-histograms.ipynb`: this will run the notebook directly and shows every output from that notebook under this cell.
- `%load ./download_tri_color_images.py`: load the functions and constants defined in the input python file, and run this file.
- `%config InlineBackend.figure_format ='retina'`: show high resolution figures for Mac Retina screen. This won't affect the figure which is saved, it only affect the figure which is showed using `plt.show()`.
- `_` means the previous output. By adding `;` in the end of a command, it will suppress the useless output of a function.
  - Basic shell commands: `!` is external shell command, and `&` is to run this command as background.
- Click + `control`: Jupyter supports multiple cursors, similar to Sublime Text. (Use `alt` on Windows)
- [Jupyter extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions): my favorite extensions are  Codefolding, Nofity and Code prettify. You can simply install it by `pip install jupyter_contrib_nbextensions` or `conda install -c conda-forge jupyter_contrib_nbextensions`. 

### Formating strings

Tutorial: [https://pyformat.info](https://pyformat.info). I often use `length = {:.2f}.format(3.1415)` or `name = "DECaLS_{}".format('g_band'}`. 

### RegEx: Regular Expression

Tutorial: [https://github.com/ziishaned/learn-regex](https://github.com/ziishaned/learn-regex).

### Using Tqdm to show progress
See [https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar](https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar).

```python
from slug.imutils import TqdmUpTo
url = imutils.gen_url_hsc_s18a(obj['RA'], obj['Dec'], 
                       size * slug.HSC_pixel_scale, 
                       size * slug.HSC_pixel_scale, band)[0]
#urllib.request.urlretrieve(url, filename, imutils.reporthook)
with TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc=prefix) as t:  # all optional kwargs
    urllib.request.urlretrieve(url, filename=filename,
                       reporthook=t.update_to, data=None)
```
# Unix

#### Rsync

We use `rsync` to transfer files between two computers. It often goes like:

`rsync -avz --progress jiaxuanli@kungpao.ucsc.edu:/Users/jiaxuanli/Document/xxx.fits ~/Research/`

#### SSH

SSH is a tunnel through which you can connect with another computer (with fixed IP). It often goes like:

Login kungpao: `ssh -A -Y jiaxuanli@kungpao.ucsc.edu`. However you can set alias for this command by write `alias login_kungpao='ssh -A -Y jiaxuanli@kungpao.ucsc.edu'` in your `.bash_profile`.

Using the internet of kungpao: `ssh -g -qfnNT -D 7070 jiaxuanli@kungpao.ucsc.edu` and then set the port of SOCKS to be 7070.

Using Jupiter Notebook on kungpao but control it locally: `ssh -Y -N -L localhost:9999:localhost:9999 jiaxuanli@kungpao.ucsc.edu` (on your laptop); `jupyter notebook --no-browser --port=9999` (on your server kungpao).

The SSH session may be timeout very soon, check [here](https://bjornjohansen.no/ssh-timeout) for solutions.

#### SSHFS

When you find that using `ssh` and `rsync` is not convenient to see what you did, you need `sshfs` to mount your remote server to the local directory. 

First, you need to download and install `OSXFUSE` and `SSHFS` on [https://osxfuse.github.io](https://osxfuse.github.io) (directly download the `.pkg` files under "Stable Releases" and then install them.) Then, you need to set a mounting folder (need to be empty). For example, `mkdir ~/Research/kungpao`. 

Finally, it goes like `sshfs jiaxuanli@kungpao.ucsc.edu:/Users/jiaxuanli/ /Users/jiaxuanli/Research/kungpao/ -ovolname=kungpao`.

You will see a disk icon in folder `~/Research`. To unmount this "disk", type `diskutil unmount ~/Research/kungpao/`.

#### Screen

`screen` enables me to use multiple windows in the background when using `ssh`. 

Make a new screen window using `screen -S Jiaxuan`; then do whatever you want in that terminal; and detach that window using `Ctrl-a + d`. After got detached, the screen terminal is still running in the background. You can reconnect that terminal with `screen -r Jiaxuan`.