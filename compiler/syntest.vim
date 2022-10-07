" override original compiler
let b:current_compiler = 'syntest'

let s:save_cpoptions = &cpoptions
set cpoptions&vim

if exists(':CompilerSet') != 2
  command -nargs=* CompilerSet setlocal <args>
endif
CompilerSet makeprg=syntest\ %:S\ .
CompilerSet errorformat=%E\ \ Assertion\ selector\ \"%o\"\ from\ line\ %l\ failed\ against\ line\ %*\\d\\,\ column\ range\ %*\\d-%*\\d\ (with\ text\ \"%.%#\")\ has\ scope\ [%m],
      \%Z,
      \%-G%.%#

let &cpoptions = s:save_cpoptions
unlet s:save_cpoptions
