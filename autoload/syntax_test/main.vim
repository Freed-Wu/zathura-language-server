function! syntax_test#main#init() abort
  let b:syntax_test_subtype = &filetype
  let &filetype = 'syntax-test.' . &filetype
  " must after set filetype
  let b:comment = split(getline(1), ' ')[0]
  let &commentstring = b:comment . '%s'
  compiler syntest

  execute 'syntax region syntaxTestTitle start=''\m\%^\s*\V' . b:comment . '\v\s+SYNTAX TEST '' end=''\v$'' contains=syntaxTestStyle'
  syntax match syntaxTestStyle '\v"\w+.sublime-syntax"' contained
  execute 'syntax region syntaxTestCaret start=''\v^\s*\V' . b:comment . '\v\s*\^+\s*'' end=''\v$'' contains=syntaxTestScope,syntaxTestNotScope'
  syntax match syntaxTestScope '\v[a-z\._]+' contained
  execute 'syntax match syntaxTestNotScope ''\v(^\s*\V' . b:comment . '\v\s*\^+\s*[a-z\._]+\s+)@<=.*'' contained'

  highlight default link syntaxTestTitle Title
  highlight default link syntaxTestStyle String
  highlight default link syntaxTestCaret Special
  highlight default link syntaxTestScope Keyword
  highlight default link syntaxTestNotScope Error
endfunction
