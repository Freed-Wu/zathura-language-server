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
" Only complete when the line is appropriate.
function! coc#source#sublime_syntax#complete(opt, cb) abort
  let g:opt = a:opt
  let l:items = []
  if a:opt.filetype ==# 'syntax_test'
        \ && a:opt.line =~# '\v^\s*\V' . b:syntax_test_comment . '\v\s*%(\^+|\<-)'
    let l:items += g:sublime_syntax#scope_items
  endif
  if a:opt.filetype ==# 'yaml'
    let l:items += g:sublime_syntax#syntax_items
    if a:opt.line =~# '\v^ *-? %(%(meta_)?scope|\d): '
      let l:items += g:sublime_syntax#scope_items
    endif
  endif
  " lazy load
  call a:cb(l:items)
endfunction
