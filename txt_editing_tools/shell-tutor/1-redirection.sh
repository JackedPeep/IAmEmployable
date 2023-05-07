#!/bin/sh

_HELP="
Shell Redirection Lesson
===========
* Redirect shell command output to a file
* Append shell command output to a file
* The STDOUT file descriptor
* The STDERR file descriptor
* Control printing to STDOUT or STDERR in python
* Remove unneeded command output

Commands used in this lesson
============================
* '>'
  * Redirect only standard output to a file
* '>>'
  * Redirect only standard output to a file, appending to existing file
* '2>'
  * Redirect only standard error to a file
* '&>'
  * Redirect standard output and standard error to a file
* /dev/null
  * A special file that acts as a 'black hole', swallowing up all
      information given to it
"

PATH="$PWD/.lib:$PATH"

. shell-compat-test.sh

source record.sh
source platform.sh

if [[ -n $_TUTR ]]; then
	source ansi-terminal-ctl.sh
	source generic-error.sh
	source nonce.sh

	_code() { (( $# == 0 )) && echo $(cyn code) || echo $(cyn "$*"); }
	_py() { (( $# == 0 )) && echo $(grn Python) || echo $(grn $*) ; }
	_STDOUT() { (( $# == 0 )) && echo $(blu STDOUT) || echo $(blu "$*"); }
	_STDERR() { (( $# == 0 )) && echo $(red STDERR) || echo $(red "$*");  }

	fix-files() {
		_generate_aux_files	
		
		if [[ -n $OUTPUT_STREAMS_CONTENTS ]]; then
			echo "$OUTPUT_STREAMS_CONTENTS" > "$_BASE/outputStreams.py"
			OUTPUT_STREAMS_HASH=$(git hash-object "$_BASE/outputStreams.py")
		fi
	}

	fix-outputStreams() {
		_generate_post_outputStreams
	}

fi

runPython() {
	# Argument 1: Path to Python program to run
	_PY_PROGRAM_PATH=$1
	if [[ $_PLAT = WSL ]]; then
		_PY_PROGRAM_PATH=$(wslpath -w "$_PY_PROGRAM_PATH")
	fi
	$_PY "$_PY_PROGRAM_PATH"
}

_generate_post_outputStreams() {
	cat <<-: > "$_BASE/outputStreams.py"
	import sys

	print("My output goes to STDOUT by default.")
	print("I can explicitly output to STDOUT with the file parameter.", file=sys.stdout)
	print("I can also put output on STDERR with the file parameter.", file=sys.stderr)
	:
	OUTPUT_STREAMS_HASH=$(git hash-object "$_BASE/outputStreams.py")
	OUTPUT_STREAMS_CONTENTS=$(cat "$_BASE/outputStreams.py")
}

_python_not_found() {
	cat <<-PNF
	I could not find a working Python 3 interpreter on your computer.
	It is required for this lesson.

	Contact erik.falor@usu.edu for help
	PNF
}

_generate_aux_files() {
	cat <<-'FILE' > "$_BASE/first.md"
	# First File

	This is the first file you should be putting together. I don't have anything
	interesting in me!

	## Subsection of First File

	Wow, even more non-interesting stuff!

	FILE

	cat <<-'FILE' > "$_BASE/second.md"
	# Second File

	This is the second file you want to stitch together. I don't have anything
	interesting in me either!

	FILE

	cat <<-'FILE' > "$_BASE/third.md"
	# Third File

	Wow, this is a *third* file! I bet you didn't expect this.

	```
	  ________________________
	< Hey... got any grapes? >
	 ------------------------
	 \
	  \
	   \ >()_
	      (__)__ _
	```

	This is the end of the third file :(
	FILE

	cat <<-'FILE' > "$_BASE/nameError.py"
	print("Hello, my friend.")
	print("I'm about to do something illegal... friends don't snitch, right?")
	print(variable_that_does_not_exist)
	FILE

	cat <<-'FILE' > "$_BASE/outputStreams.py"
	import sys

	print("My output goes to STDOUT by default.")
	print("I can explicitly output to STDOUT with the file parameter.")
	print("I can also put output on STDERR with the file parameter.")
	FILE

	FIRST_FILE_HASH=$(git hash-object "$_BASE/first.md")
	SECOND_FILE_HASH=$(git hash-object "$_BASE/second.md")
	THIRD_FILE_HASH=$(git hash-object "$_BASE/third.md")
	NAME_ERROR_HASH=$(git hash-object "$_BASE/nameError.py")
	OUTPUT_STREAMS_HASH=$(git hash-object "$_BASE/outputStreams.py")
	export FIRST_FILE_HASH SECOND_FILE_HASH THIRD_FILE_HASH NAME_ERROR_HASH OUTPUT_STREAMS_HASH
}

_damaged_files_check() {
	# Optional Argument: 
	#	1 : pre|during|post
	#	  if pre is set, check all files for changes, and restore outputStreams.py to original default 
	#		(same behavior as no arguments given)
	#	  if during is set, don't worry about changes to outputStreams.py and copy current outputStreams.py
	#		to another file before restoring others, and then move it back in place
	#	  if post is set, if files are regenerated, outputStreams.py gets changed to what it should be
	#		after adding file=sys.stdout and file=sys.stderr to the print statements

	[[ $(git hash-object "$_BASE/first.md" 2>/dev/null) == "$FIRST_FILE_HASH" ]]
	_FIRST_FILE_CHANGED=$?
	[[ $(git hash-object "$_BASE/second.md" 2>/dev/null) == "$SECOND_FILE_HASH" ]]
	_SECOND_FILE_CHANGED=$?
	[[ $(git hash-object "$_BASE/third.md" 2>/dev/null) == "$THIRD_FILE_HASH" ]]
	_THIRD_FILE_CHANGED=$?
	[[ $(git hash-object "$_BASE/nameError.py" 2>/dev/null) == "$NAME_ERROR_HASH" ]]
	_NAMEERROR_FILE_CHANGED=$?
	[[ $(git hash-object "$_BASE/outputStreams.py" 2>/dev/null) == "$OUTPUT_STREAMS_HASH" ]]
	_OUTPUTSTREAMS_FILE_CHANGED=$?
	
	_FILES_CHANGED_SUM=$(( $_FIRST_FILE_CHANGED + $_SECOND_FILE_CHANGED + $_THIRD_FILE_CHANGED + $_NAMEERROR_FILE_CHANGED ))
	
	if [[ -z $1 || $1 == post || $1 == pre ]]; then
		# check outputStreams.py file for changes
		_FILES_CHANGED_SUM=$(( $_FILES_CHANGED_SUM + $_OUTPUTSTREAMS_FILE_CHANGED ))
	fi

	if (( _FILES_CHANGED_SUM != 0 )); then
		cat <<-MSG

		It appears you have accidentally damaged one or more of the files
		needed by this lesson. I am going to go ahead and fix that for you now
		by regenerating all of the files you need for this lesson.

		Regenerating files...
		MSG

		if [[ -z $1 || $1 == pre ]]; then
			_generate_aux_files
		elif [[ $1 == during ]]; then
			[[     -f "$_BASE/outputStreams.py" ]] &&
				mv -f "$_BASE/outputStreams.py" "$_BASE/TEMP_outputStreams.py"
			_generate_aux_files
			[[     -f "$_BASE/TEMP_outputStreams.py" ]] &&
				mv -f "$_BASE/TEMP_outputStreams.py"  "$_BASE/outputStreams.py" &&
				# Hash is reset in _generate_aux_files; this makes sure it matches
				# 	the hash for the file the user created
				OUTPUT_STREAMS_HASH=$(git hash-object "$_BASE/outputStreams.py")
		elif [[ $1 == post ]]; then
			_generate_aux_files
			if [[ -n $OUTPUT_STREAMS_CONTENTS ]]; then
				echo "$OUTPUT_STREAMS_CONTENTS" > "$_BASE/outputStreams.py"
			fi
		fi
	fi


}

setup() {
	_tutr_record_repeat_prompt
	source screen-size.sh 80 30

	if   which python &>/dev/null && [[ $(python -V 2>&1) = "Python 3"* ]]; then
		export _PY=python
	elif which python3 &>/dev/null && [[ $(python3 -V 2>&1) = "Python 3"* ]]; then
		export _PY=python3
	else
		_tutr_die _python_not_found
	fi

	export _BASE="$PWD/shell-redirection"
	[[ -d "$_BASE" ]] && rm -rf "$_BASE"
	mkdir -p "$_BASE"

	_generate_aux_files
}


prologue() {
	[[ -z $DEBUG ]] && clear
	cat <<-PROLOGUE

	Shell Redirection Lesson: How to control where the output of a shell
	command goes.

	In this lesson you will learn

	* How to redirect shell command output to a file
	* How to append shell command output a file
	* The $(_STDOUT) file descriptor
	* The $(_STDERR) file descriptor
	* Control printing to $(_STDOUT) or $(_STDERR) in python
	* How to remove unneeded command output

	Commands used in this lesson
	============================
	* $(cmd '>')
	    * Redirect only standard output to a file
	* $(cmd '>>')
	    * Redirect only standard output to a file, appending to existing file
	* $(cmd '2>')
	    * Redirect only standard error to a file
	* $(cmd '&>')
	    * Redirect standard output and standard error to a file
	* $(path /dev/null)
	    * A special file that acts as a $(bld 'black hole'), swallowing up all
	        information given to it

	Let's get started!

	PROLOGUE

	_tutr_pressanykey
}



cat_to_terminal_prologue() {
	cat <<-MSG
	I'm sure you've used the $(cmd cat) command plenty of times by now. Most
	likely to have the contents of a file print out to the terminal. Are
	you aware of what the $(cmd cat) command stands for and it's original
	purpose?

	The $(cmd cat) command stands for $(bld concatenate); the process of linking
	things together. The $(cmd cat) command was created to allow someone to
	concatenate multiple text files together into one! This is done by
	giving the $(cmd cat) command multiple arguments in the order we want the
	files to be concatenated together.

	Try that now. Let's concatenate $(path first.md) and $(path second.md) together.
	MSG
}

cat_to_terminal_test() {
	_tutr_nonce && return $PASS

	_tutr_generic_test -d "$_BASE" -c cat -a "first\\.md" -a "second\\.md"
}

cat_to_terminal_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat first.md second.md" "$_BASE"
			;;
	esac
	_damaged_files_check
}

cat_to_final_md_prologue() {
	cat <<-MSG
	What if we want to concatenate those files together *and* save the
	output to a file? Well, we could always just highlight all of that
	output, copy it, open a text editor, and paste it there. That's really
	tedious though. There must be a better way...

	Luckily for us, our system shell has a feature that will help! Shell
	output redirection is the solution to our problems. We have the ability
	to place the output from one command into a specified file by adding
	just a few more characters to our initial command.

	To redirect the command output to a file, we add $(cmd '> FILENAME') to the
	end of our shell command. $(cmd '>') is the key operator that tells our shell
	we want to redirect the output, and $(path FILENAME) is the file we want to
	place the output into.

	Be careful when doing this, as the file $(path FILENAME) will be removed and
	replaced by the command output in the process.
	MSG
	_tutr_pressanykey

	cat <<-MSG

	Let's now concatenate the files $(path first.md) and $(path second.md) together,
	placing the result in the file named $(path final.md).
	MSG
}

cat_to_final_md_test() {
	MISSING_PART_OF_FILE=99
	FILES_IN_WRONG_ORDER=98
	TOO_MANY_COPIES=97

	_tutr_nonce "rm" && return $PASS

	if [[ -f "$_BASE/final.md" ]]; then
		FIRST_FILE_IN_FINAL=$(grep "# First File" "$_BASE/final.md" | wc -l)
		SECOND_FILE_IN_FINAL=$(grep "# Second File" "$_BASE/final.md" | wc -l)
		if (( $FIRST_FILE_IN_FINAL == 0 || $SECOND_FILE_IN_FINAL == 0)); then
			return $MISSING_PART_OF_FILE
		else
			if (( $FIRST_FILE_IN_FINAL > 1 || $SECOND_FILE_IN_FINAL > 1 )); then
				return $TOO_MANY_COPIES
			elif [[ $(head -n 1 final.md) == "# First File" ]]; then
				return 0
			else
				return $FILES_IN_WRONG_ORDER
			fi
		fi
	else
		_tutr_generic_test -d "$_BASE" -c cat -a "first\\.md" -a "second\\.md" -a '>' -a "final\\.md"
	fi
}

cat_to_final_md_hint() {
	case $1 in
		$PASS)
			;;
		$MISSING_PART_OF_FILE)
			cat <<-MSG
			It appears that you did not concatenate both of the files together. One
			or both of the files are missing from $(path final.md). Try again.
			MSG
			;;
		$FILES_IN_WRONG_ORDER)
			cat <<-MSG
			It appears that you accidentally swapped the order of the files. You
			want to concatenate the file $(path first.md) *before* the file $(path second.md).
			Try again.
			MSG
			;;
		$TOO_MANY_COPIES)
			cat <<-MSG
			It appears you accidentally con$(cmd cat)enated too many copies of one
			(or both) files to $(path final.md)! Try that again, only $(cmd cat)ing one copy
			of each file to $(path final.md).
			MSG
			;;
		*)
			_tutr_generic_hint $1 "cat first.md second.md > final.md" "$_BASE"
			;;
	esac

	_damaged_files_check
}

cat_to_final_md_epilogue() {
	_tutr_pressanykey
}



inspect_final_md1_prologue() {
	cat <<-MSG
	Now there's nothing new on your screen.

	Instead, the output from $(cmd cat)ing $(path first.md) and $(path second.md)
	was sent into the new file $(path final.md).

	Use $(cmd cat) or $(cmd less) to view this file.
	MSG
}

inspect_final_md1_test() {
	_tutr_nonce && return $PASS

	if [[ ${_CMD[0]} == 'less' ]]; then
		_tutr_generic_test -d "$_BASE" -c "less" -a "final\\.md"
	else
		_tutr_generic_test -d "$_BASE" -c "cat" -a "final\\.md"
	fi
}

inspect_final_md1_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat final.md" "$_BASE"
			;;
	esac

	if [[ ! -f final.md ]]; then
		cat <<-MSG

		It appears you've deleted $(path final.md) before viewing it! How about you
		don't do that, m'kay?

		You'll need to regenerate the file by running:
		  $(cmd 'cat first.md second.md > final.md')
		to continue.

		MSG
	fi

	_damaged_files_check
}

inspect_final_md1_epilogue() {
	cat <<-MSG
	Woah! We were able to successfully take the output of a command and
	place it's result into a new file. All we needed to do was add $(cmd '>') to
	the command! Isn't that neat?
	MSG
	_tutr_pressanykey
}

append_to_final_md_prologue() {
	cat <<-MSG
	We've used output redirection to take the output of one command and
	place it into a brand new file. One side effect of this action is that
	the file we place our output into gets deleted and created anew
	*before* we place the output into it. Sometimes we don't always want to
	do that. Maybe we want to add the output of a command to end of an
	existing file?

	Luckily we have another redirection operator that will perform this
	action for us! Instead of using $(cmd '>'), we use $(cmd '>>') to append to a file.

	Let's try this now by appending $(path third.md) to $(path final.md). Use $(cmd cat) to
	get the output of $(cmd third.md), and $(cmd '>>') to append it to $(path final.md).
	MSG
}

append_to_final_md_test() {
	MISSING_PART_OF_FILE=99
	FILES_IN_WRONG_ORDER=98
	FINAL_WAS_DELETED=97
	APPEND_NOT_USED=96
	TOO_MANY_COPIES=95

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/final.md" ]]; then
		FIRST_FILE_IN_FINAL=$(grep "# First File" "$_BASE/final.md" 2>/dev/null | wc -l)
		SECOND_FILE_IN_FINAL=$(grep "# Second File" "$_BASE/final.md" 2>/dev/null | wc -l)
		THIRD_FILE_IN_FINAL=$(grep "# Third File" "$_BASE/final.md" 2>/dev/null | wc -l)
		if (( $FIRST_FILE_IN_FINAL == 0 || $SECOND_FILE_IN_FINAL == 0 || $THIRD_FILE_IN_FINAL == 0 )); then
			return $MISSING_PART_OF_FILE
		else
			if [[ ${_CMD[*]} != *">>"* ]]; then
				return $APPEND_NOT_USED
			elif (( $FIRST_FILE_IN_FINAL > 1 || $SECOND_FILE_IN_FINAL > 1 || $THIRD_FILE_IN_FINAL > 1 )); then
				return $TOO_MANY_COPIES
			elif [[ $(head -n 1 "$_BASE/final.md") == "# First File" &&
				  $(tail -n 1 "$_BASE/final.md") == "This is the end of the third file :(" ]]; then
				return 0
			else
				return $FILES_IN_WRONG_ORDER
			fi
		fi
	else
		return $FINAL_WAS_DELETED
	fi
}

append_to_final_md_hint() {
	case $1 in
		$PASS)
			;;
		$MISSING_PART_OF_FILE)
			cat <<-MSG
			It appears that $(path final.md) is missing part of what it needs. You need
			to append the file $(path third.md) to the end of $(path final.md) using the append
			shell redirection operator.

			Run the command $(cmd 'cat third.md >> final.md') to proceed.
			MSG
			;;
		$FILES_IN_WRONG_ORDER)
			cat <<-MSG
			It appears that $(cmd final.md) got put together in the wrong order. I don't
			know how you did that... congrats, I guess?

			I'll fix that momentarily.

			Run the command $(cmd 'cat third.md >> final.md') to proceed.
			MSG
			# Delete final.md so it will assuredly get regenerated correctly
			[[ -f "$_BASE/final.md" ]] && command rm "$_BASE/final.md"
			;;
		$FINAL_WAS_DELETED)
			cat <<-MSG
			It appears you accidentally deleted $(path final.md)... I will regenerate it
			for you momentarily.

			Run the command $(cmd 'cat third.md >> final.md') to proceed.
			MSG
			;;
		$APPEND_NOT_USED)
			cat <<-MSG
			It appears you didn't use the append file redirection operator $(cmd '>>').
			You sneak! Try again, but this time actually use the append operator.

			Run the command $(cmd 'cat third.md >> final.md') to proceed.
			MSG
			# Delete final.md so it will assuredly get regenerated correctly
			[[ -f "$_BASE/final.md" ]] && command rm "$_BASE/final.md"
			;;
		$TOO_MANY_COPIES)
			cat <<-MSG
			It appears that $(cmd final.md) got put together with too many copies of one
			(or more) of the files it was supposed to.

			I'll fix that momentarily, and restore $(path final.md) to it's original state.

			Run the command $(cmd 'cat third.md >> final.md') to proceed.
			MSG
			# Delete final.md so it will assuredly get regenerated correctly
			[[ -f "$_BASE/final.md" ]] && command rm "$_BASE/final.md"
			;;
	esac

	_damaged_files_check

	FIRST_FILE_IN_FINAL=$(grep "# First File" "$_BASE/final.md" 2>/dev/null | wc -l)
	SECOND_FILE_IN_FINAL=$(grep "# Second File" "$_BASE/final.md" 2>/dev/null | wc -l)
	# We do NOT want third file to be in final, so let's check that
	# Can happen if student doesn't use >> and manually appends all three files
	THIRD_FILE_IN_FINAL=$(grep "# Third File" "$_BASE/final.md" 2>/dev/null | wc -l)
	if [[ ! -f "$_BASE/final.md" || (( $FIRST_FILE_IN_FINAL == 0 )) ||(( $SECOND_FILE_IN_FINAL == 0 )) || (( $THIRD_FILE_IN_FINAL > 0 ))
		  ||  $(head -n 1 final.md 2> /dev/null) != "# First File" ]]; then
		cat <<-MSG

		The file $(path final.md) was changed in a way it shouldn't have been.

		So we can be sure that you can complete this step properly, I'm going
		to regenerate $(path final.md) to be the same that it was when this step
		started.
		MSG

		cat "$_BASE/first.md" "$_BASE/second.md" > "$_BASE/final.md"
	fi
}

