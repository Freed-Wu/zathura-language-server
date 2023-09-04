if exists('b:current_syntax')
  finish
endif
let b:current_syntax = 'zathurarc'

syntax case match

syntax match zathurarcNumber `\<[0-9.]\>`
syntax region zathurarcString start=`"` skip=`\\"` end=`"`
syntax keyword zathurarcBoolean true false
" updated by scripts/update-vim-plugin.vim
syntax keyword zathurarcCommand include map set unmap
syntax keyword zathurarcOption abort-clear-search adjust-open advance-pages-per-row completion-bg completion-fg completion-group-bg completion-group-fg completion-highlight-bg completion-highlight-fg continuous-hist-save database dbus-raise-window dbus-service default-bg default-fg exec-command filemonitor first-page-column font guioptions highlight-active-color highlight-color highlight-fg highlight-transparency incremental-search index-active-bg index-active-fg index-bg index-fg inputbar-bg inputbar-fg link-hadjust link-zoom n-completion-items notification-bg notification-error-bg notification-error-fg notification-fg notification-warning-bg notification-warning-fg page-cache-size page-padding page-right-to-left page-thumbnail-size pages-per-row recolor recolor-darkcolor recolor-keephue recolor-lightcolor recolor-reverse-video render-loading render-loading-bg render-loading-fg sandbox scroll-full-overlap scroll-hstep scroll-page-aware scroll-step scroll-wrap search-hadjust selection-clipboard selection-notification show-directories show-hidden show-recent statusbar-basename statusbar-bg statusbar-fg statusbar-h-padding statusbar-home-tilde statusbar-page-percent statusbar-v-padding synctex synctex-editor-command vertical-center window-height window-icon window-icon-document window-title-basename window-title-home-tilde window-title-page window-width zoom-center zoom-max zoom-min zoom-step

highlight default link zathurarcNumber Number
highlight default link zathurarcString String
highlight default link zathurarcBoolean Boolean
" same as vim
highlight default link zathurarcCommand Statement
highlight default link zathurarcOption PreProc
" ex: nowrap
