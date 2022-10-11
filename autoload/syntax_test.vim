""
" Set b:syntax_test_syntax and b:syntax_test_comment,
" because |rainbow_csv| detects |b:current_syntax|, so use a new variable.
"
" If filetype detect fails,
" (e.g., |rainbow_csv| uses |autocmd| |Syntax| to change filetype)
" you can assign it manually. >
"     call syntax_test#init('csv')
" <
function! syntax_test#init(...) abort
  if a:0 == 1
    let b:syntax_test_syntax = a:1
  else
    filetype detect
    ""
    " |b:current_syntax| may not exist.
    " 'syntax' may be incorrect "ON" when modeline change filetype.
    " So we use 'filetype'.
    call g:sublime_syntax#utils#plugin.Flag('b:syntax_test_syntax',
          \ empty(&filetype) ? expand('%:e') : &filetype
          \ )
  endif

  " https://github.com/google/vimdoc/issues/122
  ""
  " Use the first word of the first line to be default comment symbol.
  " If the first line is blank, use 'commentstring'.
  "
  " http://www.sublimetext.com/docs/syntax.html#testing
  call g:sublime_syntax#utils#plugin.Flag('b:syntax_test_comment',
        \ get(split(getline(1)), 0, '')
        \ )
  if empty(b:syntax_test_comment)
    let b:syntax_test_comment = get(split(&commentstring, '\s*%s'), 0, '#')
  endif
  set filetype=syntax_test
endfunction

""
" if b:syntax_test_syntax or b:syntax_test_comment doesn't exist,
" call |syntax_test#init()|. if they exist, do nothing.
function! syntax_test#detect() abort
  if !exists('b:syntax_test_syntax') || !exists('b:syntax_test_comment')
    call syntax_test#init()
  endif
endfunction
