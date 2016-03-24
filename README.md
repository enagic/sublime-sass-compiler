Portable sass/scss compiler for Sublime Text 2 & 3
====================================

Description
-----------

Portable build system that includes a sidebar menu item for *.sass/*.scss files to build to *.css files.

I was motivated to create a sass build plugin for myself that didn't require any environmental dependencies due to my sans admin status on my work computer.  Being that Java is more readily available than Ruby, I decided to go with jruby.jar as the binary of choice.  This variant includes scss/sass gem preinstalled.

Prerequisites
-------------

Requires **Java**


Installing
----------
**OPTION 1 - With the Package Control plugin (recommended)**

The easiest way to install this package is through Package Control.

1. Download and install the [Package Control Plugin](http://wbond.net/sublime_packages/package_control).
Follow the instructions on the website.
2. Open the command panel: `Control+Shift+P` (Linux/Windows) or `Command+Shift+P` (OS X) and select '**Package Control: Install Package**'.
3. When the packages list appears type '**SASS**' and you'll find the **SASS Compiler**. Select to install it.
4. Find your *.sass/*.scss files in your project sidebar.  Right click the main file and select `Build to css` from the options.


**OPTION 2 - With Git**

Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/enagic/sublime-sass-compiler.git SassCompiler

You can find your 'Packages' inside the following directories:

* Sublime Text 2:
    `%APPDATA%/Sublime Text 2/Data/Packages/`
* Sublime Text 3:
    `%APPDATA%/Sublime Text 3/Data/Packages/`

**OPTION 3 - Without Git**

Download the latest source zip from [Github](https://github.com/enagic/sublime-sass-compiler) and extract it into a new folder named `SassCompiler` in your Sublime Text "Packages" folder.

Settings
--------

The following **SassCompiler** settings are available in SassCompiler/SassCompiler.sublime-settings (defaults shown below).

* `java_home`: ``
* `cache`: false
* `cache_location`: ``
* `include_line_comments`: false
* `include_line_numbers`: true
* `style`: `nested`


Todo
----

* OSX/Linux support
* Compass support

Author
------

Created by **Michael Kwon**.

Disclaimer
-----------

I do not claim Python to be my primary language so apologies to the Python community for ruining the language.

### License
Copyright (C) 2016 Michael Kwon

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
