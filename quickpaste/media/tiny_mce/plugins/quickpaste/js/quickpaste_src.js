(function ($) {
    $(document).ready(function() {
        $('#id_upload').uploadify({
        'auto': true,
        'fileDataName': 'upload',
            'uploader': _tinymce_url+'plugins/quickpaste/js/uploadify/uploadify.swf',
            'script': _quickpaste_url_upload,
            'cancelImg': _tinymce_url+'plugins/quickpaste/js/uploadify/cancel.png',
            'buttonImg': _tinymce_url+'plugins/quickpaste/img/button.png',
            'scriptData'  : {'session_key': _session_key},
            'onComplete': function(event, ID, fileObj, response, data) {
                QuickPasteDialog.insert(response);
            }
        });
    });
})(jQuery);
