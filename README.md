# abjad-ext-ipython-vscode

Abjad IPython Extension with vscode support

## Install
```
pip install abjad-ext-ipython-vscode
```

## Use

This extension was forked from `abjad-ext-ipython` and updated
to work with latest release of abjad. `abjad-ext-ipython` extension
has become outdated and can not be used with latest abjad releases.

This extension is used by abjad to display score in ipython notebook env directly
with `svg` produced by lilypond.

In addition, with vscode the color displayed for rendering score `svg`
directly looks weird and hard to see on default theme.
The `svg` is wrapped in a `div` and rendered as html to display it
correctly in this extension. 

In ipython env enable the extension,
```
%load_ext abjadext.ipython-vscode
```

you can test by running following code in the notebook,
```
import abjad
staff = abjad.Staff("c'4 d'4 e'4 f'4")
abjad.show(staff)
```

This should work in both vscode or standalone notebook environment.