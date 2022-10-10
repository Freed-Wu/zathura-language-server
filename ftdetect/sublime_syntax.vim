augroup sublime_syntax
  autocmd!
  autocmd BufNewFile,BufRead syntax_test_* call syntax_test#init()
  autocmd BufNewFile,BufRead *.sublime-syntax setfiletype sublime_syntax
augroup END
