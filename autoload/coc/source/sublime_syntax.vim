""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
function! coc#source#sublime_syntax#init() abort
  return {
        \ 'shortcut': 'sublime',
        \ 'priority': 9,
        \ 'filetypes': ['syntax_test', 'yaml'],
        \ }
endfunction

""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" Only complete when the line is appropriate.
function! coc#source#sublime_syntax#complete(opt, cb) abort
  let g:opt = a:opt
  if a:opt.filetype ==# 'syntax_test'
        \ && a:opt.line !~# '\v^\s*\V' . b:syntax_test_comment . '\v\s*(\^+|\<-)'
    return
  endif
  if a:opt.filetype ==# 'yaml'
        \ && a:opt.line !~# '\v^ *-? (meta_)?scope: '
    return
  endif
  " lazy load
  call a:cb(g:sublime_syntax#items)
endfunction
