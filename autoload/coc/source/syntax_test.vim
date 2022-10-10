""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" Press |^|, |-| and <Space> to trigger completion in the correct lines.
function! coc#source#syntax_test#init() abort
  return {
        \ 'shortcut': 'synTest',
        \ 'priority': 9,
        \ 'filetypes': ['syntax_test'],
        \ 'triggerCharacters': ['^', '-', ' '],
        \ }
endfunction

""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" only complete when the line is appropriate
function! coc#source#syntax_test#complete(opt, cb) abort
  let l:match = '\v^\s*\V' . b:syntax_test_comment . '\v\s*(\^+|\<-)'
  " 0 (found) or -1 (not found)
  if match(getline('.'), l:match)
    return
  endif
  " lazy load
  call a:cb(g:syntax_test#completion#items)
endfunction
