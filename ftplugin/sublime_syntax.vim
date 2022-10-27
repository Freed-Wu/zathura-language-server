if exists('b:did_ftplugin')
  finish
endif
runtime ftplugin/yaml.vim
let b:did_ftplugin = 1

let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin = get(b:, 'undo_ftplugin', '') . 'iskeyword<'
setlocal iskeyword+=-
compiler bat

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
