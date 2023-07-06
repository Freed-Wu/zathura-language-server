let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin =
      \ 'setl commentstring< modeline< conceallevel< modifiable< readonly<'
      \ . ' buftype< iskeyword< tabstop< shiftwidth< expandtab< formatoptions<'

if !exists('b:current_syntax') || !exists('b:syntax_test_comment')
  call syntax_test#init()
endif
let &commentstring = b:syntax_test_comment . '%s'
setlocal nomodeline
" some filetypes are nomodifiable by their ftplugin
setlocal modifiable
setlocal noreadonly
setlocal buftype=
" avoid judging wrong column
setlocal conceallevel=0
" sublime-syntax's scope use [0-9a-z-] as name and '.' as separator
setlocal iskeyword=48-57,a-z,-,A-Z,_
" syntest treats tab as one space
setlocal tabstop=1
setlocal shiftwidth=1
setlocal expandtab
setlocal formatoptions+=cro

compiler syntest

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
