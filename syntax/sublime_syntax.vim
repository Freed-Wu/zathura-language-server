if exists('b:current_syntax')
  finish
endif
let b:current_syntax = 'sublime_syntax'

set syntax=yaml

execute 'syntax keyword sublimeSyntaxKeyword' join(g:sublime_syntax#syntax_names, ' ')
execute 'syntax match sublimeSyntaxConstant `\v%(%(%(meta_)?scope|\d):\s*)@<=%(' . join(g:sublime_syntax#scope_names, '|') . ')>`'
syntax match sublimeSyntaxVariable `\v\{\{[a-z_]+\}\}` contained
" monkey patch
" make '- match' can be highlighted
syn match yamlBlockCollectionItemStart '^\s*\zs-\%(\s\+-\)*\ze\s' nextgroup=yamlBlockMappingKey,yamlBlockMappingMerge
" don't support yamlPlainScalar
syn region yamlFlowString matchgroup=yamlFlowStringDelimiter start='"' skip='\\"' end='"'
                  \ contains=yamlEscape,sublimeSyntaxVariable
                  \ nextgroup=yamlKeyValueDelimiter
syn region yamlFlowString matchgroup=yamlFlowStringDelimiter start="'" skip="''"  end="'"
                  \ contains=yamlSingleEscape,sublimeSyntaxVariable
                  \ nextgroup=yamlKeyValueDelimiter

highlight default link sublimeSyntaxKeyword Keyword
highlight default link sublimeSyntaxConstant Constant
highlight default link sublimeSyntaxVariable Macro
