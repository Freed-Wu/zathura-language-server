let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h:h:h:h')
" vim script don't have any library to handle yaml
let s:pyfile = s:path . '/rplugin/python3/syntax-test/yaml2json.py'
if exists('*stdpath')
  let s:cache_dir_home = stdpath('cache')
else
  let s:cache_dir_home = $HOME . '/.cache/nvim'
endif
let s:cache_dir = s:cache_dir_home . '/syntax-test.vim'
call mkdir(s:cache_dir, 'p')

""
" Get cache directory. Caches are json files.
function! coc#source#syntax_test#get_cache_dir() abort
  return s:cache_dir
endfunction

""
" Get "*.sublime-syntax" path.
function! coc#source#syntax_test#get_syntax_file() abort
  let l:file = findfile(get(split(getline(1), '"'), 1, ''))
  if empty(l:file)
    return ''
  endif
  let l:file = fnamemodify(l:file, ':p')
  return l:file
endfunction

""
" Get cache path.
function! coc#source#syntax_test#get_cache_file(...) abort
  if a:0 == 0
    let l:file = coc#source#syntax_test#get_syntax_file()
  else
    let l:file = a:1
  endif
  if empty(l:file)
    return ''
  endif
  return s:cache_dir . '/' . fnamemodify(l:file, ':t:r') . '.json'
endfunction

""
" Update cache.
" By default, when cache's modification time is older than "*.sublime-syntax"
" or cache does not exist, updating will be done automatically.
function! coc#source#syntax_test#update_cache(...) abort
  if a:0 == 2
    let l:file = a:1
    let l:cache = a:2
  else
    let l:file = coc#source#syntax_test#get_syntax_file()
    let l:cache = coc#source#syntax_test#get_cache_file(l:file)
  endif
  let l:cmd = 'python sys.argv = ' . string([l:file, l:cache])
  execute l:cmd
  silent execute 'pyfile' s:pyfile
endfunction

""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" Press |^|, |-| and <Space> to trigger completion in the correct lines.
function! coc#source#syntax_test#init() abort
  return {
        \ 'shortcut': 'synTest',
        \ 'priority': 9,
        \ 'filetypes': ['syntax-test'],
        \ 'triggerCharacters': ['^', '-', ' '],
        \ }
endfunction

""
" https://github.com/neoclide/coc.nvim/wiki/Create-custom-source
"
" NOTE: Don't check "SYNTAX CHECK" in the first line.
function! coc#source#syntax_test#complete(opt, cb) abort
  " 0 (found) or -1 (not found)
  if match(getline('.'), '\v^\s*\V' . b:syntax_test_comment . '\v\s*(\^+|\<-)')
    return
  endif
  let l:file = coc#source#syntax_test#get_syntax_file()
  if empty(l:file)
    return
  endif
  let l:cache = coc#source#syntax_test#get_cache_file(l:file)
  if getftime(l:cache) < getftime(l:file)
    call coc#source#syntax_test#update_cache(l:file, l:cache)
  endif
  let l:items = json_decode(readfile(l:cache)[0])
  call a:cb(l:items)
endfunction
