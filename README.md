# Python stubs for GIMP 3 plug-in development

This repository contains generated Python stubs for `gi.repository` modules that can aid in developing Python plug-ins for GIMP 3.0 or later, by providing code completion suggestions. The stubs can be used in a variety of IDEs such as PyCharm, from which these stubs were generated.

This repository additionally includes stubs for modules which PyCharm may fail to generate on some platforms [due to a bug](https://gitlab.gnome.org/GNOME/gimp/-/issues/10562).


## Installation

### PyCharm

Download the repository and copy the `gi` directory to a PyCharm directory containing other generated stubs. Overwrite if asked.

Assuming you added GIMP Python modules to your Python interpreter in PyCharm, you can find the path as follows:

1. Go to your PyCharm project and display the Project view.
2. Find `External Libraries `, expand it and find `Binary Skeletons`, right-click on `Binary Skeletons`, select `Copy Path/Reference...` and select `Absolute Path`.

It may happen that PyCharm automatically deletes the directories that you just copied when you restart PyCharm. To prevent the directories from being deleted:

* On Linux, run `chattr +i [directory]` for the `gi` directory.
* On Windows:
     1. Right-click on the `gi` directory, then go to `Properties -> Security -> Advanced`.
     2. Click on your user account (not SYSTEM or Administrators), then click `Disable inheritance`, then `Convert inherited permissions into explicit permissions for this object.`.
     3. Still having your user account selected, click `Edit`.
     4. In the displayed dialog, click `Show advanced permissions`, and then uncheck `Delete` and `Delete subfolders and files`.
     5. Save the changes.


### Other IDEs

In general, you can create a local environment (e.g. via `venv` or Anaconda) and then manually copy the `gi` directory under `Lib/site-packages`.