inspect_final_md2_prologue() {
	cat <<-MSG
	Use $(cmd cat) or $(cmd less) to inspect $(path final.md).
	MSG
}

inspect_final_md2_test() {
	_tutr_nonce && return $PASS

	if [[ ${_CMD[0]} == 'less' ]]; then
		_tutr_generic_test -d "$_BASE" -c "less" -a "final\\.md"
	else
		_tutr_generic_test -d "$_BASE" -c "cat" -a "final\\.md"
	fi
}

inspect_final_md2_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat final.md" "$_BASE"
			;;
	esac

	if [[ ! -f final.md ]]; then
		cat <<-MSG

		It appears you've deleted $(path final.md) before viewing it! How about you
		don't do that, m'kay?

		You'll need to regenerate the file by running:
		  $(cmd 'cat first.md second.md third.md > final.md')
		to continue.

		MSG
	fi

	_damaged_files_check
}

inspect_final_md2_epilogue() {
	cat <<-MSG
	Great work! We were able to add the output of a command to an existing
	file. We might not always use this feature, but it sure is handy when
	it is needed.

	MSG
	_tutr_pressanykey
}



inspect_nameerror_py_prologue() {
	cat <<-MSG
	Let's switch things up a little bit. We're going to try redirecting the
	output of a Python script that I have created for you momentarily.
	First, let's take a look at the contents of this Python file. Use $(cmd cat)
	or $(cmd less) to view the file $(path nameError.py).
	MSG
}

