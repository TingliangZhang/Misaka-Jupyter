# Misaka-Jupyter

Dependence

```
pip install digi-xbee matplotlib numpy 
```



## JupyterLab Installation

参考TUNA的[pypi 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

If you use `pip`, you can install it with:

```
pip install jupyterlab
```

Start JupyterLab using:

```
jupyter lab
```



## [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest/index.html#)

[jupyter-widgets](https://github.com/jupyter-widgets)/**[ipywidgets](https://github.com/jupyter-widgets/ipywidgets)** Installation With pip    注意安装前关闭Jupyter Lab再安装

```
pip install ipywidgets
jupyter nbextension enable --py --sys-prefix widgetsnbextension  # can be skipped for notebook version 5.3 and above
```

Besides the widgets already provided with the library, the framework can be extended with custom widget libraries.

A template project is available in the form of a cookie cutter [here](https://github.com/jupyter-widgets/widget-ts-cookiecutter).

Popular widget libraries such as [bqplot](https://github.com/bloomberg/bqplot), [pythreejs](https://github.com/jovyan/pythreejs) and [ipyleaflet](https://github.com/ellisonbg/ipyleaflet)

follow exactly the same template and directory structure. They can serve as more advanced examples of usage of the Jupyter widget infrastructure.

For detailed information, please refer to the [ipywidgets documentation](https://ipywidgets.readthedocs.io/en/latest/).



## **[ipywidgets](https://github.com/jupyter-widgets/ipywidgets)**插件安装

[bqplot](https://github.com/bloomberg/bqplot) Installation Using pip:

```
$ pip install bqplot
$ jupyter labextension install bqplot
```

bqplot    问题    Error displaying widget: model not found

通过list看一下版本是不是最新的

```
jupyter labextension list
```

尝试安装jupyter-matplotlib（没有卵用）

```
jupyter labextension install jupyter-matplotlib
```

uninstall it with `jupyter labextension uninstall bqplot`)

[pythreejs](https://github.com/jovyan/pythreejs) Installation Using pip:

```
pip install pythreejs
jupyter labextension install @jupyter-widgets/jupyterlab-manager 
jupyter labextension install jupyter-threejs
```

[ipyleaflet](https://github.com/ellisonbg/ipyleaflet) Installation Using pip:

```
pip install ipyleaflet
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet
```



## 参考

[JupyterLab Documentation](https://jupyterlab.readthedocs.io/)

[Jupyter Widgets](https://ipywidgets.readthedocs.io/en/latest/index.html#)

[XBee Python Library](https://xbplib.readthedocs.io/en/stable/index.html)

