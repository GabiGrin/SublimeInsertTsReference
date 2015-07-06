#Insert Ts Reference Sublime 3 Plugin

Quickly insert a `///<reference path=".."``` to .ts files by searching for the closest "references.ts" file in the folder tree.

##Motivation
I got sick of adding the same `///<reference path="references.ts" />``` line to my TypeScript files manually, and thinking about how deep the current file is comparing to my source root (where I usually have a single references.ts file), so I deciding to write something that will find the closest references file going upwards (until reaching project root), and will add it to the top of the file.

#Installation

Clone the repo directly into your Sublime plugin folder. For example, for Sublime Text 3 on a Mac this would look something like:

cd ~/"Library/Application Support/Sublime Text 3/Packages"
git clone --depth 1 https://github.com/GabiGrin/InsertTsReference-Sublime-Plugin.git InsertTsReference
And on Windows something like:

cd "%APPDATA%\Sublime Text 3\Packages"
git clone --depth 1 https://github.com/GabiGrin/InsertTsReference-Sublime-Plugin.git InsertTsReference
(--depth 1 downloads only the current version to reduce the clone size.)
Note if you are using the portable version of Sublime Text, the location will be different. (See http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory for more info).

#Usage

On your .ts file, press cmd+i, cmd+r (ctrl if you are using Windows), and if a references.ts file is present in your folder it will be added automatically. You can also pop up the command pallette and type "insert TS reference"
You can change the file name to a different one using settings (project settings is also supported).
Because the file will be searched in parent directories recursively, multiple reference files can be used, i.e. one for e2e tests and one for application logic.

#License
MIT
