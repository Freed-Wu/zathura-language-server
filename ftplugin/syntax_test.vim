let s:save_cpoptions = &cpoptions
set cpoptions&vim

let b:undo_ftplugin = "setl commentstring<"

let b:comment = get(split(getline(1), ' '), 0, '#')
let &commentstring = b:comment . '%s'
compiler syntest

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
