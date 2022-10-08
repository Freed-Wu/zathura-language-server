""
" True initialization.
" You can call this function when the filetype detect failed.
" Set `b:comment` and 'commentstring'.
" Set |:syntax| and |:highlight|.
function! syntax_test#main#init() abort
  let b:syntax_test_subtype = &filetype
  let &filetype = 'syntax-test.' . &filetype
  " must after set filetype
  runtime ftplugin/syntax_test.vim
  runtime syntax/syntax_test.vim
endfunction
