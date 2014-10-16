# coding: utf-8

import ui
import editor

class FindField(object):
    def textfield_did_change(self, textfield):
        global find_text
        full_text = editor.get_text()
        find_text = textfield.text
        global count
        count = full_text.count(find_text)
        select_text()
        
class ReplaceField(object):
    def textfield_did_change(self, textfield):
        global replacement
        replacement = textfield.text

find_text = ''
once_or_all = 'once'
count = 0
replacement = ''

def seg(sender):
    global once_or_all
    once_or_all = sender.segments[sender.selected_index]
    #print once_or_all
    
def select_text():
    full_text = editor.get_text()
    marker = full_text.find(find_text)
    editor.set_selection(marker, marker + len(find_text))
    
def select_next(sender):
    full_text = editor.get_text()
    marker = editor.get_selection()[1]
    start = full_text.find(find_text, marker)
    editor.set_selection(start, start + len(find_text))
    
def select_previous(sender):
    full_text = editor.get_text()
    marker = editor.get_selection()[0]
    start = full_text.rfind(find_text, 0, marker)
    editor.set_selection(start, start + len(find_text))

def replace_it(sender):
    global once_or_all, find_text, replacement
    #global find_text
    #global replacement
    if once_or_all == 'once': # Replace selected instance
        selection = editor.get_selection()
        editor.replace_text(selection[0], selection[1], replacement)
    else: # Replace all instances
        full_text = editor.get_text()
        full_replacement = full_text.replace(find_text, replacement)
        editor.replace_text(0, len(full_text), full_replacement)

v = ui.load_view('Find_and_replace')

find = v['find']
find.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
find.delegate = FindField()

replace = v['replace']
replace.autocapitalization_type = ui.AUTOCAPITALIZE_NONE
replace.delegate = ReplaceField()

back = v['back']

forward = v['forward']

once_and_for_all = v['once_and_for_all']
once_and_for_all.action = seg

replace_button = v['replace_button']

editor._set_toolbar(v)
