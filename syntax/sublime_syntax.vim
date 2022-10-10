if exists('b:current_syntax')
  finish
endif
let b:current_syntax = 'sublime_syntax'

set syntax=yaml

" don't support yamlPlainScalar
syn region yamlFlowString matchgroup=yamlFlowStringDelimiter start='"' skip='\\"' end='"'
                  \ contains=yamlEscape,sublimeSyntaxVariable
                  \ nextgroup=yamlKeyValueDelimiter
syn region yamlFlowString matchgroup=yamlFlowStringDelimiter start="'" skip="''"  end="'"
                  \ contains=yamlSingleEscape,sublimeSyntaxVariable
                  \ nextgroup=yamlKeyValueDelimiter
syntax match sublimeSyntaxVariable `\v\{\{[a-z_]+\}\}` contained

highlight default link sublimeSyntaxVariable Macro
