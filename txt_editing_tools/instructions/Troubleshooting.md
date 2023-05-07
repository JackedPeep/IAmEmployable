# CS 1440 Assignment 2: Text Tools - Troubleshooting

## bash: tt.py: command not found

This error indicates either that the directory containing `tt.py` is not
correctly specified in your `PATH`, or the `tt.py` script is not executable.

*   Launch a new console and try again.  The shell reads its startup file once upon startup; changes made to it don't automatically affect instances of the shell that are already running.
*   Double-check the spelling of the directory containing `tt.py` within `~/.bash_profile` (for Bash users) or `~/.zshrc` (for Zsh enjoyers).
*   The path to `tt.py` should end in `src`.
*   If the path to `tt.py` on your system contains spaces, make sure they are properly escaped with backslashes `\`.
*   Enter the `src/` directory of your Assignment 2 project and run this command to mark the file `tt.py` as executable:

```
$ chmod +x tt.py
```


## No such file or directory

Errors messages containing these words look like the following:

```
/usr/bin/env: 'python': No such file or directory
```

```
bash: /c/Users/user/Desktop/cs1440-falor-erik-assn2/src/tt.py: /usr/bin/env: bad interpreter: No such file or directory
```

The remedy is to update the shebang line in `tt.py`.  The first line of `tt.py`
looks like this:

```
#!/usr/bin/env python
```

This line tells the bash shell which programming language to run the contents of that file in.  The name "shebang" is short for "hash-bang" and refers to the first two characters of the file.

The shebang line I provided *should* work for most systems.  When it doesn't, you'll get one of the above error messages.  If this happens to you, replace my shebang line with the location of the Python interpreter on your system.

0.  Find your python interpreter by running `which python`.  If you need to specifically run your code with `python3`, use `which python3`.
1.  Replace the entire first line of `tt.py` with a new line that begins with `#!` followed by the path returned by `which`.  The result will look something like this if you're using Git+Bash on Windows: `#!/c/Users/user/AppData/Local/Programs/Python/Python39/python`



## Error: stdout is not a tty

If you are a Windows user who has previously taken this class, you might see this error when you try to redirect the output of `tt.py` to a file:

```
$ python src/tt.py head README.md > testfile
stdout is not a tty
```

This error occurs when your `python` command is an *alias* that runs Python through a helper program called `winpty` that is included with Git+Bash.

Recent versions of Git+Bash include a new experimental feature labeled **enable experimental support for pseudo consoles** which avoids the need for `winpty`, so you don't need that aliased command any longer.

Temporarily disable the alias in this shell session with the `unalias` command and re-run the command:

```
$ unalias python
$ python src/tt.py head README.md > testfile
```

If `unalias` fixes the problem, remove the alias from your `~/.bash_profile` and re-start your shell.

If the `alias` command reveals no alias for the `python` command, contact a TA or the instructor for help.

```
$ alias python
bash: alias: python: not found
```
