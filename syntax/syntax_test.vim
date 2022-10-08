if exists('b:current_syntax') && b:current_syntax =~# 'syntax_test'
  finish
endif
if exists('b:current_syntax')
  let b:current_syntax = b:current_syntax . '.syntax_test'
else
  let b:current_syntax = 'syntax_test'
endif

syntax case match

execute 'syntax match syntaxTestComment !\v^\s*\V' . b:comment . '\v.*$! contains=syntaxTestInclude,syntaxTestIncluded,syntaxTestCaretOrArrow,syntaxTestScope,syntaxTestNotScope'
execute 'syntax match syntaxTestInclude !\v%(^\s*\V' . b:comment . '\v\s+)@<=SYNTAX TEST(\s+)@=! contained'
execute 'syntax match syntaxTestIncluded !\v%(^\s*\V' . b:comment . '\v\s+SYNTAX TEST\s+)@<="[^"]+"! contained'
execute 'syntax match syntaxTestCaretOrArrow !\v%(^\s*\V' . b:comment . '\v\s*)@<=%(\<-|\^+)! contained'
execute 'syntax match syntaxTestScope !\v%(^\s*\V' . b:comment . '\v\s*%(\<-|\^+)\s*%(-|[a-z][a-z.\-_+]*\s+)*)@<=[a-z][a-z.\-_+]*! contained'
execute 'syntax match syntaxTestNotScope !\v%(^\s*\V' . b:comment . '\v\s*%(\<-|\^+)\s*%(-|[a-z][a-z.\-_+]*\s+)*)@<=-\s*[a-z][a-z.\-_+]*! contained'

highlight default link syntaxTestComment Comment
highlight default link syntaxTestInclude Include
highlight default link syntaxTestIncluded String
highlight default link syntaxTestCaretOrArrow Todo
highlight default link syntaxTestScope DiffAdd
highlight default link syntaxTestNotScope DiffDelete
