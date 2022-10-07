function! syntax_test#init() abort
  if split(&filetype, '\.')[0] ==# 'syntax-test'
    return
  endif
  if &filetype ==# ''
    filetype detect
    if &filetype ==# ''
      return
    endif
  endif
  " lazy load
  call syntax_test#main#init()
endfunction
