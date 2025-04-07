" Handle plugins with Plug
call plug#begin('~/.vim/plugged')  " Start the plugin section

Plug 'lervag/vimtex'                      " Vim-LaTeX
Plug 'notmuch/notmuch'                    " Notmuch email client
Plug 'octol/vim-cpp-enhanced-highlight'   " C++ enhanced syntax highlighting
Plug 'sheerun/vim-polyglot'               " Language packs for Vim
Plug 'scrooloose/nerdcommenter'           " NERD Commenter
Plug 'tpope/vim-sensible'                 " Vim-Sensible
Plug 'ycm-core/YouCompleteMe'             " YouCompleteMe
" Plug 'wellle/context.vim'                 " Context

call plug#end()  " End the plugin section

syntax on          " Enable syntax highlighting
filetype plugin indent on " Enable filetype detection and plugins

" Rainbow parentheses
Plug 'frazrepo/vim-rainbow'
" YouCompleteMe
" Plug 'Valloric/YouCompleteMe'

" Always use system clipboard (requires +clipboard in vim --version)
set clipboard=unnamedplus

" YouCompleteMe options
" let g:ycm_global_ycm_extra_conf = '~/.vim/ycm_extra_conf.py'
let g:ycm_always_populate_location_list = 1 " allows jumping to error locations

" yankring options
Plug 'vim-scripts/yankring.vim'
let g:yankring_history_dir = '~/.vim/temp'

" nerdcommented
Plug 'scrooloose/nerdcommenter'
let g:NERDSpaceDelims = 1

call plug#end()

" Turn on filetype detection, filetype-specifi plugins/indentation
filetype plugin indent on

" Enable rainbow parens only for c/c++/Fortran files
au FileType c,cpp,fortran call rainbow#load()
" let g:rainbow_active=1
let g:rainbow_load_separately = [
    \ [ '*' , [['(', ')'], ['\[', '\]'], ['{', '}']] ],
    \ [ '*.tex' , [['(', ')'], ['\[', '\]']] ],
    \ [ '*.cpp' , [['(', ')'], ['\[', '\]'], ['{', '}'], ['<', '>']] ],
    \ [ '*.{html,htm}' , [['(', ')'], ['\[', '\]'], ['{', '}'], ['<\a[^>]*>', '</[^>]*>']] ],
    \ ]

" let g:rainbow_guifgs = ['RoyalBlue3', 'DarkOrange3', 'DarkOrchid3', 'FireBrick']
" let g:rainbow_ctermfgs = ['lightblue', 'lightgreen', 'yellow', 'red', 'magenta']


" make backspace and del keys work like most other apps
set backspace=2
:fixdel

" To enable 256 colors
set t_Co=256

" Set background
set background=light
highlight Normal ctermbg=256 ctermfg=46

" Turn on syntax highlight
syntax on

" Show relative line number
set relativenumber

" Turn off the bell
set visualbell

" Add <> to parens match highlight
:set matchpairs+=<:>

" Always display file name
set ls=2

" Highlight current window
hi StatusLine gui=bold ctermfg=Blue

" Highlight errors by underlining
hi SpellBad cterm=underline ctermfg=red ctermbg=NONE

" Customize status line
set statusline=%<%f\ %h%w%m%r%y%=Row:%l/%L\ (%p%%)\ Col:%c%V

" Tab and spacing
set tabstop=2 softtabstop=2 textwidth=120 shiftwidth=2 expandtab
highlight ExtraWhitespace ctermbg=darkgreen guibg=lightgreen

" No re-tab Makefiles
autocmd BufNewFile,BufRead Makefile* setlocal noexpandtab
autocmd BufNewFile,BufRead makefile* setlocal noexpandtab
autocmd BufNewFile,BufRead MAKEFILE* setlocal noexpandtab

" Automatic re-tab
" if has("autocmd")
    " autocmd BufReadPost * if &modifiable | retab | endif
" endif

" Line numbering
highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=NONE gui=NONE guifg=DarkGrey guibg=NONE
map <F6> :set number! <CR><Bar>:echo "Line Number: " . strpart("OffOn", 3 * &number, 3 )<CR>