inspect_nameerror_py_test() {
	_tutr_nonce && return $PASS

	if [[ ${_CMD[0]} == less ]]; then
		_tutr_generic_test -d "$_BASE" -c less -a nameError.py
	else
		_tutr_generic_test -d "$_BASE" -c cat -a nameError.py
	fi
}

inspect_nameerror_py_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat nameError.py" "$_BASE"
			;;
	esac

	_damaged_files_check
}

run_nameerror_prologue() {
	cat <<-MSG
	Now, run this program with $(_py $_PY), but don't worry about redirection.
	Just notice what happens.
	MSG
}

run_nameerror_test() {
	USED_REDIRECTION=99

	_tutr_nonce && return $PASS

	[[ ${_CMD[*]} == $_PY*">"* ]] && return $USED_REDIRECTION

	_tutr_generic_test -d "$_BASE" -c "$_PY" -a "nameError\\.py" -f
}

run_nameerror_hint() {
	case $1 in
		$PASS)
			;;
		$USED_REDIRECTION)
			cat <<-MSG
			You're not supposed to redirect this file at this time! Try running it
			again, but without doing any redirection.
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY nameError.py" "$_BASE"
			;;
	esac

	_damaged_files_check
}

run_nameerror_epilogue() {
	_tutr_pressanykey

	cat <<-MSG

	Apparently there is a problem in this $(_py) program.  It tried to
	access a variable that doesn't exist, and crashed with a $(_STDERR NameError).

	Turns out the program's file name was pretty descriptive!
	MSG
}



