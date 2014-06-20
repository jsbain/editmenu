s# coding: utf-8


def buttonhandle(sender):
	print sender.name
	exec(sender.name+'()')

def showsidebar():
	import ui
	v=ui.load_view('editmenu')
	v.present('sidebar')

def indent():
	#   """indent selected lines
	import editor
	import re
	INDENTSTR='\t' #two spaces
	i=editor.get_line_selection()
	t=editor.get_text()
	# replace every occurance of newline with  ewline plus indent, except last newline
	editor.replace_text(i[0],i[1]-1,INDENTSTR+re.sub(r'\n',r'\n'+INDENTSTR,t[i[0]:i[1]-1]))

	editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))

def unindent():
	# """indent selected lines
	import editor
	import textwrap

	i=editor.get_line_selection()
	t=editor.get_text()

	editor.replace_text(i[0],i[1], textwrap.dedent(t[i[0]:i[1]]))

	editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))


def execlines():
	## executes selected lines in console
	import editor
	import textwrap

	a=editor.get_text()[editor.get_line_selection()[0]:editor.get_line_selection()[1]]

	exec(textwrap.dedent(a))


showsidebar()