" Check spelling English
if has("spell")
    map <F7> :set spell! spelllang=en_gb <CR><Bar>:echo "English Spell Check: " . strpart("OffOn", 3 * &spell, 3 )<CR>
endif

" Check spelling Italian
if has("spell")
    map <F8> :set spell! spelllang=it <CR><Bar>:echo "Italian Spell Check: " . strpart("OffOn", 3 * &spell, 3 )<CR>
endif

" Makes tilde file backups
set backup
if has('persistent_undo')
    "so is persistent undo ...
    set undofile
    "maximum number of changes that can be undone
    set undolevels=1000
    "maximum number lines to save for undo on a buffer reload
    set undoreload=10000
endif

" Match trailing white space, except when typing at the end of a line:
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$\| \t/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/

" Autoremove trailing white space on save
" autocmd BufWritePre * :%s/\s\+$//e

" Search highlight
set hlsearch

" No visual bell
set t_vb=

" Incremental search
set incsearch

" Search ignores case only if all small caps
set ignorecase
set smartcase

" Bash-like filename completion
set wildmode=longest:full
set wildmenu

" Disable autocomment in new lines
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Set some of the parameter for the viminfo: the maximum
" number of previous edited file, disable highlight when
" re-open a file and define the viminfo file.
set viminfo='50,h,n~/.viminfo

" Store a ton of history (default is 20)
set history=1000

" set vim to chdir for each file
if exists('+autochdir')
    set autochdir
else
    autocmd BufEnter * silent! lcd %:p:h:gs/ /\\ /
endif

" Tell vim to ignore certain files patterns in netrw
let g:netrw_list_hide= '.*\.swp$,^\./$'
let g:netrw_hide=1
let g:netrw_keepdir=0
let g:netrw_liststyle=0

" Backup files location
set backup                    " keep a backup file
set undodir=~/.vim/_undos     " store undo files here
set backupdir=~/.vim/_backups " store backups here
set directory=~/.vim/_swaps   " store swap files here

" Tab navigation
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" Tabline colors, to be coherent with the status line colors
hi TabLineFill ctermfg=White ctermbg=White
hi TabLine ctermfg=White ctermbg=Black term=none cterm=none
hi TabLineSel ctermfg=White ctermbg=Blue term=bold cterm=bold

" Set the default color scheme
colorscheme elflord

" Do not wrap text (i.e., break line if past textwidth)
set fo-=t

" Wait very little for combined commands
set timeoutlen=350

" Remove scratch preview window
set completeopt-=preview

" Remap some commands

" Normal mode
nnoremap ss :w<Enter>
nnoremap qa :qa<Enter>
nnoremap rr R
nnoremap wa :wa<Enter>
nnoremap sw cw
nnoremap QQ :q<Enter>
nnoremap <C-a> GVgg
nnoremap <C-o> :tabedit . <Enter>
nnoremap <C-z> u
nnoremap <C-t> :tabnew <Enter>
nnoremap TT :tabprevious <Enter>
nnoremap tt :tabnext <Enter>
nnoremap ln :lnext <Enter>
nnoremap lp :lprevious <Enter>
nnoremap E  $
" Apply YCM FixIt
nnoremap FF :YcmCompleter FixIt<CR>
nnoremap NRN :set norelativenumber <Enter>
nnoremap RN :set relativenumber <Enter>

" Visual mode
vnoremap qq <Esc>
vnoremap i I
vnoremap ginc :YcmCompleter GoToInclude <Enter>
vnoremap gdec :YcmCompleter GoToDeclaration <Enter>
vnoremap gdef :YcmCompleter GoToDefinition <Enter>
vnoremap gt   :YcmCompleter GetType <Enter>
vnoremap fix  :YcmCompleter FixIt <Enter>

" Insert mode
inoremap QQ <Esc>
inoremap <C-l> <Del>
inoremap <C-h> <BS>
" :inoremap <expr> <CR> pumvisible() ? "\<C-y><space>" : "\<C-g>u\<CR>"

" For TEX files only
augroup latex_mappings
    autocmd!
    autocmd FileType tex imap <buffer> <C-I> \begin{itemize}<CR>\item <CR>\end{itemize}<Esc> k A
    autocmd FileType tex imap <buffer> <C-F> \begin{frame}{title}<CR>\end{frame}<Esc> k A
augroup END
