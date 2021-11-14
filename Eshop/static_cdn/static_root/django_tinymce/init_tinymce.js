'use strict';

{
    function initTinyMCE(el) {
        if (el.closest('.empty-form') === null) {  // Don't do empty inlines
            var mce_conf = JSON.parse(el.dataset.mceConf);

            // There is no way to pass a JavaScript function as an option
            // because all options are serialized as JSON.
            const fns = [
                'color_picker_callback',
                'file_browser_callback',
                'file_picker_callback',
                'images_dataimg_filter',
                'images_upload_handler',
                'paste_postprocess',
                'paste_preprocess',
                'setup',
                'urlconverter_callback',
            ];
            fns.forEach((fn_name) => {
                if (typeof mce_conf[fn_name] != 'undefined') {
                    if (mce_conf[fn_name].includes('(')) {
                        mce_conf[fn_name] = eval('(' + mce_conf[fn_name] + ')');
                    } else {
                        mce_conf[fn_name] = window[mce_conf[fn_name]];
                    }
                }
            });

            const id = el.id;
            if ('elements' in mce_conf && mce_conf['mode'] == 'exact') {
                mce_conf['elements'] = id;
            }
            if (el.dataset.mceGzConf) {
                tinyMCE_GZ.init(JSON.parse(el.dataset.mceGzConf));
            }
            if (!tinyMCE.editors[id]) {
                tinyMCE.init(mce_conf);
            }
        }
    }

    // Call function fn when the DOM is loaded and ready. If it is already
    // loaded, call the function now.
    // http://youmightnotneedjquery.com/#ready
    function ready(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    ready(function () {
        // initialize the TinyMCE editors on load
        document.querySelectorAll('.tinymce').forEach(function (el) {
            initTinyMCE(el);
        });

        // initialize the TinyMCE editor after adding an inline in the django admin context.
        if (typeof (django) !== 'undefined' && typeof (django.jQuery) !== 'undefined') {
            django.jQuery(document).on('formset:added', function (event, $row, formsetName) {
                $row.find('textarea.tinymce').each(function () {
                    initTinyMCE(this);
                });
            });
        }
    });
}
tinymce.init({
  selector: 'textarea',
  height: 400,
  menubar: true,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks advcode fullscreen',
    'insertdatetime media table contextmenu powerpaste tinymcespellchecker a11ychecker linkchecker mediaembed',
    'wordcount'
  ],
  toolbar: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | advcode spellchecker  a11ycheck code',
  table_toolbar: "tableprops cellprops tabledelete | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol",
  powerpaste_allow_local_images: true,
  powerpaste_word_import: 'prompt',
  powerpaste_html_import: 'prompt',
  spellchecker_language: 'en',
  spellchecker_dialog: true,
  content_css: [
    '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
    '//www.tiny.cloud/css/codepen.min.css']
});


// var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
//
// tinymce.init({
//     selector: 'textarea#full-featured',
//     plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker imagetools textpattern noneditable help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable export',
//     tinydrive_token_provider: 'URL_TO_YOUR_TOKEN_PROVIDER',
//     tinydrive_dropbox_app_key: 'YOUR_DROPBOX_APP_KEY',
//     tinydrive_google_drive_key: 'YOUR_GOOGLE_DRIVE_KEY',
//     tinydrive_google_drive_client_id: 'YOUR_GOOGLE_DRIVE_CLIENT_ID',
//     mobile: {
//         plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker textpattern noneditable help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable'
//     },
//     menu: {
//         tc: {
//             title: 'Comments',
//             items: 'addcomment showcomments deleteallconversations'
//         }
//     },
//     menubar: 'file edit view insert format tools table tc help',
//     toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
//     autosave_ask_before_unload: true,
//     autosave_interval: '30s',
//     autosave_prefix: '{path}{query}-{id}-',
//     autosave_restore_when_empty: false,
//     autosave_retention: '2m',
//     image_advtab: true,
//     link_list: [
//         {title: 'My page 1', value: 'https://www.tiny.cloud'},
//         {title: 'My page 2', value: 'http://www.moxiecode.com'}
//     ],
//     image_list: [
//         {title: 'My page 1', value: 'https://www.tiny.cloud'},
//         {title: 'My page 2', value: 'http://www.moxiecode.com'}
//     ],
//     image_class_list: [
//         {title: 'None', value: ''},
//         {title: 'Some class', value: 'class-name'}
//     ],
//     importcss_append: true,
//     templates: [
//         {
//             title: 'New Table',
//             description: 'creates a new table',
//             content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>'
//         },
//         {title: 'Starting my story', description: 'A cure for writers block', content: 'Once upon a time...'},
//         {
//             title: 'New list with dates',
//             description: 'New List with dates',
//             content: '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>'
//         }
//     ],
//     template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
//     template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
//     height: 600,
//     image_caption: true,
//     quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
//     noneditable_noneditable_class: 'mceNonEditable',
//     toolbar_mode: 'sliding',
//     spellchecker_ignore_list: ['Ephox', 'Moxiecode'],
//     tinycomments_mode: 'embedded',
//     content_style: '.mymention{ color: gray; }',
//     contextmenu: 'link image imagetools table configurepermanentpen',
//     a11y_advanced_options: true,
//     skin: useDarkMode ? 'oxide-dark' : 'oxide',
//     content_css: useDarkMode ? 'dark' : 'default',
//     /*
//     The following settings require more configuration than shown here.
//     For information on configuring the mentions plugin, see:
//     https://www.tiny.cloud/docs/plugins/premium/mentions/.
//     */
//     mentions_selector: '.mymention',
//     mentions_fetch: mentions_fetch,
//     mentions_menu_hover: mentions_menu_hover,
//     mentions_menu_complete: mentions_menu_complete,
//     mentions_select: mentions_select,
//     mentions_item_type: 'profile'
// });
//

