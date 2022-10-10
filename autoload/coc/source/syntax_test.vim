""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
function! coc#source#syntax_test#init() abort
  return {
        \ 'shortcut': 'syntax',
        \ 'priority': 9,
        \ 'filetypes': ['syntax_test', 'yaml'],
        \ }
endfunction

""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" only complete when the line is appropriate
function! coc#source#syntax_test#complete(opt, cb) abort
  if a:opt.filetype ==# 'syntax_test'
        \ && a:opt.line !~# '\v^\s*\V' . b:syntax_test_comment . '\v\s*(\^+|\<-)'
    return
  endif
  if a:opt.filetype ==# 'yaml'
        \ && a:opt.line !~# '\v^ *-? (meta_)?scope: '
    return
  endif
  " lazy load
  call a:cb(g:syntax_test#completion#items)
endfunction
