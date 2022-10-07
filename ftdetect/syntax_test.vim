augroup syntax_test
  autocmd!
  autocmd BufNewFile,BufRead syntax_test_* call syntax_test#init()
augroup END