redir_stdout_nameerror_prologue() {
	cat <<-MSG
	Run $(cmd $_PY nameError.py) again, but this time redirect its output to
	$(path output.txt).  If the last redirection command means anything, the
	error message should go to $(path output.txt) instead of the screen.
	MSG
}

redir_stdout_nameerror_test() {
	REDIRECTED_STDERR_TOO=99
	WRONG_CONTENTS=98

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/output.txt" ]]; then
		if  [[ $(head -n 1 "$_BASE/output.txt") == "Hello, my friend."*
		    && -z $(grep "Traceback (most recent call last):" "$_BASE/output.txt") ]]; then
			return 0
		elif [[ -n $(grep "Traceback (most recent call last):" "$_BASE/output.txt") ]]; then
			return $REDIRECTED_STDERR_TOO
		else
			return $WRONG_CONTENTS
		fi
	else
		_tutr_generic_test -d "$_BASE" -c "$_PY" -a "nameError\\.py" -a ">" -a "output\\.txt" -f
	fi
}

redir_stdout_nameerror_hint() {
	case $1 in
		$PASS)
			return
			;;
		$REDIRECTED_STDERR_TOO)
			cat <<-MSG
			Wow, you already knew that? Props! Unfortunately I'm going to need you
			to redirect the output from $(_STDOUT), not $(_STDERR), to the file. Just use
			the standard $(cmd '>') redirection.
			MSG
			;;
		$WRONG_CONTENTS)
			cat <<-MSG
			It appears that you created the file $(path output.txt), but didn't redirect
			the result of running $(cmd $_PY nameError.py) to it. Try again!
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY nameError.py > output.txt" "$_BASE"
			;;
	esac

	_damaged_files_check
}

