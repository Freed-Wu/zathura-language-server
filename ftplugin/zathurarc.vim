if exists('b:did_ftplugin')
  finish
endif
let b:did_ftplugin = 1

let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin = 'setlocal comments< commentstring< include< islocked<'
setlocal comments=:#
setlocal commentstring=#\ %s
setlocal include=^\sinclude
setlocal iskeyword+=-

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
