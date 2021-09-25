# Vim keyboard generator

Simple python script that generated vim (or neovim) plugins
so that you can use your favorite keyboard in insert mode without
messing up the commands in the rest of the editor.

This is meant to be used on a keyboard with QWERTY stickers on it,
however support for others keyboard might come in the future.

In summary:

- Bind keys in insert mode so that you can use the keyboard config you like (say Colemak, or left-handed Dvorak).

- Preserves the QWERTY bindings on normal, visual and command modes
so you don't have to retrain your musle memory.

Used to generate [this colemake plugin](https://www.github.com/marhu98/)
and [and this dvorak plugin](https://www.github.com/marhu98/)
or [left handed version](https://www.github.com/marhu98/)
[or the right handed one](https://www.github.com/marhu98/)



## Use

There are several layouts, loaded in by default:

- Colemak
- Dvorak

To generate a plugin just run:

- Vim

```
python main.py layout_file
cat layout_file >> ~/.vimrc
```

- NeoVim

```
python main.py layout_file
cat layout_file >> ~/-config/nvim/init.vim
```

## Custom layout

To create a custom layout, say for example for QWERTY, just create a file
with all characters without spaces, from top to bottom and left to right:
```
cat qwerty
    qwertyuiopasdfghjklñzxcvbnm
```

Or for example left handed dvorak
```
cat qwerty
   ;qbyurso.6-kcdtheaz8'xgvwni 
```

(Notice is important to include the character left to the l, because some keyboards such as colemak or iso spanish use it).


## Custom output file

You can specify the output file by adding a cli argument:

```
python main.py layout_file result
cat result >> ~/.vimrc
```

### About the author

Check my personal website at: marhuenda.in
Check my blog at: blog.marhuenda.in