redir_stdout_nameerror_epilogue() {
	_tutr_pressanykey

	cat <<-MSG

	WOAH. Why is there still output on  ${_Y}  ___            ___
	the terminal?                       ${_Y} / _ \\__      __/ _ \\
	                                    ${_Y}| | | \\ \\ /\\ / / | | |
	Didn't you just redirect all the    ${_Y}| |_| |\\ V  V /| |_| |
	output to a file?  What gives?      ${_Y} \\___/  \\_/\\_/  \\___/

	If you inspect $(path output.txt), you'll see that the output to the terminal,
	the $(_STDERR error message), is not included.  Just the stuff that was
	considered to be $(_STDOUT standard output).

	MSG

	_tutr_pressanykey

	cat <<-MSG

	So far you have only redirected a program's $(_STDOUT ordinary output) to a
	file.  But a program can generate more types of output than what
	counts as $(_STDOUT ordinary).

	Your operating system differentiates between $(_STDOUT ordinary) and $(_STDERR error) output.

	$(_STDOUT Ordinary output) is also called $(_STDOUT standard output), or $(_STDOUT) for short.

	The second kind of output, used for error messages, is called $(_STDERR standard)
	$(_STDERR error), abbreviated as $(_STDERR).

	Programmers can choose which of these destinations that $(_code "print()") messages
	are sent.  By default, messages sent to $(_STDOUT) and $(_STDERR) both end
	up on the screen.  However, a user who knows how redirection works can
	control whether messages appear on the screen, go to files, or are
	ignored altogether.

	MSG
	_tutr_pressanykey
}



redir_stderr_nameerror_ff() {
	runPython "$_BASE/nameError.py" 2> "$_BASE/error.txt"
	true  # needed b/c the above command is supposed to fail
}

redir_stderr_nameerror_rw() {
	command rm -f "$_BASE/error.txt"
}

redir_stderr_nameerror_prologue() {
	cat <<-MSG
	Redirection of $(_STDERR) uses a slightly different redirection operator. 
	$(cmd '2>') redirects $(bld just) $(_STDERR standard error) to a file, leaving
	$(_STDOUT) to the terminal.

	$(_STDERR) is redirected with a slightly different operator.  $(cmd '2>') redirects
	only $(_STDERR error messages) to a file, leaving the terminal for $(_STDOUT).

	Why is it $(cmd '2>')?  Because $(_STDERR) is the $(bld second) file that was automatically
	opened by your program when it was started.  $(_STDOUT) was the first.  As
	it turns out, $(cmd '1>') is equivalent to $(cmd '>'), but why type an extra number
	when you don't need to?

	Your task now is to use $(cmd '2>') to redirect $(bld just) the $(_STDERR error output) of
	$(cmd $_PY nameError.py) into $(path error.txt), leaving the program's $(_STDOUT ordinary output)
	on the screen.
	MSG
}

redir_stderr_nameerror_test() {
	REDIRECTED_STDOUT=99
	WRONG_CONTENTS=98

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/error.txt" ]]; then
		if  [[ -n $(grep "Traceback (most recent call last):" "$_BASE/error.txt")
			&& -z $(grep "Hello, my friend." "$_BASE/error.txt") ]]; then
			return 0
		elif [[ -n $(grep "Hello, my friend." "$_BASE/error.txt") ]]; then
			return $REDIRECTED_STDOUT
		else
			return $WRONG_CONTENTS
		fi
	else
		_tutr_generic_test -d "$_BASE" -c "$_PY" -a "nameError\\.py" -a "2>" -a "error\\.txt" -f
	fi
}

redir_stderr_nameerror_hint() {
	case $1 in
		$PASS)
			return
			;;
		$REDIRECTED_STDOUT)
			cat <<-MSG
			Whoops! It appears you redirected the standard output, $(_STDOUT), to the
			$(path error.txt) file.

			Remember, you want to use $(cmd '2>') to redirect $(_STDERR). Try again!
			MSG
			;;
		$WRONG_CONTENTS)
			cat <<-MSG
			It appears that you created the file $(path error.txt), but didn't redirect
			the $(_STDERR) output from running $(cmd $_PY nameError.py).

			Remember, you want to use $(cmd '2>') to redirect $(_STDERR). Try again!
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY nameError.py 2> error.txt" "$_BASE"
			;;
	esac

	_damaged_files_check
}

redir_stderr_nameerror_epilogue() {
	cat <<-MSG
	Notice that the $(_STDOUT standard output) still appears on the terminal, but the
	error message doesn't.  The shell redirected only the $(_STDERR error text) into
	$(path error.txt).  This is just the opposite of when you redirected $(_STDOUT) to a
	file and let $(_STDERR) go to the terminal.

	MSG
	_tutr_pressanykey
}



view_error_txt_prologue() {
	cat <<-:
	It can be hard to make sense of a program when its bad output is all
	mixed up with the good.  This is why $(_STDOUT) and $(_STDERR) are made to be
	separate, and can be directed to different files.  This is commonly done
	to make it easy to detect and react to problems, or to keep error
	messages in their own log file for later review.

	Now look at $(path error.txt) with $(cmd cat) to see that it caught the error message.
	:
}

view_error_txt_test() {
	_tutr_nonce && return $PASS
	if [[ ${_CMD[0]} == less ]]; then
		_tutr_generic_test -d "$_BASE" -c less -a error.txt
	else
		_tutr_generic_test -d "$_BASE" -c cat -a error.txt
	fi
}

view_error_txt_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat error.txt" "$_BASE"
			;;
	esac

	_damaged_files_check

	cat <<-:

	  $(cmd cat error.txt) to see where the error message went
	:
}

