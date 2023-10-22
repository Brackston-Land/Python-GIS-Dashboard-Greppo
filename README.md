# Python-GIS-Dashboard-Greppo

## Description

A geospatial dashboard built with Greppo showing Landfills and Recycle facilities in Austin, Texas


![Demo GIF](vector-demo/Demo_GIF.gif)

## Getting Started

### Dependencies

greppo==0.0.33

Shapely==1.8.4 (be sure to use 1.8.4 or later)


### Installing

cd into working folder

```
cd Downloads\Python-Geospatial-Dashboard-Greppo-master\Python-Geospatial-Dashboard-Greppo-master
```
create a virtual environment

```
python -m venv venv
```
activate the virtual environment

```
.\venv\Scripts\activate
```
install greppo

```
python -m pip install greppo
```
ensure Shapely is up to date

```
pip install Shapely==1.8.4
```


### Executing program

run greppo 

```
greppo serve ./vector-demo/app.py
```

open up a browser and navigate to the provided address (ex:  http://127.0.0.1:8080/)



![image](https://github.com/Brackston-Land/Python-Geospatial-Dashboard-Greppo/assets/147285744/95dbbd3b-bae7-4328-9216-5109c925ab10)



## Authors

Brackston Land 

https://www.linkedin.com/in/brackston-land-799718173/

brackston.gis@gmail.com


## Acknowledgments

Inspiration, code snippets, etc.

[Build a geospatial dashboard in Python using Greppo](https://towardsdatascience.com/build-a-geospatial-dashboard-in-python-using-greppo-60aff44ba6c9)
