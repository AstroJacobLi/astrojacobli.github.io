---
layout: post
title:  "Macbook for Astronomy"
date:   2018-10-31 00:40:00
author: Jiaxuan Li
categories: Coding
---

# Set up your new MacBook for astronomy & astrophysics!
- [Anaconda](https://www.anaconda.com/download/#macos): Both python3 and python2 are OK.
- [Astroconda](https://astroconda.readthedocs.io/en/latest/): Add `astroconda` channel to your conda list, and then set up a new environment `iraf27`.
- Xcode: Download `Xcode` from your Mac AppStore.
- Useful python packages: [`fitsio`](https://github.com/esheldon/fitsio), [`emcee`](http://dfm.io/emcee/current/), [`cosmology` (a quick package for cosmology written in C)](http://dfm.io/emcee/current/), [`tqdm`](https://github.com/tqdm/tqdm).
- [XQuartz](https://www.xquartz.org): graphics library for ds9.
- Activating DS9: `export DISPLAY=:0.0` in your terminal.
- LaTeX environment: [MacTex](http://www.tug.org/mactex/) works good for me. I don't have money to buy other IDE, so I use TeXShop. But for Windows, `TexStudio` is really really good.
- `Consolas` font: You can download from https://astrojacobli.github.io/astro-ph/Consolas.ttf
- [Mendeley](https://www.mendeley.com): paper management and reader, worth trying.
- [Slack](https://slack.com/downloads/osx): definitely a good tool for communication and cooperation.
- [TOPCAT](http://www.star.bris.ac.uk/~mbt/topcat/): Best tool for manipulating tables, best assistant of catalog astrophysicist.
- [STILTS](http://www.star.bris.ac.uk/~mbt/stilts/): A command-line edition of TOPCAT. Both TOPCAT and STILTS require JAVA environment. After install JAVA, you need to write the following into your `.bash_profile`:
```python
export JAVA_HOME="/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home"
export PATH=${JAVA_HOME}/bin:$PATH
```

- [Mathematica](http://www.wolfram.com/mathematica/): Best language to do mathematical physics study.
- Don't know how to write your symbol in latex? Use [Detexify](http://detexify.kirelabs.org/classify.html)!
- Jesus! Get LaTeX code from the screenshots: [**MathPix**](https://mathpix.com)
- Jazz up your terminal **(but I failed)**: https://medium.freecodecamp.org/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22
- It's hard to get your hands on `vim` without a [cheatsheet](http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html)
- A useful widget `cosmoWidget` to calculate cosmological distances in MacOS Dashboard: https://beckermr.github.io/cosmowidget.html
- LaTeX package for SI units: [siunitx](https://ctan.org/pkg/siunitx)
- [Homebrew](https://docs.brew.sh/FAQ) is another good tool for installing packages, especially those written in C/C++. Sometimes `brew` will update itself automatically, then you can stop it directly by `control + C`. 

#### **When your terminal cannot recognize anything, do this:**
```python
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
```


### Play with a new Linux machine

Accidentally I have to make a Windows machine to Linux. I installed Debian on that machine. Some tips are listed below.

1. Originally, your account is not listed in the `sudo` group. You have to run `su -` so that you are switched to the `root` environment. After that, run `gpasswd -a jiaxuanl sudo` to add `jiaxuanli` to the `sudo` group.



## Install [the Tractor](https://github.com/dstndstn/tractor)

[`the Tractor`](https://github.com/dstndstn/tractor) is a probability-based astronomical source detection & measurement tool, written by Dustin Lang and David Hogg.

0. Make sure you have installed XCode from Mac AppStore. Then execute: 
```python
$ sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer/$.
```

1. Install fitsio: `$ pip install fitsio`
2. Install emcee: `$ pip install emcee`
3. Install Homebrew: `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
4. Using Homebrew to install cairo: `$ brew install cairo`
5. Install jpeg: `$ brew install jpge`
6. Install eigen3: `$ brew install eigen3`
7. Add these paths to your `.bash_profile`:
```python
export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"
export LDFLAGS="-L/usr/local/opt/libffi/lib"
export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
export PATH="/usr/local/opt/openssl/bin:$PATH" 
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```
7. Sometimes `cairos` still doesn't work. Then you can:

```python
$ pkg-config --atleast-version=1.12.2 cairo
$ echo $?
```
If it returns a 1 you will need to set the PKG_CONFIG_PATH environment variable so cairo.pc and fontconfig.pc can be found.
```python
$ sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist 
$ locate cairo.pc
$ export PKG_CONFIG_PATH=/usr/X11/lib/pkgconfig/
```
Then do this again:
```python
$ pkg-config --atleast-version=1.12.2 cairo
$ echo $?
```
If it returns a 0 then all is well in the hood.

8. Download `astrometry.net` package:
```python
$ wget http://astrometry.net/downloads/astrometry.net-latest.tar.bz2
$ tar xjf astrometry.net-latest.tar.bz2
$ cd astrometry.net-*
```
9. Install `astrometry.net`:
```python
$ make
$ make py
$ make extra
$ make install INSTALL_DIR="~/Research/Packages/astrometry" PYTHON_SCRIPT="/anaconda3/bin/python"
```
Sometimes, it will show an error that `fatal error: 'cairo.h' file not found`.

You can just do `export PKG_CONFIG_PATH=/opt/X11/lib/pkgconfig` and see if it could fine `cairo.h`.

10. Install `swig`: `$ brew install swig`

11. Install `tractor`: first go to its folder, then
```python
$ make
$ python setup.py install
```

😂 You get it! 👏 

***

## Install [Imfit](http://www.mpe.mpg.de/~erwin/code/imfit/markdown/index.html)

Requirements: [CFITSIO](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/fitsio_macosx.html), [GNU Scientific Library](http://ftp.wayne.edu/gnu/gsl/), [FFTW](http://www.fftw.org) (which is used by many other packages as well), [NLopt](https://nlopt.readthedocs.io/en/latest/). You also need to install `CMake` by `$ brew install cmake` to install `NLopt`. Almost all of these packages should be installed by `$ ./configure & make & make install`. However, please check `INSTALL` file for more detailed description. You also need to install `pip install scons`. After all these preparation, install `imfit` with `$ scons —no-openmp imfit & scons —no-openmp imfit-mcmc & scons —no-openmp makeimage`.

---

#### References

http://www.astrobetter.com/wiki/Setup+a+New+Mac+for+Astronomy

http://www.astrobetter.com/wiki/tiki-index.php?page=Mac+Apps

https://github.com/dstndstn/tractor

http://macappstore.org/swig/

https://stackoverflow.com/questions/22100213/package-cairo-was-not-found-in-the-pkg-config-search-path-node-j-s-install-canv