view_error_txt_epilogue() {
	_tutr_pressanykey
}



inspect_outputstreams_py_prologue() {
	cat <<-MSG
	I've mentioned that a program can control what gets printed to each of
	the output streams.  Each programming language handles this differently.
	I'll teach you how Python does it.

	First, read $(_py outputStreams.py) with $(cmd less) or $(cmd cat).
	MSG
}

inspect_outputstreams_py_test() {
	_tutr_nonce && return $PASS

	if [[ ${_CMD[0]} == less ]]; then
		_tutr_generic_test -d "$_BASE" -c less -a "outputStreams\\.py"
	else
		_tutr_generic_test -d "$_BASE" -c cat -a "outputStreams\\.py"
	fi
}

inspect_outputstreams_py_hint() {
	case $1 in
		$PASS)
			;;
		*)
			_tutr_generic_hint $1 "cat outputStreams.py" "$_BASE"
			_damaged_files_check

			cat <<-:

			Run
			  $(cmd cat outputStreams.py) to learn what this program can do.
			:
			;;
	esac
}

inspect_outputstreams_py_epilogue() {
	_tutr_pressanykey
}



edit_outputstreams_py_ff() {
	_generate_post_outputStreams
}

edit_outputstreams_py_rw() {
	OUTPUT_STREAMS_CONTENTS=
	fix-files
}

edit_outputstreams_py_prologue() {
	cat <<-MSG
	This program's code tells you that $(_py)'s $(_code "print()") function takes a
	parameter called $(_code file) which lets you chose where its output goes.  You
	will do this in an upcoming assignment when you want to write data to a
	new file.

	You have previously used $(_py "Python's") $(_code "open()") function to open existing files
	for reading.  You could instead call $(_code "open()") with a file that does not
	exist along with $(_code 'mode="w"').  This tells $(_py) to create a new, empty
	file and return a new file object.  This object can be passed to $(_code "print()"),
	sending the text into the file instead of the screen.

	MSG

	_tutr_pressanykey

	cat <<-MSG

	Every time you launch a program, two "files" are automatically opened
	for you; one that corresponds to $(_STDOUT), and one for $(_STDERR).  In
	$(_py), the variables that hold these files live in the $(_code sys) package,
	with the names $(_STDOUT sys.stdout) and $(_STDERR sys.stderr).

	As was mentioned in this program's code, $(_code "print()") sends its output to
	$(_STDOUT sys.stdout) by default.  You can make this explicit by giving
	$(_code "print()") the extra parameter $(_STDOUT file=sys.stdout).

	Likewise, when you want to write an error message on $(_STDERR), call $(_code "print()")
	with $(_STDERR file=sys.stderr).

	Now, edit $(_py outputStreams.py) to change the calls to $(_code "print()") such that their
	outputs are explicitly sent to their respective destinations.

	Use your favorite text editor to do so. $(cmd nano) would work perfectly for this
	task. If you use an external editor, you will need to run $(cmd tutor check) after
	editing and saving the file.
	MSG
	cat <<-:
	:
}

edit_outputstreams_py_test() {
	_FIX_FILES=99
	_UNCHANGED=98
	_NO_STDOUT=97
	_NO_STDERR=96
	_ERROR_IN_FILE=95

	if   [[ "$PWD" != "$_BASE" ]]; then return $WRONG_PWD
	elif _tutr_nonce; then return $PASS
	elif [[ ! -f "$_BASE/outputStreams.py" ]]; then return $_FIX_FILES
	elif [[ $(git hash-object "$_BASE/outputStreams.py") == $OUTPUT_STREAMS_HASH ]]; then return $_UNCHANGED
	fi

	if   ! grep -q -E "explicitly output to STDOUT.*, *file=sys.stdout" "$_BASE/outputStreams.py"; then
		return $_NO_STDOUT
	elif ! grep -q -E "also put output on STDERR.*, *file=sys.stderr" "$_BASE/outputStreams.py"; then
		return $_NO_STDERR
	elif ! runPython "$_BASE/outputStreams.py" &> /dev/null; then
		return $_ERROR_IN_FILE
	else
		# Set the OUTPUT_STREAMS_HASH so the students outputStreams.py file doesn't get clobbered
		OUTPUT_STREAMS_HASH=$(git hash-object "$_BASE/outputStreams.py")
		OUTPUT_STREAMS_CONTENTS=$(cat "$_BASE/outputStreams.py")
		return 0
	fi
}

edit_outputstreams_py_hint() {
	case $1 in
		$_FIX_FILES)
			cat <<-:
			Your file looks broken.
			Run $(cmd fix-files) to fix it, then try again.
			:
			;;

		$_UNCHANGED)
			cat <<-:
			You must change $(_py outputStreams.py), my friend!

			Start by adding the parameter $(_STDOUT "file=sys.stdout"), after the string
			parameter in this call to $(_code "print()"):

			  $(_code 'print("I can explicitly output to STDOUT with the file parameter.")')
			:
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_BASE"
			;;

		$_NO_STDOUT)
			cat <<-:
			Put the parameter $(_STDOUT "file=sys.stdout"), after the string parameter
			in this call to $(_code "print()"):

			  $(_code 'print("I can explicitly output to STDOUT with the file parameter.")')

			If you have mangled $(_py outputStreams.py) beyond repair, run
			$(cmd fix-files) to fix it, then try again.
			:
			;;

		$_NO_STDERR)
			cat <<-:
			Put the parameter $(_STDERR "file=sys.stderr"), after the string parameter
			in this call to $(_code "print()"):

			  $(_code 'print("I can also put output on STDERR with the file parameter.")')

			If you have mangled $(_py outputStreams.py) beyond repair, run
			$(cmd fix-files) to fix it, then try again.
			:
			;;
		$_ERROR_IN_FILE)
			cat <<-:
			Whatever you wrote in $(path outputStreams.py) has an error in it, and it's
			failing unexpectedly! Run $(cmd $_PY outputStreams.py) to see what the issue
			is, and then fix it to proceed.
			:
			;;
	esac

	_damaged_files_check during
}

