#Insert Ts Reference Sublime 3 Plugin

Quickly insert a `///<reference path=".."``` to .ts files by searching for the closest "references.ts" file in the folder tree.

##Motivation
When writing web apps with TypeScript, it's common to have an aggregated file holding all the .d.ts declarations which are not imported explicitly (like Angular for example).
I got sick of adding the same `///<reference path="references.ts" />` line to my TypeScript files manually, and thinking about how deep the current file is comparing to my source root (where I usually have a single references.ts file), so I decided to write a plugin that will find the closest references.ts file going upwards (until reaching project root), and will add it to the top of the file as a reference node.

#Installation

Clone the repo directly into your Sublime plugin folder. For example, for Sublime Text 3 on a Mac this would look something like:

cd ~/"Library/Application Support/Sublime Text 3/Packages"
git clone --depth 1 https://github.com/GabiGrin/SublimeInsertTsReference.git InsertTsReference
And on Windows something like:

cd "%APPDATA%\Sublime Text 3\Packages"
git clone --depth 1 https://github.com/GabiGrin/SublimeInsertTsReference.git InsertTsReference
(--depth 1 downloads only the current version to reduce the clone size.)
Note if you are using the portable version of Sublime Text, the location will be different. (See http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory for more info).

#Usage

On your .ts file, press cmd+i followed by cmd+r (ctrl if you are using Windows), and if a references.ts file is present in your folder or on any of it's parent folders, it will be added automatically. You can also pop up the command pallette and type "insert TS reference".
You can change the file name to a different one using settings (project settings is also supported).
Because the file will be searched in parent directories recursively, multiple reference files can be used, i.e. one for e2e tests and one for application logic.

#Contributing
Never written in Python before, so feel free to improve and send a pull request :)

#License
MIT
