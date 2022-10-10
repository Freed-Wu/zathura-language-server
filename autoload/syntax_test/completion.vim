function! s:Flag(name, default) abort
  let l:scope = get(split(a:name, ':'), 0, 'g:')
  let l:name = get(split(a:name, ':'), -1)
  let g:{name} = get({l:scope}:, l:name, a:default)
endfunction

""
" Update cache.
function! syntax_test#completion#update_cache() abort
  let l:cmd = 'python sys.argv = ' . string(['-c', s:cache])
  execute l:cmd
  silent execute 'pyfile' s:pyfile
endfunction

let s:path = fnamemodify(resolve(expand('<sfile>:p')), ':h:h:h')
let s:pyfile = s:path . '/rplugin/python3/syntax_test/__main__.py'
if exists('*stdpath')
  let s:cache_dir_home = stdpath('cache')
else
  let s:cache_dir_home = $HOME . '/.cache/nvim'
endif
let s:cache_dir = s:cache_dir_home . '/syntax-test.vim'
call mkdir(s:cache_dir, 'p')
let s:cache = s:cache_dir . '/syntax.json'
try
  let s:items = json_decode(readfile(s:cache)[0])
catch /\v^Vim%(\(\a+\))?:E(684|484|491):/
  call syntax_test#completion#update_cache()
  let s:items = json_decode(readfile(s:cache)[0])
endtry

let s:plugin = {'Flag': funcref('s:Flag')}
""
" Completion cache path.
call s:plugin.Flag('g:syntax_test#completion#cache', s:cache)
""
" Completion cache contents.
"
" www.sublimetext.com/docs/scope_naming.html
call s:plugin.Flag('g:syntax_test#completion#items', s:items)