redir_stdout_outputstreams_py_prologue() {
	cat <<-MSG
	Now that we've got those print statements printing to the right file
	descriptors, let's test it out!

	Run $(cmd $_PY outputStreams.py) and redirect $(_STDOUT) to the file
	$(path separate.txt). When done correctly, you should only see the message
	printing to $(_STDERR) in the terminal.
	MSG
}

redir_stdout_outputstreams_py_test() {
	STDERR_IS_PRESENT=99
	WRONG_CONTENTS=98

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/separate.txt" ]]; then
		if   grep -q -E "also put output on STDERR.*" "$_BASE/separate.txt"; then
			return $STDERR_IS_PRESENT
		elif grep -q -E "explicitly output to STDOUT.*" "$_BASE/separate.txt"; then
			return 0
		else
			return $WRONG_CONTENTS
		fi
	else
		_tutr_generic_test -c $_PY -a "outputStreams\\.py" -a ">" -a "separate.txt"
	fi
}

redir_stdout_outputstreams_py_hint() {
	case $1 in
		$PASS)
			return
			;;
		$STDERR_IS_PRESENT)
			cat <<-MSG
			Looks like you redirected the wrong output stream! You redirected
			$(_STDERR) to the file, when we only want $(_STDOUT). Use the
			$(cmd '>') redirection operator to redirect only $(_STDOUT).
			MSG
			;;
		$WRONG_CONTENTS)
			cat <<-MSG
			Looks like you created $(path separate.txt) with the wrong contents. You need to
			redirect $(_STDOUT) from running $(cmd $_PY outputStreams.py) to the file
			$(path separate.txt). Whatever you have in there now is not going to cut it.
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY" "$_BASE"
			;;
	esac

	cat <<-MSG

	Run the command $(cmd "$_PY outputStreams.py > separate.txt")
	to proceed.
	MSG

	_damaged_files_check post
}

redir_together_outputstreams_py_prologue() {
	cat <<-MSG
	How do you redirect *both* $(_STDOUT) and $(_STDERR) to the same file?
	With the $(cmd '&>') operator.  This one is easy to remember because
	it puts $(_STDOUT) $(cmd '&') $(_STDERR) together!

	Use $(cmd '&>') to redirect the output of $(cmd $_PY outputStreams.py) into
	one file called $(path together.txt).
	MSG
}

redir_together_outputstreams_py_test() {
	WRONG_CONTENTS=99
	JUST_STDOUT=98
	JUST_STDERR=97

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/together.txt" ]]; then
		grep -q "I can explicitly output to STDOUT with the file parameter." "$_BASE/together.txt"
		local SO=$?

		grep -q "I can also put output on STDERR with the file parameter." "$_BASE/together.txt"
		local SE=$?

		if (( SO + SE == 0 )); then
			return 0
		elif (( SO == 0 )) ; then
			return $JUST_STDOUT
		elif (( SE == 0 )); then
			return $JUST_STDERR
		else
			return $WRONG_CONTENTS
		fi
	else
		_tutr_generic_test -d "$_BASE" -c "$_PY" -a "outputStreams\\.py" -a "&>" -a "together\\.txt"
	fi
}

redir_together_outputstreams_py_hint() {
	case $1 in
		$PASS)
			;;
		$WRONG_CONTENTS)
			cat <<-MSG
			It appears that you have created the file $(path together.txt) with the wrong
			contents. You want both $(_STDOUT) $(cmd '&') $(_STDERR) output from running the
			Python program in $(path outputStreams.py).

			Remember to use the $(cmd '&>') redirection operator to redirect both $(_STDOUT)
			and $(_STDERR) to the file $(path together.txt).
			MSG
			;;
		$JUST_STDOUT)
			cat <<-MSG
			It appears that you have created the file $(path together.txt) with *only*
			the contents of $(_STDOUT). Try again!

			Remember to use the $(cmd '&>') redirection operator to redirect both $(_STDOUT)
			$(cmd '&') $(_STDERR) to the file $(path together.txt).
			MSG
			;;
		$JUST_STDERR)
			cat <<-MSG
			It appears that you have created the file $(path together.txt) with *only*
			the contents of $(_STDERR). Try again!

			Remember to use the $(cmd '&>') redirection operator to redirect both $(_STDOUT)
			$(cmd '&') $(_STDERR) to the file $(path together.txt).
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY outputStreams.py &> together.txt" "$_BASE"
			;;
	esac

	_damaged_files_check post
}

redir_together_outputstreams_py_epilogue() {
	cat <<-MSG
	Great work!  You can inspect $(path together.txt) to verify that you
	successfully redirected $(bld '*both*') $(_STDOUT) $(cmd '&') $(_STDERR) to the same file.

	MSG
	_tutr_pressanykey
}



redir_separate_outputstreams_py_prologue() {
	cat <<-MSG
	What if you want to redirect $(_STDOUT) and $(_STDERR) to $(bld different) places
	at once?  Simple!  Just use both $(cmd '>') and $(cmd '2>') in the same command!

	Example:
	  $(cmd 'command > STDOUT_FILE.txt 2> STDERR_FILE.txt')

	While I'm at it, let me teach you about a $(bld very special) file that behaves
	like a black hole on your computer.  This file is called $(path /dev/null). 

	For example, you could $(bld completely ignore everything) a command prints by
	redirecting both $(_STDOUT) and $(_STDERR) to $(path /dev/null), like this:
	  $(cmd "$_PY outputStreams.py &> /dev/null")

	I want you to try a version of this now.  Run $(cmd $_PY outputStreams.py)
	but send $(_STDOUT) to $(path /dev/null) and $(_STDERR) to $(path error2.txt).
	MSG
}

redir_separate_outputstreams_py_test() {
	WRONG_CONTENTS=99
	STDOUT_IS_PRESENT=98
	NOTHING_TO_DEV_NULL=97

	_tutr_nonce && return $PASS

	if [[ -f "$_BASE/error2.txt" ]]; then

		[[ ${_CMD[*]} != *"/dev/null"* ]] && return $NOTHING_TO_DEV_NULL

		STDOUT_CONTENTS=$(grep "My output goes to STDOUT by default." "$_BASE/error2.txt")
		STDERR_CONTENTS=$(grep "I can also put output on STDERR with the file parameter." "$_BASE/error2.txt")
		if [[ -z $STDOUT_CONTENTS && -n $STDERR_CONTENTS ]]; then
			return 0
		elif [[ -n $STDOUT_CONTENTS ]]; then
			return $STDOUT_IS_PRESENT
		else
			return $WRONG_CONTENTS
		fi
	else
		_tutr_generic_test -d "$_BASE" -c "$_PY" -a "outputStreams\\.py" -a "2>" -a "error2.txt" -a ">" -a "/dev/null"
	fi
}

