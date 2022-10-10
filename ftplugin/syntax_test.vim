let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin =
      \ "setl commentstring< modeline< conceallevel< modifiable< readonly< buftype< tabstop< shiftwidth<"

call syntax_test#detect()
let &commentstring = b:syntax_test_comment . '%s'
setlocal nomodeline
" some filetypes are nomodifiable by their ftplugin
setlocal modifiable
setlocal noreadonly
setlocal buftype=
" avoid judging wrong column
setlocal conceallevel=0
" syntest treats tab as one space
setlocal tabstop=1
setlocal shiftwidth=1

compiler syntest

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
