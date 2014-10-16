# coding: utf-8
import editor
from math import pi

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
    uncom = v['uncomment']
    uncom.transform = ui.Transform.rotation(pi)
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

def comment():
    """" comment out selected lines"""
    import editor
    import re
    COMMENT='#'
    i=editor.get_line_selection()
    t=editor.get_text()
    # replace every occurance of newline with  ewline plus COMMENT, except last newline
    editor.replace_text(i[0],i[1]-1,COMMENT+re.sub(r'\n',r'\n'+COMMENT,t[i[0]:i[1]-1]))

    editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))

def uncomment():
    """" uncomment selected lines"""
    import editor
    import re
    COMMENT='#'
    i=editor.get_line_selection()
    t=editor.get_text()
# replace every occurance of newline # with newline, except last newline
#  todo.. probably should verify every line has comment...
#  num lines= re.findall

    if all( [x.startswith('#') for x in t[i[0]:i[1]-1].split(r'\n')]):
        editor.replace_text(i[0],i[1]-1,re.sub(r'^'+COMMENT,r'',t[i[0]:i[1]-1],flags=re.MULTILINE))

    editor.set_selection(i[0],i[1]-len(t)+len(editor.get_text()))

def execlines():
    """execute selected lines in console.   """
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
    
def tabs():
    import webbrowser
    webbrowser.open('pythonista://site-packages%2Feditmenu%2Tabs.py?action=run')
    
def find_and_replace():
    import webbrowser
    webbrowser.open('pythonista://site-packages%2Feditmenu%2FFind_and_replace.py?action=run')

showsidebar()