redir_separate_outputstreams_py_hint() {
	case $1 in
		$PASS)
			;;
		$WRONG_CONTENTS)
			cat <<-MSG
			It appears that you have the wrong contents in the file $(path error2.txt)!
			You want to run the command $(cmd $_PY outputStreams.py) and send $(_STDERR) to
			the file $(path error2.txt) and $(_STDOUT) to $(path /dev/null) to ignore the standard
			output for our Python program.

			Remember, $(cmd '>') redirects $(_STDOUT) and $(cmd '2>') redirects $(_STDERR). They can be
			redirected to different places on the same command.

			Example:
			  $(cmd 'command > STDOUT_FILE.txt 2> STDERR_FILE.txt')
			MSG
			;;
		$STDOUT_IS_PRESENT)
			cat <<-MSG
			It appears that you sent $(_STDOUT) to the file $(path error2.txt)! You want to
			send $(_STDERR) to this file instead and $(_STDOUT) to $(path /dev/null) to get rid of
			the standard output for our Python program.

			Remember, $(cmd '>') redirects $(_STDOUT) and $(cmd '2>') redirects $(_STDERR). They can be
			redirected to different places on the same command.

			Example:
			  $(cmd 'command > STDOUT_FILE.txt 2> STDERR_FILE.txt')
			MSG
			;;
		$NOTHING_TO_DEV_NULL)
			cat <<-MSG
			It appears you didn't send any output to the file $(path /dev/null)! Try
			again. Remember, $(path /dev/null) is just like any other file you can redirect
			to by just specifying the file path $(path /dev/null). It will allow you to get
			rid of any output you don't particularly care about.
			MSG
			;;
		*)
			_tutr_generic_hint $1 "$_PY outputStreams.py 2> error2.txt > /dev/null"
			;;
	esac

	_damaged_files_check post
}



inspect_error2_file_prologue() {
	cat <<-MSG
	Great work!

	You are basically done with this lesson.

	Before you leave, you can take one last look at the files you created
	with $(cmd cat) or $(cmd less).  Once the lesson ends, those files will
	be deleted.
	
	The lesson will conclude when you view the last file you made,
	$(path error2.txt).
	MSG
}

inspect_error2_file_test() {
	_tutr_nonce && return $PASS

	if [[ ${_CMD[0]} == "less" ]]; then
		_tutr_generic_test -d "$_BASE" -c "less" -a "error2\\.txt"
	else
		_tutr_generic_test -d "$_BASE" -c "cat" -a "error2\\.txt"
	fi
}

inspect_error2_file_hint() {
	case $1 in
		$PASS)
			;;
		*)
			cat <<-MSG
			To finish lesson, view $(path error2.txt) with $(cmd less) or $(cmd cat).
			MSG
			;;
	esac

	_damaged_files_check post

	# If the student really messes up by deleting the file, let's just make
	#	an empty 'error2.txt' file for them to open.
	if [[ ! -f "$_BASE/error2.txt" ]]; then
		cat <<-MSG

		Well, it appears you accidentally deleted the file $(path error2.txt). Good
		job...?  I'm going to recreate it for you so you can successfully
		finish the lesson.
		MSG

		echo "It's only a mistake if you don't learn from it" > "$_BASE/error2.txt"
	fi
}

inspect_error2_file_epilogue() {
	_tutr_pressanykey
}



cleanup() {
	# Remember that this lesson has been completed
	(( $# >= 1 && $1 == $_COMPLETE)) && _tutr_record_completion ${_TUTR#./}
	[[ -d "$_BASE" ]] && rm -rf "$_BASE"
	echo "You worked on the Shell Redirection lesson for $(_tutr_pretty_time)"
}


epilogue() {
	cat <<-'EPILOGUE'
	  _____                        __       __     __  _
	 / ___/__  ___  ___ ________ _/ /___ __/ /__ _/ /_(_)__  ___  ___
	/ /__/ _ \/ _ \/ _ `/ __/ _ `/ __/ // / / _ `/ __/ / _ \/ _ \(_-<
	\___/\___/_//_/\_, /_/  \_,_/\__/\_,_/_/\_,_/\__/_/\___/_//_/___/
	              /___/

	You know the basics of shell redirection!  Now you can control where
	the output of a given shell command ends up, taking your shell-foo to
	the next level.

	EPILOGUE

	_tutr_pressanykey

	cat <<-EPILOGUE
	In summary:
	* $(cmd '>')
	    * Redirect only standard output to a file
	* $(cmd '>>')
	    * Redirect only standard output to a file, appending to existing file
	* $(cmd '2>')
	    * Redirect only standard error to a file
	* $(cmd '&>')
	    * Redirect standard output and standard error to a file
	* $(path /dev/null)
	    * A special file that acts as a $(bld 'black hole'), swallowing up all
	        information given to it

	Run $(cmd ${SHELL##*/} make-certificate.sh) to generate your certificate of completion.

	EPILOGUE

	_tutr_pressanykey
}



source main.sh && _tutr_begin \
	cat_to_terminal \
	cat_to_final_md \
	inspect_final_md1 \
	append_to_final_md \
	inspect_final_md2 \
	inspect_nameerror_py \
	run_nameerror \
	redir_stdout_nameerror \
	redir_stderr_nameerror \
	view_error_txt \
	inspect_outputstreams_py \
	edit_outputstreams_py \
	redir_stdout_outputstreams_py \
	redir_together_outputstreams_py \
	redir_separate_outputstreams_py \
	inspect_error2_file


# vim: set filetype=sh noexpandtab tabstop=4 shiftwidth=4 textwidth=76 colorcolumn=76:
