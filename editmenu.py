# coding: utf-8
import editor

def buttonhandle(sender):
	"""handler for generic button tap.
		calls function that matches button name
	"""
	#print sender.name
	exec(sender.name+'()')

def showsidebar():
	"""show the sidebar. """
	import ui
	v=ui.load_view('editmenu')
	v.present('sidebar')

def indent():
	"""indent selected lines by one tab"""
	import editor
	import re
	INDENTSTR='\t' #two spaces
	i=editor.get_line_selection()
	t=editor.get_text()
	# replace every occurance of newline with  ewline plus indent, except last newline
	editor.replace_text(i[0],i[1]-1,INDENTSTR+re.sub(r'\n',r'\n'+INDENTSTR,t[i[0]:i[1]-1]))

	editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))

def unindent():
	"""unindent selected lines all the way"""
	import editor
	import textwrap

	i=editor.get_line_selection()
	t=editor.get_text()

	editor.replace_text(i[0],i[1], textwrap.dedent(t[i[0]:i[1]]))

	editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))


def execlines():
	"""execute selected lines in console.	""" 
	import editor
	import textwrap

	a=editor.get_text()[editor.get_line_selection()[0]:editor.get_line_selection()[1]]

	exec(textwrap.dedent(a))

def selectstart():
	import editor
	i=editor.get_selection()
	editor.set_selection(i[0],i[1]+1)

def finddocstring():
	''' find the docstring at current cursor location
	'''
	import StringIO
	from jedi import Script
	
	i=editor.get_selection()
	t=editor.get_text()
	(line,txt)=[(line,n) for (line,n) in enumerate(StringIO.StringIO(editor.get_text()[:i[1]]))][-1]
	script = Script(t, line+1, len(txt))

	dfn = script.goto_definitions()
	if dfn:
		doc=dfn[0].doc
		import ui
		v=ui.TextView()
		v.width=100
		v.height=50
		v.text=doc
		editor._set_toolbar(v)
	
def copy():
	import clipboard
	i=editor.get_selection()
	t=editor.get_text()
	clipboard.set(t[i[0]:i[1]])

def paste():
	import clipboard
	i=editor.get_selection()
	t=editor.get_text()
	editor.replace_text(i[0],i[1], clipboard.get())
	editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))
	
	
showsidebar()
